---
title: "firectl deployment create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-create
path: tools-sdks/firectl/commands/deployment-create
---

Creates a new deployment.

```
firectl deployment create [flags]
```

### Examples

```
firectl deployment create falcon-7b
firectl deployment create accounts/fireworks/models/falcon-7b
firectl deployment create falcon-7b --file=/path/to/deployment-config.json
firectl deployment create falcon-7b --deployment-shape=falcon-7b-shape
```

### Flags

```
      --accelerator-count int32                  The number of accelerators to use per replica.
      --accelerator-type string                  The type of accelerator to use. Must be one of {NVIDIA_A100_80GB, NVIDIA_H100_80GB, NVIDIA_H200_141GB, NVIDIA_B200_180GB, NVIDIA_B300_288GB, AMD_MI325X_256GB, AMD_MI350X_288GB}
  -c, --cluster-id string                        The Fireworks cluster ID.
      --deployment-id string                     The ID of the deployment. If not specified, a random ID will be generated.
      --deployment-shape string                  The deployment shape to use for this deployment.
      --deployment-template string               The deployment template to use.
      --description string                       Description of the deployment.
      --direct-route-api-keys stringArray        The API keys for the direct route. Only available to enterprise accounts.
      --direct-route-type string                 If set, this deployment will expose an endpoint that bypasses our API gateway. Must be one of {INTERNET, GCP_PRIVATE_SERVICE_CONNECT, AWS_PRIVATELINK}. Only available to enterprise accounts.
      --disable-speculative-decoding             If true, speculative decoding is disabled.
      --display-name string                      Human-readable name of the deployment. Must be fewer than 64 characters long.
      --draft-model string                       The draft model to use for speculative decoding. If the model is under your account, you can specify the model ID. If the model is under another account, you can specify the full resource name (e.g. accounts/other-account/models/falcon-7b).
      --draft-token-count int32                  The number of tokens to generate per step for speculative decoding.
      --dry-run                                  Print the request proto without running it.
      --enable-addons                            If true, enable addons for this deployment.
      --enable-session-affinity                  If true, does sticky routing based on the 'user' field. Only available to enterprise accounts.
      --file string                              Path to a JSON configuration file containing deployment settings.
  -h, --help                                     help for create
      --load-targets Map                         Map of autoscaling load metric name# Data residency
Source: https://docs.fireworks.ai/accounts/data-residency

Restrict inference for your Enterprise account to a selected region

Data residency restricts inference on your account to a single region. Once a region is set, every request must use that region's API endpoint and a model served in that region.

It does not change how your requests are routed. Turning it on will not move existing traffic into the region. This setting *enforces* all requests to be in the set region, and rejects the ones that are not.

<Info>
  **Enterprise feature.** Data residency is available on Enterprise accounts. Contact your Fireworks representative if you need this enabled.
</Info>

<Info>
  Only account **Admins** can change data residency. Other roles can view the current setting but cannot change it.
</Info>

Residency applies **account-wide**: every API key on the account is restricted to the selected region.

## Available regional restrictions

| Regional restrictions | API endpoint                                  | Serverless                                           | Dedicated deployments                                                                |
| :-------------------- | :-------------------------------------------- | :--------------------------------------------------- | :----------------------------------------------------------------------------------- |
| None                  | <span><code>api.fireworks.ai</code></span>    | Any model                                            | Any region                                                                           |
| US                    | <span><code>us.api.fireworks.ai</code></span> | [US-only Serverless](/serverless/us-only-serverless) | [`US` multi-region](/deployments/regions), or a single US region such as `US_IOWA_1` |

**None** is the default. For a region that is not listed, contact [sales](https://fireworks.ai/company/contact-us).

## Before you switch it on

A residency change takes effect as soon as you save it, and anything that does not match the region is rejected.

### Serverless

Point your clients at the region's API endpoint and change every request to use a model from that region. See [US-only Serverless](/serverless/us-only-serverless) for the US endpoint and model IDs.

<Warning>
  **`inference_geo` is deprecated** in favor of data residency. As you switch over, remove the `inference_geo` field from your request bodies and the `Fireworks-Inference-Geo` header from your requests.
</Warning>

### Dedicated deployments

Every dedicated deployment must run in the selected region. Create it with `--region` set to that region, or to a single region inside it. See [Regions](/deployments/regions).

Check what you already have before you save the setting:

```bash theme={null}
firectl deployment list
```

* **New deployments outside the region are rejected** when you create them.
* **Existing deployments are not checked, moved, or stopped** when you switch the setting on. One outside the region keeps running and keeps costing you money, but requests to it are rejected. Replace it first.
* **You can move a deployment to another region inside your residency region, but not out of it.**

## Configure in the console

Account admins can set data residency in the Fireworks console at **Settings → Governances → Data Residency** ([open in console](https://app.fireworks.ai/settings/governances/region-access)).

Select the region and save. The console asks you to confirm that your clients already use the endpoint and models shown for that region.

## Configure with firectl

Set the region:

```bash theme={null}
firectl policy residency set US
```

Inspect the current setting:

```bash theme={null}
firectl policy residency get
```

Remove the restriction and return the account to unrestricted serving:

```bash theme={null}
firectl policy residency clear
```

## Pricing

Regional models are priced at a premium over the base serverless price for the same model. See [Serverless pricing](/serverless/pricing).

## Limitations

The following are not supported while a region is set: calls are rejected, and stay rejected until you clear the setting.

* **Training.** Fine-tuning and training jobs are blocked. Support is coming soon.
* **FireRouter.** [FireRouter](/ecosystem/firerouter/overview) can pass a request through to a third-party provider, which Fireworks cannot constrain to a region.
* **BYOC.** [BYOC](/ecosystem/integrations/byoc/overview) deployments run in your own cloud account, so Fireworks cannot enforce where they run.

## Related

* [US-only Serverless](/serverless/us-only-serverless) — endpoint and model IDs for the US region
* [Enterprise features](/accounts/enterprise-features) — overview of Enterprise administration capabilities
* [Managing users](/accounts/users) — account roles and permissions
* [Data Security](/guides/security_compliance/data_security) — encryption, retention, and access controls
