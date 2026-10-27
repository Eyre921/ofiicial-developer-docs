---
title: "LLM Cascading"
source: https://elevenlabs.io/docs/eleven-agents/customization/llm/llm-cascading.md
path: docs/eleven-agents/customization/llm/llm-cascading
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# LLM Cascading

## Overview

Agents Platform employs an LLM cascading mechanism to enhance the reliability and resilience of its text generation capabilities. This system automatically attempts to use backup Large Language Models (LLMs) if the primary configured LLM fails, ensuring a smoother and more consistent user experience.

Failures can include API errors, timeouts, or empty responses from the LLM provider. The cascade logic handles these situations gracefully.

## How it Works

The cascading process follows a defined sequence:

1. **Preferred LLM Attempt:** The system first attempts to generate a response using the LLM selected in the agent's configuration.

2. **Backup LLM Sequence:** If the preferred LLM fails, the system automatically falls back to a predefined sequence of backup LLMs. This sequence is curated based on model performance, speed, and reliability. The current default sequence (subject to change) is:

   1. Gemini 2.5 Flash
   2. GPT-4o
   3. Gemini 2.5 Flash Lite
   4. Claude Sonnet 4.5

3. **HIPAA Compliance:** If the agent operates in a mode requiring strict data privacy (HIPAA compliance / zero data retention), the backup list is filtered to include only compliant models from the sequence above.

4. **Retries:** The system retries the generation process multiple times (at least 3 attempts) across the sequence of available LLMs (preferred + backups). If a backup LLM also fails, it proceeds to the next one in the sequence. If it runs out of unique backup LLMs within the retry limit, it may retry previously failed backup models.

5. **Lazy Initialization:** Backup LLM connections are initialized only when needed, optimizing resource usage.

> **Info**
>
> The specific list and order of backup LLMs are managed internally by ElevenLabs and optimized for
> performance and availability. The sequence listed above represents the current default but may be
> updated without notice.

## Custom LLMs

When you configure a [Custom LLM](/docs/eleven-agents/customization/llm/custom-llm) as your primary model, the standard cascading logic to ElevenLabs-hosted models is bypassed by default. The system attempts to use your Custom LLM and, if it fails, retries the request with the *same* Custom LLM multiple times (matching the standard minimum retry count) before considering the request failed.

This default keeps all traffic on your own endpoint, but it means a sustained failure of your Custom LLM ends the conversation. To keep conversations running when your Custom LLM is unavailable, configure a custom backup cascade that falls back to other models.

### Configuring a custom backup cascade

A custom backup cascade works the same way when a Custom LLM is primary as it does for any other model. Set the agent's backup LLM preference to `override` and provide an `order` array listing the ElevenLabs-hosted models to fall back to, in sequence. See the `backup_llm_config` field on the [Create agent](/docs/api-reference/agents/create) and [Update agent](/docs/api-reference/agents/update) endpoints for the exact shape.

> **Tip**
>
> You can also configure this in the ElevenLabs dashboard under **Backup LLM configuration** by
> selecting **Custom** and arranging the fallback models. See
> [Models](/docs/eleven-agents/customization/llm#backup-llm-configuration) for the available
> options.

The cascade follows the same retry and timeout behavior described above: each model in the order is tried in turn, and the system makes at least 3 attempts across the sequence (primary plus backups) before considering the request failed. Set `cascade_timeout_seconds` (2–15 seconds, default 4) to control how long the system waits on a single model before moving to the next.

> **Note**
>
> A Custom LLM can only be used as the primary model — it cannot be listed in the backup `order`.
> Backup entries must be ElevenLabs-hosted models.

> **Warning**
>
> When your Custom LLM is primary and `backup_llm_config` is set to `default` or `disabled`, the
> system does not fall back to ElevenLabs-hosted models — a sustained failure of your Custom LLM
> ends the conversation with no backup. Use `override` to enable fallback. Only set `disabled` if
> you intentionally want no fallback (strongly discouraged for production).

On an agent using a [Realtime model](/docs/eleven-agents/customization/realtime-models), the agent falls back to a backup LLM if the Realtime model doesn't respond in time. The Realtime model sets how long the agent waits.

## Benefits

* **Increased Reliability:** Reduces the impact of temporary issues with a specific LLM provider.
* **Higher Availability:** Increases the likelihood of successfully generating a response even during partial LLM outages.
* **Seamless Operation:** The fallback mechanism is automatic and transparent to the end-user.

## Configuration

LLM cascading is an automatic background process. By default, the only configuration required is selecting your **Preferred LLM** in the agent's settings, and the system handles the rest.

To customize the fallback behavior — including when using a Custom LLM as primary — set the agent's **Backup LLM configuration** to **Default**, **Custom**, or **Disabled** (see [Custom LLMs](#custom-llms) above).
