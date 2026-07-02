---
title: "Remediation create"
source: https://docs.together.ai/reference/remediation-create
path: reference/remediation-create
---

POST /compute/clusters/{cluster_id}/instances/{instance_id}/remediations
Creates a new remediation for an instance.

Remediations created via the API goes directly to PENDING state.

Our system may trigger automated remediations that require approval. These remediations are created with PENDING_APPROVAL state.
The user must call /approve to start the actual remediation process.
These operations can also be rejected by calling /reject.
