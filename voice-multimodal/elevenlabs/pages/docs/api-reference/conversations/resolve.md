---
title: "Resolve conversation reference"
source: https://elevenlabs.io/docs/api-reference/conversations/resolve.md
path: docs/api-reference/conversations/resolve
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Resolve conversation reference

GET https://api.elevenlabs.io/v1/convai/conversations/resolve

Resolve a conversation URL (a Slack message URL or a Zendesk ticket URL) to the deterministic conversation ID for the given agent, then confirm the conversation exists.

Reference: https://elevenlabs.io/docs/api-reference/conversations/resolve

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_id` (string, required) — Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.
- `reference` (string, required) — A Slack message URL or a Zendesk ticket URL.

## Response

### 200

Successful Response

- `agent_id` (string, required)
- `status` (enum, required)
  - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
- `metadata` (object, required)
  - `start_time_unix_secs` (integer, required)
  - `call_duration_secs` (integer, required)
  - `cost_fiat` (double, required, nullable) — Total fiat cost of the conversation in USD, i.e. the sum of the LLM price and the non-LLM platform price (the fiat analogue of ``cost``). ``None`` when neither is set (e.g. conversations that predate fiat cost tracking).
  - `accepted_time_unix_secs` (integer, optional, nullable)
  - `cost` (integer, optional, nullable)
  - `deletion_settings` (object, optional)
    - `deletion_time_unix_secs` (integer, optional, nullable)
    - `deleted_logs_at_time_unix_secs` (integer, optional, nullable)
    - `deleted_audio_at_time_unix_secs` (integer, optional, nullable)
    - `deleted_transcript_at_time_unix_secs` (integer, optional, nullable)
    - `delete_transcript_and_pii` (boolean, optional, default: false)
    - `delete_audio` (boolean, optional, default: false)
  - `feedback` (object, optional)
    - `type` (enum, optional, nullable)
      - Allowed values: `thumbs`, `rating`
    - `overall_score` (enum, optional, nullable)
      - Allowed values: `like`, `dislike`
    - `likes` (integer, optional, default: 0)
    - `dislikes` (integer, optional, default: 0)
    - `rating` (integer, optional, nullable)
    - `comment` (string, optional, nullable)
  - `authorization_method` (enum, optional, default: public)
    - Allowed values: `invalid`, `public`, `authorization_header`, `signed_url`, `shareable_link`, `livekit_token`, `livekit_token_website`, `genesys_api_key`, `avaya_api_key`, `audiocodes_api_key`, `whatsapp`, `sms`
  - `charging` (object, optional)
    - `dev_discount` (boolean, optional, default: false)
    - `is_burst` (boolean, optional, default: false)
    - `tier` (string, optional, nullable)
    - `llm_usage` (object, optional)
      - `irreversible_generation` (object, optional)
        - `model_usage` (map from string to object, optional)
          - `input` (object, optional)
            - `tokens` (integer, optional, default: 0)
            - `price` (double, optional, default: 0)
          - `input_cache_read` (object, optional)
            - `tokens` (integer, optional, default: 0)
            - `price` (double, optional, default: 0)
          - `input_cache_write` (object, optional)
            - `tokens` (integer, optional, default: 0)
            - `price` (double, optional, default: 0)
          - `output_total` (object, optional)
            - `tokens` (integer, optional, default: 0)
            - `price` (double, optional, default: 0)
      - `initiated_generation` (object, optional)
        - `model_usage` (map from string to object, optional)
          - `input` (object, optional)
            - `tokens` (integer, optional, default: 0)
            - `price` (double, optional, default: 0)
          - `input_cache_read` (object, optional)
            - `tokens` (integer, optional, default: 0)
            - `price` (double, optional, default: 0)
          - `input_cache_write` (object, optional)
            - `tokens` (integer, optional, default: 0)
            - `price` (double, optional, default: 0)
          - `output_total` (object, optional)
            - `tokens` (integer, optional, default: 0)
            - `price` (double, optional, default: 0)
    - `llm_price` (double, optional, nullable)
    - `llm_charge` (integer, optional, nullable)
    - `call_charge` (integer, optional, nullable)
    - `platform_charge` (integer, optional, nullable)
    - `platform_usage` (object, optional) — Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``).
      - `category_usage` (map from string to object, optional)
        - `credits` (integer, optional, default: 0)
        - `price` (double, optional, default: 0)
        - `quantity` (double, optional, default: 0)
    - `platform_price` (double, optional, nullable)
    - `free_minutes_consumed` (double, optional, default: 0)
    - `free_llm_dollars_consumed` (double, optional, default: 0)
    - `tts_usage` (object, optional, nullable) — Aggregated TTS usage for a conversation (analytics-only, not billing).
      - `primary_tts_model` (string, optional, nullable)
      - `total_audio_output_seconds` (double, optional, default: 0)
      - `total_characters` (integer, optional, default: 0)
      - `per_voice_usage` (list of object, optional)
        - `voice_id` (string, required)
        - `audio_output_seconds` (double, optional, default: 0)
    - `asr_usage` (object, optional, nullable) — Aggregated ASR usage for a conversation (analytics-only, not billing).
      - `asr_model` (string, optional, nullable)
      - `total_transcription_calls` (integer, optional, default: 0)
      - `total_audio_input_seconds` (double, optional, default: 0)
    - `analysis` (object, optional, nullable) — Cost of running post-call analysis on this conversation. Present once an analysis pass has run, billed or not.
      - `total` (object, required) — Cumulative LLM cost of running post-call analysis on this conversation.
        - `price` (double, optional, default: 0)
        - `charge` (integer, optional, default: 0)
        - `runs` (integer, optional, default: 0)
        - `price_per_feature` (map from string to double, optional)
        - `charge_per_feature` (map from string to integer, optional)
      - `last_run` (object, required) — LLM cost of the most recent post-call analysis pass on this conversation.
        - `price` (double, optional, default: 0)
        - `charge` (integer, optional, default: 0)
        - `price_per_feature` (map from string to double, optional)
        - `charge_per_feature` (map from string to integer, optional)
  - `phone_call` (object, optional, nullable)
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
  - `batch_call` (object, optional, nullable)
    - `batch_call_id` (string, required)
    - `batch_call_recipient_id` (string, required)
  - `termination_reason` (string, optional, default: )
  - `error` (object, optional, nullable)
    - `code` (integer, required)
    - `reason` (string, optional, nullable)
  - `warnings` (list of string, optional)
  - `main_language` (string, optional, nullable)
  - `rag_usage` (object, optional, nullable)
    - `usage_count` (integer, required)
    - `embedding_model` (string, required)
  - `text_only` (boolean, optional, default: false)
  - `features_usage` (object, optional)
    - `language_detection` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `transfer_to_agent` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `transfer_to_number` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `multivoice` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `dtmf_tones` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `external_mcp_servers` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `pii_zrm_workspace` (boolean, optional, default: false)
    - `pii_zrm_agent` (boolean, optional, default: false)
    - `tool_dynamic_variable_updates` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `is_livekit` (boolean, optional, default: false)
    - `voicemail_detection` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `dtmf_input` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `workflow` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `tool_node` (object, optional)
        - `enabled` (boolean, optional, default: false)
        - `used` (boolean, optional, default: false)
      - `standalone_agent_node` (object, optional)
        - `enabled` (boolean, optional, default: false)
        - `used` (boolean, optional, default: false)
      - `phone_number_node` (object, optional)
        - `enabled` (boolean, optional, default: false)
        - `used` (boolean, optional, default: false)
      - `end_node` (object, optional)
        - `enabled` (boolean, optional, default: false)
        - `used` (boolean, optional, default: false)
    - `agent_testing` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `tests_ran_after_last_modification` (boolean, optional, default: false)
      - `tests_ran_in_last_7_days` (boolean, optional, default: false)
    - `versioning` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
    - `file_input` (object, optional)
      - `enabled` (boolean, optional, default: false)
      - `used` (boolean, optional, default: false)
  - `eleven_assistant` (object, optional)
    - `is_eleven_assistant` (boolean, optional, default: false)
  - `initiator_id` (string, optional, nullable)
  - `conversation_initiation_source` (enum, optional, default: unknown) — Enum representing the possible sources for conversation initiation.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `conversation_initiation_source_version` (string, optional, nullable)
  - `timezone` (string, optional, nullable)
  - `async_metadata` (object, optional, nullable) — Metadata for async conversation delivery (Zendesk, Slack, etc.).
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
  - `whatsapp` (object, optional, nullable)
    - `whatsapp_user_id` (string, required)
    - `direction` (enum, optional, default: unknown)
      - Allowed values: `inbound`, `outbound`, `unknown`
    - `whatsapp_phone_number_id` (string, optional, nullable)
    - `awaiting_first_user_message` (boolean, optional, nullable)
  - `sms` (object, optional, nullable)
    - `direction` (enum, required)
      - Allowed values: `inbound`, `outbound`
    - `sms_user_phone_number` (string, required)
    - `phone_number_id` (string, optional, nullable)
    - `agent_phone_number` (string, optional, nullable)
  - `agent_created_from` (enum, optional, default: unknown)
    - Allowed values: `cli`, `ui`, `api`, `template`, `unknown`
  - `agent_last_updated_from` (enum, optional, default: unknown)
    - Allowed values: `cli`, `ui`, `api`, `template`, `unknown`
  - `voice_rewards` (list of object, optional)
    - `voice_id` (string, required)
    - `reward_usd_cents` (double, required)
- `conversation_id` (string, required)
- `has_audio` (boolean, required)
- `has_user_audio` (boolean, required)
- `has_response_audio` (boolean, required)
- `has_auxiliary_audio` (boolean, required)
- `transcript` (list of object, required)
  - `role` (enum, required)
    - Allowed values: `user`, `agent`
  - `time_in_call_secs` (integer, required)
  - `agent_metadata` (object, optional, nullable)
    - `agent_id` (string, required)
    - `branch_id` (string, optional, nullable)
    - `workflow_node_id` (string, optional, nullable)
    - `version_id` (string, optional, nullable)
  - `message` (string, optional, nullable)
  - `multivoice_message` (object, optional, nullable) — Represents a message from a multi-voice agent.
    - `parts` (list of object, required)
      - `text` (string, required)
      - `voice_label` (string, required, nullable)
      - `time_in_call_secs` (integer, required, nullable)
  - `tool_calls` (list of object, optional)
    - `request_id` (string, required)
    - `tool_name` (string, required)
    - `params_as_json` (string, required)
    - `tool_has_been_called` (boolean, required)
    - `type` (enum, optional, nullable)
      - Allowed values: `system`, `webhook`, `client`, `mcp`, `workflow`, `api_integration_webhook`, `api_integration_mcp`, `smb`
    - `tool_details` (object, optional, nullable)
      - `type`: `api_integration_webhook` (ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetails)
        - `credential_id` (string, required, default: )
        - `integration_connection_id` (string, required, default: )
        - `integration_id` (string, required, default: )
        - `webhook_details` (object, required)
          - `method` (string, required)
          - `url` (string, required)
          - `headers` (map from string to string, optional)
          - `path_params` (map from string to string, optional)
          - `query_params` (map from string to string, optional)
          - `body` (string, optional, nullable)
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
  - `tool_results` (list of object or object or object or object, optional)
    - ConversationHistoryTranscriptOtherToolsResultCommonModel
      - `request_id` (string, required)
      - `tool_name` (string, required)
      - `result_value` (string, required)
      - `is_error` (boolean, required)
      - `tool_has_been_called` (boolean, required)
      - `is_blocked` (boolean, optional, default: false)
      - `tool_latency_secs` (double, optional, default: 0)
      - `error_type` (string, optional, default: )
      - `raw_error_message` (string, optional, default: )
      - `dynamic_variable_updates` (list of object, optional)
        - `variable_name` (string, required)
        - `old_value` (string, required, nullable)
        - `new_value` (string, required)
        - `updated_at` (double, required)
        - `tool_name` (string, required)
        - `tool_request_id` (string, required)
      - `type` (enum, optional, nullable)
        - Allowed values: `client`, `webhook`, `mcp`, `code`
    - ConversationHistoryTranscriptSystemToolResultCommonModel
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
      - `dynamic_variable_updates` (list of object, optional)
        - `variable_name` (string, required)
        - `old_value` (string, required, nullable)
        - `new_value` (string, required)
        - `updated_at` (double, required)
        - `tool_name` (string, required)
        - `tool_request_id` (string, required)
      - `result` (object, optional, nullable)
        - `result_type`: `dummy` (DummyToolResultModel)
        - `result_type`: `end_call_success` (EndCallToolResultModel)
          - `message` (string, optional, nullable)
          - `reason` (string, optional, nullable)
          - `status` ("success", optional, default: success)
        - `result_type`: `knowledge_base_rag_success` (KnowledgeBaseRagToolResultModel)
          - `chunk_count` (integer, optional, default: 0) — Number of relevant chunks retrieved
          - `chunks` (list of object, optional) — Retrieved chunks; populated only in the rag-result-in-tool-result mode
            - `chunk_id` (string, required)
            - `document_id` (string, required)
            - `content` (string, required)
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
          - `branch_info` (object, optional, nullable)
            - `branch_reason`: `defaulting_to_main` (TransferBranchInfoDefaultingToMain)
              - `branch_id` (string, required)
            - `branch_reason`: `traffic_split` (TransferBranchInfoTrafficSplit)
              - `branch_id` (string, required)
              - `traffic_percentage` (double, required)
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
    - ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel
      - `request_id` (string, required)
      - `tool_name` (string, required)
      - `result_value` (string, required)
      - `is_error` (boolean, required)
      - `is_blocked` (boolean, required, default: false)
      - `tool_has_been_called` (boolean, required)
      - `tool_latency_secs` (double, required, default: 0)
      - `error_type` (string, required, default: )
      - `raw_error_message` (string, required, default: )
      - `dynamic_variable_updates` (list of object, required)
        - `variable_name` (string, required)
        - `old_value` (string, required, nullable)
        - `new_value` (string, required)
        - `updated_at` (double, required)
        - `tool_name` (string, required)
        - `tool_request_id` (string, required)
      - `type` ("api_integration_webhook", required)
      - `integration_id` (string, required, default: )
      - `credential_id` (string, required, default: )
      - `integration_connection_id` (string, required, default: )
    - ConversationHistoryTranscriptWorkflowToolsResultCommonModel
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
      - `dynamic_variable_updates` (list of object, optional)
        - `variable_name` (string, required)
        - `old_value` (string, required, nullable)
        - `new_value` (string, required)
        - `updated_at` (double, required)
        - `tool_name` (string, required)
        - `tool_request_id` (string, required)
      - `result` (object, optional, nullable) — A common model for workflow tool responses.
        - `steps` (list of object, optional)
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
            - `requests` (list of object, required)
            - `results` (list of object or object or object or object, required)
            - `step_latency_secs` (double, required)
  - `feedback` (object, optional, nullable)
    - `score` (enum, required)
      - Allowed values: `like`, `dislike`
    - `time_in_call_secs` (integer, required)
  - `llm_override` (string, optional, nullable)
  - `producing_llm` (string, optional, nullable)
  - `conversation_turn_metrics` (object, optional, nullable)
    - `metrics` (map from string to object, optional)
      - `elapsed_time` (double, required)
    - `convai_asr_provider` (string, optional, nullable)
    - `convai_tts_model` (string, optional, nullable)
    - `convai_tts_cascade` (string, optional, nullable)
  - `rag_retrieval_info` (object, optional, nullable)
    - `chunks` (list of object, required)
      - `document_id` (string, required)
      - `chunk_id` (string, required)
      - `vector_distance` (double, required)
    - `embedding_model` (enum, required, default: e5_mistral_7b_instruct)
      - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
    - `retrieval_query` (string, required)
    - `rag_latency_secs` (double, required)
    - `used_chunk_ids` (list of string, optional)
  - `llm_usage` (object, optional, nullable)
    - `model_usage` (map from string to object, optional)
      - `input` (object, optional)
        - `tokens` (integer, optional, default: 0)
        - `price` (double, optional, default: 0)
      - `input_cache_read` (object, optional)
        - `tokens` (integer, optional, default: 0)
        - `price` (double, optional, default: 0)
      - `input_cache_write` (object, optional)
        - `tokens` (integer, optional, default: 0)
        - `price` (double, optional, default: 0)
      - `output_total` (object, optional)
        - `tokens` (integer, optional, default: 0)
        - `price` (double, optional, default: 0)
  - `interrupted` (boolean, optional, default: false)
  - `ignored_as_backchannel` (boolean, optional, default: false)
  - `original_message` (string, optional, nullable)
  - `reasoning` (list of object, optional)
    - `summary` (string, optional, nullable)
    - `provider_redact` (boolean, optional, default: false)
  - `source_medium` (enum, optional, nullable)
    - Allowed values: `audio`, `text`, `image`, `file`
  - `source_event_id` (integer, optional, nullable)
  - `used_static_kb_document_ids` (list of string, optional)
  - `user_identifier` (string, optional, nullable)
  - `id` (string, optional, nullable)
  - `triggered_guardrails` (list of object, optional)
    - `guardrail_type` (enum, required)
      - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
    - `guardrail_name` (string, optional, nullable)
  - `file_input` (object, optional, nullable)
    - `file_id` (string, required)
    - `original_filename` (string, required)
    - `mime_type` (string, required)
    - `file_url` (string, required)
  - `contextual_update_info` (object, optional, nullable)
    - `context_id` (string, required) — Client-supplied identifier grouping related contextual updates.
    - `is_superseded` (boolean, optional, default: false) — True when this contextual update has been replaced by a newer update with the same context_id.
  - `reasoned` (boolean, optional, default: false)
- `agent_name` (string, optional, nullable)
- `conversation_product` (string, optional, default: agent)
- `user_id` (string, optional, nullable)
- `branch_id` (string, optional, nullable)
- `version_id` (string, optional, nullable) — The ID of the agent version used for this conversation
- `analysis` (object, optional, nullable)
  - `call_successful` (enum, required)
    - Allowed values: `success`, `failure`, `unknown`
  - `transcript_summary` (string, required)
  - `evaluation_criteria_results` (map from string to object, optional)
    - `criteria_id` (string, required)
    - `result` (enum, required)
      - Allowed values: `success`, `failure`, `unknown`
    - `rationale` (string, required)
    - `scoring_mode` (enum, optional, nullable, default: binary)
      - Allowed values: `binary`, `numeric_uniform`
    - `score` (integer, optional, nullable)
    - `max_score` (integer, optional, nullable)
  - `data_collection_results` (map from string to object, optional)
    - `data_collection_id` (string, required)
    - `rationale` (string, required)
    - `value` (any, optional)
    - `json_schema` (object, optional, nullable) — Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.
      - `type` (enum or list of string, required)
      - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `enum` (list of string, optional, nullable) — List of allowed string values for string type parameters
      - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
      - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
      - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `constant_value` (string or integer or double or boolean, optional, default: ) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
      - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
  - `evaluation_criteria_results_list` (list of object, optional)
    - `criteria_id` (string, required)
    - `result` (enum, required)
      - Allowed values: `success`, `failure`, `unknown`
    - `rationale` (string, required)
    - `scoring_mode` (enum, optional, nullable, default: binary)
      - Allowed values: `binary`, `numeric_uniform`
    - `score` (integer, optional, nullable)
    - `max_score` (integer, optional, nullable)
  - `data_collection_results_list` (list of object, optional)
    - `data_collection_id` (string, required)
    - `rationale` (string, required)
    - `value` (any, optional)
    - `json_schema` (object, optional, nullable) — Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.
      - `type` (enum or list of string, required)
      - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `enum` (list of string, optional, nullable) — List of allowed string values for string type parameters
      - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
      - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
      - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `constant_value` (string or integer or double or boolean, optional, default: ) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
      - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
  - `call_success_score` (double, optional, nullable)
  - `call_summary_title` (string, optional, nullable)
  - `scoped` (list of object, optional)
    - `scope` (enum, required, default: conversation) — The scope of the analysis. 'conversation' uses the full transcript; 'agent' uses only the portion where the defining agent was active.
      - Allowed values: `conversation`, `agent`
    - `source_agent_id` (string, required)
    - `successful` (enum, required)
      - Allowed values: `success`, `failure`, `unknown`
    - `source_branch_id` (string, optional, nullable) — Branch of the agent for this scoped block; disambiguates repeated agent_id.
    - `evaluation_criteria_results` (map from string to object, optional)
      - `criteria_id` (string, required)
      - `result` (enum, required)
        - Allowed values: `success`, `failure`, `unknown`
      - `rationale` (string, required)
      - `scoring_mode` (enum, optional, nullable, default: binary)
        - Allowed values: `binary`, `numeric_uniform`
      - `score` (integer, optional, nullable)
      - `max_score` (integer, optional, nullable)
    - `data_collection_results` (map from string to object, optional)
      - `data_collection_id` (string, required)
      - `rationale` (string, required)
      - `value` (any, optional)
      - `json_schema` (object, optional, nullable) — Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.
        - `type` (enum or list of string, required)
        - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
        - `enum` (list of string, optional, nullable) — List of allowed string values for string type parameters
        - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
        - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
        - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
        - `constant_value` (string or integer or double or boolean, optional, default: ) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
        - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
    - `success_score` (double, optional, nullable)
- `visited_agents` (list of object, optional)
  - `agent_id` (string, required)
  - `branch_id` (string, optional, nullable)
- `conversation_initiation_client_data` (object, optional)
  - `conversation_config_override` (object, optional)
    - `asr` (object, optional, nullable) — Configuration for conversational transcription
      - `keywords` (list of string, optional, nullable) — Keywords to boost prediction probability for
    - `turn` (object, optional, nullable) — Configuration for turn detection
      - `soft_timeout_config` (object, optional, nullable) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
        - `message` (string, optional, nullable) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
    - `tts` (object, optional, nullable) — Configuration for conversational text to speech
      - `model_id` (enum, optional, nullable, default: eleven_flash_v2) — The model to use for TTS
        - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
      - `voice_id` (string, optional, nullable) — The voice ID to use for TTS
      - `stability` (double, optional, nullable) — The stability of generated speech
      - `speed` (double, optional, nullable) — The speed of generated speech
      - `similarity_boost` (double, optional, nullable) — The similarity boost for generated speech
      - `pronunciation_dictionary_locators` (list of object, optional, nullable) — The pronunciation dictionary locators
        - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
        - `version_id` (string, required, nullable) — The ID of the version of the pronunciation dictionary
    - `conversation` (object, optional, nullable) — Configuration for conversational events
      - `text_only` (boolean, optional, nullable) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
      - `max_duration_seconds` (integer, optional, nullable) — The maximum duration of a conversation in seconds
    - `agent` (object, optional, nullable) — Agent specific configuration
      - `first_message` (string, optional, nullable) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
      - `language` (string, optional, nullable) — Language of the agent - used for ASR and TTS
      - `max_conversation_duration_message` (string, optional, nullable) — If non-empty, the message the agent will send when max conversation duration is reached.
      - `prompt` (object, optional, nullable) — The prompt for the agent
        - `prompt` (string, optional, nullable) — The prompt for the agent
        - `llm` (enum, optional, nullable) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
          - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
        - `tool_ids` (list of string, optional, nullable) — A list of IDs of tools used by the agent
        - `native_mcp_server_ids` (list of string, optional, nullable) — A list of Native MCP server ids to be used by the agent
        - `knowledge_base` (list of object, optional, nullable) — A list of knowledge bases to be used by the agent
          - `type` (enum, required) — The type of the knowledge base
            - Allowed values: `file`, `url`, `text`, `folder`
          - `name` (string, required) — The name of the knowledge base
          - `id` (string, required) — The ID of the knowledge base
          - `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
            - Allowed values: `prompt`, `auto`
  - `custom_llm_extra_body` (map from string to any, optional)
  - `user_id` (string, optional, nullable) — ID of the end user participating in this conversation (for agent owner's user identification)
  - `source_info` (object, optional) — Information about the source of conversation initiation
    - `source` (enum, optional, nullable, default: unknown) — Source of the conversation initiation
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `version` (string, optional, nullable) — The SDK version number
  - `branch_id` (string, optional, nullable) — ID of the agent branch to use for this conversation
  - `environment` (string, optional, nullable) — Environment to use for resolving environment variables
  - `starting_workflow_node_id` (string, optional, nullable) — If set, start the workflow at this node id instead of the default entry
  - `dynamic_variables` (map from string to any, optional)
- `environment` (string, optional, default: production)
- `tag_ids` (list of string, optional) — Conversation tag ids assigned to this conversation.
- `otlp_traces` (map from string to any, optional, nullable) — OpenTelemetry trace payload when the request uses format=opentelemetry; otherwise omitted.

## Examples

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
    await client.conversationalAi.conversations.resolve({
        agentId: "agent_id",
        reference: "reference",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.resolve(
    agent_id="agent_id",
    reference="reference",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/resolve?agent_id=agent_id&reference=reference"

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/resolve?agent_id=agent_id&reference=reference")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/resolve?agent_id=agent_id&reference=reference")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/resolve?agent_id=agent_id&reference=reference');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/resolve?agent_id=agent_id&reference=reference");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/resolve?agent_id=agent_id&reference=reference")! as URL,
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
