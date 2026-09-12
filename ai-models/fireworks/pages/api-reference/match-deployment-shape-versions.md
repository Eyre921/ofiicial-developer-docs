---
title: "Match Deployment Shape Versions"
source: https://docs.fireworks.ai/api-reference/match-deployment-shape-versions
path: api-reference/match-deployment-shape-versions
---

post /v1/accounts/{account_id}/deploymentShapeVersions:match
Returns the deployment shape versions compatible with the provided deployment create request. Use this to discover a validated shape before creating a deployment with `deployment_shape` set - shapeless deployments (raw accelerator type/count) skip validated-configuration checks and are far more likely to fail at creation.

Use this endpoint to discover the deployment shape versions compatible with a model before creating a deployment. Pass a [Create Deployment](/api-reference/create-deployment) request in the body — at minimum `createDeploymentRequest.deployment.baseModel` — and the response returns the latest validated shape versions that can serve that model, ready to pass as `deploymentShape`.

Match applies the full server-side compatibility logic for you: PEFT base-model resolution (for LoRA addons and live merge, shapes are matched against the PEFT base model), model-type and parameter-count tiers, embedding vs. non-embedding models, the MULTI\_LORA capability gate when `enableAddons` is set, and hiding of FP4 shapes for full-parameter fine-tunes. [List Deployment Shape Versions](/api-reference/list-deployment-shape-versions) only lists versions of a shape you already know and cannot answer "which shapes work with this model?" — use Match for that.

<Note>
  The account in the URL must be **your own account** — the account that will own the deployment (you must be a member of it, so `accounts/fireworks` fails with a permission error). The model in the request body, however, can live in any account you can deploy from, including publisher accounts like `accounts/fireworks`; public shapes from the publisher's account flow into the results.
</Note>

## Example: Match shapes for a model

```bash theme={null}
curl -X POST "https://api.fireworks.ai/v1/accounts/YOUR_ACCOUNT_ID/deploymentShapeVersions:match" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "createDeploymentRequest": {
      "deployment": {
        "baseModel": "accounts/fireworks/models/gpt-oss-120b"
      }
    }
  }'
```

To match shapes for a deployment with LoRA addons enabled, include `enableAddons` in the request — only shapes with the MULTI\_LORA capability are returned:

```bash theme={null}
curl -X POST "https://api.fireworks.ai/v1/accounts/YOUR_ACCOUNT_ID/deploymentShapeVersions:match" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "createDeploymentRequest": {
      "deployment": {
        "baseModel": "accounts/fireworks/models/gpt-oss-120b",
        "enableAddons": true
      }
    }
  }'
```

Then pass one of the returned shape versions as `deploymentShape` in the [Create Deployment](/api-reference/create-deployment) request. See [What is a deployment shape?](/faq-new/deployment-infrastructure/what-is-a-deployment-shape) for why you should always create deployments from a shape.
