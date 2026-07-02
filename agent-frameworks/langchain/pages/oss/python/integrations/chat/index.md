---
title: "Chat model integrations"
source: https://docs.langchain.com/oss/python/integrations/chat/index
path: oss/python/integrations/chat/index
---

Integrate with chat models using LangChain Python.

[Chat models](/oss/python/langchain/models) are language models that use a sequence of [messages](/oss/python/langchain/messages) as inputs and return messages as outputs <Tooltip>(as opposed to traditional, plaintext LLMs)</Tooltip>.

## Featured models

<Info>
  **While these LangChain classes support the indicated advanced feature**, you may need to refer to provider-specific documentation to learn which hosted models or backends support the feature.
</Info>

| Model                                                                          | [Tool calling](/oss/python/langchain/tools) | [Structured output](/oss/python/langchain/structured-output/) | [Multimodal](/oss/python/langchain/messages#multimodal) |
| ------------------------------------------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------- |
| [`ChatOpenAI`](/oss/python/integrations/chat/openai)                           | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatAnthropic`](/oss/python/integrations/chat/anthropic)                     | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatVertexAI`](/oss/python/integrations/chat/google_vertex_ai) (deprecated)  | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatGoogleGenerativeAI`](/oss/python/integrations/chat/google_generative_ai) | ✅                                           | ✅                                                             | ✅                                                       |
| [`AzureChatOpenAI`](/oss/python/integrations/chat/azure_chat_openai)           | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatGroq`](/oss/python/integrations/chat/groq)                               | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatAmazonNova`](/oss/python/integrations/chat/amazon_nova)                  | ✅                                           | ❌                                                             | ✅                                                       |
| [`ChatHuggingFace`](/oss/python/integrations/chat/huggingface)                 | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatOllama`](/oss/python/integrations/chat/ollama)                           | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatXAI`](/oss/python/integrations/chat/xai)                                 | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatNVIDIA`](/oss/python/integrations/chat/nvidia_ai_endpoints)              | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatCohere`](/oss/python/integrations/chat/cohere)                           | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatMistralAI`](/oss/python/integrations/chat/mistralai)                     | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatTogether`](/oss/python/integrations/chat/together)                       | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatDeepSeek`](/oss/python/integrations/chat/deepseek)                       | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatDatabricks`](/oss/python/integrations/chat/databricks)                   | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatOpenRouter`](/oss/python/integrations/chat/openrouter)                   | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatLiteLLM`](/oss/python/integrations/chat/litellm)                         | ✅                                           | ✅                                                             | ✅                                                       |

See the [full list of chat model integrations](#all-chat-models) below for more options.

## Routers & proxies

Routers and proxies give you access to models from multiple providers through a single API and credential. They can simplify billing, let you switch between models without changing integrations, and offer features like automatic fallbacks.

| Provider                             | Integration                                                  | Description                                                                                       |
| ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| [OpenRouter](https://openrouter.ai/) | [`ChatOpenRouter`](/oss/python/integrations/chat/openrouter) | Unified access to models from OpenAI, Anthropic, Google, Meta, and more                           |
| [LiteLLM](https://www.litellm.ai/)   | [`ChatLiteLLMRouter`](/oss/python/integrations/chat/litellm) | Unified interface for OpenAI, Anthropic, Azure, Hugging Face, and more with routing and fallbacks |

## Chat Completions API

Certain model providers offer endpoints that are compatible with OpenAI's [Chat Completions API](https://platform.openai.com/docs/api-reference/chat). In such cases, you can use [`ChatOpenAI`](/oss/python/integrations/chat/openai) with a custom `base_url` to connect to these endpoints for basic chat functionality.

<Warning>
  `ChatOpenAI` targets [official OpenAI API specifications](https://github.com/openai/openai-openapi) only. Non-standard response fields from third-party providers (e.g., `reasoning_content`, `reasoning`, `reasoning_details`) **are not extracted or preserved**. Use a provider-specific package when you need access to non-standard features.

  For instance, OpenRouter has a dedicated LangChain integration. See the [`ChatOpenRouter` guide](/oss/python/integrations/chat/openrouter) for setup and usage.
</Warning>

## All chat models

<Columns>
  <Card title="Abso" icon="link" href="/oss/python/integrations/chat/abso" />

  <Card title="AI21 Labs" icon="link" href="/oss/python/integrations/chat/ai21" />

  <Card title="AI/ML API" icon="link" href="/oss/python/integrations/chat/aimlapi" />

  <Card title="Amazon Nova" icon="link" href="/oss/python/integrations/chat/amazon_nova" />

  <Card title="Anthropic" icon="link" href="/oss/python/integrations/chat/anthropic" />

  <Card title="AzureAIOpenAIApiChatModel" icon="link" href="/oss/python/integrations/chat/azure_ai" />

  <Card title="Azure OpenAI" icon="link" href="/oss/python/integrations/chat/azure_chat_openai" />

  <Card title="Baseten" icon="link" href="/oss/python/integrations/chat/baseten" />

  <Card title="Cerebras" icon="link" href="/oss/python/integrations/chat/cerebras" />

  <Card title="CloudflareWorkersAI" icon="link" href="/oss/python/integrations/chat/cloudflare_workersai" />

  <Card title="Cohere" icon="link" href="/oss/python/integrations/chat/cohere" />

  <Card title="ContextualAI" icon="link" href="/oss/python/integrations/chat/contextual" />

  <Card title="Crusoe" icon="link" href="/oss/python/integrations/chat/crusoe" />

  <Card title="Databricks" icon="link" href="/oss/python/integrations/chat/databricks" />

  <Card title="DeepSeek" icon="link" href="/oss/python/integrations/chat/deepseek" />

  <Card title="Featherless AI" icon="link" href="/oss/python/integrations/chat/featherless_ai" />

  <Card title="Google Gemini" icon="link" href="/oss/python/integrations/chat/google_generative_ai" />

  <Card title="Google Cloud Vertex AI" icon="link" href="/oss/python/integrations/chat/google_vertex_ai" />

  <Card title="Google Anthropic on Vertex AI" icon="link" href="/oss/python/integrations/chat/google_anthropic_vertex" />

  <Card title="DigitalOcean Gradient" icon="link" href="/oss/python/integrations/chat/gradientai" />

  <Card title="GreenNode" icon="link" href="/oss/python/integrations/chat/greennode" />

  <Card title="Groq" icon="link" href="/oss/python/integrations/chat/groq" />

  <Card title="ChatHuggingFace" icon="link" href="/oss/python/integrations/chat/huggingface" />

  <Card title="IBM watsonx.ai" icon="link" href="/oss/python/integrations/chat/ibm_watsonx" />

  <Card title="Kinetica" icon="link" href="/oss/python/integrations/chat/kinetica" />

  <Card title="LiteLLM" icon="link" href="/oss/python/integrations/chat/litellm" />

  <Card title="MistralAI" icon="link" href="/oss/python/integrations/chat/mistralai" />

  <Card title="ModelScope" icon="link" href="/oss/python/integrations/chat/modelscope_chat_endpoint" />

  <Card title="Naver" icon="link" href="/oss/python/integrations/chat/naver" />

  <Card title="Nebius" icon="link" href="/oss/python/integrations/chat/nebius" />

  <Card title="Netmind" icon="link" href="/oss/python/integrations/chat/netmind" />

  <Card title="NVIDIA AI Endpoints" icon="link" href="/oss/python/integrations/chat/nvidia_ai_endpoints" />

  <Card title="OCIGenAI" icon="link" href="/oss/python/integrations/chat/oci_generative_ai" />

  <Card title="OCI Data Science" icon="link" href="/oss/python/integrations/chat/oci_data_science" />

  <Card title="Ollama" icon="link" href="/oss/python/integrations/chat/ollama" />

  <Card title="OpenAI" icon="link" href="/oss/python/integrations/chat/openai" />

  <Card title="OpenRouter" icon="link" href="/oss/python/integrations/chat/openrouter" />

  <Card title="Parallel" icon="link" href="/oss/python/integrations/chat/parallel" />

  <Card title="Pipeshift" icon="link" href="/oss/python/integrations/chat/pipeshift" />

  <Card title="ChatPredictionGuard" icon="link" href="/oss/python/integrations/chat/predictionguard" />

  <Card title="Qwen QwQ" icon="link" href="/oss/python/integrations/chat/qwq" />

  <Card title="Qwen" icon="link" href="/oss/python/integrations/chat/qwen" />

  <Card title="RunPod Chat Model" icon="link" href="/oss/python/integrations/chat/runpod" />

  <Card title="SambaNova" icon="link" href="/oss/python/integrations/chat/sambanova" />

  <Card title="ChatSeekrFlow" icon="link" href="/oss/python/integrations/chat/seekrflow" />

  <Card title="Together" icon="link" href="/oss/python/integrations/chat/together" />

  <Card title="Upstage" icon="link" href="/oss/python/integrations/chat/upstage" />

  <Card title="vLLM Chat" icon="link" href="/oss/python/integrations/chat/vllm" />

  <Card title="ChatWriter" icon="link" href="/oss/python/integrations/chat/writer" />

  <Card title="xAI" icon="link" href="/oss/python/integrations/chat/xai" />

  <Card title="Xinference" icon="link" href="/oss/python/integrations/chat/xinference" />
</Columns>

<Info>
  If you'd like to contribute an integration, see [Contributing integrations](/oss/python/contributing#add-a-new-integration).
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/chat/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
