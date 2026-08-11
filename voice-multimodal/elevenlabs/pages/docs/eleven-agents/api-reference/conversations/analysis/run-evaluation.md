---
title: "Run conversation evaluation"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/analysis/run-evaluation.md
path: docs/eleven-agents/api-reference/conversations/analysis/run-evaluation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Run conversation evaluation

POST https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/analysis/evaluations/run
Content-Type: application/json

Rerun a specific evaluation for a conversation.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/analysis/run-evaluation

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

- `evaluation_id` (string, required) — ID of the single evaluation criterion to rerun.
- `scope` (enum, optional, default: conversation)
  - Allowed values: `conversation`, `agent`

## Response

### 200

Successful Response

- `agent_id` (string, required)
- `status` (enum, required)
  - Allowed values: `initiated`, `in-progress`, `processing`, `done`, `failed`
- `metadata` (object, required)
  - `start_time_unix_secs` (integer, required)
  - `call_duration_secs` (integer, required)
  - `accepted_time_unix_secs` (integer, optional)
  - `cost` (integer, optional)
  - `deletion_settings` (object, optional)
    - `deletion_time_unix_secs` (integer, optional)
    - `deleted_logs_at_time_unix_secs` (integer, optional)
    - `deleted_audio_at_time_unix_secs` (integer, optional)
    - `deleted_transcript_at_time_unix_secs` (integer, optional)
    - `delete_transcript_and_pii` (boolean, optional, default: false)
    - `delete_audio` (boolean, optional, default: false)
  - `feedback` (object, optional)
    - `type` (enum, optional)
      - Allowed values: `thumbs`, `rating`
    - `overall_score` (enum, optional)
      - Allowed values: `like`, `dislike`
    - `likes` (integer, optional, default: 0)
    - `dislikes` (integer, optional, default: 0)
    - `rating` (integer, optional)
    - `comment` (string, optional)
  - `authorization_method` (enum, optional, default: public)
    - Allowed values: `invalid`, `public`, `authorization_header`, `signed_url`, `shareable_link`, `livekit_token`, `livekit_token_website`, `genesys_api_key`, `avaya_api_key`, `audiocodes_api_key`, `whatsapp`, `sms`
  - `charging` (object, optional)
    - `dev_discount` (boolean, optional, default: false)
    - `is_burst` (boolean, optional, default: false)
    - `tier` (string, optional)
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
    - `llm_price` (double, optional)
    - `llm_charge` (integer, optional)
    - `call_charge` (integer, optional)
    - `platform_charge` (integer, optional)
    - `platform_usage` (object, optional) — Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``).
      - `category_usage` (map from string to object, optional)
        - `credits` (integer, optional, default: 0)
        - `price` (double, optional, default: 0)
        - `quantity` (double, optional, default: 0)
    - `platform_price` (double, optional)
    - `free_minutes_consumed` (double, optional, default: 0)
    - `free_llm_dollars_consumed` (double, optional, default: 0)
    - `tts_usage` (object, optional) — Aggregated TTS usage for a conversation (analytics-only, not billing).
      - `primary_tts_model` (string, optional)
      - `total_audio_output_seconds` (double, optional, default: 0)
      - `total_characters` (integer, optional, default: 0)
      - `per_voice_usage` (list of object, optional)
        - `voice_id` (string, required)
        - `audio_output_seconds` (double, optional, default: 0)
    - `asr_usage` (object, optional) — Aggregated ASR usage for a conversation (analytics-only, not billing).
      - `asr_model` (string, optional)
      - `total_transcription_calls` (integer, optional, default: 0)
      - `total_audio_input_seconds` (double, optional, default: 0)
    - `analysis` (object, optional) — Cost of running post-call analysis on this conversation. Present once an analysis pass has run, billed or not.
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
  - `phone_call` (object, optional)
    - `type`: `exotel`
      - `agent_number` (string, required)
      - `call_sid` (string, required)
      - `direction` (enum, required, default: inbound)
        - Allowed values: `inbound`, `outbound`
      - `external_number` (string, required)
      - `phone_number_id` (string, required)
      - `stream_sid` (string, required)
    - `type`: `sip_trunking`
      - `agent_number` (string, required)
      - `call_sid` (string, required)
      - `direction` (enum, required, default: inbound)
        - Allowed values: `inbound`, `outbound`
      - `external_number` (string, required)
      - `phone_number_id` (string, required)
      - `call_id` (string, optional)
      - `sip_header_dynamic_variables` (map from string to string, optional)
    - `type`: `twilio`
      - `agent_number` (string, required)
      - `call_sid` (string, required)
      - `direction` (enum, required, default: inbound)
        - Allowed values: `inbound`, `outbound`
      - `external_number` (string, required)
      - `phone_number_id` (string, required)
      - `stream_sid` (string, required)
  - `batch_call` (object, optional)
    - `batch_call_id` (string, required)
    - `batch_call_recipient_id` (string, required)
  - `termination_reason` (string, optional, default: )
  - `error` (object, optional)
    - `code` (integer, required)
    - `reason` (string, optional)
  - `warnings` (list of string, optional)
  - `main_language` (string, optional)
  - `rag_usage` (object, optional)
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
  - `initiator_id` (string, optional)
  - `conversation_initiation_source` (enum, optional, default: unknown) — Enum representing the possible sources for conversation initiation.
    - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
  - `conversation_initiation_source_version` (string, optional)
  - `timezone` (string, optional)
  - `async_metadata` (object, optional) — Metadata for async conversation delivery (Zendesk, Slack, etc.).
    - `delivery_status` (enum, required)
      - Allowed values: `pending`, `success`, `failed`
    - `delivery_timestamp` (integer, required)
    - `external_system` (string, required)
    - `external_id` (string, required)
    - `delivery_error` (string, optional)
    - `external_link` (string, optional)
    - `retry_count` (integer, optional, default: 0)
    - `last_retry_timestamp` (integer, optional)
    - `last_processed_external_message_id` (string, optional)
  - `whatsapp` (object, optional)
    - `whatsapp_user_id` (string, required)
    - `direction` (enum, optional, default: unknown)
      - Allowed values: `inbound`, `outbound`, `unknown`
    - `whatsapp_phone_number_id` (string, optional)
    - `awaiting_first_user_message` (boolean, optional)
  - `sms` (object, optional)
    - `direction` (enum, required)
      - Allowed values: `inbound`, `outbound`
    - `sms_user_phone_number` (string, required)
    - `phone_number_id` (string, optional)
    - `agent_phone_number` (string, optional)
  - `agent_created_from` (enum, optional, default: unknown)
    - Allowed values: `cli`, `ui`, `api`, `template`, `unknown`
  - `agent_last_updated_from` (enum, optional, default: unknown)
    - Allowed values: `cli`, `ui`, `api`, `template`, `unknown`
  - `voice_rewards` (list of object, optional)
    - `voice_id` (string, required)
    - `reward_usd_cents` (double, required)
  - `cost_fiat` (double, optional) — Total fiat cost of the conversation in USD, i.e. the sum of the LLM price and the non-LLM platform price (the fiat analogue of ``cost``). ``None`` when neither is set (e.g. conversations that predate fiat cost tracking).
- `conversation_id` (string, required)
- `has_audio` (boolean, required)
- `has_user_audio` (boolean, required)
- `has_response_audio` (boolean, required)
- `has_auxiliary_audio` (boolean, required)
- `transcript` (list of object, required)
  - `role` (enum, required)
    - Allowed values: `user`, `agent`
  - `time_in_call_secs` (integer, required)
  - `agent_metadata` (object, optional)
    - `agent_id` (string, required)
    - `branch_id` (string, optional)
    - `workflow_node_id` (string, optional)
    - `version_id` (string, optional)
  - `message` (string, optional)
  - `multivoice_message` (object, optional) — Represents a message from a multi-voice agent.
    - `parts` (list of object, required)
      - `text` (string, required)
      - `voice_label` (string, optional)
      - `time_in_call_secs` (integer, optional)
  - `tool_calls` (list of object, optional)
    - `request_id` (string, required)
    - `tool_name` (string, required)
    - `params_as_json` (string, required)
    - `tool_has_been_called` (boolean, required)
    - `type` (enum, optional)
      - Allowed values: `system`, `webhook`, `client`, `mcp`, `workflow`, `api_integration_webhook`, `api_integration_mcp`, `smb`
    - `tool_details` (object, optional)
      - `type`: `api_integration_webhook`
        - `credential_id` (string, required, default: )
        - `integration_connection_id` (string, required, default: )
        - `integration_id` (string, required, default: )
        - `webhook_details` (object, required)
          - `method` (string, required)
          - `url` (string, required)
          - `type` ("webhook", optional)
          - `headers` (map from string to string, optional)
          - `path_params` (map from string to string, optional)
          - `query_params` (map from string to string, optional)
          - `body` (string, optional)
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
  - `tool_results` (list of object or object or object or object, optional)
    - Conversation History Transcript Other Tools Result Common Model
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
        - `new_value` (string, required)
        - `updated_at` (double, required)
        - `tool_name` (string, required)
        - `tool_request_id` (string, required)
        - `old_value` (string, optional)
      - `type` (enum, optional)
        - Allowed values: `client`, `webhook`, `mcp`, `code`
    - Conversation History Transcript System Tool Result Common Model Output
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
        - `new_value` (string, required)
        - `updated_at` (double, required)
        - `tool_name` (string, required)
        - `tool_request_id` (string, required)
        - `old_value` (string, optional)
      - `result` (object, optional)
        - `result_type`: `dummy`
        - `result_type`: `end_call_success`
          - `message` (string, optional)
          - `reason` (string, optional)
          - `status` ("success", optional)
        - `result_type`: `knowledge_base_rag_success`
          - `chunk_count` (integer, optional, default: 0) — Number of relevant chunks retrieved
          - `chunks` (list of object, optional) — Retrieved chunks; populated only in the rag-result-in-tool-result mode
            - `chunk_id` (string, required)
            - `document_id` (string, required)
            - `content` (string, required)
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
          - `branch_info` (object, optional)
            - `branch_reason`: `defaulting_to_main`
              - `branch_id` (string, required)
            - `branch_reason`: `traffic_split`
              - `branch_id` (string, required)
              - `traffic_percentage` (double, required)
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
    - Conversation History Transcript API Integration Webhook Tools Result Common Model Output
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
        - `new_value` (string, required)
        - `updated_at` (double, required)
        - `tool_name` (string, required)
        - `tool_request_id` (string, required)
        - `old_value` (string, optional)
      - `type` ("api_integration_webhook", required)
      - `integration_id` (string, required, default: )
      - `credential_id` (string, required, default: )
      - `integration_connection_id` (string, required, default: )
    - Conversation History Transcript Workflow Tools Result Common Model Output
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
        - `new_value` (string, required)
        - `updated_at` (double, required)
        - `tool_name` (string, required)
        - `tool_request_id` (string, required)
        - `old_value` (string, optional)
      - `result` (object, optional) — A common model for workflow tool responses.
        - `steps` (list of object, optional)
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
            - `requests` (list of object, required)
            - `results` (list of object or object or object or object, required)
            - `step_latency_secs` (double, required)
  - `feedback` (object, optional)
    - `score` (enum, required)
      - Allowed values: `like`, `dislike`
    - `time_in_call_secs` (integer, required)
  - `llm_override` (string, optional)
  - `producing_llm` (string, optional)
  - `conversation_turn_metrics` (object, optional)
    - `metrics` (map from string to object, optional)
      - `elapsed_time` (double, required)
    - `convai_asr_provider` (string, optional)
    - `convai_tts_model` (string, optional)
    - `convai_tts_cascade` (string, optional)
  - `rag_retrieval_info` (object, optional)
    - `chunks` (list of object, required)
      - `document_id` (string, required)
      - `chunk_id` (string, required)
      - `vector_distance` (double, required)
    - `embedding_model` (enum, required, default: e5_mistral_7b_instruct)
      - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
    - `retrieval_query` (string, required)
    - `rag_latency_secs` (double, required)
    - `used_chunk_ids` (list of string, optional)
  - `llm_usage` (object, optional)
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
  - `original_message` (string, optional)
  - `reasoning` (list of object, optional)
    - `summary` (string, optional)
    - `provider_redact` (boolean, optional, default: false)
  - `source_medium` (enum, optional)
    - Allowed values: `audio`, `text`, `image`, `file`
  - `source_event_id` (integer, optional)
  - `used_static_kb_document_ids` (list of string, optional)
  - `user_identifier` (string, optional)
  - `id` (string, optional)
  - `triggered_guardrails` (list of object, optional)
    - `guardrail_type` (enum, required)
      - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
    - `guardrail_name` (string, optional)
  - `file_input` (object, optional)
    - `file_id` (string, required)
    - `original_filename` (string, required)
    - `mime_type` (string, required)
    - `file_url` (string, required)
  - `contextual_update_info` (object, optional)
    - `context_id` (string, required) — Client-supplied identifier grouping related contextual updates.
    - `is_superseded` (boolean, optional, default: false) — True when this contextual update has been replaced by a newer update with the same context_id.
  - `reasoned` (boolean, optional, default: false)
- `agent_name` (string, optional)
- `conversation_product` (string, optional, default: agent)
- `user_id` (string, optional)
- `branch_id` (string, optional)
- `version_id` (string, optional) — The ID of the agent version used for this conversation
- `analysis` (object, optional)
  - `call_successful` (enum, required)
    - Allowed values: `success`, `failure`, `unknown`
  - `transcript_summary` (string, required)
  - `evaluation_criteria_results` (map from string to object, optional)
    - `criteria_id` (string, required)
    - `result` (enum, required)
      - Allowed values: `success`, `failure`, `unknown`
    - `rationale` (string, required)
    - `scoring_mode` (enum, optional, default: binary)
      - Allowed values: `binary`, `numeric_uniform`
    - `score` (integer, optional)
    - `max_score` (integer, optional)
  - `data_collection_results` (map from string to object, optional)
    - `data_collection_id` (string, required)
    - `rationale` (string, required)
    - `value` (any, optional)
    - `json_schema` (object, optional) — Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.
      - `type` ("boolean" or "string" or "integer" or "number" or list of string, required)
      - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `enum` (list of string, optional) — List of allowed string values for string type parameters
      - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
      - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
      - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
      - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
  - `evaluation_criteria_results_list` (list of object, optional)
    - `criteria_id` (string, required)
    - `result` (enum, required)
      - Allowed values: `success`, `failure`, `unknown`
    - `rationale` (string, required)
    - `scoring_mode` (enum, optional, default: binary)
      - Allowed values: `binary`, `numeric_uniform`
    - `score` (integer, optional)
    - `max_score` (integer, optional)
  - `data_collection_results_list` (list of object, optional)
    - `data_collection_id` (string, required)
    - `rationale` (string, required)
    - `value` (any, optional)
    - `json_schema` (object, optional) — Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.
      - `type` ("boolean" or "string" or "integer" or "number" or list of string, required)
      - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `enum` (list of string, optional) — List of allowed string values for string type parameters
      - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
      - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
      - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
      - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
  - `call_success_score` (double, optional)
  - `call_summary_title` (string, optional)
  - `scoped` (list of object, optional)
    - `scope` (enum, required, default: conversation) — The scope of the analysis. 'conversation' uses the full transcript; 'agent' uses only the portion where the defining agent was active.
      - Allowed values: `conversation`, `agent`
    - `source_agent_id` (string, required)
    - `successful` (enum, required)
      - Allowed values: `success`, `failure`, `unknown`
    - `source_branch_id` (string, optional) — Branch of the agent for this scoped block; disambiguates repeated agent_id.
    - `evaluation_criteria_results` (map from string to object, optional)
      - `criteria_id` (string, required)
      - `result` (enum, required)
        - Allowed values: `success`, `failure`, `unknown`
      - `rationale` (string, required)
      - `scoring_mode` (enum, optional, default: binary)
        - Allowed values: `binary`, `numeric_uniform`
      - `score` (integer, optional)
      - `max_score` (integer, optional)
    - `data_collection_results` (map from string to object, optional)
      - `data_collection_id` (string, required)
      - `rationale` (string, required)
      - `value` (any, optional)
      - `json_schema` (object, optional) — Schema property for literal JSON types. IMPORTANT: Only ONE of the following fields can be set: description (LLM provides value), dynamic_variable (value from variable), is_system_provided (system provides value), constant_value (fixed value), or is_omitted (parameter is omitted). These are mutually exclusive.
        - `type` ("boolean" or "string" or "integer" or "number" or list of string, required)
        - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
        - `enum` (list of string, optional) — List of allowed string values for string type parameters
        - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
        - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
        - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
        - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
        - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
    - `success_score` (double, optional)
- `visited_agents` (list of object, optional)
  - `agent_id` (string, required)
  - `branch_id` (string, optional)
- `conversation_initiation_client_data` (object, optional)
  - `conversation_config_override` (object, optional)
    - `asr` (object, optional) — Configuration for conversational transcription
      - `keywords` (list of string, optional) — Keywords to boost prediction probability for
    - `turn` (object, optional) — Configuration for turn detection
      - `soft_timeout_config` (object, optional) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
        - `message` (string, optional) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
    - `tts` (object, optional) — Configuration for conversational text to speech
      - `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
        - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
      - `voice_id` (string, optional) — The voice ID to use for TTS
      - `stability` (double, optional) — The stability of generated speech
      - `speed` (double, optional) — The speed of generated speech
      - `similarity_boost` (double, optional) — The similarity boost for generated speech
      - `pronunciation_dictionary_locators` (list of object, optional) — The pronunciation dictionary locators
        - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
        - `version_id` (string, optional) — The ID of the version of the pronunciation dictionary
    - `conversation` (object, optional) — Configuration for conversational events
      - `text_only` (boolean, optional) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
      - `max_duration_seconds` (integer, optional) — The maximum duration of a conversation in seconds
    - `agent` (object, optional) — Agent specific configuration
      - `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
      - `language` (string, optional) — Language of the agent - used for ASR and TTS
      - `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
      - `prompt` (object, optional) — The prompt for the agent
        - `prompt` (string, optional) — The prompt for the agent
        - `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
          - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
        - `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
        - `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
        - `knowledge_base` (list of object, optional) — A list of knowledge bases to be used by the agent
          - `type` (enum, required) — The type of the knowledge base
            - Allowed values: `file`, `url`, `text`, `folder`
          - `name` (string, required) — The name of the knowledge base
          - `id` (string, required) — The ID of the knowledge base
          - `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
            - Allowed values: `prompt`, `auto`
  - `custom_llm_extra_body` (map from string to any, optional)
  - `user_id` (string, optional) — ID of the end user participating in this conversation (for agent owner's user identification)
  - `source_info` (object, optional) — Information about the source of conversation initiation
    - `source` (enum, optional, default: unknown) — Source of the conversation initiation
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `version` (string, optional) — The SDK version number
  - `branch_id` (string, optional) — ID of the agent branch to use for this conversation
  - `environment` (string, optional) — Environment to use for resolving environment variables
  - `starting_workflow_node_id` (string, optional) — If set, start the workflow at this node id instead of the default entry
  - `dynamic_variables` (map from string to any, optional)
- `environment` (string, optional, default: production)
- `tag_ids` (list of string, optional) — Conversation tag ids assigned to this conversation.
- `otlp_traces` (map from string to any, optional) — OpenTelemetry trace payload when the request uses format=opentelemetry; otherwise omitted.

## Examples

**Request**

```json
{
  "evaluation_id": "evaluation_id"
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
    "accepted_time_unix_secs": 1,
    "cost": 1,
    "deletion_settings": {
      "deletion_time_unix_secs": 1,
      "deleted_logs_at_time_unix_secs": 1,
      "deleted_audio_at_time_unix_secs": 1,
      "deleted_transcript_at_time_unix_secs": 1,
      "delete_transcript_and_pii": true,
      "delete_audio": true
    },
    "feedback": {
      "type": "thumbs",
      "overall_score": "like",
      "likes": 1,
      "dislikes": 1,
      "rating": 1,
      "comment": "comment"
    },
    "authorization_method": "invalid",
    "charging": {
      "dev_discount": true,
      "is_burst": true,
      "tier": "tier",
      "llm_price": 1.1,
      "llm_charge": 1,
      "call_charge": 1,
      "platform_charge": 1,
      "platform_price": 1.1,
      "free_minutes_consumed": 1.1,
      "free_llm_dollars_consumed": 1.1,
      "analysis": {
        "total": {},
        "last_run": {}
      }
    },
    "phone_call": {
      "type": "exotel",
      "agent_number": "agent_number",
      "call_sid": "call_sid",
      "direction": "inbound",
      "external_number": "external_number",
      "phone_number_id": "phone_number_id",
      "stream_sid": "stream_sid"
    },
    "batch_call": {
      "batch_call_id": "batch_call_id",
      "batch_call_recipient_id": "batch_call_recipient_id"
    },
    "termination_reason": "termination_reason",
    "error": {
      "code": 1,
      "reason": "reason"
    },
    "warnings": [
      "warnings"
    ],
    "main_language": "main_language",
    "rag_usage": {
      "usage_count": 1,
      "embedding_model": "embedding_model"
    },
    "text_only": true,
    "features_usage": {
      "pii_zrm_workspace": true,
      "pii_zrm_agent": true,
      "is_livekit": true
    },
    "eleven_assistant": {
      "is_eleven_assistant": true
    },
    "initiator_id": "initiator_id",
    "conversation_initiation_source": "unknown",
    "conversation_initiation_source_version": "conversation_initiation_source_version",
    "timezone": "timezone",
    "async_metadata": {
      "delivery_status": "pending",
      "delivery_timestamp": 1,
      "external_system": "external_system",
      "external_id": "external_id",
      "delivery_error": "delivery_error",
      "external_link": "external_link",
      "retry_count": 1,
      "last_retry_timestamp": 1,
      "last_processed_external_message_id": "last_processed_external_message_id"
    },
    "whatsapp": {
      "whatsapp_user_id": "whatsapp_user_id",
      "direction": "inbound",
      "whatsapp_phone_number_id": "whatsapp_phone_number_id",
      "awaiting_first_user_message": true
    },
    "sms": {
      "direction": "inbound",
      "sms_user_phone_number": "sms_user_phone_number",
      "phone_number_id": "phone_number_id",
      "agent_phone_number": "agent_phone_number"
    },
    "agent_created_from": "cli",
    "agent_last_updated_from": "cli",
    "voice_rewards": [
      {
        "voice_id": "voice_id",
        "reward_usd_cents": 1.1
      }
    ],
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
      "agent_metadata": {
        "agent_id": "agent_id"
      },
      "message": "Hello, how are you?",
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
      "contextual_update_info": {
        "context_id": "context_id"
      },
      "reasoned": true
    }
  ],
  "agent_name": "My agent",
  "conversation_product": "conversation_product",
  "user_id": "user_id",
  "branch_id": "branch_id",
  "version_id": "agtvrsn_5xM3yVvZQKV0EfqQpLr2",
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
  },
  "visited_agents": [
    {
      "agent_id": "agent_id",
      "branch_id": "branch_id"
    }
  ],
  "conversation_initiation_client_data": {
    "conversation_config_override": {
      "asr": {
        "keywords": [
          "hello",
          "world"
        ]
      },
      "turn": {
        "soft_timeout_config": {
          "message": "Hhmmmm...yeah."
        }
      },
      "tts": {
        "model_id": "eleven_turbo_v2",
        "voice_id": "cjVigY5qzO86Huf0OWal",
        "stability": 0.5,
        "speed": 1,
        "similarity_boost": 0.8,
        "pronunciation_dictionary_locators": [
          {
            "pronunciation_dictionary_id": "pronunciation_dictionary_id",
            "version_id": null
          }
        ]
      },
      "conversation": {
        "max_duration_seconds": 600
      },
      "agent": {
        "first_message": "Hello, how can I help you today?",
        "language": "en",
        "prompt": {
          "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
          "llm": "gemini-2.0-flash-001",
          "tool_ids": [
            "tool_ids"
          ],
          "knowledge_base": [
            {
              "type": "file",
              "name": "My Knowledge Base",
              "id": "123",
              "usage_mode": "auto"
            }
          ]
        }
      }
    },
    "custom_llm_extra_body": {
      "key": "value"
    },
    "user_id": "user_id",
    "source_info": {
      "source": "unknown",
      "version": "version"
    },
    "branch_id": "branch_id",
    "environment": "environment",
    "starting_workflow_node_id": "starting_workflow_node_id",
    "dynamic_variables": {
      "key": "value"
    }
  },
  "environment": "production",
  "tag_ids": [
    "tag_ids"
  ],
  "otlp_traces": {
    "key": "value"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.analysis.runEvaluation("conversation_id", {
        evaluationId: "evaluation_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.analysis.run_evaluation(
    conversation_id="conversation_id",
    evaluation_id="evaluation_id",
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

	payload := strings.NewReader("{\n  \"evaluation_id\": \"evaluation_id\"\n}")

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
request.body = "{\n  \"evaluation_id\": \"evaluation_id\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run")
  .header("Content-Type", "application/json")
  .body("{\n  \"evaluation_id\": \"evaluation_id\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run', [
  'body' => '{
  "evaluation_id": "evaluation_id"
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
request.AddParameter("application/json", "{\n  \"evaluation_id\": \"evaluation_id\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["evaluation_id": "evaluation_id"] as [String : Any]

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
