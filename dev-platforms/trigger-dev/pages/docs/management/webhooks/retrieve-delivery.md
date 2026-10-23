---
title: "Retrieve a webhook delivery"
source: https://trigger.dev/docs/management/webhooks/retrieve-delivery
path: docs/management/webhooks/retrieve-delivery
---

v3-openapi GET /api/v1/webhooks/deliveries/{deliveryId}
Retrieve one delivery: its status and error, the event body and headers it carried, and a `targets` entry per subscriber with the run or session it started or why its filter skipped the event. When the delivery resumed waiting runs, one more entry summarizes them.
