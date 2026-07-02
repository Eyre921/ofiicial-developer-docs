---
title: "Smart formatting"
source: https://developers.deepgram.com/docs/self-hosted-smart-formatting.md
path: docs/self-hosted-smart-formatting
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Smart formatting

[Smart Format](https://developers.deepgram.com/docs/smart-format) applies automatic formatting to transcripts to improve human readability. In a self-hosted deployment, smart formatting behavior depends on the model type, language, TOML file configuration, and which models are present on the deployment.

## Model and language support overview

| Model       | Language     | Formatted models available | NER formatting supported            | Smart formatting result                                                                           |
| ----------- | ------------ | -------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------- |
| Nova-3      | English      | No                         | Yes (required)                      | NER formatting via the entity-detector model                                                      |
| Nova-3      | Multilingual | No                         | Yes (required for English segments) | NER formatting for English-detected segments; punctuation and paragraphs for non-English segments |
| Nova-2      | English      | Yes                        | Yes (optional)                      | Formatted model alone, or non-formatted model + NER formatting                                    |
| Nova-3      | Non-English  | No                         | No                                  | Punctuation and paragraphs only                                                                   |
| Nova-2      | Non-English  | No                         | No                                  | Punctuation and paragraphs only                                                                   |
| Flux        | Any          | No                         | No                                  | Non-formatted transcripts only                                                                    |

## Nova-3 English

Nova-3 is only comprised of non-formatted models. To produce smart-formatted transcripts, you must deploy the **entity-detector** model alongside your Nova-3 model. The entity-detector model provides NER (named entity recognition) formatting, which detects and formats entities such as dates, times, currency amounts, phone numbers, emails, and URLs.

## Nova-3 multilingual

When processing multilingual audio, Nova-3 applies formatting based on the detected language of each transcript segment:

* **English-detected segments**: NER formatting is applied (requires the entity-detector model).
* **Non-English-detected segments**: Punctuation and paragraphs are applied.

This means a single multilingual stream can produce both NER-formatted English segments and punctuation-only non-English segments, depending on the language detected in each portion of the audio.

## Nova-2 English

Nova-2 provides both formatted and non-formatted English models. You can achieve smart formatting in either of two ways:

* **Formatted model**: Deploy a Nova-2 formatted model. The model produces smart-formatted output directly without any additional components.
* **Non-formatted model + NER formatting**: Deploy a Nova-2 non-formatted model alongside the entity-detector model. NER formatting applies entity detection on top of the base transcript.

NER formatting is optional for Nova-2 English because the formatted model already includes entity formatting. Choose whichever approach best fits your deployment constraints. NER is recommended for highest-quality formatting.

## Non-English languages (Nova-3 and Nova-2)

For non-English languages, Deepgram applies punctuation and paragraphs when smart formatting is enabled. Neither formatted models nor NER formatting applies to non-English transcription. This is the same behavior for both Nova-3 and Nova-2.

## Flux

Flux does not support smart formatting. Flux transcripts are always returned without formatting, regardless of whether `smart_format=true` is set in the request. The entity-detector model is not compatible with Flux.

See [Deploy Flux Model (STT)](/docs/flux-self-hosted) for Flux deployment details.

## Configure NER formatting in a self-hosted deployment

Enabling NER formatting requires the entity-detector model files and configuration changes in your TOML files. For full details, see [How can I enable NER formatting in my self-hosted deployment?](https://deepgram.gitbook.io/help-center/self-hosted/how-can-i-enable-ner-formatting-in-my-self-hosted-deployment).

### 1. Add the entity-detector model files

Add the appropriate entity-detector model files to your Engine's `models` directory. Your Deepgram account representative can provide these files.

* **Streaming**: Add the streaming entity-detector model (e.g. `entity-detector.en.streaming.********.dg`) and non-formatted streaming transcription models.
* **Pre-recorded (batch)**: Add the batch entity-detector model (e.g. `entity-detector.batch.********.dg`) and non-formatted batch transcription models.

### 2. Enable NER feature flags

For **streaming** STT, add the following to `engine.toml`:

```toml engine.toml
[features]
streaming_ner = true
```

For **pre-recorded (batch)** STT, add the following to `api.toml`:

```toml api.toml
[features]
format_entity_tags = true
```

You can enable both flags if your deployments handle both streaming and batch requests. There is no downside to enabling NER on both batch and streaming when a deployment only handles one or the other. It is expected that each deployment serves one mode of STT, not both.

### 3. Restart your containers

Restart your containers so that the configuration changes and new models take effect:

```shell
# Docker
sudo docker compose restart

# Or start if containers are stopped
sudo docker compose up -d
```

Contact your Deepgram account representative if you need assistance obtaining the entity-detector model files or verifying that NER formatting is active in your deployment.

## NER compatibility by model type

When NER formatting is enabled (`streaming_ner = true` and/or `format_entity_tags = true`), not all model types are compatible. NER formatting operates on non-formatted model output only. The following table shows which combinations produce valid smart-formatted results.

| Model       | Model type                          | NER enabled | Smart formatting result                                      |
| ----------- | ----------------------------------- | ----------- | ------------------------------------------------------------ |
| Nova-3      | Non-formatted (only type available) | Yes         | Smart-formatted transcript                                   |
| Nova-2      | Non-formatted                       | Yes         | Smart-formatted transcript                                   |
| Nova-2      | Formatted                           | Yes         | **Not compatible** — NER requires non-formatted model output |
| Nova-2      | Formatted                           | No          | Smart-formatted transcript (formatting built into model)     |

If you enable NER formatting and deploy Nova-2 **formatted** models, smart formatting requests will raise 400 Bad Request errors, since no model exists to serve the requests. NER formatting expects non-formatted model output as input. When using NER, replace any Nova-2 formatted models with their non-formatted equivalents.

## Further reading

* [Smart Format (Deepgram API docs)](https://developers.deepgram.com/docs/smart-format) — full reference for the smart formatting feature, including supported formatters and API usage.
* [How can I enable NER formatting in my self-hosted deployment?](https://deepgram.gitbook.io/help-center/self-hosted/how-can-i-enable-ner-formatting-in-my-self-hosted-deployment) — step-by-step NER enablement guide.
* [Deploy STT Services](/docs/deploy-stt-services) — guide for deploying speech-to-text services in a self-hosted environment.
* [System Maintenance](/docs/maintaining) — model selection and maintenance for self-hosted deployments.
