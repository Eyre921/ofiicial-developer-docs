---
title: "Get test invocation"
source: https://elevenlabs.io/docs/api-reference/tests/test-invocations/get.md
path: docs/api-reference/tests/test-invocations/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get test invocation

GET https://api.elevenlabs.io/v1/convai/test-invocations/{test_invocation_id}

Gets a test invocation by ID.

Reference: https://elevenlabs.io/docs/api-reference/tests/test-invocations/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `test_invocation_id` (string, required) — The id of a test invocation. This is returned when tests are run.

## Response

### 200

Successful Response

- `id` (string, required)
- `test_runs` (list of UnitTestRunResponseModel, required)
- `agent_id` (string, optional, nullable)
- `branch_id` (string, optional, nullable)
- `version_id` (string, optional, nullable)
- `ran_against_draft` (boolean, optional, default: false)
- `created_at` (integer, optional)
- `folder_id` (string, optional, nullable)
- `repeat_count` (integer, optional, default: 1)
- `bucketing_status` (enum, optional, nullable) — None when repeat_count==1 (no bucketing). Otherwise tracks bucketing lifecycle.
  - Allowed values: `pending`, `completed`, `failed`
- `result_groups` (list of TestRunResultSummary, optional)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### UnitTestRunResponseModel

- `test_run_id` (string, required)
- `test_invocation_id` (string, required)
- `agent_id` (string, required)
- `status` (enum, required)
  - Allowed values: `pending`, `passed`, `failed`
- `test_id` (string, required)
- `test_info` (UnitTestRunResponseModelTestInfo, optional, nullable)
- `branch_id` (string, optional, nullable)
- `version_id` (string, optional, nullable)
- `ran_against_draft` (boolean, optional, default: false)
- `workflow_node_id` (string, optional, nullable)
- `agent_responses` (list of ConversationHistoryTranscriptCommonModel-Output, optional, nullable)
- `test_name` (string, optional, default: Unknown Test)
- `condition_result` (TestConditionResultCommonModel, optional, nullable)
- `last_updated_at_unix` (integer, optional)
- `metadata` (TestRunMetadata, optional, nullable)
- `root_folder_id` (string, optional, nullable)
- `root_folder_name` (string, optional, nullable)
- `environment` (string, optional, nullable)
- `credits_used` (integer, optional, nullable) — Credits billed for this test run. None for runs created before cost tracking.
- `charging` (ConversationChargingCommonModel, optional, nullable) — Finalized billing and provider-usage breakdown for this test run.

### TestRunResultSummary

- `test_id` (string, required)
- `test_name` (string, required)
- `buckets` (list of TestRunResultBucket, required)
- `workflow_node_id` (string, optional, nullable)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### UnitTestRunResponseModelTestInfo

- `type`: `llm` (ResponseUnitTestModel)
  - `chat_history` (list of ConversationHistoryTranscriptCommonModel-Output, optional)
  - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
  - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
  - `failure_examples` (list of AgentFailureResponseExample, optional) — Non-empty list of example responses that should be considered failures
  - `from_conversation_metadata` (TestFromConversationMetadata-Output, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
  - `success_condition` (string, optional, default: ) — A prompt that evaluates whether the agent's response is successful. Should return True or False.
  - `success_examples` (list of AgentSuccessfulResponseExample, optional) — Non-empty list of example responses that should be considered successful
- `type`: `simulation` (SimulationTestModel)
  - `chat_history` (list of ConversationHistoryTranscriptCommonModel-Output, optional)
  - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
  - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
  - `evaluation_model` (enum, optional, nullable, default: claude-sonnet-4-6) — LLM model to use for evaluating simulation results.
    - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
  - `from_conversation_metadata` (TestFromConversationMetadata-Output, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
  - `simulated_user_model` (enum, optional, nullable, default: claude-sonnet-4-6) — LLM model for the simulated user.
    - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
  - `simulation_environment` (string, optional, nullable) — The environment to use when running this simulation test. If not provided, defaults to 'production'.
  - `simulation_max_turns` (integer, optional, default: 5) — Maximum number of conversation turns for simulation tests.
  - `simulation_scenario` (string, optional, default: ) — Description of the simulation scenario and user persona for simulation tests.
  - `success_conditions` (list of string, optional) — List of prompts that evaluate whether the simulation was successful. If provided, all criteria are evaluated and merged into a final result. Capped at the maximum number of evaluation criteria.
  - `tool_mock_config` (SimulationToolMockBehaviorConfig, optional) — Configuration for which tools to mock and fallback behavior.
  - `tool_mock_overrides` (map from string to list of ToolResponseMockConfig-Output, optional) — Test-specific response mocks, keyed by tool ID. Applied ahead of the tool's shared mocks and only within this test. Only take effect for tools that are mocked (see tool_mock_config).
  - `success_condition` (string, optional, nullable, deprecated) — Deprecated legacy single success criterion. Use success_conditions instead. At least one of success_condition or success_conditions is required.
- `type`: `tool` (ToolCallUnitTestModel)
  - `chat_history` (list of ConversationHistoryTranscriptCommonModel-Output, optional)
  - `check_any_tool_matches` (boolean, optional, nullable) — If set to True this test will pass if any tool call returned by the LLM matches the criteria. Otherwise it will fail if more than one tool is returned by the agent.
  - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
  - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
  - `from_conversation_metadata` (TestFromConversationMetadata-Output, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
  - `tool_call_parameters` (UnitTestToolCallEvaluationModel-Output, optional, nullable) — How to evaluate the agent's tool call (if any). If empty, the tool call is not evaluated.

### ConversationHistoryTranscriptCommonModel-Output

- `role` (enum, required)
  - Allowed values: `user`, `agent`
- `time_in_call_secs` (integer, required)
- `agent_metadata` (AgentMetadata, optional, nullable)
- `message` (string, optional, nullable)
- `multivoice_message` (ConversationHistoryMultivoiceMessageModel, optional, nullable) — Represents a message from a multi-voice agent.
- `tool_calls` (list of ConversationHistoryTranscriptToolCallCommonModel-Output, optional)
- `tool_results` (list of ConversationHistoryTranscriptCommonModelOutputToolResultsItems, optional)
- `feedback` (UserFeedback, optional, nullable)
- `llm_override` (string, optional, nullable)
- `producing_llm` (string, optional, nullable)
- `conversation_turn_metrics` (ConversationTurnMetrics, optional, nullable)
- `rag_retrieval_info` (RagRetrievalInfo, optional, nullable)
- `llm_usage` (LLMUsage-Output, optional, nullable)
- `interrupted` (boolean, optional, default: false)
- `ignored_as_backchannel` (boolean, optional, default: false)
- `original_message` (string, optional, nullable)
- `reasoning` (list of ConversationReasoningModel, optional)
- `source_medium` (enum, optional, nullable)
  - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
- `source_event_id` (integer, optional, nullable)
- `used_static_kb_document_ids` (list of string, optional)
- `user_identifier` (string, optional, nullable)
- `id` (string, optional, nullable)
- `triggered_guardrails` (list of TriggeredGuardrailCommonModel, optional)

### TestConditionResultCommonModel

- `result` (enum, required)
  - Allowed values: `success`, `failure`, `unknown`
- `rationale` (TestConditionRationaleCommonModel, optional, nullable) — Structured rationale for test condition results containing individual failure/success reasons.

### TestRunMetadata

- `workspace_id` (string, required)
- `test_name` (string, required)
- `ran_by_user_email` (string, required)
- `test_type` (enum, optional, default: llm)
  - Allowed values: `llm`, `tool_call`, `simulation`

### ConversationChargingCommonModel

- `dev_discount` (boolean, optional, default: false)
- `is_burst` (boolean, optional, default: false)
- `tier` (string, optional, nullable)
- `llm_usage` (LLMCategoryUsage, optional)
- `llm_price` (double, optional, nullable)
- `llm_charge` (integer, optional, nullable)
- `call_charge` (integer, optional, nullable)
- `platform_charge` (integer, optional, nullable)
- `platform_usage` (PlatformUsage, optional) — Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``).
- `platform_price` (double, optional, nullable)
- `free_minutes_consumed` (double, optional, default: 0)
- `free_llm_dollars_consumed` (double, optional, default: 0)
- `tts_usage` (ConversationTTSUsageModel, optional, nullable) — Aggregated TTS usage for a conversation (analytics-only, not billing).
- `asr_usage` (ConversationASRUsageModel, optional, nullable) — Aggregated ASR usage for a conversation (analytics-only, not billing).
- `analysis` (AnalysisCharging, optional, nullable) — Cost of running post-call analysis on this conversation. Present once an analysis pass has run, billed or not.

### TestRunResultBucket

- `test_run_ids` (list of string, required)
- `title` (string, required) — Short one-line title for this bucket
- `reason` (string, required) — Short summary of why the test runs in this bucket passed or failed
- `status` (enum, required)
  - Allowed values: `pending`, `passed`, `failed`

### ValidationErrorLocItems

### AgentFailureResponseExample

- `response` (string, required)
- `type` ("failure", required)

### TestFromConversationMetadata-Output

- `conversation_id` (string, required)
- `agent_id` (string, required)
- `branch_id` (string, optional, nullable)
- `workflow_node_id` (string, optional, nullable)
- `original_agent_reply` (list of ConversationHistoryTranscriptCommonModel-Output, optional, default: [])

### AgentSuccessfulResponseExample

- `response` (string, required)
- `type` ("success", required)

### SimulationToolMockBehaviorConfig

Simulation/preview-side config: tools are identified by IDs, resolved to names at runtime.

- `mocking_strategy` (enum, optional, default: none) — Which tools to mock: 'all' mocks every mockable tool, 'selected' mocks only those in mocked_tool_names/mocked_tool_ids, 'none' disables mocking.
  - Allowed values: `all`, `selected`, `none`
- `fallback_strategy` (enum, optional, default: raise_error) — Behavior when no mock matches a tool call.
  - Allowed values: `call_real_tool`, `raise_error`
- `mocked_tool_ids` (list of string, optional) — Tool IDs to mock. Resolved to tool names before being passed to the orchestrator.

### ToolResponseMockConfig-Output

- `mock_result` (string, required) — The return value the LLM sees when this mock is active.
- `parameter_conditions` (list of UnitTestToolCallParameter, optional) — If the list is empty, the mock will always activate.
- `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.

### UnitTestToolCallEvaluationModel-Output

- `parameters` (list of UnitTestToolCallParameter, optional) — Parameters to evaluate for the agent's tool call. If empty, the tool call parameters are not evaluated.
- `referenced_tool` (ReferencedToolCommonModel, optional, nullable) — The tool to evaluate a call against.
- `verify_absence` (boolean, optional, default: false) — Whether to verify that the tool was NOT called.
- `workflow_node_transition` (UnitTestWorkflowNodeTransitionEvaluationNodeId, optional, nullable) — Configuration for testing workflow node transitions. When set, the test will verify the agent transitions to the specified workflow node.

### AgentMetadata

- `agent_id` (string, required)
- `branch_id` (string, optional, nullable)
- `workflow_node_id` (string, optional, nullable)
- `version_id` (string, optional, nullable)

### ConversationHistoryMultivoiceMessageModel

Represents a message from a multi-voice agent.

- `parts` (list of ConversationHistoryMultivoiceMessagePartModel, required)

### ConversationHistoryTranscriptToolCallCommonModel-Output

- `request_id` (string, required)
- `tool_name` (string, required)
- `params_as_json` (string, required)
- `tool_has_been_called` (boolean, required)
- `type` (enum, optional, nullable)
  - Allowed values: `system`, `webhook`, `client`, `mcp`, `workflow`, `api_integration_webhook`, `api_integration_mcp`, `smb`
- `tool_details` (ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails, optional, nullable)

### ConversationHistoryTranscriptCommonModelOutputToolResultsItems

### UserFeedback

- `score` (enum, required)
  - Allowed values: `like`, `dislike`
- `time_in_call_secs` (integer, required)

### ConversationTurnMetrics

- `metrics` (map from string to MetricRecord, optional)
- `convai_asr_provider` (string, optional, nullable)
- `convai_tts_model` (string, optional, nullable)
- `convai_tts_cascade` (string, optional, nullable)

### RagRetrievalInfo

- `chunks` (list of RagChunkMetadata, required)
- `embedding_model` (enum, required, default: e5_mistral_7b_instruct)
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
- `retrieval_query` (string, required)
- `rag_latency_secs` (double, required)
- `used_chunk_ids` (list of string, optional)

### LLMUsage-Output

- `model_usage` (map from string to LLMInputOutputTokensUsage, optional)

### ConversationReasoningModel

- `summary` (string, optional, nullable)
- `provider_redact` (boolean, optional, default: false)

### TriggeredGuardrailCommonModel

- `guardrail_type` (enum, required)
  - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
- `guardrail_name` (string, optional, nullable)

### TestConditionRationaleCommonModel

Structured rationale for test condition results containing individual failure/success reasons.

- `messages` (list of string, optional) — List of individual parameter evaluation messages or reasons
- `summary` (string, optional, default: ) — High-level summary of the evaluation result

### LLMCategoryUsage

- `irreversible_generation` (LLMUsage-Output, optional)
- `initiated_generation` (LLMUsage-Output, optional)

### PlatformUsage

Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``).

- `category_usage` (map from string to PlatformCategoryUsage, optional)

### ConversationTTSUsageModel

Aggregated TTS usage for a conversation (analytics-only, not billing).

- `primary_tts_model` (string, optional, nullable)
- `total_audio_output_seconds` (double, optional, default: 0)
- `total_characters` (integer, optional, default: 0)
- `per_voice_usage` (list of ConversationVoiceUsageModel, optional)

### ConversationASRUsageModel

Aggregated ASR usage for a conversation (analytics-only, not billing).

- `asr_model` (string, optional, nullable)
- `total_transcription_calls` (integer, optional, default: 0)
- `total_audio_input_seconds` (double, optional, default: 0)

### AnalysisCharging

Cost of running post-call analysis on this conversation. Present once an analysis pass has run, billed or not.

- `total` (AnalysisRunningTotal, required) — Cumulative LLM cost of running post-call analysis on this conversation.
- `last_run` (AnalysisRunSnapshot, required) — LLM cost of the most recent post-call analysis pass on this conversation.

### UnitTestToolCallParameter

- `eval` (UnitTestToolCallParameterEval, required)
- `path` (string, required)

### ReferencedToolCommonModel

Reference to a tool for unit test evaluation.

- `id` (string, required) — The ID of the tool
- `type` (enum, required) — The type of the tool
  - Allowed values: `system`, `webhook`, `client`, `workflow`, `api_integration_webhook`, `mcp`, `code`

### UnitTestWorkflowNodeTransitionEvaluationNodeId

- `agent_id` (string, required) — The ID of the agent whose workflow contains the target node.
- `target_node_id` (string, required) — The ID of the workflow node that the agent should transition to.
- `type` ("node_id", optional, default: node_id)

### ConversationHistoryMultivoiceMessagePartModel

Represents a single voice part of a multi-voice message.

- `text` (string, required)
- `voice_label` (string, required, nullable)
- `time_in_call_secs` (integer, required, nullable)

### ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails

- `type`: `api_integration_webhook` (ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetails)
  - `credential_id` (string, required, default: )
  - `integration_connection_id` (string, required, default: )
  - `integration_id` (string, required, default: )
  - `webhook_details` (ConversationHistoryTranscriptToolCallWebhookDetails, required)
- `type`: `client` (ConversationHistoryTranscriptToolCallClientDetails)
  - `parameters` (string, required)
- `type`: `mcp` (ConversationHistoryTranscriptToolCallMCPDetails)
  - `approval_policy` (string, required)
  - `integration_type` (string, required)
  - `mcp_server_id` (string, required)
  - `mcp_server_name` (string, required)
  - `mcp_tool_description` (string, optional, default: )
  - `mcp_tool_name` (string, optional, default: )
  - `parameters` (map from string to string, optional)
  - `requires_approval` (boolean, optional, default: false)
- `type`: `webhook` (ConversationHistoryTranscriptToolCallWebhookDetails)
  - `method` (string, required)
  - `url` (string, required)
  - `body` (string, optional, nullable)
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
- `type` (enum, optional, nullable)
  - Allowed values: `client`, `webhook`, `mcp`, `code`

### ConversationHistoryTranscriptSystemToolResultCommonModel-Output

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
- `result` (ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult, optional, nullable)

### ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Output

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

### ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Output

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
- `result` (WorkflowToolResponseModel-Output, optional, nullable) — A common model for workflow tool responses.

### MetricRecord

- `elapsed_time` (double, required)

### RagChunkMetadata

- `document_id` (string, required)
- `chunk_id` (string, required)
- `vector_distance` (double, required)

### LLMInputOutputTokensUsage

- `input` (LLMTokensCategoryUsage, optional)
- `input_cache_read` (LLMTokensCategoryUsage, optional)
- `input_cache_write` (LLMTokensCategoryUsage, optional)
- `output_total` (LLMTokensCategoryUsage, optional)

### PlatformCategoryUsage

Accumulated charge for a single :class:`PlatformCategory`.

- `credits` (integer, optional, default: 0)
- `price` (double, optional, default: 0)
- `quantity` (double, optional, default: 0)

### ConversationVoiceUsageModel

- `voice_id` (string, required)
- `audio_output_seconds` (double, optional, default: 0)

### AnalysisRunningTotal

Cumulative LLM cost of running post-call analysis on this conversation.

- `price` (double, optional, default: 0)
- `charge` (integer, optional, default: 0)
- `runs` (integer, optional, default: 0)
- `price_per_feature` (map from string to double, optional)
- `charge_per_feature` (map from string to integer, optional)

### AnalysisRunSnapshot

LLM cost of the most recent post-call analysis pass on this conversation.

- `price` (double, optional, default: 0)
- `charge` (integer, optional, default: 0)
- `price_per_feature` (map from string to double, optional)
- `charge_per_feature` (map from string to integer, optional)

### UnitTestToolCallParameterEval

- `type`: `anything` (MatchAnythingParameterEvaluationStrategy)
- `type`: `exact` (ExactParameterEvaluationStrategy)
  - `expected_value` (string, required) — The exact string value that the parameter must match.
- `type`: `llm` (LLMParameterEvaluationStrategy)
  - `description` (string, required) — A description of the evaluation strategy to use for the test.
- `type`: `regex` (RegexParameterEvaluationStrategy)
  - `pattern` (string, required) — A regex pattern to match the agent's response against.

### ConversationHistoryTranscriptToolCallWebhookDetails

- `method` (string, required)
- `url` (string, required)
- `headers` (map from string to string, optional)
- `path_params` (map from string to string, optional)
- `query_params` (map from string to string, optional)
- `body` (string, optional, nullable)

### DynamicVariableUpdateCommonModel

Tracks a dynamic variable update that occurred during tool execution.

- `variable_name` (string, required)
- `old_value` (string, required, nullable)
- `new_value` (string, required)
- `updated_at` (double, required)
- `tool_name` (string, required)
- `tool_request_id` (string, required)

### ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult

- `result_type`: `dummy` (DummyToolResultModel)
- `result_type`: `end_call_success` (EndCallToolResultModel)
  - `message` (string, optional, nullable)
  - `reason` (string, optional, nullable)
  - `status` ("success", optional, default: success)
- `result_type`: `end_procedure_error` (EndProcedureToolResultErrorModel)
  - `message` (string, required)
  - `status` (enum, required)
    - Allowed values: `not_found`, `invalid_id`
  - `procedure_id` (string, optional, nullable)
- `result_type`: `end_procedure_success` (EndProcedureToolResultSuccessModel)
  - `procedure_id` (string, required)
  - `procedure_name` (string, required)
  - `message` (string, optional, default: )
  - `status` ("success", optional, default: success)
- `result_type`: `knowledge_base_rag_success` (KnowledgeBaseRagToolResultModel)
  - `chunk_count` (integer, optional, default: 0) — Number of relevant chunks retrieved
  - `chunks` (list of KnowledgeBaseRagChunkModel, optional) — Retrieved chunks; populated only in the rag-result-in-tool-result mode
  - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
  - `status` (enum, optional, default: success)
    - Allowed values: `success`, `no_documents`, `no_results`
- `result_type`: `knowledge_base_success` (KnowledgeBaseToolResultModel)
  - `chunk_count` (integer, optional, default: 0)
  - `message` (string, optional, default: Referenced knowledge base.)
  - `status` (enum, optional, default: success)
    - Allowed values: `success`, `no_matching_documents`, `no_results`
- `result_type`: `language_detection_success` (LanguageDetectionToolResultModel)
  - `language` (string, optional, nullable)
  - `reason` (string, optional, nullable)
  - `status` ("success", optional, default: success)
- `result_type`: `play_dtmf_error` (PlayDTMFResultErrorModel)
  - `error` (string, required)
  - `details` (string, optional, nullable)
  - `status` ("error", optional, default: error)
- `result_type`: `play_dtmf_success` (PlayDTMFResultSuccessModel)
  - `dtmf_tones` (string, required)
  - `reason` (string, optional, nullable)
  - `status` ("success", optional, default: success)
- `result_type`: `skip_turn_success` (SkipTurnToolResponseModel)
  - `reason` (string, optional, nullable)
  - `status` ("success", optional, default: success)
- `result_type`: `start_procedure_error` (StartProcedureToolResultErrorModel)
  - `message` (string, required)
  - `status` (enum, required)
    - Allowed values: `not_found`, `invalid_name`, `already_active`
  - `procedure_id` (string, optional, nullable)
- `result_type`: `start_procedure_success` (StartProcedureToolResultSuccessModel)
  - `procedure_id` (string, required)
  - `procedure_name` (string, required)
  - `message` (string, optional, default: Procedure is now started. Follow its instructions from the <active-procedures> section of your system prompt.)
  - `procedure_entry_workflow_node` (string, optional, nullable)
  - `procedure_return_workflow_node` (string, optional, nullable)
  - `status` ("success", optional, default: success)
- `result_type`: `testing_tool_result` (TestToolResultModel)
  - `reason` (string, optional, default: Skipping tool call in test mode)
  - `status` ("success", optional, default: success)
- `result_type`: `transfer_to_agent_error` (TransferToAgentToolResultErrorModel)
  - `error` (string, required)
  - `from_agent` (string, required)
  - `status` ("error", optional, default: error)
- `result_type`: `transfer_to_agent_success` (TransferToAgentToolResultSuccessModel)
  - `condition` (string, required)
  - `from_agent` (string, required)
  - `to_agent` (string, required)
  - `branch_info` (TransferToAgentToolResultSuccessModelOutputBranchInfo, optional, nullable)
  - `delay_ms` (integer, optional, default: 0)
  - `enable_transferred_agent_first_message` (boolean, optional, default: false)
  - `preserve_client_tts_overrides` (boolean, optional, default: false)
  - `status` ("success", optional, default: success)
  - `to_node` (string, optional, nullable)
  - `transfer_message` (string, optional, nullable)
- `result_type`: `transfer_to_number_error` (TransferToNumberResultErrorModel)
  - `error` (string, required)
  - `details` (string, optional, nullable)
  - `status` ("error", optional, default: error)
- `result_type`: `transfer_to_number_exotel_success` (TransferToNumberResultExotelSuccessModel)
  - `transfer_number` (string, required)
  - `agent_message` (string, optional, nullable)
  - `note` (string, optional, nullable)
  - `reason` (string, optional, nullable)
  - `status` ("success", optional, default: success)
- `result_type`: `transfer_to_number_sip_success` (TransferToNumberResultSipSuccessModel)
  - `transfer_number` (string, required)
  - `note` (string, optional, nullable)
  - `reason` (string, optional, nullable)
  - `status` ("success", optional, default: success)
- `result_type`: `transfer_to_number_twilio_success` (TransferToNumberResultTwilioSuccessModel)
  - `agent_message` (string, required)
  - `conference_name` (string, required)
  - `transfer_number` (string, required)
  - `client_message` (string, optional, nullable)
  - `note` (string, optional, nullable)
  - `post_dial_digits` (string, optional, nullable)
  - `reason` (string, optional, nullable)
  - `status` ("success", optional, default: success)
- `result_type`: `voicemail_detection_success` (VoiceMailDetectionResultSuccessModel)
  - `reason` (string, optional, nullable)
  - `status` ("success", optional, default: success)
  - `voicemail_message` (string, optional, nullable)

### WorkflowToolResponseModel-Output

A common model for workflow tool responses.

- `steps` (list of WorkflowToolResponseModelOutputStepsItems, optional)

### LLMTokensCategoryUsage

- `tokens` (integer, optional, default: 0)
- `price` (double, optional, default: 0)

### KnowledgeBaseRagChunkModel

- `chunk_id` (string, required)
- `document_id` (string, required)
- `content` (string, required)

### TransferToAgentToolResultSuccessModelOutputBranchInfo

- `branch_reason`: `defaulting_to_main` (TransferBranchInfoDefaultingToMain)
  - `branch_id` (string, required)
- `branch_reason`: `traffic_split` (TransferBranchInfoTrafficSplit)
  - `branch_id` (string, required)
  - `traffic_percentage` (double, required)

### WorkflowToolResponseModelOutputStepsItems

- `type`: `edge` (WorkflowToolEdgeStepModel)
  - `edge_id` (string, required)
  - `step_latency_secs` (double, required)
  - `target_node_id` (string, required)
- `type`: `max_iterations_exceeded` (WorkflowToolMaxIterationsExceededStepModel)
  - `max_iterations` (integer, required)
  - `step_latency_secs` (double, required)
- `type`: `nested_tools` (WorkflowToolNestedToolsStepModel)
  - `is_successful` (boolean, required)
  - `node_id` (string, required)
  - `requests` (list of ConversationHistoryTranscriptToolCallCommonModel-Output, required)
  - `results` (list of WorkflowToolResponseModelOutputStepsItemsDiscriminatorMappingNestedToolsResultsItems, required)
  - `step_latency_secs` (double, required)

### WorkflowToolResponseModelOutputStepsItemsDiscriminatorMappingNestedToolsResultsItems

## Examples

**Response**

```json
{
  "id": "string",
  "test_runs": [
    {
      "test_run_id": "string",
      "test_invocation_id": "string",
      "agent_id": "string",
      "status": "pending",
      "test_id": "string",
      "test_info": {
        "type": "llm",
        "chat_history": [
          {
            "role": "user",
            "time_in_call_secs": 1,
            "agent_metadata": {
              "agent_id": "string",
              "branch_id": "string",
              "workflow_node_id": "string",
              "version_id": "string"
            },
            "message": "string",
            "multivoice_message": {
              "parts": [
                {
                  "text": "string",
                  "voice_label": "string",
                  "time_in_call_secs": 1
                }
              ]
            },
            "tool_calls": [
              {
                "request_id": "string",
                "tool_name": "string",
                "params_as_json": "string",
                "tool_has_been_called": true,
                "type": "system",
                "tool_details": {
                  "type": "webhook",
                  "method": "string",
                  "url": "string",
                  "body": "string",
                  "headers": {},
                  "path_params": {},
                  "query_params": {}
                }
              }
            ],
            "tool_results": [
              {
                "dynamic_variable_updates": [
                  {
                    "new_value": "string",
                    "old_value": "string",
                    "tool_name": "string",
                    "tool_request_id": "string",
                    "updated_at": 1.1,
                    "variable_name": "string"
                  }
                ],
                "error_type": "",
                "is_blocked": false,
                "is_error": true,
                "raw_error_message": "",
                "request_id": "string",
                "result_value": "string",
                "tool_has_been_called": true,
                "tool_latency_secs": 0,
                "tool_name": "string",
                "type": "client"
              }
            ],
            "feedback": {
              "score": "like",
              "time_in_call_secs": 1
            },
            "llm_override": "string",
            "producing_llm": "string",
            "conversation_turn_metrics": {
              "metrics": {},
              "convai_asr_provider": "string",
              "convai_tts_model": "string",
              "convai_tts_cascade": "string"
            },
            "rag_retrieval_info": {
              "chunks": [
                {
                  "document_id": "string",
                  "chunk_id": "string",
                  "vector_distance": 1.1
                }
              ],
              "embedding_model": "e5_mistral_7b_instruct",
              "retrieval_query": "string",
              "rag_latency_secs": 1.1,
              "used_chunk_ids": [
                "string"
              ]
            },
            "llm_usage": {
              "model_usage": {}
            },
            "interrupted": false,
            "ignored_as_backchannel": false,
            "original_message": "string",
            "reasoning": [
              {
                "summary": "string",
                "provider_redact": false
              }
            ],
            "source_medium": "audio",
            "source_event_id": 1,
            "used_static_kb_document_ids": [
              "string"
            ],
            "user_identifier": "string",
            "id": "string",
            "triggered_guardrails": [
              {
                "guardrail_type": "custom",
                "guardrail_name": "string"
              }
            ]
          }
        ],
        "conversation_initiation_source": "unknown",
        "dynamic_variables": {},
        "environment": "string",
        "failure_examples": [
          {
            "response": "string",
            "type": "string"
          }
        ],
        "from_conversation_metadata": {
          "conversation_id": "string",
          "agent_id": "string",
          "branch_id": "string",
          "workflow_node_id": "string",
          "original_agent_reply": [
            {
              "role": "user",
              "time_in_call_secs": 1,
              "agent_metadata": {
                "agent_id": "string",
                "branch_id": "string",
                "workflow_node_id": "string",
                "version_id": "string"
              },
              "message": "string",
              "multivoice_message": {
                "parts": [
                  {
                    "text": "string",
                    "voice_label": "string",
                    "time_in_call_secs": 1
                  }
                ]
              },
              "tool_calls": [
                {
                  "request_id": "string",
                  "tool_name": "string",
                  "params_as_json": "string",
                  "tool_has_been_called": true,
                  "type": "system",
                  "tool_details": {
                    "type": "api_integration_webhook",
                    "credential_id": "",
                    "integration_connection_id": "",
                    "integration_id": "",
                    "webhook_details": {
                      "method": {},
                      "url": {},
                      "headers": {},
                      "path_params": {},
                      "query_params": {},
                      "body": {},
                      "type": {}
                    }
                  }
                }
              ],
              "tool_results": [
                {
                  "dynamic_variable_updates": [
                    {
                      "new_value": "string",
                      "old_value": "string",
                      "tool_name": "string",
                      "tool_request_id": "string",
                      "updated_at": 1.1,
                      "variable_name": "string"
                    }
                  ],
                  "error_type": "",
                  "is_blocked": false,
                  "is_error": true,
                  "raw_error_message": "",
                  "request_id": "string",
                  "result_value": "string",
                  "tool_has_been_called": true,
                  "tool_latency_secs": 0,
                  "tool_name": "string",
                  "type": "client"
                }
              ],
              "feedback": {
                "score": "like",
                "time_in_call_secs": 1
              },
              "llm_override": "string",
              "producing_llm": "string",
              "conversation_turn_metrics": {
                "metrics": {},
                "convai_asr_provider": "string",
                "convai_tts_model": "string",
                "convai_tts_cascade": "string"
              },
              "rag_retrieval_info": {
                "chunks": [
                  {
                    "document_id": "string",
                    "chunk_id": "string",
                    "vector_distance": 1.1
                  }
                ],
                "embedding_model": "e5_mistral_7b_instruct",
                "retrieval_query": "string",
                "rag_latency_secs": 1.1,
                "used_chunk_ids": [
                  "string"
                ]
              },
              "llm_usage": {
                "model_usage": {}
              },
              "interrupted": false,
              "ignored_as_backchannel": false,
              "original_message": "string",
              "reasoning": [
                {
                  "summary": "string",
                  "provider_redact": false
                }
              ],
              "source_medium": "audio",
              "source_event_id": 1,
              "used_static_kb_document_ids": [
                "string"
              ],
              "user_identifier": "string",
              "id": "string",
              "triggered_guardrails": [
                {
                  "guardrail_type": "custom",
                  "guardrail_name": "string"
                }
              ]
            }
          ]
        },
        "success_condition": "",
        "success_examples": [
          {
            "response": "string",
            "type": "string"
          }
        ]
      },
      "branch_id": "string",
      "version_id": "string",
      "ran_against_draft": false,
      "workflow_node_id": "string",
      "agent_responses": [
        {
          "role": "user",
          "time_in_call_secs": 1,
          "agent_metadata": {
            "agent_id": "string",
            "branch_id": "string",
            "workflow_node_id": "string",
            "version_id": "string"
          },
          "message": "string",
          "multivoice_message": {
            "parts": [
              {
                "text": "string",
                "voice_label": "string",
                "time_in_call_secs": 1
              }
            ]
          },
          "tool_calls": [
            {
              "request_id": "string",
              "tool_name": "string",
              "params_as_json": "string",
              "tool_has_been_called": true,
              "type": "system",
              "tool_details": {
                "type": "webhook",
                "method": "string",
                "url": "string",
                "body": "string",
                "headers": {},
                "path_params": {},
                "query_params": {}
              }
            }
          ],
          "tool_results": [
            {
              "dynamic_variable_updates": [
                {
                  "new_value": "string",
                  "old_value": "string",
                  "tool_name": "string",
                  "tool_request_id": "string",
                  "updated_at": 1.1,
                  "variable_name": "string"
                }
              ],
              "error_type": "",
              "is_blocked": false,
              "is_error": true,
              "raw_error_message": "",
              "request_id": "string",
              "result_value": "string",
              "tool_has_been_called": true,
              "tool_latency_secs": 0,
              "tool_name": "string",
              "type": "client"
            }
          ],
          "feedback": {
            "score": "like",
            "time_in_call_secs": 1
          },
          "llm_override": "string",
          "producing_llm": "string",
          "conversation_turn_metrics": {
            "metrics": {},
            "convai_asr_provider": "string",
            "convai_tts_model": "string",
            "convai_tts_cascade": "string"
          },
          "rag_retrieval_info": {
            "chunks": [
              {
                "document_id": "string",
                "chunk_id": "string",
                "vector_distance": 1.1
              }
            ],
            "embedding_model": "e5_mistral_7b_instruct",
            "retrieval_query": "string",
            "rag_latency_secs": 1.1,
            "used_chunk_ids": [
              "string"
            ]
          },
          "llm_usage": {
            "model_usage": {}
          },
          "interrupted": false,
          "ignored_as_backchannel": false,
          "original_message": "string",
          "reasoning": [
            {
              "summary": "string",
              "provider_redact": false
            }
          ],
          "source_medium": "audio",
          "source_event_id": 1,
          "used_static_kb_document_ids": [
            "string"
          ],
          "user_identifier": "string",
          "id": "string",
          "triggered_guardrails": [
            {
              "guardrail_type": "custom",
              "guardrail_name": "string"
            }
          ]
        }
      ],
      "test_name": "Unknown Test",
      "condition_result": {
        "result": "success",
        "rationale": {
          "messages": [
            "string"
          ],
          "summary": ""
        }
      },
      "last_updated_at_unix": 1,
      "metadata": {
        "workspace_id": "string",
        "test_name": "string",
        "ran_by_user_email": "string",
        "test_type": "llm"
      },
      "root_folder_id": "string",
      "root_folder_name": "string",
      "environment": "string",
      "credits_used": 1,
      "charging": {
        "dev_discount": false,
        "is_burst": false,
        "tier": "string",
        "llm_usage": {
          "irreversible_generation": {
            "model_usage": {}
          },
          "initiated_generation": {
            "model_usage": {}
          }
        },
        "llm_price": 1.1,
        "llm_charge": 1,
        "call_charge": 1,
        "platform_charge": 1,
        "platform_usage": {
          "category_usage": {}
        },
        "platform_price": 1.1,
        "free_minutes_consumed": 0,
        "free_llm_dollars_consumed": 0,
        "tts_usage": {
          "primary_tts_model": "string",
          "total_audio_output_seconds": 0,
          "total_characters": 0,
          "per_voice_usage": [
            {
              "voice_id": "string",
              "audio_output_seconds": 0
            }
          ]
        },
        "asr_usage": {
          "asr_model": "string",
          "total_transcription_calls": 0,
          "total_audio_input_seconds": 0
        },
        "analysis": {
          "total": {
            "price": 0,
            "charge": 0,
            "runs": 0,
            "price_per_feature": {},
            "charge_per_feature": {}
          },
          "last_run": {
            "price": 0,
            "charge": 0,
            "price_per_feature": {},
            "charge_per_feature": {}
          }
        }
      }
    }
  ],
  "agent_id": "string",
  "branch_id": "string",
  "version_id": "string",
  "ran_against_draft": false,
  "created_at": 1,
  "folder_id": "string",
  "repeat_count": 1,
  "bucketing_status": "pending",
  "result_groups": [
    {
      "test_id": "string",
      "test_name": "string",
      "buckets": [
        {
          "test_run_ids": [
            "string"
          ],
          "title": "string",
          "reason": "string",
          "status": "pending"
        }
      ],
      "workflow_node_id": "string"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.invocations.get("test_invocation_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.invocations.get(
    test_invocation_id="test_invocation_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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
