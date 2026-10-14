---
title: "Replay run"
source: https://trigger.dev/docs/management/runs/replay
path: docs/management/runs/replay
---

v3-openapi POST /api/v1/runs/{runId}/replay
Creates a new run with the same payload and options as the original run, in the same environment. Send a body to override the payload, metadata, or trigger options for the new run. The body is optional; an empty body replays the run unchanged.
