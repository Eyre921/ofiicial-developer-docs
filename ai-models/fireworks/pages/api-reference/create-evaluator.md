---
title: "Create Evaluator"
source: https://docs.fireworks.ai/api-reference/create-evaluator
path: api-reference/create-evaluator
---

post /v1/accounts/{account_id}/evaluatorsV2
Creates a custom evaluator for scoring model outputs. Evaluators use the
[Eval Protocol](https://evalprotocol.io) to define test cases, run model
inference, and score responses. They are used with evaluation jobs and
Reinforcement Fine-Tuning (RFT).

## Source Code Requirements

Your project should contain:
- `requirements.txt` - Python dependencies for your evaluator
- `test_*.py` - Pytest test file(s) with
  [`@evaluation_test`](https://evalprotocol.io/reference/evaluation-test)
  decorated functions
- Any additional code/modules your evaluator needs

## Workflow

**Recommended:** Use the [`ep upload`](https://evalprotocol.io/reference/cli#ep-upload)
CLI command to handle all these steps automatically.

If using the API directly:

1. Call this endpoint to create the evaluator resource
2. Package your source directory as a `.tar.gz` (respecting `.gitignore`)
3. Call [Get Evaluator Upload Endpoint](/api-reference/get-evaluator-upload-endpoint) to get a signed upload URL
4. `PUT` the tar.gz file to the signed URL
5. Call [Validate Evaluator Upload](/api-reference/validate-evaluator-upload) to trigger server-side validation
6. Poll [Get Evaluator](/api-reference/get-evaluator) until ready

Once active, reference the evaluator in [Create Evaluation Job](/api-reference/create-evaluation-job) or [Create Reinforcement Fine-tuning Job](/api-reference/create-reinforcement-fine-tuning-job).
