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
| [Roles](/accounts/users) | Keep Model Providers and Spend Limits with account admins | Every plan |
| [Model Providers](/nexus/provider-keys) | Store Anthropic, OpenAI, or Amazon Bedrock credentials once for the whole team | Every plan |
| [Model access](#control-models-and-regions) | Choose which Fireworks open models people and Nexus Auto can use | Enterprise |
| [Data residency](#control-models-and-regions) | Keep inference in one region, such as the US | Enterprise |
| [Spend Limits](/nexus/usage-limits) | Cap spend with an account default, group limits, and per-user overrides | Enterprise |
| [Audit & Access Logs](/guides/security_compliance/audit_logs) | Review account activity for investigations and compliance reporting | Enterprise |

To get Nexus Enterprise, [contact sales](https://fireworks.ai/contact). To compare plans, see [Plans and Accounts](/nexus/plans).

## Sign in with your identity provider

With [Custom SSO](/accounts/sso), people sign in to the Nexus app and to Nexus CLI through your identity provider. With [SCIM provisioning](/accounts/sso#scim-provisioning), people you remove in your directory lose access to Nexus.

> [!NOTE]
>
> SSO enforcement does not revoke API keys that already exist. When you remove someone's access, also review their API keys.

## Keep provider credentials with admins

With [Model Providers](/nexus/provider-keys), an admin connects each closed-model provider once. Developers send only their Nexus key. Closed-model turns run on your own Anthropic, OpenAI, or Amazon Bedrock account, under your agreement with that provider.

For Amazon Bedrock, connect an [IAM role](/nexus/provider-keys/bedrock) instead of an API key, so Fireworks holds no long-lived AWS secret.

## Control models and regions

In the Nexus app, open **Settings → Governances**.

* **Model access** limits the account to the Fireworks open models you allow. Nexus Auto only picks from allowed models. The policy applies to everyone on the account and does not yet cover Anthropic or OpenAI models.
* **Data residency** keeps inference in one region. With US residency, Nexus Auto runs open-model turns on US-only Serverless through `us.api.fireworks.ai`. Other regions can't use Nexus Auto.

- Governances uses the platform [Model Access Policy](/accounts/model-access-policy) and [Data Residency](/accounts/data-residency). In the Nexus app, enabling a model allows both standard and Fast serverless inference for it.
- Pro and Team accounts don't have the Governances page.
- There are no per-user or per-group model rules.

## Compliance

Fireworks holds SOC 2 Type II, ISO 27001, ISO 27701, and ISO 42001 certifications. Reports and the data processing agreement are in the [Trust Center](https://trust.fireworks.ai/).
