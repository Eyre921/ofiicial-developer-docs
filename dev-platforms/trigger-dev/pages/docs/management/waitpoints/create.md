---
title: "Create a waitpoint token"
source: https://trigger.dev/docs/management/waitpoints/create
path: docs/management/waitpoints/create
---

v3-openapi POST /api/v1/waitpoints/tokens
Creates a new waitpoint token that can be used to pause a run until an external event completes it. The token includes a `url` which can be called via HTTP POST to complete the waitpoint. Use the token ID with `wait.forToken()` inside a task to pause execution until the token is completed.
