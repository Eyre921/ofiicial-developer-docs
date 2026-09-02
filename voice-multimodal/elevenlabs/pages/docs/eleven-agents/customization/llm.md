---
title: "Models"
source: https://elevenlabs.io/docs/eleven-agents/customization/llm.md
path: docs/eleven-agents/customization/llm
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Models

ElevenAgents provides a unified interface to connect your agent to multiple models and providers, offering flexibility, reliability, and cost optimization.

## Key features

* **Unified access**: Switch between providers and models with minimal code changes
* **High reliability**: Automatically cascade from one provider to another if one fails
* **Spend monitoring**: Monitor your spending across different models

## Supported models

Currently, the following models are natively supported and can be configured via the agent settings:

| Provider       | Model                  |
| -------------- | ---------------------- |
| **ElevenLabs** | Qwen3.6-35B-A3B        |
|                | Qwen3.5-397B-A17B      |
| **Google**     | Gemini 3.7 Flash       |
|                | Gemini 3.6 Flash       |
|                | Gemini 3.5 Flash       |
|                | Gemini 3.5 Flash-Lite  |
|                | Gemini 3.1 Pro Preview |
|                | Gemini 3.1 Flash Lite  |
|                | Gemini 3 Flash Preview |
|                | Gemini 2.5 Flash       |
|                | Gemini 2.5 Flash Lite  |
| **OpenAI**     | GPT-5.6 Sol            |
|                | GPT-5.6 Terra          |
|                | GPT-5.6 Luna           |
|                | GPT-5.5                |
|                | GPT-5.4                |
|                | GPT-5.4 Mini           |
|                | GPT-5.4 Nano           |
|                | GPT-5.2                |
|                | GPT-5.1                |
|                | GPT-5                  |
|                | GPT-5 Mini             |
|                | GPT-5 Nano             |
|                | GPT-4.1                |
|                | GPT-4.1 Mini           |
|                | GPT-4.1 Nano           |
|                | GPT-4o                 |
|                | GPT-4o Mini            |
| **Anthropic**  | Claude Opus 4.8        |
|                | Claude Opus 4.7        |
|                | Claude Sonnet 5        |
|                | Claude Sonnet 4.6      |
|                | Claude Sonnet 4.5      |
|                | Claude Haiku 4.5       |

Pricing is typically denoted in USD per 1 million tokens unless specified otherwise. A token is a
fundamental unit of text data for LLMs, roughly equivalent to 4 characters on average.

### Custom LLM

Using your own custom LLM is supported by specifying the endpoint we should make requests to and providing credentials through our secure secret storage. Learn more about [custom LLM integration](/docs/eleven-agents/customization/llm/custom-llm).

With EU data residency enabled, a small number of older Gemini and Claude LLMs are not available
in ElevenLabs Agents to maintain compliance with EU data residency. Custom LLMs and OpenAI LLMs
remain fully available. For more information please see [GDPR and data residency](/docs/overview/administration/data-residency).

## Choosing a model

Selecting the most suitable LLM for your application involves considering several factors:

* **Task complexity**: More demanding or nuanced tasks generally benefit from more powerful models (for example, OpenAI's GPT-5.6 / GPT-5.5 series, Anthropic's Claude Opus and Claude Sonnet 5, or Google's Gemini Pro models)
* **Latency requirements**: For live voice conversations and other real-time applications, [ElevenLabs-hosted models](#models-hosted-by-elevenlabs) typically have the lowest latency. Google's Gemini Flash series, Anthropic's Claude Haiku, and OpenAI Mini and Nano models are also optimized for speed.
* **Context window size**: If your application needs to process, understand, or recall information from long conversations or extensive documents, select models with larger context windows
* **Cost-effectiveness**: Balance the desired performance and features against your budget. LLM prices can vary significantly, so analyze the pricing structure (input, output, and cache tokens) in relation to your expected usage patterns
* **HIPAA compliance**: If your application involves Protected Health Information (PHI), it is crucial to use an LLM that is designated as HIPAA compliant and ensure your entire data handling process meets regulatory standards

The maximum system prompt size is 2MB, which includes your agent's instructions, knowledge base
content, and other system-level context.

## Model configuration

### Temperature

Temperature controls the randomness of model responses. Lower values produce more consistent, focused outputs while higher values increase creativity and variation.

* **Low (0.0-0.3)**: Deterministic, consistent responses for structured interactions
* **Medium (0.4-0.7)**: Balanced creativity and consistency
* **High (0.8-1.0)**: Creative, varied responses for dynamic conversations

### Backup LLM configuration

Configure backup LLMs to ensure conversation continuity when the primary LLM fails or becomes unavailable.

**Configuration options:**

* **Default**: Uses ElevenLabs' recommended fallback sequence
* **Custom**: Define your own cascading sequence of backup models
* **Disabled**: No fallback (strongly discouraged for production)

Disabling backup LLMs means conversations will end abruptly if your primary LLM fails or becomes
unavailable. This is strongly discouraged for production use.

Learn more about [LLM cascading](/docs/eleven-agents/customization/llm/llm-cascading).

### Thinking budget

Control how many internal reasoning tokens the model can use before responding. More tokens improve answer quality but slow down response time.

**Options:**

* **Disabled**: Fastest replies with no internal reasoning overhead
* **Low**: Minimal reasoning for quick responses
* **Medium**: Balanced reasoning and speed
* **High**: Maximum reasoning for complex queries

### Reasoning effort

Some models support configurable reasoning effort. Higher effort can improve answer quality but increases latency.

**For conversational use-cases:**

Keep reasoning effort as low as the model allows to avoid the agent thinking too long, which can disrupt natural conversation flow.

**For workflow steps:**

Higher reasoning effort is useful for workflow steps that require complex thought or decision-making where response time is less critical.

### Reasoning summary

Reasoning summary stores a summary of the model's reasoning on the conversation transcript, so you can review why the agent responded or called a tool the way it did. Messages that involved reasoning show a **Reasoning** badge in the conversation history; select it to expand the summary.

Enable the **Reasoning summary** toggle (off by default) in the agent's LLM settings, or set `enable_reasoning_summary` via the API.

#### Custom LLMs

Reasoning summary works with custom LLMs that return reasoning in a supported OpenAI-compatible format. ElevenLabs stores the reasoning returned by your endpoint; it does not generate a summary from the model's final answer.

| API type             | Supported reasoning format                                                                                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chat Completions API | Stream reasoning in the `reasoning` or `reasoning_content` field of each response delta. For Gemini-compatible endpoints, ElevenLabs requests thoughts with `google.thinking_config.include_thoughts` and reads content marked with `extra_content.google.thought`. |
| Responses API        | Return a `reasoning` output item with summary text in its `summary` field. When reasoning effort is configured, ElevenLabs requests an automatic summary by setting `reasoning.summary` to `auto`.                                                                  |

Reasoning content is excluded from the agent's spoken response and stored with the corresponding transcript item. If the custom LLM does not return reasoning in one of these formats, the transcript does not include a reasoning summary for that turn.

**Limitations:**

* Summaries only appear for turns where the model actually reasoned (see [Reasoning effort](#reasoning-effort)). The setting stores the summary; it does not change how the model reasons.
* Some providers respond faster when no summary is requested, so test the latency impact before enabling it on latency-sensitive voice agents.
* Providers decide whether to return a summary, so some reasoned turns will have none. ElevenLabs-hosted models return the full reasoning trace.
* Summaries are part of the stored transcript: they are not streamed during the conversation, follow retention and PII redaction settings, and are unavailable with [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm).

Summaries are also returned in the `reasoning` field of each transcript item in the [Get conversation](/docs/api-reference/conversations/get) response.

## Understanding pricing

* **Tokens**: LLM usage is typically billed based on the number of tokens processed. As a general guideline for English text, 100 tokens is approximately equivalent to 75 words
* **Input vs. output pricing**: Providers often differentiate pricing for input tokens (the data you send to the model) and output tokens (the data the model generates in response)
* **Cache pricing**:
  * `input_cache_read`: This refers to the cost associated with retrieving previously processed input data from a cache. Utilizing cached data can lead to cost savings if identical inputs are processed multiple times
  * `input_cache_write`: This is the cost associated with storing input data into a cache. Some LLM providers may charge for this operation
* The prices listed in this document are per 1 million tokens and are based on the information available at the time of writing. These prices are subject to change by the LLM providers

For the most accurate and current information on model capabilities, pricing, and terms of service, always consult the official documentation from the respective LLM providers (OpenAI, Google, Anthropic).

## HIPAA compliance

Certain LLMs available on our platform may be suitable for use in environments requiring HIPAA compliance, please see the [HIPAA compliance docs](/docs/eleven-agents/legal/hipaa) for more details.

## Related resources

* [Custom LLM integration](/docs/eleven-agents/customization/llm/custom-llm)
* [LLM cascading](/docs/eleven-agents/customization/llm/llm-cascading)
* [Optimizing costs](/docs/eleven-agents/customization/llm/optimizing-costs)

## Models Hosted by ElevenLabs

ElevenLabs offers access to a variety of AI models, including select third-party models that are hosted by ElevenLabs.

When a model is designated as “Hosted by ElevenLabs”, the model is deployed and operated on infrastructure managed by ElevenLabs. These models are currently hosted in the United States, or in the region of your enterprise deployment.

#### How to identify models Hosted by ElevenLabs

Models hosted by ElevenLabs are clearly labeled in the ElevenLabs interface. Look for the “Hosted by ElevenLabs” designation when browsing or selecting models.

#### How your data is handled

For models hosted by ElevenLabs, requests are processed within ElevenLabs-managed infrastructure. This means that the original model provider does not receive, access, or process the inputs and outputs submitted through ElevenLabs.

By hosting these models, ElevenLabs can provide a consistent experience while maintaining control over the infrastructure used to serve model requests.

## Frequently asked questions

#### Where are self-hosted models hosted?

Models hosted by ElevenLabs are currently hosted on infrastructure located in the United States, or in the region of your enterprise deployment.

#### Does the original model provider access my data or metadata of my usage?

For models hosted by ElevenLabs, the model’s original developer never receives your inputs or outputs and has no access to the data about the deployment that processes them.

#### How do I know whether a model is Hosted by ElevenLabs?

Models hosted by ElevenLabs are clearly identified in the ElevenLabs interface with a “Hosted by ElevenLabs” designation.
