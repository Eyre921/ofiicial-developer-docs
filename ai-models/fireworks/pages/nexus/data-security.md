---
title: "Data Security & Privacy"
source: https://docs.fireworks.ai/nexus/data-security
path: nexus/data-security
---

Nexus is Zero Data Retention on every account. It never stores prompts, responses, or traces.

## Zero Data Retention on every account

Nexus is Zero Data Retention (ZDR) on every account and every plan: Pro, Team, and Enterprise.

* Nexus does not store prompts, responses, code, or tool calls.
* Nexus never keeps traces.
* Nexus keeps [service metadata](#service-metadata) to provide the routing service and de-identifies it after 30 days.

| Data | What Nexus does with it |
| :- | :- |
| **Prompts, responses, and tool calls** | Processed to serve each turn. Never stored |
| **Traces** | Never kept |
| **Service metadata** | Kept to run Nexus services, including Nexus Auto, and show your usage. De-identified after 30 days |

## Service metadata

Service metadata is information about each request, not its content. Nexus uses it to choose a model for each turn, check the quality of those choices, and show your usage and cost. It includes:

* Account ID and request time
* Token counts and billing
* Harness and Nexus CLI version
* Request shape, such as message size and whether it includes code or images
* The model that served each turn
* Routing quality scores

Service metadata does not include prompts, responses, system prompts, or the content or results of tool calls.

## Where your requests go

* **Open models** run on Fireworks under the same [Zero Data Retention](/guides/security_compliance/data_handling) policy.
* **Subprocessors.** Fireworks may send data to its [registered subprocessors](https://trust.fireworks.ai/subprocessors) to serve a request. These subprocessors are held to Zero Data Retention as well.
* **Your own provider accounts.** When Nexus Auto sends a turn to Anthropic, OpenAI, or Amazon Bedrock on your own account, that provider's data policies apply. The same is true for MCP servers you connect.

## How Nexus protects your data

* **Your key stays on your machine.** `nexus login` saves your Nexus key in the OS keychain, or in an encrypted file when no keychain is available.
* **Provider credentials stay with admins.** [Model Providers](/nexus/provider-keys) are encrypted at rest and never returned in full, so developers never handle them.
* **Platform security.** Fireworks encrypts data in transit and at rest, and holds SOC 2 Type II, ISO 27001, ISO 27701, and ISO 42001 certifications. Reports are available in the [Trust Center](https://trust.fireworks.ai/).

## Download or delete your data

To download or delete any data Fireworks holds about you, email [privacy@fireworks.ai](mailto:privacy@fireworks.ai).

For SSO, roles, and other admin settings, see [Enterprise Controls](/nexus/enterprise-controls).
