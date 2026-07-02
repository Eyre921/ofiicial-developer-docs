---
title: "Close session"
source: https://trigger.dev/docs/management/sessions/close
path: docs/management/sessions/close
---

v3-openapi POST /api/v1/sessions/{session}/close
Close a session. Closing is terminal and idempotent — closing an already-closed session returns the existing row unchanged. A closed session cannot be reopened, and reusing its `externalId` on create returns `409`.

Requires a secret key — a session public token cannot close a session.
