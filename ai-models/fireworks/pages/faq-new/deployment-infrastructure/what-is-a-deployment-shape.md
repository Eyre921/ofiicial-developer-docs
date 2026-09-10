---
title: "What is a deployment shape, and why did my deployment fail to create?"
source: https://docs.fireworks.ai/faq-new/deployment-infrastructure/what-is-a-deployment-shape
path: faq-new/deployment-infrastructure/what-is-a-deployment-shape
---

A **deployment shape** is a pre-validated, pre-configured deployment template. It bundles a known-good combination of GPU type and count, precision, and serving parameters, optimized for speed (`fast`), cost per token at scale (`throughput`), or lowest cost (`minimal`). A deployment created from a shape starts from a configuration that is known to work for that model.

## Why deployments created without a shape often fail

If you create a deployment without a shape — that is, without passing `--deployment-shape` (or `deploymentShape` in the API) — the configuration is not validated ahead of time. Mistakes only surface at creation, where they cause failures. Common examples:

* A GPU count that cannot fit the model in memory
* An accelerator type the model isn't validated on (for example, requesting H200 for a model whose shapes are all B200)
* A context length the configuration can't serve
* A quantization or precision the model doesn't support on that hardware

Deployments created without a shape fail far more often than deployments created from a shape — they are the most common cause of failed deployment creations on Fireworks. Do not create deployments without a shape; the unshaped path may be deprecated in the future.

## How to find and use a shape

The shape list is also the authoritative way to discover which GPU types, GPU counts, and precisions a model supports — a hardware combination with no shape is not a validated configuration.

<Tabs>
  <Tab title="firectl">
    List the shapes available for your model:

    ```bash theme={null}
    firectl deployment-shape-version list --base-model accounts/fireworks/models/gpt-oss-120b
    ```

    Then pass the shape's name to `--deployment-shape` when creating the deployment:

    ```bash theme={null}
    firectl deployment create accounts/fireworks/models/gpt-oss-120b \
      --deployment-shape accounts/fireworks/deploymentShapes/gpt-oss-120b-fast
    ```
  </Tab>

  <Tab title="REST API">
    Call [List Deployment Shape Versions](/api-reference/list-deployment-shape-versions) to find shapes for your model, then pass the shape name as `deploymentShape` in the [Create Deployment](/api-reference/create-deployment) request body:

    ```bash theme={null}
    curl -X POST "https://api.fireworks.ai/v1/accounts/YOUR_ACCOUNT_ID/deployments" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "baseModel": "accounts/fireworks/models/gpt-oss-120b",
        "deploymentShape": "accounts/fireworks/deploymentShapes/gpt-oss-120b-fast"
      }'
    ```
  </Tab>

  <Tab title="Web UI">
    On the model page, choose **Deploy** and pick a shape.
  </Tab>
</Tabs>

## If no shape fits

If you need a configuration that no existing shape covers, [contact us](https://fireworks.ai/contact) — we'll help you find the right shape or add one for your workload.
