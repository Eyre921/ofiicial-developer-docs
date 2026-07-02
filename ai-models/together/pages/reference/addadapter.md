---
title: "Add a LoRA adapter to an endpoint"
source: https://docs.together.ai/reference/addadapter
path: reference/addadapter
---

POST /endpoints/{endpointId}/adapters
Adds a LoRA adapter model to a dedicated endpoint. After this call,
inference requests to the adapter model name will be routed to the
specified endpoint. The endpoint must have LoRA enabled, and the
adapter's base model must be compatible with the endpoint's model.
The endpoint name prefix in model_id must match the resolved endpoint.
