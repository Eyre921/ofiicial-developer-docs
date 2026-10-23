---
title: "Effort"
source: https://docs.fireworks.ai/nexus/orchestration-preferences
path: nexus/orchestration-preferences
---

Set effort in your coding harness. Nexus Auto uses that when it picks a model.

Set effort in the harness you already use. Nexus Auto reads it when it picks a model for the turn. Higher effort asks for a more thorough attempt. Lower effort asks for a lighter one.

## Claude Code

Open `/model`. Effort appears under the model list, for example **High effort**. Press the left and right arrow keys to change it. Enter saves it as the default. `s` applies it to this session only.

## Codex and the ChatGPT desktop app

Open the model picker. In the Codex CLI, that is `/model`, titled **Select Model and Effort**. Choose the effort there. The ChatGPT desktop app reads the same Codex config, so the effort applies to both.

## Other harnesses

Use the harness's own effort control where it has one. Nexus CLI does not set effort for you. The old `--routing-preference` flag has no effect.

## Related

* [Nexus Auto](/nexus/auto): how `auto` picks a model for each turn
* [Claude Code](/nexus/harnesses/claude-code)
* [Codex](/nexus/harnesses/codex)
