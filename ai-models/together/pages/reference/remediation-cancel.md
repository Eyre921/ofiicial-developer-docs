---
title: "Remediation cancel"
source: https://docs.together.ai/reference/remediation-cancel
path: reference/remediation-cancel
---

POST /compute/clusters/{cluster_id}/instances/{instance_id}/remediations/{remediation_id}/cancel
Cancels a pending remediation.

Only remediations in PENDING_APPROVAL or PENDING state can be cancelled.
