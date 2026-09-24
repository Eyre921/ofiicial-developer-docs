---
title: "Preview rebased configuration"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/preview-rebase.md
path: docs/eleven-agents/api-reference/agents/branches/preview-rebase
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Preview rebased configuration

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}/rebase-preview

Returns the result of rebasing the branch onto main without performing the rebase. Useful for showing an accurate diff before confirming.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/preview-rebase

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.
- `branch_id` (string, required) — Unique identifier for the source branch to merge from.

## Response

### 200

Successful Response

- `agent_id` (string, required) — The ID of the agent
- `name` (string, required) — The name of the agent
- `conversation_config` (ConversationalConfig, required) — The conversation configuration of the agent
- `metadata` (AgentMetadataResponseModel, required) — The metadata of the agent
- `platform_settings` (AgentPlatformSettingsResponseModel, optional) — The platform settings of the agent
- `phone_numbers` (list of MergePreviewResponseModelPhoneNumbersItem, optional) — The phone numbers of the agent
- `whatsapp_accounts` (list of GetWhatsAppAccountResponse, optional) — WhatsApp accounts assigned to the agent
- `workflow` (AgentWorkflowResponseModel, optional) — The workflow of the agent
- `access_info` (ResourceAccessInfo, optional) — The access information of the agent for the user
- `tags` (list of string, optional) — Agent tags used to categorize the agent
- `version_id` (string, optional) — The ID of the version the agent is on
- `branch_id` (string, optional) — The ID of the branch the agent is on
- `main_branch_id` (string, optional) — The ID of the main branch for this agent
- `procedures` (map from string to ProcedureRefResponseModel, optional) — Procedures keyed by procedure_id.
- `default_hold_audio_url` (string, optional, default: https://eleven-public-cdn-common.elevenlabs.io/convai/ambient-audio-assets/elevator1.mp3) — URL of the default hold tone played to queued callers when no custom hold audio is uploaded, so the dashboard can preview it.
- `overridden_fields` (list of string, optional) — Dot-paths of config fields where both branches modified the same field relative to their common ancestor (conflicts). Present regardless of which side wins the conflict.
- `conflicts` (list of FieldConflict, optional) — Structured view of the same conflicts as overridden_fields, each carrying the value on the base (common ancestor), source branch, and target branch so the divergence can be presented and resolved field-by-field.
- `source_identical_to_target` (boolean, optional, default: false) — True when the merge/rebase would be a no-op, i.e. the merged result is identical to the source branch tip. The rebase endpoint rejects in this case.

## Errors

### 422 Branches Preview Rebase Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ConversationalConfig

- `asr` (AsrConversationalConfig, optional) — Configuration for conversational transcription
- `turn` (TurnConfig, optional) — Configuration for turn detection
- `tts` (TtsConversationalConfigOutput, optional) — Configuration for conversational text to speech
- `conversation` (ConversationConfigOutput, optional) — Configuration for conversational events
- `language_presets` (map from string to LanguagePresetOutput, optional) — Language presets for conversations
- `vad` (VadConfig, optional) — Configuration for voice activity detection
- `agent` (AgentConfig, optional) — Agent specific configuration

### AgentMetadataResponseModel

- `created_at_unix_secs` (integer, required) — The creation time of the agent in unix seconds
- `updated_at_unix_secs` (integer, required) — The last update time of the agent in unix seconds

### AgentPlatformSettingsResponseModel

- `evaluation` (EvaluationSettingsOutput, optional) — Settings for evaluation
- `widget` (WidgetConfig, optional) — Configuration for the widget
- `data_collection` (map from string to AnalysisProperty, optional) — Data collection settings
- `data_collection_scopes` (map from string to enum, optional) — Scope per data collection item ID. Missing keys default to conversation scope.
  - Allowed values: `conversation`, `agent`
- `analysis_items` (AgentAnalysisItemsOutput, optional) — Evaluation + data-collection items attached by reference. None means the agent has not been migrated onto analysis items yet (distinct from an empty, migrated set); reads fall back to the legacy evaluation/data_collection fields in that case.
- `overrides` (ConversationInitiationClientDataConfigOutput, optional) — Additional overrides for the agent during conversation initiation
- `workspace_overrides` (AgentWorkspaceOverridesOutput, optional) — Workspace overrides for the agent
- `testing` (AgentTestingSettings, optional) — Testing configuration for the agent
- `archived` (boolean, optional, default: false) — Whether the agent is archived
- `guardrails` (GuardrailsV1Output, optional) — Guardrails configuration for the agent
- `summary_language` (string, optional) — Language for all conversation analysis outputs (summaries, titles, evaluation rationales, data collection rationales). If not set, the language will be inferred from the conversation. Must be one of the supported conversation languages.
- `auto_translate_transcript_to_app_language` (boolean, optional) — When enabled, a conversation transcript is automatically translated to the viewer's application language when they open the transcript page. If not set or false, transcripts are shown in their original language unless the viewer manually selects a translation.
- `auth` (AuthSettings, optional) — Settings for authentication
- `call_limits` (AgentCallLimits, optional) — Call limits for the agent
- `queueing_config` (AgentQueueingConfig, optional) — Concurrency wait-queue config for the agent
- `privacy` (PrivacyConfigOutput, optional) — Privacy settings for the agent
- `trust_context` (enum, optional, default: unknown) — The trust context in which the agent operates.
  - Allowed values: `unknown`, `low`, `high`
- `analysis_llm` (enum, optional) — Default LLM model for post-call analysis (evaluation and data collection)
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `topic_discovery` (TopicDiscoverySettings, optional) — Per-agent topic discovery configuration
- `sentiment_analysis` (SentimentAnalysisSettings, optional) — Per-agent post-call sentiment analysis configuration
- `alerting` (AlertingSettingsResponse, optional) — Agent-level alerting configuration overriding workspace settings.
- `safety` (SafetyResponseModel, optional)

### MergePreviewResponseModelPhoneNumbersItem

- `provider`: `exotel`
  - `label` (string, required) — Label for the phone number
  - `phone_number` (string, required) — Phone number
  - `phone_number_id` (string, required) — The ID of the phone number
  - `assigned_agent` (PhoneNumberAgentInfo, optional) — The agent that is assigned to the phone number
  - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
  - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls
- `provider`: `sip_trunk`
  - `label` (string, required) — Label for the phone number
  - `livekit_stack` (enum, required, default: standard) — Type of Livekit stack used for this number.
    - Allowed values: `standard`, `static`
  - `phone_number` (string, required) — Phone number
  - `phone_number_id` (string, required) — The ID of the phone number
  - `assigned_agent` (PhoneNumberAgentInfo, optional) — The agent that is assigned to the phone number
  - `inbound_trunk` (GetPhoneNumberInboundSipTrunkConfigResponseModel, optional) — Configuration of the Inbound SIP trunk - if configured.
  - `outbound_trunk` (GetPhoneNumberOutboundSipTrunkConfigResponseModel, optional) — Configuration of the Outbound SIP trunk - if configured.
  - `store_sip_messages` (boolean, optional, default: true) — Whether to store SIP messages for this phone number.
  - `provider_config` (GetPhoneNumberOutboundSipTrunkConfigResponseModel, optional, deprecated) — SIP Trunk configuration details for a phone number
  - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
  - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls
- `provider`: `twilio`
  - `label` (string, required) — Label for the phone number
  - `phone_number` (string, required) — Phone number
  - `phone_number_id` (string, required) — The ID of the phone number
  - `assigned_agent` (PhoneNumberAgentInfo, optional) — The agent that is assigned to the phone number
  - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
  - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls

### GetWhatsAppAccountResponse

- `business_account_id` (string, required)
- `phone_number_id` (string, required)
- `business_account_name` (string, required)
- `phone_number_name` (string, required)
- `phone_number` (string, required)
- `account_type` (enum, optional, default: cloud_api) — Which Embedded Signup flow produced this account.
  - Allowed values: `cloud_api`, `coexistence`
- `assigned_agent_id` (string, optional)
- `enable_messaging` (boolean, optional, default: true)
- `enable_audio_message_response` (boolean, optional, default: true)
- `enable_typing_indicator` (boolean, optional, default: true)
- `assigned_agent_name` (string, optional)
- `is_token_expired` (boolean, optional, default: false)

### AgentWorkflowResponseModel

- `edges` (map from string to WorkflowEdgeModelOutput, required)
- `nodes` (map from string to AgentWorkflowResponseModelNodesValue, required)
- `prevent_subagent_loops` (boolean, required, default: false) — Whether to prevent loops in the workflow execution.

### ResourceAccessInfo

- `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
- `creator_name` (string, required) — Name of the agent's creator
- `creator_email` (string, required) — Email of the agent's creator
- `role` (enum, required) — The role of the user making the request
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
  - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`

### ProcedureRefResponseModel

- `procedure_id` (string, required) — Procedure ID
- `version_id` (string, optional) — Version ID of a version of the procedure. None for a procedure never versioned.
- `name` (string, optional, default: ) — Procedure name
- `type` (enum, optional, default: free_form) — Procedure type
  - Allowed values: `free_form`, `deterministic`, `folder`
- `trigger` (string, optional, default: ) — When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it.
- `referenced_tool_ids` (list of string, optional) — Tool IDs referenced in the procedure content
- `referenced_kb_ids` (list of string, optional) — Knowledge base IDs referenced in the procedure content
- `referenced_procedure_ids` (list of string, optional) — Procedure IDs referenced in the procedure content
- `referenced_dynamic_variables` (list of string, optional) — Dynamic variable names used in the procedure content
- `folder_parent_id` (string, optional) — Procedure ID of the folder this procedure is placed in. None means root.

### FieldConflict

- `path` (string, required) — Identifier of the conflicting field relative to its section: a dot-path within conversation_config/platform_settings, or a procedure id.
- `section` (enum, required) — Which config section this path belongs to.
  - Allowed values: `conversation_config`, `platform_settings`, `procedures`, `workflow`
- `base_value` (any, optional) — Value at the common ancestor (merge base).
- `source_value` (any, optional) — Value on the source branch tip.
- `target_value` (any, optional) — Value on the target branch tip.

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

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

### EvaluationSettingsOutput

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

### AgentAnalysisItemsOutput

- `evaluation_criteria` (list of AgentAnalysisItemsOutputEvaluationCriteriaItem, optional)
- `data_collection` (list of AgentAnalysisItemsOutputDataCollectionItem, optional)

### ConversationInitiationClientDataConfigOutput

- `conversation_config_override` (ConversationConfigClientOverrideConfigOutput, optional) — Overrides for the conversation configuration
- `custom_llm_extra_body` (boolean, optional, default: false) — Whether to include custom LLM extra body
- `enable_conversation_initiation_client_data_from_webhook` (boolean, optional, default: false) — Whether to enable conversation initiation client data from webhooks
- `enable_starting_workflow_node_id_from_client` (boolean, optional, default: false) — Whether clients may pass starting_workflow_node_id in initiation client data; if false, sending it fails conversation start.
- `enable_procedure_ids_from_client` (boolean, optional, default: false) — Whether clients may pass procedure_ids in initiation client data to select which of the agent's procedures are available for the conversation; if false, sending it fails conversation start.

### AgentWorkspaceOverridesOutput

- `conversation_initiation_client_data_webhook` (ConversationInitiationClientDataWebhook, optional) — The webhook to send conversation initiation client data to
- `webhooks` (ConvAiWebhooks, optional)

### AgentTestingSettings

Settings for agent testing configuration.

- `attached_tests` (list of AttachedTestModel, optional) — List of test IDs that should be run for this agent

### GuardrailsV1Output

- `version` ("1", optional)
- `focus` (FocusGuardrail, optional)
- `prompt_injection` (PromptInjectionGuardrail, optional)
- `content` (ContentGuardrailOutput, optional)
- `custom` (CustomGuardrailOutput, optional) — Container for custom guardrails, matching ModerationGuardrail pattern

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

### PrivacyConfigOutput

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

### AlertingSettingsResponse

Customer-facing view of alerting settings. Unlike AdminAlertingSettingsResponse, it has no internal_notifiers field: those are ElevenLabs-internal delivery channels whose URLs must never be returned outside the admin API.

- `monitor_configs` (map from string to AlertingMonitorConfig, optional)
- `auto_resolve_after_inactive_minutes` (integer, optional)
- `notifiers` (list of AlertingSettingsResponseNotifiersItem, optional)

### SafetyResponseModel

- `is_blocked_ivc` (boolean, optional, default: false)
- `is_blocked_non_ivc` (boolean, optional, default: false)
- `ignore_safety_evaluation` (boolean, optional, default: false)

### PhoneNumberAgentInfo

- `agent_id` (string, required) — The ID of the agent
- `agent_name` (string, required) — The name of the agent
- `environment` (string, optional) — Environment to use for resolving environment variables on calls to this number.
- `branch_id` (string, optional) — Agent branch to use for calls to this number.

### GetPhoneNumberInboundSipTrunkConfigResponseModel

- `allowed_addresses` (list of string, required) — List of IP addresses that are allowed to use the trunk. Each item in the list can be an individual IP address or a Classless Inter-Domain Routing notation representing a CIDR block.
- `media_encryption` (enum, required, default: allowed)
  - Allowed values: `disabled`, `allowed`, `required`
- `has_auth_credentials` (boolean, required) — Whether authentication credentials are configured
- `allowed_numbers` (list of string, optional) — List of phone numbers that are allowed to use the trunk.
- `username` (string, optional) — SIP trunk username (if available)
- `remote_domains` (list of string, optional) — Domains of remote SIP servers used to validate TLS certificates.
- `attributes_to_headers` (map from string to string, optional) — Map of dynamic variable name to header name for attributes_to_headers

### GetPhoneNumberOutboundSipTrunkConfigResponseModel

SIP Trunk configuration details for a phone number

- `address` (string, required) — Hostname or IP the SIP INVITE is sent to
- `transport` (enum, required, default: auto) — Protocol to use for SIP transport
  - Allowed values: `auto`, `udp`, `tcp`, `tls`
- `media_encryption` (enum, required, default: allowed) — Whether or not to encrypt media (data layer).
  - Allowed values: `disabled`, `allowed`, `required`
- `has_auth_credentials` (boolean, required) — Whether authentication credentials are configured
- `headers` (map from string to string, optional) — SIP headers for INVITE request
- `attributes_to_headers` (map from string to string, optional) — Map of dynamic variable name to header name for attributes_to_headers
- `username` (string, optional) — SIP trunk username (if available)
- `has_outbound_trunk` (boolean, optional, default: false) — Whether a LiveKit SIP outbound trunk is configured
- `enabled_codecs` (list of enum, optional) — Media codecs that are offered in the SDP for outbound calls. If empty, all supported codecs are offered.
  - Allowed values: `G722/8000`, `PCMU/8000`, `PCMA/8000`

### WorkflowEdgeModelOutput

- `source` (string, required) — ID of the source node.
- `target` (string, required) — ID of the target node.
- `forward_condition` (WorkflowEdgeModelOutputForwardCondition, optional) — Condition that must be met for the edge to be traversed in the forward direction (source to target).
- `backward_condition` (WorkflowEdgeModelOutputBackwardCondition, optional) — Condition that must be met for the edge to be traversed in the backward direction (target to source).

### AgentWorkflowResponseModelNodesValue

- `type`: `end`
  - `edge_order` (list of string, required) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionOutput, required) — Position of the node in the workflow.
- `type`: `override_agent`
  - `additional_knowledge_base` (list of KnowledgeBaseLocator, required) — Additional knowledge base documents that the subagent has access to. These will be used in addition to the main agent's documents.
  - `additional_prompt` (string, required) — Specific goal for this subagent. It will be added to the system prompt and can be used to further refine the agent's behavior in this specific context.
  - `additional_tool_ids` (list of string, required) — IDs of additional tools that the subagent has access to. These will be used in addition to the main agent's tools.
  - `conversation_config` (ConversationalConfigApiModelWorkflowOverrideOutput, required) — Configuration overrides applied while the subagent is conducting the conversation.
  - `edge_order` (list of string, required) — The ids of outgoing edges in the order they should be evaluated.
  - `entry_behavior` (enum, required, default: auto) — Dictates whether this node should immediately generate a response upon entry or wait for the user input. When set to "auto", the behavior will be decided based on the type of the preceding node: "wait_for_user" after the "say" and "start" nodes and "generate_immediately" otherwise.
    - Allowed values: `generate_immediately`, `wait_for_user`, `auto`
  - `label` (string, required) — Human-readable label for the node used throughout the UI.
  - `position` (PositionOutput, required) — Position of the node in the workflow.
- `type`: `phone_number`
  - `custom_sip_headers` (list of WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem, required) — Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.
  - `edge_order` (list of string, required) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionOutput, required) — Position of the node in the workflow.
  - `sip_refer_play_dialtone` (boolean, required, default: true) — When True, a ringing tone is played on the original call leg while a SIP REFER transfer completes. The tone is carried over RTP to the SIP peer executing the REFER, so disable this if the receiving system (e.g. an SBC or contact center) should not hear it. When disabled the caller hears silence until the transfer completes. SIP REFER transfers only.
  - `transfer_destination` (WorkflowPhoneNumberNodeModelOutputTransferDestination, required)
  - `transfer_type` (enum, required, default: conference)
    - Allowed values: `blind`, `conference`, `sip_refer`
  - `post_dial_digits` (WorkflowPhoneNumberNodeModelOutputPostDialDigits, optional) — DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.
  - `uui` (UuiTransferConfig, optional) — User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.
- `type`: `standalone_agent`
  - `delay_ms` (integer, required, default: 0) — Artificial delay in milliseconds applied before transferring the conversation.
  - `edge_order` (list of string, required) — The ids of outgoing edges in the order they should be evaluated.
  - `enable_transferred_agent_first_message` (boolean, required, default: false) — Whether to enable the transferred agent to send its configured first message after the transfer.
  - `position` (PositionOutput, required) — Position of the node in the workflow.
  - `preserve_client_tts_overrides` (boolean, required, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.
  - `agent_id` (string, optional) — The ID of the agent to transfer the conversation to. None means transfer within the current agent.
  - `node_id` (string, optional) — Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node.
  - `transfer_message` (string, optional) — Optional message sent to the user before the transfer is initiated.
- `type`: `start`
  - `edge_order` (list of string, required) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionOutput, required) — Position of the node in the workflow.
- `type`: `tool`
  - `edge_order` (list of string, required) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionOutput, required) — Position of the node in the workflow.
  - `tools` (list of WorkflowToolLocator, required) — List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully.

### ValidationErrorLocItem

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

### AgentAnalysisItemsOutputEvaluationCriteriaItem

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

### AgentAnalysisItemsOutputDataCollectionItem

- `source`: `system`
  - `analysis_item_id` ("__system_data_collection_topic", required) — Id of the referenced built-in system data-collection item.
  - `scope` (enum, optional, default: conversation) — Transcript context ('conversation' or 'agent') used when running this item.
    - Allowed values: `conversation`, `agent`
- `source`: `user`
  - `analysis_item_id` (string, required) — Id of the referenced user data-collection item.
  - `scope` (enum, optional, default: conversation) — Transcript context ('conversation' or 'agent') used when running this item.
    - Allowed values: `conversation`, `agent`
  - `version_id` (string, optional) — Pinned item version. None tracks the item's latest published version.

### ConversationConfigClientOverrideConfigOutput

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

### ContentGuardrailOutput

- `execution_mode` (enum, optional, default: streaming)
  - Allowed values: `streaming`, `blocking`
- `config` (ContentConfig, optional)
- `trigger_action` (ContentGuardrailOutputTriggerAction, optional)

### CustomGuardrailOutput

Container for custom guardrails, matching ModerationGuardrail pattern

- `config` (CustomGuardrailsConfigOutput, optional) — Config container for custom guardrails list

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

### AlertingSettingsResponseNotifiersItem

- `type`: `webhook`
  - `webhook_id` (string, required)
- `type`: `integration`
  - `connection_id` (string, required)
  - `channel_id` (string, optional)
  - `integration_type` (enum, optional)
    - Allowed values: `pagerduty`, `slack`

### WorkflowEdgeModelOutputForwardCondition

- `type`: `expression`
  - `expression` (AstNodeOutput, required) — Expression to evaluate.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `llm`
  - `condition` (string, required) — Condition to evaluate
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `result`
  - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `unconditional`
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.

### WorkflowEdgeModelOutputBackwardCondition

- `type`: `expression`
  - `expression` (AstNodeOutput, required) — Expression to evaluate.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `llm`
  - `condition` (string, required) — Condition to evaluate
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `result`
  - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `unconditional`
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.

### PositionOutput

- `x` (double, required, default: 0)
- `y` (double, required, default: 0)

### KnowledgeBaseLocator

- `type` (enum, required) — The type of the knowledge base
  - Allowed values: `file`, `url`, `text`, `folder`
- `name` (string, required) — The name of the knowledge base
- `id` (string, required) — The ID of the knowledge base
- `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
  - Allowed values: `prompt`, `auto`

### ConversationalConfigApiModelWorkflowOverrideOutput

- `asr` (AsrConversationalConfigWorkflowOverride, optional) — Configuration for conversational transcription
- `turn` (TurnConfigWorkflowOverride, optional) — Configuration for turn detection
- `tts` (TtsConversationalConfigWorkflowOverrideOutput, optional) — Configuration for conversational text to speech
- `conversation` (ConversationConfigWorkflowOverrideOutput, optional) — Configuration for conversational events
- `language_presets` (map from string to LanguagePresetOutput, optional) — Language presets for conversations
- `vad` (VadConfigWorkflowOverride, optional) — Configuration for voice activity detection
- `agent` (AgentConfigApiModelWorkflowOverrideOutput, optional) — Agent specific configuration

### WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem

- `type`: `dynamic`
  - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
  - `value` (string, required) — The dynamic variable name to resolve
- `type`: `static`
  - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
  - `value` (string, required) — The header value

### WorkflowPhoneNumberNodeModelOutputTransferDestination

- `type`: `phone`
  - `phone_number` (string, required)
- `type`: `phone_dynamic_variable`
  - `phone_number` (string, required)
- `type`: `sip_uri`
  - `sip_uri` (string, required)
- `type`: `sip_uri_dynamic_variable`
  - `sip_uri` (string, required)

### WorkflowPhoneNumberNodeModelOutputPostDialDigits

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

### ContentGuardrailOutputTriggerAction

- `type`: `end_call`
- `type`: `retry`
  - `feedback` (string, optional, default: Your response was blocked by a guardrail that blocks content that matches this condition/category: '{{trigger_reason}}' During your next turn you must tell the user "I'm sorry but I can't answer that question, would you like to know something else?".) — Custom feedback to inject into the agent when retrying after guardrail trigger.

### CustomGuardrailsConfigOutput

Config container for custom guardrails list

- `configs` (list of CustomGuardrailConfig, optional)

### AstNodeOutput

- `type`: `add_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `and_operator`
  - `children` (list of AstNodeOutput, required) — Child nodes of the logical operator.
- `type`: `boolean_literal`
  - `value` (boolean, required) — Value of this literal.
- `type`: `conditional_operator`
  - `condition` (AstNodeOutput, required) — Condition deciding which expression should be selected.
  - `falseExpression` (AstNodeOutput, required) — Expression selected if the condition is false.
  - `trueExpression` (AstNodeOutput, required) — Expression selected if the condition is true.
- `type`: `div_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `dynamic_variable`
  - `name` (string, required) — The name of the dynamic variable.
- `type`: `eq_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `gt_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `gte_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `llm`
  - `value_schema` (LlmLiteralJsonSchemaProperty, required) — JSON schema describing the value that the LLM should extract.
  - `prompt` (string, required, deprecated) — The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead.
- `type`: `lt_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `lte_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `mul_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `neq_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.
- `type`: `null_literal`
- `type`: `number_literal`
  - `value` (AstNumberNodeOutputValue, required) — Value of this literal.
- `type`: `or_operator`
  - `children` (list of AstNodeOutput, required) — Child nodes of the logical operator.
- `type`: `string_literal`
  - `value` (string, required) — Value of this literal.
- `type`: `sub_operator`
  - `left` (AstNodeOutput, required) — Left operand of the binary operator.
  - `right` (AstNodeOutput, required) — Right operand of the binary operator.

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

### TtsConversationalConfigWorkflowOverrideOutput

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
- `audio_effects` (EffectsSpecOutput, optional) — Optional TTS effects spec: filter preset, distance (proximity EQ), and environment (convolution reverb).

### ConversationConfigWorkflowOverrideOutput

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

### VadConfigWorkflowOverride

### AgentConfigApiModelWorkflowOverrideOutput

- `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional) — Language of the agent - used for ASR and TTS
- `hinglish_mode` (boolean, optional) — When enabled and language is Hindi, the agent will respond in Hinglish
- `dynamic_variables` (DynamicVariablesConfigWorkflowOverride, optional) — Configuration for dynamic variables
- `disable_first_message_interruptions` (boolean, optional) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
- `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
- `text_behavior_overrides` (map from string to BehaviorOverride, optional) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
- `prompt` (PromptAgentApiModelWorkflowOverrideOutput, optional) — The prompt for the agent

### WorkflowToolLocatorSchemaOverridesValue

- `source`: `constant`
  - `constant_value` (ConstantSchemaOverrideConstantValue, optional) — The constant value to use
- `source`: `dynamic_variable`
  - `dynamic_variable` (string, required) — The name of the dynamic variable to use
- `source`: `llm`
  - `prompt` (string, optional) — Prompt override for the LLM. If not provided, the original schema description is used.
- `source`: `omit`

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

### AstNumberNodeOutputValue

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

### DynamicVariablesConfigWorkflowOverride

- `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values

### PromptAgentApiModelWorkflowOverrideOutput

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
- `built_in_tools` (BuiltInToolsWorkflowOverrideOutput, optional) — Built-in system tools to be used by the agent
- `enable_parallel_tool_calls` (boolean, optional) — Enable parallel tool calling. When enabled, the agent can execute multiple tools in parallel within a single turn. Not supported by all models.
- `mcp_server_ids` (list of string, optional) — A list of MCP server ids to be used by the agent
- `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional) — A list of knowledge bases to be used by the agent
- `custom_llm` (CustomLlm, optional) — Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
- `ignore_default_personality` (boolean, optional) — Whether to remove the default personality lines from the system prompt
- `rag` (RagConfigWorkflowOverrideOutput, optional) — Configuration for RAG
- `timezone` (string, optional) — Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references.
- `backup_llm_config` (PromptAgentApiModelWorkflowOverrideOutputBackupLlmConfig, optional) — Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.
- `cascade_timeout_seconds` (double, optional) — Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.
- `tools` (list of PromptAgentApiModelWorkflowOverrideOutputToolsItem, optional) — A list of tools that the agent can use over the course of the conversation, use tool_ids instead

### ConstantSchemaOverrideConstantValue

The constant value to use

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

### BuiltInToolsWorkflowOverrideOutput

- `transfer_to_agent` (SystemToolConfigOutput, optional) — The transfer to agent tool
- `end_call` (SystemToolConfigOutput, optional) — The end call tool
- `language_detection` (SystemToolConfigOutput, optional) — The language detection tool
- `transfer_to_number` (SystemToolConfigOutput, optional) — The transfer to number tool
- `skip_turn` (SystemToolConfigOutput, optional) — The skip turn tool
- `play_keypad_touch_tone` (SystemToolConfigOutput, optional) — The play DTMF tool
- `voicemail_detection` (SystemToolConfigOutput, optional) — The voicemail detection tool

### RagConfigWorkflowOverrideOutput

- `enabled` (boolean, optional)
- `embedding_model` (enum, optional, default: e5_mistral_7b_instruct)
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
- `max_vector_distance` (double, optional) — Maximum vector distance of retrieved chunks.
- `max_documents_length` (integer, optional) — Maximum total length of document chunks retrieved from RAG.
- `max_retrieved_rag_chunks_count` (integer, optional) — Maximum number of RAG document chunks to initially retrieve from the vector store. These are then further filtered by vector distance and total length.
- `num_candidates` (integer, optional) — Number of candidates evaluated in ANN vector search. Higher number means better results, but higher latency. Minimum recommended value is 100. If disabled, the default value is used.
- `query_rewrite_prompt_override` (string, optional) — Custom prompt for rewriting user queries before RAG retrieval. The conversation history will be automatically appended at the end. If not set, the default prompt will be used.
- `knowledge_base_tool_info` (KnowledgeBaseToolInfo, optional) — When set, the agent uses the knowledge_base tool instead of the legacy knowledge_base_rag tool. None means the agent is not opted in.

### PromptAgentApiModelWorkflowOverrideOutputBackupLlmConfig

Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.

### PromptAgentApiModelWorkflowOverrideOutputToolsItem

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

### BackupLlmDefault

- `preference` ("default", optional)

### BackupLlmDisabled

- `preference` ("disabled", optional)

### BackupLlmOverride

- `order` (list of enum, required)
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `preference` ("override", optional)

### ArrayJsonSchemaPropertyOutputItems

Schema for array elements.

## Examples

**Response**

```json
{
  "agent_id": "agent_7101k5zvyjhmfg983brhmhkd98n6",
  "name": "My Agent",
  "conversation_config": {
    "asr": {
      "quality": "high",
      "provider": "scribe_realtime",
      "user_input_audio_format": "pcm_16000",
      "keywords": [
        "hello",
        "world"
      ]
    },
    "turn": {
      "turn_timeout": 7,
      "initial_wait_time": 1.1,
      "silence_end_call_timeout": -1,
      "turn_eagerness": "normal",
      "spelling_patience": "auto",
      "speculative_turn": false,
      "retranscribe_on_turn_timeout": false,
      "turn_model": "turn_v3",
      "interruption_ignore_terms": [
        "interruption_ignore_terms"
      ],
      "interruption_ignore_term_languages": [
        "interruption_ignore_term_languages"
      ],
      "merge_with_default_ignore_terms": false,
      "transcribe_on_disabled_interruptions": false,
      "soft_timeout_config": {
        "timeout_seconds": -1,
        "message": "Hhmmmm...yeah."
      }
    },
    "tts": {
      "model_id": "eleven_turbo_v2",
      "voice_id": "cjVigY5qzO86Huf0OWal",
      "supported_voices": [
        {
          "label": "label",
          "voice_id": "voice_id"
        }
      ],
      "expressive_mode": true,
      "suggested_audio_tags": [
        {
          "tag": "tag"
        }
      ],
      "agent_output_audio_format": "pcm_16000",
      "optimize_streaming_latency": 3,
      "stability": 0.5,
      "speed": 1,
      "similarity_boost": 0.8,
      "text_normalisation_type": "system_prompt",
      "pronunciation_dictionary_locators": [
        {
          "pronunciation_dictionary_id": "pronunciation_dictionary_id",
          "version_id": null
        }
      ],
      "enable_phoneme_tags": true,
      "audio_effects": {
        "distance": 1.1,
        "send_level": 1.1,
        "filter_preset_id": null,
        "environment_id": null,
        "background_noise_id": null,
        "seed": null
      }
    },
    "conversation": {
      "text_only": true,
      "max_duration_seconds": 600,
      "client_events": [
        "audio",
        "interruption"
      ],
      "monitoring_enabled": true,
      "monitoring_events": [
        "conversation_initiation_metadata"
      ],
      "source_attribution": true
    },
    "language_presets": {
      "key": {
        "overrides": {
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
        }
      }
    },
    "agent": {
      "first_message": "Hello, how can I help you today?",
      "language": "en",
      "hinglish_mode": true,
      "disable_first_message_interruptions": false,
      "max_conversation_duration_message": "max_conversation_duration_message",
      "prompt": {
        "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
        "llm": "gemini-2.0-flash-001",
        "temperature": 0,
        "max_tokens": -1,
        "tool_ids": [
          "tool_ids"
        ],
        "built_in_tools": {
          "transfer_to_agent": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "end_call": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "language_detection": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "transfer_to_number": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "skip_turn": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "play_keypad_touch_tone": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "voicemail_detection": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          }
        },
        "knowledge_base": [
          {
            "type": "file",
            "name": "My Knowledge Base",
            "id": "123",
            "usage_mode": "auto"
          }
        ],
        "rag": {
          "max_vector_distance": 0.5,
          "max_retrieved_rag_chunks_count": 5
        }
      }
    }
  },
  "metadata": {
    "created_at_unix_secs": 1,
    "updated_at_unix_secs": 1
  },
  "platform_settings": {
    "evaluation": {
      "criteria": [
        {
          "id": "criterion_binary_001",
          "name": "Issue resolved",
          "conversation_goal_prompt": "Determine whether the agent fully resolved the user's issue.",
          "use_knowledge_base": false,
          "scope": "conversation",
          "scoring_mode": "binary",
          "max_score": 100
        }
      ]
    },
    "widget": {
      "variant": "tiny",
      "placement": "top-left",
      "expandable": "never",
      "avatar": {
        "type": "orb",
        "color_1": "#2792dc",
        "color_2": "#9ce6e6"
      },
      "feedback_mode": "none",
      "bg_color": "bg_color",
      "text_color": "text_color",
      "btn_color": "btn_color",
      "btn_text_color": "btn_text_color",
      "border_color": "border_color",
      "focus_color": "focus_color",
      "border_radius": 1,
      "btn_radius": 1,
      "action_text": "action_text",
      "start_call_text": "start_call_text",
      "end_call_text": "end_call_text",
      "expand_text": "expand_text",
      "listening_text": "listening_text",
      "speaking_text": "speaking_text",
      "shareable_page_text": "shareable_page_text",
      "shareable_page_show_terms": true,
      "terms_text": "terms_text",
      "terms_html": "terms_html",
      "terms_key": "terms_key",
      "show_avatar_when_collapsed": true,
      "disable_banner": true,
      "override_link": "override_link",
      "markdown_link_allowed_hosts": [
        {
          "hostname": "hostname"
        }
      ],
      "markdown_link_include_www": true,
      "markdown_link_allow_http": true,
      "mic_muting_enabled": true,
      "transcript_enabled": true,
      "text_input_enabled": true,
      "conversation_mode_toggle_enabled": true,
      "default_expanded": true,
      "always_expanded": true,
      "dismissible": true,
      "show_agent_status": true,
      "show_conversation_id": true,
      "strip_audio_tags": true,
      "syntax_highlight_theme": "light",
      "show_resize_button": true,
      "language_selector": false,
      "supports_text_only": true,
      "custom_avatar_path": "https://example.com/avatar.png",
      "language_presets": {
        "key": {}
      }
    },
    "data_collection": {
      "key": {
        "type": "string",
        "description": "My property",
        "is_system_provided": false,
        "dynamic_variable": "",
        "constant_value": ""
      }
    },
    "data_collection_scopes": {
      "key": "conversation"
    },
    "analysis_items": {
      "evaluation_criteria": [
        {
          "source": "system",
          "analysis_item_id": "__system_eval_criteria_sentiment"
        }
      ],
      "data_collection": [
        {
          "source": "system",
          "analysis_item_id": "__system_data_collection_topic"
        }
      ]
    },
    "overrides": {
      "custom_llm_extra_body": true,
      "enable_conversation_initiation_client_data_from_webhook": true,
      "enable_starting_workflow_node_id_from_client": true,
      "enable_procedure_ids_from_client": true
    },
    "workspace_overrides": {
      "conversation_initiation_client_data_webhook": {
        "url": "https://example.com/webhook",
        "request_headers": {
          "Content-Type": "application/json"
        }
      }
    },
    "testing": {
      "attached_tests": [
        {
          "test_id": "test_123",
          "workflow_node_id": "node_abc"
        },
        {
          "test_id": "test_456"
        }
      ]
    },
    "archived": true,
    "guardrails": {
      "version": "1"
    },
    "summary_language": "summary_language",
    "auto_translate_transcript_to_app_language": true,
    "auth": {
      "enable_auth": true,
      "allowlist": [
        {
          "hostname": "https://example.com"
        }
      ],
      "require_origin_header": true,
      "shareable_token": "1234567890"
    },
    "call_limits": {
      "agent_concurrency_limit": -1,
      "daily_limit": 100000,
      "bursting_enabled": true
    },
    "queueing_config": {
      "enabled": true,
      "wait_timeout_seconds": 1,
      "hold_audio": {
        "audio_path": "audio_path",
        "audio_url": "audio_url",
        "original_filename": "original_filename",
        "duration_secs": 1.1,
        "size_bytes": 1
      }
    },
    "privacy": {
      "record_voice": true,
      "retention_days": -1,
      "delete_transcript_and_pii": false,
      "delete_audio": false,
      "apply_to_existing_conversations": false,
      "zero_retention_mode": false
    },
    "trust_context": "unknown",
    "analysis_llm": "gpt-4o-mini",
    "alerting": {
      "monitor_configs": {
        "key": {}
      },
      "auto_resolve_after_inactive_minutes": 1,
      "notifiers": [
        {
          "type": "webhook",
          "webhook_id": "webhook_id"
        }
      ]
    },
    "safety": {
      "is_blocked_ivc": true,
      "is_blocked_non_ivc": true,
      "ignore_safety_evaluation": true
    }
  },
  "phone_numbers": [
    {
      "provider": "exotel",
      "label": "Exotel Outbound",
      "phone_number": "+919999999999",
      "phone_number_id": "phnum_X3Pbu5gP6NNKBscdCdwB",
      "assigned_agent": {
        "agent_id": "F3Pbu5gP6NNKBscdCdwB",
        "agent_name": "My Agent"
      }
    }
  ],
  "whatsapp_accounts": [
    {
      "business_account_id": "business_account_id",
      "phone_number_id": "phone_number_id",
      "business_account_name": "business_account_name",
      "phone_number_name": "phone_number_name",
      "phone_number": "phone_number",
      "account_type": "cloud_api",
      "assigned_agent_id": "assigned_agent_id",
      "enable_messaging": true,
      "enable_audio_message_response": true,
      "enable_typing_indicator": true,
      "assigned_agent_name": "assigned_agent_name",
      "is_token_expired": true
    }
  ],
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "type": "llm",
          "condition": "User's last message contains a question about our pricing.",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {
          "type": "unconditional",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "type": "result",
          "successful": true,
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "type": "result",
          "successful": true,
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {
          "type": "unconditional",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "type": "llm",
          "condition": "User's last message contains a question about our pricing.",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_b_to_end": {
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": {
          "type": "llm",
          "condition": "User's last message contains a question about our pricing.",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_b_to_phone": {
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      }
    },
    "nodes": {
      "entry_node": {
        "type": "override_agent",
        "additional_knowledge_base": [
          {
            "type": "file",
            "name": "My Knowledge Base",
            "id": "123",
            "usage_mode": "auto"
          }
        ],
        "additional_prompt": "additional_prompt",
        "additional_tool_ids": [
          "additional_tool_ids"
        ],
        "conversation_config": {
          "asr": {
            "quality": "high",
            "provider": "scribe_realtime",
            "user_input_audio_format": "pcm_16000",
            "keywords": [
              "hello",
              "world"
            ]
          },
          "turn": {
            "turn_timeout": 7,
            "silence_end_call_timeout": -1,
            "turn_eagerness": "normal",
            "spelling_patience": "auto",
            "speculative_turn": false,
            "retranscribe_on_turn_timeout": false,
            "turn_model": "turn_v3",
            "interruption_ignore_terms": [
              "interruption_ignore_terms"
            ],
            "interruption_ignore_term_languages": [
              "interruption_ignore_term_languages"
            ],
            "merge_with_default_ignore_terms": false,
            "transcribe_on_disabled_interruptions": false,
            "soft_timeout_config": {
              "timeout_seconds": -1,
              "message": "Hhmmmm...yeah.",
              "use_llm_generated_message": false
            }
          },
          "tts": {
            "model_id": "eleven_turbo_v2",
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "agent_output_audio_format": "pcm_16000",
            "optimize_streaming_latency": 3,
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
            "max_duration_seconds": 600,
            "client_events": [
              "audio",
              "interruption"
            ]
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "dynamic_variables": {
              "dynamic_variable_placeholders": {
                "user_name": "John Doe"
              }
            },
            "disable_first_message_interruptions": false,
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "temperature": 0,
              "max_tokens": -1,
              "tool_ids": [
                "tool_ids"
              ],
              "built_in_tools": {
                "transfer_to_agent": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "end_call": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "language_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_number": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "skip_turn": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "play_keypad_touch_tone": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "voicemail_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                }
              },
              "knowledge_base": [
                {
                  "type": "file",
                  "name": "My Knowledge Base",
                  "id": "123",
                  "usage_mode": "auto"
                }
              ],
              "tools": [
                {
                  "type": "api_integration_webhook",
                  "api_integration_connection_id": "api_integration_connection_id",
                  "api_integration_id": "api_integration_id",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ],
                  "description": "description",
                  "dynamic_variables": {
                    "dynamic_variable_placeholders": {
                      "user_name": "John Doe"
                    }
                  },
                  "execution_mode": "immediate",
                  "interruption_mode": "allow",
                  "name": "name",
                  "pre_tool_speech": "auto",
                  "response_timeout_secs": 1,
                  "tool_call_sound_behavior": "auto",
                  "tool_error_handling_mode": "auto",
                  "tool_version": "tool_version",
                  "disable_interruptions": true,
                  "force_pre_tool_speech": true,
                  "api_schema_overrides": null,
                  "tool_call_sound": null
                }
              ]
            }
          }
        },
        "edge_order": [
          "edge_order"
        ],
        "entry_behavior": "generate_immediately",
        "label": "label",
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "failure_node": {
        "type": "override_agent",
        "additional_knowledge_base": [
          {
            "type": "file",
            "name": "My Knowledge Base",
            "id": "123",
            "usage_mode": "auto"
          }
        ],
        "additional_prompt": "additional_prompt",
        "additional_tool_ids": [
          "additional_tool_ids"
        ],
        "conversation_config": {
          "asr": {
            "quality": "high",
            "provider": "scribe_realtime",
            "user_input_audio_format": "pcm_16000",
            "keywords": [
              "hello",
              "world"
            ]
          },
          "turn": {
            "turn_timeout": 7,
            "silence_end_call_timeout": -1,
            "turn_eagerness": "normal",
            "spelling_patience": "auto",
            "speculative_turn": false,
            "retranscribe_on_turn_timeout": false,
            "turn_model": "turn_v3",
            "interruption_ignore_terms": [
              "interruption_ignore_terms"
            ],
            "interruption_ignore_term_languages": [
              "interruption_ignore_term_languages"
            ],
            "merge_with_default_ignore_terms": false,
            "transcribe_on_disabled_interruptions": false,
            "soft_timeout_config": {
              "timeout_seconds": -1,
              "message": "Hhmmmm...yeah.",
              "use_llm_generated_message": false
            }
          },
          "tts": {
            "model_id": "eleven_turbo_v2",
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "agent_output_audio_format": "pcm_16000",
            "optimize_streaming_latency": 3,
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
            "max_duration_seconds": 600,
            "client_events": [
              "audio",
              "interruption"
            ]
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "dynamic_variables": {
              "dynamic_variable_placeholders": {
                "user_name": "John Doe"
              }
            },
            "disable_first_message_interruptions": false,
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "temperature": 0,
              "max_tokens": -1,
              "tool_ids": [
                "tool_ids"
              ],
              "built_in_tools": {
                "transfer_to_agent": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "end_call": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "language_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_number": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "skip_turn": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "play_keypad_touch_tone": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "voicemail_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                }
              },
              "knowledge_base": [
                {
                  "type": "file",
                  "name": "My Knowledge Base",
                  "id": "123",
                  "usage_mode": "auto"
                }
              ],
              "tools": [
                {
                  "type": "api_integration_webhook",
                  "api_integration_connection_id": "api_integration_connection_id",
                  "api_integration_id": "api_integration_id",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ],
                  "description": "description",
                  "dynamic_variables": {
                    "dynamic_variable_placeholders": {
                      "user_name": "John Doe"
                    }
                  },
                  "execution_mode": "immediate",
                  "interruption_mode": "allow",
                  "name": "name",
                  "pre_tool_speech": "auto",
                  "response_timeout_secs": 1,
                  "tool_call_sound_behavior": "auto",
                  "tool_error_handling_mode": "auto",
                  "tool_version": "tool_version",
                  "disable_interruptions": true,
                  "force_pre_tool_speech": true,
                  "api_schema_overrides": null,
                  "tool_call_sound": null
                }
              ]
            }
          }
        },
        "edge_order": [
          "edge_order"
        ],
        "entry_behavior": "generate_immediately",
        "label": "label",
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "start_node": {
        "type": "start",
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "success_conversation": {
        "type": "override_agent",
        "additional_knowledge_base": [
          {
            "type": "file",
            "name": "My Knowledge Base",
            "id": "123",
            "usage_mode": "auto"
          }
        ],
        "additional_prompt": "additional_prompt",
        "additional_tool_ids": [
          "additional_tool_ids"
        ],
        "conversation_config": {
          "asr": {
            "quality": "high",
            "provider": "scribe_realtime",
            "user_input_audio_format": "pcm_16000",
            "keywords": [
              "hello",
              "world"
            ]
          },
          "turn": {
            "turn_timeout": 7,
            "silence_end_call_timeout": -1,
            "turn_eagerness": "normal",
            "spelling_patience": "auto",
            "speculative_turn": false,
            "retranscribe_on_turn_timeout": false,
            "turn_model": "turn_v3",
            "interruption_ignore_terms": [
              "interruption_ignore_terms"
            ],
            "interruption_ignore_term_languages": [
              "interruption_ignore_term_languages"
            ],
            "merge_with_default_ignore_terms": false,
            "transcribe_on_disabled_interruptions": false,
            "soft_timeout_config": {
              "timeout_seconds": -1,
              "message": "Hhmmmm...yeah.",
              "use_llm_generated_message": false
            }
          },
          "tts": {
            "model_id": "eleven_turbo_v2",
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "agent_output_audio_format": "pcm_16000",
            "optimize_streaming_latency": 3,
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
            "max_duration_seconds": 600,
            "client_events": [
              "audio",
              "interruption"
            ]
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "dynamic_variables": {
              "dynamic_variable_placeholders": {
                "user_name": "John Doe"
              }
            },
            "disable_first_message_interruptions": false,
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "temperature": 0,
              "max_tokens": -1,
              "tool_ids": [
                "tool_ids"
              ],
              "built_in_tools": {
                "transfer_to_agent": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "end_call": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "language_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_number": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "skip_turn": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "play_keypad_touch_tone": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "voicemail_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                }
              },
              "knowledge_base": [
                {
                  "type": "file",
                  "name": "My Knowledge Base",
                  "id": "123",
                  "usage_mode": "auto"
                }
              ],
              "tools": [
                {
                  "type": "api_integration_webhook",
                  "api_integration_connection_id": "api_integration_connection_id",
                  "api_integration_id": "api_integration_id",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ],
                  "description": "description",
                  "dynamic_variables": {
                    "dynamic_variable_placeholders": {
                      "user_name": "John Doe"
                    }
                  },
                  "execution_mode": "immediate",
                  "interruption_mode": "allow",
                  "name": "name",
                  "pre_tool_speech": "auto",
                  "response_timeout_secs": 1,
                  "tool_call_sound_behavior": "auto",
                  "tool_error_handling_mode": "auto",
                  "tool_version": "tool_version",
                  "disable_interruptions": true,
                  "force_pre_tool_speech": true,
                  "api_schema_overrides": null,
                  "tool_call_sound": null
                }
              ]
            }
          }
        },
        "edge_order": [
          "edge_order"
        ],
        "entry_behavior": "generate_immediately",
        "label": "label",
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "success_end": {
        "type": "end",
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "success_phone": {
        "type": "phone_number",
        "custom_sip_headers": [
          {
            "type": "dynamic",
            "key": "key",
            "value": "value"
          }
        ],
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        },
        "sip_refer_play_dialtone": true,
        "transfer_destination": {
          "type": "phone",
          "phone_number": "phone_number"
        },
        "transfer_type": "blind",
        "post_dial_digits": null,
        "uui": null
      },
      "success_transfer": {
        "type": "standalone_agent",
        "delay_ms": 1,
        "edge_order": [
          "edge_order"
        ],
        "enable_transferred_agent_first_message": true,
        "position": {
          "x": 1.1,
          "y": 1.1
        },
        "preserve_client_tts_overrides": true,
        "agent_id": null,
        "node_id": null,
        "transfer_message": null
      },
      "tool_node_a": {
        "type": "tool",
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        },
        "tools": [
          {
            "tool_id": "tool_id"
          }
        ]
      },
      "tool_node_b": {
        "type": "tool",
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        },
        "tools": [
          {
            "tool_id": "tool_id"
          }
        ]
      }
    },
    "prevent_subagent_loops": false
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "anonymous_access_level_override": "admin",
    "access_source": "creator"
  },
  "tags": [
    "tags"
  ],
  "version_id": "version_id",
  "branch_id": "branch_id",
  "main_branch_id": "main_branch_id",
  "procedures": {
    "key": {
      "procedure_id": "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
      "version_id": "agtprcv_7rbqxer9o12cyxi55ckw6sgz1dl4",
      "name": "Customer Support Procedure",
      "type": "free_form",
      "trigger": "When the customer asks for support",
      "referenced_tool_ids": [
        "tool_123"
      ],
      "referenced_kb_ids": [
        "kb_123"
      ],
      "referenced_procedure_ids": [
        "agtprc_other"
      ],
      "referenced_dynamic_variables": [
        "customer_id"
      ],
      "folder_parent_id": "folder_parent_id"
    }
  },
  "default_hold_audio_url": "default_hold_audio_url",
  "overridden_fields": [
    "overridden_fields"
  ],
  "conflicts": [
    {
      "path": "path",
      "section": "conversation_config",
      "base_value": {
        "key": "value"
      },
      "source_value": {
        "key": "value"
      },
      "target_value": {
        "key": "value"
      }
    }
  ],
  "source_identical_to_target": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.previewRebase("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtbrch_8901k4t9z5defmb8vh3e9361y7nj");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.preview_rebase(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview")! as URL,
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
