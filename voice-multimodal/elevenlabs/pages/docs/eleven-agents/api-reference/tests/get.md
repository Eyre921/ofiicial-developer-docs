---
title: "Get test"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/get.md
path: docs/eleven-agents/api-reference/tests/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get test

GET https://api.elevenlabs.io/v1/convai/agent-testing/{test_id}

Gets an agent response test by ID.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `test_id` (string, required) — The id of a chat response test. This is returned on test creation.

## Response

### 200

Successful Response

- `object`
  - `type`: `llm`
    - `id` (string, required)
    - `name` (string, required)
    - `chat_history` (list of object, optional)
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success`
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
    - `conversation_initiation_source` (enum, optional, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `failure_examples` (list of object, optional) — Non-empty list of example responses that should be considered failures
      - `response` (string, required)
      - `type` ("failure", required)
    - `from_conversation_metadata` (object, optional) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional)
      - `workflow_node_id` (string, optional)
      - `original_agent_reply` (list of object, optional, default: [])
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
            - `type` (enum, optional)
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
            - `result` (object, optional)
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
            - `result` (object, optional) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
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
    - `success_condition` (string, optional, default: ) — A prompt that evaluates whether the agent's response is successful. Should return True or False.
    - `success_examples` (list of object, optional) — Non-empty list of example responses that should be considered successful
      - `response` (string, required)
      - `type` ("success", required)
  - `type`: `tool`
    - `id` (string, required)
    - `name` (string, required)
    - `chat_history` (list of object, optional)
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success`
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
    - `check_any_tool_matches` (boolean, optional) — If set to True this test will pass if any tool call returned by the LLM matches the criteria. Otherwise it will fail if more than one tool is returned by the agent.
    - `conversation_initiation_source` (enum, optional, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `from_conversation_metadata` (object, optional) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional)
      - `workflow_node_id` (string, optional)
      - `original_agent_reply` (list of object, optional, default: [])
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
            - `type` (enum, optional)
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
            - `result` (object, optional)
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
            - `result` (object, optional) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
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
    - `tool_call_parameters` (object, optional) — How to evaluate the agent's tool call (if any). If empty, the tool call is not evaluated.
      - `parameters` (list of object, optional) — Parameters to evaluate for the agent's tool call. If empty, the tool call parameters are not evaluated.
        - `eval` (object, required)
          - `type`: `anything`
          - `type`: `exact`
            - `expected_value` (string, required) — The exact string value that the parameter must match.
          - `type`: `llm`
            - `description` (string, required) — A description of the evaluation strategy to use for the test.
          - `type`: `regex`
            - `pattern` (string, required) — A regex pattern to match the agent's response against.
        - `path` (string, required)
      - `referenced_tool` (object, optional) — The tool to evaluate a call against.
        - `id` (string, required) — The ID of the tool
        - `type` (enum, required) — The type of the tool
          - Allowed values: `system`, `webhook`, `client`, `workflow`, `api_integration_webhook`, `mcp`, `code`
      - `verify_absence` (boolean, optional, default: false) — Whether to verify that the tool was NOT called.
      - `workflow_node_transition` (object, optional) — Configuration for testing workflow node transitions. When set, the test will verify the agent transitions to the specified workflow node.
        - `agent_id` (string, required) — The ID of the agent whose workflow contains the target node.
        - `target_node_id` (string, required) — The ID of the workflow node that the agent should transition to.
        - `type` ("node_id", optional)
  - `type`: `simulation`
    - `id` (string, required)
    - `name` (string, required)
    - `chat_history` (list of object, optional)
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success`
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
    - `conversation_initiation_source` (enum, optional, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `evaluation_model` (enum, optional) — LLM model to use for evaluating simulation results.
      - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
    - `from_conversation_metadata` (object, optional) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional)
      - `workflow_node_id` (string, optional)
      - `original_agent_reply` (list of object, optional, default: [])
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
            - `type` (enum, optional)
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
            - `result` (object, optional)
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
            - `result` (object, optional) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
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
    - `simulated_user_model` (enum, optional) — LLM model for the simulated user.
      - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
    - `simulation_environment` (string, optional) — The environment to use when running this simulation test. If not provided, defaults to 'production'.
    - `simulation_max_turns` (integer, optional, default: 5) — Maximum number of conversation turns for simulation tests.
    - `simulation_scenario` (string, optional, default: ) — Description of the simulation scenario and user persona for simulation tests.
    - `success_conditions` (list of string, optional) — List of prompts that evaluate whether the simulation was successful. If provided, all criteria are evaluated and merged into a final result. Capped at the maximum number of evaluation criteria.
    - `tool_mock_config` (object, optional) — Configuration for which tools to mock and fallback behavior.
      - `mocking_strategy` (enum, optional, default: none) — Which tools to mock: 'all' mocks every mockable tool, 'selected' mocks only those in mocked_tool_names/mocked_tool_ids, 'none' disables mocking.
        - Allowed values: `all`, `selected`, `none`
      - `fallback_strategy` (enum, optional, default: raise_error) — Behavior when no mock matches a tool call.
        - Allowed values: `call_real_tool`, `raise_error`
      - `mocked_tool_ids` (list of string, optional) — Tool IDs to mock. Resolved to tool names before being passed to the orchestrator.
    - `tool_mock_overrides` (map from string to list of object, optional) — Test-specific response mocks, keyed by tool ID. Applied ahead of the tool's shared mocks and only within this test. Only take effect for tools that are mocked (see tool_mock_config).
      - `mock_result` (string, required) — The return value the LLM sees when this mock is active.
      - `parameter_conditions` (list of object, optional) — If the list is empty, the mock will always activate.
        - `eval` (object, required)
          - `type`: `anything`
          - `type`: `exact`
            - `expected_value` (string, required) — The exact string value that the parameter must match.
          - `type`: `llm`
            - `description` (string, required) — A description of the evaluation strategy to use for the test.
          - `type`: `regex`
            - `pattern` (string, required) — A regex pattern to match the agent's response against.
        - `path` (string, required)
      - `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.
    - `success_condition` (string, optional, deprecated) — Deprecated legacy single success criterion. Use success_conditions instead. At least one of success_condition or success_conditions is required.

## Examples

**Response**

```json
{
  "type": "llm",
  "id": "id",
  "name": "name",
  "chat_history": [
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
      ]
    }
  ],
  "conversation_initiation_source": "unknown",
  "dynamic_variables": {
    "key": "value"
  },
  "failure_examples": [
    {
      "response": "response",
      "type": "failure"
    }
  ],
  "from_conversation_metadata": {
    "conversation_id": "conversation_id",
    "agent_id": "agent_id",
    "branch_id": "branch_id",
    "workflow_node_id": "workflow_node_id",
    "original_agent_reply": [
      {
        "role": "user",
        "time_in_call_secs": 1
      }
    ]
  },
  "success_condition": "success_condition",
  "success_examples": [
    {
      "response": "response",
      "type": "success"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.get("TeaqRRdTcIfIu2i7BYfT");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.get(
    test_id="TeaqRRdTcIfIu2i7BYfT",
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

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/TeaqRRdTcIfIu2i7BYfT"

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/TeaqRRdTcIfIu2i7BYfT")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agent-testing/TeaqRRdTcIfIu2i7BYfT")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agent-testing/TeaqRRdTcIfIu2i7BYfT');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/TeaqRRdTcIfIu2i7BYfT");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/TeaqRRdTcIfIu2i7BYfT")! as URL,
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
