---
title: "Run tests on agent"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/run-tests.md
path: docs/eleven-agents/api-reference/tests/run-tests
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Run tests on agent

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/run-tests
Content-Type: application/json

Run selected tests on the agent with provided configuration. If the agent configuration is provided, it will be used to override default agent configuration.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/run-tests

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

- `tests` (list of SingleTestRunRequestModel, required) — List of tests to run on the agent
- `agent_config_override` (AdhocAgentConfigOverrideForTestRequestModel, optional) — Configuration overrides to use for testing. If not provided, the agent's default configuration will be used.
- `branch_id` (string, optional) — ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch.
- `repeat_count` (integer, optional, default: 1) — Number of times to run each test. When greater than 1, results are grouped and summarized.

## Response

### 200

Successful Response

- `id` (string, required)
- `test_runs` (list of UnitTestRunResponseModel, required)
- `agent_id` (string, optional)
- `branch_id` (string, optional)
- `version_id` (string, optional)
- `ran_against_draft` (boolean, optional, default: false)
- `created_at` (integer, optional)
- `folder_id` (string, optional)
- `repeat_count` (integer, optional, default: 1)
- `bucketing_status` (enum, optional) — None when repeat_count==1 (no bucketing). Otherwise tracks bucketing lifecycle.
  - Allowed values: `pending`, `completed`, `failed`
- `result_groups` (list of TestRunResultSummary, optional)

## Errors

### 422 Agents Run Tests Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### SingleTestRunRequestModel

- `test_id` (string, required) — ID of the test to run
- `workflow_node_id` (string, optional) — ID of the workflow node to run the test on. If not provided, the test will be run on the agent's default workflow node.
- `root_folder_id` (string, optional) — ID of the root folder to run the test on. If not provided, the test will be run on the agent's default folder.
- `root_folder_name` (string, optional) — Name of the root folder to run the test on. If not provided, the test will be run on the agent's default folder.

### AdhocAgentConfigOverrideForTestRequestModel

- `conversation_config` (ConversationalConfig, required)
- `platform_settings` (AgentPlatformSettingsRequestModel, required)
- `workflow` (AgentWorkflowRequestModel, optional)

### UnitTestRunResponseModel

- `test_run_id` (string, required)
- `test_invocation_id` (string, required)
- `agent_id` (string, required)
- `status` (enum, required)
  - Allowed values: `pending`, `passed`, `failed`
- `test_id` (string, required)
- `test_info` (UnitTestRunResponseModelTestInfo, optional)
- `branch_id` (string, optional)
- `version_id` (string, optional)
- `ran_against_draft` (boolean, optional, default: false)
- `workflow_node_id` (string, optional)
- `agent_responses` (list of ConversationHistoryTranscriptCommonModelOutput, optional)
- `test_name` (string, optional, default: Unknown Test)
- `condition_result` (TestConditionResultCommonModel, optional)
- `last_updated_at_unix` (integer, optional)
- `metadata` (TestRunMetadata, optional)
- `root_folder_id` (string, optional)
- `root_folder_name` (string, optional)
- `environment` (string, optional)
- `credits_used` (integer, optional) — Credits billed for this test run. None for runs created before cost tracking.
- `charging` (ConversationChargingCommonModel, optional) — Finalized billing and provider-usage breakdown for this test run.

### TestRunResultSummary

- `test_id` (string, required)
- `test_name` (string, required)
- `buckets` (list of TestRunResultBucket, required)
- `workflow_node_id` (string, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### ConversationalConfig

- `asr` (AsrConversationalConfig, optional) — Configuration for conversational transcription
- `turn` (TurnConfig, optional) — Configuration for turn detection
- `tts` (TtsConversationalConfigOutput, optional) — Configuration for conversational text to speech
- `conversation` (ConversationConfigOutput, optional) — Configuration for conversational events
- `language_presets` (map from string to LanguagePresetOutput, optional) — Language presets for conversations
- `vad` (VadConfig, optional) — Configuration for voice activity detection
- `agent` (AgentConfig, optional) — Agent specific configuration

### AgentPlatformSettingsRequestModel

- `evaluation` (EvaluationSettingsInput, optional) — Settings for evaluation
- `widget` (WidgetConfig, optional) — Configuration for the widget
- `data_collection` (map from string to AnalysisProperty, optional) — Data collection settings
- `data_collection_scopes` (map from string to enum, optional) — Scope per data collection item ID. Missing keys default to conversation scope.
  - Allowed values: `conversation`, `agent`
- `analysis_items` (AgentAnalysisItemsInput, optional) — Evaluation + data-collection items attached by reference. None means the agent has not been migrated onto analysis items yet (distinct from an empty, migrated set); reads fall back to the legacy evaluation/data_collection fields in that case.
- `overrides` (ConversationInitiationClientDataConfigInput, optional) — Additional overrides for the agent during conversation initiation
- `workspace_overrides` (AgentWorkspaceOverridesInput, optional) — Workspace overrides for the agent
- `testing` (AgentTestingSettings, optional) — Testing configuration for the agent
- `archived` (boolean, optional, default: false) — Whether the agent is archived
- `guardrails` (GuardrailsV1Input, optional) — Guardrails configuration for the agent
- `summary_language` (string, optional) — Language for all conversation analysis outputs (summaries, titles, evaluation rationales, data collection rationales). If not set, the language will be inferred from the conversation. Must be one of the supported conversation languages.
- `auto_translate_transcript_to_app_language` (boolean, optional) — When enabled, a conversation transcript is automatically translated to the viewer's application language when they open the transcript page. If not set or false, transcripts are shown in their original language unless the viewer manually selects a translation.
- `auth` (AuthSettings, optional) — Settings for authentication
- `call_limits` (AgentCallLimits, optional) — Call limits for the agent
- `queueing_config` (AgentQueueingConfig, optional) — Concurrency wait-queue config for the agent
- `privacy` (PrivacyConfigInput, optional) — Privacy settings for the agent
- `trust_context` (enum, optional, default: unknown) — The trust context in which the agent operates.
  - Allowed values: `unknown`, `low`, `high`
- `analysis_llm` (enum, optional) — Default LLM model for post-call analysis (evaluation and data collection)
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `topic_discovery` (TopicDiscoverySettings, optional) — Per-agent topic discovery configuration
- `sentiment_analysis` (SentimentAnalysisSettings, optional) — Per-agent post-call sentiment analysis configuration
- `alerting` (AlertingSettings, optional) — Agent-level alerting configuration overriding workspace settings.

### AgentWorkflowRequestModel

- `edges` (map from string to WorkflowEdgeModelInput, optional)
- `nodes` (map from string to AgentWorkflowRequestModelNodesValue, optional)
- `prevent_subagent_loops` (boolean, optional, default: false) — Whether to prevent loops in the workflow execution.

### UnitTestRunResponseModelTestInfo

- `type`: `llm`
  - `chat_history` (list of ConversationHistoryTranscriptCommonModelOutput, optional)
  - `conversation_initiation_source` (enum, optional, default: unknown) — Simulate the test as if the conversation originated from this channel.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
  - `environment` (string, optional) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
  - `failure_examples` (list of AgentFailureResponseExample, optional) — Non-empty list of example responses that should be considered failures
  - `from_conversation_metadata` (TestFromConversationMetadataOutput, optional) — Metadata of a conversation this test was created from (if applicable).
  - `success_condition` (string, optional, default: ) — A prompt that evaluates whether the agent's response is successful. Should return True or False.
  - `success_examples` (list of AgentSuccessfulResponseExample, optional) — Non-empty list of example responses that should be considered successful
- `type`: `simulation`
  - `chat_history` (list of ConversationHistoryTranscriptCommonModelOutput, optional)
  - `conversation_initiation_source` (enum, optional, default: unknown) — Simulate the test as if the conversation originated from this channel.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
  - `environment` (string, optional) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
  - `evaluation_model` (enum, optional) — LLM model to use for evaluating simulation results.
    - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
  - `from_conversation_metadata` (TestFromConversationMetadataOutput, optional) — Metadata of a conversation this test was created from (if applicable).
  - `simulated_user_model` (enum, optional) — LLM model for the simulated user.
    - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
  - `simulation_environment` (string, optional) — The environment to use when running this simulation test. If not provided, defaults to 'production'.
  - `simulation_max_turns` (integer, optional, default: 5) — Maximum number of conversation turns for simulation tests.
  - `simulation_scenario` (string, optional, default: ) — Description of the simulation scenario and user persona for simulation tests.
  - `success_conditions` (list of string, optional) — List of prompts that evaluate whether the simulation was successful. If provided, all criteria are evaluated and merged into a final result. Capped at the maximum number of evaluation criteria.
  - `tool_mock_config` (SimulationToolMockBehaviorConfig, optional) — Configuration for which tools to mock and fallback behavior.
  - `tool_mock_overrides` (map from string to list of ToolResponseMockConfigOutput, optional) — Test-specific response mocks, keyed by tool ID. Applied ahead of the tool's shared mocks and only within this test. Only take effect for tools that are mocked (see tool_mock_config).
  - `success_condition` (string, optional, deprecated) — Deprecated legacy single success criterion. Use success_conditions instead. At least one of success_condition or success_conditions is required.
- `type`: `tool`
  - `chat_history` (list of ConversationHistoryTranscriptCommonModelOutput, optional)
  - `check_any_tool_matches` (boolean, optional) — If set to True this test will pass if any tool call returned by the LLM matches the criteria. Otherwise it will fail if more than one tool is returned by the agent.
  - `conversation_initiation_source` (enum, optional, default: unknown) — Simulate the test as if the conversation originated from this channel.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
  - `environment` (string, optional) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
  - `from_conversation_metadata` (TestFromConversationMetadataOutput, optional) — Metadata of a conversation this test was created from (if applicable).
  - `tool_call_parameters` (UnitTestToolCallEvaluationModelOutput, optional) — How to evaluate the agent's tool call (if any). If empty, the tool call is not evaluated.

### ConversationHistoryTranscriptCommonModelOutput

- `role` (enum, required)
  - Allowed values: `user`, `agent`
- `time_in_call_secs` (integer, required)
- `agent_metadata` (AgentMetadata, optional)
- `message` (string, optional)
- `multivoice_message` (ConversationHistoryMultivoiceMessageModel, optional) — Represents a message from a multi-voice agent.
- `tool_calls` (list of ConversationHistoryTranscriptToolCallCommonModelOutput, optional)
- `tool_results` (list of ConversationHistoryTranscriptCommonModelOutputToolResultsItem, optional)
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

### TestConditionResultCommonModel

- `result` (enum, required)
  - Allowed values: `success`, `failure`, `unknown`
- `rationale` (TestConditionRationaleCommonModel, optional) — Structured rationale for test condition results containing individual failure/success reasons.

### TestRunMetadata

- `workspace_id` (string, required)
- `test_name` (string, required)
- `ran_by_user_email` (string, required)
- `test_type` (enum, optional, default: llm)
  - Allowed values: `llm`, `tool_call`, `simulation`

### ConversationChargingCommonModel

- `dev_discount` (boolean, optional, default: false)
- `is_burst` (boolean, optional, default: false)
- `tier` (string, optional)
- `llm_usage` (LlmCategoryUsage, optional)
- `llm_price` (double, optional)
- `llm_charge` (integer, optional)
- `call_charge` (integer, optional)
- `platform_charge` (integer, optional)
- `platform_usage` (PlatformUsage, optional) — Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``).
- `platform_price` (double, optional)
- `free_minutes_consumed` (double, optional, default: 0)
- `free_llm_dollars_consumed` (double, optional, default: 0)
- `tts_usage` (ConversationTtsUsageModel, optional) — Aggregated TTS usage for a conversation (analytics-only, not billing).
- `asr_usage` (ConversationAsrUsageModel, optional) — Aggregated ASR usage for a conversation (analytics-only, not billing).
- `analysis` (AnalysisCharging, optional) — Cost of running post-call analysis on this conversation. Present once an analysis pass has run, billed or not.

### TestRunResultBucket

- `test_run_ids` (list of string, required)
- `title` (string, required) — Short one-line title for this bucket
- `reason` (string, required) — Short summary of why the test runs in this bucket passed or failed
- `status` (enum, required)
  - Allowed values: `pending`, `passed`, `failed`

### ValidationErrorLocItem

### AsrConversationalConfig

- `quality` ("high", optional) — The quality of the transcription
- `provider` (enum, optional, default: scribe_realtime) — The provider of the transcription service
  - Allowed values: `elevenlabs`, `scribe_realtime`
- `user_input_audio_format` (enum, optional, default: pcm_16000) — The format of the audio to be transcribed
  - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
- `keywords` (list of string, optional) — Keywords to boost prediction probability for

### TurnConfig

- `turn_timeout` (double, optional, default: 7) — Maximum wait time for the user's reply before re-engaging the user
- `initial_wait_time` (double, optional) — How long the agent will wait for the user to start the conversation if the first message is empty. If not set, uses the regular turn_timeout.
- `silence_end_call_timeout` (double, optional, default: -1) — Maximum wait time since the user last spoke before terminating the call
- `turn_eagerness` (enum, optional, default: normal) — Controls how eager the agent is to respond. Low = less eager (waits longer), Standard = default eagerness, High = more eager (responds sooner)
  - Allowed values: `patient`, `normal`, `eager`
- `spelling_patience` (enum, optional, default: auto) — Controls if the agent should be more patient when user is spelling numbers and named entities. Auto = model based, Off = never wait extra
  - Allowed values: `auto`, `off`
- `speculative_turn` (boolean, optional, default: false) — When enabled, starts generating LLM responses during silence before full turn confidence is reached, reducing perceived latency. May increase LLM costs.
- `retranscribe_on_turn_timeout` (boolean, optional, default: false) — When enabled, if VAD detects no speech, attempts to re-transcribe accumulated audio at turn timeout. Disables silence discount billing for affected turns.
- `turn_model` (enum, optional, default: turn_v3) — Version of the turn detection model to use.
  - Allowed values: `turn_v2`, `turn_v3`
- `interruption_ignore_terms` (list of string, optional) — List of terms that should not trigger an interruption when spoken by the user (e.g. 'gotcha', 'understood'). Uses case-insensitive exact matching.
- `interruption_ignore_term_languages` (list of string, optional) — Language codes for which preset ignore-term categories have been activated. Stored explicitly so display is not inferred from term overlap.
- `merge_with_default_ignore_terms` (boolean, optional, default: false) — When enabled, the curated default terms for interruption_ignore_term_languages are used in addition to interruption_ignore_terms.
- `transcribe_on_disabled_interruptions` (boolean, optional, default: false) — When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.
- `soft_timeout_config` (SoftTimeoutConfig, optional) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.

### TtsConversationalConfigOutput

- `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
  - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
- `voice_id` (string, optional, default: cjVigY5qzO86Huf0OWal) — The voice ID to use for TTS
- `supported_voices` (list of SupportedVoice, optional) — Additional supported voices for the agent
- `expressive_mode` (boolean, optional, default: true) — When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.
- `suggested_audio_tags` (list of SuggestedAudioTag, optional) — Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.
- `agent_output_audio_format` (enum, optional, default: pcm_16000) — The audio format to use for TTS
  - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
- `optimize_streaming_latency` (integer, optional) — Deprecated: this field is a no-op and is ignored.
- `stability` (double, optional, default: 0.5) — The stability of generated speech
- `speed` (double, optional, default: 1) — The speed of generated speech
- `similarity_boost` (double, optional, default: 0.8) — The similarity boost for generated speech
- `text_normalisation_type` (enum, optional, default: system_prompt) — Method for converting numbers to words before converting text to speech. If set to SYSTEM_PROMPT, the system prompt will be updated to include normalization instructions. If set to ELEVENLABS, the text will be normalized after generation, incurring slight additional latency.
  - Allowed values: `system_prompt`, `elevenlabs`
- `pronunciation_dictionary_locators` (list of PydanticPronunciationDictionaryVersionLocator, optional) — The pronunciation dictionary locators
- `enable_phoneme_tags` (boolean, optional, default: true) — Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.
- `audio_effects` (EffectsSpecOutput, optional) — Optional TTS effects spec: filter preset, distance (proximity EQ), and environment (convolution reverb).

### ConversationConfigOutput

- `text_only` (boolean, optional, default: false) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
- `max_duration_seconds` (integer, optional, default: 600) — The maximum duration of a conversation in seconds
- `client_events` (list of enum, optional) — The events that will be sent to the client
  - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `context_usage`, `internal_turn_probability`, `internal_tentative_agent_response`
- `file_input` (FileInputConfig, optional) — Configuration for file input (image/PDF uploads) during conversations.
- `monitoring_enabled` (boolean, optional, default: false) — Enable real-time monitoring of conversations via WebSocket
- `monitoring_events` (list of enum, optional) — The events that will be sent to monitoring connections.
  - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `context_usage`, `internal_turn_probability`, `internal_tentative_agent_response`
- `dtmf_input_settings` (DtmfInputConfig, optional) — Configure DTMF (keypad) input collection during phone calls
- `background_sound` (BackgroundSoundConfig, optional) — Configuration for background sound during conversations.
- `source_attribution` (boolean, optional, default: false) — When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.

### LanguagePresetOutput

- `overrides` (ConversationConfigClientOverrideOutput, required) — The overrides for the language preset
- `first_message_translation` (LanguagePresetTranslation, optional) — The translation of the first message
- `soft_timeout_translation` (LanguagePresetTranslation, optional) — The translation of the soft timeout message

### VadConfig

### AgentConfig

- `first_message` (string, optional, default: ) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional, default: en) — Language of the agent - used for ASR and TTS
- `hinglish_mode` (boolean, optional, default: false) — When enabled and language is Hindi, the agent will respond in Hinglish
- `dynamic_variables` (any, optional)
- `disable_first_message_interruptions` (boolean, optional, default: false) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
- `max_conversation_duration_message` (string, optional, default: ) — If non-empty, the message the agent will send when max conversation duration is reached.
- `text_behavior_overrides` (map from string to BehaviorOverride, optional) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
- `prompt` (PromptAgentApiModelOutput, optional) — The prompt for the agent

### EvaluationSettingsInput

Settings to evaluate an agent's performance. Agents are evaluated against a set of criteria, with success being defined as meeting some combination of those criteria.

- `criteria` (list of PromptEvaluationCriteria, optional) — Individual criteria that the agent should be evaluated against

### WidgetConfig

- `variant` (enum, optional, default: full) — The variant of the widget
  - Allowed values: `tiny`, `compact`, `full`, `expandable`
- `placement` (enum, optional, default: bottom-right) — The placement of the widget on the screen
  - Allowed values: `top-left`, `top`, `top-right`, `bottom-left`, `bottom`, `bottom-right`
- `expandable` (enum, optional, default: never) — Whether the widget is expandable
  - Allowed values: `never`, `mobile`, `desktop`, `always`
- `avatar` (WidgetConfigAvatar, optional) — The avatar of the widget
- `feedback_mode` (enum, optional, default: none) — The feedback mode of the widget
  - Allowed values: `none`, `during`, `end`
- `end_feedback` (WidgetEndFeedbackConfig, optional) — Configuration for feedback collected at the end of the conversation
- `bg_color` (string, optional, default: #ffffff) — The background color of the widget
- `text_color` (string, optional, default: #000000) — The text color of the widget
- `btn_color` (string, optional, default: #000000) — The button color of the widget
- `btn_text_color` (string, optional, default: #ffffff) — The button text color of the widget
- `border_color` (string, optional, default: #e1e1e1) — The border color of the widget
- `focus_color` (string, optional, default: #000000) — The focus color of the widget
- `border_radius` (integer, optional) — The border radius of the widget
- `btn_radius` (integer, optional) — The button radius of the widget
- `action_text` (string, optional) — The action text of the widget
- `start_call_text` (string, optional) — The start call text of the widget
- `end_call_text` (string, optional) — The end call text of the widget
- `expand_text` (string, optional) — The expand text of the widget
- `listening_text` (string, optional) — The text to display when the agent is listening
- `speaking_text` (string, optional) — The text to display when the agent is speaking
- `shareable_page_text` (string, optional) — The text to display when sharing
- `shareable_page_show_terms` (boolean, optional, default: true) — Whether to show terms and conditions on the shareable page
- `terms_text` (string, optional) — The text to display for terms and conditions
- `terms_html` (string, optional) — The HTML to display for terms and conditions
- `terms_key` (string, optional) — The key to display for terms and conditions
- `show_avatar_when_collapsed` (boolean, optional) — Whether to show the avatar when the widget is collapsed
- `disable_banner` (boolean, optional, default: false) — Whether to disable the banner
- `override_link` (string, optional) — The override link for the widget
- `markdown_link_allowed_hosts` (list of AllowlistItem, optional) — List of allowed hostnames for clickable markdown links. Use \{ hostname: '\*' } to allow any domain. Empty means no links are allowed.
- `markdown_link_include_www` (boolean, optional, default: true) — Whether to automatically include www. variants of allowed hosts
- `markdown_link_allow_http` (boolean, optional, default: true) — Whether to allow http:// in addition to https:// for allowed hosts
- `mic_muting_enabled` (boolean, optional, default: true) — Whether to enable mic muting
- `transcript_enabled` (boolean, optional, default: true) — Whether the widget should show the conversation transcript as it goes on
- `text_input_enabled` (boolean, optional, default: true) — Whether the user should be able to send text messages
- `conversation_mode_toggle_enabled` (boolean, optional, default: false) — Whether to enable the conversation mode toggle in the widget
- `default_expanded` (boolean, optional, default: false) — Whether the widget should be expanded by default
- `always_expanded` (boolean, optional, default: false) — Whether the widget should always be expanded
- `dismissible` (boolean, optional, default: false) — Whether the widget can be dismissed by the user
- `show_agent_status` (boolean, optional, default: false) — Whether to show agent working/done/error status during tool use
- `show_conversation_id` (boolean, optional, default: true) — Whether to show the conversation ID after disconnection.
- `strip_audio_tags` (boolean, optional, default: true) — Whether to strip audio markup from messages.
- `syntax_highlight_theme` (enum, optional) — Theme for code block syntax highlighting. Defaults to auto-detection by the widget when not set.
  - Allowed values: `light`, `dark`
- `text_contents` (WidgetTextContents, optional) — Text contents of the widget
- `styles` (WidgetStyles, optional) — Styles for the widget
- `show_resize_button` (boolean, optional, default: true) — Whether to show the resize button
- `language_selector` (boolean, optional, default: false) — Whether to show the language selector
- `supports_text_only` (boolean, optional, default: true) — Whether the widget can switch to text only mode
- `custom_avatar_path` (string, optional) — The custom avatar path
- `language_presets` (map from string to WidgetLanguagePreset, optional) — Language presets for the widget

### AnalysisProperty

Data collection property with optional per-item LLM override for post-call analysis. TODO: migrate to composition (value_schema: LiteralJsonSchemaProperty + llm) instead of inheritance, so this generalizes cleanly to object/array schemas in the future.

- `type` (enum, required)
  - Allowed values: `boolean`, `string`, `integer`, `number`
- `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
- `enum` (list of string, optional) — List of allowed string values for string type parameters
- `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
- `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
- `allowed_values` (AllowedValues, optional) — Server-side rejection guard for an LLM-provided value: the runtime rejects any value outside the permitted set this object names, and the set is not advertised to the LLM as an enum. Only supported when the value source is `description`; combining it with dynamic_variable, is_system_provided, constant_value, or is_omitted is rejected.
- `constant_value` (AnalysisPropertyConstantValue, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
- `name` (string, optional) — The name of this data collection item.
- `llm` (enum, optional) — LLM model to use for this analysis item. If not set, uses agent's analysis_llm default.
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `allowed_values_dynamic_variable` (string, optional, default: , deprecated) — DEPRECATED: use `allowed_values` instead. When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable (must be a JSON array such as ["ws_alpha", "ws_beta"]). Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.

### AgentAnalysisItemsInput

- `evaluation_criteria` (list of AgentAnalysisItemsInputEvaluationCriteriaItem, optional)
- `data_collection` (list of AgentAnalysisItemsInputDataCollectionItem, optional)

### ConversationInitiationClientDataConfigInput

- `conversation_config_override` (ConversationConfigClientOverrideConfigInput, optional) — Overrides for the conversation configuration
- `custom_llm_extra_body` (boolean, optional, default: false) — Whether to include custom LLM extra body
- `enable_conversation_initiation_client_data_from_webhook` (boolean, optional, default: false) — Whether to enable conversation initiation client data from webhooks
- `enable_starting_workflow_node_id_from_client` (boolean, optional, default: false) — Whether clients may pass starting_workflow_node_id in initiation client data; if false, sending it fails conversation start.
- `enable_procedure_ids_from_client` (boolean, optional, default: false) — Whether clients may pass procedure_ids in initiation client data to select which of the agent's procedures are available for the conversation; if false, sending it fails conversation start.

### AgentWorkspaceOverridesInput

- `conversation_initiation_client_data_webhook` (ConversationInitiationClientDataWebhook, optional) — The webhook to send conversation initiation client data to
- `webhooks` (ConvAiWebhooks, optional)

### AgentTestingSettings

Settings for agent testing configuration.

- `attached_tests` (list of AttachedTestModel, optional) — List of test IDs that should be run for this agent

### GuardrailsV1Input

- `version` ("1", optional)
- `focus` (FocusGuardrail, optional)
- `prompt_injection` (PromptInjectionGuardrail, optional)
- `content` (ContentGuardrailInput, optional)
- `custom` (CustomGuardrailInput, optional) — Container for custom guardrails, matching ModerationGuardrail pattern

### AuthSettings

- `enable_auth` (boolean, optional, default: false) — If set to true, starting a conversation with an agent will require a signed token
- `allowlist` (list of AllowlistItem, optional) — A list of hosts that are allowed to start conversations with the agent
- `require_origin_header` (boolean, optional, default: false) — When enabled, connections with no origin header will be rejected. If the allowlist is empty, this option has no effect.
- `shareable_token` (string, optional) — A shareable token that can be used to start a conversation with the agent

### AgentCallLimits

- `agent_concurrency_limit` (integer, optional, default: -1) — The maximum number of concurrent conversations. -1 indicates that there is no maximum
- `daily_limit` (integer, optional, default: 100000) — The maximum number of conversations per day
- `bursting_enabled` (boolean, optional, default: true) — Whether to enable bursting. If true, exceeding workspace concurrency limit will be allowed up to 3 times the limit. Calls will be charged at double rate when exceeding the limit.

### AgentQueueingConfig

- `enabled` (boolean, optional, default: false) — Hold callers in a wait queue when the agent is at its concurrency limit, instead of rejecting them immediately
- `wait_timeout_seconds` (integer, optional, default: 180) — Maximum time a caller can wait in the queue before being rejected
- `hold_audio` (AgentHoldAudioConfig, optional) — Custom hold audio played to queued callers; when unset, callers hear the default hold tone. Read-only: set it by uploading a file through the agent hold-audio endpoint.

### PrivacyConfigInput

- `record_voice` (boolean, optional, default: true) — Whether to record the conversation
- `retention_days` (integer, optional, default: -1) — The number of days to retain the conversation. -1 indicates there is no retention limit
- `delete_transcript_and_pii` (boolean, optional, default: false) — Whether to delete the transcript and PII
- `delete_audio` (boolean, optional, default: false) — Whether to delete the audio
- `apply_to_existing_conversations` (boolean, optional, default: false) — Whether to apply the privacy settings to existing conversations
- `zero_retention_mode` (boolean, optional, default: false) — Whether to enable zero retention mode - no PII data is stored
- `conversation_history_redaction` (ConversationHistoryRedactionConfig, optional) — Config for PII redaction in the conversation history

### TopicDiscoverySettings

Per-agent topic-discovery configuration. Cadence and analysis window are managed internally; this only exposes the customer-facing on/off toggle.

### SentimentAnalysisSettings

### AlertingSettings

Alerting configuration used at both per-agent and per-workspace level. Cascade order for per-monitor threshold and auto-resolve: agent → workspace → system default.

- `monitor_configs` (map from string to AlertingMonitorConfig, optional) — Alerting configuration keyed by monitor name.
- `auto_resolve_after_inactive_minutes` (integer, optional) — How many minutes an alert can stay inactive before it is auto-resolved. Unset values fall through to the next layer.
- `notifiers` (list of AlertingSettingsNotifiersItem, optional) — Delivery channels for alert lifecycle notifications. Stacked with other layers and deduped by ``webhook_id``, PagerDuty ``connection_id``, or Slack ``(connection_id, channel_id)``.

### WorkflowEdgeModelInput

- `source` (string, required) — ID of the source node.
- `target` (string, required) — ID of the target node.
- `forward_condition` (WorkflowEdgeModelInputForwardCondition, optional) — Condition that must be met for the edge to be traversed in the forward direction (source to target).
- `backward_condition` (WorkflowEdgeModelInputBackwardCondition, optional) — Condition that must be met for the edge to be traversed in the backward direction (target to source).

### AgentWorkflowRequestModelNodesValue

- `type`: `end`
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
- `type`: `override_agent`
  - `label` (string, required) — Human-readable label for the node used throughout the UI.
  - `additional_knowledge_base` (list of KnowledgeBaseLocator, optional) — Additional knowledge base documents that the subagent has access to. These will be used in addition to the main agent's documents.
  - `additional_prompt` (string, optional) — Specific goal for this subagent. It will be added to the system prompt and can be used to further refine the agent's behavior in this specific context.
  - `additional_tool_ids` (list of string, optional) — IDs of additional tools that the subagent has access to. These will be used in addition to the main agent's tools.
  - `conversation_config` (ConversationalConfigApiModelWorkflowOverrideInput, optional) — Configuration overrides applied while the subagent is conducting the conversation.
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `entry_behavior` (enum, optional, default: auto) — Dictates whether this node should immediately generate a response upon entry or wait for the user input. When set to "auto", the behavior will be decided based on the type of the preceding node: "wait_for_user" after the "say" and "start" nodes and "generate_immediately" otherwise.
    - Allowed values: `generate_immediately`, `wait_for_user`, `auto`
  - `position` (PositionInput, optional) — Position of the node in the workflow.
- `type`: `phone_number`
  - `transfer_destination` (WorkflowPhoneNumberNodeModelInputTransferDestination, required)
  - `custom_sip_headers` (list of WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem, optional) — Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
  - `post_dial_digits` (WorkflowPhoneNumberNodeModelInputPostDialDigits, optional) — DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.
  - `sip_refer_play_dialtone` (boolean, optional, default: true) — When True, a ringing tone is played on the original call leg while a SIP REFER transfer completes. The tone is carried over RTP to the SIP peer executing the REFER, so disable this if the receiving system (e.g. an SBC or contact center) should not hear it. When disabled the caller hears silence until the transfer completes. SIP REFER transfers only.
  - `transfer_type` (enum, optional, default: conference)
    - Allowed values: `blind`, `conference`, `sip_refer`
  - `uui` (UuiTransferConfig, optional) — User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.
- `type`: `standalone_agent`
  - `agent_id` (string, optional) — The ID of the agent to transfer the conversation to. None means transfer within the current agent.
  - `delay_ms` (integer, optional, default: 0) — Artificial delay in milliseconds applied before transferring the conversation.
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `enable_transferred_agent_first_message` (boolean, optional, default: false) — Whether to enable the transferred agent to send its configured first message after the transfer.
  - `node_id` (string, optional) — Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
  - `preserve_client_tts_overrides` (boolean, optional, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.
  - `transfer_message` (string, optional) — Optional message sent to the user before the transfer is initiated.
- `type`: `start`
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
- `type`: `tool`
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
  - `tools` (list of WorkflowToolLocator, optional) — List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully.

### AgentFailureResponseExample

- `response` (string, required)
- `type` ("failure", required)

### TestFromConversationMetadataOutput

- `conversation_id` (string, required)
- `agent_id` (string, required)
- `branch_id` (string, optional)
- `workflow_node_id` (string, optional)
- `original_agent_reply` (list of ConversationHistoryTranscriptCommonModelOutput, optional, default: [])

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

### ToolResponseMockConfigOutput

- `mock_result` (string, required) — The return value the LLM sees when this mock is active.
- `parameter_conditions` (list of UnitTestToolCallParameter, optional) — If the list is empty, the mock will always activate.
- `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.

### UnitTestToolCallEvaluationModelOutput

- `parameters` (list of UnitTestToolCallParameter, optional) — Parameters to evaluate for the agent's tool call. If empty, the tool call parameters are not evaluated.
- `referenced_tool` (ReferencedToolCommonModel, optional) — The tool to evaluate a call against.
- `verify_absence` (boolean, optional, default: false) — Whether to verify that the tool was NOT called.
- `workflow_node_transition` (UnitTestWorkflowNodeTransitionEvaluationNodeId, optional) — Configuration for testing workflow node transitions. When set, the test will verify the agent transitions to the specified workflow node.

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

### ConversationHistoryTranscriptCommonModelOutputToolResultsItem

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

### TestConditionRationaleCommonModel

Structured rationale for test condition results containing individual failure/success reasons.

- `messages` (list of string, optional) — List of individual parameter evaluation messages or reasons
- `summary` (string, optional, default: ) — High-level summary of the evaluation result

### LlmCategoryUsage

- `irreversible_generation` (LlmUsageOutput, optional)
- `initiated_generation` (LlmUsageOutput, optional)

### PlatformUsage

Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``).

- `category_usage` (map from string to PlatformCategoryUsage, optional)

### ConversationTtsUsageModel

Aggregated TTS usage for a conversation (analytics-only, not billing).

- `primary_tts_model` (string, optional)
- `total_audio_output_seconds` (double, optional, default: 0)
- `total_characters` (integer, optional, default: 0)
- `per_voice_usage` (list of ConversationVoiceUsageModel, optional)

### ConversationAsrUsageModel

Aggregated ASR usage for a conversation (analytics-only, not billing).

- `asr_model` (string, optional)
- `total_transcription_calls` (integer, optional, default: 0)
- `total_audio_input_seconds` (double, optional, default: 0)

### AnalysisCharging

Cost of running post-call analysis on this conversation. Present once an analysis pass has run, billed or not.

- `total` (AnalysisRunningTotal, required) — Cumulative LLM cost of running post-call analysis on this conversation.
- `last_run` (AnalysisRunSnapshot, required) — LLM cost of the most recent post-call analysis pass on this conversation.

### SoftTimeoutConfig

Configuration for soft timeout functionality during LLM response generation.

- `timeout_seconds` (double, optional, default: -1) — Time in seconds before showing the predefined message while waiting for LLM response. Set to -1 to disable.
- `message` (string, optional, default: Hhmmmm...yeah.) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
- `additional_soft_timeout_messages` (list of string, optional) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.
- `use_llm_generated_message` (boolean, optional, default: false) — If enabled, the soft timeout message will be generated dynamically instead of using the static message.
- `randomize_fillers` (boolean, optional, default: false) — If enabled, shuffle the order of static soft timeout messages once at the start of each turn. Only applies when use_llm_generated_message is false.
- `max_soft_timeouts_per_generation` (integer, optional, default: 1) — Maximum filler messages while waiting for a single LLM response. Fires every timeout_seconds until the LLM streams content or this limit is reached.
- `llm_generated_message_prompt_override` (string, optional) — Custom prompt for generating the soft timeout filler message when use\_llm\_generated\_message is enabled. Recent conversation context is provided as a separate user message. If not set, the default prompt will be used. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
- `disable_until_first_user_message` (boolean, optional, default: false) — When true, soft timeout fillers are suppressed until the conversation has at least one real user message. Prevents fillers during the agent's opening turn (e.g. workflow generate-immediately / tool calls before the user speaks).

### SupportedVoice

- `label` (string, required)
- `voice_id` (string, required)
- `description` (string, optional)
- `language` (string, optional)
- `model_family` (enum, optional)
  - Allowed values: `turbo`, `flash`, `multilingual`, `v3_conversational`
- `optimize_streaming_latency` (integer, optional)
- `stability` (double, optional)
- `speed` (double, optional)
- `similarity_boost` (double, optional)

### SuggestedAudioTag

- `tag` (string, required) — Audio tag to use (for best performance, 1-2 words, e.g., 'happy', 'excited')
- `description` (string, optional) — Optional description of when to use this tag

### PydanticPronunciationDictionaryVersionLocator

A locator for other documents to be able to reference a specific dictionary and it's version. This is a pydantic version of PronunciationDictionaryVersionLocatorDBModel. Required to ensure compat with the rest of the agent data models.

- `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
- `version_id` (string, optional) — The ID of the version of the pronunciation dictionary

### EffectsSpecOutput

Filter preset, distance (proximity EQ), and environment (convolution reverb).

- `distance` (double, required, default: 0)
- `send_level` (double, required, default: 1)
- `filter_preset_id` (string, optional)
- `environment_id` (string, optional)
- `background_noise_id` (string, optional)
- `seed` (integer, optional)

### FileInputConfig

- `enabled` (boolean, optional, default: true) — When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.
- `max_files_in_memory` (integer, optional, default: 10) — Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.
- `max_files_per_conversation` (integer, optional, default: 10) — Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.

### DtmfInputConfig

Configuration for DTMF (keypad) input collection during phone calls.

- `dtmf_input_timeout` (double, optional, default: 2) — Timeout in seconds to wait for additional DTMF digits
- `hash_terminator` (boolean, optional, default: true) — If true, pressing # immediately completes DTMF input
- `redact_input` (boolean, optional, default: false) — If true, replace the caller's DTMF (keypad) entries with a redaction marker in the transcript, conversation log and analysis. Digits the agent repeats back or passes to a tool are not affected.

### BackgroundSoundConfig

- `source_type` ("preset", optional) — The type of background sound source.
- `source_id` (enum, optional) — Identifier for the sound source.
  - Allowed values: `office2`, `office1`, `restaurant`, `city`, `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
- `volume` (double, optional, default: 0.15) — Volume level for background sound (0.01 to 1.0).
- `crossfade_loop` (boolean, optional, default: true) — Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.

### ConversationConfigClientOverrideOutput

- `asr` (AsrConversationalConfigOverride, optional) — Configuration for conversational transcription
- `turn` (TurnConfigOverride, optional) — Configuration for turn detection
- `tts` (TtsConversationalConfigOverride, optional) — Configuration for conversational text to speech
- `conversation` (ConversationConfigOverride, optional) — Configuration for conversational events
- `agent` (AgentConfigOverrideOutput, optional) — Agent specific configuration

### LanguagePresetTranslation

- `source_hash` (string, required)
- `text` (string, required)

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

### WidgetConfigAvatar

The avatar of the widget

- `type`: `orb`
  - `color_1` (string, optional, default: #2792dc) — The first color of the avatar
  - `color_2` (string, optional, default: #9ce6e6) — The second color of the avatar
- `type`: `url`
  - `custom_url` (string, optional, default: ) — The custom URL of the avatar
- `type`: `image`
  - `url` (string, optional, default: ) — The URL of the avatar

### WidgetEndFeedbackConfig

- `type` ("rating", optional) — The type of feedback to collect at the end of the conversation

### AllowlistItem

- `hostname` (string, required) — The hostname of the allowed origin

### WidgetTextContents

- `main_label` (string, optional) — Call to action displayed inside the compact and full variants.
- `start_call` (string, optional) — Text and ARIA label for the start call button.
- `start_chat` (string, optional) — Text and ARIA label for the start chat button (text only)
- `new_call` (string, optional) — Text and ARIA label for the new call button. Displayed when the caller already finished at least one call in order ot start the next one.
- `end_call` (string, optional) — Text and ARIA label for the end call button.
- `mute_microphone` (string, optional) — ARIA label for the mute microphone button.
- `change_language` (string, optional) — ARIA label for the change language dropdown.
- `collapse` (string, optional) — ARIA label for the collapse button.
- `expand` (string, optional) — ARIA label for the expand button.
- `copied` (string, optional) — Text displayed when the user copies a value using the copy button.
- `accept_terms` (string, optional) — Text and ARIA label for the accept terms button.
- `dismiss_terms` (string, optional) — Text and ARIA label for the cancel terms button.
- `listening_status` (string, optional) — Status displayed when the agent is listening.
- `speaking_status` (string, optional) — Status displayed when the agent is speaking.
- `connecting_status` (string, optional) — Status displayed when the agent is connecting.
- `chatting_status` (string, optional) — Status displayed when the agent is chatting (text only)
- `input_label` (string, optional) — ARIA label for the text message input.
- `input_placeholder` (string, optional) — Placeholder text for the text message input.
- `input_placeholder_text_only` (string, optional) — Placeholder text for the text message input (text only)
- `input_placeholder_new_conversation` (string, optional) — Placeholder text for the text message input when starting a new conversation (text only)
- `user_ended_conversation` (string, optional) — Information message displayed when the user ends the conversation.
- `agent_ended_conversation` (string, optional) — Information message displayed when the agent ends the conversation.
- `conversation_id` (string, optional) — Text label used next to the conversation ID.
- `error_occurred` (string, optional) — Text label used when an error occurs.
- `copy_id` (string, optional) — Text and ARIA label used for the copy ID button.
- `initiate_feedback` (string, optional) — Text displayed to prompt the user for feedback.
- `request_follow_up_feedback` (string, optional) — Text displayed to request additional feedback details.
- `thanks_for_feedback` (string, optional) — Text displayed to thank the user for providing feedback.
- `thanks_for_feedback_details` (string, optional) — Additional text displayed explaining the value of user feedback.
- `follow_up_feedback_placeholder` (string, optional) — Placeholder text for the follow-up feedback input field.
- `submit` (string, optional) — Text and ARIA label for the submit button.
- `go_back` (string, optional) — Text and ARIA label for the go back button.
- `send_message` (string, optional) — Text and ARIA label for the send message button.
- `text_mode` (string, optional) — Text and ARIA label for the switch to text mode button.
- `voice_mode` (string, optional) — Text and ARIA label for the switch to voice mode button.
- `switched_to_text_mode` (string, optional) — Toast notification displayed when switching to text mode.
- `switched_to_voice_mode` (string, optional) — Toast notification displayed when switching to voice mode.
- `copy` (string, optional) — Text and ARIA label for the copy button.
- `download` (string, optional) — Text and ARIA label for the download button.
- `wrap` (string, optional) — Text and ARIA label for the wrap toggle button.
- `agent_working` (string, optional) — Status text displayed when the agent is processing a tool call.
- `agent_done` (string, optional) — Status text displayed when the agent finishes processing a tool call.
- `agent_error` (string, optional) — Status text displayed when the agent encounters an error during a tool call.
- `attach_file` (string, optional) — Text and ARIA label for the attach file button.
- `remove_file` (string, optional) — ARIA label for the remove file button.
- `file_upload_error` (string, optional) — Error message displayed when a file fails to upload.
- `file_type_unsupported` (string, optional) — Error message displayed when an unsupported file type is selected. Followed by the list of accepted types.
- `file_too_large` (string, optional) — Error message displayed when a file exceeds the maximum size limit.
- `file_limit_reached` (string, optional) — Error message displayed when the maximum number of files for a conversation is reached.
- `typing_indicator` (string, optional) — Status text displayed while the agent is typing.

### WidgetStyles

- `base` (string, optional) — The base background color.
- `base_hover` (string, optional) — The color of the base background when hovered.
- `base_active` (string, optional) — The color of the base background when active (clicked).
- `base_border` (string, optional) — The color of the border against the base background.
- `base_subtle` (string, optional) — The color of subtle text against the base background.
- `base_primary` (string, optional) — The color of primary text against the base background.
- `base_error` (string, optional) — The color of error text against the base background.
- `accent` (string, optional) — The accent background color.
- `accent_hover` (string, optional) — The color of the accent background when hovered.
- `accent_active` (string, optional) — The color of the accent background when active (clicked).
- `accent_border` (string, optional) — The color of the border against the accent background.
- `accent_subtle` (string, optional) — The color of subtle text against the accent background.
- `accent_primary` (string, optional) — The color of primary text against the accent background.
- `overlay_padding` (double, optional) — The padding around the edges of the viewport.
- `button_radius` (double, optional) — The radius of the buttons.
- `input_radius` (double, optional) — The radius of the input fields.
- `bubble_radius` (double, optional) — The radius of the chat bubbles.
- `sheet_radius` (double, optional) — The default radius of sheets.
- `compact_sheet_radius` (double, optional) — The radius of the sheet in compact mode.
- `dropdown_sheet_radius` (double, optional) — The radius of the dropdown sheet.

### WidgetLanguagePreset

- `text_contents` (WidgetTextContents, optional) — The text contents for the selected language
- `text_contents_translation` (WidgetTextContentsTranslation, optional) — The translation cache for the text contents
- `terms_text` (string, optional) — The text to display for terms and conditions in this language
- `terms_html` (string, optional) — The HTML to display for terms and conditions in this language
- `terms_key` (string, optional) — The key to display for terms and conditions in this language
- `terms_translation` (WidgetTermsTranslation, optional) — The translation cache for the terms

### AllowedValues

- `dynamic_variable` (string, required) — Name of a dynamic variable that must resolve to a JSON array of permitted values, e.g. ["ws_alpha", "ws_beta"]. System variables work only if they resolve to a list.

### AnalysisPropertyConstantValue

A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.

### AgentAnalysisItemsInputEvaluationCriteriaItem

- `source`: `system`
  - `analysis_item_id` (enum, required) — Id of the referenced built-in system evaluation.
    - Allowed values: `__system_eval_criteria_sentiment`, `__system_eval_criteria_frustration`
  - `scope` (enum, optional, default: conversation) — Transcript context ('conversation' or 'agent') used when running this item.
    - Allowed values: `conversation`, `agent`
  - `weight` (double, optional) — Optional relative weight for aggregate scoring.
- `source`: `user`
  - `analysis_item_id` (string, required) — Id of the referenced user evaluation item.
  - `additional_version_ids` (list of string, optional) — Extra item versions to also run for comparison (A/B). These are executed and stored but excluded from scoring; the primary version_id is the one that scores.
  - `scope` (enum, optional, default: conversation) — Transcript context ('conversation' or 'agent') used when running this item.
    - Allowed values: `conversation`, `agent`
  - `version_id` (string, optional) — Primary item version whose result feeds scoring. None tracks the item's latest published version.
  - `weight` (double, optional) — Optional relative weight for aggregate scoring.

### AgentAnalysisItemsInputDataCollectionItem

- `source`: `system`
  - `analysis_item_id` ("__system_data_collection_topic", required) — Id of the referenced built-in system data-collection item.
  - `scope` (enum, optional, default: conversation) — Transcript context ('conversation' or 'agent') used when running this item.
    - Allowed values: `conversation`, `agent`
- `source`: `user`
  - `analysis_item_id` (string, required) — Id of the referenced user data-collection item.
  - `scope` (enum, optional, default: conversation) — Transcript context ('conversation' or 'agent') used when running this item.
    - Allowed values: `conversation`, `agent`
  - `version_id` (string, optional) — Pinned item version. None tracks the item's latest published version.

### ConversationConfigClientOverrideConfigInput

- `asr` (AsrConversationalConfigOverrideConfig, optional) — Configures overrides for nested fields.
- `turn` (TurnConfigOverrideConfig, optional) — Configures overrides for nested fields.
- `tts` (TtsConversationalConfigOverrideConfig, optional) — Configures overrides for nested fields.
- `conversation` (ConversationConfigOverrideConfig, optional) — Configures overrides for nested fields.
- `agent` (AgentConfigOverrideConfig, optional) — Configures overrides for nested fields.

### ConversationInitiationClientDataWebhook

- `url` (string, required) — The URL to send the webhook to
- `request_headers` (map from string to ConversationInitiationClientDataWebhookRequestHeadersValue, required) — The headers to send with the webhook request

### ConvAiWebhooks

- `post_call_webhook_id` (string, optional)
- `events` (list of enum, optional) — List of event types to send via webhook. Options: transcript, audio, call_initiation_failure, answering_machine_detection, unredacted_transcript, unredacted_audio.
  - Allowed values: `transcript`, `audio`, `call_initiation_failure`, `answering_machine_detection`, `unredacted_transcript`, `unredacted_audio`
- `transcript_format` (enum, optional, default: json) — Format for transcript webhooks.
  - Allowed values: `json`, `opentelemetry`
- `send_audio` (boolean, optional, deprecated) — DEPRECATED: Use 'events' field instead. Whether to send audio data with post-call webhooks for ConvAI conversations

### AttachedTestModel

- `test_id` (string, required)
- `workflow_node_id` (string, optional)

### FocusGuardrail

- `is_enabled` (boolean, optional, default: false)

### PromptInjectionGuardrail

- `is_enabled` (boolean, optional, default: false)

### ContentGuardrailInput

- `execution_mode` (enum, optional, default: streaming)
  - Allowed values: `streaming`, `blocking`
- `config` (ContentConfig, optional)
- `trigger_action` (ContentGuardrailInputTriggerAction, optional)

### CustomGuardrailInput

Container for custom guardrails, matching ModerationGuardrail pattern

- `config` (CustomGuardrailsConfigInput, optional) — Config container for custom guardrails list

### AgentHoldAudioConfig

Custom hold audio played on loop to callers waiting in the agent's queue. Set by uploading a file through the agent hold-audio endpoint. Values sent in agent create or update requests are ignored.

- `audio_path` (string, required) — Storage path of the uploaded clip
- `audio_url` (string, required) — Public CDN URL of the uploaded clip
- `original_filename` (string, required) — Filename of the uploaded clip as provided by the user
- `duration_secs` (double, required) — Duration of the uploaded clip in seconds
- `size_bytes` (integer, required) — Size of the uploaded clip in bytes

### ConversationHistoryRedactionConfig

- `enabled` (boolean, optional, default: false) — Whether conversation history redaction is enabled
- `entities` (list of enum, optional) — The entities to redact from the conversation transcript, audio and analysis. Use top-level types like 'name', 'email_address', or dot notation for specific subtypes like 'name.full_name'.
  - Allowed values: `name`, `name.name_given`, `name.name_family`, `name.name_other`, `email_address`, `contact_number`, `dob`, `age`, `religious_belief`, `political_opinion`, `sexual_orientation`, `ethnicity_race`, `marital_status`, `occupation`, `physical_attribute`, `language`, `username`, `password`, `url`, `organization`, `financial_id`, `financial_id.payment_card`, `financial_id.payment_card.payment_card_number`, `financial_id.payment_card.payment_card_expiration_date`, `financial_id.payment_card.payment_card_cvv`, `financial_id.bank_account`, `financial_id.bank_account.bank_account_number`, `financial_id.bank_account.bank_routing_number`, `financial_id.bank_account.swift_bic_code`, `financial_id.financial_id_other`, `location`, `location.location_address`, `location.location_city`, `location.location_postal_code`, `location.location_coordinate`, `location.location_state`, `location.location_country`, `location.location_other`, `date`, `date_interval`, `unique_id`, `unique_id.government_issued_id`, `unique_id.account_number`, `unique_id.vehicle_id`, `unique_id.healthcare_number`, `unique_id.healthcare_number.medical_record_number`, `unique_id.healthcare_number.health_plan_beneficiary_number`, `unique_id.device_id`, `unique_id.unique_id_other`, `medical`, `medical.medical_condition`, `medical.medication`, `medical.medical_procedure`, `medical.medical_measurement`, `medical.medical_other`

### AlertingMonitorConfig

- `enabled` (boolean, optional) — Whether this monitor is enabled and can notify
- `threshold` (double, optional) — Failure rate threshold at which this monitor can notify.
- `relative_increase_threshold` (double, optional) — Relative increase over the trailing baseline at which this monitor can notify (0.2 = 20% above baseline, 0 = any failure).
- `min_failure_count` (integer, optional) — Minimum failures in the window before this monitor can fire.
- `min_history_bucket_count` (integer, optional) — Minimum trailing buckets with traffic before spike detection can fire.
- `min_sample_count` (integer, optional) — Minimum samples in the window before this monitor can fire.
- `suspect_trigger_threshold` (integer, optional) — How many suspect buckets within the lookback window are required to promote a suspect to an alert.
- `auto_resolve_after_inactive_minutes` (integer, optional) — How many minutes an alert can stay inactive before it is auto-resolved.

### AlertingSettingsNotifiersItem

- `type`: `webhook`
  - `webhook_id` (string, required) — ID of the workspace webhook to deliver alert lifecycle notifications to.
- `type`: `integration`
  - `connection_id` (string, required) — ID of the workspace integration connection to deliver alert lifecycle notifications to. The connection's integration must have the monitoring capability and match ``integration_type``.
  - `channel_id` (string, optional) — ID of the Slack channel to post alert notifications to, e.g. ``C0123456789``. Required when ``integration_type`` is ``slack``. The Slack app must be a member of the channel and have the ``chat:write`` scope, or ``chat:write.public`` for public channels it has not joined.
  - `integration_type` (enum, optional) — Integration to deliver to. The server treats an omitted value as ``pagerduty``.
    - Allowed values: `pagerduty`, `slack`

### WorkflowEdgeModelInputForwardCondition

- `type`: `expression`
  - `expression` (AstNodeInput, required) — Expression to evaluate.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `llm`
  - `condition` (string, required) — Condition to evaluate
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `result`
  - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `unconditional`
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.

### WorkflowEdgeModelInputBackwardCondition

- `type`: `expression`
  - `expression` (AstNodeInput, required) — Expression to evaluate.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `llm`
  - `condition` (string, required) — Condition to evaluate
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `result`
  - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `unconditional`
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.

### PositionInput

- `x` (double, optional, default: 0)
- `y` (double, optional, default: 0)

### KnowledgeBaseLocator

- `type` (enum, required) — The type of the knowledge base
  - Allowed values: `file`, `url`, `text`, `folder`
- `name` (string, required) — The name of the knowledge base
- `id` (string, required) — The ID of the knowledge base
- `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
  - Allowed values: `prompt`, `auto`

### ConversationalConfigApiModelWorkflowOverrideInput

- `asr` (AsrConversationalConfigWorkflowOverride, optional) — Configuration for conversational transcription
- `turn` (TurnConfigWorkflowOverride, optional) — Configuration for turn detection
- `tts` (TtsConversationalConfigWorkflowOverrideInput, optional) — Configuration for conversational text to speech
- `conversation` (ConversationConfigWorkflowOverrideInput, optional) — Configuration for conversational events
- `language_presets` (map from string to LanguagePresetInput, optional) — Language presets for conversations
- `vad` (VadConfigWorkflowOverride, optional) — Configuration for voice activity detection
- `agent` (AgentConfigApiModelWorkflowOverrideInput, optional) — Agent specific configuration

### WorkflowPhoneNumberNodeModelInputTransferDestination

- `type`: `phone`
  - `phone_number` (string, required)
- `type`: `phone_dynamic_variable`
  - `phone_number` (string, required)
- `type`: `sip_uri`
  - `sip_uri` (string, required)
- `type`: `sip_uri_dynamic_variable`
  - `sip_uri` (string, required)

### WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem

- `type`: `dynamic`
  - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
  - `value` (string, required) — The dynamic variable name to resolve
- `type`: `static`
  - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
  - `value` (string, required) — The header value

### WorkflowPhoneNumberNodeModelInputPostDialDigits

- `type`: `dynamic`
  - `value` (string, required) — The dynamic variable name to resolve
- `type`: `static`
  - `value` (string, required) — DTMF digits to send after call connects (e.g., 'ww1234' for extension)

### UuiTransferConfig

User-to-User Information envelope for SIP REFER transfers (RFC 7433). Outbound payloads are hex-encoded (the only encoding RFC 7433 defines). The protocol discriminator axis lets per-platform formats (Talkdesk, Genesys, ...) be expressed by configuration rather than scattered transfer flags. Further axes (ASCII encoding, header name, purpose/content parameters) can be added here without touching the transfer model.

- `data` (string, required) — UUI payload to send on SIP REFER transfers. Supports inline dynamic variables and is hex-encoded at transfer time.
- `protocol_discriminator` (string, optional) — Optional one-octet protocol discriminator (two hex digits, e.g. '00'). Required by platforms such as Genesys Cloud, which otherwise strip the first octet of the payload. Leave unset for platforms like Talkdesk that expect a bare hex payload.
- `protocol_discriminator_mode` (enum, optional, default: prefix) — How to attach protocol\_discriminator. 'prefix' prepends the octet to the hex payload (User-to-User=XX\<hex>;encoding=hex). 'pd\_parameter' sends it as a separate parameter (User-to-User=\<hex>;pd=XX;encoding=hex). Ignored when protocol\_discriminator is unset.
  - Allowed values: `prefix`, `pd_parameter`

### WorkflowToolLocator

- `tool_id` (string, required)
- `schema_overrides` (map from string to WorkflowToolLocatorSchemaOverridesValue, optional) — Per-node parameter overrides applied on top of the tool's own configuration. Keys are dotted parameter paths (webhook tools prefix keys with path_params./query_params./request_body.). These take precedence over any overrides already defined on the tool itself.

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
- `type` ("node_id", optional)

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

### AsrConversationalConfigOverride

- `keywords` (list of string, optional) — Keywords to boost prediction probability for

### TurnConfigOverride

- `soft_timeout_config` (SoftTimeoutConfigOverride, optional) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.

### TtsConversationalConfigOverride

- `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
  - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
- `voice_id` (string, optional) — The voice ID to use for TTS
- `supported_voices` (list of SupportedVoice, optional) — Additional supported voices for the agent
- `stability` (double, optional) — The stability of generated speech
- `speed` (double, optional) — The speed of generated speech
- `similarity_boost` (double, optional) — The similarity boost for generated speech
- `pronunciation_dictionary_locators` (list of PydanticPronunciationDictionaryVersionLocator, optional) — The pronunciation dictionary locators

### ConversationConfigOverride

- `text_only` (boolean, optional) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
- `max_duration_seconds` (integer, optional) — The maximum duration of a conversation in seconds

### AgentConfigOverrideOutput

- `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional) — Language of the agent - used for ASR and TTS
- `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
- `prompt` (PromptAgentApiModelOverrideOutput, optional) — The prompt for the agent

### BuiltInToolsOutput

System tools a conversational agent can be given. Deliberately not named ConversationalBuiltInTools: BuiltInToolsInput and BuiltInToolsOutput are part of the public API spec and the generated SDKs.

- `transfer_to_agent` (SystemToolConfigOutput, optional) — The transfer to agent tool
- `end_call` (SystemToolConfigOutput, optional) — The end call tool
- `language_detection` (SystemToolConfigOutput, optional) — The language detection tool
- `transfer_to_number` (SystemToolConfigOutput, optional) — The transfer to number tool
- `skip_turn` (SystemToolConfigOutput, optional) — The skip turn tool
- `play_keypad_touch_tone` (SystemToolConfigOutput, optional) — The play DTMF tool
- `voicemail_detection` (SystemToolConfigOutput, optional) — The voicemail detection tool

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

### WidgetTextContentsTranslation

- `source` (map from string to string, optional) — The source text each translated field was derived from
- `text` (map from string to string, optional) — The last auto-translated output for each translated field

### WidgetTermsTranslation

- `source_hash` (string, required)
- `text` (string, required)

### AsrConversationalConfigOverrideConfig

- `keywords` (boolean, optional, default: false) — Whether to allow overriding the keywords field.

### TurnConfigOverrideConfig

- `soft_timeout_config` (SoftTimeoutConfigOverrideConfig, optional) — Configures overrides for nested fields.

### TtsConversationalConfigOverrideConfig

- `model_id` (boolean, optional, default: false) — Whether to allow overriding the model_id field.
- `voice_id` (boolean, optional, default: false) — Whether to allow overriding the voice_id field.
- `supported_voices` (boolean, optional, default: false) — Whether to allow overriding the supported_voices field.
- `stability` (boolean, optional, default: false) — Whether to allow overriding the stability field.
- `speed` (boolean, optional, default: false) — Whether to allow overriding the speed field.
- `similarity_boost` (boolean, optional, default: false) — Whether to allow overriding the similarity_boost field.
- `pronunciation_dictionary_locators` (boolean, optional, default: false) — Whether to allow overriding the pronunciation_dictionary_locators field.

### ConversationConfigOverrideConfig

- `text_only` (boolean, optional, default: false) — Whether to allow overriding the text_only field.
- `max_duration_seconds` (boolean, optional, default: false) — Whether to allow overriding the max_duration_seconds field.

### AgentConfigOverrideConfig

- `first_message` (boolean, optional, default: false) — Whether to allow overriding the first_message field.
- `language` (boolean, optional, default: false) — Whether to allow overriding the language field.
- `max_conversation_duration_message` (boolean, optional, default: false) — Whether to allow overriding the max_conversation_duration_message field.
- `prompt` (PromptAgentApiModelOverrideConfig, optional) — Configures overrides for nested fields.

### ConversationInitiationClientDataWebhookRequestHeadersValue

### ContentConfig

- `sexual` (ContentThresholdGuardrail, optional)
- `violence` (ContentThresholdGuardrail, optional)
- `harassment` (ContentThresholdGuardrail, optional)
- `self_harm` (ContentThresholdGuardrail, optional)
- `profanity` (ContentThresholdGuardrail, optional)
- `religion_or_politics` (ContentThresholdGuardrail, optional)
- `medical_and_legal_information` (ContentThresholdGuardrail, optional)

### ContentGuardrailInputTriggerAction

- `type`: `end_call`
- `type`: `retry`
  - `feedback` (string, optional, default: Your response was blocked by a guardrail that blocks content that matches this condition/category: '{{trigger_reason}}' During your next turn you must tell the user "I'm sorry but I can't answer that question, would you like to know something else?".) — Custom feedback to inject into the agent when retrying after guardrail trigger.

### CustomGuardrailsConfigInput

Config container for custom guardrails list

- `configs` (list of CustomGuardrailConfig, optional)

### AstNodeInput

- `type`: `add_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `and_operator`
  - `children` (list of AstNodeInput, required) — Child nodes of the logical operator.
- `type`: `boolean_literal`
  - `value` (boolean, required) — Value of this literal.
- `type`: `conditional_operator`
  - `condition` (AstNodeInput, required) — Condition deciding which expression should be selected.
  - `falseExpression` (AstNodeInput, required) — Expression selected if the condition is false.
  - `trueExpression` (AstNodeInput, required) — Expression selected if the condition is true.
- `type`: `div_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `dynamic_variable`
  - `name` (string, required) — The name of the dynamic variable.
- `type`: `eq_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `gt_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `gte_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `llm`
  - `value_schema` (LlmLiteralJsonSchemaProperty, optional) — JSON schema describing the value that the LLM should extract.
  - `prompt` (string, optional, deprecated) — The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead.
- `type`: `lt_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `lte_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `mul_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `neq_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `null_literal`
- `type`: `number_literal`
  - `value` (AstNumberNodeInputValue, required) — Value of this literal.
- `type`: `or_operator`
  - `children` (list of AstNodeInput, required) — Child nodes of the logical operator.
- `type`: `string_literal`
  - `value` (string, required) — Value of this literal.
- `type`: `sub_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.

### AsrConversationalConfigWorkflowOverride

- `quality` ("high", optional) — The quality of the transcription
- `provider` (enum, optional, default: scribe_realtime) — The provider of the transcription service
  - Allowed values: `elevenlabs`, `scribe_realtime`
- `user_input_audio_format` (enum, optional, default: pcm_16000) — The format of the audio to be transcribed
  - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
- `keywords` (list of string, optional) — Keywords to boost prediction probability for

### TurnConfigWorkflowOverride

- `turn_timeout` (double, optional) — Maximum wait time for the user's reply before re-engaging the user
- `initial_wait_time` (double, optional) — How long the agent will wait for the user to start the conversation if the first message is empty. If not set, uses the regular turn_timeout.
- `silence_end_call_timeout` (double, optional) — Maximum wait time since the user last spoke before terminating the call
- `turn_eagerness` (enum, optional, default: normal) — Controls how eager the agent is to respond. Low = less eager (waits longer), Standard = default eagerness, High = more eager (responds sooner)
  - Allowed values: `patient`, `normal`, `eager`
- `spelling_patience` (enum, optional, default: auto) — Controls if the agent should be more patient when user is spelling numbers and named entities. Auto = model based, Off = never wait extra
  - Allowed values: `auto`, `off`
- `speculative_turn` (boolean, optional) — When enabled, starts generating LLM responses during silence before full turn confidence is reached, reducing perceived latency. May increase LLM costs.
- `retranscribe_on_turn_timeout` (boolean, optional) — When enabled, if VAD detects no speech, attempts to re-transcribe accumulated audio at turn timeout. Disables silence discount billing for affected turns.
- `turn_model` (enum, optional, default: turn_v3) — Version of the turn detection model to use.
  - Allowed values: `turn_v2`, `turn_v3`
- `interruption_ignore_terms` (list of string, optional) — List of terms that should not trigger an interruption when spoken by the user (e.g. 'gotcha', 'understood'). Uses case-insensitive exact matching.
- `interruption_ignore_term_languages` (list of string, optional) — Language codes for which preset ignore-term categories have been activated. Stored explicitly so display is not inferred from term overlap.
- `merge_with_default_ignore_terms` (boolean, optional) — When enabled, the curated default terms for interruption_ignore_term_languages are used in addition to interruption_ignore_terms.
- `transcribe_on_disabled_interruptions` (boolean, optional) — When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.
- `soft_timeout_config` (SoftTimeoutConfigWorkflowOverride, optional) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.

### TtsConversationalConfigWorkflowOverrideInput

- `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
  - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
- `voice_id` (string, optional) — The voice ID to use for TTS
- `supported_voices` (list of SupportedVoice, optional) — Additional supported voices for the agent
- `expressive_mode` (boolean, optional) — When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.
- `suggested_audio_tags` (list of SuggestedAudioTag, optional) — Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.
- `agent_output_audio_format` (enum, optional, default: pcm_16000) — The audio format to use for TTS
  - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
- `optimize_streaming_latency` (integer, optional) — Deprecated: this field is a no-op and is ignored.
- `stability` (double, optional) — The stability of generated speech
- `speed` (double, optional) — The speed of generated speech
- `similarity_boost` (double, optional) — The similarity boost for generated speech
- `text_normalisation_type` (enum, optional, default: system_prompt) — Method for converting numbers to words before converting text to speech. If set to SYSTEM_PROMPT, the system prompt will be updated to include normalization instructions. If set to ELEVENLABS, the text will be normalized after generation, incurring slight additional latency.
  - Allowed values: `system_prompt`, `elevenlabs`
- `pronunciation_dictionary_locators` (list of PydanticPronunciationDictionaryVersionLocator, optional) — The pronunciation dictionary locators
- `enable_phoneme_tags` (boolean, optional) — Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.
- `audio_effects` (EffectsSpecInput, optional) — Optional TTS effects spec: filter preset, distance (proximity EQ), and environment (convolution reverb).

### ConversationConfigWorkflowOverrideInput

- `text_only` (boolean, optional) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
- `max_duration_seconds` (integer, optional) — The maximum duration of a conversation in seconds
- `client_events` (list of enum, optional) — The events that will be sent to the client
  - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `context_usage`, `internal_turn_probability`, `internal_tentative_agent_response`
- `file_input` (FileInputConfigWorkflowOverride, optional) — Configuration for file input (image/PDF uploads) during conversations.
- `monitoring_enabled` (boolean, optional) — Enable real-time monitoring of conversations via WebSocket
- `monitoring_events` (list of enum, optional) — The events that will be sent to monitoring connections.
  - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `context_usage`, `internal_turn_probability`, `internal_tentative_agent_response`
- `dtmf_input_settings` (DtmfInputConfig, optional) — Configure DTMF (keypad) input collection during phone calls
- `background_sound` (BackgroundSoundConfigWorkflowOverride, optional) — Configuration for background sound during conversations.
- `source_attribution` (boolean, optional) — When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.

### LanguagePresetInput

- `overrides` (ConversationConfigClientOverrideInput, required) — The overrides for the language preset
- `first_message_translation` (LanguagePresetTranslation, optional) — The translation of the first message
- `soft_timeout_translation` (LanguagePresetTranslation, optional) — The translation of the soft timeout message

### VadConfigWorkflowOverride

### AgentConfigApiModelWorkflowOverrideInput

- `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional) — Language of the agent - used for ASR and TTS
- `hinglish_mode` (boolean, optional) — When enabled and language is Hindi, the agent will respond in Hinglish
- `dynamic_variables` (DynamicVariablesConfigWorkflowOverride, optional) — Configuration for dynamic variables
- `disable_first_message_interruptions` (boolean, optional) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
- `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
- `text_behavior_overrides` (map from string to BehaviorOverride, optional) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
- `prompt` (PromptAgentApiModelWorkflowOverrideInput, optional) — The prompt for the agent

### WorkflowToolLocatorSchemaOverridesValue

- `source`: `constant`
  - `constant_value` (ConstantSchemaOverrideConstantValue, optional) — The constant value to use
- `source`: `dynamic_variable`
  - `dynamic_variable` (string, required) — The name of the dynamic variable to use
- `source`: `llm`
  - `prompt` (string, optional) — Prompt override for the LLM. If not provided, the original schema description is used.
- `source`: `omit`

### UnitTestToolCallParameterEval

- `type`: `anything`
- `type`: `exact`
  - `expected_value` (string, required) — The exact string value that the parameter must match.
- `type`: `llm`
  - `description` (string, required) — A description of the evaluation strategy to use for the test.
- `type`: `regex`
  - `pattern` (string, required) — A regex pattern to match the agent's response against.

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

### SoftTimeoutConfigOverride

- `message` (string, optional) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
- `additional_soft_timeout_messages` (list of string, optional) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.

### PromptAgentApiModelOverrideOutput

- `prompt` (string, optional) — The prompt for the agent
- `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
- `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional) — A list of knowledge bases to be used by the agent

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

### SoftTimeoutConfigOverrideConfig

- `message` (boolean, optional, default: false) — Whether to allow overriding the message field.
- `additional_soft_timeout_messages` (boolean, optional, default: false) — Whether to allow overriding the additional_soft_timeout_messages field.

### PromptAgentApiModelOverrideConfig

- `prompt` (boolean, optional, default: false) — Whether to allow overriding the prompt field.
- `llm` (boolean, optional, default: false) — Whether to allow overriding the llm field.
- `tool_ids` (boolean, optional, default: false) — Whether to allow overriding the tool_ids field.
- `native_mcp_server_ids` (boolean, optional, default: false) — Whether to allow overriding the native_mcp_server_ids field.
- `knowledge_base` (boolean, optional, default: false) — Whether to allow overriding the knowledge_base field.

### ConvAiSecretLocator

Used to reference a secret from the agent's secret store.

- `secret_id` (string, required)

### ContentThresholdGuardrail

- `is_enabled` (boolean, optional, default: false)
- `threshold` (ContentThresholdGuardrailThreshold, optional)

### CustomGuardrailConfig

Single custom guardrail configuration

- `name` (string, required) — User-facing name for this guardrail
- `prompt` (string, required) — Instruction describing what to block, e.g. 'don't talk about politics'
- `is_enabled` (boolean, optional, default: false)
- `execution_mode` (enum, optional, default: streaming)
  - Allowed values: `streaming`, `blocking`
- `model` (enum, optional, default: gemini-3.1-flash-lite) — LLM model to use for custom guardrail evaluation
  - Allowed values: `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `claude-haiku-4-5`, `claude-sonnet-4-6`, `gpt-5.4-nano`, `gpt-5.4-mini`
- `history_message_count` (integer, optional, default: 0) — How much recent history the guardrail sees before the reply it evaluates, counted in user messages (the agent replies between them are included too). The guardrail always gets a single \<conversation\_history> transcript ending in the evaluated reply, marked 'AGENT \[current reply]:'. 0 (default) adds no prior history (just that line); 1 adds the latest user message onward.
- `trigger_action` (CustomGuardrailConfigTriggerAction, optional)
- `evaluate_full_response_only` (boolean, optional, default: false) — Evaluate once against the complete non-TTS response instead of cumulative partials. Requires blocking mode.

### LlmLiteralJsonSchemaProperty

- `type` (LlmLiteralJsonSchemaPropertyType, required)
- `description` (string, required)
- `enum` (list of string, optional) — List of allowed string values for string type parameters

### AstNumberNodeInputValue

Value of this literal.

### SoftTimeoutConfigWorkflowOverride

- `timeout_seconds` (double, optional) — Time in seconds before showing the predefined message while waiting for LLM response. Set to -1 to disable.
- `message` (string, optional) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
- `additional_soft_timeout_messages` (list of string, optional) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.
- `use_llm_generated_message` (boolean, optional) — If enabled, the soft timeout message will be generated dynamically instead of using the static message.
- `randomize_fillers` (boolean, optional) — If enabled, shuffle the order of static soft timeout messages once at the start of each turn. Only applies when use_llm_generated_message is false.
- `max_soft_timeouts_per_generation` (integer, optional) — Maximum filler messages while waiting for a single LLM response. Fires every timeout_seconds until the LLM streams content or this limit is reached.
- `llm_generated_message_prompt_override` (string, optional) — Custom prompt for generating the soft timeout filler message when use\_llm\_generated\_message is enabled. Recent conversation context is provided as a separate user message. If not set, the default prompt will be used. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
- `disable_until_first_user_message` (boolean, optional) — When true, soft timeout fillers are suppressed until the conversation has at least one real user message. Prevents fillers during the agent's opening turn (e.g. workflow generate-immediately / tool calls before the user speaks).

### EffectsSpecInput

Filter preset, distance (proximity EQ), and environment (convolution reverb).

- `filter_preset_id` (string, optional)
- `distance` (double, optional, default: 0)
- `environment_id` (string, optional)
- `background_noise_id` (string, optional)
- `send_level` (double, optional, default: 1)
- `seed` (integer, optional)

### FileInputConfigWorkflowOverride

- `enabled` (boolean, optional) — When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.
- `max_files_in_memory` (integer, optional) — Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.
- `max_files_per_conversation` (integer, optional) — Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.

### BackgroundSoundConfigWorkflowOverride

- `source_type` ("preset", optional) — The type of background sound source.
- `source_id` (enum, optional) — Identifier for the sound source.
  - Allowed values: `office2`, `office1`, `restaurant`, `city`, `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
- `volume` (double, optional) — Volume level for background sound (0.01 to 1.0).
- `crossfade_loop` (boolean, optional) — Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.

### ConversationConfigClientOverrideInput

- `asr` (AsrConversationalConfigOverride, optional) — Configuration for conversational transcription
- `turn` (TurnConfigOverride, optional) — Configuration for turn detection
- `tts` (TtsConversationalConfigOverride, optional) — Configuration for conversational text to speech
- `conversation` (ConversationConfigOverride, optional) — Configuration for conversational events
- `agent` (AgentConfigOverrideInput, optional) — Agent specific configuration

### DynamicVariablesConfigWorkflowOverride

- `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values

### PromptAgentApiModelWorkflowOverrideInput

- `prompt` (string, optional) — The prompt for the agent
- `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `reasoning_effort` (enum, optional) — Reasoning effort of the model. Only available for some models.
  - Allowed values: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`
- `thinking_budget` (integer, optional) — Max number of tokens used for thinking. Use 0 to turn off if supported by the model.
- `enable_reasoning_summary` (boolean, optional) — Enable model reasoning summaries. When disabled, we do not request summaries from provider if possible for faster TTFB. Not ZRM compatible.
- `temperature` (double, optional) — The temperature for the LLM. Defaults to 0. Set to null to omit the parameter from the LLM request entirely (useful for custom LLMs that reject the temperature field).
- `max_tokens` (integer, optional) — If greater than 0, maximum number of tokens the LLM can predict
- `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
- `built_in_tools` (BuiltInToolsWorkflowOverrideInput, optional) — Built-in system tools to be used by the agent
- `enable_parallel_tool_calls` (boolean, optional) — Enable parallel tool calling. When enabled, the agent can execute multiple tools in parallel within a single turn. Not supported by all models.
- `mcp_server_ids` (list of string, optional) — A list of MCP server ids to be used by the agent
- `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional) — A list of knowledge bases to be used by the agent
- `custom_llm` (CustomLlm, optional) — Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
- `ignore_default_personality` (boolean, optional) — Whether to remove the default personality lines from the system prompt
- `rag` (RagConfigWorkflowOverrideInput, optional) — Configuration for RAG
- `timezone` (string, optional) — Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references.
- `backup_llm_config` (PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig, optional) — Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.
- `cascade_timeout_seconds` (double, optional) — Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.
- `tools` (list of PromptAgentApiModelWorkflowOverrideInputToolsItem, optional) — A list of tools that the agent can use over the course of the conversation, use tool_ids instead

### ConstantSchemaOverrideConstantValue

The constant value to use

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

### ContentThresholdGuardrailThreshold

### CustomGuardrailConfigTriggerAction

- `type`: `end_call`
- `type`: `retry`
  - `feedback` (string, optional, default: Your response was blocked by a guardrail that blocks content that matches this condition/category: '{{trigger_reason}}' During your next turn you must tell the user "I'm sorry but I can't answer that question, would you like to know something else?".) — Custom feedback to inject into the agent when retrying after guardrail trigger.

### LlmLiteralJsonSchemaPropertyType

### AgentConfigOverrideInput

- `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional) — Language of the agent - used for ASR and TTS
- `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
- `prompt` (PromptAgentApiModelOverrideInput, optional) — The prompt for the agent

### BuiltInToolsWorkflowOverrideInput

- `transfer_to_agent` (SystemToolConfigInput, optional) — The transfer to agent tool
- `end_call` (SystemToolConfigInput, optional) — The end call tool
- `language_detection` (SystemToolConfigInput, optional) — The language detection tool
- `transfer_to_number` (SystemToolConfigInput, optional) — The transfer to number tool
- `skip_turn` (SystemToolConfigInput, optional) — The skip turn tool
- `play_keypad_touch_tone` (SystemToolConfigInput, optional) — The play DTMF tool
- `voicemail_detection` (SystemToolConfigInput, optional) — The voicemail detection tool

### RagConfigWorkflowOverrideInput

- `enabled` (boolean, optional)
- `embedding_model` (enum, optional, default: e5_mistral_7b_instruct)
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
- `max_vector_distance` (double, optional) — Maximum vector distance of retrieved chunks.
- `max_documents_length` (integer, optional) — Maximum total length of document chunks retrieved from RAG.
- `max_retrieved_rag_chunks_count` (integer, optional) — Maximum number of RAG document chunks to initially retrieve from the vector store. These are then further filtered by vector distance and total length.
- `num_candidates` (integer, optional) — Number of candidates evaluated in ANN vector search. Higher number means better results, but higher latency. Minimum recommended value is 100. If disabled, the default value is used.
- `query_rewrite_prompt_override` (string, optional) — Custom prompt for rewriting user queries before RAG retrieval. The conversation history will be automatically appended at the end. If not set, the default prompt will be used.
- `knowledge_base_tool_info` (KnowledgeBaseToolInfo, optional) — When set, the agent uses the knowledge_base tool instead of the legacy knowledge_base_rag tool. None means the agent is not opted in.

### PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig

Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.

### PromptAgentApiModelWorkflowOverrideInputToolsItem

The type of tool

- `type`: `api_integration_webhook`
  - `api_integration_connection_id` (string, required)
  - `api_integration_id` (string, required)
  - `description` (string, required) — Description of when the tool should be used and what it does.
  - `name` (string, required)
  - `api_schema_overrides` (ApiIntegrationWebhookOverrides, optional) — User overrides applied on top of the base api_schema
  - `assignments` (list of DynamicVariableAssignment, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
  - `dynamic_variables` (DynamicVariablesConfig, optional) — Configuration for dynamic variables
  - `execution_mode` (enum, optional, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
    - Allowed values: `immediate`, `post_tool_speech`, `async`
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
  - `tool_version` (string, optional, default: 1.0.0) — The version of the API integration tool
  - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
  - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
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
  - `parameters` (ObjectJsonSchemaPropertyInput, optional) — Schema for any parameters to pass to the client
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
  - `params` (SystemToolConfigInputParams, required)
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
  - `api_schema` (WebhookToolApiSchemaConfigInput, required) — The schema for the outgoing webhoook, including parameters and URL specification
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

### WorkflowToolNestedToolsStepModelOutputResultsItem

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

### PhoneNumberTransferPostDialDigits

- `type`: `dynamic`
  - `value` (string, required) — The dynamic variable name to resolve
- `type`: `static`
  - `value` (string, required) — DTMF digits to send after call connects (e.g., 'ww1234' for extension)

### LiteralJsonSchemaPropertyType

### LiteralJsonSchemaPropertyConstantValue

A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.

### PromptAgentApiModelOverrideInput

- `prompt` (string, optional) — The prompt for the agent
- `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
- `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional) — A list of knowledge bases to be used by the agent

### SystemToolConfigInput

A system tool is a tool that is used to call a system method in the server

- `name` (string, required)
- `params` (SystemToolConfigInputParams, required)
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

### BackupLlmDefault

- `preference` ("default", optional)

### BackupLlmDisabled

- `preference` ("disabled", optional)

### BackupLlmOverride

- `order` (list of enum, required)
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `preference` ("override", optional)

### ObjectJsonSchemaPropertyInput

- `property_kind` (enum, optional, default: object)
  - Allowed values: `array`, `object`
- `description` (string, optional, default: )
- `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
- `constant_value` (map from string to any, optional) — When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
- `type` ("object", optional)
- `required` (list of string, optional)
- `properties` (map from string to ObjectJsonSchemaPropertyInputPropertiesValue, optional)
- `required_constraints` (RequiredConstraints, optional) — Wrapper for anyOf/allOf composition constraints scoped to required fields.

### SystemToolConfigInputParams

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
  - `transfers` (list of AgentTransferInput, required)
- `system_tool_type`: `transfer_to_number`
  - `transfers` (list of PhoneNumberTransfer, required)
  - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
- `system_tool_type`: `voicemail_detection`
  - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).

### WebhookToolApiSchemaConfigInput

- `url` (string, required) — The URL that the webhook will be sent to. May include path parameters, e.g. [https://example.com/agents/\{agent\_id}](https://example.com/agents/\{agent_id})
- `request_headers` (map from string to WebhookToolApiSchemaConfigInputRequestHeadersValue, optional) — Headers that should be included in the request
- `method` (enum, optional, default: GET) — The HTTP method to use for the webhook
  - Allowed values: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- `path_params_schema` (map from string to LiteralJsonSchemaProperty, optional) — Schema for path parameters, if any. The keys should match the placeholders in the URL.
- `query_params_schema` (QueryParamsJsonSchemaInput, optional) — Schema for any query params, if any. These will be added to end of the URL as query params. Note: properties in a query param must all be literal types
- `request_body_schema` (ObjectJsonSchemaPropertyInput, optional) — Schema for the body parameters, if any. Used for POST/PATCH/PUT requests. The schema should be an object which will be sent as the json body
- `response_body_schema` (ObjectJsonSchemaPropertyInput, optional) — Schema describing the expected response body structure. For documentation only; not surfaced to the LLM.
- `response_filter` (ResponseFilter, optional) — Optional allow-list filter applied to the response before the LLM sees it, so large responses don't pollute the context. Defaults to the full response.
- `content_type` (enum, optional, default: application/json) — Content type for the request body. Only applies to POST/PUT/PATCH requests.
  - Allowed values: `application/json`, `application/x-www-form-urlencoded`
- `auth_resolved_params` (list of string, optional) — URL placeholders resolved from the auth connection (e.g. secrets injected via UrlSecretAuthConnection) rather than from path_params_schema.
- `auth_connection` (WebhookToolApiSchemaConfigInputAuthConnection, optional) — Optional auth connection to use for authentication with this webhook

### ArrayJsonSchemaPropertyOutputItems

Schema for array elements.

### ObjectJsonSchemaPropertyInputPropertiesValue

### AgentTransferInput

- `condition` (string, required)
- `agent_id` (string, optional)
- `node_id` (string, optional)
- `delay_ms` (integer, optional, default: 0)
- `transfer_message` (string, optional)
- `enable_transferred_agent_first_message` (boolean, optional, default: false)
- `is_workflow_node_transfer` (boolean, optional, default: false)
- `preserve_client_tts_overrides` (boolean, optional, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.

### WebhookToolApiSchemaConfigInputRequestHeadersValue

### QueryParamsJsonSchemaInput

- `properties` (map from string to LiteralJsonSchemaProperty, required)
- `required` (list of string, optional)

### WebhookToolApiSchemaConfigInputAuthConnection

Optional auth connection to use for authentication with this webhook

### ArrayJsonSchemaPropertyInput

- `property_kind` (enum, optional, default: array)
  - Allowed values: `array`, `object`
- `description` (string, optional, default: )
- `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
- `constant_value` (list of any, optional) — When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
- `type` ("array", optional)
- `items` (ArrayJsonSchemaPropertyInputItems, optional) — Schema for array elements.

### ArrayJsonSchemaPropertyInputItems

Schema for array elements.

## Examples

**Request**

```json
{
  "tests": [
    {
      "test_id": "test_id"
    }
  ]
}
```

**Response**

```json
{
  "id": "id",
  "test_runs": [
    {
      "test_run_id": "test_run_id",
      "test_invocation_id": "test_invocation_id",
      "agent_id": "agent_id",
      "status": "pending",
      "test_id": "test_id",
      "test_info": {
        "type": "llm"
      },
      "branch_id": "branch_id",
      "version_id": "version_id",
      "ran_against_draft": true,
      "workflow_node_id": "workflow_node_id",
      "agent_responses": [
        {
          "role": "user",
          "time_in_call_secs": 1
        }
      ],
      "test_name": "test_name",
      "condition_result": {
        "result": "success"
      },
      "last_updated_at_unix": 1,
      "metadata": {
        "workspace_id": "workspace_id",
        "test_name": "test_name",
        "ran_by_user_email": "ran_by_user_email"
      },
      "root_folder_id": "root_folder_id",
      "root_folder_name": "root_folder_name",
      "environment": "environment",
      "credits_used": 1
    }
  ],
  "agent_id": "agent_id",
  "branch_id": "branch_id",
  "version_id": "version_id",
  "ran_against_draft": true,
  "created_at": 1,
  "folder_id": "folder_id",
  "repeat_count": 1,
  "bucketing_status": "pending",
  "result_groups": [
    {
      "test_id": "test_id",
      "test_name": "test_name",
      "buckets": [
        {
          "test_run_ids": [
            "test_run_ids"
          ],
          "title": "title",
          "reason": "reason",
          "status": "pending"
        }
      ],
      "workflow_node_id": "workflow_node_id"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.runTests("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        tests: [
            {
                testId: "test_id",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, SingleTestRunRequestModel

client = ElevenLabs()

client.conversational_ai.agents.run_tests(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    tests=[
        SingleTestRunRequestModel(
            test_id="test_id",
        )
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests"

	payload := strings.NewReader("{\n  \"tests\": [\n    {\n      \"test_id\": \"test_id\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tests\": [\n    {\n      \"test_id\": \"test_id\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests")
  .header("Content-Type", "application/json")
  .body("{\n  \"tests\": [\n    {\n      \"test_id\": \"test_id\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests', [
  'body' => '{
  "tests": [
    {
      "test_id": "test_id"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tests\": [\n    {\n      \"test_id\": \"test_id\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["tests": [["test_id": "test_id"]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests")! as URL,
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
