---
title: "Audit logs"
source: https://elevenlabs.io/docs/overview/administration/workspaces/audit-logs.md
path: docs/overview/administration/workspaces/audit-logs
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audit logs

## Overview

Audit logs provide a chronological record of administrative actions performed within your workspace, supporting security monitoring, compliance reporting, and incident investigation. Coverage spans over 100 endpoints across user provisioning, authentication, API key management, and other administrative surfaces.

Logs are emitted in the [OCSF v1.6.0](https://schema.ocsf.io/1.6.0) schema with the `datetime` and `host` profiles applied, so most entries can be ingested into a SIEM with minimal normalisation.

## Access requirements

Two independent checks gate retrieval:

| Requirement        | Detail           |
| ------------------ | ---------------- |
| Workspace tier     | Enterprise       |
| API key permission | `audit_log_read` |

Requests authenticate with a workspace API key. The user or service account associated with the key must hold the `audit_log_read` permission.

## Retrieving logs

Audit logs are returned by [`GET /v1/workspace/audit-logs`](/docs/api-reference/workspace/audit-logs/list). See the API reference for the full list of query parameters and pagination details.

#### Python

```python
from dotenv import load_dotenv
import os
from elevenlabs import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

page = elevenlabs.workspace.audit_logs.list(limit=50)
for entry in page.entries:
    print(entry.time_dt, entry.class_name, entry.activity_name)
```

#### TypeScript

```typescript
import 'dotenv/config';
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient({ apiKey: process.env.ELEVENLABS_API_KEY });

const page = await elevenlabs.workspace.auditLogs.list({ limit: 50 });
for (const entry of page.entries) {
  console.log(entry.timeDt, entry.className, entry.activityName);
}
```

### Rate limits

Requests are limited to 30 per minute per user. Combined with the maximum `limit` of 100, this allows up to 3,000 entries per minute.

## Schema

Audit logs follow the [OCSF v1.6.0](https://schema.ocsf.io/1.6.0) specification. Event-class-specific fields supplement a common base; see the API reference for the per-field response schema.

### Event classes

The following OCSF classes are emitted today:

| Class                  | UID    | Examples                                                         |
| ---------------------- | ------ | ---------------------------------------------------------------- |
| Account Change         | `3001` | User created, password changed, MFA factor enabled.              |
| Authentication         | `3002` | Logon, logoff, account switch.                                   |
| Entity Management      | `3004` | Resource created, updated, deleted, or moved.                    |
| User Access Management | `3005` | Privileges assigned or revoked.                                  |
| Group Management       | `3006` | Group created, user added or removed, subgroup added or removed. |

OCSF compliance is best-effort. Where a canonical OCSF field exists, audit entries use it; the `unmapped` field carries any ElevenLabs-specific attributes that don't fit the standard.

## Redaction

Sensitive material that would otherwise appear in URL paths or query parameters is redacted before audit entries are written. Password reset tokens are one such case; equivalent redaction applies to any audit-relevant request whose URL structure carries secrets.
