---
title: "Privacy and security"
source: https://docs.together.ai/docs/privacy-and-security
path: docs/privacy-and-security
---

How Together handles your inputs, outputs, and account data, plus enterprise options for data residency and private networking.

## What Together stores

Together does not store inputs or outputs by default, i.e. it supports zero data retention (ZDR). Temporary caching may be used to improve performance unless otherwise configured.

## Training opt-in

Data sharing for training other models is **opt-in and not enabled by default**. Check or change this setting under **Privacy & Security** at [api.together.ai/settings/profile](https://api.together.ai/settings/profile). See the [privacy policy](https://www.together.ai/privacy) for the full legal picture.

### Account vs. organization settings

You may see a privacy toggle on both your personal account profile and your organization settings. These control different scopes:

* The **account** setting only applies to traffic you send under your personal account when it's not attached to an organization.
* The **organization** setting governs all traffic made under that organization's projects and API keys, regardless of which member sends the request.

When a request is made with an organization's API key, the **organization setting is what applies**. To turn data sharing off for your team, change it in the organization's settings (not just on your personal profile).

## Passthrough third-party models

Some models are offered as **passthrough**, meaning that Together forwards your prompts and responses directly to the upstream provider, and data is handled under that provider's own data policy. Passthrough is controlled by a separate organization-level toggle ("Allow my organization to use passthrough models…") and is independent of the training opt-in above. If you do not want any traffic leaving Together's infrastructure, leave that toggle off, and non-passthrough models will continue to work as normal.

## Enterprise data residency and private networking

For customers with data-residency, regulatory, or compliance requirements, Together supports private networking and VPC-based deployments. [Contact us](https://www.together.ai/contact) to discuss the right setup for your workload.

## Third-party model providers

Models published by third-party authors (DeepSeek, Qwen, Mistral, etc.) and hosted on Together run on Together's own infrastructure. They do not call out to the model author. The model author has no access to your requests or API calls.

For example, DeepSeek models are hosted in Together's secure North America data centers; DeepSeek itself receives no user requests or API traffic from this deployment.

Models on Together are hosted at full precision. Together does not distill them, force system prompts, or layer censorship on top. The version you call is the version the model author published.
