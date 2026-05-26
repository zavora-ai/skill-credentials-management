# Credentials Cross-MCP Workflows

## Credentials + Registry: Server Authentication
```
REGISTRY: inspect_server(id: "mcp_crm") → {credentials: ["vault://hubspot-token"]}
CREDENTIALS: validate_secret_scope(secret: "hubspot-token", requester: "agent_1") → allowed
CREDENTIALS: request_runtime_secret(name: "hubspot-token", purpose: "CRM sync") → {token: "***", ttl: 3600}
```

## Credentials + Identity: Rotation on Compromise
```
IDENTITY: emergency_revoke(user_id: "compromised_user")
CREDENTIALS: rotate_credential(name: "api-key-prod", reason: "User compromise detected")
CREDENTIALS: audit_credential_access(name: "api-key-prod", last_24h: true) → access log
SLACK: send_message(channel: "#security", text: "🔑 Credential rotated: api-key-prod. Triggered by user compromise.")
```
