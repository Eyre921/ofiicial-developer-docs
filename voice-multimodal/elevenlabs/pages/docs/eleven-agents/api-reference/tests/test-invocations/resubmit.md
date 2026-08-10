---
title: "Resubmit test invocation"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-invocations/resubmit.md
path: docs/eleven-agents/api-reference/tests/test-invocations/resubmit
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Resubmit test invocation

POST https://api.elevenlabs.io/v1/convai/test-invocations/{test_invocation_id}/resubmit
Content-Type: application/json

Resubmits specific test runs from a test invocation.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-invocations/resubmit

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `test_invocation_id` (string, required) — The id of a test invocation. This is returned when tests are run.

### Body (application/json)

- `test_run_ids` (list of string, required) — List of test run IDs to resubmit
- `agent_id` (string, required) — Agent ID to resubmit tests for
- `agent_config_override` (object, optional) — Configuration overrides to use for testing. If not provided, the agent's default configuration will be used.
  - `conversation_config` (object, required)
    - `asr` (object, optional) — Configuration for conversational transcription
      - `quality` ("high", optional) — The quality of the transcription
      - `provider` (enum, optional, default: scribe_realtime) — The provider of the transcription service
        - Allowed values: `elevenlabs`, `scribe_realtime`
      - `user_input_audio_format` (enum, optional, default: pcm_16000) — The format of the audio to be transcribed
        - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
      - `keywords` (list of string, optional) — Keywords to boost prediction probability for
    - `turn` (object, optional) — Configuration for turn detection
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
      - `transcribe_on_disabled_interruptions` (boolean, optional, default: false) — When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.
      - `soft_timeout_config` (object, optional) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
        - `timeout_seconds` (double, optional, default: -1) — Time in seconds before showing the predefined message while waiting for LLM response. Set to -1 to disable.
        - `message` (string, optional, default: Hhmmmm...yeah.) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
        - `additional_soft_timeout_messages` (list of string, optional) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.
        - `use_llm_generated_message` (boolean, optional, default: false) — If enabled, the soft timeout message will be generated dynamically instead of using the static message.
        - `randomize_fillers` (boolean, optional, default: false) — If enabled, shuffle the order of static soft timeout messages once at the start of each turn. Only applies when use_llm_generated_message is false.
        - `max_soft_timeouts_per_generation` (integer, optional, default: 1) — Maximum filler messages while waiting for a single LLM response. Fires every timeout_seconds until the LLM streams content or this limit is reached.
        - `llm_generated_message_prompt_override` (string, optional) — Custom prompt for generating the soft timeout filler message when use\_llm\_generated\_message is enabled. Recent conversation context is provided as a separate user message. If not set, the default prompt will be used. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
    - `tts` (object, optional) — Configuration for conversational text to speech
      - `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
        - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
      - `voice_id` (string, optional, default: cjVigY5qzO86Huf0OWal) — The voice ID to use for TTS
      - `supported_voices` (list of object, optional) — Additional supported voices for the agent
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
      - `expressive_mode` (boolean, optional, default: true) — When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.
      - `suggested_audio_tags` (list of object, optional) — Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.
        - `tag` (string, required) — Audio tag to use (for best performance, 1-2 words, e.g., 'happy', 'excited')
        - `description` (string, optional) — Optional description of when to use this tag
      - `agent_output_audio_format` (enum, optional, default: pcm_16000) — The audio format to use for TTS
        - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
      - `optimize_streaming_latency` (integer, optional) — Deprecated: this field is a no-op and is ignored.
      - `stability` (double, optional, default: 0.5) — The stability of generated speech
      - `speed` (double, optional, default: 1) — The speed of generated speech
      - `similarity_boost` (double, optional, default: 0.8) — The similarity boost for generated speech
      - `text_normalisation_type` (enum, optional, default: system_prompt) — Method for converting numbers to words before converting text to speech. If set to SYSTEM_PROMPT, the system prompt will be updated to include normalization instructions. If set to ELEVENLABS, the text will be normalized after generation, incurring slight additional latency.
        - Allowed values: `system_prompt`, `elevenlabs`
      - `pronunciation_dictionary_locators` (list of object, optional) — The pronunciation dictionary locators
        - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
        - `version_id` (string, optional) — The ID of the version of the pronunciation dictionary
      - `enable_phoneme_tags` (boolean, optional, default: true) — Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.
    - `conversation` (object, optional) — Configuration for conversational events
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
        - `source_type` ("preset", optional) — The type of background sound source.
        - `source_id` (enum, optional) — Identifier for the sound source.
          - Allowed values: `office2`, `office1`, `restaurant`, `city`, `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
        - `volume` (double, optional, default: 0.6) — Volume level for background sound (0.01 to 1.0).
        - `crossfade_loop` (boolean, optional, default: false) — Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.
      - `source_attribution` (boolean, optional, default: false) — When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.
    - `language_presets` (map from string to object, optional) — Language presets for conversations
      - `overrides` (object, required) — The overrides for the language preset
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
            - `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
            - `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
            - `knowledge_base` (list of object, optional) — A list of knowledge bases to be used by the agent
      - `first_message_translation` (object, optional) — The translation of the first message
        - `source_hash` (string, required)
        - `text` (string, required)
      - `soft_timeout_translation` (object, optional) — The translation of the soft timeout message
        - `source_hash` (string, required)
        - `text` (string, required)
    - `vad` (object, optional) — Configuration for voice activity detection
    - `agent` (object, optional) — Agent specific configuration
      - `first_message` (string, optional, default: ) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
      - `language` (string, optional, default: en) — Language of the agent - used for ASR and TTS
      - `hinglish_mode` (boolean, optional, default: false) — When enabled and language is Hindi, the agent will respond in Hinglish
      - `dynamic_variables` (any, optional)
      - `disable_first_message_interruptions` (boolean, optional, default: false) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
      - `max_conversation_duration_message` (string, optional, default: ) — If non-empty, the message the agent will send when max conversation duration is reached.
      - `text_behavior_overrides` (map from string to object, optional) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
        - `verbosity` (enum, optional) — Verbosity override. Underlying default applies when unset.
          - Allowed values: `auto`, `concise`, `thorough`
        - `output_format` (enum, optional) — Output format override. Underlying default applies when unset.
          - Allowed values: `mp3_22050_32`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `ulaw_8000`
        - `interaction_budget` (enum, optional) — Interaction budget override. Underlying default applies when unset.
          - Allowed values: `realtime`, `5_minutes`, `10_minutes`, `1_hour`
      - `prompt` (object, optional) — The prompt for the agent
        - `prompt` (string, optional, default: ) — The prompt for the agent
        - `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
          - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
        - `reasoning_effort` (enum, optional) — Reasoning effort of the model. Only available for some models.
          - Allowed values: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`
        - `thinking_budget` (integer, optional) — Max number of tokens used for thinking. Use 0 to turn off if supported by the model.
        - `enable_reasoning_summary` (boolean, optional, default: false) — Enable model reasoning summaries. When disabled, we do not request summaries from provider if possible for faster TTFB. Not ZRM compatible.
        - `temperature` (double, optional) — The temperature for the LLM. Defaults to 0. Set to null to omit the parameter from the LLM request entirely (useful for custom LLMs that reject the temperature field).
        - `max_tokens` (integer, optional, default: -1) — If greater than 0, maximum number of tokens the LLM can predict
        - `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
        - `built_in_tools` (object, optional) — Built-in system tools to be used by the agent
          - `end_call` (object, optional) — The end call tool
            - `name` (string, required)
            - `params` (object, required)
            - `type` ("system", optional) — The type of tool
            - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
          - `language_detection` (object, optional) — The language detection tool
            - `name` (string, required)
            - `params` (object, required)
            - `type` ("system", optional) — The type of tool
            - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
          - `transfer_to_agent` (object, optional) — The transfer to agent tool
            - `name` (string, required)
            - `params` (object, required)
            - `type` ("system", optional) — The type of tool
            - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
          - `transfer_to_number` (object, optional) — The transfer to number tool
            - `name` (string, required)
            - `params` (object, required)
            - `type` ("system", optional) — The type of tool
            - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
          - `skip_turn` (object, optional) — The skip turn tool
            - `name` (string, required)
            - `params` (object, required)
            - `type` ("system", optional) — The type of tool
            - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
          - `play_keypad_touch_tone` (object, optional) — The play DTMF tool
            - `name` (string, required)
            - `params` (object, required)
            - `type` ("system", optional) — The type of tool
            - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
          - `voicemail_detection` (object, optional) — The voicemail detection tool
            - `name` (string, required)
            - `params` (object, required)
            - `type` ("system", optional) — The type of tool
            - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
        - `mcp_server_ids` (list of string, optional) — A list of MCP server ids to be used by the agent
        - `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
        - `knowledge_base` (list of object, optional) — A list of knowledge bases to be used by the agent
          - `type` (enum, required) — The type of the knowledge base
            - Allowed values: `file`, `url`, `text`, `folder`
          - `name` (string, required) — The name of the knowledge base
          - `id` (string, required) — The ID of the knowledge base
          - `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
            - Allowed values: `prompt`, `auto`
        - `custom_llm` (object, optional) — Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
          - `url` (string, required) — The URL of the Chat Completions compatible endpoint
          - `model_id` (string, optional) — The model ID to be used if URL serves multiple models
          - `api_key` (object or object, optional) — The API key for authentication. Either a workspace secret reference \{'secret\_id': '...'} or an environment variable reference \{'env\_var\_label': '...'}.
            - Conv AI Secret Locator
            - Conv AI Env Var Locator
          - `auth_connection` (object or object, optional) — Optional workspace auth connection for authentication. Only auth connections that produce an Authorization Bearer token are supported; Basic auth, mTLS, custom header, and URL secret auth connections are not supported.
            - Auth Connection Locator
            - Environment Auth Connection Locator
          - `request_headers` (map from string to string or object or object or object, optional) — Headers that should be included in the request
            - Conv AI Secret Locator
            - Conv AI Dynamic Variable
            - Conv AI Env Var Locator
          - `api_version` (string, optional) — The API version to use for the request
          - `api_type` (enum, optional, default: chat_completions) — The API type to use (chat_completions, responses or websocket)
            - Allowed values: `chat_completions`, `responses`, `websocket`
        - `ignore_default_personality` (boolean, optional) — Whether to remove the default personality lines from the system prompt
        - `rag` (object, optional) — Configuration for RAG
          - `enabled` (boolean, optional, default: false)
          - `embedding_model` (enum, optional, default: e5_mistral_7b_instruct)
            - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
          - `max_vector_distance` (double, optional, default: 0.6) — Maximum vector distance of retrieved chunks.
          - `max_documents_length` (integer, optional, default: 50000) — Maximum total length of document chunks retrieved from RAG.
          - `max_retrieved_rag_chunks_count` (integer, optional, default: 20) — Maximum number of RAG document chunks to initially retrieve from the vector store. These are then further filtered by vector distance and total length.
          - `num_candidates` (integer, optional) — Number of candidates evaluated in ANN vector search. Higher number means better results, but higher latency. Minimum recommended value is 100. If disabled, the default value is used.
          - `query_rewrite_prompt_override` (string, optional) — Custom prompt for rewriting user queries before RAG retrieval. The conversation history will be automatically appended at the end. If not set, the default prompt will be used.
        - `timezone` (string, optional) — Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references.
        - `backup_llm_config` (object, optional) — Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.
          - `preference`: `default`
          - `preference`: `disabled`
          - `preference`: `override`
            - `order` (list of enum, required)
        - `cascade_timeout_seconds` (double, optional, default: 4) — Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.
        - `tools` (list of object, optional, deprecated) — A list of tools that the agent can use over the course of the conversation, use tool_ids instead
          - `type`: `api_integration_webhook`
            - `api_integration_connection_id` (string, required)
            - `api_integration_id` (string, required)
            - `assignments` (list of object, required) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `description` (string, required) — Description of when the tool should be used and what it does.
            - `dynamic_variables` (object, required) — Configuration for dynamic variables
            - `execution_mode` (enum, required, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
            - `interruption_mode` (enum, required, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `name` (string, required)
            - `pre_tool_speech` (enum, required, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `response_timeout_secs` (integer, required, default: 20) — The maximum time in seconds to wait for the tool call to complete. Must be between 5 and 300 seconds (inclusive).
            - `tool_call_sound_behavior` (enum, required, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, required, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `tool_version` (string, required, default: 1.0.0) — The version of the API integration tool
            - `disable_interruptions` (boolean, required, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, required, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
            - `api_schema_overrides` (object, optional) — User overrides applied on top of the base api_schema
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
          - `type`: `client`
            - `description` (string, required) — Description of when the tool should be used and what it does.
            - `name` (string, required)
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variables` (object, optional) — Configuration for dynamic variables
            - `execution_mode` (enum, optional, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
            - `expects_response` (boolean, optional, default: false) — If true, calling this tool should block the conversation until the client responds with some response which is passed to the llm. If false then we will continue the conversation without waiting for the client to respond, this is useful to show content to a user but not block the conversation
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `parameters` (object, optional) — Schema for any parameters to pass to the client
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete. Must be between 1 and 120 seconds (inclusive).
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
          - `type`: `mcp`
            - `value` (any, required)
          - `type`: `smb`
            - `value` (any, required)
          - `type`: `system`
            - `name` (string, required)
            - `params` (object, required)
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
          - `type`: `webhook`
            - `api_schema` (object, required) — The schema for the outgoing webhoook, including parameters and URL specification
            - `description` (string, required) — Description of when the tool should be used and what it does.
            - `name` (string, required)
            - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variables` (object, optional) — Configuration for dynamic variables
            - `execution_mode` (enum, optional, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
            - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete. Must be between 5 and 300 seconds (inclusive).
            - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
            - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
  - `platform_settings` (object, required)
    - `evaluation` (object, optional) — Settings for evaluation
      - `criteria` (list of object, optional) — Individual criteria that the agent should be evaluated against
        - `id` (string, required) — The unique identifier for the evaluation criteria
        - `name` (string, required)
        - `conversation_goal_prompt` (string, required) — The prompt that the agent should use to evaluate the conversation
        - `type` ("prompt", optional) — The type of evaluation criteria
        - `use_knowledge_base` (boolean, optional, default: false) — When evaluating the prompt, should the agent's knowledge base be used.
        - `scope` (enum, optional, default: conversation) — The scope of transcript context used when evaluating this criterion. 'conversation' uses the full transcript; 'agent' uses only the portion where the defining agent was active.
          - Allowed values: `conversation`, `agent`
        - `llm` (enum, optional) — LLM model to use for this evaluation criteria. If not set, uses agent's analysis_llm default.
          - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
        - `scoring_mode` (enum, optional, default: binary) — How this criterion is scored. 'binary' resolves to success/failure/unknown. 'numeric_uniform' returns a number on the [0, max_score] scale which is normalized into the aggregate conversation success percentage.
          - Allowed values: `binary`, `numeric_uniform`
        - `max_score` (integer, optional, default: 100) — Maximum value of the numeric score scale (minimum is always 0). Only used when scoring_mode is 'numeric_uniform'.
        - `score_instructions` (string, optional) — Optional free-text instructions describing how to assign values on the numeric scale. Only used when scoring_mode is 'numeric_uniform'.
    - `widget` (object, optional) — Configuration for the widget
      - `variant` (enum, optional, default: full) — The variant of the widget
        - Allowed values: `tiny`, `compact`, `full`, `expandable`
      - `placement` (enum, optional, default: bottom-right) — The placement of the widget on the screen
        - Allowed values: `top-left`, `top`, `top-right`, `bottom-left`, `bottom`, `bottom-right`
      - `expandable` (enum, optional, default: never) — Whether the widget is expandable
        - Allowed values: `never`, `mobile`, `desktop`, `always`
      - `avatar` (object, optional) — The avatar of the widget
        - `type`: `orb`
          - `color_1` (string, optional, default: #2792dc) — The first color of the avatar
          - `color_2` (string, optional, default: #9ce6e6) — The second color of the avatar
        - `type`: `url`
          - `custom_url` (string, optional, default: ) — The custom URL of the avatar
        - `type`: `image`
          - `url` (string, optional, default: ) — The URL of the avatar
      - `feedback_mode` (enum, optional, default: none) — The feedback mode of the widget
        - Allowed values: `none`, `during`, `end`
      - `end_feedback` (object, optional) — Configuration for feedback collected at the end of the conversation
        - `type` ("rating", optional) — The type of feedback to collect at the end of the conversation
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
      - `markdown_link_allowed_hosts` (list of object, optional) — List of allowed hostnames for clickable markdown links. Use \{ hostname: '\*' } to allow any domain. Empty means no links are allowed.
        - `hostname` (string, required) — The hostname of the allowed origin
      - `markdown_link_include_www` (boolean, optional, default: true) — Whether to automatically include www. variants of allowed hosts
      - `markdown_link_allow_http` (boolean, optional, default: true) — Whether to allow http:// in addition to https:// for allowed hosts
      - `mic_muting_enabled` (boolean, optional, default: false) — Whether to enable mic muting
      - `transcript_enabled` (boolean, optional, default: false) — Whether the widget should show the conversation transcript as it goes on
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
      - `text_contents` (object, optional) — Text contents of the widget
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
      - `styles` (object, optional) — Styles for the widget
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
      - `show_resize_button` (boolean, optional, default: true) — Whether to show the resize button
      - `language_selector` (boolean, optional, default: false) — Whether to show the language selector
      - `supports_text_only` (boolean, optional, default: true) — Whether the widget can switch to text only mode
      - `custom_avatar_path` (string, optional) — The custom avatar path
      - `language_presets` (map from string to object, optional) — Language presets for the widget
        - `text_contents` (object, optional) — The text contents for the selected language
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
        - `text_contents_translation` (object, optional) — The translation cache for the text contents
          - `source` (map from string to string, optional) — The source text each translated field was derived from
          - `text` (map from string to string, optional) — The last auto-translated output for each translated field
        - `terms_text` (string, optional) — The text to display for terms and conditions in this language
        - `terms_html` (string, optional) — The HTML to display for terms and conditions in this language
        - `terms_key` (string, optional) — The key to display for terms and conditions in this language
        - `terms_translation` (object, optional) — The translation cache for the terms
          - `source_hash` (string, required)
          - `text` (string, required)
    - `data_collection` (map from string to object, optional) — Data collection settings
      - `type` (enum, required)
        - Allowed values: `boolean`, `string`, `integer`, `number`
      - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `enum` (list of string, optional) — List of allowed string values for string type parameters
      - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
      - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
      - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
      - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
      - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
      - `llm` (enum, optional) — LLM model to use for this analysis item. If not set, uses agent's analysis_llm default.
        - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
    - `data_collection_scopes` (map from string to enum, optional) — Scope per data collection item ID. Missing keys default to conversation scope.
      - Allowed values: `conversation`, `agent`
    - `analysis_items` (object, optional) — Evaluation + data-collection items attached by reference. None means the agent has not been migrated onto analysis items yet (distinct from an empty, migrated set); reads fall back to the legacy evaluation/data_collection fields in that case.
      - `evaluation_criteria` (list of object, optional)
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
      - `data_collection` (list of object, optional)
        - `source`: `system`
          - `analysis_item_id` ("__system_data_collection_topic", required) — Id of the referenced built-in system data-collection item.
          - `scope` (enum, optional, default: conversation) — Transcript context ('conversation' or 'agent') used when running this item.
            - Allowed values: `conversation`, `agent`
        - `source`: `user`
          - `analysis_item_id` (string, required) — Id of the referenced user data-collection item.
          - `scope` (enum, optional, default: conversation) — Transcript context ('conversation' or 'agent') used when running this item.
            - Allowed values: `conversation`, `agent`
          - `version_id` (string, optional) — Pinned item version. None tracks the item's latest published version.
    - `overrides` (object, optional) — Additional overrides for the agent during conversation initiation
      - `conversation_config_override` (object, optional) — Overrides for the conversation configuration
        - `asr` (object, optional) — Configures overrides for nested fields.
          - `keywords` (boolean, optional, default: false) — Whether to allow overriding the keywords field.
        - `turn` (object, optional) — Configures overrides for nested fields.
          - `soft_timeout_config` (object, optional) — Configures overrides for nested fields.
            - `message` (boolean, optional, default: false) — Whether to allow overriding the message field.
        - `tts` (object, optional) — Configures overrides for nested fields.
          - `model_id` (boolean, optional, default: false) — Whether to allow overriding the model_id field.
          - `voice_id` (boolean, optional, default: false) — Whether to allow overriding the voice_id field.
          - `stability` (boolean, optional, default: false) — Whether to allow overriding the stability field.
          - `speed` (boolean, optional, default: false) — Whether to allow overriding the speed field.
          - `similarity_boost` (boolean, optional, default: false) — Whether to allow overriding the similarity_boost field.
          - `pronunciation_dictionary_locators` (boolean, optional, default: false) — Whether to allow overriding the pronunciation_dictionary_locators field.
        - `conversation` (object, optional) — Configures overrides for nested fields.
          - `text_only` (boolean, optional, default: false) — Whether to allow overriding the text_only field.
          - `max_duration_seconds` (boolean, optional, default: false) — Whether to allow overriding the max_duration_seconds field.
        - `agent` (object, optional) — Configures overrides for nested fields.
          - `first_message` (boolean, optional, default: false) — Whether to allow overriding the first_message field.
          - `language` (boolean, optional, default: false) — Whether to allow overriding the language field.
          - `max_conversation_duration_message` (boolean, optional, default: false) — Whether to allow overriding the max_conversation_duration_message field.
          - `prompt` (object, optional) — Configures overrides for nested fields.
            - `prompt` (boolean, optional, default: false) — Whether to allow overriding the prompt field.
            - `llm` (boolean, optional, default: false) — Whether to allow overriding the llm field.
            - `tool_ids` (boolean, optional, default: false) — Whether to allow overriding the tool_ids field.
            - `native_mcp_server_ids` (boolean, optional, default: false) — Whether to allow overriding the native_mcp_server_ids field.
            - `knowledge_base` (boolean, optional, default: false) — Whether to allow overriding the knowledge_base field.
      - `custom_llm_extra_body` (boolean, optional, default: false) — Whether to include custom LLM extra body
      - `enable_conversation_initiation_client_data_from_webhook` (boolean, optional, default: false) — Whether to enable conversation initiation client data from webhooks
      - `enable_starting_workflow_node_id_from_client` (boolean, optional, default: false) — Whether clients may pass starting_workflow_node_id in initiation client data; if false, sending it fails conversation start.
    - `workspace_overrides` (object, optional) — Workspace overrides for the agent
      - `conversation_initiation_client_data_webhook` (object, optional) — The webhook to send conversation initiation client data to
        - `url` (string, required) — The URL to send the webhook to
        - `request_headers` (map from string to string or object, required) — The headers to send with the webhook request
          - Conv AI Secret Locator
            - `secret_id` (string, required)
      - `webhooks` (object, optional)
        - `post_call_webhook_id` (string, optional)
        - `events` (list of enum, optional) — List of event types to send via webhook. Options: transcript, audio, call_initiation_failure, unredacted_transcript, unredacted_audio.
          - Allowed values: `transcript`, `audio`, `call_initiation_failure`, `unredacted_transcript`, `unredacted_audio`
        - `transcript_format` (enum, optional, default: json) — Format for transcript webhooks.
          - Allowed values: `json`, `opentelemetry`
        - `send_audio` (boolean, optional, deprecated) — DEPRECATED: Use 'events' field instead. Whether to send audio data with post-call webhooks for ConvAI conversations
    - `testing` (object, optional) — Testing configuration for the agent
      - `attached_tests` (list of object, optional) — List of test IDs that should be run for this agent
        - `test_id` (string, required)
        - `workflow_node_id` (string, optional)
    - `archived` (boolean, optional, default: false) — Whether the agent is archived
    - `guardrails` (object, optional) — Guardrails configuration for the agent
      - `version` ("1", optional)
      - `focus` (object, optional)
        - `is_enabled` (boolean, optional, default: false)
      - `prompt_injection` (object, optional)
        - `is_enabled` (boolean, optional, default: false)
      - `content` (object, optional)
        - `execution_mode` (enum, optional, default: streaming)
          - Allowed values: `streaming`, `blocking`
        - `config` (object, optional)
          - `sexual` (object, optional)
            - `is_enabled` (boolean, optional, default: false)
            - `threshold` (double or "low" or "medium" or "high", optional)
          - `violence` (object, optional)
            - `is_enabled` (boolean, optional, default: false)
            - `threshold` (double or "low" or "medium" or "high", optional)
          - `harassment` (object, optional)
            - `is_enabled` (boolean, optional, default: false)
            - `threshold` (double or "low" or "medium" or "high", optional)
          - `self_harm` (object, optional)
            - `is_enabled` (boolean, optional, default: false)
            - `threshold` (double or "low" or "medium" or "high", optional)
          - `profanity` (object, optional)
            - `is_enabled` (boolean, optional, default: false)
            - `threshold` (double or "low" or "medium" or "high", optional)
          - `religion_or_politics` (object, optional)
            - `is_enabled` (boolean, optional, default: false)
            - `threshold` (double or "low" or "medium" or "high", optional)
          - `medical_and_legal_information` (object, optional)
            - `is_enabled` (boolean, optional, default: false)
            - `threshold` (double or "low" or "medium" or "high", optional)
        - `trigger_action` (object, optional)
          - `type`: `end_call`
          - `type`: `retry`
            - `feedback` (string, optional, default: Your response was blocked by a guardrail that blocks content that matches this condition/category: '{{trigger_reason}}' During your next turn you must tell the user "I'm sorry but I can't answer that question, would you like to know something else?".) — Custom feedback to inject into the agent when retrying after guardrail trigger.
      - `custom` (object, optional) — Container for custom guardrails, matching ModerationGuardrail pattern
        - `config` (object, optional) — Config container for custom guardrails list
          - `configs` (list of object, optional)
            - `name` (string, required) — User-facing name for this guardrail
            - `prompt` (string, required) — Instruction describing what to block, e.g. 'don't talk about politics'
            - `is_enabled` (boolean, optional, default: false)
            - `execution_mode` (enum, optional, default: streaming)
            - `model` (enum, optional, default: gemini-3.1-flash-lite) — LLM model to use for custom guardrail evaluation
            - `history_message_count` (integer, optional, default: 0) — How much recent history the guardrail sees before the reply it evaluates, counted in user messages (the agent replies between them are included too). The guardrail always gets a single \<conversation\_history> transcript ending in the evaluated reply, marked 'AGENT \[current reply]:'. 0 (default) adds no prior history (just that line); 1 adds the latest user message onward.
            - `trigger_action` (object, optional)
            - `evaluate_full_response_only` (boolean, optional, default: false) — Evaluate once against the complete non-TTS response instead of cumulative partials. Requires blocking mode.
    - `summary_language` (string, optional) — Language for all conversation analysis outputs (summaries, titles, evaluation rationales, data collection rationales). If not set, the language will be inferred from the conversation. Must be one of the supported conversation languages.
    - `auto_translate_transcript_to_app_language` (boolean, optional) — When enabled, a conversation transcript is automatically translated to the viewer's application language when they open the transcript page. If not set or false, transcripts are shown in their original language unless the viewer manually selects a translation.
    - `auth` (object, optional) — Settings for authentication
      - `enable_auth` (boolean, optional, default: false) — If set to true, starting a conversation with an agent will require a signed token
      - `allowlist` (list of object, optional) — A list of hosts that are allowed to start conversations with the agent
        - `hostname` (string, required) — The hostname of the allowed origin
      - `require_origin_header` (boolean, optional, default: false) — When enabled, connections with no origin header will be rejected. If the allowlist is empty, this option has no effect.
      - `shareable_token` (string, optional) — A shareable token that can be used to start a conversation with the agent
    - `call_limits` (object, optional) — Call limits for the agent
      - `agent_concurrency_limit` (integer, optional, default: -1) — The maximum number of concurrent conversations. -1 indicates that there is no maximum
      - `daily_limit` (integer, optional, default: 100000) — The maximum number of conversations per day
      - `bursting_enabled` (boolean, optional, default: true) — Whether to enable bursting. If true, exceeding workspace concurrency limit will be allowed up to 3 times the limit. Calls will be charged at double rate when exceeding the limit.
    - `privacy` (object, optional) — Privacy settings for the agent
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
    - `trust_context` (enum, optional, default: unknown) — The trust context in which the agent operates.
      - Allowed values: `unknown`, `low`, `high`
    - `analysis_llm` (enum, optional) — Default LLM model for post-call analysis (evaluation and data collection)
      - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
    - `topic_discovery` (object, optional) — Per-agent topic discovery configuration
    - `sentiment_analysis` (object, optional) — Per-agent post-call sentiment analysis configuration
    - `alerting` (object, optional) — Agent-level alerting configuration overriding workspace settings.
      - `monitor_configs` (map from string to object, optional) — Alerting configuration keyed by monitor name.
        - `threshold` (double, optional) — Failure rate threshold at which this monitor can notify.
        - `auto_resolve_after_inactive_minutes` (integer, optional) — How many minutes an alert can stay inactive before it is auto-resolved.
      - `auto_resolve_after_inactive_minutes` (integer, optional) — How many minutes an alert can stay inactive before it is auto-resolved. Unset values fall through to the next layer.
      - `notifiers` (list of object, optional) — Delivery channels for alert lifecycle notifications. Stacked and deduped by webhook_id with other layers.
        - `webhook_id` (string, required) — ID of the workspace webhook to deliver alert lifecycle notifications to.
        - `type` ("webhook", optional)
  - `workflow` (object, optional)
    - `edges` (map from string to object, optional)
      - `source` (string, required) — ID of the source node.
      - `target` (string, required) — ID of the target node.
      - `forward_condition` (object, optional) — Condition that must be met for the edge to be traversed in the forward direction (source to target).
        - `type`: `expression`
          - `expression` (object, required) — Expression to evaluate.
            - `type`: `add_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `and_operator`
              - `children` (list of object, required) — Child nodes of the logical operator.
            - `type`: `boolean_literal`
              - `value` (boolean, required) — Value of this literal.
            - `type`: `conditional_operator`
              - `condition` (object, required) — Condition deciding which expression should be selected.
              - `falseExpression` (object, required) — Expression selected if the condition is false.
              - `trueExpression` (object, required) — Expression selected if the condition is true.
            - `type`: `div_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `dynamic_variable`
              - `name` (string, required) — The name of the dynamic variable.
            - `type`: `eq_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `gt_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `gte_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `llm`
              - `value_schema` (object, optional) — JSON schema describing the value that the LLM should extract.
              - `prompt` (string, optional, deprecated) — The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead.
            - `type`: `lt_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `lte_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `mul_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `neq_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `null_literal`
            - `type`: `number_literal`
              - `value` (double or integer, required) — Value of this literal.
            - `type`: `or_operator`
              - `children` (list of object, required) — Child nodes of the logical operator.
            - `type`: `string_literal`
              - `value` (string, required) — Value of this literal.
            - `type`: `sub_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
          - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
        - `type`: `llm`
          - `condition` (string, required) — Condition to evaluate
          - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
        - `type`: `result`
          - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
          - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
        - `type`: `unconditional`
          - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
      - `backward_condition` (object, optional) — Condition that must be met for the edge to be traversed in the backward direction (target to source).
        - `type`: `expression`
          - `expression` (object, required) — Expression to evaluate.
            - `type`: `add_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `and_operator`
              - `children` (list of object, required) — Child nodes of the logical operator.
            - `type`: `boolean_literal`
              - `value` (boolean, required) — Value of this literal.
            - `type`: `conditional_operator`
              - `condition` (object, required) — Condition deciding which expression should be selected.
              - `falseExpression` (object, required) — Expression selected if the condition is false.
              - `trueExpression` (object, required) — Expression selected if the condition is true.
            - `type`: `div_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `dynamic_variable`
              - `name` (string, required) — The name of the dynamic variable.
            - `type`: `eq_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `gt_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `gte_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `llm`
              - `value_schema` (object, optional) — JSON schema describing the value that the LLM should extract.
              - `prompt` (string, optional, deprecated) — The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead.
            - `type`: `lt_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `lte_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `mul_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `neq_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
            - `type`: `null_literal`
            - `type`: `number_literal`
              - `value` (double or integer, required) — Value of this literal.
            - `type`: `or_operator`
              - `children` (list of object, required) — Child nodes of the logical operator.
            - `type`: `string_literal`
              - `value` (string, required) — Value of this literal.
            - `type`: `sub_operator`
              - `left` (object, required) — Left operand of the binary operator.
              - `right` (object, required) — Right operand of the binary operator.
          - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
        - `type`: `llm`
          - `condition` (string, required) — Condition to evaluate
          - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
        - `type`: `result`
          - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
          - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
        - `type`: `unconditional`
          - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
    - `nodes` (map from string to object, optional)
      - `type`: `end`
        - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
        - `position` (object, optional) — Position of the node in the workflow.
          - `x` (double, optional, default: 0)
          - `y` (double, optional, default: 0)
      - `type`: `override_agent`
        - `label` (string, required) — Human-readable label for the node used throughout the UI.
        - `additional_knowledge_base` (list of object, optional) — Additional knowledge base documents that the subagent has access to. These will be used in addition to the main agent's documents.
          - `type` (enum, required) — The type of the knowledge base
            - Allowed values: `file`, `url`, `text`, `folder`
          - `name` (string, required) — The name of the knowledge base
          - `id` (string, required) — The ID of the knowledge base
          - `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
            - Allowed values: `prompt`, `auto`
        - `additional_prompt` (string, optional) — Specific goal for this subagent. It will be added to the system prompt and can be used to further refine the agent's behavior in this specific context.
        - `additional_tool_ids` (list of string, optional) — IDs of additional tools that the subagent has access to. These will be used in addition to the main agent's tools.
        - `conversation_config` (object, optional) — Configuration overrides applied while the subagent is conducting the conversation.
          - `asr` (object, optional) — Configuration for conversational transcription
            - `quality` ("high", optional) — The quality of the transcription
            - `provider` (enum, optional, default: scribe_realtime) — The provider of the transcription service
            - `user_input_audio_format` (enum, optional, default: pcm_16000) — The format of the audio to be transcribed
            - `keywords` (list of string, optional) — Keywords to boost prediction probability for
          - `turn` (object, optional) — Configuration for turn detection
            - `turn_timeout` (double, optional) — Maximum wait time for the user's reply before re-engaging the user
            - `initial_wait_time` (double, optional) — How long the agent will wait for the user to start the conversation if the first message is empty. If not set, uses the regular turn_timeout.
            - `silence_end_call_timeout` (double, optional) — Maximum wait time since the user last spoke before terminating the call
            - `turn_eagerness` (enum, optional, default: normal) — Controls how eager the agent is to respond. Low = less eager (waits longer), Standard = default eagerness, High = more eager (responds sooner)
            - `spelling_patience` (enum, optional, default: auto) — Controls if the agent should be more patient when user is spelling numbers and named entities. Auto = model based, Off = never wait extra
            - `speculative_turn` (boolean, optional) — When enabled, starts generating LLM responses during silence before full turn confidence is reached, reducing perceived latency. May increase LLM costs.
            - `retranscribe_on_turn_timeout` (boolean, optional) — When enabled, if VAD detects no speech, attempts to re-transcribe accumulated audio at turn timeout. Disables silence discount billing for affected turns.
            - `turn_model` (enum, optional, default: turn_v3) — Version of the turn detection model to use.
            - `interruption_ignore_terms` (list of string, optional) — List of terms that should not trigger an interruption when spoken by the user (e.g. 'gotcha', 'understood'). Uses case-insensitive exact matching.
            - `interruption_ignore_term_languages` (list of string, optional) — Language codes for which preset ignore-term categories have been activated. Stored explicitly so display is not inferred from term overlap.
            - `transcribe_on_disabled_interruptions` (boolean, optional) — When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.
            - `soft_timeout_config` (object, optional) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
          - `tts` (object, optional) — Configuration for conversational text to speech
            - `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
            - `voice_id` (string, optional) — The voice ID to use for TTS
            - `supported_voices` (list of object, optional) — Additional supported voices for the agent
            - `expressive_mode` (boolean, optional) — When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.
            - `suggested_audio_tags` (list of object, optional) — Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.
            - `agent_output_audio_format` (enum, optional, default: pcm_16000) — The audio format to use for TTS
            - `optimize_streaming_latency` (integer, optional) — Deprecated: this field is a no-op and is ignored.
            - `stability` (double, optional) — The stability of generated speech
            - `speed` (double, optional) — The speed of generated speech
            - `similarity_boost` (double, optional) — The similarity boost for generated speech
            - `text_normalisation_type` (enum, optional, default: system_prompt) — Method for converting numbers to words before converting text to speech. If set to SYSTEM_PROMPT, the system prompt will be updated to include normalization instructions. If set to ELEVENLABS, the text will be normalized after generation, incurring slight additional latency.
            - `pronunciation_dictionary_locators` (list of object, optional) — The pronunciation dictionary locators
            - `enable_phoneme_tags` (boolean, optional) — Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.
          - `conversation` (object, optional) — Configuration for conversational events
            - `text_only` (boolean, optional) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
            - `max_duration_seconds` (integer, optional) — The maximum duration of a conversation in seconds
            - `client_events` (list of enum, optional) — The events that will be sent to the client
            - `file_input` (object, optional) — Configuration for file input (image/PDF uploads) during conversations.
            - `monitoring_enabled` (boolean, optional) — Enable real-time monitoring of conversations via WebSocket
            - `monitoring_events` (list of enum, optional) — The events that will be sent to monitoring connections.
            - `background_sound` (object, optional) — Configuration for background sound during conversations.
            - `source_attribution` (boolean, optional) — When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.
          - `language_presets` (map from string to object, optional) — Language presets for conversations
            - `overrides` (object, required) — The overrides for the language preset
            - `first_message_translation` (object, optional) — The translation of the first message
            - `soft_timeout_translation` (object, optional) — The translation of the soft timeout message
          - `vad` (object, optional) — Configuration for voice activity detection
          - `agent` (object, optional) — Agent specific configuration
            - `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
            - `language` (string, optional) — Language of the agent - used for ASR and TTS
            - `hinglish_mode` (boolean, optional) — When enabled and language is Hindi, the agent will respond in Hinglish
            - `dynamic_variables` (object, optional) — Configuration for dynamic variables
            - `disable_first_message_interruptions` (boolean, optional) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
            - `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
            - `text_behavior_overrides` (map from string to object, optional) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
            - `prompt` (object, optional) — The prompt for the agent
        - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
        - `entry_behavior` (enum, optional, default: auto) — Dictates whether this node should immediately generate a response upon entry or wait for the user input. When set to "auto", the behavior will be decided based on the type of the preceding node: "wait_for_user" after the "say" and "start" nodes and "generate_immediately" otherwise.
          - Allowed values: `generate_immediately`, `wait_for_user`, `auto`
        - `position` (object, optional) — Position of the node in the workflow.
          - `x` (double, optional, default: 0)
          - `y` (double, optional, default: 0)
      - `type`: `phone_number`
        - `transfer_destination` (object, required)
          - `type`: `phone`
            - `phone_number` (string, required)
          - `type`: `phone_dynamic_variable`
            - `phone_number` (string, required)
          - `type`: `sip_uri`
            - `sip_uri` (string, required)
          - `type`: `sip_uri_dynamic_variable`
            - `sip_uri` (string, required)
        - `custom_sip_headers` (list of object, optional) — Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.
          - `type`: `dynamic`
            - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
            - `value` (string, required) — The dynamic variable name to resolve
          - `type`: `static`
            - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
            - `value` (string, required) — The header value
        - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
        - `position` (object, optional) — Position of the node in the workflow.
          - `x` (double, optional, default: 0)
          - `y` (double, optional, default: 0)
        - `post_dial_digits` (object, optional) — DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.
          - `type`: `dynamic`
            - `value` (string, required) — The dynamic variable name to resolve
          - `type`: `static`
            - `value` (string, required) — DTMF digits to send after call connects (e.g., 'ww1234' for extension)
        - `transfer_type` (enum, optional, default: conference)
          - Allowed values: `blind`, `conference`, `sip_refer`
        - `uui` (object, optional) — User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.
          - `data` (string, required) — UUI payload to send on SIP REFER transfers. Supports inline dynamic variables and is hex-encoded at transfer time.
          - `protocol_discriminator` (string, optional) — Optional one-octet protocol discriminator (two hex digits, e.g. '00'). Required by platforms such as Genesys Cloud, which otherwise strip the first octet of the payload. Leave unset for platforms like Talkdesk that expect a bare hex payload.
          - `protocol_discriminator_mode` (enum, optional, default: prefix) — How to attach protocol\_discriminator. 'prefix' prepends the octet to the hex payload (User-to-User=XX\<hex>;encoding=hex). 'pd\_parameter' sends it as a separate parameter (User-to-User=\<hex>;pd=XX;encoding=hex). Ignored when protocol\_discriminator is unset.
            - Allowed values: `prefix`, `pd_parameter`
      - `type`: `standalone_agent`
        - `agent_id` (string, optional) — The ID of the agent to transfer the conversation to. None means transfer within the current agent.
        - `delay_ms` (integer, optional, default: 0) — Artificial delay in milliseconds applied before transferring the conversation.
        - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
        - `enable_transferred_agent_first_message` (boolean, optional, default: false) — Whether to enable the transferred agent to send its configured first message after the transfer.
        - `node_id` (string, optional) — Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node.
        - `position` (object, optional) — Position of the node in the workflow.
          - `x` (double, optional, default: 0)
          - `y` (double, optional, default: 0)
        - `preserve_client_tts_overrides` (boolean, optional, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.
        - `transfer_message` (string, optional) — Optional message sent to the user before the transfer is initiated.
      - `type`: `start`
        - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
        - `position` (object, optional) — Position of the node in the workflow.
          - `x` (double, optional, default: 0)
          - `y` (double, optional, default: 0)
      - `type`: `tool`
        - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
        - `position` (object, optional) — Position of the node in the workflow.
          - `x` (double, optional, default: 0)
          - `y` (double, optional, default: 0)
        - `tools` (list of object, optional) — List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully.
          - `tool_id` (string, required)
    - `prevent_subagent_loops` (boolean, optional, default: false) — Whether to prevent loops in the workflow execution.
- `branch_id` (string, optional) — ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch.

## Response

### 200

Successful Response

- `any`

## Examples

**Request**

```json
{
  "test_run_ids": [
    "test_run_ids"
  ],
  "agent_id": "agent_id"
}
```

**Response**

```json
{
  "key": "value"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.invocations.resubmit("test_invocation_id", {
        testRunIds: [
            "test_run_ids",
        ],
        agentId: "agent_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.invocations.resubmit(
    test_invocation_id="test_invocation_id",
    test_run_ids=[
        "test_run_ids"
    ],
    agent_id="agent_id",
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

	url := "https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id/resubmit"

	payload := strings.NewReader("{\n  \"test_run_ids\": [\n    \"test_run_ids\"\n  ],\n  \"agent_id\": \"agent_id\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id/resubmit")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"test_run_ids\": [\n    \"test_run_ids\"\n  ],\n  \"agent_id\": \"agent_id\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id/resubmit")
  .header("Content-Type", "application/json")
  .body("{\n  \"test_run_ids\": [\n    \"test_run_ids\"\n  ],\n  \"agent_id\": \"agent_id\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id/resubmit', [
  'body' => '{
  "test_run_ids": [
    "test_run_ids"
  ],
  "agent_id": "agent_id"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id/resubmit");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"test_run_ids\": [\n    \"test_run_ids\"\n  ],\n  \"agent_id\": \"agent_id\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "test_run_ids": ["test_run_ids"],
  "agent_id": "agent_id"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id/resubmit")! as URL,
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
