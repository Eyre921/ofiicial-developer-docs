---
title: "Run conversation evaluation"
source: https://elevenlabs.io/docs/api-reference/conversations/analysis/run-evaluation.md
path: docs/api-reference/conversations/analysis/run-evaluation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Run conversation evaluation

POST https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/analysis/evaluations/run
Content-Type: application/json

Rerun a specific evaluation for a conversation.

Reference: https://elevenlabs.io/docs/api-reference/conversations/analysis/run-evaluation

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `conversation_id` (string, required) — ID of the conversation

### Body (application/json)

This endpoint expects a RunConversationEvaluationsRequest.

- `evaluation_id` (string, required) — ID of the single evaluation criterion to rerun.
- `scope` (enum, optional, default: conversation)
  - Allowed values: `conversation`, `agent`

## Response

### 200

Successful Response

- `agent_id` (string, required)
- `status` (enum, required)
  - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
- `metadata` (ConversationHistoryMetadataCommonModel, required)
- `conversation_id` (string, required)
- `has_audio` (boolean, required)
- `has_user_audio` (boolean, required)
- `has_response_audio` (boolean, required)
- `has_auxiliary_audio` (boolean, required)
- `transcript` (list of ConversationHistoryTranscriptResponseModel, required)
- `agent_name` (string, optional, nullable)
- `conversation_product` (string, optional, default: agent)
- `user_id` (string, optional, nullable)
- `branch_id` (string, optional, nullable)
- `version_id` (string, optional, nullable) — The ID of the agent version used for this conversation
- `analysis` (ConversationHistoryAnalysisCommonModel, optional, nullable)
- `visited_agents` (list of VisitedAgentRef, optional)
- `conversation_initiation_client_data` (ConversationInitiationClientDataRequest-Output, optional)
- `environment` (string, optional, default: production)
- `tag_ids` (list of string, optional) — Conversation tag ids assigned to this conversation.
- `otlp_traces` (map from string to any, optional, nullable) — OpenTelemetry trace payload when the request uses format=opentelemetry; otherwise omitted.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ConversationHistoryMetadataCommonModel

- `start_time_unix_secs` (integer, required)
- `call_duration_secs` (integer, required)
- `cost_fiat` (double, required, nullable) — Total fiat cost of the conversation in USD, i.e. the sum of the LLM price and the non-LLM platform price (the fiat analogue of ``cost``). ``None`` when neither is set (e.g. conversations that predate fiat cost tracking).
- `accepted_time_unix_secs` (integer, optional, nullable)
- `queue_wait_secs` (double, optional, nullable) — Seconds the caller was held in the concurrency wait queue. Excluded from call_duration_secs and from billed time. None when the conversation was never queued.
- `cost` (integer, optional, nullable)
- `deletion_settings` (ConversationDeletionSettings, optional)
- `feedback` (ConversationHistoryFeedbackCommonModel, optional)
- `authorization_method` (enum, optional, default: public)
  - Allowed values: `invalid`, `public`, `authorization_header`, `signed_url`, `shareable_link`, `livekit_token`, `livekit_token_website`, `genesys_api_key`, `avaya_api_key`, `audiocodes_api_key`, `whatsapp`, `sms`
- `charging` (ConversationChargingCommonModel, optional)
- `phone_call` (ConversationHistoryMetadataCommonModelPhoneCall, optional, nullable)
- `batch_call` (ConversationHistoryBatchCallModel, optional, nullable)
- `termination_reason` (string, optional, default: )
- `error` (ConversationHistoryErrorCommonModel, optional, nullable)
- `warnings` (list of string, optional)
- `main_language` (string, optional, nullable)
- `rag_usage` (ConversationHistoryRagUsageCommonModel, optional, nullable)
- `text_only` (boolean, optional, default: false)
- `features_usage` (FeaturesUsageCommonModel, optional)
- `eleven_assistant` (ConversationHistoryElevenAssistantCommonModel, optional)
- `initiator_id` (string, optional, nullable)
- `conversation_initiation_source` (enum, optional, default: unknown) — Enum representing the possible sources for conversation initiation.
  - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
- `conversation_initiation_source_version` (string, optional, nullable)
- `timezone` (string, optional, nullable)
- `async_metadata` (AsyncConversationMetadata, optional, nullable) — Metadata for async conversation delivery (Zendesk, Slack, etc.).
- `whatsapp` (WhatsAppConversationInfo, optional, nullable)
- `sms` (SMSConversationInfo, optional, nullable)
- `agent_created_from` (enum, optional, default: unknown)
  - Allowed values: `cli`, `ui`, `api`, `template`, `unknown`
- `agent_last_updated_from` (enum, optional, default: unknown)
  - Allowed values: `cli`, `ui`, `api`, `template`, `unknown`
- `voice_rewards` (list of ConversationVoiceRewardModel, optional)

### ConversationHistoryTranscriptResponseModel

- `role` (enum, required)
  - Allowed values: `user`, `agent`
- `time_in_call_secs` (integer, required)
- `agent_metadata` (AgentMetadata, optional, nullable)
- `message` (string, optional, nullable)
- `multivoice_message` (ConversationHistoryMultivoiceMessageModel, optional, nullable) — Represents a message from a multi-voice agent.
- `tool_calls` (list of ConversationHistoryTranscriptToolCallCommonModel-Output, optional)
- `tool_results` (list of ConversationHistoryTranscriptResponseModelToolResultsItems, optional)
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
- `file_input` (ConversationHistoryTranscriptFileInputResponseModel, optional, nullable) — Deprecated: the first attachment on this turn. Use `file_inputs` to see every attachment.
- `file_inputs` (list of ConversationHistoryTranscriptFileInputResponseModel, optional) — All files attached to this turn, in the order the user attached them.
- `contextual_update_info` (ContextualUpdateInfo, optional, nullable)
- `reasoned` (boolean, optional, default: false)

### ConversationHistoryAnalysisCommonModel

- `call_successful` (enum, required)
  - Allowed values: `success`, `failure`, `unknown`
- `transcript_summary` (string, required)
- `evaluation_criteria_results` (map from string to ConversationHistoryEvaluationCriteriaResultCommonModel, optional)
- `data_collection_results` (map from string to DataCollectionResultCommonModel, optional)
- `evaluation_criteria_results_list` (list of ConversationHistoryEvaluationCriteriaResultCommonModel, optional)
- `data_collection_results_list` (list of DataCollectionResultCommonModel, optional)
- `call_success_score` (double, optional, nullable)
- `call_summary_title` (string, optional, nullable)
- `scoped` (list of ScopedAnalysisResult, optional)

### VisitedAgentRef

An agent (and optional branch) that participated in the call, in first-seen transcript order.

- `agent_id` (string, required)
- `branch_id` (string, optional, nullable)

### ConversationInitiationClientDataRequest-Output

- `conversation_config_override` (ConversationConfigClientOverride-Output, optional)
- `custom_llm_extra_body` (map from string to any, optional)
- `user_id` (string, optional, nullable) — ID of the end user participating in this conversation (for agent owner's user identification)
- `source_info` (ConversationInitiationSourceInfo, optional) — Information about the source of conversation initiation
- `branch_id` (string, optional, nullable) — ID of the agent branch to use for this conversation
- `environment` (string, optional, nullable) — Environment to use for resolving environment variables
- `starting_workflow_node_id` (string, optional, nullable) — If set, start the workflow at this node id instead of the default entry
- `procedure_ids` (list of string, optional, nullable) — If set, only these procedures are available to the starting agent. Each ID must be attached to that agent; unknown IDs fail conversation start. An empty list disables all of that agent's procedures. Not applied after an agent transfer. Requires enable_procedure_ids_from_client.
- `dynamic_variables` (map from string to any, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ConversationDeletionSettings

- `deletion_time_unix_secs` (integer, optional, nullable)
- `deleted_logs_at_time_unix_secs` (integer, optional, nullable)
- `deleted_audio_at_time_unix_secs` (integer, optional, nullable)
- `deleted_transcript_at_time_unix_secs` (integer, optional, nullable)
- `delete_transcript_and_pii` (boolean, optional, default: false)
- `delete_audio` (boolean, optional, default: false)

### ConversationHistoryFeedbackCommonModel

- `type` (enum, optional, nullable)
  - Allowed values: `thumbs`, `rating`
- `overall_score` (enum, optional, nullable)
  - Allowed values: `like`, `dislike`
- `likes` (integer, optional, default: 0)
- `dislikes` (integer, optional, default: 0)
- `rating` (integer, optional, nullable)
- `comment` (string, optional, nullable)

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

### ConversationHistoryMetadataCommonModelPhoneCall

- `type`: `exotel` (ConversationHistoryExotelPhoneCallModel)
  - `agent_number` (string, required)
  - `call_sid` (string, required)
  - `direction` (enum, required, default: inbound)
    - Allowed values: `inbound`, `outbound`
  - `external_number` (string, required)
  - `phone_number_id` (string, required)
  - `stream_sid` (string, required)
- `type`: `sip_trunking` (ConversationHistorySIPTrunkingPhoneCallModel)
  - `agent_number` (string, required)
  - `call_sid` (string, required)
  - `direction` (enum, required, default: inbound)
    - Allowed values: `inbound`, `outbound`
  - `external_number` (string, required)
  - `phone_number_id` (string, required)
  - `call_id` (string, optional, nullable)
  - `sip_header_dynamic_variables` (map from string to string, optional)
- `type`: `twilio` (ConversationHistoryTwilioPhoneCallModel)
  - `agent_number` (string, required)
  - `call_sid` (string, required)
  - `direction` (enum, required, default: inbound)
    - Allowed values: `inbound`, `outbound`
  - `external_number` (string, required)
  - `phone_number_id` (string, required)
  - `stream_sid` (string, required)

### ConversationHistoryBatchCallModel

- `batch_call_id` (string, required)
- `batch_call_recipient_id` (string, required)
- `campaign` (BatchCallingCampaignInformation, optional, nullable)

### ConversationHistoryErrorCommonModel

- `code` (integer, required)
- `reason` (string, optional, nullable)

### ConversationHistoryRagUsageCommonModel

- `usage_count` (integer, required)
- `embedding_model` (string, required)

### FeaturesUsageCommonModel

- `language_detection` (FeatureStatusCommonModel, optional)
- `transfer_to_agent` (FeatureStatusCommonModel, optional)
- `transfer_to_number` (FeatureStatusCommonModel, optional)
- `multivoice` (FeatureStatusCommonModel, optional)
- `dtmf_tones` (FeatureStatusCommonModel, optional)
- `external_mcp_servers` (FeatureStatusCommonModel, optional)
- `pii_zrm_workspace` (boolean, optional, default: false)
- `pii_zrm_agent` (boolean, optional, default: false)
- `tool_dynamic_variable_updates` (FeatureStatusCommonModel, optional)
- `is_livekit` (boolean, optional, default: false)
- `voicemail_detection` (FeatureStatusCommonModel, optional)
- `dtmf_input` (FeatureStatusCommonModel, optional)
- `workflow` (WorkflowFeaturesUsageCommonModel, optional)
- `agent_testing` (TestsFeatureUsageCommonModel, optional)
- `versioning` (FeatureStatusCommonModel, optional)
- `file_input` (FeatureStatusCommonModel, optional)
- `freeform_procedure` (FeatureStatusCommonModel, optional)
- `structured_procedure` (FeatureStatusCommonModel, optional)

### ConversationHistoryElevenAssistantCommonModel

- `is_eleven_assistant` (boolean, optional, default: false)

### AsyncConversationMetadata

Metadata for async conversation delivery (Zendesk, Slack, etc.).

- `delivery_status` (enum, required)
  - Allowed values: `pending`, `success`, `failed`
- `delivery_timestamp` (integer, required)
- `external_system` (string, required)
- `external_id` (string, required)
- `delivery_error` (string, optional, nullable)
- `external_link` (string, optional, nullable)
- `retry_count` (integer, optional, default: 0)
- `last_retry_timestamp` (integer, optional, nullable)
- `last_processed_external_message_id` (string, optional, nullable)

### WhatsAppConversationInfo

- `whatsapp_user_id` (string, required)
- `direction` (enum, optional, default: unknown)
  - Allowed values: `inbound`, `outbound`, `unknown`
- `whatsapp_phone_number_id` (string, optional, nullable)
- `awaiting_first_user_message` (boolean, optional, nullable)

### SMSConversationInfo

- `direction` (enum, required)
  - Allowed values: `inbound`, `outbound`
- `sms_user_phone_number` (string, required)
- `phone_number_id` (string, optional, nullable)
- `agent_phone_number` (string, optional, nullable)

### ConversationVoiceRewardModel

- `voice_id` (string, required)
- `reward_usd_cents` (double, required)

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

### ConversationHistoryTranscriptResponseModelToolResultsItems

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
- `scoring_mode` (enum, optional, nullable, default: binary)
  - Allowed values: `binary`, `numeric_uniform`
- `score` (integer, optional, nullable)
- `max_score` (integer, optional, nullable)

### DataCollectionResultCommonModel

- `data_collection_id` (string, required)
- `rationale` (string, required)
- `name` (string, optional, nullable)
- `value` (any, optional)
- `json_schema` (LiteralJsonSchemaProperty, optional, nullable) — Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.

### ScopedAnalysisResult

- `scope` (enum, required, default: conversation) — The scope of the analysis. 'conversation' uses the full transcript; 'agent' uses only the portion where the defining agent was active.
  - Allowed values: `conversation`, `agent`
- `source_agent_id` (string, required)
- `successful` (enum, required)
  - Allowed values: `success`, `failure`, `unknown`
- `source_branch_id` (string, optional, nullable) — Branch of the agent for this scoped block; disambiguates repeated agent_id.
- `evaluation_criteria_results` (map from string to ConversationHistoryEvaluationCriteriaResultCommonModel, optional)
- `data_collection_results` (map from string to DataCollectionResultCommonModel, optional)
- `success_score` (double, optional, nullable)

### ConversationConfigClientOverride-Output

- `asr` (ASRConversationalConfigOverride, optional, nullable) — Configuration for conversational transcription
- `turn` (TurnConfigOverride, optional, nullable) — Configuration for turn detection
- `tts` (TTSConversationalConfigOverride, optional, nullable) — Configuration for conversational text to speech
- `conversation` (ConversationConfigOverride, optional, nullable) — Configuration for conversational events
- `agent` (AgentConfigOverride-Output, optional, nullable) — Agent specific configuration

### ConversationInitiationSourceInfo

Information about the source of conversation initiation

- `source` (enum, optional, nullable, default: unknown) — Source of the conversation initiation
  - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
- `version` (string, optional, nullable) — The SDK version number

### ValidationErrorLocItems

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

### BatchCallingCampaignInformation

- `campaign_id` (string, required)
- `campaign_lead_id` (string, required)

### FeatureStatusCommonModel

- `enabled` (boolean, optional, default: false)
- `used` (boolean, optional, default: false)

### WorkflowFeaturesUsageCommonModel

- `enabled` (boolean, optional, default: false)
- `tool_node` (FeatureStatusCommonModel, optional)
- `standalone_agent_node` (FeatureStatusCommonModel, optional)
- `phone_number_node` (FeatureStatusCommonModel, optional)
- `end_node` (FeatureStatusCommonModel, optional)

### TestsFeatureUsageCommonModel

- `enabled` (boolean, optional, default: false)
- `tests_ran_after_last_modification` (boolean, optional, default: false)
- `tests_ran_in_last_7_days` (boolean, optional, default: false)

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

### LiteralJsonSchemaProperty

Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.

- `type` (LiteralJsonSchemaPropertyType, required)
- `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
- `enum` (list of string, optional, nullable) — List of allowed string values for string type parameters
- `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
- `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
- `allowed_values` (AllowedValues, optional, nullable) — Server-side rejection guard for an LLM-provided value: the runtime rejects any value outside the permitted set this object names, and the set is not advertised to the LLM as an enum. Only supported when the value source is `description`; combining it with dynamic_variable, is_system_provided, constant_value, or is_omitted is rejected.
- `constant_value` (LiteralJsonSchemaPropertyConstantValue, optional, nullable, default: ) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
- `allowed_values_dynamic_variable` (string, optional, default: , deprecated) — DEPRECATED: use `allowed_values` instead. When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable (must be a JSON array such as ["ws_alpha", "ws_beta"]). Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.

### ASRConversationalConfigOverride

- `keywords` (list of string, optional, nullable) — Keywords to boost prediction probability for

### TurnConfigOverride

- `soft_timeout_config` (SoftTimeoutConfigOverride, optional, nullable) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.

### TTSConversationalConfigOverride

- `model_id` (enum, optional, nullable, default: eleven_flash_v2) — The model to use for TTS
  - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
- `voice_id` (string, optional, nullable) — The voice ID to use for TTS
- `supported_voices` (list of SupportedVoice, optional, nullable) — Additional supported voices for the agent
- `stability` (double, optional, nullable) — The stability of generated speech
- `speed` (double, optional, nullable) — The speed of generated speech
- `similarity_boost` (double, optional, nullable) — The similarity boost for generated speech
- `pronunciation_dictionary_locators` (list of PydanticPronunciationDictionaryVersionLocator, optional, nullable) — The pronunciation dictionary locators

### ConversationConfigOverride

- `text_only` (boolean, optional, nullable) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
- `max_duration_seconds` (integer, optional, nullable) — The maximum duration of a conversation in seconds

### AgentConfigOverride-Output

- `first_message` (string, optional, nullable) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional, nullable) — Language of the agent - used for ASR and TTS
- `max_conversation_duration_message` (string, optional, nullable) — If non-empty, the message the agent will send when max conversation duration is reached.
- `prompt` (PromptAgentAPIModelOverride-Output, optional, nullable) — The prompt for the agent

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

### LiteralJsonSchemaPropertyType

### AllowedValues

- `dynamic_variable` (string, required) — Name of a dynamic variable that must resolve to a JSON array of permitted values, e.g. ["ws_alpha", "ws_beta"]. System variables work only if they resolve to a list.

### LiteralJsonSchemaPropertyConstantValue

A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.

### SoftTimeoutConfigOverride

- `message` (string, optional, nullable) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
- `additional_soft_timeout_messages` (list of string, optional, nullable) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.

### SupportedVoice

- `label` (string, required)
- `voice_id` (string, required)
- `description` (string, optional, nullable)
- `language` (string, optional, nullable)
- `model_family` (enum, optional, nullable)
  - Allowed values: `turbo`, `flash`, `multilingual`, `v3_conversational`
- `optimize_streaming_latency` (enum, optional, nullable)
  - Allowed values: `0`, `1`, `2`, `3`, `4`
- `stability` (double, optional, nullable)
- `speed` (double, optional, nullable)
- `similarity_boost` (double, optional, nullable)

### PydanticPronunciationDictionaryVersionLocator

A locator for other documents to be able to reference a specific dictionary and it's version. This is a pydantic version of PronunciationDictionaryVersionLocatorDBModel. Required to ensure compat with the rest of the agent data models.

- `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
- `version_id` (string, required, nullable) — The ID of the version of the pronunciation dictionary

### PromptAgentAPIModelOverride-Output

- `prompt` (string, optional, nullable) — The prompt for the agent
- `llm` (enum, optional, nullable) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `tool_ids` (list of string, optional, nullable) — A list of IDs of tools used by the agent
- `native_mcp_server_ids` (list of string, optional, nullable) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional, nullable) — A list of knowledge bases to be used by the agent

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

### KnowledgeBaseLocator

- `type` (enum, required) — The type of the knowledge base
  - Allowed values: `file`, `url`, `text`, `folder`
- `name` (string, required) — The name of the knowledge base
- `id` (string, required) — The ID of the knowledge base
- `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
  - Allowed values: `prompt`, `auto`

### WorkflowToolResponseModelOutputStepsItemsDiscriminatorMappingNestedToolsResultsItems

## Examples

**Request**

```json
{
  "evaluation_id": "string"
}
```

**Response**

```json
{
  "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
  "status": "processing",
  "metadata": {
    "start_time_unix_secs": 1714423232,
    "call_duration_secs": 10,
    "cost_fiat": 1.1
  },
  "conversation_id": "conv_7401k5m9x2p8ec3rqv6dtnhb0fzw",
  "has_audio": true,
  "has_user_audio": true,
  "has_response_audio": true,
  "has_auxiliary_audio": true,
  "transcript": [
    {
      "role": "user",
      "time_in_call_secs": 10,
      "message": "Hello, how are you?"
    }
  ],
  "agent_name": "My agent",
  "version_id": "agtvrsn_5xM3yVvZQKV0EfqQpLr2",
  "environment": "production",
  "tag_ids": []
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.analysis.runEvaluation("conversation_id", {
        evaluationId: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.analysis.run_evaluation(
    conversation_id="conversation_id",
    evaluation_id="string",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run"

	payload := strings.NewReader("{\n  \"evaluation_id\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"evaluation_id\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run")
  .header("Content-Type", "application/json")
  .body("{\n  \"evaluation_id\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run', [
  'body' => '{
  "evaluation_id": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"evaluation_id\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["evaluation_id": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run")! as URL,
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
