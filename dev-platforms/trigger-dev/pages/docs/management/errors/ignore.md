---
title: "Ignore an error"
source: https://trigger.dev/docs/management/errors/ignore
path: docs/management/errors/ignore
---

v3-openapi POST /api/v1/errors/{errorId}/ignore
Mark an error group as ignored. Provide a `duration` to ignore it for a fixed window, and/or thresholds that re-surface the error when exceeded. Send a JSON body (use `{}` to ignore indefinitely).
