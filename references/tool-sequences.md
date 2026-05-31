# Credentials Management Tool Sequences (8 tools)

## Discovery (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_credentials` | List available credentials (names only) | read |
| `get_credential_metadata` | Get metadata: scope, TTL, last rotated | read |

## Access (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `request_runtime_secret` | Request secret value for runtime use | **sensitive** |
| `request_workload_token` | Request scoped workload token | **sensitive** |

## Lifecycle (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `rotate_credential` | Generate new credential value | **production** |
| `revoke_credential` | Immediately revoke a credential | **destructive** |

## Audit (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `audit_credential_access` | View access log for a credential | read |
| `validate_secret_scope` | Check if scope is sufficient for action | read |

## Sequence: Scoped Secret Request (3 calls)
```
1. list_credentials(namespace: "production") → [{name: "STRIPE_API_KEY", scope: "payments"}, {name: "DB_PASSWORD", scope: "database"}]
2. validate_secret_scope(credential: "STRIPE_API_KEY", required_scope: "payments:charge") → {valid: true, granted_scopes: ["payments:*"]}
3. request_runtime_secret(credential: "STRIPE_API_KEY", purpose: "process refund", ttl: 300) → {token_ref: "tok-xxx", expires_in: 300}
```

## Sequence: Emergency Rotation (3 calls)
```
1. audit_credential_access(credential: "DB_PASSWORD") → {recent: [{actor: "unknown-ip", time: "5min ago", action: "read"}]}
2. revoke_credential(credential: "DB_PASSWORD", reason: "suspicious access detected") → {revoked: true, effective: "immediate"}
3. rotate_credential(credential: "DB_PASSWORD", notify: ["ops-team"]) → {rotated: true, new_version: 4, notified: ["ops-team"]}
```

## Sequence: Workload Token for CI (3 calls)
```
1. get_credential_metadata(credential: "CI_DEPLOY_TOKEN") → {scope: "deploy:staging", ttl: 3600, last_rotated: "2026-05-28"}
2. validate_secret_scope(credential: "CI_DEPLOY_TOKEN", required_scope: "deploy:staging") → {valid: true}
3. request_workload_token(credential: "CI_DEPLOY_TOKEN", workload: "pipeline-92", ttl: 600) → {token_ref: "wt-ci-92", expires_in: 600}
```
