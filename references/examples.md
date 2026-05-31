# Credentials Management Examples

## Example 1: "I need the Stripe API key to process a refund"
```
validate_secret_scope(credential: "STRIPE_API_KEY", required_scope: "payments:refund") → {valid: true, granted_scopes: ["payments:*"]}
request_runtime_secret(credential: "STRIPE_API_KEY", purpose: "process refund for order-5521", ttl: 120) → {token_ref: "tok-rf5521", expires_in: 120}
```
Response: "🔑 Credential issued (ref: tok-rf5521). Scope validated for payments:refund. Expires in 2 minutes. Value not displayed — use token_ref in your runtime call."

## Example 2: "The database password may be compromised — rotate it now"
```
audit_credential_access(credential: "PROD_DB_PASSWORD") → {total_accesses: 47, recent: [{actor: "10.0.0.99", time: "3min ago", action: "read", context: "unknown"}, {actor: "deploy-bot", time: "1hr ago", action: "read", context: "deploy"}]}
revoke_credential(credential: "PROD_DB_PASSWORD", reason: "unrecognized access from 10.0.0.99") → {revoked: true, effective: "immediate"}
rotate_credential(credential: "PROD_DB_PASSWORD", notify: ["dba-team", "security"]) → {rotated: true, new_version: 7, notified: ["dba-team", "security"]}
```
Response: "🚨 Emergency rotation complete:\n1. Suspicious access detected from 10.0.0.99 (3min ago)\n2. Old credential revoked immediately\n3. New credential generated (version 7)\n4. Notified: dba-team, security\n\nAll services using PROD_DB_PASSWORD will need to re-authenticate."

## Example 3: "What credentials are available for the staging environment?"
```
list_credentials(namespace: "staging") → [{name: "STAGING_DB_URL", scope: "database", last_rotated: "2026-05-25"}, {name: "STAGING_REDIS_PASSWORD", scope: "cache", last_rotated: "2026-05-20"}, {name: "STAGING_API_TOKEN", scope: "api:read", last_rotated: "2026-05-29"}]
get_credential_metadata(credential: "STAGING_DB_URL") → {scope: "database", ttl: 86400, last_rotated: "2026-05-25", rotation_policy: "every 7 days", expires: "2026-06-01"}
```
Response: "Staging credentials (3 available):\n| Name | Scope | Last Rotated | Status |\n|------|-------|-------------|--------|\n| STAGING_DB_URL | database | May 25 | ⚠️ Due for rotation Jun 1 |\n| STAGING_REDIS_PASSWORD | cache | May 20 | ✅ OK |\n| STAGING_API_TOKEN | api:read | May 29 | ✅ OK |"
