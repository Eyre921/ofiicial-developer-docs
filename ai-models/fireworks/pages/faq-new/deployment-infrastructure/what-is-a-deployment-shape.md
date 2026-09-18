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

Deployments created without a shape fail far more often than deployments created from a shape — they are the most common cause of failed deployment creations on Fireworks. Do not create deployments without a shape: pass `--deployment-shape` (or `deploymentShape` in the API), or `default` to have Fireworks pick one. Enforcement is coming soon — shapeless creation will then require an explicit opt-in ([`acceptShapelessRisk`](/guides/ondemand-deployments#explicitly-creating-a-deployment-without-a-shape-advanced-users-only)).

## How to find and use a shape

The shape list is also the authoritative way to discover which GPU types, GPU counts, and precisions a model supports — a hardware combination with no shape is not a validated configuration.

<Tabs>
  <Tab title="firectl">
    Match the shapes available for your model:

    ```bash theme={null}
    firectl deployment-shape-version match --model accounts/fireworks/models/gpt-oss-120b
    ```

    Then pass the shape's name to `--deployment-shape` when creating the deployment — or `--deployment-shape default` to have Fireworks pick one:

    ```bash theme={null}
    firectl deployment create accounts/fireworks/models/gpt-oss-120b \
      --deployment-shape default
    ```
  </Tab>

  <Tab title="REST API">
    Call [Match Deployment Shape Versions](/api-reference/match-deployment-shape-versions) with a deployment create request for your model — the same match the `firectl deployment-shape-version match` command runs. It returns the validated shape versions compatible with that model, applying the server-side compatibility rules for you — for LoRA addons and live-merge models, shapes are matched against the model's base model. To get shapes filtered for LoRA addon serving (`enableAddons`), include it in the request. The CLI command does not take addons into account:

    ```bash theme={null}
    # YOUR_ACCOUNT_ID is the account that will own the deployment, not the
    # model's publisher. The model in the body can live anywhere you can
    # deploy it, e.g. accounts/fireworks.
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

    Then pass one of the returned shape versions as `deploymentShape` in the [Create Deployment](/api-reference/create-deployment) request body. To have Fireworks pick a validated shape for you, pass `deploymentShape: "default"` instead — the server picks a compatible shape and applies it, and fails rather than override fields you set explicitly:

    ```bash theme={null}
    curl -X POST "https://api.fireworks.ai/v1/accounts/YOUR_ACCOUNT_ID/deployments" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "baseModel": "accounts/fireworks/models/gpt-oss-120b",
        "deploymentShape": "default"
      }'
    ```
  </Tab>

  <Tab title="Web UI">
    On the model page, choose **Deploy** and pick a shape.
  </Tab>
</Tabs>

## If no shape fits

If you need a configuration that no existing shape covers, [contact us](https://fireworks.ai/contact) — we'll help you find the right shape or add one for your workload.

If you deliberately need a configuration no shape covers, every surface accepts an [explicit opt-out](/guides/ondemand-deployments#explicitly-creating-a-deployment-without-a-shape-advanced-users-only) that creates the deployment without a shape.
