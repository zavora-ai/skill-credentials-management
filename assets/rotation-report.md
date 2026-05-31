# 🔑 Credential Rotation Report

**Generated:** {timestamp}
**Vault:** {vault_name}
**Policy:** {rotation_policy}

## Rotation Status

| Credential | Type | Last Rotated | Expires | Status |
|-----------|------|-------------|---------|--------|
| {cred_1} | {type_1} | {rotated_1} | {expires_1} | {status_1} |
| {cred_2} | {type_2} | {rotated_2} | {expires_2} | {status_2} |
| {cred_3} | {type_3} | {rotated_3} | {expires_3} | {status_3} |

## Summary

| Metric | Value |
|--------|-------|
| Total Credentials | {total_creds} |
| Rotated (on schedule) | {rotated_count} ✅ |
| Expiring Soon | {expiring_count} ⚠️ |
| Expired | {expired_count} ❌ |

## Actions Required

{action_items}

---
*Managed by {agent_name} • Next rotation: {next_rotation}*
