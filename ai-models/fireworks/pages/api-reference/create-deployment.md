---
title: "Create Deployment"
source: https://docs.fireworks.ai/api-reference/create-deployment
path: api-reference/create-deployment
---

post /v1/accounts/{account_id}/deployments

## Creating a deployment with a deployment shape

[Deployment shapes](/guides/ondemand-deployments#deployment-shapes) are pre-configured templates optimized for speed, cost, or efficiency. To create a deployment with a specific shape, pass the `deploymentShape` field in the request body along with `baseModel`.

Use the [Match Deployment Shape Versions](/api-reference/match-deployment-shape-versions) endpoint to find available shapes for your model: it takes a deployment create request and returns the validated shape versions compatible with that model, ready to pass as `deploymentShape`.

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

Shapes are validated, so the hardware, precision, and serving configuration are known to work together. Omitting `deploymentShape` — whether or not you set `acceleratorType`, `acceleratorCount`, or `precision` — creates the deployment without a shape. Deployments without a shape are the most common cause of failed deployment creations, and shapeless creation will soon require an explicit opt-in: always pass `deploymentShape`. See [What is a deployment shape?](/faq-new/deployment-infrastructure/what-is-a-deployment-shape) for how to find shapes for your model.

`deploymentShape` also accepts the special value `default`: the server picks a validated shape compatible with the model and your request, and the deployment is created from it. If every compatible shape conflicts with fields you set, or no shape is compatible with the model, the request fails with an error naming the conflicting fields and the compatible shapes — the pick never silently overrides your fields or falls back to a shapeless create.

Each model is validated only on the accelerator type, GPU count, and precision combinations covered by its shapes — many models support just one. Check [Match Deployment Shape Versions](/api-reference/match-deployment-shape-versions) before overriding `acceleratorType` or `acceleratorCount`: an unsupported combination typically fails at creation with a generic `Internal error occurred` message that does not name the hardware mismatch.

## Creating a deployment without a shape (advanced users only)

Pass the query parameter `acceptShapelessRisk=true` to explicitly create a deployment without a shape. It cannot be combined with `deploymentShape` — a deployment is either shaped or explicitly shapeless. Shape-specific fields like `acceleratorType`, `acceleratorCount`, and `precision` can still be set:

```bash theme={null}
curl -X POST "https://api.fireworks.ai/v1/accounts/YOUR_ACCOUNT_ID/deployments?acceptShapelessRisk=true" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "baseModel": "accounts/fireworks/models/gpt-oss-120b",
    "acceleratorType": "NVIDIA_H100_80GB",
    "acceleratorCount": 8,
    "precision": "FP8",
    "minReplicaCount": 1,
    "maxReplicaCount": 2
  }'
```

Deployments created this way skip shape validation and are far more likely to fail at creation. Enforcement is coming soon: shapeless creation will then require this flag, so use a shape (or `default`) now unless you deliberately need this path. If you need a configuration no shape covers, [contact us](https://fireworks.ai/contact) and we'll help you find or add one.
