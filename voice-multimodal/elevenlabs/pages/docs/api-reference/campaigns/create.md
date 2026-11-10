---
title: "Create campaign"
source: https://elevenlabs.io/docs/api-reference/campaigns/create.md
path: docs/api-reference/campaigns/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create campaign

POST https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit
Content-Type: application/json

Create an outbound campaign that calls or messages each recipient with the agent, within the policy's calling windows, retrying and following up as it allows. Returns `201` for a new campaign. A repeated request, matched by `idempotency_key` or else by its body, returns the existing campaign with `created` false.

Reference: https://elevenlabs.io/docs/api-reference/campaigns/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

This endpoint expects a SubmitCampaignRequest.

- `call_name` (string, required) — The campaign's name.
- `agent_id` (string, required) — The agent that places the calls.
- `recipients` (list of SubmitCampaignRecipient, required) — Who to call. Each recipient becomes a lead of the campaign.
- `channel_config` (SubmitCampaignRequestChannelConfig, required)
- `scheduled_time_unix` (integer, optional, nullable) — When to start calling; omit to start now. Calls still wait for the next calling window.
- `timezone` (string, optional, nullable) — IANA timezone to read the calling windows in, overriding the policy's.
- `branch_id` (string, optional, nullable) — The agent branch to call with.
- `environment` (string, optional, nullable) — The environment to resolve the agent's environment variables in.
- `target_concurrency_limit` (integer, optional, nullable) — The most calls to place at once.
- `idempotency_key` (string, optional, nullable) — Makes the request safe to retry: a repeat with the same key returns the campaign it created.
- `outcome` (SubmitCampaignRequestOutcome, optional, nullable) — The result that counts as success for the campaign's calls.
- `policy` (PolicyConfig-Input, optional, nullable) — Policy to snapshot onto the campaign. When set, it wins over the workspace default and any per-agent override; when omitted, the workspace configuration must exist and supplies the policy.
- `variant` (enum, optional, nullable) — `simple` runs one attempt per recipient with always-on calling windows and nothing collected, and cannot be combined with `policy`. `advanced` uses `policy` or the workspace configuration, and is the default for phone campaigns.
  - Allowed values: `simple`, `advanced`

## Response

### 200

Successful Response

- `campaign` (CampaignResponse, required)
- `created` (boolean, required) — False when the request repeated an earlier one and returned its campaign.
- `within_calling_window` (boolean, required) — Whether calling starts right away rather than at the next calling window.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### SubmitCampaignRecipient

- `phone_number` (string, optional, nullable) — The number to call, in E.164 format such as `+14155550100`.
- `phone_numbers` (list of string, optional, nullable) — More numbers to call, in order after `phone_number`. The lead moves on to the next one when calls to its current number keep failing.
- `whatsapp_user_id` (string, optional, nullable) — The contact's WhatsApp user ID. WhatsApp campaigns use it instead of the phone numbers.
- `id` (string, optional, nullable) — Your identifier for the recipient, returned as its lead's `recipient_id`.
- `conversation_initiation_client_data` (ConversationInitiationClientDataRequest-Input, optional, nullable) — Dynamic variables and overrides for this recipient's calls.

### SubmitCampaignRequestChannelConfig

- `channel`: `phone` (PhoneChannelConfig)
  - `agent_phone_number_id` (string, required) — The phone number to call from.
  - `mode_config` (PhoneVoiceConfig-Input, optional)
- `channel`: `whatsapp` (SubmitWhatsAppChannelConfig)
  - `mode_config` (SubmitWhatsAppChannelConfigModeConfig, required)
  - `whatsapp_phone_number_id` (string, required) — The WhatsApp phone number to call or message from.

### SubmitCampaignRequestOutcome

The result that counts as success for the campaign's calls.

- `type`: `data_collection` (DataCollectionOutcome)
  - `data_collection_id` (string, required) — The agent's data collection item a successful call sets.
  - `equals` (list of CampaignResponseOutcomeDiscriminatorMappingDataCollectionEqualsItems, required) — Values that count as success, all of the item's type.
- `type`: `evaluation_criteria` (EvaluationCriterionOutcome)
  - `criteria_id` (string, required) — The agent's evaluation criterion a successful call meets.

### PolicyConfig-Input

- `timezone` (string, optional, default: UTC) — IANA timezone the calling periods are read in.
- `retry` (RetryPolicy, optional)
- `calling_periods` (list of CallingPeriod, optional) — The weekly windows calls may be placed in.
- `data_collection` (DataCollectionConfig, optional) — The agent's data collection items that steer follow-up calls. Each defaults to the built-in item for its purpose; `null` turns it off.
- `followup_context` (FollowupContextPolicy, optional) — Which `campaign__` dynamic variables follow-up calls get.

### CampaignResponse

- `campaign_id` (string, required)
- `call_name` (string, required) — The campaign's name.
- `agent_id` (string, required)
- `channel_config` (CampaignResponseChannelConfig, required)
- `status` (enum, required) — `attention` means an open attention item holds back some of the campaign's calls while the rest go ahead. `stopping` means queued calls are cancelled and calls already placed are finishing.
  - Allowed values: `active`, `paused`, `stopping`, `stopped`, `completed`, `failed`, `attention`
- `policy` (CampaignPolicySnapshot, required) — The policy the campaign took when it was created.
- `variant` (enum, required)
  - Allowed values: `simple`, `advanced`
- `source` (enum, required, nullable) — Whether the campaign was created in the app or through the API.
  - Allowed values: `ui`, `api`
- `outcome` (CampaignResponseOutcome, required, nullable) — The result that counts as success for the campaign's calls.
- `created_at_unix` (integer, required)
- `scheduled_time_unix` (integer, required, nullable) — When the campaign starts calling; unset to start once created.
- `updated_at_unix` (integer, required)
- `branch_id` (string, required, nullable) — The agent branch the campaign calls with.
- `environment` (string, required, nullable) — The environment the agent's environment variables resolve in.
- `target_concurrency_limit` (integer, required, nullable) — The most calls the campaign places at once.
- `channel` (enum, required)
  - Allowed values: `phone`, `whatsapp`
- `mode` (enum, required)
  - Allowed values: `voice`, `message`
- `counts` (CampaignSummaryCounts, required)
- `agent_name` (string, required, default: )

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ConversationInitiationClientDataRequest-Input

- `conversation_config_override` (ConversationConfigClientOverride-Input, optional)
- `custom_llm_extra_body` (map from string to any, optional)
- `user_id` (string, optional, nullable) — ID of the end user participating in this conversation (for agent owner's user identification)
- `source_info` (ConversationInitiationSourceInfo, optional) — Information about the source of conversation initiation
- `branch_id` (string, optional, nullable) — ID of the agent branch to use for this conversation
- `environment` (string, optional, nullable) — Environment to use for resolving environment variables
- `starting_workflow_node_id` (string, optional, nullable) — If set, start the workflow at this node id instead of the default entry
- `procedure_ids` (list of string, optional, nullable) — If set, only these procedures are available to the starting agent. Each ID must be attached to that agent; unknown IDs fail conversation start. An empty list disables all of that agent's procedures. Not applied after an agent transfer. Requires enable_procedure_ids_from_client.
- `start_procedure_ids` (list of string, optional, nullable) — If set, these free-form procedures start when the conversation starts. Accepts at most five IDs. Each ID must be available after procedure_ids is applied. Unknown IDs and structured procedures fail conversation start. Requires enable_procedure_ids_from_client.
- `dynamic_variables` (map from string to any, optional)

### PhoneVoiceConfig-Input

- `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
- `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `twilio_machine_detection` (TwilioMachineDetectionConfig, optional, nullable) — Configuration for Twilio's carrier-level answering machine detection (AMD). Omit or set to null to disable it. Ignored for non-Twilio providers and for inbound calls. The resulting verdict is delivered as its own `answering_machine_detection` webhook event, which requires that event to be enabled on the workspace or agent webhook settings; it is not part of the conversation or the post-call webhook. Detection runs asynchronously so it never delays the start of the conversation, and the verdict can arrive at any point during the call -- with `detect_message_end`, even after it has ended. Twilio bills separately for AMD.
- `mode` ("voice", optional, default: voice)

### SubmitWhatsAppChannelConfigModeConfig

- `mode`: `message` (SubmitWhatsAppMessageConfig)
  - `template` (SubmitWhatsAppTemplateRef, required) — Names the approved Meta template to send. The server loads the template itself, so the client never supplies its components.
- `mode`: `voice` (WhatsAppVoiceConfig)
  - `whatsapp_call_permission_request_template_language_code` (string, required) — The language code of that template.
  - `whatsapp_call_permission_request_template_name` (string, required) — The approved template that asks the contact for permission to call.

### CampaignResponseOutcomeDiscriminatorMappingDataCollectionEqualsItems

- string
- integer
- double
- boolean

### RetryPolicy

- `retry_delay_seconds` (integer, optional, default: 600) — How long to wait before a short retry.
- `max_short_retries` (integer, optional, default: 1) — Retries a calling window allows after a failed call. Once used up, the next retry waits for the following window, which starts afresh.
- `max_total_calls` (integer, optional, default: 6) — The most calls a lead gets, counting the first.
- `max_callbacks` (integer, optional, default: 2) — The most callbacks to honor for one number.
- `max_redirects` (integer, optional, default: 2) — The most times a lead follows a request to call another number.
- `interval_placement` (enum, optional, default: start) — Where in a later calling window a pushed-back call lands: at its `start`, at a `random` time, or `rotate`d `rotate_step_seconds` past where the last call in that window failed.
  - Allowed values: `start`, `random`, `rotate`
- `rotate_step_seconds` (integer, optional, default: 900) — How far `rotate` placement moves each call. Only used by `rotate`.
- `max_consecutive_failures_per_number` (integer, optional, nullable) — Calls to one number that may fail in a row before the lead moves on to its next listed number, or ends when there is none. An answered call, or a redirect to a new number, restarts the count. Unset leaves only `max_total_calls`.

### CallingPeriod

- `weekdays` (list of integer, required) — Days the intervals apply on, from `0` (Monday) to `6` (Sunday).
- `intervals` (list of CallingIntervalPolicy, required) — Windows on each of those days. They may not overlap on any day.

### DataCollectionConfig

The agent's data collection items that steer follow-up calls. Each defaults to the built-in item for its purpose; `null` turns it off.

- `callback_time` (string, optional, nullable, default: __system_data_collection_callback_time) — The item holding when the contact asked to be called back.
- `redirect_phone_number` (string, optional, nullable, default: __system_data_collection_redirect_phone_number) — The item holding another number the contact asked to be called on.
- `stop` (string, optional, nullable, default: __system_data_collection_do_not_call) — The item that is true when the contact asked not to be called again.
- `mappings` (map from string to string, optional) — Copies data collection results into dynamic variables for later calls: each key is a data collection item ID and its value the variable's name.

### FollowupContextPolicy

Which `campaign__` dynamic variables follow-up calls get.

- `call_type` (boolean, optional, default: true) — Pass the call type as `campaign__call_type`.
- `previous_conversation_id` (boolean, optional, default: true) — Pass the last conversation's ID as `campaign__previous_conversation_id`.
- `previous_summary` (boolean, optional, default: true) — Pass the last conversation's summary as `campaign__previous_summary`.
- `previous_transcript` (boolean, optional, default: true) — Pass the last conversation's transcript as `campaign__previous_transcript`.

### CampaignResponseChannelConfig

- `channel`: `phone` (PhoneChannelConfig)
  - `agent_phone_number_id` (string, required) — The phone number to call from.
  - `mode_config` (PhoneVoiceConfig-Output, optional)
- `channel`: `whatsapp` (WhatsAppChannelConfig)
  - `mode_config` (WhatsAppChannelConfigModeConfig, required)
  - `whatsapp_phone_number_id` (string, required) — The WhatsApp phone number to call or message from.

### CampaignPolicySnapshot

The policy the campaign took when it was created, laid out like a submitted `policy`.

- `timezone` (string, required)
- `retry` (RetryPolicy, required)
- `calling_periods` (list of CallingPeriodPolicy, required)
- `data_collection` (DataCollectionPolicy, required)
- `followup_context` (FollowupContextPolicy, required) — Which `campaign__` dynamic variables follow-up calls get.

### CampaignResponseOutcome

The result that counts as success for the campaign's calls.

- `type`: `data_collection` (DataCollectionOutcome)
  - `data_collection_id` (string, required) — The agent's data collection item a successful call sets.
  - `equals` (list of CampaignResponseOutcomeDiscriminatorMappingDataCollectionEqualsItems, required) — Values that count as success, all of the item's type.
- `type`: `evaluation_criteria` (EvaluationCriterionOutcome)
  - `criteria_id` (string, required) — The agent's evaluation criterion a successful call meets.

### CampaignSummaryCounts

- `leads` (integer, required)
- `terminal_leads` (integer, required) — Leads that won't be called again.
- `open_attention` (integer, required) — Attention items not yet resolved.
- `delivery` (RecipientDeliveryCounts, optional, nullable) — How many messages reached each stage; set when getting one message campaign.

### ValidationErrorLocItems

- string
- integer

### ConversationConfigClientOverride-Input

- `asr` (ASRConversationalConfigOverride, optional, nullable) — Configuration for conversational transcription
- `turn` (TurnConfigOverride, optional, nullable) — Configuration for turn detection
- `tts` (TTSConversationalConfigOverride, optional, nullable) — Configuration for conversational text to speech
- `conversation` (ConversationConfigOverride, optional, nullable) — Configuration for conversational events
- `agent` (AgentConfigOverride-Input, optional, nullable) — Agent specific configuration

### ConversationInitiationSourceInfo

Information about the source of conversation initiation

- `source` (enum, optional, nullable, default: unknown) — Source of the conversation initiation
  - Allowed values: `unknown`, `android_sdk`, `node_js_sdk`, `react_native_sdk`, `react_sdk`, `js_sdk`, `python_sdk`, `widget`, `sip_trunk`, `twilio`, `exotel`, `genesys`, `avaya`, `audiocodes`, `swift_sdk`, `whatsapp`, `twilio_sms`, `flutter_sdk`, `zendesk_integration`, `slack_integration`, `telegram_integration`, `intercom_integration`, `freshdesk_integration`, `salesforce_integration`, `template_preview`, `genesys_bot_connector`, `subagent_tool`
- `version` (string, optional, nullable) — The SDK version number

### TwilioMachineDetectionConfig

How to run Twilio's carrier-level answering machine detection (AMD) on a call.

- `mode` (enum, optional, default: enable) — How thorough the detection should be. `enable` returns a verdict as soon as Twilio can tell a human from a machine. `detect_message_end` also waits for the voicemail greeting to finish, which is what produces the `machine_end_*` verdicts, but returns a result later.
  - Allowed values: `enable`, `detect_message_end`
- `actions` (list of TwilioMachineDetectionRule, optional) — Actions to take on the call per AMD verdict. Each action can appear in at most one rule, so list all of its verdicts together. Verdicts without a rule leave the call running.

### SubmitWhatsAppTemplateRef

Names the approved Meta template to send. The server loads the template itself, so the client never supplies its components.

- `name` (string, required)
- `language` (string, required) — The template's language code, such as `en_US`.

### CallingIntervalPolicy

- `start` (string, required) — Local start time, as `HH:MM`.
- `end` (string, required) — Local end time, as `HH:MM`; `24:00` ends at midnight.

### PhoneVoiceConfig-Output

- `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
- `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `twilio_machine_detection` (TwilioMachineDetectionConfig, optional, nullable) — Configuration for Twilio's carrier-level answering machine detection (AMD). Omit or set to null to disable it. Ignored for non-Twilio providers and for inbound calls. The resulting verdict is delivered as its own `answering_machine_detection` webhook event, which requires that event to be enabled on the workspace or agent webhook settings; it is not part of the conversation or the post-call webhook. Detection runs asynchronously so it never delays the start of the conversation, and the verdict can arrive at any point during the call -- with `detect_message_end`, even after it has ended. Twilio bills separately for AMD.
- `mode` ("voice", optional, default: voice)

### WhatsAppChannelConfigModeConfig

- `mode`: `message` (WhatsAppMessageConfig)
  - `template` (WhatsAppTemplate, required) — The Meta template as it was approved at submission.
- `mode`: `voice` (WhatsAppVoiceConfig)
  - `whatsapp_call_permission_request_template_language_code` (string, required) — The language code of that template.
  - `whatsapp_call_permission_request_template_name` (string, required) — The approved template that asks the contact for permission to call.

### CallingPeriodPolicy

- `weekdays` (list of integer, required)
- `intervals` (list of CallingIntervalPolicy, required) — Windows on each of those days. They may not overlap on any day.

### DataCollectionPolicy

- `callback_time` (string, optional, nullable)
- `redirect_phone_number` (string, optional, nullable)
- `stop` (string, optional, nullable)
- `mappings` (map from string to string, optional) — Copies data collection results into dynamic variables for later calls: each key is a data collection item ID and its value the variable's name.

### RecipientDeliveryCounts

- `sent` (integer, optional, default: 0)
- `delivered` (integer, optional, default: 0)
- `read` (integer, optional, default: 0)
- `replied` (integer, optional, default: 0)
- `failed` (integer, optional, default: 0)

### ASRConversationalConfigOverride

- `keywords` (list of string, optional, nullable) — Keywords to boost prediction probability for

### TurnConfigOverride

- `soft_timeout_config` (SoftTimeoutConfigOverride, optional, nullable) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
- `noisy_environment_message` (string, optional, nullable) — What the agent says when it detects a noisy environment.

### TTSConversationalConfigOverride

- `model_id` (enum, optional, nullable, default: eleven_v4_turbo) — The model to use for TTS
  - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`, `eleven_v4`, `eleven_v4_turbo`
- `voice_id` (string, optional, nullable) — The voice ID to use for TTS
- `supported_voices` (list of SupportedVoice, optional, nullable) — Additional supported voices for the agent
- `stability` (double, optional, nullable) — The stability of generated speech
- `speed` (double, optional, nullable) — The speed of generated speech
- `similarity_boost` (double, optional, nullable) — The similarity boost for generated speech
- `pronunciation_dictionary_locators` (list of PydanticPronunciationDictionaryVersionLocator, optional, nullable) — The pronunciation dictionary locators

### ConversationConfigOverride

- `text_only` (boolean, optional, nullable) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
- `max_duration_seconds` (integer, optional, nullable) — The maximum duration of a conversation in seconds

### AgentConfigOverride-Input

- `first_message` (string, optional, nullable) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional, nullable) — Language of the agent - used for ASR and TTS
- `max_conversation_duration_message` (string, optional, nullable) — If non-empty, the message the agent will send when max conversation duration is reached.
- `prompt` (PromptAgentAPIModelOverride-Input, optional, nullable) — The prompt for the agent

### TwilioMachineDetectionRule

Action to take on a live call for the given AMD verdicts.

- `action` (enum, required)
  - Allowed values: `hang_up`
- `answered_by` (list of enum, required) — Verdicts that trigger the action.
  - Allowed values: `human`, `fax`, `unknown`, `machine_start`, `machine_end_beep`, `machine_end_silence`, `machine_end_other`

### WhatsAppTemplate

- `name` (string, required)
- `language` (string, required) — https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/supported-languages
- `components` (list of WhatsAppTemplateComponent, required)
- `parameter_format` (enum, optional, default: POSITIONAL)
  - Allowed values: `POSITIONAL`, `NAMED`
- `category` (string, optional, nullable) — https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/

### SoftTimeoutConfigOverride

- `message` (string, optional, nullable) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
- `additional_soft_timeout_messages` (list of string, optional, nullable) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.

### SupportedVoice

- `label` (string, required)
- `voice_id` (string, required)
- `description` (string, optional, nullable)
- `language` (string, optional, nullable)
- `model_family` (enum, optional, nullable)
  - Allowed values: `turbo`, `flash`, `multilingual`, `v3_conversational`, `v4`, `v4_turbo`
- `optimize_streaming_latency` (enum, optional, nullable)
  - Allowed values: `0`, `1`, `2`, `3`, `4`
- `stability` (double, optional, nullable)
- `speed` (double, optional, nullable)
- `similarity_boost` (double, optional, nullable)

### PydanticPronunciationDictionaryVersionLocator

A locator for other documents to be able to reference a specific dictionary and it's version. This is a pydantic version of PronunciationDictionaryVersionLocatorDBModel. Required to ensure compat with the rest of the agent data models.

- `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
- `version_id` (string, required, nullable) — The ID of the version of the pronunciation dictionary

### PromptAgentAPIModelOverride-Input

- `prompt` (string, optional, nullable) — The prompt for the agent
- `llm` (enum, optional, nullable) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `gemini-4-argon`, `claude-sonnet-4-5`, `claude-opus-4-6`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-5-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-haiku-5-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `deepseek-v41-flash`, `nemotron-35-super-vl-nvfp4`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `tool_ids` (list of string, optional, nullable) — A list of IDs of tools used by the agent
- `tool_ids_strict` (boolean, optional, nullable) — Only applies as a conversation override, allowed whenever tool_ids may be overridden. When true, the overridden tool_ids is the full list of tools allowed in the conversation, including tools on workflow nodes. Ignored when set on the agent.
- `native_mcp_server_ids` (list of string, optional, nullable) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional, nullable) — A list of knowledge bases to be used by the agent

### WhatsAppTemplateComponent

- `type` (string, required)
- `format` (string, optional, nullable)
- `text` (string, optional, nullable)
- `buttons` (list of WhatsAppTemplateComponentButton, optional, nullable)

### KnowledgeBaseLocator

- `type` (enum, required) — The type of the knowledge base
  - Allowed values: `file`, `url`, `text`, `folder`
- `name` (string, required) — The name of the knowledge base
- `id` (string, required) — The ID of the knowledge base
- `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
  - Allowed values: `prompt`, `auto`

### WhatsAppTemplateComponentButton

- `type` (string, required)
- `text` (string, optional, nullable)
- `url` (string, optional, nullable)

## Examples

**Request**

```json
{
  "call_name": "string",
  "agent_id": "string",
  "recipients": [
    {}
  ],
  "channel_config": {
    "agent_phone_number_id": "string"
  }
}
```

**Response**

```json
{
  "campaign": {
    "campaign_id": "string",
    "call_name": "string",
    "agent_id": "string",
    "channel_config": {
      "channel": "phone",
      "agent_phone_number_id": "string",
      "mode_config": {
        "ringing_timeout_secs": 60,
        "twilio_call_recording_enabled": false,
        "twilio_machine_detection": {
          "mode": "enable",
          "actions": [
            {
              "action": "hang_up",
              "answered_by": [
                "human"
              ]
            }
          ]
        },
        "mode": "voice"
      }
    },
    "status": "active",
    "policy": {
      "timezone": "string",
      "retry": {
        "retry_delay_seconds": 600,
        "max_short_retries": 1,
        "max_total_calls": 6,
        "max_callbacks": 2,
        "max_redirects": 2,
        "interval_placement": "start",
        "rotate_step_seconds": 900,
        "max_consecutive_failures_per_number": 1
      },
      "calling_periods": [
        {
          "weekdays": [
            1
          ],
          "intervals": [
            {
              "start": "string",
              "end": "string"
            }
          ]
        }
      ],
      "data_collection": {
        "callback_time": "string",
        "redirect_phone_number": "string",
        "stop": "string",
        "mappings": {}
      },
      "followup_context": {
        "call_type": true,
        "previous_conversation_id": true,
        "previous_summary": true,
        "previous_transcript": true
      }
    },
    "variant": "simple",
    "source": "ui",
    "outcome": {
      "type": "evaluation_criteria",
      "criteria_id": "string"
    },
    "created_at_unix": 1,
    "scheduled_time_unix": 1,
    "updated_at_unix": 1,
    "branch_id": "string",
    "environment": "string",
    "target_concurrency_limit": 1,
    "channel": "phone",
    "mode": "voice",
    "counts": {
      "leads": 1,
      "terminal_leads": 1,
      "open_attention": 1,
      "delivery": {
        "sent": 0,
        "delivered": 0,
        "read": 0,
        "replied": 0,
        "failed": 0
      }
    },
    "agent_name": ""
  },
  "created": true,
  "within_calling_window": true
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit"

payload = {
    "call_name": "string",
    "agent_id": "string",
    "recipients": [{}],
    "channel_config": { "agent_phone_number_id": "string" }
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"call_name":"string","agent_id":"string","recipients":[{}],"channel_config":{"agent_phone_number_id":"string"}}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit"

	payload := strings.NewReader("{\n  \"call_name\": \"string\",\n  \"agent_id\": \"string\",\n  \"recipients\": [\n    {}\n  ],\n  \"channel_config\": {\n    \"agent_phone_number_id\": \"string\"\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"call_name\": \"string\",\n  \"agent_id\": \"string\",\n  \"recipients\": [\n    {}\n  ],\n  \"channel_config\": {\n    \"agent_phone_number_id\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit")
  .header("Content-Type", "application/json")
  .body("{\n  \"call_name\": \"string\",\n  \"agent_id\": \"string\",\n  \"recipients\": [\n    {}\n  ],\n  \"channel_config\": {\n    \"agent_phone_number_id\": \"string\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit', [
  'body' => '{
  "call_name": "string",
  "agent_id": "string",
  "recipients": [
    {}
  ],
  "channel_config": {
    "agent_phone_number_id": "string"
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"call_name\": \"string\",\n  \"agent_id\": \"string\",\n  \"recipients\": [\n    {}\n  ],\n  \"channel_config\": {\n    \"agent_phone_number_id\": \"string\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "call_name": "string",
  "agent_id": "string",
  "recipients": [[]],
  "channel_config": ["agent_phone_number_id": "string"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/submit")! as URL,
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
