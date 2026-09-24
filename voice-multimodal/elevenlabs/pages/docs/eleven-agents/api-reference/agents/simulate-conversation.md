---
title: "Simulate conversation"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/simulate-conversation.md
path: docs/eleven-agents/api-reference/agents/simulate-conversation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Simulate conversation

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/simulate-conversation
Content-Type: application/json

Deprecated. Use the `/v1/convai/agent-testing/create` and `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run simulations. Run a conversation between the agent and a simulated user.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/simulate-conversation

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Body (application/json)

This endpoint expects an object.

- `simulation_specification` (ConversationSimulationSpecification, required) — A specification detailing how the conversation should be simulated
- `extra_evaluation_criteria` (list of PromptEvaluationCriteria, optional) — A list of evaluation criteria to test
- `new_turns_limit` (integer, optional, default: 10000) — Maximum number of new turns to generate in the conversation simulation

## Response

### 200

Successful Response

- `simulated_conversation` (list of ConversationHistoryTranscriptResponseModel, required)
- `analysis` (ConversationHistoryAnalysisCommonModel, required)

## Errors

### 422 Agents Simulate Conversation Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ConversationSimulationSpecification

A specification that will be used to simulate a conversation between an agent and an AI user.

- `simulated_user_config` (AgentConfig, required)
- `tool_mock_config` (map from string to ToolMockConfig, optional)
- `partial_conversation_history` (list of ConversationHistoryTranscriptCommonModelInput, optional) — A partial conversation history to start the simulation from. If empty, simulation starts fresh.
- `dynamic_variables` (map from string to any, optional)

### PromptEvaluationCriteria

An evaluation using the transcript and a prompt for a yes/no achieved answer

- `id` (string, required) — The unique identifier for the evaluation criteria
- `name` (string, required)
- `conversation_goal_prompt` (string, required) — The prompt that the agent should use to evaluate the conversation
- `type` ("prompt", optional) — The type of evaluation criteria
- `use_knowledge_base` (boolean, optional, default: false) — When evaluating the prompt, should the agent's knowledge base be used.
- `scope` (enum, optional, default: conversation) — The scope of transcript context used when evaluating this criterion. 'conversation' uses the full transcript; 'agent' uses only the portion where the defining agent was active.
  - Allowed values: `conversation`, `agent`
- `llm` (enum, optional) — LLM model to use for this evaluation criteria. If not set, uses agent's analysis_llm default.
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `scoring_mode` (enum, optional, default: binary) — How this criterion is scored. 'binary' resolves to success/failure/unknown. 'numeric_uniform' returns a number on the [0, max_score] scale which is normalized into the aggregate conversation success percentage.
  - Allowed values: `binary`, `numeric_uniform`
- `max_score` (integer, optional, default: 100) — Maximum value of the numeric score scale (minimum is always 0). Only used when scoring_mode is 'numeric_uniform'.
- `score_instructions` (string, optional) — Optional free-text instructions describing how to assign values on the numeric scale. Only used when scoring_mode is 'numeric_uniform'.

### ConversationHistoryTranscriptResponseModel

- `role` (enum, required)
  - Allowed values: `user`, `agent`
- `time_in_call_secs` (integer, required)
- `agent_metadata` (AgentMetadata, optional)
- `message` (string, optional)
- `multivoice_message` (ConversationHistoryMultivoiceMessageModel, optional) — Represents a message from a multi-voice agent.
- `tool_calls` (list of ConversationHistoryTranscriptToolCallCommonModelOutput, optional)
- `tool_results` (list of ConversationHistoryTranscriptResponseModelToolResultsItem, optional)
- `feedback` (UserFeedback, optional)
- `llm_override` (string, optional)
- `producing_llm` (string, optional)
- `conversation_turn_metrics` (ConversationTurnMetrics, optional)
- `rag_retrieval_info` (RagRetrievalInfo, optional)
- `llm_usage` (LlmUsageOutput, optional)
- `interrupted` (boolean, optional, default: false)
- `ignored_as_backchannel` (boolean, optional, default: false)
- `original_message` (string, optional)
- `reasoning` (list of ConversationReasoningModel, optional)
- `source_medium` (enum, optional)
  - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
- `source_event_id` (integer, optional)
- `used_static_kb_document_ids` (list of string, optional)
- `user_identifier` (string, optional)
- `id` (string, optional)
- `triggered_guardrails` (list of TriggeredGuardrailCommonModel, optional)
- `file_input` (ConversationHistoryTranscriptFileInputResponseModel, optional) — Deprecated: the first attachment on this turn. Use `file_inputs` to see every attachment.
- `file_inputs` (list of ConversationHistoryTranscriptFileInputResponseModel, optional) — All files attached to this turn, in the order the user attached them.
- `contextual_update_info` (ContextualUpdateInfo, optional)
- `reasoned` (boolean, optional, default: false)

### ConversationHistoryAnalysisCommonModel

- `call_successful` (enum, required)
  - Allowed values: `success`, `failure`, `unknown`
- `transcript_summary` (string, required)
- `evaluation_criteria_results` (map from string to ConversationHistoryEvaluationCriteriaResultCommonModel, optional)
- `data_collection_results` (map from string to DataCollectionResultCommonModel, optional)
- `evaluation_criteria_results_list` (list of ConversationHistoryEvaluationCriteriaResultCommonModel, optional)
- `data_collection_results_list` (list of DataCollectionResultCommonModel, optional)
- `call_success_score` (double, optional)
- `call_summary_title` (string, optional)
- `scoped` (list of ScopedAnalysisResult, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### AgentConfig

- `first_message` (string, optional, default: ) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional, default: en) — Language of the agent - used for ASR and TTS
- `hinglish_mode` (boolean, optional, default: false) — When enabled and language is Hindi, the agent will respond in Hinglish
- `dynamic_variables` (any, optional)
- `disable_first_message_interruptions` (boolean, optional, default: false) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
- `max_conversation_duration_message` (string, optional, default: ) — If non-empty, the message the agent will send when max conversation duration is reached.
- `text_behavior_overrides` (map from string to BehaviorOverride, optional) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
- `prompt` (PromptAgentApiModelOutput, optional) — The prompt for the agent

### ToolMockConfig

- `default_return_value` (string, optional, default: Tool Called.)
- `default_is_error` (boolean, optional, default: false)

### ConversationHistoryTranscriptCommonModelInput

- `role` (enum, required)
  - Allowed values: `user`, `agent`
- `time_in_call_secs` (integer, required)
- `agent_metadata` (AgentMetadata, optional)
- `message` (string, optional)
- `multivoice_message` (ConversationHistoryMultivoiceMessageModel, optional) — Represents a message from a multi-voice agent.
- `tool_calls` (list of ConversationHistoryTranscriptToolCallCommonModelInput, optional)
- `tool_results` (list of ConversationHistoryTranscriptCommonModelInputToolResultsItem, optional)
- `feedback` (UserFeedback, optional)
- `llm_override` (string, optional)
- `producing_llm` (string, optional)
- `conversation_turn_metrics` (ConversationTurnMetrics, optional)
- `rag_retrieval_info` (RagRetrievalInfo, optional)
- `llm_usage` (LlmUsageInput, optional)
- `interrupted` (boolean, optional, default: false)
- `ignored_as_backchannel` (boolean, optional, default: false)
- `original_message` (string, optional)
- `reasoning` (list of ConversationReasoningModel, optional)
- `source_medium` (enum, optional)
  - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
- `source_event_id` (integer, optional)
- `used_static_kb_document_ids` (list of string, optional)
- `user_identifier` (string, optional)
- `id` (string, optional)
- `triggered_guardrails` (list of TriggeredGuardrailCommonModel, optional)

### AgentMetadata

- `agent_id` (string, required)
- `branch_id` (string, optional)
- `workflow_node_id` (string, optional)
- `version_id` (string, optional)

### ConversationHistoryMultivoiceMessageModel

Represents a message from a multi-voice agent.

- `parts` (list of ConversationHistoryMultivoiceMessagePartModel, required)

### ConversationHistoryTranscriptToolCallCommonModelOutput

- `request_id` (string, required)
- `tool_name` (string, required)
- `params_as_json` (string, required)
- `tool_has_been_called` (boolean, required)
- `type` (enum, optional)
  - Allowed values: `system`, `webhook`, `client`, `mcp`, `workflow`, `api_integration_webhook`, `api_integration_mcp`, `smb`
- `tool_details` (ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails, optional)

### ConversationHistoryTranscriptResponseModelToolResultsItem

### UserFeedback

- `score` (enum, required)
  - Allowed values: `like`, `dislike`
- `time_in_call_secs` (integer, required)

### ConversationTurnMetrics

- `metrics` (map from string to MetricRecord, optional)
- `convai_asr_provider` (string, optional)
- `convai_tts_model` (string, optional)
- `convai_tts_cascade` (string, optional)

### RagRetrievalInfo

- `chunks` (list of RagChunkMetadata, required)
- `embedding_model` (enum, required, default: e5_mistral_7b_instruct)
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
- `retrieval_query` (string, required)
- `rag_latency_secs` (double, required)
- `used_chunk_ids` (list of string, optional)

### LlmUsageOutput

- `model_usage` (map from string to LlmInputOutputTokensUsage, optional)

### ConversationReasoningModel

- `summary` (string, optional)
- `provider_redact` (boolean, optional, default: false)

### TriggeredGuardrailCommonModel

- `guardrail_type` (enum, required)
  - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
- `guardrail_name` (string, optional)

### ConversationHistoryTranscriptFileInputResponseModel

- `file_id` (string, required)
- `original_filename` (string, required)
- `mime_type` (string, required)
- `file_url` (string, required)

### ContextualUpdateInfo

- `context_id` (string, required) — Client-supplied identifier grouping related contextual updates.
- `is_superseded` (boolean, optional, default: false) — True when this contextual update has been replaced by a newer update with the same context_id.

### ConversationHistoryEvaluationCriteriaResultCommonModel

- `criteria_id` (string, required)
- `result` (enum, required)
  - Allowed values: `success`, `failure`, `unknown`
- `rationale` (string, required)
- `scoring_mode` (enum, optional, default: binary)
  - Allowed values: `binary`, `numeric_uniform`
- `score` (integer, optional)
- `max_score` (integer, optional)

### DataCollectionResultCommonModel

- `data_collection_id` (string, required)
- `rationale` (string, required)
- `name` (string, optional)
- `value` (any, optional)
- `json_schema` (LiteralJsonSchemaProperty, optional) — Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.

### ScopedAnalysisResult

- `scope` (enum, required, default: conversation) — The scope of the analysis. 'conversation' uses the full transcript; 'agent' uses only the portion where the defining agent was active.
  - Allowed values: `conversation`, `agent`
- `source_agent_id` (string, required)
- `successful` (enum, required)
  - Allowed values: `success`, `failure`, `unknown`
- `source_branch_id` (string, optional) — Branch of the agent for this scoped block; disambiguates repeated agent_id.
- `evaluation_criteria_results` (map from string to ConversationHistoryEvaluationCriteriaResultCommonModel, optional)
- `data_collection_results` (map from string to DataCollectionResultCommonModel, optional)
- `success_score` (double, optional)

### ValidationErrorLocItem

### BehaviorOverride

- `verbosity` (enum, optional) — Verbosity override. Underlying default applies when unset.
  - Allowed values: `auto`, `concise`, `thorough`
- `output_format` (enum, optional) — Output format override. Underlying default applies when unset.
  - Allowed values: `mp3_22050_32`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `ulaw_8000`
- `interaction_budget` (enum, optional) — Interaction budget override. Underlying default applies when unset.
  - Allowed values: `realtime`, `5_minutes`, `10_minutes`, `1_hour`

### PromptAgentApiModelOutput

- `prompt` (string, optional, default: ) — The prompt for the agent
- `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `reasoning_effort` (enum, optional) — Reasoning effort of the model. Only available for some models.
  - Allowed values: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`
- `thinking_budget` (integer, optional) — Max number of tokens used for thinking. Use 0 to turn off if supported by the model.
- `enable_reasoning_summary` (boolean, optional, default: false) — Enable model reasoning summaries. When disabled, we do not request summaries from provider if possible for faster TTFB. Not ZRM compatible.
- `temperature` (double, optional) — The temperature for the LLM. Defaults to 0. Set to null to omit the parameter from the LLM request entirely (useful for custom LLMs that reject the temperature field).
- `max_tokens` (integer, optional, default: -1) — If greater than 0, maximum number of tokens the LLM can predict
- `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
- `built_in_tools` (BuiltInToolsOutput, optional) — Built-in system tools to be used by the agent
- `enable_parallel_tool_calls` (boolean, optional, default: true) — Enable parallel tool calling. When enabled, the agent can execute multiple tools in parallel within a single turn. Not supported by all models.
- `mcp_server_ids` (list of string, optional) — A list of MCP server ids to be used by the agent
- `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional) — A list of knowledge bases to be used by the agent
- `custom_llm` (CustomLlm, optional) — Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
- `ignore_default_personality` (boolean, optional) — Whether to remove the default personality lines from the system prompt
- `rag` (RagConfigOutput, optional) — Configuration for RAG
- `timezone` (string, optional) — Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references.
- `backup_llm_config` (PromptAgentApiModelOutputBackupLlmConfig, optional) — Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.
- `cascade_timeout_seconds` (double, optional, default: 4) — Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.
- `tools` (list of PromptAgentApiModelOutputToolsItem, optional, deprecated) — A list of tools that the agent can use over the course of the conversation, use tool_ids instead

### ConversationHistoryTranscriptToolCallCommonModelInput

- `request_id` (string, required)
- `tool_name` (string, required)
- `params_as_json` (string, required)
- `tool_has_been_called` (boolean, required)
- `type` (enum, optional)
  - Allowed values: `system`, `webhook`, `client`, `mcp`, `workflow`, `api_integration_webhook`, `api_integration_mcp`, `smb`
- `tool_details` (ConversationHistoryTranscriptToolCallCommonModelInputToolDetails, optional)

### ConversationHistoryTranscriptCommonModelInputToolResultsItem

### LlmUsageInput

- `model_usage` (map from string to LlmInputOutputTokensUsage, optional)

### ConversationHistoryMultivoiceMessagePartModel

Represents a single voice part of a multi-voice message.

- `text` (string, required)
- `voice_label` (string, optional)
- `time_in_call_secs` (integer, optional)

### ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails

- `type`: `api_integration_webhook`
  - `credential_id` (string, required, default: )
  - `integration_connection_id` (string, required, default: )
  - `integration_id` (string, required, default: )
  - `webhook_details` (ConversationHistoryTranscriptToolCallWebhookDetails, required)
- `type`: `client`
  - `parameters` (string, required)
- `type`: `mcp`
  - `approval_policy` (string, required)
  - `integration_type` (string, required)
  - `mcp_server_id` (string, required)
  - `mcp_server_name` (string, required)
  - `mcp_tool_description` (string, optional, default: )
  - `mcp_tool_name` (string, optional, default: )
  - `parameters` (map from string to string, optional)
  - `requires_approval` (boolean, optional, default: false)
- `type`: `webhook`
  - `method` (string, required)
  - `url` (string, required)
  - `body` (string, optional)
  - `headers` (map from string to string, optional)
  - `path_params` (map from string to string, optional)
  - `query_params` (map from string to string, optional)

### ConversationHistoryTranscriptOtherToolsResultCommonModel

- `request_id` (string, required)
- `tool_name` (string, required)
- `result_value` (string, required)
- `is_error` (boolean, required)
- `tool_has_been_called` (boolean, required)
- `is_blocked` (boolean, optional, default: false)
- `tool_latency_secs` (double, optional, default: 0)
- `error_type` (string, optional, default: )
- `raw_error_message` (string, optional, default: )
- `dynamic_variable_updates` (list of DynamicVariableUpdateCommonModel, optional)
- `type` (enum, optional)
  - Allowed values: `client`, `webhook`, `mcp`, `code`

### ConversationHistoryTranscriptSystemToolResultCommonModelOutput

- `request_id` (string, required)
- `tool_name` (string, required)
- `result_value` (string, required)
- `is_error` (boolean, required)
- `tool_has_been_called` (boolean, required)
- `type` ("system", required)
- `is_blocked` (boolean, optional, default: false)
- `tool_latency_secs` (double, optional, default: 0)
- `error_type` (string, optional, default: )
- `raw_error_message` (string, optional, default: )
- `dynamic_variable_updates` (list of DynamicVariableUpdateCommonModel, optional)
- `result` (ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult, optional)

### ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput

- `request_id` (string, required)
- `tool_name` (string, required)
- `result_value` (string, required)
- `is_error` (boolean, required)
- `is_blocked` (boolean, required, default: false)
- `tool_has_been_called` (boolean, required)
- `tool_latency_secs` (double, required, default: 0)
- `error_type` (string, required, default: )
- `raw_error_message` (string, required, default: )
- `dynamic_variable_updates` (list of DynamicVariableUpdateCommonModel, required)
- `type` ("api_integration_webhook", required)
- `integration_id` (string, required, default: )
- `credential_id` (string, required, default: )
- `integration_connection_id` (string, required, default: )

### ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput

- `request_id` (string, required)
- `tool_name` (string, required)
- `result_value` (string, required)
- `is_error` (boolean, required)
- `tool_has_been_called` (boolean, required)
- `type` ("workflow", required)
- `is_blocked` (boolean, optional, default: false)
- `tool_latency_secs` (double, optional, default: 0)
- `error_type` (string, optional, default: )
- `raw_error_message` (string, optional, default: )
- `dynamic_variable_updates` (list of DynamicVariableUpdateCommonModel, optional)
- `result` (WorkflowToolResponseModelOutput, optional) — A common model for workflow tool responses.

### MetricRecord

- `elapsed_time` (double, required)

### RagChunkMetadata

- `document_id` (string, required)
- `chunk_id` (string, required)
- `vector_distance` (double, required)

### LlmInputOutputTokensUsage

- `input` (LlmTokensCategoryUsage, optional)
- `input_cache_read` (LlmTokensCategoryUsage, optional)
- `input_cache_write` (LlmTokensCategoryUsage, optional)
- `output_total` (LlmTokensCategoryUsage, optional)

### LiteralJsonSchemaProperty

Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.

- `type` (LiteralJsonSchemaPropertyType, required)
- `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
- `enum` (list of string, optional) — List of allowed string values for string type parameters
- `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
- `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
- `allowed_values` (AllowedValues, optional) — Server-side rejection guard for an LLM-provided value: the runtime rejects any value outside the permitted set this object names, and the set is not advertised to the LLM as an enum. Only supported when the value source is `description`; combining it with dynamic_variable, is_system_provided, constant_value, or is_omitted is rejected.
- `constant_value` (LiteralJsonSchemaPropertyConstantValue, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
- `allowed_values_dynamic_variable` (string, optional, default: , deprecated) — DEPRECATED: use `allowed_values` instead. When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable (must be a JSON array such as ["ws_alpha", "ws_beta"]). Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.

### BuiltInToolsOutput

System tools a conversational agent can be given. Deliberately not named ConversationalBuiltInTools: BuiltInToolsInput and BuiltInToolsOutput are part of the public API spec and the generated SDKs.

- `transfer_to_agent` (SystemToolConfigOutput, optional) — The transfer to agent tool
- `end_call` (SystemToolConfigOutput, optional) — The end call tool
- `language_detection` (SystemToolConfigOutput, optional) — The language detection tool
- `transfer_to_number` (SystemToolConfigOutput, optional) — The transfer to number tool
- `skip_turn` (SystemToolConfigOutput, optional) — The skip turn tool
- `play_keypad_touch_tone` (SystemToolConfigOutput, optional) — The play DTMF tool
- `voicemail_detection` (SystemToolConfigOutput, optional) — The voicemail detection tool

### KnowledgeBaseLocator

- `type` (enum, required) — The type of the knowledge base
  - Allowed values: `file`, `url`, `text`, `folder`
- `name` (string, required) — The name of the knowledge base
- `id` (string, required) — The ID of the knowledge base
- `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
  - Allowed values: `prompt`, `auto`

### CustomLlm

- `url` (string, required) — The URL of the Chat Completions compatible endpoint
- `model_id` (string, optional) — The model ID to be used if URL serves multiple models
- `api_key` (CustomLlmApiKey, optional) — The API key for authentication. Either a workspace secret reference \{'secret\_id': '...'} or an environment variable reference \{'env\_var\_label': '...'}.
- `auth_connection` (CustomLlmAuthConnection, optional) — Optional workspace auth connection for authentication. Only auth connections that produce an Authorization Bearer token are supported; Basic auth, mTLS, custom header, and URL secret auth connections are not supported.
- `request_headers` (map from string to CustomLlmRequestHeadersValue, optional) — Headers that should be included in the request
- `api_version` (string, optional) — The API version to use for the request
- `api_type` (enum, optional, default: chat_completions) — The API type to use (chat_completions, responses or websocket)
  - Allowed values: `chat_completions`, `responses`, `websocket`

### RagConfigOutput

- `enabled` (boolean, optional, default: false)
- `embedding_model` (enum, optional, default: e5_mistral_7b_instruct)
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
- `max_vector_distance` (double, optional, default: 0.6) — Maximum vector distance of retrieved chunks.
- `max_documents_length` (integer, optional, default: 50000) — Maximum total length of document chunks retrieved from RAG.
- `max_retrieved_rag_chunks_count` (integer, optional, default: 20) — Maximum number of RAG document chunks to initially retrieve from the vector store. These are then further filtered by vector distance and total length.
- `num_candidates` (integer, optional) — Number of candidates evaluated in ANN vector search. Higher number means better results, but higher latency. Minimum recommended value is 100. If disabled, the default value is used.
- `query_rewrite_prompt_override` (string, optional) — Custom prompt for rewriting user queries before RAG retrieval. The conversation history will be automatically appended at the end. If not set, the default prompt will be used.
- `knowledge_base_tool_info` (KnowledgeBaseToolInfo, optional) — When set, the agent uses the knowledge_base tool instead of the legacy knowledge_base_rag tool. None means the agent is not opted in.

### PromptAgentApiModelOutputBackupLlmConfig

Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.

- `preference`: `default`
- `preference`: `disabled`
- `preference`: `override`
  - `order` (list of enum, required)
    - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`

### PromptAgentApiModelOutputToolsItem

The type of tool

- `type`: `api_integration_webhook`
  - `api_integration_connection_id` (string, required)
  - `api_integration_id` (string, required)
  - `assignments` (list of DynamicVariableAssignment, required) — Configuration for extracting values from tool responses and assigning them to dynamic variables
  - `description` (string, required) — Description of when the tool should be used and what it does.
  - `dynamic_variables` (DynamicVariablesConfig, required) — Configuration for dynamic variables
  - `execution_mode` (enum, required, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
    - Allowed values: `immediate`, `post_tool_speech`, `async`
  - `interruption_mode` (enum, required, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
    - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
  - `name` (string, required)
  - `pre_tool_speech` (enum, required, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
    - Allowed values: `auto`, `force`, `off`
  - `response_timeout_secs` (integer, required, default: 20) — The maximum time in seconds to wait for the tool call to complete. Must be between 5 and 300 seconds (inclusive).
  - `tool_call_sound_behavior` (enum, required, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
    - Allowed values: `auto`, `always`
  - `tool_error_handling_mode` (enum, required, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
    - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
  - `tool_version` (string, required, default: 1.0.0) — The version of the API integration tool
  - `disable_interruptions` (boolean, required, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
  - `force_pre_tool_speech` (boolean, required, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
  - `api_schema_overrides` (ApiIntegrationWebhookOverrides, optional) — User overrides applied on top of the base api_schema
  - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
    - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
- `type`: `client`
  - `description` (string, required) — Description of when the tool should be used and what it does.
  - `name` (string, required)
  - `assignments` (list of DynamicVariableAssignment, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
  - `dynamic_variables` (DynamicVariablesConfig, optional) — Configuration for dynamic variables
  - `execution_mode` (enum, optional, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
    - Allowed values: `immediate`, `post_tool_speech`, `async`
  - `expects_response` (boolean, optional, default: false) — If true, calling this tool should block the conversation until the client responds with some response which is passed to the llm. If false then we will continue the conversation without waiting for the client to respond, this is useful to show content to a user but not block the conversation
  - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
    - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
  - `parameters` (ObjectJsonSchemaPropertyOutput, optional) — Schema for any parameters to pass to the client
  - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
    - Allowed values: `auto`, `force`, `off`
  - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete. Must be between 1 and 120 seconds (inclusive).
  - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
    - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
  - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
    - Allowed values: `auto`, `always`
  - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
    - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
  - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
  - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
- `type`: `mcp`
  - `value` (any, required)
- `type`: `smb`
  - `value` (any, required)
- `type`: `system`
  - `name` (string, required)
  - `params` (SystemToolConfigOutputParams, required)
  - `assignments` (list of DynamicVariableAssignment, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
  - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
  - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
    - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
  - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
    - Allowed values: `auto`, `force`, `off`
  - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
  - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
    - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
  - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
    - Allowed values: `auto`, `always`
  - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
    - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
  - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
  - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
- `type`: `webhook`
  - `api_schema` (WebhookToolApiSchemaConfigOutput, required) — The schema for the outgoing webhoook, including parameters and URL specification
  - `description` (string, required) — Description of when the tool should be used and what it does.
  - `name` (string, required)
  - `assignments` (list of DynamicVariableAssignment, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
  - `dynamic_variables` (DynamicVariablesConfig, optional) — Configuration for dynamic variables
  - `execution_mode` (enum, optional, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
    - Allowed values: `immediate`, `post_tool_speech`, `async`
  - `follow_redirects` (boolean, optional, default: false) — Whether to resolve a redirect from the endpoint and return the final response. One redirect is followed, as a GET without the request body; nothing configured on this tool (headers, authentication, client certificate) is sent to the redirect target. Both the endpoint and the redirect target must use HTTPS. Not supported for API integration tools.
  - `follow_redirects_allowed_domains` (list of string, optional) — Domains a redirect may point at, e.g. 'test.example.com'. Required when following redirects, and a target outside the list is refused.
  - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
    - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
  - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
    - Allowed values: `auto`, `force`, `off`
  - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete. Must be between 5 and 300 seconds (inclusive).
  - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
    - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
  - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
    - Allowed values: `auto`, `always`
  - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
    - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
  - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
  - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.

### ConversationHistoryTranscriptToolCallCommonModelInputToolDetails

- `type`: `api_integration_webhook`
  - `webhook_details` (ConversationHistoryTranscriptToolCallWebhookDetails, required)
  - `credential_id` (string, optional, default: )
  - `integration_connection_id` (string, optional, default: )
  - `integration_id` (string, optional, default: )
- `type`: `client`
  - `parameters` (string, required)
- `type`: `mcp`
  - `approval_policy` (string, required)
  - `integration_type` (string, required)
  - `mcp_server_id` (string, required)
  - `mcp_server_name` (string, required)
  - `mcp_tool_description` (string, optional, default: )
  - `mcp_tool_name` (string, optional, default: )
  - `parameters` (map from string to string, optional)
  - `requires_approval` (boolean, optional, default: false)
- `type`: `webhook`
  - `method` (string, required)
  - `url` (string, required)
  - `body` (string, optional)
  - `headers` (map from string to string, optional)
  - `path_params` (map from string to string, optional)
  - `query_params` (map from string to string, optional)

### ConversationHistoryTranscriptSystemToolResultCommonModelInput

- `request_id` (string, required)
- `tool_name` (string, required)
- `result_value` (string, required)
- `is_error` (boolean, required)
- `tool_has_been_called` (boolean, required)
- `type` ("system", required)
- `is_blocked` (boolean, optional, default: false)
- `tool_latency_secs` (double, optional, default: 0)
- `error_type` (string, optional, default: )
- `raw_error_message` (string, optional, default: )
- `dynamic_variable_updates` (list of DynamicVariableUpdateCommonModel, optional)
- `result` (ConversationHistoryTranscriptSystemToolResultCommonModelInputResult, optional)

### ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelInput

- `request_id` (string, required)
- `tool_name` (string, required)
- `result_value` (string, required)
- `is_error` (boolean, required)
- `tool_has_been_called` (boolean, required)
- `type` ("api_integration_webhook", required)
- `is_blocked` (boolean, optional, default: false)
- `tool_latency_secs` (double, optional, default: 0)
- `error_type` (string, optional, default: )
- `raw_error_message` (string, optional, default: )
- `dynamic_variable_updates` (list of DynamicVariableUpdateCommonModel, optional)
- `integration_id` (string, optional, default: )
- `credential_id` (string, optional, default: )
- `integration_connection_id` (string, optional, default: )

### ConversationHistoryTranscriptWorkflowToolsResultCommonModelInput

- `request_id` (string, required)
- `tool_name` (string, required)
- `result_value` (string, required)
- `is_error` (boolean, required)
- `tool_has_been_called` (boolean, required)
- `type` ("workflow", required)
- `is_blocked` (boolean, optional, default: false)
- `tool_latency_secs` (double, optional, default: 0)
- `error_type` (string, optional, default: )
- `raw_error_message` (string, optional, default: )
- `dynamic_variable_updates` (list of DynamicVariableUpdateCommonModel, optional)
- `result` (WorkflowToolResponseModelInput, optional) — A common model for workflow tool responses.

### ConversationHistoryTranscriptToolCallWebhookDetails

- `method` (string, required)
- `url` (string, required)
- `type` ("webhook", optional)
- `headers` (map from string to string, optional)
- `path_params` (map from string to string, optional)
- `query_params` (map from string to string, optional)
- `body` (string, optional)

### DynamicVariableUpdateCommonModel

Tracks a dynamic variable update that occurred during tool execution.

- `variable_name` (string, required)
- `new_value` (string, required)
- `updated_at` (double, required)
- `tool_name` (string, required)
- `tool_request_id` (string, required)
- `old_value` (string, optional)

### ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult

- `result_type`: `dummy`
- `result_type`: `end_call_success`
  - `message` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `end_procedure_error`
  - `message` (string, required)
  - `status` (enum, required)
    - Allowed values: `not_found`, `invalid_id`
  - `procedure_id` (string, optional)
- `result_type`: `end_procedure_success`
  - `procedure_id` (string, required)
  - `procedure_name` (string, required)
  - `message` (string, optional, default: )
  - `status` ("success", optional)
- `result_type`: `knowledge_base_rag_success`
  - `chunk_count` (integer, optional, default: 0) — Number of relevant chunks retrieved
  - `chunks` (list of KnowledgeBaseRagChunkModel, optional) — Retrieved chunks; populated only in the rag-result-in-tool-result mode
  - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
  - `status` (enum, optional, default: success)
    - Allowed values: `success`, `no_documents`, `no_results`
- `result_type`: `knowledge_base_success`
  - `chunk_count` (integer, optional, default: 0)
  - `message` (string, optional, default: Referenced knowledge base.)
  - `status` (enum, optional, default: success)
    - Allowed values: `success`, `no_matching_documents`, `no_results`
- `result_type`: `language_detection_success`
  - `language` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `play_dtmf_error`
  - `error` (string, required)
  - `details` (string, optional)
  - `status` ("error", optional)
- `result_type`: `play_dtmf_success`
  - `dtmf_tones` (string, required)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `skip_turn_success`
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `start_procedure_error`
  - `message` (string, required)
  - `status` (enum, required)
    - Allowed values: `not_found`, `invalid_name`, `already_active`
  - `procedure_id` (string, optional)
- `result_type`: `start_procedure_success`
  - `procedure_id` (string, required)
  - `procedure_name` (string, required)
  - `message` (string, optional, default: Procedure is now started. Follow its instructions from the <active-procedures> section of your system prompt.)
  - `procedure_entry_workflow_node` (string, optional)
  - `procedure_return_workflow_node` (string, optional)
  - `status` ("success", optional)
- `result_type`: `testing_tool_result`
  - `reason` (string, optional, default: Skipping tool call in test mode)
  - `status` ("success", optional)
- `result_type`: `transfer_to_agent_error`
  - `error` (string, required)
  - `from_agent` (string, required)
  - `status` ("error", optional)
- `result_type`: `transfer_to_agent_success`
  - `condition` (string, required)
  - `from_agent` (string, required)
  - `to_agent` (string, required)
  - `branch_info` (TransferToAgentToolResultSuccessModelOutputBranchInfo, optional)
  - `delay_ms` (integer, optional, default: 0)
  - `enable_transferred_agent_first_message` (boolean, optional, default: false)
  - `preserve_client_tts_overrides` (boolean, optional, default: false)
  - `status` ("success", optional)
  - `to_node` (string, optional)
  - `transfer_message` (string, optional)
- `result_type`: `transfer_to_number_error`
  - `error` (string, required)
  - `details` (string, optional)
  - `status` ("error", optional)
- `result_type`: `transfer_to_number_exotel_success`
  - `transfer_number` (string, required)
  - `agent_message` (string, optional)
  - `note` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `transfer_to_number_sip_success`
  - `transfer_number` (string, required)
  - `note` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `transfer_to_number_twilio_success`
  - `agent_message` (string, required)
  - `conference_name` (string, required)
  - `transfer_number` (string, required)
  - `client_message` (string, optional)
  - `note` (string, optional)
  - `post_dial_digits` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `voicemail_detection_success`
  - `reason` (string, optional)
  - `status` ("success", optional)
  - `voicemail_message` (string, optional)

### WorkflowToolResponseModelOutput

A common model for workflow tool responses.

- `steps` (list of WorkflowToolResponseModelOutputStepsItem, optional)

### LlmTokensCategoryUsage

- `tokens` (integer, optional, default: 0)
- `price` (double, optional, default: 0)

### LiteralJsonSchemaPropertyType

### AllowedValues

- `dynamic_variable` (string, required) — Name of a dynamic variable that must resolve to a JSON array of permitted values, e.g. ["ws_alpha", "ws_beta"]. System variables work only if they resolve to a list.

### LiteralJsonSchemaPropertyConstantValue

A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.

### SystemToolConfigOutput

A system tool is a tool that is used to call a system method in the server

- `name` (string, required)
- `params` (SystemToolConfigOutputParams, required)
- `type` ("system", optional) — The type of tool
- `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
- `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
- `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
  - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
- `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
  - Allowed values: `auto`, `force`, `off`
- `assignments` (list of DynamicVariableAssignment, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
- `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
  - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
- `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
  - Allowed values: `auto`, `always`
- `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
  - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
- `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
- `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.

### CustomLlmApiKey

The API key for authentication. Either a workspace secret reference \{'secret\_id': '...'} or an environment variable reference \{'env\_var\_label': '...'}.

### CustomLlmAuthConnection

Optional workspace auth connection for authentication. Only auth connections that produce an Authorization Bearer token are supported; Basic auth, mTLS, custom header, and URL secret auth connections are not supported.

### CustomLlmRequestHeadersValue

### KnowledgeBaseToolInfo

- `enabled_strategies` (list of enum, optional) — Search strategies exposed to the model. Must be non-empty.
  - Allowed values: `cat`, `keyword`, `semantic`, `ls`

### DynamicVariableAssignment

Configuration for extracting values from tool responses and assigning them to dynamic variables.

- `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
- `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
- `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
- `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
- `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.

### DynamicVariablesConfig

- `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values

### ApiIntegrationWebhookOverrides

- `schema_overrides` (map from string to ApiIntegrationWebhookOverridesSchemaOverridesValue, optional)
- `response_filter_mode` (enum, optional, default: all) — Controls how tool responses are filtered before being visible to the agent.
  - Allowed values: `all`, `allow`, `hide_all`
- `response_filters` (list of string, optional)
- `request_headers` (map from string to ApiIntegrationWebhookOverridesRequestHeadersValue, optional)

### ObjectJsonSchemaPropertyOutput

- `description` (string, optional, default: )
- `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
- `constant_value` (map from string to any, optional) — When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
- `type` ("object", optional)
- `required` (list of string, optional)
- `properties` (map from string to ObjectJsonSchemaPropertyOutputPropertiesValue, optional)
- `required_constraints` (RequiredConstraints, optional) — Wrapper for anyOf/allOf composition constraints scoped to required fields.

### SystemToolConfigOutputParams

- `system_tool_type`: `end_call`
- `system_tool_type`: `end_procedure`
  - `procedures` (map from string to EndProcedureToolConfigProceduresValue, optional)
- `system_tool_type`: `knowledge_base`
  - `enabled_strategies` (list of enum, optional)
    - Allowed values: `cat`, `keyword`, `semantic`, `ls`
- `system_tool_type`: `knowledge_base_rag`
- `system_tool_type`: `language_detection`
  - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
- `system_tool_type`: `play_keypad_touch_tone`
  - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
  - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
- `system_tool_type`: `skip_turn`
- `system_tool_type`: `start_procedure`
  - `procedures` (map from string to StartProcedureToolConfigProceduresValue, optional)
- `system_tool_type`: `transfer_to_agent`
  - `transfers` (list of AgentTransferOutput, required)
- `system_tool_type`: `transfer_to_number`
  - `transfers` (list of PhoneNumberTransfer, required)
  - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
- `system_tool_type`: `voicemail_detection`
  - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).

### WebhookToolApiSchemaConfigOutput

- `url` (string, required) — The URL that the webhook will be sent to. May include path parameters, e.g. [https://example.com/agents/\{agent\_id}](https://example.com/agents/\{agent_id})
- `request_headers` (map from string to WebhookToolApiSchemaConfigOutputRequestHeadersValue, optional) — Headers that should be included in the request
- `method` (enum, optional, default: GET) — The HTTP method to use for the webhook
  - Allowed values: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- `path_params_schema` (map from string to LiteralJsonSchemaProperty, optional) — Schema for path parameters, if any. The keys should match the placeholders in the URL.
- `query_params_schema` (QueryParamsJsonSchemaOutput, optional) — Schema for any query params, if any. These will be added to end of the URL as query params. Note: properties in a query param must all be literal types
- `request_body_schema` (ObjectJsonSchemaPropertyOutput, optional) — Schema for the body parameters, if any. Used for POST/PATCH/PUT requests. The schema should be an object which will be sent as the json body
- `response_body_schema` (ObjectJsonSchemaPropertyOutput, optional) — Schema describing the expected response body structure. For documentation only; not surfaced to the LLM.
- `response_filter` (ResponseFilter, optional) — Optional allow-list filter applied to the response before the LLM sees it, so large responses don't pollute the context. Defaults to the full response.
- `content_type` (enum, optional, default: application/json) — Content type for the request body. Only applies to POST/PUT/PATCH requests.
  - Allowed values: `application/json`, `application/x-www-form-urlencoded`
- `auth_resolved_params` (list of string, optional) — URL placeholders resolved from the auth connection (e.g. secrets injected via UrlSecretAuthConnection) rather than from path_params_schema.
- `auth_connection` (WebhookToolApiSchemaConfigOutputAuthConnection, optional) — Optional auth connection to use for authentication with this webhook

### ConversationHistoryTranscriptSystemToolResultCommonModelInputResult

- `result_type`: `dummy`
- `result_type`: `end_call_success`
  - `message` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `end_procedure_error`
  - `message` (string, required)
  - `status` (enum, required)
    - Allowed values: `not_found`, `invalid_id`
  - `procedure_id` (string, optional)
- `result_type`: `end_procedure_success`
  - `procedure_id` (string, required)
  - `procedure_name` (string, required)
  - `message` (string, optional, default: )
  - `status` ("success", optional)
- `result_type`: `knowledge_base_rag_success`
  - `chunk_count` (integer, optional, default: 0) — Number of relevant chunks retrieved
  - `chunks` (list of KnowledgeBaseRagChunkModel, optional) — Retrieved chunks; populated only in the rag-result-in-tool-result mode
  - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
  - `status` (enum, optional, default: success)
    - Allowed values: `success`, `no_documents`, `no_results`
- `result_type`: `knowledge_base_success`
  - `chunk_count` (integer, optional, default: 0)
  - `message` (string, optional, default: Referenced knowledge base.)
  - `status` (enum, optional, default: success)
    - Allowed values: `success`, `no_matching_documents`, `no_results`
- `result_type`: `language_detection_success`
  - `language` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `play_dtmf_error`
  - `error` (string, required)
  - `details` (string, optional)
  - `status` ("error", optional)
- `result_type`: `play_dtmf_success`
  - `dtmf_tones` (string, required)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `skip_turn_success`
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `start_procedure_error`
  - `message` (string, required)
  - `status` (enum, required)
    - Allowed values: `not_found`, `invalid_name`, `already_active`
  - `procedure_id` (string, optional)
- `result_type`: `start_procedure_success`
  - `procedure_id` (string, required)
  - `procedure_name` (string, required)
  - `message` (string, optional, default: Procedure is now started. Follow its instructions from the <active-procedures> section of your system prompt.)
  - `procedure_entry_workflow_node` (string, optional)
  - `procedure_return_workflow_node` (string, optional)
  - `status` ("success", optional)
- `result_type`: `testing_tool_result`
  - `reason` (string, optional, default: Skipping tool call in test mode)
  - `status` ("success", optional)
- `result_type`: `transfer_to_agent_error`
  - `error` (string, required)
  - `from_agent` (string, required)
  - `status` ("error", optional)
- `result_type`: `transfer_to_agent_success`
  - `condition` (string, required)
  - `from_agent` (string, required)
  - `to_agent` (string, required)
  - `branch_info` (TransferToAgentToolResultSuccessModelInputBranchInfo, optional)
  - `delay_ms` (integer, optional, default: 0)
  - `enable_transferred_agent_first_message` (boolean, optional, default: false)
  - `preserve_client_tts_overrides` (boolean, optional, default: false)
  - `status` ("success", optional)
  - `to_node` (string, optional)
  - `transfer_message` (string, optional)
- `result_type`: `transfer_to_number_error`
  - `error` (string, required)
  - `details` (string, optional)
  - `status` ("error", optional)
- `result_type`: `transfer_to_number_exotel_success`
  - `transfer_number` (string, required)
  - `agent_message` (string, optional)
  - `note` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `transfer_to_number_sip_success`
  - `transfer_number` (string, required)
  - `note` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `transfer_to_number_twilio_success`
  - `agent_message` (string, required)
  - `conference_name` (string, required)
  - `transfer_number` (string, required)
  - `client_message` (string, optional)
  - `note` (string, optional)
  - `post_dial_digits` (string, optional)
  - `reason` (string, optional)
  - `status` ("success", optional)
- `result_type`: `voicemail_detection_success`
  - `reason` (string, optional)
  - `status` ("success", optional)
  - `voicemail_message` (string, optional)

### WorkflowToolResponseModelInput

A common model for workflow tool responses.

- `steps` (list of WorkflowToolResponseModelInputStepsItem, optional)

### KnowledgeBaseRagChunkModel

- `chunk_id` (string, required)
- `document_id` (string, required)
- `content` (string, required)

### TransferToAgentToolResultSuccessModelOutputBranchInfo

- `branch_reason`: `defaulting_to_main`
  - `branch_id` (string, required)
- `branch_reason`: `traffic_split`
  - `branch_id` (string, required)
  - `traffic_percentage` (double, required)

### WorkflowToolResponseModelOutputStepsItem

- `type`: `edge`
  - `edge_id` (string, required)
  - `step_latency_secs` (double, required)
  - `target_node_id` (string, required)
- `type`: `max_iterations_exceeded`
  - `max_iterations` (integer, required)
  - `step_latency_secs` (double, required)
- `type`: `nested_tools`
  - `is_successful` (boolean, required)
  - `node_id` (string, required)
  - `requests` (list of ConversationHistoryTranscriptToolCallCommonModelOutput, required)
  - `results` (list of WorkflowToolNestedToolsStepModelOutputResultsItem, required)
  - `step_latency_secs` (double, required)

### ConvAiSecretLocator

Used to reference a secret from the agent's secret store.

- `secret_id` (string, required)

### ConvAiEnvVarLocator

Used to reference an environment variable by label.

- `env_var_label` (string, required)

### AuthConnectionLocator

Used to reference an auth connection from the workspace's auth connection store.

- `auth_connection_id` (string, required)

### EnvironmentAuthConnectionLocator

References an environment variable of type 'auth_connection' by label. At runtime, resolves to the auth connection for the current environment, falling back to the default environment.

- `env_var_label` (string, required)

### ConvAiDynamicVariable

Used to reference a dynamic variable.

- `variable_name` (string, required)

### ApiIntegrationWebhookOverridesSchemaOverridesValue

- `source`: `constant`
  - `constant_value` (ConstantSchemaOverrideConstantValue, optional) — The constant value to use
- `source`: `dynamic_variable`
  - `dynamic_variable` (string, required) — The name of the dynamic variable to use
- `source`: `llm`
  - `prompt` (string, optional) — Prompt override for the LLM. If not provided, the original schema description is used.
- `source`: `omit`

### ApiIntegrationWebhookOverridesRequestHeadersValue

### ObjectJsonSchemaPropertyOutputPropertiesValue

### RequiredConstraints

Wrapper for anyOf/allOf composition constraints scoped to required fields.

- `any_of` (list of RequiredConstraint, optional)
- `all_of` (list of RequiredConstraint, optional)

### EndProcedureToolConfigProceduresValue

### StartProcedureToolConfigProceduresValue

### AgentTransferOutput

- `condition` (string, required)
- `agent_id` (string, optional)
- `node_id` (string, optional)
- `delay_ms` (integer, optional, default: 0)
- `transfer_message` (string, optional)
- `enable_transferred_agent_first_message` (boolean, optional, default: false)
- `is_workflow_node_transfer` (boolean, optional, default: false)
- `preserve_client_tts_overrides` (boolean, optional, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.

### PhoneNumberTransfer

- `transfer_destination` (PhoneNumberTransferTransferDestination, required)
- `condition` (string, required)
- `custom_sip_headers` (list of PhoneNumberTransferCustomSipHeadersItem, optional) — Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.
- `transfer_type` (enum, optional, default: conference)
  - Allowed values: `blind`, `conference`, `sip_refer`
- `sip_refer_play_dialtone` (boolean, optional, default: true) — When True, a ringing tone is played on the original call leg while a SIP REFER transfer completes. The tone is carried over RTP to the SIP peer executing the REFER, so disable this if the receiving system (e.g. an SBC or contact center) should not hear it. When disabled the caller hears silence until the transfer completes. SIP REFER transfers only.
- `uui` (UuiTransferConfig, optional) — User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.
- `post_dial_digits` (PhoneNumberTransferPostDialDigits, optional) — DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.
- `phone_number` (string, optional, deprecated)

### WebhookToolApiSchemaConfigOutputRequestHeadersValue

### QueryParamsJsonSchemaOutput

- `properties` (map from string to LiteralJsonSchemaProperty, required)
- `required` (list of string, optional)

### ResponseFilter

Configuration for filtering tool responses before they are visible to the agent.

- `mode` (enum, optional, default: all) — Controls how tool responses are filtered. 'all' returns entire response, 'allow' returns only specified paths, 'hide_all' hides the entire response.
  - Allowed values: `all`, `allow`, `hide_all`
- `filters` (list of string, optional) — Dot notation paths to include when mode is 'allow' (e.g., ['ticket.id', 'ticket.status']).
- `content_type` ("application/json", optional) — Content type for response filtering. Only 'application/json' responses are filtered.

### WebhookToolApiSchemaConfigOutputAuthConnection

Optional auth connection to use for authentication with this webhook

### TransferToAgentToolResultSuccessModelInputBranchInfo

- `branch_reason`: `defaulting_to_main`
  - `branch_id` (string, required)
- `branch_reason`: `traffic_split`
  - `branch_id` (string, required)
  - `traffic_percentage` (double, required)

### WorkflowToolResponseModelInputStepsItem

- `type`: `edge`
  - `edge_id` (string, required)
  - `step_latency_secs` (double, required)
  - `target_node_id` (string, required)
- `type`: `max_iterations_exceeded`
  - `max_iterations` (integer, required)
  - `step_latency_secs` (double, required)
- `type`: `nested_tools`
  - `is_successful` (boolean, required)
  - `node_id` (string, required)
  - `requests` (list of ConversationHistoryTranscriptToolCallCommonModelInput, required)
  - `results` (list of WorkflowToolNestedToolsStepModelInputResultsItem, required)
  - `step_latency_secs` (double, required)

### WorkflowToolNestedToolsStepModelOutputResultsItem

### ConstantSchemaOverrideConstantValue

The constant value to use

### ArrayJsonSchemaPropertyOutput

- `description` (string, optional, default: )
- `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
- `constant_value` (list of any, optional) — When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
- `type` ("array", optional)
- `items` (ArrayJsonSchemaPropertyOutputItems, optional) — Schema for array elements.

### RequiredConstraint

A set of fields that must all be present to satisfy this constraint.

- `required` (list of string, required)

### ProcedureVersionRef

- `procedure_id` (string, required) — Procedure ID
- `version_id` (string, required) — Version ID of the procedure version.

### ProcedureDraftRef

- `procedure_id` (string, required) — Procedure ID
- `version_id` (any, optional)

### PhoneNumberTransferTransferDestination

- `type`: `phone`
  - `phone_number` (string, required)
- `type`: `phone_dynamic_variable`
  - `phone_number` (string, required)
- `type`: `sip_uri`
  - `sip_uri` (string, required)
- `type`: `sip_uri_dynamic_variable`
  - `sip_uri` (string, required)

### PhoneNumberTransferCustomSipHeadersItem

- `type`: `dynamic`
  - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
  - `value` (string, required) — The dynamic variable name to resolve
- `type`: `static`
  - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
  - `value` (string, required) — The header value

### UuiTransferConfig

User-to-User Information envelope for SIP REFER transfers (RFC 7433). Outbound payloads are hex-encoded (the only encoding RFC 7433 defines). The protocol discriminator axis lets per-platform formats (Talkdesk, Genesys, ...) be expressed by configuration rather than scattered transfer flags. Further axes (ASCII encoding, header name, purpose/content parameters) can be added here without touching the transfer model.

- `data` (string, required) — UUI payload to send on SIP REFER transfers. Supports inline dynamic variables and is hex-encoded at transfer time.
- `protocol_discriminator` (string, optional) — Optional one-octet protocol discriminator (two hex digits, e.g. '00'). Required by platforms such as Genesys Cloud, which otherwise strip the first octet of the payload. Leave unset for platforms like Talkdesk that expect a bare hex payload.
- `protocol_discriminator_mode` (enum, optional, default: prefix) — How to attach protocol\_discriminator. 'prefix' prepends the octet to the hex payload (User-to-User=XX\<hex>;encoding=hex). 'pd\_parameter' sends it as a separate parameter (User-to-User=\<hex>;pd=XX;encoding=hex). Ignored when protocol\_discriminator is unset.
  - Allowed values: `prefix`, `pd_parameter`

### PhoneNumberTransferPostDialDigits

- `type`: `dynamic`
  - `value` (string, required) — The dynamic variable name to resolve
- `type`: `static`
  - `value` (string, required) — DTMF digits to send after call connects (e.g., 'ww1234' for extension)

### WorkflowToolNestedToolsStepModelInputResultsItem

### ArrayJsonSchemaPropertyOutputItems

Schema for array elements.

## Examples

**Request**

```json
{
  "simulation_specification": {
    "simulated_user_config": {
      "first_message": "Hello, how can I help you today?",
      "language": "en",
      "disable_first_message_interruptions": false
    }
  }
}
```

**Response**

```json
{
  "simulated_conversation": [
    {
      "role": "user",
      "time_in_call_secs": 1,
      "agent_metadata": {
        "agent_id": "agent_id"
      },
      "message": "message",
      "multivoice_message": {
        "parts": [
          {
            "text": "text",
            "voice_label": null,
            "time_in_call_secs": null
          }
        ]
      },
      "tool_calls": [
        {
          "request_id": "request_id",
          "tool_name": "tool_name",
          "params_as_json": "params_as_json",
          "tool_has_been_called": true
        }
      ],
      "tool_results": [
        {
          "is_error": true,
          "request_id": "request_id",
          "result_value": "result_value",
          "tool_has_been_called": true,
          "tool_name": "tool_name"
        }
      ],
      "feedback": {
        "score": "like",
        "time_in_call_secs": 1
      },
      "llm_override": "llm_override",
      "producing_llm": "producing_llm",
      "rag_retrieval_info": {
        "chunks": [
          {
            "document_id": "document_id",
            "chunk_id": "chunk_id",
            "vector_distance": 1.1
          }
        ],
        "embedding_model": "e5_mistral_7b_instruct",
        "retrieval_query": "retrieval_query",
        "rag_latency_secs": 1.1
      },
      "interrupted": true,
      "ignored_as_backchannel": true,
      "original_message": "original_message",
      "reasoning": [
        {}
      ],
      "source_medium": "audio",
      "source_event_id": 1,
      "used_static_kb_document_ids": [
        "used_static_kb_document_ids"
      ],
      "user_identifier": "user_identifier",
      "id": "id",
      "triggered_guardrails": [
        {
          "guardrail_type": "custom"
        }
      ],
      "file_input": {
        "file_id": "file_id",
        "original_filename": "original_filename",
        "mime_type": "mime_type",
        "file_url": "file_url"
      },
      "file_inputs": [
        {
          "file_id": "file_id",
          "original_filename": "original_filename",
          "mime_type": "mime_type",
          "file_url": "file_url"
        }
      ],
      "contextual_update_info": {
        "context_id": "context_id"
      },
      "reasoned": true
    }
  ],
  "analysis": {
    "call_successful": "success",
    "transcript_summary": "transcript_summary",
    "evaluation_criteria_results": {
      "key": {
        "criteria_id": "criteria_id",
        "result": "success",
        "rationale": "rationale"
      }
    },
    "data_collection_results": {
      "key": {
        "data_collection_id": "data_collection_id",
        "rationale": "rationale",
        "json_schema": {
          "type": "string",
          "description": "A user-provided message"
        }
      }
    },
    "evaluation_criteria_results_list": [
      {
        "criteria_id": "criteria_id",
        "result": "success",
        "rationale": "rationale"
      }
    ],
    "data_collection_results_list": [
      {
        "data_collection_id": "data_collection_id",
        "rationale": "rationale",
        "json_schema": {
          "type": "string",
          "description": "A user-provided message"
        }
      }
    ],
    "call_success_score": 1.1,
    "call_summary_title": "call_summary_title",
    "scoped": [
      {
        "scope": "conversation",
        "source_agent_id": "source_agent_id",
        "successful": "success"
      }
    ]
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.simulateConversation("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        simulationSpecification: {
            simulatedUserConfig: {
                firstMessage: "Hello, how can I help you today?",
                language: "en",
                disableFirstMessageInterruptions: false,
            },
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, ConversationSimulationSpecification, AgentConfig

client = ElevenLabs()

client.conversational_ai.agents.simulate_conversation(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    simulation_specification=ConversationSimulationSpecification(
        simulated_user_config=AgentConfig(
            first_message="Hello, how can I help you today?",
            language="en",
            disable_first_message_interruptions=False,
        ),
    ),
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation"

	payload := strings.NewReader("{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation")
  .header("Content-Type", "application/json")
  .body("{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation', [
  'body' => '{
  "simulation_specification": {
    "simulated_user_config": {
      "first_message": "Hello, how can I help you today?",
      "language": "en",
      "disable_first_message_interruptions": false
    }
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["simulation_specification": ["simulated_user_config": [
      "first_message": "Hello, how can I help you today?",
      "language": "en",
      "disable_first_message_interruptions": false
    ]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
