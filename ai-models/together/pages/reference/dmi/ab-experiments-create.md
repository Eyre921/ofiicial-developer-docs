---
title: "Create an A/B experiment"
source: https://docs.together.ai/reference/dmi/ab-experiments-create
path: reference/dmi/ab-experiments-create
---

POST /projects/{projectId}/endpoints/{endpointId}/abExperiments
Creates a managed control/variant split across two to 20 deployments under the same endpoint. Exactly one member is the control, member percentages must add up to 100, and the split applies only to traffic that the endpoint would otherwise send to the control.
