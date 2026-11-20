---
title: "Enterprise Controls"
source: https://docs.fireworks.ai/nexus/enterprise-controls
path: nexus/enterprise-controls
---

Security and admin controls for Nexus Enterprise: Zero Data Retention, custom SSO, SCIM, roles, Model Providers, model access, data residency, Spend Limits, and audit logs.

| Control | What it gives you | Availability |
| :- | :- | :- |
| [Zero Data Retention](/nexus/data-security) | Nexus never stores prompts, responses, or traces | Every account |
| [Custom SSO](/accounts/sso) | Sign in through your OIDC or SAML identity provider, in the web app and in Nexus CLI | Enterprise |
| [SCIM provisioning](/accounts/sso#scim-provisioning) | Sync users and groups from Okta, Microsoft Entra ID, or Google Workspace | Enterprise |
| [Roles](#roles) | Keep members, Model Providers, and Spend Limits with account admins | Team and Enterprise |
| [Model Providers](/nexus/provider-keys) | Store Anthropic, OpenAI, or Amazon Bedrock credentials once for the whole team | Every plan |
| [Model access](#control-models-and-regions) | Choose which Fireworks open models people and Nexus Auto can use | Enterprise |
| [Data residency](#data-residency) | Keep Fireworks inference in the US. Closed-model calls follow the region you configured with that provider | Enterprise |
| [Spend Limits](/nexus/usage-limits) | Cap spend with an account default, group limits, and per-user overrides | Enterprise |
| [Audit & Access Logs](/guides/security_compliance/audit_logs) | Review account activity for investigations and compliance reporting | Enterprise |

To get Nexus Enterprise, [contact sales](https://fireworks.ai/contact). To compare plans, see [Plans and Accounts](/nexus/plans).

## Sign in with your identity provider

With [Custom SSO](/accounts/sso), people sign in to the Nexus app and to Nexus CLI through your identity provider. With [SCIM provisioning](/accounts/sso#scim-provisioning), people you remove in your directory lose access to Nexus.

> [!NOTE]
>
> SSO enforcement does not revoke API keys that already exist. When you remove someone's access, also review their API keys.

## Roles

Nexus has two roles:

* **Admin:** invites and removes members, changes roles, and manages Model Providers. On Enterprise, admins also manage Spend Limits.
* **Member:** uses Nexus with their own Nexus key.

Admins manage members on **Members** (Team) or **Settings → Users & Access** (Enterprise). On Enterprise, members can view that page but can't change it.

* **Member** is the platform `user` role. Nexus also shows `inference-user` as **Member**; people who join through SSO sign-up get that role when the identity provider sets no default role. The label changes only what the Nexus app shows, not the stored role or its permissions.
* Other platform roles, such as Contributor, keep their platform name and can't be chosen in the Nexus app.

## Keep provider credentials with admins

With [Model Providers](/nexus/provider-keys), an admin connects each closed-model provider once. Developers send only their Nexus key. Closed-model turns run on your own Anthropic, OpenAI, or Amazon Bedrock account, under your agreement with that provider.

For Amazon Bedrock, connect an [IAM role](/nexus/provider-keys/bedrock) instead of an API key, so Fireworks holds no long-lived AWS secret.

## Control models and regions

In the Nexus app, open **Settings → Governances**.

* **Model access** limits the account to the Fireworks open models you allow. Nexus Auto only picks from allowed models. The policy applies to everyone on the account and does not yet cover Anthropic or OpenAI models.
* **Data residency** keeps Fireworks inference in one region. See [Data residency](#data-residency).

- Governances uses the platform [Model Access Policy](/accounts/model-access-policy) and [Data Residency](/accounts/data-residency). In the Nexus app, enabling a model allows both standard and Fast serverless inference for it.
- Pro and Team accounts don't have the Governances page.
- There are no per-user or per-group model rules.

## Data residency

[Data residency](/accounts/data-residency) sets where Fireworks serves. For a model that runs on a third-party provider, Fireworks follows the region you have already configured with that provider.

| Call | Where it runs with residency on |
| :- | :- |
| A [US-only Fireworks model](/serverless/us-only-serverless#available-models) you named | [US-only Serverless](/serverless/us-only-serverless), through `us.api.fireworks.ai` |
| A [Nexus Auto](/nexus/auto) call routed to a Fireworks open model | US-only Serverless, through `us.api.fireworks.ai` |
| A call routed to Anthropic or OpenAI | Sent through `us.api.fireworks.ai`, then that provider, on your own account, in the region you configured with them |
| A call routed to Amazon Bedrock | Sent through `us.api.fireworks.ai`, then your own AWS account, on the route's own inference profile, from a US endpoint |

Three things to know before you turn it on:

* **US is the only region Nexus supports.** Set any other region and `auto` is rejected, along with Anthropic, OpenAI, and Amazon Bedrock models.
* **It covers every Fireworks model, not just `auto`.** A call naming an open model must use a [US-only model ID](/serverless/us-only-serverless#available-models), such as `glm-5p3-us`, on `us.api.fireworks.ai`. Other model IDs are rejected, and only `auto` is mapped to a US twin for you.
* **Closed-model calls follow your own provider setting.** Fireworks picks no region: Anthropic applies your workspace default, OpenAI is detected from your key's project host, and Amazon Bedrock uses each route's own inference profile from a US endpoint. See [Third-party providers](/accounts/data-residency#third-party-providers).

Admins set residency in the Nexus app at **Settings → Governances → Data Residency**.

* Residency is enforced at the API gateway, on the endpoint the request used, the ingress PoP, and the Fireworks route it resolved to. The endpoint and PoP checks apply to provider-key traffic too, since `externalBackendMiddleware` runs them before dispatch; only the resolved-route check has nothing to match. Bedrock's profile and region filtering happens in FireRouter's `bedrock_routes.within`, not at the gateway: a route outside the residency region is dropped, and a request that names its model returns `403` with error code `region_unavailable` (`reason_code: residency` is internal and not in the response). Your own `global.` profiles on a `us-*` endpoint are kept, except for an account Fireworks has set to pin provider calls to the US, and for a request that sends `inference_geo: "us"`, where naming that Bedrock model returns `400` `invalid_request`.
* Claude subscription and ChatGPT or Codex logins work under US residency. Both used to be refused, because the US region was forced onto the leg.
* OpenAI host detection applies to OpenAI API keys, client or Provider Key, on every account. It does not apply to a ChatGPT or Codex login, a deployment with its own endpoint, or an account Fireworks has set to pin provider calls to the US, whose calls go straight to `us.api.openai.com`. Any 401 other than `incorrect_hostname` is not resent.
* Through Nexus on the Messages API, a request whose own `inference_geo: "us"` rules out every model returns `400` `invalid_request`. When the account's residency rules it out, the request returns `403` `region_unavailable`. On Fireworks Serverless outside Nexus, `inference_geo` for a model with no deployment in that region returns `404`.
* While a region is set, the third-party model catalog API is denied: `ListThirdPartyModels` and `GetThirdPartyModel` (`GET /v1/accounts/*/thirdPartyModels`, `firectl third-party-model list`). The Model Providers page does not call it, so it keeps working.
* Zero Data Retention covers what Fireworks handles, whatever the residency setting. What a provider keeps on your own account follows your agreement and settings with them, and some models require retention to be enabled there. See [Data Security & Privacy](/nexus/data-security).

## Compliance

Fireworks holds SOC 2 Type II, ISO 27001, ISO 27701, and ISO 42001 certifications. Reports and the data processing agreement are in the [Trust Center](https://trust.fireworks.ai/).
