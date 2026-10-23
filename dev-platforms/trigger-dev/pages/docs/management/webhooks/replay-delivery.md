---
title: "Replay a webhook delivery"
source: https://trigger.dev/docs/management/webhooks/replay-delivery
path: docs/management/webhooks/replay-delivery
---

v3-openapi POST /api/v1/webhooks/deliveries/{deliveryId}/replay
Route a delivery's stored event again as a new delivery. Without `targetId` every current subscriber is checked against its filter again. With `targetId` the event goes to that one subscriber, even if its filter skipped it. A replay never resumes waiting runs. Replays start real runs, so the key needs permission to trigger every task the replay runs, and to write sessions if it reaches an agent's subscriber.
