---
title: "Stream simulate conversation"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/simulate-conversation-stream.md
path: docs/eleven-agents/api-reference/agents/simulate-conversation-stream
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Stream simulate conversation

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/simulate-conversation/stream
Content-Type: application/json

Deprecated. Use the `/v1/convai/agent-testing/create` and `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run simulations. Run a conversation between the agent and a simulated user and stream back the response. Response is streamed back as partial lists of messages that should be concatenated and once the conversation has complete a single final message with the conversation analysis will be sent.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/simulate-conversation-stream

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

- `simulation_specification` (object, required) — A specification detailing how the conversation should be simulated
  - `simulated_user_config` (object, required)
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
        - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
      - `reasoning_effort` (enum, optional) — Reasoning effort of the model. Only available for some models.
        - Allowed values: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`
      - `thinking_budget` (integer, optional) — Max number of tokens used for thinking. Use 0 to turn off if supported by the model.
      - `enable_reasoning_summary` (boolean, optional, default: false) — Enable model reasoning summaries. When disabled, we do not request summaries from provider if possible for faster TTFB. Not ZRM compatible.
      - `temperature` (double, optional) — The temperature for the LLM. Defaults to 0. Set to null to omit the parameter from the LLM request entirely (useful for custom LLMs that reject the temperature field).
      - `max_tokens` (integer, optional, default: -1) — If greater than 0, maximum number of tokens the LLM can predict
      - `tool_ids` (list of string, optional) — A list of IDs of tools used by the agent
      - `built_in_tools` (object, optional) — Built-in system tools to be used by the agent
        - `transfer_to_agent` (object, optional) — The transfer to agent tool
          - `name` (string, required)
          - `params` (object, required)
            - `system_tool_type`: `end_call`
            - `system_tool_type`: `end_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `knowledge_base`
              - `enabled_strategies` (list of enum, optional)
            - `system_tool_type`: `knowledge_base_rag`
            - `system_tool_type`: `language_detection`
              - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
            - `system_tool_type`: `play_keypad_touch_tone`
              - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
              - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
            - `system_tool_type`: `run_subagent`
              - `agents` (list of object, required)
            - `system_tool_type`: `skip_turn`
            - `system_tool_type`: `start_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `transfer_to_agent`
              - `transfers` (list of object, required)
            - `system_tool_type`: `transfer_to_number`
              - `transfers` (list of object, required)
              - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
            - `system_tool_type`: `voicemail_detection`
              - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).
          - `type` ("system", optional) — The type of tool
          - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
          - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
          - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
          - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - Allowed values: `auto`, `force`, `off`
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
          - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - Allowed values: `auto`, `always`
          - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
          - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
          - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
        - `end_call` (object, optional) — The end call tool
          - `name` (string, required)
          - `params` (object, required)
            - `system_tool_type`: `end_call`
            - `system_tool_type`: `end_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `knowledge_base`
              - `enabled_strategies` (list of enum, optional)
            - `system_tool_type`: `knowledge_base_rag`
            - `system_tool_type`: `language_detection`
              - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
            - `system_tool_type`: `play_keypad_touch_tone`
              - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
              - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
            - `system_tool_type`: `run_subagent`
              - `agents` (list of object, required)
            - `system_tool_type`: `skip_turn`
            - `system_tool_type`: `start_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `transfer_to_agent`
              - `transfers` (list of object, required)
            - `system_tool_type`: `transfer_to_number`
              - `transfers` (list of object, required)
              - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
            - `system_tool_type`: `voicemail_detection`
              - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).
          - `type` ("system", optional) — The type of tool
          - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
          - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
          - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
          - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - Allowed values: `auto`, `force`, `off`
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
          - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - Allowed values: `auto`, `always`
          - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
          - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
          - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
        - `language_detection` (object, optional) — The language detection tool
          - `name` (string, required)
          - `params` (object, required)
            - `system_tool_type`: `end_call`
            - `system_tool_type`: `end_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `knowledge_base`
              - `enabled_strategies` (list of enum, optional)
            - `system_tool_type`: `knowledge_base_rag`
            - `system_tool_type`: `language_detection`
              - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
            - `system_tool_type`: `play_keypad_touch_tone`
              - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
              - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
            - `system_tool_type`: `run_subagent`
              - `agents` (list of object, required)
            - `system_tool_type`: `skip_turn`
            - `system_tool_type`: `start_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `transfer_to_agent`
              - `transfers` (list of object, required)
            - `system_tool_type`: `transfer_to_number`
              - `transfers` (list of object, required)
              - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
            - `system_tool_type`: `voicemail_detection`
              - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).
          - `type` ("system", optional) — The type of tool
          - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
          - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
          - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
          - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - Allowed values: `auto`, `force`, `off`
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
          - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - Allowed values: `auto`, `always`
          - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
          - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
          - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
        - `transfer_to_number` (object, optional) — The transfer to number tool
          - `name` (string, required)
          - `params` (object, required)
            - `system_tool_type`: `end_call`
            - `system_tool_type`: `end_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `knowledge_base`
              - `enabled_strategies` (list of enum, optional)
            - `system_tool_type`: `knowledge_base_rag`
            - `system_tool_type`: `language_detection`
              - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
            - `system_tool_type`: `play_keypad_touch_tone`
              - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
              - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
            - `system_tool_type`: `run_subagent`
              - `agents` (list of object, required)
            - `system_tool_type`: `skip_turn`
            - `system_tool_type`: `start_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `transfer_to_agent`
              - `transfers` (list of object, required)
            - `system_tool_type`: `transfer_to_number`
              - `transfers` (list of object, required)
              - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
            - `system_tool_type`: `voicemail_detection`
              - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).
          - `type` ("system", optional) — The type of tool
          - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
          - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
          - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
          - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - Allowed values: `auto`, `force`, `off`
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
          - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - Allowed values: `auto`, `always`
          - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
          - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
          - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
        - `skip_turn` (object, optional) — The skip turn tool
          - `name` (string, required)
          - `params` (object, required)
            - `system_tool_type`: `end_call`
            - `system_tool_type`: `end_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `knowledge_base`
              - `enabled_strategies` (list of enum, optional)
            - `system_tool_type`: `knowledge_base_rag`
            - `system_tool_type`: `language_detection`
              - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
            - `system_tool_type`: `play_keypad_touch_tone`
              - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
              - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
            - `system_tool_type`: `run_subagent`
              - `agents` (list of object, required)
            - `system_tool_type`: `skip_turn`
            - `system_tool_type`: `start_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `transfer_to_agent`
              - `transfers` (list of object, required)
            - `system_tool_type`: `transfer_to_number`
              - `transfers` (list of object, required)
              - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
            - `system_tool_type`: `voicemail_detection`
              - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).
          - `type` ("system", optional) — The type of tool
          - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
          - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
          - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
          - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - Allowed values: `auto`, `force`, `off`
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
          - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - Allowed values: `auto`, `always`
          - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
          - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
          - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
        - `play_keypad_touch_tone` (object, optional) — The play DTMF tool
          - `name` (string, required)
          - `params` (object, required)
            - `system_tool_type`: `end_call`
            - `system_tool_type`: `end_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `knowledge_base`
              - `enabled_strategies` (list of enum, optional)
            - `system_tool_type`: `knowledge_base_rag`
            - `system_tool_type`: `language_detection`
              - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
            - `system_tool_type`: `play_keypad_touch_tone`
              - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
              - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
            - `system_tool_type`: `run_subagent`
              - `agents` (list of object, required)
            - `system_tool_type`: `skip_turn`
            - `system_tool_type`: `start_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `transfer_to_agent`
              - `transfers` (list of object, required)
            - `system_tool_type`: `transfer_to_number`
              - `transfers` (list of object, required)
              - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
            - `system_tool_type`: `voicemail_detection`
              - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).
          - `type` ("system", optional) — The type of tool
          - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
          - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
          - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
          - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - Allowed values: `auto`, `force`, `off`
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
          - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - Allowed values: `auto`, `always`
          - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
          - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
          - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
        - `voicemail_detection` (object, optional) — The voicemail detection tool
          - `name` (string, required)
          - `params` (object, required)
            - `system_tool_type`: `end_call`
            - `system_tool_type`: `end_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `knowledge_base`
              - `enabled_strategies` (list of enum, optional)
            - `system_tool_type`: `knowledge_base_rag`
            - `system_tool_type`: `language_detection`
              - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
            - `system_tool_type`: `play_keypad_touch_tone`
              - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
              - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
            - `system_tool_type`: `run_subagent`
              - `agents` (list of object, required)
            - `system_tool_type`: `skip_turn`
            - `system_tool_type`: `start_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `transfer_to_agent`
              - `transfers` (list of object, required)
            - `system_tool_type`: `transfer_to_number`
              - `transfers` (list of object, required)
              - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
            - `system_tool_type`: `voicemail_detection`
              - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).
          - `type` ("system", optional) — The type of tool
          - `description` (string, optional, default: ) — Description of when the tool should be used and what it does. Leave empty to use the default description that's optimized for the specific tool type.
          - `response_timeout_secs` (integer, optional, default: 20) — The maximum time in seconds to wait for the tool call to complete.
          - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
          - `pre_tool_speech` (enum, optional, default: auto) — Controls whether the agent speaks before this tool is called. 'auto' (default) decides based on recent tool latency, 'force' always asks the agent to speak, 'off' fully opts out regardless of latency.
            - Allowed values: `auto`, `force`, `off`
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
          - `tool_call_sound_behavior` (enum, optional, default: auto) — Determines when the tool call sound should play. 'auto' only plays when there's pre-tool speech, 'always' plays for every tool call.
            - Allowed values: `auto`, `always`
          - `tool_error_handling_mode` (enum, optional, default: auto) — Controls how tool errors are processed before being shared with the agent. 'auto' determines handling based on tool type (summarized for native integrations, hide for others), 'summarized' sends an LLM-generated summary, 'passthrough' sends the raw error, 'hide' does not share the error with the agent.
            - Allowed values: `auto`, `summarized`, `passthrough`, `hide`
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
            - `secret_id` (string, required)
          - Conv AI Env Var Locator
            - `env_var_label` (string, required)
        - `auth_connection` (object or object, optional) — Optional workspace auth connection for authentication. Only auth connections that produce an Authorization Bearer token are supported; Basic auth, mTLS, custom header, and URL secret auth connections are not supported.
          - Auth Connection Locator
            - `auth_connection_id` (string, required)
          - Environment Auth Connection Locator
            - `env_var_label` (string, required)
        - `request_headers` (map from string to string or object or object or object, optional) — Headers that should be included in the request
          - Conv AI Secret Locator
            - `secret_id` (string, required)
          - Conv AI Dynamic Variable
            - `variable_name` (string, required)
          - Conv AI Env Var Locator
            - `env_var_label` (string, required)
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
            - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
      - `cascade_timeout_seconds` (double, optional, default: 4) — Time in seconds before cascading to backup LLM. Must be between 2 and 15 seconds.
      - `tools` (list of object, optional, deprecated) — A list of tools that the agent can use over the course of the conversation, use tool_ids instead
        - `type`: `api_integration_webhook`
          - `api_integration_connection_id` (string, required)
          - `api_integration_id` (string, required)
          - `assignments` (list of object, required) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `description` (string, required) — Description of when the tool should be used and what it does.
          - `dynamic_variables` (object, required) — Configuration for dynamic variables
            - `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values
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
          - `api_schema_overrides` (object, optional) — User overrides applied on top of the base api_schema
            - `schema_overrides` (map from string to object, optional)
            - `response_filter_mode` (enum, optional, default: all) — Controls how tool responses are filtered before being visible to the agent.
            - `response_filters` (list of string, optional)
            - `request_headers` (map from string to string or object, optional)
          - `tool_call_sound` (enum, optional) — Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.
            - Allowed values: `typing`, `elevator1`, `elevator2`, `elevator3`, `elevator4`
        - `type`: `client`
          - `description` (string, required) — Description of when the tool should be used and what it does.
          - `name` (string, required)
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `dynamic_variables` (object, optional) — Configuration for dynamic variables
            - `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values
          - `execution_mode` (enum, optional, default: immediate) — Determines when and how the tool executes: 'immediate' executes the tool right away when requested by the LLM, 'post_tool_speech' waits for the agent to finish speaking before executing, 'async' runs the tool in the background without blocking - best for long-running operations.
            - Allowed values: `immediate`, `post_tool_speech`, `async`
          - `expects_response` (boolean, optional, default: false) — If true, calling this tool should block the conversation until the client responds with some response which is passed to the llm. If false then we will continue the conversation without waiting for the client to respond, this is useful to show content to a user but not block the conversation
          - `interruption_mode` (enum, optional, default: allow) — Controls whether the user can interrupt the agent around this tool call. 'allow' (default) lets the user interrupt at any time, 'disable_during_tool' suppresses interruptions only while the tool is running, 'disable_during_tool_and_turn' suppresses interruptions while the tool runs and for the agent response that follows it.
            - Allowed values: `allow`, `disable_during_tool`, `disable_during_tool_and_turn`
          - `parameters` (object, optional) — Schema for any parameters to pass to the client
            - `description` (string, optional, default: )
            - `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
            - `constant_value` (map from string to any, optional) — When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted.
            - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
            - `type` ("object", optional)
            - `required` (list of string, optional)
            - `properties` (map from string to object or object or object, optional)
            - `required_constraints` (object, optional) — Wrapper for anyOf/allOf composition constraints scoped to required fields.
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
          - `params` (object, required)
            - `system_tool_type`: `end_call`
            - `system_tool_type`: `end_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `knowledge_base`
              - `enabled_strategies` (list of enum, optional)
            - `system_tool_type`: `knowledge_base_rag`
            - `system_tool_type`: `language_detection`
              - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
            - `system_tool_type`: `play_keypad_touch_tone`
              - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
              - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
            - `system_tool_type`: `run_subagent`
              - `agents` (list of object, required)
            - `system_tool_type`: `skip_turn`
            - `system_tool_type`: `start_procedure`
              - `procedures` (map from string to object, optional)
            - `system_tool_type`: `transfer_to_agent`
              - `transfers` (list of object, required)
            - `system_tool_type`: `transfer_to_number`
              - `transfers` (list of object, required)
              - `enable_client_message` (boolean, optional, default: true) — Whether to play a message to the client while they wait for transfer. Defaults to true for backward compatibility.
            - `system_tool_type`: `voicemail_detection`
              - `voicemail_message` (string, optional) — Optional message to leave on voicemail when detected. If not provided, the call will end immediately when voicemail is detected. Supports dynamic variables (e.g., \{\{system\_\_time}}, \{\{system\_\_call\_duration\_secs}}, \{\{custom\_variable}}).
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
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
          - `api_schema` (object, required) — The schema for the outgoing webhoook, including parameters and URL specification
            - `url` (string, required) — The URL that the webhook will be sent to. May include path parameters, e.g. [https://example.com/agents/\{agent\_id}](https://example.com/agents/\{agent_id})
            - `request_headers` (map from string to string or object or object or object, optional) — Headers that should be included in the request
            - `method` (enum, optional, default: GET) — The HTTP method to use for the webhook
            - `path_params_schema` (map from string to object, optional) — Schema for path parameters, if any. The keys should match the placeholders in the URL.
            - `query_params_schema` (object, optional) — Schema for any query params, if any. These will be added to end of the URL as query params. Note: properties in a query param must all be literal types
            - `request_body_schema` (object, optional) — Schema for the body parameters, if any. Used for POST/PATCH/PUT requests. The schema should be an object which will be sent as the json body
            - `response_body_schema` (object, optional) — Schema describing the expected response body structure. For documentation only; not surfaced to the LLM.
            - `response_filter` (object, optional) — Optional allow-list filter applied to the response before the LLM sees it, so large responses don't pollute the context. Defaults to the full response.
            - `content_type` (enum, optional, default: application/json) — Content type for the request body. Only applies to POST/PUT/PATCH requests.
            - `auth_resolved_params` (list of string, optional) — URL placeholders resolved from the auth connection (e.g. secrets injected via UrlSecretAuthConnection) rather than from path_params_schema.
            - `auth_connection` (object or object, optional) — Optional auth connection to use for authentication with this webhook
          - `description` (string, required) — Description of when the tool should be used and what it does.
          - `name` (string, required)
          - `assignments` (list of object, optional) — Configuration for extracting values from tool responses and assigning them to dynamic variables
            - `dynamic_variable` (string, required) — The name of the dynamic variable to assign the extracted value to
            - `value_path` (string, required) — Dot notation path to extract the value from the source (e.g., 'user.name' or 'data.0.id')
            - `source` ("response", optional) — The source to extract the value from. Currently only 'response' is supported.
            - `sanitize` (boolean, optional, default: false) — If true, this assignment's value will be removed from the tool response before sending to the LLM and transcript, but still processed for variable assignment.
            - `preserve_native_type` (boolean, optional, default: false) — If true, non-scalar values (lists, objects) extracted from the tool response are stored as their native type instead of being stringified to JSON. Enable this to use extracted arrays directly as list dynamic variables.
          - `dynamic_variables` (object, optional) — Configuration for dynamic variables
            - `dynamic_variable_placeholders` (map from string to any, optional) — A dictionary of dynamic variable placeholders and their values
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
          - `disable_interruptions` (boolean, optional, default: false, deprecated) — DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.
          - `force_pre_tool_speech` (boolean, optional, default: false, deprecated) — DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.
  - `tool_mock_config` (map from string to object, optional)
    - `default_return_value` (string, optional, default: Tool Called.)
    - `default_is_error` (boolean, optional, default: false)
  - `partial_conversation_history` (list of object, optional) — A partial conversation history to start the simulation from. If empty, simulation starts fresh.
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
          - `webhook_details` (object, required)
            - `method` (string, required)
            - `url` (string, required)
            - `type` ("webhook", optional)
            - `headers` (map from string to string, optional)
            - `path_params` (map from string to string, optional)
            - `query_params` (map from string to string, optional)
            - `body` (string, optional)
          - `credential_id` (string, optional, default: )
          - `integration_connection_id` (string, optional, default: )
          - `integration_id` (string, optional, default: )
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
      - Conversation History Transcript System Tool Result Common Model Input
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
      - Conversation History Transcript API Integration Webhook Tools Result Common Model Input
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
          - `new_value` (string, required)
          - `updated_at` (double, required)
          - `tool_name` (string, required)
          - `tool_request_id` (string, required)
          - `old_value` (string, optional)
        - `integration_id` (string, optional, default: )
        - `credential_id` (string, optional, default: )
        - `integration_connection_id` (string, optional, default: )
      - Conversation History Transcript Workflow Tools Result Common Model Input
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
  - `dynamic_variables` (map from string to any, optional)
- `extra_evaluation_criteria` (list of object, optional) — A list of evaluation criteria to test
  - `id` (string, required) — The unique identifier for the evaluation criteria
  - `name` (string, required)
  - `conversation_goal_prompt` (string, required) — The prompt that the agent should use to evaluate the conversation
  - `type` ("prompt", optional) — The type of evaluation criteria
  - `use_knowledge_base` (boolean, optional, default: false) — When evaluating the prompt, should the agent's knowledge base be used.
  - `scope` (enum, optional, default: conversation) — The scope of transcript context used when evaluating this criterion. 'conversation' uses the full transcript; 'agent' uses only the portion where the defining agent was active.
    - Allowed values: `conversation`, `agent`
  - `llm` (enum, optional) — LLM model to use for this evaluation criteria. If not set, uses agent's analysis_llm default.
    - Allowed values: `gpt-4o-mini`, `gpt-4o`, `gpt-4`, `gpt-4-turbo`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.2-chat-latest`, `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-5.5`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5-mini`, `gpt-5-nano`, `gpt-3.5-turbo`, `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-2.5-flash-lite`, `gemini-2.5-flash`, `gemini-3-pro-preview`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite-preview`, `gemini-3.1-flash-lite`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`, `claude-sonnet-4-5`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-sonnet-4`, `claude-haiku-4-5`, `claude-3-7-sonnet`, `claude-3-5-sonnet`, `claude-3-5-sonnet-v1`, `claude-3-haiku`, `grok-beta`, `custom-llm`, `qwen3-4b`, `qwen3-30b-a3b`, `qwen36-35b-a3b`, `qwen35-397b-a17b`, `gpt-oss-20b`, `gpt-oss-120b`, `glm-45-air-fp8`, `gemini-2.5-flash-preview-09-2025`, `gemini-2.5-flash-lite-preview-09-2025`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.0-flash-lite-001`, `gemini-2.0-flash-001`, `gemini-1.5-flash-002`, `gemini-1.5-flash-001`, `gemini-1.5-pro-002`, `gemini-1.5-pro-001`, `claude-sonnet-4@20250514`, `claude-sonnet-4-5@20250929`, `claude-haiku-4-5@20251001`, `claude-3-7-sonnet@20250219`, `claude-3-5-sonnet@20240620`, `claude-3-5-sonnet-v2@20241022`, `claude-3-haiku@20240307`, `gpt-5-2025-08-07`, `gpt-5.1-2025-11-13`, `gpt-5.2-2025-12-11`, `gpt-5.4-2026-03-05`, `gpt-5.4-mini-2026-03-17`, `gpt-5.4-nano-2026-03-17`, `gpt-5.5-2026-04-23`, `gpt-5-mini-2025-08-07`, `gpt-5-nano-2025-08-07`, `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`, `gpt-4o-mini-2024-07-18`, `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, `gpt-4-0613`, `gpt-4-0314`, `gpt-4-turbo-2024-04-09`, `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `watt-tool-8b`, `watt-tool-70b`
  - `scoring_mode` (enum, optional, default: binary) — How this criterion is scored. 'binary' resolves to success/failure/unknown. 'numeric_uniform' returns a number on the [0, max_score] scale which is normalized into the aggregate conversation success percentage.
    - Allowed values: `binary`, `numeric_uniform`
  - `max_score` (integer, optional, default: 100) — Maximum value of the numeric score scale (minimum is always 0). Only used when scoring_mode is 'numeric_uniform'.
  - `score_instructions` (string, optional) — Optional free-text instructions describing how to assign values on the numeric scale. Only used when scoring_mode is 'numeric_uniform'.
- `new_turns_limit` (integer, optional, default: 10000) — Maximum number of new turns to generate in the conversation simulation

## Examples

**Request**

```json
{
  "simulation_specification": {
    "simulated_user_config": {
      "first_message": "Hello, how can I help you today?",
      "language": "en",
      "disable_first_message_interruptions": false
    }
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.simulateConversationStream("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        simulationSpecification: {
            simulatedUserConfig: {
                firstMessage: "Hello, how can I help you today?",
                language: "en",
                disableFirstMessageInterruptions: false,
            },
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, ConversationSimulationSpecification, AgentConfig

client = ElevenLabs()

client.conversational_ai.agents.simulate_conversation_stream(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    simulation_specification=ConversationSimulationSpecification(
        simulated_user_config=AgentConfig(
            first_message="Hello, how can I help you today?",
            language="en",
            disable_first_message_interruptions=False,
        ),
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation/stream"

	payload := strings.NewReader("{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation/stream")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation/stream")
  .header("Content-Type", "application/json")
  .body("{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation/stream', [
  'body' => '{
  "simulation_specification": {
    "simulated_user_config": {
      "first_message": "Hello, how can I help you today?",
      "language": "en",
      "disable_first_message_interruptions": false
    }
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation/stream");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["simulation_specification": ["simulated_user_config": [
      "first_message": "Hello, how can I help you today?",
      "language": "en",
      "disable_first_message_interruptions": false
    ]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation/stream")! as URL,
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
