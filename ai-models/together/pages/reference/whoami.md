---
title: "Get API key identity"
source: https://docs.together.ai/reference/whoami
path: reference/whoami
---

GET /whoami
Returns identity information about the authenticated API key. Useful for confirming which project and organization a key is scoped to, and for obtaining the project slug used to compose the `model` value (`<project_slug>/<endpoint_slug>`) in dedicated endpoint inference calls.
Requires a Bearer API key in the `Authorization` header. Cookie, session, and SLS JWT credentials are not accepted.
