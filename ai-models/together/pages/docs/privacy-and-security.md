---
title: "Privacy and security"
source: https://docs.together.ai/docs/privacy-and-security
path: docs/privacy-and-security
---

How Together handles your inputs, outputs, and account data, plus enterprise options for data residency and private networking.

## What Together stores

Together does not store inputs or outputs by default, i.e. it supports zero data retention (ZDR). Temporary caching may be used to improve performance unless otherwise configured.

## Training opt-in

Data sharing for training other models is **opt-in and not enabled by default**. Check or change this setting in the **Privacy** section of [Organization Settings](https://api.together.ai/settings/organization/~current). See the [privacy policy](https://www.together.ai/privacy) for the full legal picture.

## Organization privacy settings

Organization-level privacy toggles live on the main [Organization Settings](https://api.together.ai/settings/organization/~current) page under **Privacy**. Only organization admins can change them:

* **Store prompts and model responses**: opt in to storing prompts and outputs for product improvements. Required before you can enable passthrough models.
* **Allow organization's data for training**: opt in to using your organization's data for training models released by Together AI and partners.
* **Allow passthrough models**: opt in to models that forward prompts and responses to third-party providers (see below).

If your organization is on the Limited tier, add a payment method before updating these settings.

## Account vs. organization settings

You may see a privacy toggle on both your personal account profile and your organization settings. These control different scopes:

* The **account** setting applies only to traffic you send under your personal account when it isn't attached to an organization.
* The **organization** setting governs all traffic sent under that organization's projects and API keys, regardless of which member makes the request.

When a request uses an organization's API key, the **organization setting is what applies**. To turn data sharing off for your team, change it in organization settings, not on your personal profile.

## Passthrough third-party models

Some models are offered as **passthrough**, meaning that Together forwards your prompts and responses directly to the upstream provider, and data is handled under that provider's own data policy. Passthrough is controlled by a separate organization-level toggle ("Allow my organization to use passthrough models…") and is independent of the training opt-in above. If you do not want any traffic leaving Together's infrastructure, leave that toggle off, and non-passthrough models will continue to work as normal.

## Enterprise data residency and private networking

For customers with data-residency, regulatory, or compliance requirements (for example, GDPR-driven EU-region deployments), Together supports private networking and VPC-based deployments, including in EU regions. Serverless endpoints do not offer region selection; use a [dedicated endpoint](/docs/dedicated-endpoints/overview) or [contact us](https://www.together.ai/contact) to discuss the right setup for your workload. For the full legal picture, see the [privacy policy](https://www.together.ai/privacy).

## Third-party model providers

Models published by third-party authors (DeepSeek, Qwen, Mistral, etc.) and hosted on Together run on Together's own infrastructure. They do not call out to the model author. The model author has no access to your requests or API calls.

For example, DeepSeek models are hosted in Together's secure North America data centers. DeepSeek itself receives no user requests or API traffic from this deployment.

Models on Together are hosted at full precision. Together does not distill them, force system prompts, or layer censorship on top. The version you call is the version the model author published.
