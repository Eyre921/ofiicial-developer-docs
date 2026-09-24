---
title: "Harness Compatibility"
source: https://docs.fireworks.ai/nexus/harness-compatibility
path: nexus/harness-compatibility
---

Connect credentials for closed model families, understand harness support, and troubleshoot explicit model changes.

Start with [Coding Harnesses](/ecosystem/fireconnect/harnesses) for setup by client. This page covers explicit model changes, closed-model credentials, and Foundry support.

## Add an explicit model

Connecting a harness already registers coding-ready Fireworks models, including `auto`. Use `--model` only when you want an explicit model or router:

```bash wrap theme={null}
fireconnect claude --model glm-latest
```

Replace `claude` and `glm-latest` with the harness and model you want. On Claude Code, `--model` adds the model to `/model` without replacing native Anthropic tiers. After changing a model, follow the restart or reopen instructions in [Coding Harnesses](/ecosystem/fireconnect/harnesses).

For model IDs, aliases, fast tiers, pinned versions, image support, and US-only models, see [Open Models](/nexus/open-models).

## Connect credentials for closed model families

Your Fireworks key pays for the open-model leg. A closed model family also needs a credential for its provider.

<Tip>
  For a route containing Claude or another Anthropic model, connect an
  account-level Anthropic key in [Provider Keys](/nexus/provider-keys) when possible.
  Developers then need only their Fireworks API key, which `fireconnect login`
  configures for them. The table below shows harness-local alternatives and
  current FireConnect constraints.
</Tip>

| Harness                                    | Local alternative for an Anthropic route                                                        | Astra or another OpenAI route                       |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Claude Code                                | Existing Claude login, OAuth, or `ANTHROPIC_API_KEY`                                            | OpenAI key in [Provider Keys](/nexus/provider-keys) |
| OpenCode, Pi, VS Code                      | Local Anthropic key from `--anthropic-api-key`, `ANTHROPIC_API_KEY`, or `fireconnect configure` | OpenAI Provider Key                                 |
| Codex                                      | Local Anthropic key forwarded through an `ANTHROPIC_API_KEY` environment reference              | OpenAI Provider Key                                 |
| Cursor IDE                                 | Not supported because Cursor IDE cannot send the additional Anthropic header                    | OpenAI Provider Key                                 |
| Copilot App, Copilot CLI, DeepSeek Harness | Not yet configured by FireConnect                                                               | OpenAI Provider Key                                 |

FireConnect currently refuses routes that require Anthropic credentials on Cursor IDE, Copilot App, Copilot CLI, and DeepSeek Harness. For Cursor IDE, this is a client header limitation. For Copilot and DeepSeek, it is a FireConnect integration gap.

OpenAI models use an account-level OpenAI Provider Key. FireConnect does not have a local OpenAI-key flag. For direct HTTP calls, see [APIs and SDKs](/ecosystem/firerouter/apis-and-sdks#credentials).

To control the balance between predicted quality and cost, see [Routing Preferences](/nexus/routing-preferences).

## Foundry compatibility

On the Foundry path, pass the Azure deployment name, such as `FW-GLM-5.2`, instead of a short Fireworks ID.

Model routers are not available on the Foundry path. Claude Code, DeepSeek Harness, Copilot App, and Copilot CLI do not support Foundry.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Nothing changed after --model">
    Follow the restart or reopen instructions for your client in [Coding Harnesses](/ecosystem/fireconnect/harnesses).
  </Accordion>
</AccordionGroup>
