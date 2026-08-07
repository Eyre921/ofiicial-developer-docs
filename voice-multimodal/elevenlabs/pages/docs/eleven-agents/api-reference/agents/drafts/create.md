---
title: "Create draft"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/drafts/create.md
path: docs/eleven-agents/api-reference/agents/drafts/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create draft

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/drafts
Content-Type: application/json

Create a new draft for an agent

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/drafts/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Query parameters

- `branch_id` (string, required) — The ID of the agent branch to use

### Body (application/json)

- `conversation_config` (map from string to any, required) — Conversation config for the draft
- `platform_settings` (map from string to any, required) — Platform settings for the draft
- `workflow` (object, required) — Workflow for the draft
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
            - `value` (double, required) — Value of this literal.
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
            - `value` (double, required) — Value of this literal.
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
            - Allowed values: `elevenlabs`, `scribe_realtime`
          - `user_input_audio_format` (enum, optional, default: pcm_16000) — The format of the audio to be transcribed
            - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
          - `keywords` (list of string, optional) — Keywords to boost prediction probability for
        - `turn` (object, optional) — Configuration for turn detection
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
          - `transcribe_on_disabled_interruptions` (boolean, optional) — When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.
          - `soft_timeout_config` (object, optional) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
            - `timeout_seconds` (double, optional) — Time in seconds before showing the predefined message while waiting for LLM response. Set to -1 to disable.
            - `message` (string, optional) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
            - `additional_soft_timeout_messages` (list of string, optional) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.
            - `use_llm_generated_message` (boolean, optional) — If enabled, the soft timeout message will be generated dynamically instead of using the static message.
            - `randomize_fillers` (boolean, optional) — If enabled, shuffle the order of static soft timeout messages once at the start of each turn. Only applies when use_llm_generated_message is false.
            - `max_soft_timeouts_per_generation` (integer, optional) — Maximum filler messages while waiting for a single LLM response. Fires every timeout_seconds until the LLM streams content or this limit is reached.
            - `llm_generated_message_prompt_override` (string, optional) — Custom prompt for generating the soft timeout filler message when use\_llm\_generated\_message is enabled. Recent conversation context is provided as a separate user message. If not set, the default prompt will be used. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
        - `tts` (object, optional) — Configuration for conversational text to speech
          - `model_id` (enum, optional, default: eleven_flash_v2) — The model to use for TTS
            - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
          - `voice_id` (string, optional) — The voice ID to use for TTS
          - `supported_voices` (list of object, optional) — Additional supported voices for the agent
            - `label` (string, required)
            - `voice_id` (string, required)
            - `description` (string, optional)
            - `language` (string, optional)
            - `model_family` (enum, optional)
            - `optimize_streaming_latency` (integer, optional)
            - `stability` (double, optional)
            - `speed` (double, optional)
            - `similarity_boost` (double, optional)
          - `expressive_mode` (boolean, optional) — When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.
          - `suggested_audio_tags` (list of object, optional) — Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.
            - `tag` (string, required) — Audio tag to use (for best performance, 1-2 words, e.g., 'happy', 'excited')
            - `description` (string, optional) — Optional description of when to use this tag
          - `agent_output_audio_format` (enum, optional, default: pcm_16000) — The audio format to use for TTS
            - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
          - `optimize_streaming_latency` (integer, optional) — Deprecated: this field is a no-op and is ignored.
          - `stability` (double, optional) — The stability of generated speech
          - `speed` (double, optional) — The speed of generated speech
          - `similarity_boost` (double, optional) — The similarity boost for generated speech
          - `text_normalisation_type` (enum, optional, default: system_prompt) — Method for converting numbers to words before converting text to speech. If set to SYSTEM_PROMPT, the system prompt will be updated to include normalization instructions. If set to ELEVENLABS, the text will be normalized after generation, incurring slight additional latency.
            - Allowed values: `system_prompt`, `elevenlabs`
          - `pronunciation_dictionary_locators` (list of object, optional) — The pronunciation dictionary locators
            - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
            - `version_id` (string, optional) — The ID of the version of the pronunciation dictionary
          - `enable_phoneme_tags` (boolean, optional) — Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.
        - `conversation` (object, optional) — Configuration for conversational events
          - `text_only` (boolean, optional) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
          - `max_duration_seconds` (integer, optional) — The maximum duration of a conversation in seconds
          - `client_events` (list of enum, optional) — The events that will be sent to the client
            - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `internal_turn_probability`, `internal_tentative_agent_response`
          - `file_input` (object, optional) — Configuration for file input (image/PDF uploads) during conversations.
            - `enabled` (boolean, optional) — When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.
            - `max_files_in_memory` (integer, optional) — Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.
            - `max_files_per_conversation` (integer, optional) — Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.
          - `monitoring_enabled` (boolean, optional) — Enable real-time monitoring of conversations via WebSocket
          - `monitoring_events` (list of enum, optional) — The events that will be sent to monitoring connections.
            - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `internal_turn_probability`, `internal_tentative_agent_response`
          - `background_sound` (object, optional) — Configuration for background sound during conversations.
            - `source_type` ("preset", optional) — The type of background sound source.
            - `source_id` (enum, optional) — Identifier for the sound source.
            - `volume` (double, optional) — Volume level for background sound (0.01 to 1.0).
            - `crossfade_loop` (boolean, optional) — Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.
          - `source_attribution` (boolean, optional) — When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.
        - `language_presets` (map from string to object, optional) — Language presets for conversations
          - `overrides` (object, required) — The overrides for the language preset
            - `asr` (object, optional) — Configuration for conversational transcription
            - `turn` (object, optional) — Configuration for turn detection
            - `tts` (object, optional) — Configuration for conversational text to speech
            - `conversation` (object, optional) — Configuration for conversational events
            - `agent` (object, optional) — Agent specific configuration
          - `first_message_translation` (object, optional) — The translation of the first message
            - `source_hash` (string, required)
            - `text` (string, required)
          - `soft_timeout_translation` (object, optional) — The translation of the soft timeout message
            - `source_hash` (string, required)
            - `text` (string, required)
        - `vad` (object, optional) — Configuration for voice activity detection
        - `agent` (object, optional) — Agent specific configuration
          - `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
          - `language` (string, optional) — Language of the agent - used for ASR and TTS
          - `hinglish_mode` (boolean, optional) — When enabled and language is Hindi, the agent will respond in Hinglish
          - `dynamic_variables` (object, optional) — Configuration for dynamic variables
            - `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values
          - `disable_first_message_interruptions` (boolean, optional) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
          - `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
          - `text_behavior_overrides` (map from string to object, optional) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
            - `verbosity` (enum, optional) — Verbosity override. Underlying default applies when unset.
            - `output_format` (enum, optional) — Output format override. Underlying default applies when unset.
            - `interaction_budget` (enum, optional) — Interaction budget override. Underlying default applies when unset.
          - `prompt` (object, optional) — The prompt for the agent
            - `prompt` (string, optional) — The prompt for the agent
            - `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
            - `reasoning_effort` (enum, optional) — Reasoning effort of the model. Only available for some models.
            - `thinking_budget` (integer, optional) — Max number of tokens used for thinking. Use 0 to turn off if supported by the model.
            - `enable_reasoning_summary` (boolean, optional) — Enable model reasoning summaries. When disabled, we do not request summaries from provider if possible for faster TTFB. Not ZRM compatible.
            - `temperature` (double, optional) — The temperature for the LLM. Defaults to 0. Set to null to omit the parameter from the LLM request entirely (useful for custom LLMs that reject the temperature field).
            - `max_tokens` (integer, optional) — If greater than 0, maximum number of tokens the LLM can predict
            - `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
            - `built_in_tools` (object, optional) — Built-in system tools to be used by the agent
            - `mcp_server_ids` (list of string, optional) — A list of MCP server ids to be used by the agent
            - `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
            - `knowledge_base` (list of object, optional) — A list of knowledge bases to be used by the agent
            - `custom_llm` (object, optional) — Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
            - `ignore_default_personality` (boolean, optional) — Whether to remove the default personality lines from the system prompt
            - `rag` (object, optional) — Configuration for RAG
            - `timezone` (string, optional) — Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references.
            - `backup_llm_config` (object or object or object, optional) — Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.
            - `cascade_timeout_seconds` (double, optional) — Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.
            - `tools` (list of object, optional) — A list of tools that the agent can use over the course of the conversation, use tool_ids instead
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
- `name` (string, required) — Name for the draft
- `tags` (list of string, optional) — Tags to help classify and filter the agent

## Response

### 200

Successful Response

- `any`

## Examples

**Request**

```json
{
  "conversation_config": {
    "key": "value"
  },
  "platform_settings": {
    "key": "value"
  },
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_end": {
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
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
          }
        }
      }
    },
    "nodes": {
      "entry_node": {
        "type": "end"
      },
      "failure_node": {
        "type": "end"
      },
      "start_node": {
        "type": "end"
      },
      "success_conversation": {
        "type": "end"
      },
      "success_end": {
        "type": "end"
      },
      "success_phone": {
        "type": "end"
      },
      "success_transfer": {
        "type": "end"
      },
      "tool_node_a": {
        "type": "end"
      },
      "tool_node_b": {
        "type": "end"
      }
    }
  },
  "name": "name"
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
    await client.conversationalAi.agents.drafts.create("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        branchId: "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        conversationConfig: {
            "key": "value",
        },
        platformSettings: {
            "key": "value",
        },
        workflow: {
            edges: {
                "entry_to_tool_a": {
                    source: "entry_node",
                    target: "tool_node_a",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "start_to_entry": {
                    source: "start_node",
                    target: "entry_node",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_a_to_failure": {
                    source: "tool_node_a",
                    target: "failure_node",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_a_to_tool_b": {
                    source: "tool_node_a",
                    target: "tool_node_b",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_b_to_agent_transfer": {
                    source: "tool_node_b",
                    target: "success_transfer",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_b_to_conversation": {
                    source: "tool_node_b",
                    target: "success_conversation",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_b_to_end": {
                    source: "tool_node_b",
                    target: "success_end",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_b_to_phone": {
                    source: "tool_node_b",
                    target: "success_phone",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
            },
            nodes: {
                "entry_node": {
                    type: "end",
                },
                "failure_node": {
                    type: "end",
                },
                "start_node": {
                    type: "end",
                },
                "success_conversation": {
                    type: "end",
                },
                "success_end": {
                    type: "end",
                },
                "success_phone": {
                    type: "end",
                },
                "success_transfer": {
                    type: "end",
                },
                "tool_node_a": {
                    type: "end",
                },
                "tool_node_b": {
                    type: "end",
                },
            },
        },
        name: "name",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, AgentWorkflowRequestModel, WorkflowEdgeModelInput, WorkflowEdgeModelInputForwardCondition_Expression, AstNodeInput_AndOperator, AgentWorkflowRequestModelNodesValue_End

client = ElevenLabs()

client.conversational_ai.agents.drafts.create(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
    conversation_config={
        "key": "value"
    },
    platform_settings={
        "key": "value"
    },
    workflow=AgentWorkflowRequestModel(
        edges={
            "entry_to_tool_a": WorkflowEdgeModelInput(
                source="entry_node",
                target="tool_node_a",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "start_to_entry": WorkflowEdgeModelInput(
                source="start_node",
                target="entry_node",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_a_to_failure": WorkflowEdgeModelInput(
                source="tool_node_a",
                target="failure_node",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_a_to_tool_b": WorkflowEdgeModelInput(
                source="tool_node_a",
                target="tool_node_b",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_b_to_agent_transfer": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_transfer",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_b_to_conversation": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_conversation",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_b_to_end": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_end",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_b_to_phone": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_phone",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            )
        },
        nodes={
            "entry_node": AgentWorkflowRequestModelNodesValue_End(),
            "failure_node": AgentWorkflowRequestModelNodesValue_End(),
            "start_node": AgentWorkflowRequestModelNodesValue_End(),
            "success_conversation": AgentWorkflowRequestModelNodesValue_End(),
            "success_end": AgentWorkflowRequestModelNodesValue_End(),
            "success_phone": AgentWorkflowRequestModelNodesValue_End(),
            "success_transfer": AgentWorkflowRequestModelNodesValue_End(),
            "tool_node_a": AgentWorkflowRequestModelNodesValue_End(),
            "tool_node_b": AgentWorkflowRequestModelNodesValue_End()
        },
    ),
    name="name",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj"

	payload := strings.NewReader("{\n  \"conversation_config\": {\n    \"key\": \"value\"\n  },\n  \"platform_settings\": {\n    \"key\": \"value\"\n  },\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"type\": \"end\"\n      },\n      \"failure_node\": {\n        \"type\": \"end\"\n      },\n      \"start_node\": {\n        \"type\": \"end\"\n      },\n      \"success_conversation\": {\n        \"type\": \"end\"\n      },\n      \"success_end\": {\n        \"type\": \"end\"\n      },\n      \"success_phone\": {\n        \"type\": \"end\"\n      },\n      \"success_transfer\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_a\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_b\": {\n        \"type\": \"end\"\n      }\n    }\n  },\n  \"name\": \"name\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"conversation_config\": {\n    \"key\": \"value\"\n  },\n  \"platform_settings\": {\n    \"key\": \"value\"\n  },\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"type\": \"end\"\n      },\n      \"failure_node\": {\n        \"type\": \"end\"\n      },\n      \"start_node\": {\n        \"type\": \"end\"\n      },\n      \"success_conversation\": {\n        \"type\": \"end\"\n      },\n      \"success_end\": {\n        \"type\": \"end\"\n      },\n      \"success_phone\": {\n        \"type\": \"end\"\n      },\n      \"success_transfer\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_a\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_b\": {\n        \"type\": \"end\"\n      }\n    }\n  },\n  \"name\": \"name\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")
  .header("Content-Type", "application/json")
  .body("{\n  \"conversation_config\": {\n    \"key\": \"value\"\n  },\n  \"platform_settings\": {\n    \"key\": \"value\"\n  },\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"type\": \"end\"\n      },\n      \"failure_node\": {\n        \"type\": \"end\"\n      },\n      \"start_node\": {\n        \"type\": \"end\"\n      },\n      \"success_conversation\": {\n        \"type\": \"end\"\n      },\n      \"success_end\": {\n        \"type\": \"end\"\n      },\n      \"success_phone\": {\n        \"type\": \"end\"\n      },\n      \"success_transfer\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_a\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_b\": {\n        \"type\": \"end\"\n      }\n    }\n  },\n  \"name\": \"name\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj', [
  'body' => '{
  "conversation_config": {
    "key": "value"
  },
  "platform_settings": {
    "key": "value"
  },
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_end": {
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
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
          }
        }
      }
    },
    "nodes": {
      "entry_node": {
        "type": "end"
      },
      "failure_node": {
        "type": "end"
      },
      "start_node": {
        "type": "end"
      },
      "success_conversation": {
        "type": "end"
      },
      "success_end": {
        "type": "end"
      },
      "success_phone": {
        "type": "end"
      },
      "success_transfer": {
        "type": "end"
      },
      "tool_node_a": {
        "type": "end"
      },
      "tool_node_b": {
        "type": "end"
      }
    }
  },
  "name": "name"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"conversation_config\": {\n    \"key\": \"value\"\n  },\n  \"platform_settings\": {\n    \"key\": \"value\"\n  },\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"type\": \"end\"\n      },\n      \"failure_node\": {\n        \"type\": \"end\"\n      },\n      \"start_node\": {\n        \"type\": \"end\"\n      },\n      \"success_conversation\": {\n        \"type\": \"end\"\n      },\n      \"success_end\": {\n        \"type\": \"end\"\n      },\n      \"success_phone\": {\n        \"type\": \"end\"\n      },\n      \"success_transfer\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_a\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_b\": {\n        \"type\": \"end\"\n      }\n    }\n  },\n  \"name\": \"name\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "conversation_config": ["key": "value"],
  "platform_settings": ["key": "value"],
  "workflow": [
    "edges": [
      "entry_to_tool_a": [
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "start_to_entry": [
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_a_to_failure": [
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_a_to_tool_b": [
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_b_to_agent_transfer": [
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_b_to_conversation": [
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_b_to_end": [
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_b_to_phone": [
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ]
    ],
    "nodes": [
      "entry_node": ["type": "end"],
      "failure_node": ["type": "end"],
      "start_node": ["type": "end"],
      "success_conversation": ["type": "end"],
      "success_end": ["type": "end"],
      "success_phone": ["type": "end"],
      "success_transfer": ["type": "end"],
      "tool_node_a": ["type": "end"],
      "tool_node_b": ["type": "end"]
    ]
  ],
  "name": "name"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")! as URL,
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
