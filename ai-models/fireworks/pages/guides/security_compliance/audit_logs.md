---
title: "Audit & Access Logs"
source: https://docs.fireworks.ai/guides/security_compliance/audit_logs
path: guides/security_compliance/audit_logs
---

Monitor and track account activities with audit logging for Enterprise accounts

Audit logs are available for Enterprise accounts. This feature enhances security visibility, incident investigation, and compliance reporting.

Audit logs include data access logs. All read, write, and delete operations on storage are logged, normalized, and enriched with account context for complete visibility.

## View audit logs

You can view audit logs, including data access logs, using the Fireworks CLI:

```bash theme={null}
firectl ls audit-logs
```

<Frame>
  <img alt="Audit logs table showing data access activities with columns for timestamp, principal, response code, resource path, and message" />
</Frame>
