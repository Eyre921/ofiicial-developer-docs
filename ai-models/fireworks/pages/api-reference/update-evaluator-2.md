---
title: "Update Evaluator"
source: https://docs.fireworks.ai/api-reference/update-evaluator
path: api-reference/update-evaluator
---

patch /v1/accounts/{account_id}/evaluators/{evaluator_id}
Updates evaluator metadata (display_name, description, default_dataset).
Changing `requirements` or `entry_point` triggers a rebuild. To upload new
source code, set `prepare_code_upload: true` then follow the upload flow.
