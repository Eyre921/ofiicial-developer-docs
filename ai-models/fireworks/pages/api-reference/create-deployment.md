---
title: "Create Deployment"
source: https://docs.fireworks.ai/api-reference/create-deployment
path: api-reference/create-deployment
---

post /v1/accounts/{account_id}/deployments

## Creating a deployment with a deployment shape

[Deployment shapes](/guides/ondemand-deployments#deployment-shapes) are pre-configured templates optimized for speed, cost, or efficiency. To create a deployment with a specific shape, pass the `deploymentShape` field in the request body along with `baseModel`.

Use the [List Deployment Shape Versions](/api-reference/list-deployment-shape-versions) endpoint to find available shapes for your model.

```bash theme={null}
curl -X POST "https://api.fireworks.ai/v1/accounts/YOUR_ACCOUNT_ID/deployments" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "baseModel": "accounts/fireworks/models/gpt-oss-120b",
    "deploymentShape": "accounts/fireworks/deploymentShapes/gpt-oss-120b-minimal",
    "minReplicaCount": 0,
    "maxReplicaCount": 1
  }'
```

<Note>
  When using a deployment shape, you do not need to specify `activeModelVersion` or `targetModelVersion` — the shape provides the necessary configuration.
</Note>

## Always pass `deploymentShape`

Shapes are validated, so the hardware, precision, and serving configuration are known to work together. Omitting `deploymentShape` — whether or not you set `acceleratorType`, `acceleratorCount`, or `precision` — creates the deployment without a shape. Deployments without a shape are the most common cause of failed deployment creations, and the unshaped path may be deprecated in the future: always pass `deploymentShape`. See [What is a deployment shape?](/faq-new/deployment-infrastructure/what-is-a-deployment-shape) for how to find shapes for your model.

Each model is validated only on the accelerator type, GPU count, and precision combinations covered by its shapes — many models support just one. Check [List Deployment Shape Versions](/api-reference/list-deployment-shape-versions) before overriding `acceleratorType` or `acceleratorCount`: an unsupported combination typically fails at creation with a generic `Internal error occurred` message that does not name the hardware mismatch.
