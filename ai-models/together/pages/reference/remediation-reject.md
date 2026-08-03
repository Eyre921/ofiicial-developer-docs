---
title: "Remediation reject"
source: https://docs.together.ai/reference/remediation-reject
path: reference/remediation-reject
---

openapi.yaml POST /compute/clusters/{cluster_id}/instances/{instance_id}/remediations/{remediation_id}/reject
Rejects a pending remediation.

Only remediations with state PENDING_APPROVAL can be rejected.

On REJECT: state changes to CANCELLED.
The reviewed_by, review_time, and review_comment fields are populated
on the remediation after rejection.
