---
title: "Execute code"
source: https://docs.together.ai/reference/tci-execute
path: reference/tci-execute
---

openapi.yaml POST /tci/execute
Executes the given code snippet and returns the output. Without a session_id, a new session is created to run the code. If you pass a valid session_id, the code runs in that session. This is useful for running multiple code snippets in the same environment, because dependencies and similar things are persisted
between calls to the same session.
