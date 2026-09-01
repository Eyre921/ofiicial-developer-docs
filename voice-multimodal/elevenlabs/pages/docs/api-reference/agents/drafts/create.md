---
title: "Create draft"
source: https://elevenlabs.io/docs/api-reference/agents/drafts/create.md
path: docs/api-reference/agents/drafts/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create draft

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/drafts
Content-Type: application/json

Create a new draft for an agent

Reference: https://elevenlabs.io/docs/api-reference/agents/drafts/create

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
    - `forward_condition` (object, optional, nullable) — Condition that must be met for the edge to be traversed in the forward direction (source to target).
      - `type`: `expression` (WorkflowExpressionConditionModel)
        - `expression` (object, required) — Expression to evaluate.
          - `type`: `add_operator` (ASTAdditionOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `and_operator` (ASTAndOperatorNode)
            - `children` (list of object, required) — Child nodes of the logical operator.
          - `type`: `boolean_literal` (ASTBooleanNode)
            - `value` (boolean, required) — Value of this literal.
          - `type`: `conditional_operator` (ASTConditionalOperatorNode)
            - `condition` (object, required) — Condition deciding which expression should be selected.
            - `falseExpression` (object, required) — Expression selected if the condition is false.
            - `trueExpression` (object, required) — Expression selected if the condition is true.
          - `type`: `div_operator` (ASTDivisionOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `dynamic_variable` (ASTDynamicVariableNode)
            - `name` (string, required) — The name of the dynamic variable.
          - `type`: `eq_operator` (ASTEqualsOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `gt_operator` (ASTGreaterThanOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `gte_operator` (ASTGreaterThanOrEqualsOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `llm` (llm)
          - `type`: `lt_operator` (ASTLessThanOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `lte_operator` (ASTLessThanOrEqualsOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `mul_operator` (ASTMultiplicationOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `neq_operator` (ASTNotEqualsOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `null_literal` (ASTNullNode)
          - `type`: `number_literal` (ASTNumberNode)
            - `value` (double or integer, required) — Value of this literal.
          - `type`: `or_operator` (ASTOrOperatorNode)
            - `children` (list of object, required) — Child nodes of the logical operator.
          - `type`: `string_literal` (ASTStringNode)
            - `value` (string, required) — Value of this literal.
          - `type`: `sub_operator` (ASTSubtractionOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
        - `label` (string, optional, nullable) — Optional human-readable label for the condition used throughout the UI.
      - `type`: `llm` (WorkflowLLMConditionModel)
        - `condition` (string, required) — Condition to evaluate
        - `label` (string, optional, nullable) — Optional human-readable label for the condition used throughout the UI.
      - `type`: `result` (WorkflowResultConditionModel)
        - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
        - `label` (string, optional, nullable) — Optional human-readable label for the condition used throughout the UI.
      - `type`: `unconditional` (WorkflowUnconditionalModel)
        - `label` (string, optional, nullable) — Optional human-readable label for the condition used throughout the UI.
    - `backward_condition` (object, optional, nullable) — Condition that must be met for the edge to be traversed in the backward direction (target to source).
      - `type`: `expression` (WorkflowExpressionConditionModel)
        - `expression` (object, required) — Expression to evaluate.
          - `type`: `add_operator` (ASTAdditionOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `and_operator` (ASTAndOperatorNode)
            - `children` (list of object, required) — Child nodes of the logical operator.
          - `type`: `boolean_literal` (ASTBooleanNode)
            - `value` (boolean, required) — Value of this literal.
          - `type`: `conditional_operator` (ASTConditionalOperatorNode)
            - `condition` (object, required) — Condition deciding which expression should be selected.
            - `falseExpression` (object, required) — Expression selected if the condition is false.
            - `trueExpression` (object, required) — Expression selected if the condition is true.
          - `type`: `div_operator` (ASTDivisionOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `dynamic_variable` (ASTDynamicVariableNode)
            - `name` (string, required) — The name of the dynamic variable.
          - `type`: `eq_operator` (ASTEqualsOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `gt_operator` (ASTGreaterThanOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `gte_operator` (ASTGreaterThanOrEqualsOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `llm` (llm)
          - `type`: `lt_operator` (ASTLessThanOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `lte_operator` (ASTLessThanOrEqualsOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `mul_operator` (ASTMultiplicationOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `neq_operator` (ASTNotEqualsOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
          - `type`: `null_literal` (ASTNullNode)
          - `type`: `number_literal` (ASTNumberNode)
            - `value` (double or integer, required) — Value of this literal.
          - `type`: `or_operator` (ASTOrOperatorNode)
            - `children` (list of object, required) — Child nodes of the logical operator.
          - `type`: `string_literal` (ASTStringNode)
            - `value` (string, required) — Value of this literal.
          - `type`: `sub_operator` (ASTSubtractionOperatorNode)
            - `left` (object, required) — Left operand of the binary operator.
            - `right` (object, required) — Right operand of the binary operator.
        - `label` (string, optional, nullable) — Optional human-readable label for the condition used throughout the UI.
      - `type`: `llm` (WorkflowLLMConditionModel)
        - `condition` (string, required) — Condition to evaluate
        - `label` (string, optional, nullable) — Optional human-readable label for the condition used throughout the UI.
      - `type`: `result` (WorkflowResultConditionModel)
        - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
        - `label` (string, optional, nullable) — Optional human-readable label for the condition used throughout the UI.
      - `type`: `unconditional` (WorkflowUnconditionalModel)
        - `label` (string, optional, nullable) — Optional human-readable label for the condition used throughout the UI.
  - `nodes` (map from string to object, optional)
    - `type`: `end` (WorkflowEndNodeModel)
      - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
      - `position` (object, optional) — Position of the node in the workflow.
        - `x` (double, optional, default: 0)
        - `y` (double, optional, default: 0)
    - `type`: `override_agent` (WorkflowOverrideAgentNodeModel)
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
        - `asr` (object, optional, nullable) — Configuration for conversational transcription
          - `quality` (enum, optional, nullable, default: high) — The quality of the transcription
            - Allowed values: `high`
          - `provider` (enum, optional, nullable, default: scribe_realtime) — The provider of the transcription service
            - Allowed values: `elevenlabs`, `scribe_realtime`
          - `user_input_audio_format` (enum, optional, nullable, default: pcm_16000) — The format of the audio to be transcribed
            - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
          - `keywords` (list of string, optional, nullable) — Keywords to boost prediction probability for
        - `turn` (object, optional, nullable) — Configuration for turn detection
          - `turn_timeout` (double, optional, nullable) — Maximum wait time for the user's reply before re-engaging the user
          - `initial_wait_time` (double, optional, nullable) — How long the agent will wait for the user to start the conversation if the first message is empty. If not set, uses the regular turn_timeout.
          - `silence_end_call_timeout` (double, optional, nullable) — Maximum wait time since the user last spoke before terminating the call
          - `turn_eagerness` (enum, optional, nullable, default: normal) — Controls how eager the agent is to respond. Low = less eager (waits longer), Standard = default eagerness, High = more eager (responds sooner)
            - Allowed values: `patient`, `normal`, `eager`
          - `spelling_patience` (enum, optional, nullable, default: auto) — Controls if the agent should be more patient when user is spelling numbers and named entities. Auto = model based, Off = never wait extra
            - Allowed values: `auto`, `off`
          - `speculative_turn` (boolean, optional, nullable) — When enabled, starts generating LLM responses during silence before full turn confidence is reached, reducing perceived latency. May increase LLM costs.
          - `retranscribe_on_turn_timeout` (boolean, optional, nullable) — When enabled, if VAD detects no speech, attempts to re-transcribe accumulated audio at turn timeout. Disables silence discount billing for affected turns.
          - `turn_model` (enum, optional, nullable, default: turn_v3) — Version of the turn detection model to use.
            - Allowed values: `turn_v2`, `turn_v3`
          - `interruption_ignore_terms` (list of string, optional, nullable) — List of terms that should not trigger an interruption when spoken by the user (e.g. 'gotcha', 'understood'). Uses case-insensitive exact matching.
          - `interruption_ignore_term_languages` (list of string, optional, nullable) — Language codes for which preset ignore-term categories have been activated. Stored explicitly so display is not inferred from term overlap.
          - `merge_with_default_ignore_terms` (boolean, optional, nullable) — When enabled, the curated default terms for interruption_ignore_term_languages are used in addition to interruption_ignore_terms.
          - `transcribe_on_disabled_interruptions` (boolean, optional, nullable) — When interruptions are disabled, still transcribe what the user says so it can carry into the next turn. When off, user speech during a non-interruptible turn is ignored and won't trigger a turn.
          - `soft_timeout_config` (object, optional, nullable) — Configuration for soft timeout functionality. Provides immediate feedback during longer LLM responses.
            - `timeout_seconds` (double, optional, nullable) — Time in seconds before showing the predefined message while waiting for LLM response. Set to -1 to disable.
            - `message` (string, optional, nullable) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
            - `additional_soft_timeout_messages` (list of string, optional, nullable) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.
            - `use_llm_generated_message` (boolean, optional, nullable) — If enabled, the soft timeout message will be generated dynamically instead of using the static message.
            - `randomize_fillers` (boolean, optional, nullable) — If enabled, shuffle the order of static soft timeout messages once at the start of each turn. Only applies when use_llm_generated_message is false.
            - `max_soft_timeouts_per_generation` (integer, optional, nullable) — Maximum filler messages while waiting for a single LLM response. Fires every timeout_seconds until the LLM streams content or this limit is reached.
            - `llm_generated_message_prompt_override` (string, optional, nullable) — Custom prompt for generating the soft timeout filler message when use\_llm\_generated\_message is enabled. Recent conversation context is provided as a separate user message. If not set, the default prompt will be used. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
            - `disable_until_first_user_message` (boolean, optional, nullable) — When true, soft timeout fillers are suppressed until the conversation has at least one real user message. Prevents fillers during the agent's opening turn (e.g. workflow generate-immediately / tool calls before the user speaks).
        - `tts` (object, optional, nullable) — Configuration for conversational text to speech
          - `model_id` (enum, optional, nullable, default: eleven_flash_v2) — The model to use for TTS
            - Allowed values: `eleven_turbo_v2`, `eleven_turbo_v2_5`, `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`
          - `voice_id` (string, optional, nullable) — The voice ID to use for TTS
          - `supported_voices` (list of object, optional, nullable) — Additional supported voices for the agent
            - `label` (string, required)
            - `voice_id` (string, required)
            - `description` (string, optional, nullable)
            - `language` (string, optional, nullable)
            - `model_family` (enum, optional, nullable)
            - `optimize_streaming_latency` (enum, optional, nullable)
            - `stability` (double, optional, nullable)
            - `speed` (double, optional, nullable)
            - `similarity_boost` (double, optional, nullable)
          - `expressive_mode` (boolean, optional, nullable) — When enabled, applies expressive audio tags prompt. Automatically disabled for non-v3 models.
          - `suggested_audio_tags` (list of object, optional, nullable) — Suggested audio tags to boost expressive speech (for eleven_v3 and eleven_v3_conversational models). The agent can still use other tags not listed here.
            - `tag` (string, required) — Audio tag to use (for best performance, 1-2 words, e.g., 'happy', 'excited')
            - `description` (string, optional, nullable) — Optional description of when to use this tag
          - `agent_output_audio_format` (enum, optional, nullable, default: pcm_16000) — The audio format to use for TTS
            - Allowed values: `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`
          - `optimize_streaming_latency` (enum, optional, nullable) — Deprecated: this field is a no-op and is ignored.
            - Allowed values: `0`, `1`, `2`, `3`, `4`
          - `stability` (double, optional, nullable) — The stability of generated speech
          - `speed` (double, optional, nullable) — The speed of generated speech
          - `similarity_boost` (double, optional, nullable) — The similarity boost for generated speech
          - `text_normalisation_type` (enum, optional, nullable, default: system_prompt) — Method for converting numbers to words before converting text to speech. If set to SYSTEM_PROMPT, the system prompt will be updated to include normalization instructions. If set to ELEVENLABS, the text will be normalized after generation, incurring slight additional latency.
            - Allowed values: `system_prompt`, `elevenlabs`
          - `pronunciation_dictionary_locators` (list of object, optional, nullable) — The pronunciation dictionary locators
            - `pronunciation_dictionary_id` (string, required) — The ID of the pronunciation dictionary
            - `version_id` (string, required, nullable) — The ID of the version of the pronunciation dictionary
          - `enable_phoneme_tags` (boolean, optional, nullable) — Opt-in to SSML phoneme tag handling for V3 models. When enabled, phoneme tags (inline and from pronunciation dictionaries) are parsed into inline IPA before being sent to the model.
          - `audio_effects` (object, optional, nullable) — Optional TTS effects spec: filter preset, distance (proximity EQ), and environment (convolution reverb).
            - `filter_preset_id` (string, optional, nullable)
            - `distance` (double, optional, default: 0)
            - `environment_id` (string, optional, nullable)
            - `background_noise_id` (string, optional, nullable)
            - `send_level` (double, optional, default: 1)
            - `seed` (integer, optional, nullable)
        - `conversation` (object, optional, nullable) — Configuration for conversational events
          - `text_only` (boolean, optional, nullable) — If enabled audio will not be processed and only text will be used, use to avoid audio pricing.
          - `max_duration_seconds` (integer, optional, nullable) — The maximum duration of a conversation in seconds
          - `client_events` (list of enum, optional, nullable) — The events that will be sent to the client
            - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `context_usage`, `internal_turn_probability`, `internal_tentative_agent_response`
          - `file_input` (object, optional, nullable) — Configuration for file input (image/PDF uploads) during conversations.
            - `enabled` (boolean, optional, nullable) — When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.
            - `max_files_in_memory` (integer, optional, nullable) — Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.
            - `max_files_per_conversation` (integer, optional, nullable) — Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.
          - `monitoring_enabled` (boolean, optional, nullable) — Enable real-time monitoring of conversations via WebSocket
          - `monitoring_events` (list of enum, optional, nullable) — The events that will be sent to monitoring connections.
            - Allowed values: `conversation_initiation_metadata`, `asr_initiation_metadata`, `ping`, `audio`, `interruption`, `user_transcript`, `tentative_user_transcript`, `agent_response`, `agent_response_correction`, `client_tool_call`, `mcp_tool_call`, `mcp_connection_status`, `agent_tool_request`, `agent_tool_response`, `agent_tool_response_full_payload`, `agent_response_metadata`, `vad_score`, `agent_chat_response_part`, `client_error`, `guardrail_triggered`, `dtmf_request`, `agent_response_complete`, `context_usage`, `internal_turn_probability`, `internal_tentative_agent_response`
          - `dtmf_input_settings` (object, optional, nullable) — Configure DTMF (keypad) input collection during phone calls
            - `dtmf_input_timeout` (double, optional, default: 2) — Timeout in seconds to wait for additional DTMF digits
            - `hash_terminator` (boolean, optional, default: true) — If true, pressing # immediately completes DTMF input
            - `redact_input` (boolean, optional, default: false) — If true, replace the caller's DTMF (keypad) entries with a redaction marker in the transcript, conversation log and analysis. Digits the agent repeats back or passes to a tool are not affected.
          - `background_sound` (object, optional, nullable) — Configuration for background sound during conversations.
            - `source_type` (enum, optional, nullable) — The type of background sound source.
            - `source_id` (enum, optional, nullable) — Identifier for the sound source.
            - `volume` (double, optional, nullable) — Volume level for background sound (0.01 to 1.0).
            - `crossfade_loop` (boolean, optional, nullable) — Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.
          - `source_attribution` (boolean, optional, nullable) — When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.
        - `language_presets` (map from string to object, optional, nullable) — Language presets for conversations
          - `overrides` (object, required) — The overrides for the language preset
            - `asr` (object, optional, nullable) — Configuration for conversational transcription
            - `turn` (object, optional, nullable) — Configuration for turn detection
            - `tts` (object, optional, nullable) — Configuration for conversational text to speech
            - `conversation` (object, optional, nullable) — Configuration for conversational events
            - `agent` (object, optional, nullable) — Agent specific configuration
          - `first_message_translation` (object, optional, nullable) — The translation of the first message
            - `source_hash` (string, required)
            - `text` (string, required)
          - `soft_timeout_translation` (object, optional, nullable) — The translation of the soft timeout message
            - `source_hash` (string, required)
            - `text` (string, required)
        - `vad` (object, optional, nullable) — Configuration for voice activity detection
        - `agent` (object, optional, nullable) — Agent specific configuration
          - `first_message` (string, optional, nullable) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
          - `language` (string, optional, nullable) — Language of the agent - used for ASR and TTS
          - `hinglish_mode` (boolean, optional, nullable) — When enabled and language is Hindi, the agent will respond in Hinglish
          - `dynamic_variables` (object, optional, nullable) — Configuration for dynamic variables
            - `dynamic_variable_placeholders` (map from string to any, optional, nullable) — A dictionary of dynamic variable placeholders and their values
          - `disable_first_message_interruptions` (boolean, optional, nullable) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
          - `max_conversation_duration_message` (string, optional, nullable) — If non-empty, the message the agent will send when max conversation duration is reached.
          - `text_behavior_overrides` (map from string to object, optional, nullable) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
            - `verbosity` (enum, optional, nullable) — Verbosity override. Underlying default applies when unset.
            - `output_format` (enum, optional, nullable) — Output format override. Underlying default applies when unset.
            - `interaction_budget` (enum, optional, nullable) — Interaction budget override. Underlying default applies when unset.
          - `prompt` (object, optional, nullable) — The prompt for the agent
            - `prompt` (string, optional, nullable) — The prompt for the agent
            - `llm` (enum, optional, nullable) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
            - `reasoning_effort` (enum, optional, nullable) — Reasoning effort of the model. Only available for some models.
            - `thinking_budget` (integer, optional, nullable) — Max number of tokens used for thinking. Use 0 to turn off if supported by the model.
            - `enable_reasoning_summary` (boolean, optional, nullable) — Enable model reasoning summaries. When disabled, we do not request summaries from provider if possible for faster TTFB. Not ZRM compatible.
            - `temperature` (double, optional, nullable) — The temperature for the LLM. Defaults to 0. Set to null to omit the parameter from the LLM request entirely (useful for custom LLMs that reject the temperature field).
            - `max_tokens` (integer, optional, nullable) — If greater than 0, maximum number of tokens the LLM can predict
            - `tool_ids` (list of string, optional, nullable) — A list of IDs of tools used by the agent
            - `built_in_tools` (object, optional, nullable) — Built-in system tools to be used by the agent
            - `mcp_server_ids` (list of string, optional, nullable) — A list of MCP server ids to be used by the agent
            - `native_mcp_server_ids` (list of string, optional, nullable) — A list of Native MCP server ids to be used by the agent
            - `knowledge_base` (list of object, optional, nullable) — A list of knowledge bases to be used by the agent
            - `custom_llm` (object, optional, nullable) — Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
            - `ignore_default_personality` (boolean, optional, nullable) — Whether to remove the default personality lines from the system prompt
            - `rag` (object, optional, nullable) — Configuration for RAG
            - `timezone` (string, optional, nullable) — Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references.
            - `backup_llm_config` (object or object or object, optional, nullable) — Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.
            - `cascade_timeout_seconds` (double, optional, nullable) — Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.
            - `tools` (list of object, optional, nullable) — A list of tools that the agent can use over the course of the conversation, use tool_ids instead
      - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
      - `entry_behavior` (enum, optional, default: auto) — Dictates whether this node should immediately generate a response upon entry or wait for the user input. When set to "auto", the behavior will be decided based on the type of the preceding node: "wait_for_user" after the "say" and "start" nodes and "generate_immediately" otherwise.
        - Allowed values: `generate_immediately`, `wait_for_user`, `auto`
      - `position` (object, optional) — Position of the node in the workflow.
        - `x` (double, optional, default: 0)
        - `y` (double, optional, default: 0)
    - `type`: `phone_number` (WorkflowPhoneNumberNodeModel)
      - `transfer_destination` (object, required)
        - `type`: `phone` (PhoneNumberTransferDestination)
          - `phone_number` (string, required)
        - `type`: `phone_dynamic_variable` (PhoneNumberDynamicVariableTransferDestination)
          - `phone_number` (string, required)
        - `type`: `sip_uri` (SIPUriTransferDestination)
          - `sip_uri` (string, required)
        - `type`: `sip_uri_dynamic_variable` (SIPUriDynamicVariableTransferDestination)
          - `sip_uri` (string, required)
      - `custom_sip_headers` (list of object, optional) — Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.
        - `type`: `dynamic` (CustomSIPHeaderWithDynamicVariable)
          - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
          - `value` (string, required) — The dynamic variable name to resolve
        - `type`: `static` (CustomSIPHeader)
          - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
          - `value` (string, required) — The header value
      - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
      - `position` (object, optional) — Position of the node in the workflow.
        - `x` (double, optional, default: 0)
        - `y` (double, optional, default: 0)
      - `post_dial_digits` (object, optional, nullable) — DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.
        - `type`: `dynamic` (PostDialDigitsDynamicVariable)
          - `value` (string, required) — The dynamic variable name to resolve
        - `type`: `static` (PostDialDigitsStatic)
          - `value` (string, required) — DTMF digits to send after call connects (e.g., 'ww1234' for extension)
      - `sip_refer_play_dialtone` (boolean, optional, default: true) — When True, a ringing tone is played on the original call leg while a SIP REFER transfer completes. The tone is carried over RTP to the SIP peer executing the REFER, so disable this if the receiving system (e.g. an SBC or contact center) should not hear it. When disabled the caller hears silence until the transfer completes. SIP REFER transfers only.
      - `transfer_type` (enum, optional, default: conference)
        - Allowed values: `blind`, `conference`, `sip_refer`
      - `uui` (object, optional, nullable) — User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.
        - `data` (string, required) — UUI payload to send on SIP REFER transfers. Supports inline dynamic variables and is hex-encoded at transfer time.
        - `protocol_discriminator` (string, optional, nullable) — Optional one-octet protocol discriminator (two hex digits, e.g. '00'). Required by platforms such as Genesys Cloud, which otherwise strip the first octet of the payload. Leave unset for platforms like Talkdesk that expect a bare hex payload.
        - `protocol_discriminator_mode` (enum, optional, default: prefix) — How to attach protocol\_discriminator. 'prefix' prepends the octet to the hex payload (User-to-User=XX\<hex>;encoding=hex). 'pd\_parameter' sends it as a separate parameter (User-to-User=\<hex>;pd=XX;encoding=hex). Ignored when protocol\_discriminator is unset.
          - Allowed values: `prefix`, `pd_parameter`
    - `type`: `standalone_agent` (WorkflowStandaloneAgentNodeModel)
      - `agent_id` (string, optional, nullable) — The ID of the agent to transfer the conversation to. None means transfer within the current agent.
      - `delay_ms` (integer, optional, default: 0) — Artificial delay in milliseconds applied before transferring the conversation.
      - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
      - `enable_transferred_agent_first_message` (boolean, optional, default: false) — Whether to enable the transferred agent to send its configured first message after the transfer.
      - `node_id` (string, optional, nullable) — Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node.
      - `position` (object, optional) — Position of the node in the workflow.
        - `x` (double, optional, default: 0)
        - `y` (double, optional, default: 0)
      - `preserve_client_tts_overrides` (boolean, optional, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.
      - `transfer_message` (string, optional, nullable) — Optional message sent to the user before the transfer is initiated.
    - `type`: `start` (WorkflowStartNodeModel)
      - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
      - `position` (object, optional) — Position of the node in the workflow.
        - `x` (double, optional, default: 0)
        - `y` (double, optional, default: 0)
    - `type`: `tool` (WorkflowToolNodeModel)
      - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
      - `position` (object, optional) — Position of the node in the workflow.
        - `x` (double, optional, default: 0)
        - `y` (double, optional, default: 0)
      - `tools` (list of object, optional) — List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully.
        - `tool_id` (string, required)
        - `schema_overrides` (map from string to object, optional, nullable) — Per-node parameter overrides applied on top of the tool's own configuration. Keys are dotted parameter paths (webhook tools prefix keys with path_params./query_params./request_body.). These take precedence over any overrides already defined on the tool itself.
          - `source`: `constant` (ConstantSchemaOverride)
            - `constant_value` (string or integer or double or boolean or list of any or map from string to any, required, nullable) — The constant value to use
          - `source`: `dynamic_variable` (DynamicVariableSchemaOverride)
            - `dynamic_variable` (string, required) — The name of the dynamic variable to use
          - `source`: `llm` (LLMSchemaOverride)
            - `prompt` (string, optional, nullable) — Prompt override for the LLM. If not provided, the original schema description is used.
          - `source`: `omit` (OmitSchemaOverride)
  - `prevent_subagent_loops` (boolean, optional, default: false) — Whether to prevent loops in the workflow execution.
- `name` (string, required) — Name for the draft
- `tags` (list of string, optional, nullable) — Tags to help classify and filter the agent

## Response

### 200

Successful Response

- `any`

## Examples

**Request**

```json
{
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "condition": "Tool A condition"
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {}
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "successful": false
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "successful": true
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {}
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "condition": "Conversation condition"
        }
      },
      "tool_b_to_end": {
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": {
          "condition": "End condition"
        }
      },
      "tool_b_to_phone": {
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": {
          "expression": {
            "children": [
              {
                "name": "force_phone_transfer"
              },
              {
                "prompt": "Phone condition",
                "value_schema": {
                  "description": "Phone condition",
                  "type": "boolean"
                }
              },
              {
                "left": {
                  "name": "mode"
                },
                "right": {
                  "value": "dev"
                }
              }
            ]
          }
        }
      }
    },
    "nodes": {
      "entry_node": {
        "conversation_config": {},
        "edge_order": [
          "entry_to_tool_a"
        ],
        "label": "Entry"
      },
      "failure_node": {
        "conversation_config": {},
        "label": "Failure"
      },
      "start_node": {
        "edge_order": [
          "start_to_entry"
        ]
      },
      "success_conversation": {
        "conversation_config": {},
        "label": "Success A"
      },
      "success_end": {},
      "success_phone": {
        "transfer_destination": {
          "phone_number": "+1234567890"
        }
      },
      "success_transfer": {
        "agent_id": "success_transfer_agent"
      },
      "tool_node_a": {
        "edge_order": [
          "tool_a_to_failure",
          "tool_a_to_tool_b"
        ],
        "tools": [
          {
            "tool_id": "tool_a"
          },
          {
            "tool_id": "tool_b"
          }
        ]
      },
      "tool_node_b": {
        "edge_order": [
          "tool_b_to_conversation",
          "tool_b_to_end",
          "tool_b_to_phone",
          "tool_b_to_agent_transfer"
        ],
        "tools": [
          {
            "tool_id": "tool_a"
          }
        ]
      }
    }
  },
  "name": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.drafts.create("agent_id", {
        branchId: "branch_id",
        workflow: {
            edges: {
                entry_to_tool_a: {
                    source: "entry_node",
                    target: "tool_node_a",
                },
                start_to_entry: {
                    source: "start_node",
                    target: "entry_node",
                },
                tool_a_to_failure: {
                    source: "tool_node_a",
                    target: "failure_node",
                },
                tool_a_to_tool_b: {
                    source: "tool_node_a",
                    target: "tool_node_b",
                },
                tool_b_to_agent_transfer: {
                    source: "tool_node_b",
                    target: "success_transfer",
                },
                tool_b_to_conversation: {
                    source: "tool_node_b",
                    target: "success_conversation",
                },
                tool_b_to_end: {
                    source: "tool_node_b",
                    target: "success_end",
                },
                tool_b_to_phone: {
                    source: "tool_node_b",
                    target: "success_phone",
                },
            },
            nodes: {},
        },
        name: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, AgentWorkflowRequestModel, WorkflowEdgeModelInput

client = ElevenLabs()

client.conversational_ai.agents.drafts.create(
    agent_id="agent_id",
    branch_id="branch_id",
    workflow=AgentWorkflowRequestModel(
        edges={
            "entry_to_tool_a": WorkflowEdgeModelInput(
                source="entry_node",
                target="tool_node_a",
            ),
            "start_to_entry": WorkflowEdgeModelInput(
                source="start_node",
                target="entry_node",
            ),
            "tool_a_to_failure": WorkflowEdgeModelInput(
                source="tool_node_a",
                target="failure_node",
            ),
            "tool_a_to_tool_b": WorkflowEdgeModelInput(
                source="tool_node_a",
                target="tool_node_b",
            ),
            "tool_b_to_agent_transfer": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_transfer",
            ),
            "tool_b_to_conversation": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_conversation",
            ),
            "tool_b_to_end": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_end",
            ),
            "tool_b_to_phone": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_phone",
            )
        },
        nodes={},
    ),
    name="string",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/drafts?branch_id=branch_id"

	payload := strings.NewReader("{\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"condition\": \"Tool A condition\"\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {}\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"successful\": false\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"successful\": true\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {}\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"condition\": \"Conversation condition\"\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"condition\": \"End condition\"\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"expression\": {\n            \"children\": [\n              {\n                \"name\": \"force_phone_transfer\"\n              },\n              {\n                \"prompt\": \"Phone condition\",\n                \"value_schema\": {\n                  \"description\": \"Phone condition\",\n                  \"type\": \"boolean\"\n                }\n              },\n              {\n                \"left\": {\n                  \"name\": \"mode\"\n                },\n                \"right\": {\n                  \"value\": \"dev\"\n                }\n              }\n            ]\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"conversation_config\": {},\n        \"edge_order\": [\n          \"entry_to_tool_a\"\n        ],\n        \"label\": \"Entry\"\n      },\n      \"failure_node\": {\n        \"conversation_config\": {},\n        \"label\": \"Failure\"\n      },\n      \"start_node\": {\n        \"edge_order\": [\n          \"start_to_entry\"\n        ]\n      },\n      \"success_conversation\": {\n        \"conversation_config\": {},\n        \"label\": \"Success A\"\n      },\n      \"success_end\": {},\n      \"success_phone\": {\n        \"transfer_destination\": {\n          \"phone_number\": \"+1234567890\"\n        }\n      },\n      \"success_transfer\": {\n        \"agent_id\": \"success_transfer_agent\"\n      },\n      \"tool_node_a\": {\n        \"edge_order\": [\n          \"tool_a_to_failure\",\n          \"tool_a_to_tool_b\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          },\n          {\n            \"tool_id\": \"tool_b\"\n          }\n        ]\n      },\n      \"tool_node_b\": {\n        \"edge_order\": [\n          \"tool_b_to_conversation\",\n          \"tool_b_to_end\",\n          \"tool_b_to_phone\",\n          \"tool_b_to_agent_transfer\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          }\n        ]\n      }\n    }\n  },\n  \"name\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/drafts?branch_id=branch_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"condition\": \"Tool A condition\"\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {}\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"successful\": false\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"successful\": true\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {}\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"condition\": \"Conversation condition\"\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"condition\": \"End condition\"\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"expression\": {\n            \"children\": [\n              {\n                \"name\": \"force_phone_transfer\"\n              },\n              {\n                \"prompt\": \"Phone condition\",\n                \"value_schema\": {\n                  \"description\": \"Phone condition\",\n                  \"type\": \"boolean\"\n                }\n              },\n              {\n                \"left\": {\n                  \"name\": \"mode\"\n                },\n                \"right\": {\n                  \"value\": \"dev\"\n                }\n              }\n            ]\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"conversation_config\": {},\n        \"edge_order\": [\n          \"entry_to_tool_a\"\n        ],\n        \"label\": \"Entry\"\n      },\n      \"failure_node\": {\n        \"conversation_config\": {},\n        \"label\": \"Failure\"\n      },\n      \"start_node\": {\n        \"edge_order\": [\n          \"start_to_entry\"\n        ]\n      },\n      \"success_conversation\": {\n        \"conversation_config\": {},\n        \"label\": \"Success A\"\n      },\n      \"success_end\": {},\n      \"success_phone\": {\n        \"transfer_destination\": {\n          \"phone_number\": \"+1234567890\"\n        }\n      },\n      \"success_transfer\": {\n        \"agent_id\": \"success_transfer_agent\"\n      },\n      \"tool_node_a\": {\n        \"edge_order\": [\n          \"tool_a_to_failure\",\n          \"tool_a_to_tool_b\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          },\n          {\n            \"tool_id\": \"tool_b\"\n          }\n        ]\n      },\n      \"tool_node_b\": {\n        \"edge_order\": [\n          \"tool_b_to_conversation\",\n          \"tool_b_to_end\",\n          \"tool_b_to_phone\",\n          \"tool_b_to_agent_transfer\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          }\n        ]\n      }\n    }\n  },\n  \"name\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_id/drafts?branch_id=branch_id")
  .header("Content-Type", "application/json")
  .body("{\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"condition\": \"Tool A condition\"\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {}\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"successful\": false\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"successful\": true\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {}\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"condition\": \"Conversation condition\"\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"condition\": \"End condition\"\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"expression\": {\n            \"children\": [\n              {\n                \"name\": \"force_phone_transfer\"\n              },\n              {\n                \"prompt\": \"Phone condition\",\n                \"value_schema\": {\n                  \"description\": \"Phone condition\",\n                  \"type\": \"boolean\"\n                }\n              },\n              {\n                \"left\": {\n                  \"name\": \"mode\"\n                },\n                \"right\": {\n                  \"value\": \"dev\"\n                }\n              }\n            ]\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"conversation_config\": {},\n        \"edge_order\": [\n          \"entry_to_tool_a\"\n        ],\n        \"label\": \"Entry\"\n      },\n      \"failure_node\": {\n        \"conversation_config\": {},\n        \"label\": \"Failure\"\n      },\n      \"start_node\": {\n        \"edge_order\": [\n          \"start_to_entry\"\n        ]\n      },\n      \"success_conversation\": {\n        \"conversation_config\": {},\n        \"label\": \"Success A\"\n      },\n      \"success_end\": {},\n      \"success_phone\": {\n        \"transfer_destination\": {\n          \"phone_number\": \"+1234567890\"\n        }\n      },\n      \"success_transfer\": {\n        \"agent_id\": \"success_transfer_agent\"\n      },\n      \"tool_node_a\": {\n        \"edge_order\": [\n          \"tool_a_to_failure\",\n          \"tool_a_to_tool_b\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          },\n          {\n            \"tool_id\": \"tool_b\"\n          }\n        ]\n      },\n      \"tool_node_b\": {\n        \"edge_order\": [\n          \"tool_b_to_conversation\",\n          \"tool_b_to_end\",\n          \"tool_b_to_phone\",\n          \"tool_b_to_agent_transfer\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          }\n        ]\n      }\n    }\n  },\n  \"name\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/drafts?branch_id=branch_id', [
  'body' => '{
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "condition": "Tool A condition"
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {}
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "successful": false
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "successful": true
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {}
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "condition": "Conversation condition"
        }
      },
      "tool_b_to_end": {
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": {
          "condition": "End condition"
        }
      },
      "tool_b_to_phone": {
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": {
          "expression": {
            "children": [
              {
                "name": "force_phone_transfer"
              },
              {
                "prompt": "Phone condition",
                "value_schema": {
                  "description": "Phone condition",
                  "type": "boolean"
                }
              },
              {
                "left": {
                  "name": "mode"
                },
                "right": {
                  "value": "dev"
                }
              }
            ]
          }
        }
      }
    },
    "nodes": {
      "entry_node": {
        "conversation_config": {},
        "edge_order": [
          "entry_to_tool_a"
        ],
        "label": "Entry"
      },
      "failure_node": {
        "conversation_config": {},
        "label": "Failure"
      },
      "start_node": {
        "edge_order": [
          "start_to_entry"
        ]
      },
      "success_conversation": {
        "conversation_config": {},
        "label": "Success A"
      },
      "success_end": {},
      "success_phone": {
        "transfer_destination": {
          "phone_number": "+1234567890"
        }
      },
      "success_transfer": {
        "agent_id": "success_transfer_agent"
      },
      "tool_node_a": {
        "edge_order": [
          "tool_a_to_failure",
          "tool_a_to_tool_b"
        ],
        "tools": [
          {
            "tool_id": "tool_a"
          },
          {
            "tool_id": "tool_b"
          }
        ]
      },
      "tool_node_b": {
        "edge_order": [
          "tool_b_to_conversation",
          "tool_b_to_end",
          "tool_b_to_phone",
          "tool_b_to_agent_transfer"
        ],
        "tools": [
          {
            "tool_id": "tool_a"
          }
        ]
      }
    }
  },
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/drafts?branch_id=branch_id");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"condition\": \"Tool A condition\"\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {}\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"successful\": false\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"successful\": true\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {}\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"condition\": \"Conversation condition\"\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"condition\": \"End condition\"\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"expression\": {\n            \"children\": [\n              {\n                \"name\": \"force_phone_transfer\"\n              },\n              {\n                \"prompt\": \"Phone condition\",\n                \"value_schema\": {\n                  \"description\": \"Phone condition\",\n                  \"type\": \"boolean\"\n                }\n              },\n              {\n                \"left\": {\n                  \"name\": \"mode\"\n                },\n                \"right\": {\n                  \"value\": \"dev\"\n                }\n              }\n            ]\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"conversation_config\": {},\n        \"edge_order\": [\n          \"entry_to_tool_a\"\n        ],\n        \"label\": \"Entry\"\n      },\n      \"failure_node\": {\n        \"conversation_config\": {},\n        \"label\": \"Failure\"\n      },\n      \"start_node\": {\n        \"edge_order\": [\n          \"start_to_entry\"\n        ]\n      },\n      \"success_conversation\": {\n        \"conversation_config\": {},\n        \"label\": \"Success A\"\n      },\n      \"success_end\": {},\n      \"success_phone\": {\n        \"transfer_destination\": {\n          \"phone_number\": \"+1234567890\"\n        }\n      },\n      \"success_transfer\": {\n        \"agent_id\": \"success_transfer_agent\"\n      },\n      \"tool_node_a\": {\n        \"edge_order\": [\n          \"tool_a_to_failure\",\n          \"tool_a_to_tool_b\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          },\n          {\n            \"tool_id\": \"tool_b\"\n          }\n        ]\n      },\n      \"tool_node_b\": {\n        \"edge_order\": [\n          \"tool_b_to_conversation\",\n          \"tool_b_to_end\",\n          \"tool_b_to_phone\",\n          \"tool_b_to_agent_transfer\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          }\n        ]\n      }\n    }\n  },\n  \"name\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "workflow": [
    "edges": [
      "entry_to_tool_a": [
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": ["condition": "Tool A condition"]
      ],
      "start_to_entry": [
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": []
      ],
      "tool_a_to_failure": [
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": ["successful": false]
      ],
      "tool_a_to_tool_b": [
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": ["successful": true]
      ],
      "tool_b_to_agent_transfer": [
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": []
      ],
      "tool_b_to_conversation": [
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": ["condition": "Conversation condition"]
      ],
      "tool_b_to_end": [
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": ["condition": "End condition"]
      ],
      "tool_b_to_phone": [
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": ["expression": ["children": [
              ["name": "force_phone_transfer"],
              [
                "prompt": "Phone condition",
                "value_schema": [
                  "description": "Phone condition",
                  "type": "boolean"
                ]
              ],
              [
                "left": ["name": "mode"],
                "right": ["value": "dev"]
              ]
            ]]]
      ]
    ],
    "nodes": [
      "entry_node": [
        "conversation_config": [],
        "edge_order": ["entry_to_tool_a"],
        "label": "Entry"
      ],
      "failure_node": [
        "conversation_config": [],
        "label": "Failure"
      ],
      "start_node": ["edge_order": ["start_to_entry"]],
      "success_conversation": [
        "conversation_config": [],
        "label": "Success A"
      ],
      "success_end": [],
      "success_phone": ["transfer_destination": ["phone_number": "+1234567890"]],
      "success_transfer": ["agent_id": "success_transfer_agent"],
      "tool_node_a": [
        "edge_order": ["tool_a_to_failure", "tool_a_to_tool_b"],
        "tools": [["tool_id": "tool_a"], ["tool_id": "tool_b"]]
      ],
      "tool_node_b": [
        "edge_order": ["tool_b_to_conversation", "tool_b_to_end", "tool_b_to_phone", "tool_b_to_agent_transfer"],
        "tools": [["tool_id": "tool_a"]]
      ]
    ]
  ],
  "name": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/drafts?branch_id=branch_id")! as URL,
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
