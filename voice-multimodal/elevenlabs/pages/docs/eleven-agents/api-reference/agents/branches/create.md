---
title: "Create agent branch"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/create.md
path: docs/eleven-agents/api-reference/agents/branches/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create agent branch

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches
Content-Type: application/json

Create a new branch from a given version of any branch

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Body (application/json)

This endpoint expects an object.

- `parent_version_id` (string, required) — ID of the version to branch from
- `name` (string, required) — Name of the branch. It is unique within the agent.
- `description` (string, required) — Description for the branch
- `conversation_config` (map from string to any, optional) — Changes to apply to conversation config
- `platform_settings` (map from string to any, optional) — Changes to apply to platform settings
- `workflow` (AgentWorkflowRequestModel, optional) — Updated workflow definition
- `include_draft` (boolean, optional, default: false) — When true, the new branch uses the caller's draft procedure set instead of the branch tip. Requires parent_version_id to be the branch tip.

## Response

### 200

Successful Response

- `created_branch_id` (string, required) — ID of the created branch
- `created_version_id` (string, required) — ID of the first version on the created branch

## Errors

### 422 Branches Create Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AgentWorkflowRequestModel

- `edges` (map from string to WorkflowEdgeModelInput, optional)
- `nodes` (map from string to AgentWorkflowRequestModelNodesValue, optional)
- `prevent_subagent_loops` (boolean, optional, default: false) — Whether to prevent loops in the workflow execution.

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### WorkflowEdgeModelInput

- `source` (string, required) — ID of the source node.
- `target` (string, required) — ID of the target node.
- `forward_condition` (WorkflowEdgeModelInputForwardCondition, optional) — Condition that must be met for the edge to be traversed in the forward direction (source to target).
- `backward_condition` (WorkflowEdgeModelInputBackwardCondition, optional) — Condition that must be met for the edge to be traversed in the backward direction (target to source).

### AgentWorkflowRequestModelNodesValue

- `type`: `end`
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
- `type`: `override_agent`
  - `label` (string, required) — Human-readable label for the node used throughout the UI.
  - `additional_knowledge_base` (list of KnowledgeBaseLocator, optional) — Additional knowledge base documents that the subagent has access to. These will be used in addition to the main agent's documents.
  - `additional_prompt` (string, optional) — Specific goal for this subagent. It will be added to the system prompt and can be used to further refine the agent's behavior in this specific context.
  - `additional_tool_ids` (list of string, optional) — IDs of additional tools that the subagent has access to. These will be used in addition to the main agent's tools.
  - `conversation_config` (ConversationalConfigApiModelWorkflowOverrideInput, optional) — Configuration overrides applied while the subagent is conducting the conversation.
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `entry_behavior` (enum, optional, default: auto) — Dictates whether this node should immediately generate a response upon entry or wait for the user input. When set to "auto", the behavior will be decided based on the type of the preceding node: "wait_for_user" after the "say" and "start" nodes and "generate_immediately" otherwise.
    - Allowed values: `generate_immediately`, `wait_for_user`, `auto`
  - `position` (PositionInput, optional) — Position of the node in the workflow.
- `type`: `phone_number`
  - `transfer_destination` (WorkflowPhoneNumberNodeModelInputTransferDestination, required)
  - `custom_sip_headers` (list of WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem, optional) — Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
  - `post_dial_digits` (WorkflowPhoneNumberNodeModelInputPostDialDigits, optional) — DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.
  - `sip_refer_play_dialtone` (boolean, optional, default: true) — When True, a ringing tone is played on the original call leg while a SIP REFER transfer completes. The tone is carried over RTP to the SIP peer executing the REFER, so disable this if the receiving system (e.g. an SBC or contact center) should not hear it. When disabled the caller hears silence until the transfer completes. SIP REFER transfers only.
  - `transfer_type` (enum, optional, default: conference)
    - Allowed values: `blind`, `conference`, `sip_refer`
  - `uui` (UuiTransferConfig, optional) — User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.
- `type`: `standalone_agent`
  - `agent_id` (string, optional) — The ID of the agent to transfer the conversation to. None means transfer within the current agent.
  - `delay_ms` (integer, optional, default: 0) — Artificial delay in milliseconds applied before transferring the conversation.
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `enable_transferred_agent_first_message` (boolean, optional, default: false) — Whether to enable the transferred agent to send its configured first message after the transfer.
  - `node_id` (string, optional) — Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
  - `preserve_client_tts_overrides` (boolean, optional, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.
  - `transfer_message` (string, optional) — Optional message sent to the user before the transfer is initiated.
- `type`: `start`
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
- `type`: `tool`
  - `edge_order` (list of string, optional) — The ids of outgoing edges in the order they should be evaluated.
  - `position` (PositionInput, optional) — Position of the node in the workflow.
  - `tools` (list of WorkflowToolLocator, optional) — List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully.

### ValidationErrorLocItem

### WorkflowEdgeModelInputForwardCondition

- `type`: `expression`
  - `expression` (AstNodeInput, required) — Expression to evaluate.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `llm`
  - `condition` (string, required) — Condition to evaluate
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `result`
  - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `unconditional`
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.

### WorkflowEdgeModelInputBackwardCondition

- `type`: `expression`
  - `expression` (AstNodeInput, required) — Expression to evaluate.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `llm`
  - `condition` (string, required) — Condition to evaluate
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `result`
  - `successful` (boolean, required) — Whether all tools in the previously executed tool node were executed successfully.
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.
- `type`: `unconditional`
  - `label` (string, optional) — Optional human-readable label for the condition used throughout the UI.

### PositionInput

- `x` (double, optional, default: 0)
- `y` (double, optional, default: 0)

### KnowledgeBaseLocator

- `type` (enum, required) — The type of the knowledge base
  - Allowed values: `file`, `url`, `text`, `folder`
- `name` (string, required) — The name of the knowledge base
- `id` (string, required) — The ID of the knowledge base
- `usage_mode` (enum, optional, default: auto) — The usage mode of the knowledge base
  - Allowed values: `prompt`, `auto`

### ConversationalConfigApiModelWorkflowOverrideInput

- `asr` (AsrConversationalConfigWorkflowOverride, optional) — Configuration for conversational transcription
- `turn` (TurnConfigWorkflowOverride, optional) — Configuration for turn detection
- `tts` (TtsConversationalConfigWorkflowOverrideInput, optional) — Configuration for conversational text to speech
- `conversation` (ConversationConfigWorkflowOverrideInput, optional) — Configuration for conversational events
- `language_presets` (map from string to LanguagePresetInput, optional) — Language presets for conversations
- `vad` (VadConfigWorkflowOverride, optional) — Configuration for voice activity detection
- `agent` (AgentConfigApiModelWorkflowOverrideInput, optional) — Agent specific configuration

### WorkflowPhoneNumberNodeModelInputTransferDestination

- `type`: `phone`
  - `phone_number` (string, required)
- `type`: `phone_dynamic_variable`
  - `phone_number` (string, required)
- `type`: `sip_uri`
  - `sip_uri` (string, required)
- `type`: `sip_uri_dynamic_variable`
  - `sip_uri` (string, required)

### WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem

- `type`: `dynamic`
  - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
  - `value` (string, required) — The dynamic variable name to resolve
- `type`: `static`
  - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
  - `value` (string, required) — The header value

### WorkflowPhoneNumberNodeModelInputPostDialDigits

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

### AstNodeInput

- `type`: `add_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `and_operator`
  - `children` (list of AstNodeInput, required) — Child nodes of the logical operator.
- `type`: `boolean_literal`
  - `value` (boolean, required) — Value of this literal.
- `type`: `conditional_operator`
  - `condition` (AstNodeInput, required) — Condition deciding which expression should be selected.
  - `falseExpression` (AstNodeInput, required) — Expression selected if the condition is false.
  - `trueExpression` (AstNodeInput, required) — Expression selected if the condition is true.
- `type`: `div_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `dynamic_variable`
  - `name` (string, required) — The name of the dynamic variable.
- `type`: `eq_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `gt_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `gte_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `llm`
  - `value_schema` (LlmLiteralJsonSchemaProperty, optional) — JSON schema describing the value that the LLM should extract.
  - `prompt` (string, optional, deprecated) — The prompt to evaluate to a boolean value. Deprecated. Use a boolean schema instead.
- `type`: `lt_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `lte_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `mul_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `neq_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.
- `type`: `null_literal`
- `type`: `number_literal`
  - `value` (AstNumberNodeInputValue, required) — Value of this literal.
- `type`: `or_operator`
  - `children` (list of AstNodeInput, required) — Child nodes of the logical operator.
- `type`: `string_literal`
  - `value` (string, required) — Value of this literal.
- `type`: `sub_operator`
  - `left` (AstNodeInput, required) — Left operand of the binary operator.
  - `right` (AstNodeInput, required) — Right operand of the binary operator.

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

### TtsConversationalConfigWorkflowOverrideInput

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
- `audio_effects` (EffectsSpecInput, optional) — Optional TTS effects spec: filter preset, distance (proximity EQ), and environment (convolution reverb).

### ConversationConfigWorkflowOverrideInput

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

### LanguagePresetInput

- `overrides` (ConversationConfigClientOverrideInput, required) — The overrides for the language preset
- `first_message_translation` (LanguagePresetTranslation, optional) — The translation of the first message
- `soft_timeout_translation` (LanguagePresetTranslation, optional) — The translation of the soft timeout message

### VadConfigWorkflowOverride

### AgentConfigApiModelWorkflowOverrideInput

- `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional) — Language of the agent - used for ASR and TTS
- `hinglish_mode` (boolean, optional) — When enabled and language is Hindi, the agent will respond in Hinglish
- `dynamic_variables` (DynamicVariablesConfigWorkflowOverride, optional) — Configuration for dynamic variables
- `disable_first_message_interruptions` (boolean, optional) — If true, the user will not be able to interrupt the agent while the first message is being delivered.
- `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
- `text_behavior_overrides` (map from string to BehaviorOverride, optional) — Per-channel response behavior overrides for text conversations. Built-in channel defaults apply when unset.
- `prompt` (PromptAgentApiModelWorkflowOverrideInput, optional) — The prompt for the agent

### WorkflowToolLocatorSchemaOverridesValue

- `source`: `constant`
  - `constant_value` (ConstantSchemaOverrideConstantValue, optional) — The constant value to use
- `source`: `dynamic_variable`
  - `dynamic_variable` (string, required) — The name of the dynamic variable to use
- `source`: `llm`
  - `prompt` (string, optional) — Prompt override for the LLM. If not provided, the original schema description is used.
- `source`: `omit`

### LlmLiteralJsonSchemaProperty

- `type` (LlmLiteralJsonSchemaPropertyType, required)
- `description` (string, required)
- `enum` (list of string, optional) — List of allowed string values for string type parameters

### AstNumberNodeInputValue

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

### EffectsSpecInput

Filter preset, distance (proximity EQ), and environment (convolution reverb).

- `filter_preset_id` (string, optional)
- `distance` (double, optional, default: 0)
- `environment_id` (string, optional)
- `background_noise_id` (string, optional)
- `send_level` (double, optional, default: 1)
- `seed` (integer, optional)

### FileInputConfigWorkflowOverride

- `enabled` (boolean, optional) — When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.
- `max_files_in_memory` (integer, optional) — Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.
- `max_files_per_conversation` (integer, optional) — Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.

### DtmfInputConfig

Configuration for DTMF (keypad) input collection during phone calls.

- `dtmf_input_timeout` (double, optional, default: 2) — Timeout in seconds to wait for additional DTMF digits
- `hash_terminator` (boolean, optional, default: true) — If true, pressing # immediately completes DTMF input
- `redact_input` (boolean, optional, default: false) — If true, replace the caller's DTMF (keypad) entries with a redaction marker in the transcript, conversation log and analysis. Digits the agent repeats back or passes to a tool are not affected.

### BackgroundSoundConfigWorkflowOverride

- `source_type` ("preset", optional) — The type of background sound source.
- `source_id` (enum, optional) — Identifier for the sound source.
  - Allowed values: `office2`, `office1`, `restaurant`, `city`, `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
- `volume` (double, optional) — Volume level for background sound (0.01 to 1.0).
- `crossfade_loop` (boolean, optional) — Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.

### ConversationConfigClientOverrideInput

- `asr` (AsrConversationalConfigOverride, optional) — Configuration for conversational transcription
- `turn` (TurnConfigOverride, optional) — Configuration for turn detection
- `tts` (TtsConversationalConfigOverride, optional) — Configuration for conversational text to speech
- `conversation` (ConversationConfigOverride, optional) — Configuration for conversational events
- `agent` (AgentConfigOverrideInput, optional) — Agent specific configuration

### LanguagePresetTranslation

- `source_hash` (string, required)
- `text` (string, required)

### DynamicVariablesConfigWorkflowOverride

- `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values

### BehaviorOverride

- `verbosity` (enum, optional) — Verbosity override. Underlying default applies when unset.
  - Allowed values: `auto`, `concise`, `thorough`
- `output_format` (enum, optional) — Output format override. Underlying default applies when unset.
  - Allowed values: `mp3_22050_32`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `ulaw_8000`
- `interaction_budget` (enum, optional) — Interaction budget override. Underlying default applies when unset.
  - Allowed values: `realtime`, `5_minutes`, `10_minutes`, `1_hour`

### PromptAgentApiModelWorkflowOverrideInput

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
- `built_in_tools` (BuiltInToolsWorkflowOverrideInput, optional) — Built-in system tools to be used by the agent
- `enable_parallel_tool_calls` (boolean, optional) — Enable parallel tool calling. When enabled, the agent can execute multiple tools in parallel within a single turn. Not supported by all models.
- `mcp_server_ids` (list of string, optional) — A list of MCP server ids to be used by the agent
- `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional) — A list of knowledge bases to be used by the agent
- `custom_llm` (CustomLlm, optional) — Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
- `ignore_default_personality` (boolean, optional) — Whether to remove the default personality lines from the system prompt
- `rag` (RagConfigWorkflowOverrideInput, optional) — Configuration for RAG
- `timezone` (string, optional) — Timezone for displaying current time in system prompt. If set, the current time will be included in the system prompt using this timezone. Must be a valid timezone name (e.g., 'America/New_York', 'Europe/London', 'UTC'). Recommended for accurate time-aware responses; without this, the agent has no knowledge of the current date/time unless you provide it via dynamic variables or tools, which can lead to incorrect or hallucinated time references.
- `backup_llm_config` (PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig, optional) — Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.
- `cascade_timeout_seconds` (double, optional) — Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.
- `tools` (list of PromptAgentApiModelWorkflowOverrideInputToolsItem, optional) — A list of tools that the agent can use over the course of the conversation, use tool_ids instead

### ConstantSchemaOverrideConstantValue

The constant value to use

### LlmLiteralJsonSchemaPropertyType

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

### AgentConfigOverrideInput

- `first_message` (string, optional) — If non-empty, the first message the agent will say. If empty, the agent waits for the user to start the discussion.
- `language` (string, optional) — Language of the agent - used for ASR and TTS
- `max_conversation_duration_message` (string, optional) — If non-empty, the message the agent will send when max conversation duration is reached.
- `prompt` (PromptAgentApiModelOverrideInput, optional) — The prompt for the agent

### BuiltInToolsWorkflowOverrideInput

- `transfer_to_agent` (SystemToolConfigInput, optional) — The transfer to agent tool
- `end_call` (SystemToolConfigInput, optional) — The end call tool
- `language_detection` (SystemToolConfigInput, optional) — The language detection tool
- `transfer_to_number` (SystemToolConfigInput, optional) — The transfer to number tool
- `skip_turn` (SystemToolConfigInput, optional) — The skip turn tool
- `play_keypad_touch_tone` (SystemToolConfigInput, optional) — The play DTMF tool
- `voicemail_detection` (SystemToolConfigInput, optional) — The voicemail detection tool

### CustomLlm

- `url` (string, required) — The URL of the Chat Completions compatible endpoint
- `model_id` (string, optional) — The model ID to be used if URL serves multiple models
- `api_key` (CustomLlmApiKey, optional) — The API key for authentication. Either a workspace secret reference \{'secret\_id': '...'} or an environment variable reference \{'env\_var\_label': '...'}.
- `auth_connection` (CustomLlmAuthConnection, optional) — Optional workspace auth connection for authentication. Only auth connections that produce an Authorization Bearer token are supported; Basic auth, mTLS, custom header, and URL secret auth connections are not supported.
- `request_headers` (map from string to CustomLlmRequestHeadersValue, optional) — Headers that should be included in the request
- `api_version` (string, optional) — The API version to use for the request
- `api_type` (enum, optional, default: chat_completions) — The API type to use (chat_completions, responses or websocket)
  - Allowed values: `chat_completions`, `responses`, `websocket`

### RagConfigWorkflowOverrideInput

- `enabled` (boolean, optional)
- `embedding_model` (enum, optional, default: e5_mistral_7b_instruct)
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
- `max_vector_distance` (double, optional) — Maximum vector distance of retrieved chunks.
- `max_documents_length` (integer, optional) — Maximum total length of document chunks retrieved from RAG.
- `max_retrieved_rag_chunks_count` (integer, optional) — Maximum number of RAG document chunks to initially retrieve from the vector store. These are then further filtered by vector distance and total length.
- `num_candidates` (integer, optional) — Number of candidates evaluated in ANN vector search. Higher number means better results, but higher latency. Minimum recommended value is 100. If disabled, the default value is used.
- `query_rewrite_prompt_override` (string, optional) — Custom prompt for rewriting user queries before RAG retrieval. The conversation history will be automatically appended at the end. If not set, the default prompt will be used.
- `knowledge_base_tool_info` (KnowledgeBaseToolInfo, optional) — When set, the agent uses the knowledge_base tool instead of the legacy knowledge_base_rag tool. None means the agent is not opted in.

### PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig

Configuration for backup LLM cascading. Can be disabled, use system defaults, or specify custom order.

### PromptAgentApiModelWorkflowOverrideInputToolsItem

The type of tool

- `type`: `api_integration_webhook`
  - `api_integration_connection_id` (string, required)
  - `api_integration_id` (string, required)
  - `description` (string, required) — Description of when the tool should be used and what it does.
  - `name` (string, required)
  - `api_schema_overrides` (ApiIntegrationWebhookOverrides, optional) — User overrides applied on top of the base api_schema
  - `assignments` (list of DynamicVariableAssignment, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
  - `dynamic_variables` (DynamicVariablesConfig, optional) — Configuration for dynamic variables
  - `execution_mode` (enum, optional, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
    - Allowed values: `immediate`, `post_tool_speech`, `async`
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
  - `tool_version` (string, optional, default: 1.0.0) — The version of the API integration tool
  - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
  - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
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
  - `parameters` (ObjectJsonSchemaPropertyInput, optional) — Schema for any parameters to pass to the client
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
  - `params` (SystemToolConfigInputParams, required)
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
  - `api_schema` (WebhookToolApiSchemaConfigInput, required) — The schema for the outgoing webhoook, including parameters and URL specification
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

### SoftTimeoutConfigOverride

- `message` (string, optional) — Message to show when the first soft timeout is reached while waiting for LLM response. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{custom\_variable}}).
- `additional_soft_timeout_messages` (list of string, optional) — Extra static filler messages for subsequent soft timeouts in the same LLM generation. The first timeout uses `message`. If fewer messages are configured than `max_soft_timeouts_per_generation`, the last configured message is repeated; otherwise a built-in filler is used.

### PromptAgentApiModelOverrideInput

- `prompt` (string, optional) — The prompt for the agent
- `llm` (enum, optional) — The LLM to query with the prompt and the chat history. If using data residency, the LLM must be supported in the data residency environment
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
- `native_mcp_server_ids` (list of string, optional) — A list of Native MCP server ids to be used by the agent
- `knowledge_base` (list of KnowledgeBaseLocator, optional) — A list of knowledge bases to be used by the agent

### SystemToolConfigInput

A system tool is a tool that is used to call a system method in the server

- `name` (string, required)
- `params` (SystemToolConfigInputParams, required)
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

### BackupLlmDefault

- `preference` ("default", optional)

### BackupLlmDisabled

- `preference` ("disabled", optional)

### BackupLlmOverride

- `order` (list of enum, required)
  - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `gemini-3.8-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `glm-52`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
- `preference` ("override", optional)

### ApiIntegrationWebhookOverrides

- `schema_overrides` (map from string to ApiIntegrationWebhookOverridesSchemaOverridesValue, optional)
- `response_filter_mode` (enum, optional, default: all) — Controls how tool responses are filtered before being visible to the agent.
  - Allowed values: `all`, `allow`, `hide_all`
- `response_filters` (list of string, optional)
- `request_headers` (map from string to ApiIntegrationWebhookOverridesRequestHeadersValue, optional)

### DynamicVariableAssignment

Configuration for extracting values from tool responses and assigning them to dynamic variables.

- `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
- `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
- `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
- `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
- `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.

### DynamicVariablesConfig

- `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values

### ObjectJsonSchemaPropertyInput

- `property_kind` (enum, optional, default: object)
  - Allowed values: `array`, `object`
- `description` (string, optional, default: )
- `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
- `constant_value` (map from string to any, optional) — When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
- `type` ("object", optional)
- `required` (list of string, optional)
- `properties` (map from string to ObjectJsonSchemaPropertyInputPropertiesValue, optional)
- `required_constraints` (RequiredConstraints, optional) — Wrapper for anyOf/allOf composition constraints scoped to required fields.

### SystemToolConfigInputParams

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
  - `transfers` (list of AgentTransferInput, required)
- `system_tool_type`: `transfer_to_number`
  - `transfers` (list of PhoneNumberTransfer, required)
  - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
- `system_tool_type`: `voicemail_detection`
  - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).

### WebhookToolApiSchemaConfigInput

- `url` (string, required) — The URL that the webhook will be sent to. May include path parameters, e.g. [https://example.com/agents/\{agent\_id}](https://example.com/agents/\{agent_id})
- `request_headers` (map from string to WebhookToolApiSchemaConfigInputRequestHeadersValue, optional) — Headers that should be included in the request
- `method` (enum, optional, default: GET) — The HTTP method to use for the webhook
  - Allowed values: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- `path_params_schema` (map from string to LiteralJsonSchemaProperty, optional) — Schema for path parameters, if any. The keys should match the placeholders in the URL.
- `query_params_schema` (QueryParamsJsonSchemaInput, optional) — Schema for any query params, if any. These will be added to end of the URL as query params. Note: properties in a query param must all be literal types
- `request_body_schema` (ObjectJsonSchemaPropertyInput, optional) — Schema for the body parameters, if any. Used for POST/PATCH/PUT requests. The schema should be an object which will be sent as the json body
- `response_body_schema` (ObjectJsonSchemaPropertyInput, optional) — Schema describing the expected response body structure. For documentation only; not surfaced to the LLM.
- `response_filter` (ResponseFilter, optional) — Optional allow-list filter applied to the response before the LLM sees it, so large responses don't pollute the context. Defaults to the full response.
- `content_type` (enum, optional, default: application/json) — Content type for the request body. Only applies to POST/PUT/PATCH requests.
  - Allowed values: `application/json`, `application/x-www-form-urlencoded`
- `auth_resolved_params` (list of string, optional) — URL placeholders resolved from the auth connection (e.g. secrets injected via UrlSecretAuthConnection) rather than from path_params_schema.
- `auth_connection` (WebhookToolApiSchemaConfigInputAuthConnection, optional) — Optional auth connection to use for authentication with this webhook

### ConvAiSecretLocator

Used to reference a secret from the agent's secret store.

- `secret_id` (string, required)

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

### ObjectJsonSchemaPropertyInputPropertiesValue

### RequiredConstraints

Wrapper for anyOf/allOf composition constraints scoped to required fields.

- `any_of` (list of RequiredConstraint, optional)
- `all_of` (list of RequiredConstraint, optional)

### EndProcedureToolConfigProceduresValue

### StartProcedureToolConfigProceduresValue

### AgentTransferInput

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

### WebhookToolApiSchemaConfigInputRequestHeadersValue

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

### QueryParamsJsonSchemaInput

- `properties` (map from string to LiteralJsonSchemaProperty, required)
- `required` (list of string, optional)

### ResponseFilter

Configuration for filtering tool responses before they are visible to the agent.

- `mode` (enum, optional, default: all) — Controls how tool responses are filtered. 'all' returns entire response, 'allow' returns only specified paths, 'hide_all' hides the entire response.
  - Allowed values: `all`, `allow`, `hide_all`
- `filters` (list of string, optional) — Dot notation paths to include when mode is 'allow' (e.g., ['ticket.id', 'ticket.status']).
- `content_type` ("application/json", optional) — Content type for response filtering. Only 'application/json' responses are filtered.

### WebhookToolApiSchemaConfigInputAuthConnection

Optional auth connection to use for authentication with this webhook

### ArrayJsonSchemaPropertyInput

- `property_kind` (enum, optional, default: array)
  - Allowed values: `array`, `object`
- `description` (string, optional, default: )
- `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
- `constant_value` (list of any, optional) — When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
- `type` ("array", optional)
- `items` (ArrayJsonSchemaPropertyInputItems, optional) — Schema for array elements.

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

### AllowedValues

- `dynamic_variable` (string, required) — Name of a dynamic variable that must resolve to a JSON array of permitted values, e.g. ["ws_alpha", "ws_beta"]. System variables work only if they resolve to a list.

### LiteralJsonSchemaPropertyConstantValue

A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.

### ArrayJsonSchemaPropertyInputItems

Schema for array elements.

## Examples

**Request**

```json
{
  "parent_version_id": "parent_version_id",
  "name": "name",
  "description": "description"
}
```

**Response**

```json
{
  "created_branch_id": "created_branch_id",
  "created_version_id": "created_version_id"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.create("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        parentVersionId: "parent_version_id",
        name: "name",
        description: "description",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.create(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    parent_version_id="parent_version_id",
    name="name",
    description="description",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches"

	payload := strings.NewReader("{\n  \"parent_version_id\": \"parent_version_id\",\n  \"name\": \"name\",\n  \"description\": \"description\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"parent_version_id\": \"parent_version_id\",\n  \"name\": \"name\",\n  \"description\": \"description\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches")
  .header("Content-Type", "application/json")
  .body("{\n  \"parent_version_id\": \"parent_version_id\",\n  \"name\": \"name\",\n  \"description\": \"description\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches', [
  'body' => '{
  "parent_version_id": "parent_version_id",
  "name": "name",
  "description": "description"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"parent_version_id\": \"parent_version_id\",\n  \"name\": \"name\",\n  \"description\": \"description\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "parent_version_id": "parent_version_id",
  "name": "name",
  "description": "description"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches")! as URL,
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
