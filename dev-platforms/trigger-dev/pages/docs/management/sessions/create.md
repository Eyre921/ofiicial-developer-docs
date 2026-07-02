---
title: "Create session"
source: https://trigger.dev/docs/management/sessions/create
path: docs/management/sessions/create
---

v3-openapi POST /api/v1/sessions
Create a Session and trigger its first run in one atomic call. A Session is the durable identity for a bi-directional stream of records (the `.in` and `.out` channels) that survives across the runs processing it.

Idempotent on `externalId` within an environment. Calling create again with an `externalId` that already maps to an open session returns the existing session with `isCached: true` and `201` becomes `200`. Reusing an `externalId` whose session is already closed or expired returns `409`.

Authorize with a secret key, or a public token carrying `write:sessions` for the session you are creating.
