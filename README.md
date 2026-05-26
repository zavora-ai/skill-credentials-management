# Credentials Management Skill

> Secure credential operations — request runtime secrets with scope validation, rotate keys on schedule, revoke on compromise, and audit all access.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Request Secret | 1-2 | Scope check → deliver with TTL |
| Rotate | 1 | Generate new → verify → retire old |
| Revoke | 1 | Immediate invalidation |
| Audit | 1 | Access log by credential/time |

### Without this skill:
- Secrets cached beyond expiry
- No rotation schedule (keys used forever)
- Credential values logged in plain text
- No audit trail of who accessed what

### With this skill:
- TTL enforced (no stale secrets)
- Rotation on schedule + on compromise
- NEVER logs credential values
- Full audit trail with accessor + purpose

## Installation

```bash
git clone https://github.com/zavora-ai/skill-credentials-management.git \
  ~/.skills/skills/credentials-management
```

## Requirements

**Required:** `mcp-credentials-vault (8 tools)`

**Cross-MCP:** mcp-registry (server auth), mcp-identity (rotation on compromise)

## Folder Structure

```
credentials-management/
├── SKILL.md                       # Decision tree + workflows + MUST DO/MUST NOT DO
├── scripts/
│   └── rotation_check.py
├── references/
│   ├── tool-sequences.md
│   ├── cross-mcp-workflows.md
│   └── examples.md
├── README.md
└── LICENSE
```

## Example

**User:** "Which credentials need rotation?"

**Result:**
```
2 credentials overdue:
- api-key-prod: 95 days old (max 90) — OVERDUE
- hubspot-token: 88 days old (max 90) — due in 2 days
```

## Scripts

### `rotation_check.py`
```bash
python scripts/rotation_check.py '[{"name": "api-key", "last_rotated": "2025-01-01", "max_age_days": 90}]'
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
