---
title: "Effort"
source: https://docs.fireworks.ai/nexus/orchestration-preferences
path: nexus/orchestration-preferences
---

Set effort in your coding harness. Nexus Auto uses that when it picks a model.

Higher effort asks for a more thorough attempt. Lower effort asks for a lighter one.

## Claude Code

In [Claude Code](/nexus/harnesses/claude-code), open `/model`. Effort appears under the model list, for example **High effort**. Use the left and right arrow keys to change it, then press Enter to save it as the default, or press `s` to apply it to this session only.

## Codex and the ChatGPT desktop app

Open the model picker and choose the effort. In the [Codex](/nexus/harnesses/codex) CLI, that is `/model`, titled **Select Model and Effort**. The ChatGPT desktop app reads the same Codex config, so the effort applies to both.

## Other harnesses

Use the harness's own effort control where it has one. Nexus CLI does not set effort.

* The old `--routing-preference` flag has no effect.
