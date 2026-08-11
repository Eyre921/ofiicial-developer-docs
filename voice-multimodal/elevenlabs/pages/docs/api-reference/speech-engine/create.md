---
title: "Create Speech Engine"
source: https://elevenlabs.io/docs/api-reference/speech-engine/create.md
path: docs/api-reference/speech-engine/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Speech Engine

POST https://api.elevenlabs.io/v1/speech-engine
Content-Type: application/json

Create a new Speech Engine resource

Reference: https://elevenlabs.io/docs/api-reference/speech-engine/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `speech_engine` (object, required) — Speech engine WebSocket configuration
  - `ws_url` (string, required) — The WebSocket URL for the transcript server
  - `request_headers` (map from string to string or object or object, optional) — Headers to include in the WebSocket connection request
    - ConvAISecretLocator
      - `secret_id` (string, required)
    - ConvAIDynamicVariable
      - `variable_name` (string, required)
- `name` (string, optional, default: Speech Engine) — Name of the speech engine
- `asr` (object, optional) — ASR configuration
  - `quality` (enum, optional, default: high) — The quality of the transcription
    - Allowed values: `high`
  - `provider` (enum, optional, default: scribe_realtime) — The provider of the transcription service
    - Allowed values: `elevenlabs`, `scribe_realtime`
  - `user_input_audio_format` (enum, optional, default: pcm_16000) — The format of the audio to be transcribed
    - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
  - `keywords` (list of string, optional) — Keywords to boost prediction probability for
- `tts` (object, optional) — TTS configuration
  - `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
    - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
  - `voice_id` (string, optional, default: cjVigY5qzO86Huf0OWal) — The voice ID to use for TTS
  - `supported_voices` (list of object, optional) — Additional supported voices for the agent
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
  - `expressive_mode` (boolean, optional, default: true) — When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.
  - `suggested_audio_tags` (list of object, optional) — Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.
    - `tag` (string, required) — Audio tag to use (for best performance, 1-2 words, e.g., 'happy', 'excited')
    - `description` (string, optional, nullable) — Optional description of when to use this tag
  - `agent_output_audio_format` (enum, optional, default: pcm_16000) — The audio format to use for TTS
    - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
  - `optimize_streaming_latency` (enum, optional) — Deprecated: this field is a no-op and is ignored.
    - Allowed values: `0`, `1`, `2`, `3`, `4`
  - `stability` (double, optional, default: 0.5) — The stability of generated speech
  - `speed` (double, optional, default: 1) — The speed of generated speech
  - `similarity_boost` (double, optional, default: 0.8) — The similarity boost for generated speech
  - `text_normalisation_type` (enum, optional, default: system_prompt) — Method for converting numbers to words before converting text to speech. If set to SYSTEM_PROMPT, the system prompt will be updated to include normalization instructions. If set to ELEVENLABS, the text will be normalized after generation, incurring slight additional latency.
    - Allowed values: `system_prompt`, `elevenlabs`
  - `pronunciation_dictionary_locators` (list of object, optional) — The pronunciation dictionary locators
    - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
    - `version_id` (string, required, nullable) — The ID of the version of the pronunciation dictionary
  - `enable_phoneme_tags` (boolean, optional, default: true) — Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.
- `turn` (object, optional) — Turn detection configuration
  - `turn_timeout` (double, optional, default: 7) — Maximum wait time for the user's reply before re-engaging the user
  - `initial_wait_time` (double, optional, nullable) — How long the agent will wait for the user to start the conversation if the first message is empty. If not set, uses the regular turn_timeout.
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
  - `transcribe_on_disabled_interruptions` (boolean, optional, default: false) — When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.
- `vad` (object, optional) — Configuration for voice activity detection
- `conversation` (object, optional) — Conversation configuration (client events, etc.)
  - `text_only` (boolean, optional, default: false) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
  - `max_duration_seconds` (integer, optional, default: 600) — The maximum duration of a conversation in seconds
  - `client_events` (list of enum, optional) — The events that will be sent to the client
    - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `internal_turn_probability`, `internal_tentative_agent_response`
  - `file_input` (object, optional) — Configuration for file input (image/PDF uploads) during conversations.
    - `enabled` (boolean, optional, default: true) — When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.
    - `max_files_in_memory` (integer, optional, default: 10) — Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.
    - `max_files_per_conversation` (integer, optional, default: 10) — Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.
  - `monitoring_enabled` (boolean, optional, default: false) — Enable real-time monitoring of conversations via WebSocket
  - `monitoring_events` (list of enum, optional) — The events that will be sent to monitoring connections.
    - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `internal_turn_probability`, `internal_tentative_agent_response`
  - `background_sound` (object, optional) — Configuration for background sound during conversations.
    - `source_type` (enum, optional, nullable) — The type of background sound source.
      - Allowed values: `preset`
    - `source_id` (enum, optional, nullable) — Identifier for the sound source.
      - Allowed values: `office2`, `office1`, `restaurant`, `city`, `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
    - `volume` (double, optional, default: 0.15) — Volume level for background sound (0.01 to 1.0).
    - `crossfade_loop` (boolean, optional, default: true) — Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.
  - `source_attribution` (boolean, optional, default: false) — When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.
- `privacy` (object, optional) — Privacy settings (recording, retention, zero retention mode)
  - `record_voice` (boolean, optional, default: true) — Whether to record the conversation
  - `retention_days` (integer, optional, default: -1) — The number of days to retain the conversation. -1 indicates there is no retention limit
  - `delete_transcript_and_pii` (boolean, optional, default: false) — Whether to delete the transcript and PII
  - `delete_audio` (boolean, optional, default: false) — Whether to delete the audio
  - `apply_to_existing_conversations` (boolean, optional, default: false) — Whether to apply the privacy settings to existing conversations
  - `zero_retention_mode` (boolean, optional, default: false) — Whether to enable zero retention mode - no PII data is stored
  - `conversation_history_redaction` (object, optional) — Config for PII redaction in the conversation history
    - `enabled` (boolean, optional, default: false) — Whether conversation history redaction is enabled
    - `entities` (list of enum, optional) — The entities to redact from the conversation transcript, audio and analysis. Use top-level types like 'name', 'email_address', or dot notation for specific subtypes like 'name.full_name'.
      - Allowed values: `name`, `name.name_given`, `name.name_family`, `name.name_other`, `email_address`, `contact_number`, `dob`, `age`, `religious_belief`, `political_opinion`, `sexual_orientation`, `ethnicity_race`, `marital_status`, `occupation`, `physical_attribute`, `language`, `username`, `password`, `url`, `organization`, `financial_id`, `financial_id.payment_card`, `financial_id.payment_card.payment_card_number`, `financial_id.payment_card.payment_card_expiration_date`, `financial_id.payment_card.payment_card_cvv`, `financial_id.bank_account`, `financial_id.bank_account.bank_account_number`, `financial_id.bank_account.bank_routing_number`, `financial_id.bank_account.swift_bic_code`, `financial_id.financial_id_other`, `location`, `location.location_address`, `location.location_city`, `location.location_postal_code`, `location.location_coordinate`, `location.location_state`, `location.location_country`, `location.location_other`, `date`, `date_interval`, `unique_id`, `unique_id.government_issued_id`, `unique_id.account_number`, `unique_id.vehicle_id`, `unique_id.healthcare_number`, `unique_id.healthcare_number.medical_record_number`, `unique_id.healthcare_number.health_plan_beneficiary_number`, `unique_id.device_id`, `unique_id.unique_id_other`, `medical`, `medical.medical_condition`, `medical.medication`, `medical.medical_procedure`, `medical.medical_measurement`, `medical.medical_other`
- `call_limits` (object, optional) — Concurrency and daily conversation limits for this speech engine
  - `agent_concurrency_limit` (integer, optional, default: -1) — The maximum number of concurrent conversations. -1 indicates that there is no maximum
  - `daily_limit` (integer, optional, default: 100000) — The maximum number of conversations per day
  - `bursting_enabled` (boolean, optional, default: true) — Whether to enable bursting. If true, exceeding workspace concurrency limit will be allowed up to 3 times the limit. Calls will be charged at double rate when exceeding the limit.
- `language` (string, optional, default: en) — Language for the speech engine
- `tags` (list of string, optional) — Tags for categorization
- `overrides` (object, optional) — Override settings the client may set during conversation initiation
  - `first_message` (boolean, optional, default: false) — Whether the first message can be overridden by the client

## Response

### 201

Successful Response

- `speech_engine_id` (string, required) — The speech engine resource ID
- `name` (string, required) — Human-readable name for the speech engine
- `speech_engine` (object, required) — WebSocket connection settings for the upstream transcript server
  - `ws_url` (string, required) — The WebSocket URL for the transcript server
  - `request_headers` (map from string to string or object or object, optional) — Headers to include in the WebSocket connection request
    - ConvAISecretLocator
      - `secret_id` (string, required)
    - ConvAIDynamicVariable
      - `variable_name` (string, required)
- `asr` (object, required) — Automatic speech recognition configuration
  - `quality` (enum, optional, default: high) — The quality of the transcription
    - Allowed values: `high`
  - `provider` (enum, optional, default: scribe_realtime) — The provider of the transcription service
    - Allowed values: `elevenlabs`, `scribe_realtime`
  - `user_input_audio_format` (enum, optional, default: pcm_16000) — The format of the audio to be transcribed
    - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
  - `keywords` (list of string, optional) — Keywords to boost prediction probability for
- `tts` (object, required) — Text-to-speech output configuration
  - `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
    - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
  - `voice_id` (string, optional, default: cjVigY5qzO86Huf0OWal) — The voice ID to use for TTS
  - `supported_voices` (list of object, optional) — Additional supported voices for the agent
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
  - `expressive_mode` (boolean, optional, default: true) — When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.
  - `suggested_audio_tags` (list of object, optional) — Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.
    - `tag` (string, required) — Audio tag to use (for best performance, 1-2 words, e.g., 'happy', 'excited')
    - `description` (string, optional, nullable) — Optional description of when to use this tag
  - `agent_output_audio_format` (enum, optional, default: pcm_16000) — The audio format to use for TTS
    - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
  - `optimize_streaming_latency` (enum, optional) — Deprecated: this field is a no-op and is ignored.
    - Allowed values: `0`, `1`, `2`, `3`, `4`
  - `stability` (double, optional, default: 0.5) — The stability of generated speech
  - `speed` (double, optional, default: 1) — The speed of generated speech
  - `similarity_boost` (double, optional, default: 0.8) — The similarity boost for generated speech
  - `text_normalisation_type` (enum, optional, default: system_prompt) — Method for converting numbers to words before converting text to speech. If set to SYSTEM_PROMPT, the system prompt will be updated to include normalization instructions. If set to ELEVENLABS, the text will be normalized after generation, incurring slight additional latency.
    - Allowed values: `system_prompt`, `elevenlabs`
  - `pronunciation_dictionary_locators` (list of object, optional) — The pronunciation dictionary locators
    - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
    - `version_id` (string, required, nullable) — The ID of the version of the pronunciation dictionary
  - `enable_phoneme_tags` (boolean, optional, default: true) — Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.
- `turn` (object, required) — Turn detection configuration
  - `turn_timeout` (double, optional, default: 7) — Maximum wait time for the user's reply before re-engaging the user
  - `initial_wait_time` (double, optional, nullable) — How long the agent will wait for the user to start the conversation if the first message is empty. If not set, uses the regular turn_timeout.
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
  - `transcribe_on_disabled_interruptions` (boolean, optional, default: false) — When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.
- `vad` (object, required) — Configuration for voice activity detection
- `conversation` (object, required) — Conversation-level settings including client events and duration limits
  - `text_only` (boolean, optional, default: false) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
  - `max_duration_seconds` (integer, optional, default: 600) — The maximum duration of a conversation in seconds
  - `client_events` (list of enum, optional) — The events that will be sent to the client
    - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `internal_turn_probability`, `internal_tentative_agent_response`
  - `file_input` (object, optional) — Configuration for file input (image/PDF uploads) during conversations.
    - `enabled` (boolean, optional, default: true) — When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.
    - `max_files_in_memory` (integer, optional, default: 10) — Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.
    - `max_files_per_conversation` (integer, optional, default: 10) — Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.
  - `monitoring_enabled` (boolean, optional, default: false) — Enable real-time monitoring of conversations via WebSocket
  - `monitoring_events` (list of enum, optional) — The events that will be sent to monitoring connections.
    - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `internal_turn_probability`, `internal_tentative_agent_response`
  - `background_sound` (object, optional) — Configuration for background sound during conversations.
    - `source_type` (enum, optional, nullable) — The type of background sound source.
      - Allowed values: `preset`
    - `source_id` (enum, optional, nullable) — Identifier for the sound source.
      - Allowed values: `office2`, `office1`, `restaurant`, `city`, `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
    - `volume` (double, optional, default: 0.15) — Volume level for background sound (0.01 to 1.0).
    - `crossfade_loop` (boolean, optional, default: true) — Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.
  - `source_attribution` (boolean, optional, default: false) — When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.
- `privacy` (object, required) — Privacy settings controlling recording, retention, and PII handling
  - `record_voice` (boolean, optional, default: true) — Whether to record the conversation
  - `retention_days` (integer, optional, default: -1) — The number of days to retain the conversation. -1 indicates there is no retention limit
  - `delete_transcript_and_pii` (boolean, optional, default: false) — Whether to delete the transcript and PII
  - `delete_audio` (boolean, optional, default: false) — Whether to delete the audio
  - `apply_to_existing_conversations` (boolean, optional, default: false) — Whether to apply the privacy settings to existing conversations
  - `zero_retention_mode` (boolean, optional, default: false) — Whether to enable zero retention mode - no PII data is stored
  - `conversation_history_redaction` (object, optional) — Config for PII redaction in the conversation history
    - `enabled` (boolean, optional, default: false) — Whether conversation history redaction is enabled
    - `entities` (list of enum, optional) — The entities to redact from the conversation transcript, audio and analysis. Use top-level types like 'name', 'email_address', or dot notation for specific subtypes like 'name.full_name'.
      - Allowed values: `name`, `name.name_given`, `name.name_family`, `name.name_other`, `email_address`, `contact_number`, `dob`, `age`, `religious_belief`, `political_opinion`, `sexual_orientation`, `ethnicity_race`, `marital_status`, `occupation`, `physical_attribute`, `language`, `username`, `password`, `url`, `organization`, `financial_id`, `financial_id.payment_card`, `financial_id.payment_card.payment_card_number`, `financial_id.payment_card.payment_card_expiration_date`, `financial_id.payment_card.payment_card_cvv`, `financial_id.bank_account`, `financial_id.bank_account.bank_account_number`, `financial_id.bank_account.bank_routing_number`, `financial_id.bank_account.swift_bic_code`, `financial_id.financial_id_other`, `location`, `location.location_address`, `location.location_city`, `location.location_postal_code`, `location.location_coordinate`, `location.location_state`, `location.location_country`, `location.location_other`, `date`, `date_interval`, `unique_id`, `unique_id.government_issued_id`, `unique_id.account_number`, `unique_id.vehicle_id`, `unique_id.healthcare_number`, `unique_id.healthcare_number.medical_record_number`, `unique_id.healthcare_number.health_plan_beneficiary_number`, `unique_id.device_id`, `unique_id.unique_id_other`, `medical`, `medical.medical_condition`, `medical.medication`, `medical.medical_procedure`, `medical.medical_measurement`, `medical.medical_other`
- `call_limits` (object, required) — Concurrency and daily conversation limits for this speech engine
  - `agent_concurrency_limit` (integer, optional, default: -1) — The maximum number of concurrent conversations. -1 indicates that there is no maximum
  - `daily_limit` (integer, optional, default: 100000) — The maximum number of conversations per day
  - `bursting_enabled` (boolean, optional, default: true) — Whether to enable bursting. If true, exceeding workspace concurrency limit will be allowed up to 3 times the limit. Calls will be charged at double rate when exceeding the limit.
- `language` (string, required) — ISO language code used by the speech engine (e.g. 'en')
- `tags` (list of string, required) — Arbitrary tags for categorization and filtering
- `overrides` (object, required) — Override settings the client may set during conversation initiation
  - `first_message` (boolean, optional, default: false) — Whether the first message can be overridden by the client
- `metadata` (object, required) — Creation and update timestamps with source information
  - `created_at_unix_secs` (integer, required)
  - `updated_at_unix_secs` (integer, required)
  - `created_from` (enum, optional, default: unknown)
    - Allowed values: `cli`, `ui`, `api`, `template`, `unknown`
  - `last_updated_from` (enum, optional, default: unknown)
    - Allowed values: `cli`, `ui`, `api`, `template`, `unknown`
- `access_info` (object, optional, nullable) — The access information of the speech engine for the user
  - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
  - `creator_name` (string, required) — Name of the agent's creator
  - `creator_email` (string, required) — Email of the agent's creator
  - `role` (enum, required) — The role of the user making the request
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
    - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`

## Examples

**Request**

```json
{
  "speech_engine": {
    "ws_url": "string"
  }
}
```

**Response**

```json
{
  "speech_engine_id": "seng_3701k3ttaq12ewp8b7qv5rfyszkz",
  "name": "My Speech Engine",
  "speech_engine": {
    "ws_url": "wss://example.com/transcript",
    "request_headers": {}
  },
  "asr": {
    "quality": "high",
    "provider": "elevenlabs",
    "user_input_audio_format": "pcm_16000",
    "keywords": []
  },
  "tts": {
    "model_id": "eleven_flash_v2",
    "voice_id": "cjVigY5qzO86Huf0OWal",
    "agent_output_audio_format": "pcm_16000",
    "optimize_streaming_latency": 3,
    "stability": 0.5,
    "speed": 1,
    "similarity_boost": 0.8
  },
  "turn": {
    "turn_timeout": 7,
    "silence_end_call_timeout": -1,
    "turn_eagerness": "normal",
    "mode": "turn"
  },
  "vad": {
    "background_voice_detection": false
  },
  "conversation": {
    "max_duration_seconds": 600,
    "client_events": [
      "audio",
      "interruption",
      "agent_response",
      "user_transcript"
    ]
  },
  "privacy": {
    "record_voice": true,
    "retention_days": -1,
    "delete_transcript_and_pii": false,
    "delete_audio": false,
    "apply_to_existing_conversations": false,
    "zero_retention_mode": false
  },
  "call_limits": {
    "agent_concurrency_limit": -1,
    "daily_limit": 100000,
    "bursting_enabled": true
  },
  "language": "en",
  "tags": [
    "production",
    "v1"
  ],
  "overrides": {
    "first_message": false
  },
  "metadata": {
    "created_at_unix_secs": 1714000000,
    "updated_at_unix_secs": 1714000000,
    "created_from": "api",
    "last_updated_from": "api"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.speechEngine.create({
        speechEngine: {
            wsUrl: "string",
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, SpeechEngineConfig

client = ElevenLabs()

client.speech_engine.create(
    speech_engine=SpeechEngineConfig(
        ws_url="string",
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

	url := "https://api.elevenlabs.io/v1/speech-engine"

	payload := strings.NewReader("{\n  \"speech_engine\": {\n    \"ws_url\": \"string\"\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/speech-engine")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"speech_engine\": {\n    \"ws_url\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-engine")
  .header("Content-Type", "application/json")
  .body("{\n  \"speech_engine\": {\n    \"ws_url\": \"string\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-engine', [
  'body' => '{
  "speech_engine": {
    "ws_url": "string"
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

var client = new RestClient("https://api.elevenlabs.io/v1/speech-engine");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"speech_engine\": {\n    \"ws_url\": \"string\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["speech_engine": ["ws_url": "string"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-engine")! as URL,
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
