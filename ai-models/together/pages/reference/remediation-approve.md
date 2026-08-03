---
title: "Remediation approve"
source: https://docs.together.ai/reference/remediation-approve
path: reference/remediation-approve
---

openapi.yaml POST /compute/clusters/{cluster_id}/instances/{instance_id}/remediations/{remediation_id}/approve
Approves a pending remediation.

Only remediations with state PENDING_APPROVAL can be approved.

On APPROVE: state changes to PENDING and the remediation process begins.
The reviewed_by, review_time, and review_comment fields are populated
on the remediation after approval.
