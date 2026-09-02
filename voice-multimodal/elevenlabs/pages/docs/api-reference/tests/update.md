---
title: "Update test"
source: https://elevenlabs.io/docs/api-reference/tests/update.md
path: docs/api-reference/tests/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update test

PUT https://api.elevenlabs.io/v1/convai/agent-testing/{test_id}
Content-Type: application/json

Updates an agent response test by ID.

Reference: https://elevenlabs.io/docs/api-reference/tests/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `test_id` (string, required) — The id of a chat response test. This is returned on test creation.

### Body (application/json)

- `object or object or object`
  - UpdateResponseUnitTestRequest
    - `name` (string, required)
    - `from_conversation_metadata` (object, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional, nullable)
      - `workflow_node_id` (string, optional, nullable)
      - `original_agent_reply` (list of object, optional, default: [])
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
              - `webhook_details` (object, required)
              - `credential_id` (string, optional, default: )
              - `integration_connection_id` (string, optional, default: )
              - `integration_id` (string, optional, default: )
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
            - `type` (enum, optional, nullable)
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
            - `result` (object, optional, nullable)
          - ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel
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
            - `dynamic_variable_updates` (list of object, optional)
            - `integration_id` (string, optional, default: )
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
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
            - `result` (object, optional, nullable) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
        - `interrupted` (boolean, optional, default: false)
        - `ignored_as_backchannel` (boolean, optional, default: false)
        - `original_message` (string, optional, nullable)
        - `reasoning` (list of object, optional)
          - `summary` (string, optional, nullable)
          - `provider_redact` (boolean, optional, default: false)
        - `source_medium` (enum, optional, nullable)
          - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
        - `source_event_id` (integer, optional, nullable)
        - `used_static_kb_document_ids` (list of string, optional)
        - `user_identifier` (string, optional, nullable)
        - `id` (string, optional, nullable)
        - `triggered_guardrails` (list of object, optional)
          - `guardrail_type` (enum, required)
            - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
          - `guardrail_name` (string, optional, nullable)
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `chat_history` (list of object, optional)
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
            - `webhook_details` (object, required)
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
            - `integration_id` (string, optional, default: )
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success` (KnowledgeBaseToolResultModel)
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
          - `tool_has_been_called` (boolean, required)
          - `type` ("api_integration_webhook", required)
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
          - `integration_id` (string, optional, default: )
          - `credential_id` (string, optional, default: )
          - `integration_connection_id` (string, optional, default: )
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
        - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
      - `source_event_id` (integer, optional, nullable)
      - `used_static_kb_document_ids` (list of string, optional)
      - `user_identifier` (string, optional, nullable)
      - `id` (string, optional, nullable)
      - `triggered_guardrails` (list of object, optional)
        - `guardrail_type` (enum, required)
          - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
        - `guardrail_name` (string, optional, nullable)
    - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
    - `type` ("llm", optional, default: llm)
    - `success_condition` (string, optional, default: ) — A prompt that evaluates whether the agent's response is successful. Should return True or False.
    - `success_examples` (list of object, optional) — Non-empty list of example responses that should be considered successful
      - `response` (string, required)
      - `type` ("success", required)
    - `failure_examples` (list of object, optional) — Non-empty list of example responses that should be considered failures
      - `response` (string, required)
      - `type` ("failure", required)
    - `parent_folder_id` (string, optional, nullable) — The ID of the parent folder. If not provided, the test will be moved to the root level.
  - UpdateToolCallUnitTestRequest
    - `name` (string, required)
    - `from_conversation_metadata` (object, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional, nullable)
      - `workflow_node_id` (string, optional, nullable)
      - `original_agent_reply` (list of object, optional, default: [])
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
              - `webhook_details` (object, required)
              - `credential_id` (string, optional, default: )
              - `integration_connection_id` (string, optional, default: )
              - `integration_id` (string, optional, default: )
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
            - `type` (enum, optional, nullable)
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
            - `result` (object, optional, nullable)
          - ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel
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
            - `dynamic_variable_updates` (list of object, optional)
            - `integration_id` (string, optional, default: )
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
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
            - `result` (object, optional, nullable) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
        - `interrupted` (boolean, optional, default: false)
        - `ignored_as_backchannel` (boolean, optional, default: false)
        - `original_message` (string, optional, nullable)
        - `reasoning` (list of object, optional)
          - `summary` (string, optional, nullable)
          - `provider_redact` (boolean, optional, default: false)
        - `source_medium` (enum, optional, nullable)
          - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
        - `source_event_id` (integer, optional, nullable)
        - `used_static_kb_document_ids` (list of string, optional)
        - `user_identifier` (string, optional, nullable)
        - `id` (string, optional, nullable)
        - `triggered_guardrails` (list of object, optional)
          - `guardrail_type` (enum, required)
            - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
          - `guardrail_name` (string, optional, nullable)
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `chat_history` (list of object, optional)
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
          - `time_in_call_secs` (integer, require> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update test

PUT https://api.elevenlabs.io/v1/convai/agent-testing/{test_id}
Content-Type: application/json

Updates an agent response test by ID.

Reference: https://elevenlabs.io/docs/api-reference/tests/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `test_id` (string, required) — The id of a chat response test. This is returned on test creation.

### Body (application/json)

- `object or object or object`
  - UpdateResponseUnitTestRequest
    - `name` (string, required)
    - `from_conversation_metadata` (object, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional, nullable)
      - `workflow_node_id` (string, optional, nullable)
      - `original_agent_reply` (list of object, optional, default: [])
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
              - `webhook_details` (object, required)
              - `credential_id` (string, optional, default: )
              - `integration_connection_id` (string, optional, default: )
              - `integration_id` (string, optional, default: )
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
            - `type` (enum, optional, nullable)
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
            - `result` (object, optional, nullable)
          - ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel
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
            - `dynamic_variable_updates` (list of object, optional)
            - `integration_id` (string, optional, default: )
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
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
            - `result` (object, optional, nullable) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
        - `interrupted` (boolean, optional, default: false)
        - `ignored_as_backchannel` (boolean, optional, default: false)
        - `original_message` (string, optional, nullable)
        - `reasoning` (list of object, optional)
          - `summary` (string, optional, nullable)
          - `provider_redact` (boolean, optional, default: false)
        - `source_medium` (enum, optional, nullable)
          - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
        - `source_event_id` (integer, optional, nullable)
        - `used_static_kb_document_ids` (list of string, optional)
        - `user_identifier` (string, optional, nullable)
        - `id` (string, optional, nullable)
        - `triggered_guardrails` (list of object, optional)
          - `guardrail_type` (enum, required)
            - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
          - `guardrail_name` (string, optional, nullable)
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `chat_history` (list of object, optional)
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
            - `webhook_details` (object, required)
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
            - `integration_id` (string, optional, default: )
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success` (KnowledgeBaseToolResultModel)
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
          - `tool_has_been_called` (boolean, required)
          - `type` ("api_integration_webhook", required)
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
          - `integration_id` (string, optional, default: )
          - `credential_id` (string, optional, default: )
          - `integration_connection_id` (string, optional, default: )
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
        - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
      - `source_event_id` (integer, optional, nullable)
      - `used_static_kb_document_ids` (list of string, optional)
      - `user_identifier` (string, optional, nullable)
      - `id` (string, optional, nullable)
      - `triggered_guardrails` (list of object, optional)
        - `guardrail_type` (enum, required)
          - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
        - `guardrail_name` (string, optional, nullable)
    - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
    - `type` ("llm", optional, default: llm)
    - `success_condition` (string, optional, default: ) — A prompt that evaluates whether the agent's response is successful. Should return True or False.
    - `success_examples` (list of object, optional) — Non-empty list of example responses that should be considered successful
      - `response` (string, required)
      - `type` ("success", required)
    - `failure_examples` (list of object, optional) — Non-empty list of example responses that should be considered failures
      - `response` (string, required)
      - `type` ("failure", required)
    - `parent_folder_id` (string, optional, nullable) — The ID of the parent folder. If not provided, the test will be moved to the root level.
  - UpdateToolCallUnitTestRequest
    - `name` (string, required)
    - `from_conversation_metadata` (object, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional, nullable)
      - `workflow_node_id` (string, optional, nullable)
      - `original_agent_reply` (list of object, optional, default: [])
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
              - `webhook_details` (object, required)
              - `credential_id` (string, optional, default: )
              - `integration_connection_id` (string, optional, default: )
              - `integration_id` (string, optional, default: )
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
            - `type` (enum, optional, nullable)
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
            - `result` (object, optional, nullable)
          - ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel
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
            - `dynamic_variable_updates` (list of object, optional)
            - `integration_id` (string, optional, default: )
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
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
            - `result` (object, optional, nullable) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
        - `interrupted` (boolean, optional, default: false)
        - `ignored_as_backchannel` (boolean, optional, default: false)
        - `original_message` (string, optional, nullable)
        - `reasoning` (list of object, optional)
          - `summary` (string, optional, nullable)
          - `provider_redact` (boolean, optional, default: false)
        - `source_medium` (enum, optional, nullable)
          - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
        - `source_event_id` (integer, optional, nullable)
        - `used_static_kb_document_ids` (list of string, optional)
        - `user_identifier` (string, optional, nullable)
        - `id` (string, optional, nullable)
        - `triggered_guardrails` (list of object, optional)
          - `guardrail_type` (enum, required)
            - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
          - `guardrail_name` (string, optional, nullable)
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `chat_history` (list of object, optional)
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
            - `webhook_details` (object, required)
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
            - `integration_id` (string, optional, default: )
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success` (KnowledgeBaseToolResultModel)
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
          - `tool_has_been_called` (boolean, required)
          - `type` ("api_integration_webhook", required)
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
          - `integration_id` (string, optional, default: )
          - `credential_id` (string, optional, default: )
          - `integration_connection_id` (string, optional, default: )
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
        - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
      - `source_event_id` (integer, optional, nullable)
      - `used_static_kb_document_ids` (list of string, optional)
      - `user_identifier` (string, optional, nullable)
      - `id` (string, optional, nullable)
      - `triggered_guardrails` (list of object, optional)
        - `guardrail_type` (enum, required)
          - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
        - `guardrail_name` (string, optional, nullable)
    - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
    - `type` ("tool", optional, default: tool)
    - `tool_call_parameters` (object, optional, nullable) — How to evaluate the agent's tool call (if any). If empty, the tool call is not evaluated.
      - `parameters` (list of object, optional) — Parameters to evaluate for the agent's tool call. If empty, the tool call parameters are not evaluated.
        - `eval` (object, required)
          - `type`: `anything` (MatchAnythingParameterEvaluationStrategy)
          - `type`: `exact` (ExactParameterEvaluationStrategy)
            - `expected_value` (string, required) — The exact string value that the parameter must match.
          - `type`: `llm` (LLMParameterEvaluationStrategy)
            - `description` (string, required) — A description of the evaluation strategy to use for the test.
          - `type`: `regex` (RegexParameterEvaluationStrategy)
            - `pattern` (string, required) — A regex pattern to match the agent's response against.
        - `path` (string, required)
      - `referenced_tool` (object, optional, nullable) — The tool to evaluate a call against.
        - `id` (string, required) — The ID of the tool
        - `type` (enum, required) — The type of the tool
          - Allowed values: `system`, `webhook`, `client`, `workflow`, `api_integration_webhook`, `mcp`, `code`
      - `verify_absence` (boolean, optional, default: false) — Whether to verify that the tool was NOT called.
      - `workflow_node_transition` (object, optional, nullable) — Configuration for testing workflow node transitions. When set, the test will verify the agent transitions to the specified workflow node.
        - `agent_id` (string, required) — The ID of the agent whose workflow contains the target node.
        - `target_node_id` (string, required) — The ID of the workflow node that the agent should transition to.
        - `type` ("node_id", optional, default: node_id)
    - `check_any_tool_matches` (boolean, optional, nullable) — If set to True this test will pass if any tool call returned by the LLM matches the criteria. Otherwise it will fail if more than one tool is returned by the agent.
    - `parent_folder_id` (string, optional, nullable) — The ID of the parent folder. If not provided, the test will be moved to the root level.
  - UpdateSimulationTestRequest
    - `name` (string, required)
    - `from_conversation_metadata` (object, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional, nullable)
      - `workflow_node_id` (string, optional, nullable)
      - `original_agent_reply` (list of object, optional, default: [])
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
              - `webhook_details` (object, required)
              - `credential_id` (string, optional, default: )
              - `integration_connection_id` (string, optional, default: )
              - `integration_id` (string, optional, default: )
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
            - `type` (enum, optional, nullable)
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
            - `result` (object, optional, nullable)
          - ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel
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
            - `dynamic_variable_updates` (list of object, optional)
            - `integration_id` (string, optional, default: )
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
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
            - `result` (object, optional, nullable) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
        - `interrupted` (boolean, optional, default: false)
        - `ignored_as_backchannel` (boolean, optional, default: false)
        - `original_message` (string, optional, nullable)
        - `reasoning` (list of object, optional)
          - `summary` (string, optional, nullable)
          - `provider_redact` (boolean, optional, default: false)
        - `source_medium` (enum, optional, nullable)
          - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
        - `source_event_id` (integer, optional, nullable)
        - `used_static_kb_document_ids` (list of string, optional)
        - `user_identifier` (string, optional, nullable)
        - `id` (string, optional, nullable)
        - `triggered_guardrails` (list of object, optional)
          - `guardrail_type` (enum, required)
            - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
          - `guardrail_name` (string, optional, nullable)
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `chat_history` (list of object, optional)
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
            - `webhook_details` (object, required)
            - `credential_id` (string, optional, default: )
            - `integration_connection_id` (string, optional, default: )
            - `integration_id` (string, optional, default: )
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success` (KnowledgeBaseToolResultModel)
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
          - `tool_has_been_called` (boolean, required)
          - `type` ("api_integration_webhook", required)
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
          - `integration_id` (string, optional, default: )
          - `credential_id` (string, optional, default: )
          - `integration_connection_id` (string, optional, default: )
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
        - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
      - `source_event_id` (integer, optional, nullable)
      - `used_static_kb_document_ids` (list of string, optional)
      - `user_identifier` (string, optional, nullable)
      - `id` (string, optional, nullable)
      - `triggered_guardrails` (list of object, optional)
        - `guardrail_type` (enum, required)
          - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
        - `guardrail_name` (string, optional, nullable)
    - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
    - `type` ("simulation", optional, default: simulation)
    - `success_conditions` (list of string, optional) — List of prompts that evaluate whether the simulation was successful. If provided, all criteria are evaluated and merged into a final result. Capped at the maximum number of evaluation criteria.
    - `simulation_scenario` (string, optional, default: ) — Description of the simulation scenario and user persona for simulation tests.
    - `simulation_max_turns` (integer, optional, default: 5) — Maximum number of conversation turns for simulation tests.
    - `simulation_environment` (string, optional, nullable) — The environment to use when running this simulation test. If not provided, defaults to 'production'.
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
          - `type`: `anything` (MatchAnythingParameterEvaluationStrategy)
          - `type`: `exact` (ExactParameterEvaluationStrategy)
            - `expected_value` (string, required) — The exact string value that the parameter must match.
          - `type`: `llm` (LLMParameterEvaluationStrategy)
            - `description` (string, required) — A description of the evaluation strategy to use for the test.
          - `type`: `regex` (RegexParameterEvaluationStrategy)
            - `pattern` (string, required) — A regex pattern to match the agent's response against.
        - `path` (string, required)
      - `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.
    - `evaluation_model` (enum, optional, nullable, default: claude-sonnet-4-6) — LLM model to use for evaluating simulation results.
      - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
    - `simulated_user_model` (enum, optional, nullable, default: claude-sonnet-4-6) — LLM model for the simulated user.
      - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
    - `parent_folder_id` (string, optional, nullable) — The ID of the parent folder. If not provided, the test will be moved to the root level.
    - `success_condition` (string, optional, nullable, deprecated) — Deprecated legacy single success criterion. Use success_conditions instead. At least one of success_condition or success_conditions is required.

## Response

### 200

Successful Response

- `object`
  - `type`: `llm` (GetResponseUnitTestResponseModel)
    - `id` (string, required)
    - `name` (string, required)
    - `chat_history` (list of object, optional)
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success` (KnowledgeBaseToolResultModel)
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
        - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
      - `source_event_id` (integer, optional, nullable)
      - `used_static_kb_document_ids` (list of string, optional)
      - `user_identifier` (string, optional, nullable)
      - `id` (string, optional, nullable)
      - `triggered_guardrails` (list of object, optional)
        - `guardrail_type` (enum, required)
          - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
        - `guardrail_name` (string, optional, nullable)
    - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
    - `failure_examples` (list of object, optional) — Non-empty list of example responses that should be considered failures
      - `response` (string, required)
      - `type` ("failure", required)
    - `from_conversation_metadata` (object, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional, nullable)
      - `workflow_node_id` (string, optional, nullable)
      - `original_agent_reply` (list of object, optional, default: [])
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
            - `type` (enum, optional, nullable)
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
            - `result` (object, optional, nullable)
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
            - `result` (object, optional, nullable) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
        - `interrupted` (boolean, optional, default: false)
        - `ignored_as_backchannel` (boolean, optional, default: false)
        - `original_message` (string, optional, nullable)
        - `reasoning` (list of object, optional)
          - `summary` (string, optional, nullable)
          - `provider_redact` (boolean, optional, default: false)
        - `source_medium` (enum, optional, nullable)
          - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
        - `source_event_id` (integer, optional, nullable)
        - `used_static_kb_document_ids` (list of string, optional)
        - `user_identifier` (string, optional, nullable)
        - `id` (string, optional, nullable)
        - `triggered_guardrails` (list of object, optional)
          - `guardrail_type` (enum, required)
            - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
          - `guardrail_name` (string, optional, nullable)
    - `success_condition` (string, optional, default: ) — A prompt that evaluates whether the agent's response is successful. Should return True or False.
    - `success_examples` (list of object, optional) — Non-empty list of example responses that should be considered successful
      - `response` (string, required)
      - `type` ("success", required)
  - `type`: `tool` (GetToolCallUnitTestResponseModel)
    - `id` (string, required)
    - `name` (string, required)
    - `chat_history` (list of object, optional)
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success` (KnowledgeBaseToolResultModel)
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
        - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
      - `source_event_id` (integer, optional, nullable)
      - `used_static_kb_document_ids` (list of string, optional)
      - `user_identifier` (string, optional, nullable)
      - `id` (string, optional, nullable)
      - `triggered_guardrails` (list of object, optional)
        - `guardrail_type` (enum, required)
          - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
        - `guardrail_name` (string, optional, nullable)
    - `check_any_tool_matches` (boolean, optional, nullable) — If set to True this test will pass if any tool call returned by the LLM matches the criteria. Otherwise it will fail if more than one tool is returned by the agent.
    - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
    - `from_conversation_metadata` (object, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional, nullable)
      - `workflow_node_id` (string, optional, nullable)
      - `original_agent_reply` (list of object, optional, default: [])
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
            - `type` (enum, optional, nullable)
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
            - `result` (object, optional, nullable)
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
            - `result` (object, optional, nullable) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
        - `interrupted` (boolean, optional, default: false)
        - `ignored_as_backchannel` (boolean, optional, default: false)
        - `original_message` (string, optional, nullable)
        - `reasoning` (list of object, optional)
          - `summary` (string, optional, nullable)
          - `provider_redact` (boolean, optional, default: false)
        - `source_medium` (enum, optional, nullable)
          - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
        - `source_event_id` (integer, optional, nullable)
        - `used_static_kb_document_ids` (list of string, optional)
        - `user_identifier` (string, optional, nullable)
        - `id` (string, optional, nullable)
        - `triggered_guardrails` (list of object, optional)
          - `guardrail_type` (enum, required)
            - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
          - `guardrail_name` (string, optional, nullable)
    - `tool_call_parameters` (object, optional, nullable) — How to evaluate the agent's tool call (if any). If empty, the tool call is not evaluated.
      - `parameters` (list of object, optional) — Parameters to evaluate for the agent's tool call. If empty, the tool call parameters are not evaluated.
        - `eval` (object, required)
          - `type`: `anything` (MatchAnythingParameterEvaluationStrategy)
          - `type`: `exact` (ExactParameterEvaluationStrategy)
            - `expected_value` (string, required) — The exact string value that the parameter must match.
          - `type`: `llm` (LLMParameterEvaluationStrategy)
            - `description` (string, required) — A description of the evaluation strategy to use for the test.
          - `type`: `regex` (RegexParameterEvaluationStrategy)
            - `pattern` (string, required) — A regex pattern to match the agent's response against.
        - `path` (string, required)
      - `referenced_tool` (object, optional, nullable) — The tool to evaluate a call against.
        - `id` (string, required) — The ID of the tool
        - `type` (enum, required) — The type of the tool
          - Allowed values: `system`, `webhook`, `client`, `workflow`, `api_integration_webhook`, `mcp`, `code`
      - `verify_absence` (boolean, optional, default: false) — Whether to verify that the tool was NOT called.
      - `workflow_node_transition` (object, optional, nullable) — Configuration for testing workflow node transitions. When set, the test will verify the agent transitions to the specified workflow node.
        - `agent_id` (string, required) — The ID of the agent whose workflow contains the target node.
        - `target_node_id` (string, required) — The ID of the workflow node that the agent should transition to.
        - `type` ("node_id", optional, default: node_id)
  - `type`: `simulation` (GetSimulationTestResponseModel)
    - `id` (string, required)
    - `name` (string, required)
    - `chat_history` (list of object, optional)
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
              - `message` (string, optional, default: Referenced knowledge base.) — Human-readable status for the LLM about the search results
              - `status` (enum, optional, default: success)
            - `result_type`: `knowledge_base_success` (KnowledgeBaseToolResultModel)
              - `chunk_count` (integer, optional, default: 0)
              - `message` (string, optional, default: Referenced knowledge base.)
              - `status` (enum, optional, default: success)
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
        - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
      - `source_event_id` (integer, optional, nullable)
      - `used_static_kb_document_ids` (list of string, optional)
      - `user_identifier` (string, optional, nullable)
      - `id` (string, optional, nullable)
      - `triggered_guardrails` (list of object, optional)
        - `guardrail_type` (enum, required)
          - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
        - `guardrail_name` (string, optional, nullable)
    - `conversation_initiation_source` (enum, optional, nullable, default: unknown) — Simulate the test as if the conversation originated from this channel.
      - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
    - `dynamic_variables` (map from string to any, optional) — Dynamic variables to replace in the agent config during testing
    - `environment` (string, optional, nullable) — The environment to resolve environment-specific variable values against when running this test (URL, headers, auth connections). If not provided, defaults to 'production'. For simulation tests, simulation_environment takes precedence when set.
    - `evaluation_model` (enum, optional, nullable, default: claude-sonnet-4-6) — LLM model to use for evaluating simulation results.
      - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
    - `from_conversation_metadata` (object, optional, nullable) — Metadata of a conversation this test was created from (if applicable).
      - `conversation_id` (string, required)
      - `agent_id` (string, required)
      - `branch_id` (string, optional, nullable)
      - `workflow_node_id` (string, optional, nullable)
      - `original_agent_reply` (list of object, optional, default: [])
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
            - `type` (enum, optional, nullable)
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
            - `result` (object, optional, nullable)
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
            - `result` (object, optional, nullable) — A common model for workflow tool responses.
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
            - `input_cache_read` (object, optional)
            - `input_cache_write` (object, optional)
            - `output_total` (object, optional)
        - `interrupted` (boolean, optional, default: false)
        - `ignored_as_backchannel` (boolean, optional, default: false)
        - `original_message` (string, optional, nullable)
        - `reasoning` (list of object, optional)
          - `summary` (string, optional, nullable)
          - `provider_redact` (boolean, optional, default: false)
        - `source_medium` (enum, optional, nullable)
          - Allowed values: `audio`, `dtmf`, `text`, `image`, `file`
        - `source_event_id` (integer, optional, nullable)
        - `used_static_kb_document_ids` (list of string, optional)
        - `user_identifier` (string, optional, nullable)
        - `id` (string, optional, nullable)
        - `triggered_guardrails` (list of object, optional)
          - `guardrail_type` (enum, required)
            - Allowed values: `custom`, `prompt_injection`, `self_harm_intent`, `violence_graphic`, `sexual`, `violence`, `harassment`, `sexual_minors`, `self_harm`, `self_harm_instructions`, `harassment_threatening`, `hate`, `hate_threatening`, `profanity`, `religion_or_politics`, `medical_and_legal`, `guardrail`
          - `guardrail_name` (string, optional, nullable)
    - `simulated_user_model` (enum, optional, nullable, default: claude-sonnet-4-6) — LLM model for the simulated user.
      - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
    - `simulation_environment` (string, optional, nullable) — The environment to use when running this simulation test. If not provided, defaults to 'production'.
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
          - `type`: `anything` (MatchAnythingParameterEvaluationStrategy)
          - `type`: `exact` (ExactParameterEvaluationStrategy)
            - `expected_value` (string, required) — The exact string value that the parameter must match.
          - `type`: `llm` (LLMParameterEvaluationStrategy)
            - `description` (string, required) — A description of the evaluation strategy to use for the test.
          - `type`: `regex` (RegexParameterEvaluationStrategy)
            - `pattern` (string, required) — A regex pattern to match the agent's response against.
        - `path` (string, required)
      - `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.
    - `success_condition` (string, optional, nullable, deprecated) — Deprecated legacy single success criterion. Use success_conditions instead. At least one of success_condition or success_conditions is required.

## Examples

**Request**

```json
{
  "name": "string"
}
```

**Response**

```json
{
  "type": "llm",
  "id": "string",
  "name": "string",
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
    ]
  },
  "success_condition": "",
  "success_examples": [
    {
      "response": "string",
      "type": "string"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.update("test_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.update(
    test_id="test_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/test_id"

	payload := strings.NewReader("{\n  \"name\": \"string\"\n}")

	req, _ := http.NewRequest("PUT", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/test_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.elevenlabs.io/v1/convai/agent-testing/test_id")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.elevenlabs.io/v1/convai/agent-testing/test_id', [
  'body' => '{
  "name": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/test_id");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/test_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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
