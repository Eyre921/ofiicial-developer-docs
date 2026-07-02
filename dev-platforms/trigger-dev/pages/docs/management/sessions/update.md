---
title: "Update session"
source: https://trigger.dev/docs/management/sessions/update
path: docs/management/sessions/update
---

v3-openapi PATCH /api/v1/sessions/{session}
Update a session's `tags` or `metadata`. Pass `metadata: null` to clear it.

Requires a secret key — a session public token cannot update a session. `externalId` is read-only after create: it cannot be changed or cleared. Sending a value different from the current one (including `null` when one is set) returns `422`; sending the same value is accepted as a no-op.
