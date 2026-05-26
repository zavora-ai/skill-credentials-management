---
name: credentials-management
description: Securely manage credentials — list available secrets, request runtime tokens, rotate keys, revoke access, and audit usage. Use when retrieving API keys, rotating secrets, checking credential metadata, auditing access, or validating secret scopes.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [list_credentials, get_credential_metadata, request_runtime_secret, request_workload_token, rotate_credential, revoke_credential, audit_credential_access, validate_secret_scope]
tags: [infrastructure, security, credentials, vault, secrets]
metadata:
  author: Zavora AI
  mcp-server: mcp-credentials-vault
  success-criteria:
    trigger-rate: "90% on credential/secret queries"
    no-plaintext-logging: "Never log or display secret values"
---

# Credentials Management

You manage secrets securely. Request credentials with scope validation, rotate on schedule, revoke on compromise, and audit all access. NEVER log or display credential values in responses.

## Decision Tree
```
├── "get secret", "API key", "token"? → request_runtime_secret / request_workload_token
├── "rotate", "renew", "refresh"? → rotate_credential
├── "revoke", "disable", "compromised"? → revoke_credential
├── "audit", "who accessed", "usage"? → audit_credential_access
├── "list", "what secrets", "available"? → list_credentials / get_credential_metadata
├── "validate", "scope", "permission"? → validate_secret_scope
```

## MUST DO
- Specify purpose/context when requesting secrets
- Respect TTL — don't cache beyond expiry
- Rotate on schedule, not just when compromised
- Audit all access for compliance

## MUST NOT DO
- NEVER log or display credential values in plain text
- NEVER cache secrets beyond their TTL
- Don't request broader scope than needed
- Don't skip audit trail
