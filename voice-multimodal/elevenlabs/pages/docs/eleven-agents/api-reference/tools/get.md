---
title: "Get tool"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get.md
path: docs/eleven-agents/api-reference/tools/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get tool

GET https://api.elevenlabs.io/v1/convai/tools/{tool_id}

Get tool that is available in the workspace.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `tool_id` (string, required) — ID of the requested tool.

### Query parameters

- `environment` (string, optional, default: production) — Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

## Response

### 200

Successful Response

- `id` (string, required)
- `tool_config` (object, required) — The type of tool
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
        - Literal JSON Schema Property
          - `type` ("boolean" or "string" or "integer" or "number" or list of string, required)
          - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
          - `enum` (list of string, optional) — List of allowed string values for string type parameters
          - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
          - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
          - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
          - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
          - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
        - Array JSON Schema Property Output
          - `description` (string, optional, default: )
          - `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
          - `constant_value` (list of any, optional) — When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted.
          - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
          - `type` ("array", optional)
          - `items` (object or object or object, optional) — Schema for array elements.
            - Literal JSON Schema Property
      - `required_constraints` (object, optional) — Wrapper for anyOf/allOf composition constraints scoped to required fields.
        - `any_of` (list of object, optional)
          - `required` (list of string, required)
        - `all_of` (list of object, optional)
          - `required` (list of string, required)
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
  - `type`: `system`
    - `name` (string, required)
    - `params` (object, required)
      - `system_tool_type`: `end_call`
      - `system_tool_type`: `end_procedure`
        - `procedures` (map from string to object or object, optional)
          - Procedure Version Ref
            - `procedure_id` (string, required) — Procedure ID
            - `version_id` (string, required) — Version ID of the procedure version.
          - Procedure Draft Ref
            - `procedure_id` (string, required) — Procedure ID
            - `version_id` (any, optional)
      - `system_tool_type`: `knowledge_base`
        - `enabled_strategies` (list of enum, optional)
          - Allowed values: `cat`, `keyword`, `semantic`, `ls`
      - `system_tool_type`: `knowledge_base_rag`
      - `system_tool_type`: `language_detection`
        - `only_at_conversation_start` (boolean, optional, default: false) — If no language switch happens in the first 2 user turns, later attempts fail and the conversation stays in the current language. If the language switches during those turns, later switching stays available. Enable to reduce the possibility of false switching.
      - `system_tool_type`: `play_keypad_touch_tone`
        - `suppress_turn_after_dtmf` (boolean, optional, default: false) — If true, the agent will not generate further speech after playing DTMF tones. This prevents the agent's speech from interfering with IVR systems.
        - `use_out_of_band_dtmf` (boolean, optional, default: true) — Send DTMF tones as out-of-band RTP events (RFC 4733) instead of in-band audio. Only effective for SIP trunk imported numbers.
      - `system_tool_type`: `run_subagent`
        - `agents` (list of object, required)
          - `agent_id` (string, required)
          - `description` (string, required)
          - `branch_id` (string, optional)
          - `parameters` (object, optional)
            - `description` (string, optional, default: )
            - `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
            - `constant_value` (map from string to any, optional) — When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted.
            - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
            - `type` ("object", optional)
            - `required` (list of string, optional)
            - `properties` (map from string to object or object or object, optional)
            - `required_constraints` (object, optional) — Wrapper for anyOf/allOf composition constraints scoped to required fields.
      - `system_tool_type`: `skip_turn`
      - `system_tool_type`: `start_procedure`
        - `procedures` (map from string to object or object, optional)
          - Procedure Version Ref
            - `procedure_id` (string, required) — Procedure ID
            - `version_id` (string, required) — Version ID of the procedure version.
          - Procedure Draft Ref
            - `procedure_id` (string, required) — Procedure ID
            - `version_id` (any, optional)
      - `system_tool_type`: `transfer_to_agent`
        - `transfers` (list of object, required)
          - `condition` (string, required)
          - `agent_id` (string, optional)
          - `node_id` (string, optional)
          - `delay_ms` (integer, optional, default: 0)
          - `transfer_message` (string, optional)
          - `enable_transferred_agent_first_message` (boolean, optional, default: false)
          - `is_workflow_node_transfer` (boolean, optional, default: false)
          - `preserve_client_tts_overrides` (boolean, optional, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.
      - `system_tool_type`: `transfer_to_number`
        - `transfers` (list of object, required)
          - `transfer_destination` (object, required)
            - `type`: `phone`
              - `phone_number` (string, required)
            - `type`: `phone_dynamic_variable`
              - `phone_number` (string, required)
            - `type`: `sip_uri`
              - `sip_uri` (string, required)
            - `type`: `sip_uri_dynamic_variable`
              - `sip_uri` (string, required)
          - `condition` (string, required)
          - `custom_sip_headers` (list of object, optional) — Custom SIP headers to include when transferring the call. Each header can be either a static value or a dynamic variable reference.
            - `type`: `dynamic`
              - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
              - `value` (string, required) — The dynamic variable name to resolve
            - `type`: `static`
              - `key` (string, required) — The SIP header name (e.g., 'X-Customer-ID')
              - `value` (string, required) — The header value
          - `transfer_type` (enum, optional, default: conference)
            - Allowed values: `blind`, `conference`, `sip_refer`
          - `sip_refer_play_dialtone` (boolean, optional, default: true) — When True, a ringing tone is played on the original call leg while a SIP REFER transfer completes. The tone is carried over RTP to the SIP peer executing the REFER, so disable this if the receiving system (e.g. an SBC or contact center) should not hear it. When disabled the caller hears silence until the transfer completes. SIP REFER transfers only.
          - `uui` (object, optional) — User-to-User Information (RFC 7433) to attach to SIP REFER transfers. Carries call context such as CRM identifiers or escalation reason across the transfer boundary.
            - `data` (string, required) — UUI payload to send on SIP REFER transfers. Supports inline dynamic variables and is hex-encoded at transfer time.
            - `protocol_discriminator` (string, optional) — Optional one-octet protocol discriminator (two hex digits, e.g. '00'). Required by platforms such as Genesys Cloud, which otherwise strip the first octet of the payload. Leave unset for platforms like Talkdesk that expect a bare hex payload.
            - `protocol_discriminator_mode` (enum, optional, default: prefix) — How to attach protocol\_discriminator. 'prefix' prepends the octet to the hex payload (User-to-User=XX\<hex>;encoding=hex). 'pd\_parameter' sends it as a separate parameter (User-to-User=\<hex>;pd=XX;encoding=hex). Ignored when protocol\_discriminator is unset.
          - `post_dial_digits` (object, optional) — DTMF digits to send after call connects (e.g., 'ww1234' for extension). Can be either a static value or a dynamic variable reference. Use 'w' for 0.5s pause. Only supported for Twilio transfers.
            - `type`: `dynamic`
              - `value` (string, required) — The dynamic variable name to resolve
            - `type`: `static`
              - `value` (string, required) — DTMF digits to send after call connects (e.g., 'ww1234' for extension)
          - `phone_number` (string, optional, deprecated)
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
        - Conv AI Secret Locator
          - `secret_id` (string, required)
        - Conv AI Dynamic Variable
          - `variable_name` (string, required)
        - Conv AI Env Var Locator
          - `env_var_label` (string, required)
      - `method` (enum, optional, default: GET) — The HTTP method to use for the webhook
        - Allowed values: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
      - `path_params_schema` (map from string to object, optional) — Schema for path parameters, if any. The keys should match the placeholders in the URL.
        - `type` ("boolean" or "string" or "integer" or "number" or list of string, required)
        - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
        - `enum` (list of string, optional) — List of allowed string values for string type parameters
        - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
        - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
        - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
        - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
        - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
      - `query_params_schema` (object, optional) — Schema for any query params, if any. These will be added to end of the URL as query params. Note: properties in a query param must all be literal types
        - `properties` (map from string to object, required)
          - `type` ("boolean" or "string" or "integer" or "number" or list of string, required)
          - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
          - `enum` (list of string, optional) — List of allowed string values for string type parameters
          - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
          - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
          - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
          - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
          - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
        - `required` (list of string, optional)
      - `request_body_schema` (object, optional) — Schema for the body parameters, if any. Used for POST/PATCH/PUT requests. The schema should be an object which will be sent as the json body
        - `description` (string, optional, default: )
        - `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
        - `constant_value` (map from string to any, optional) — When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted.
        - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
        - `type` ("object", optional)
        - `required` (list of string, optional)
        - `properties` (map from string to object or object or object, optional)
          - Literal JSON Schema Property
            - `type` ("boolean" or "string" or "integer" or "number" or list of string, required)
            - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
            - `enum` (list of string, optional) — List of allowed string values for string type parameters
            - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
            - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
            - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
            - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
            - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
          - Array JSON Schema Property Output
            - `description` (string, optional, default: )
            - `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
            - `constant_value` (list of any, optional) — When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted.
            - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
            - `type` ("array", optional)
            - `items` (object or object or object, optional) — Schema for array elements.
        - `required_constraints` (object, optional) — Wrapper for anyOf/allOf composition constraints scoped to required fields.
          - `any_of` (list of object, optional)
            - `required` (list of string, required)
          - `all_of` (list of object, optional)
            - `required` (list of string, required)
      - `response_body_schema` (object, optional) — Schema describing the expected response body structure. For documentation only; not surfaced to the LLM.
        - `description` (string, optional, default: )
        - `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
        - `constant_value` (map from string to any, optional) — When set, the entire object uses this constant JSON value at runtime. Mutually exclusive with description (LLM-provided object), dynamic_variable, and is_omitted.
        - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
        - `type` ("object", optional)
        - `required` (list of string, optional)
        - `properties` (map from string to object or object or object, optional)
          - Literal JSON Schema Property
            - `type` ("boolean" or "string" or "integer" or "number" or list of string, required)
            - `description` (string, optional, default: ) — The description of the property. When set, the LLM will provide the value based on this description. Mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
            - `enum` (list of string, optional) — List of allowed string values for string type parameters
            - `is_system_provided` (boolean, optional, default: false) — If true, the value will be populated by the system at runtime. Used by API Integration Webhook tools for templating. Mutually exclusive with description, dynamic_variable, constant_value, and is_omitted.
            - `dynamic_variable` (string, optional, default: ) — The name of the dynamic variable to use for this property's value. Mutually exclusive with description, is_system_provided, constant_value, and is_omitted.
            - `allowed_values_dynamic_variable` (string, optional, default: ) — When set, the LLM provides the value but the runtime rejects any value not present in the list held by this dynamic variable. Use to let the LLM pick from a server-verified set (e.g. the IDs the current user is allowed to access). Requires description; mutually exclusive with dynamic_variable, is_system_provided, constant_value, and is_omitted.
            - `constant_value` (string or integer or double or boolean, optional) — A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.
            - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, is_system_provided, and constant_value.
          - Array JSON Schema Property Output
            - `description` (string, optional, default: )
            - `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
            - `constant_value` (list of any, optional) — When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted.
            - `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
            - `type` ("array", optional)
            - `items` (object or object or object, optional) — Schema for array elements.
        - `required_constraints` (object, optional) — Wrapper for anyOf/allOf composition constraints scoped to required fields.
          - `any_of` (list of object, optional)
            - `required` (list of string, required)
          - `all_of` (list of object, optional)
            - `required` (list of string, required)
      - `response_filter` (object, optional) — Optional allow-list filter applied to the response before the LLM sees it, so large responses don't pollute the context. Defaults to the full response.
        - `mode` (enum, optional, default: all) — Controls how tool responses are filtered. 'all' returns entire response, 'allow' returns only specified paths, 'hide_all' hides the entire response.
          - Allowed values: `all`, `allow`, `hide_all`
        - `filters` (list of string, optional) — Dot notation paths to include when mode is 'allow' (e.g., ['ticket.id', 'ticket.status']).
        - `content_type` ("application/json", optional) — Content type for response filtering. Only 'application/json' responses are filtered.
      - `content_type` (enum, optional, default: application/json) — Content type for the request body. Only applies to POST/PUT/PATCH requests.
        - Allowed values: `application/json`, `application/x-www-form-urlencoded`
      - `auth_resolved_params` (list of string, optional) — URL placeholders resolved from the auth connection (e.g. secrets injected via UrlSecretAuthConnection) rather than from path_params_schema.
      - `auth_connection` (object or object, optional) — Optional auth connection to use for authentication with this webhook
        - Auth Connection Locator
          - `auth_connection_id` (string, required)
        - Environment Auth Connection Locator
          - `env_var_label` (string, required)
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
- `access_info` (object, required)
  - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
  - `creator_name` (string, required) — Name of the agent's creator
  - `creator_email` (string, required) — Email of the agent's creator
  - `role` (enum, required) — The role of the user making the request
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
    - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
- `usage_stats` (object, required)
  - `avg_latency_secs` (double, required)
  - `total_calls` (integer, optional, default: 0) — The total number of calls to the tool
- `response_mocks` (list of object, optional) — Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.
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

## Examples

**Response**

```json
{
  "id": "id",
  "tool_config": {
    "type": "client",
    "description": "description",
    "name": "name",
    "assignments": [
      {
        "dynamic_variable": "user_name",
        "value_path": "user.name",
        "source": "response",
        "sanitize": false,
        "preserve_native_type": false
      }
    ],
    "dynamic_variables": {
      "dynamic_variable_placeholders": {
        "user_name": "John Doe"
      }
    },
    "execution_mode": "immediate",
    "expects_response": false,
    "interruption_mode": "allow",
    "parameters": {
      "description": "description",
      "dynamic_variable": "dynamic_variable",
      "constant_value": {
        "key": "value"
      },
      "is_omitted": true,
      "type": "object",
      "required": [
        "required"
      ],
      "properties": {
        "key": {
          "description": "A user-provided message",
          "type": "string"
        }
      }
    },
    "pre_tool_speech": "auto",
    "response_timeout_secs": 1,
    "tool_call_sound": "typing",
    "tool_call_sound_behavior": "auto",
    "tool_error_handling_mode": "auto"
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "anonymous_access_level_override": "admin",
    "access_source": "creator"
  },
  "usage_stats": {
    "avg_latency_secs": 1.1,
    "total_calls": 1
  },
  "response_mocks": [
    {
      "mock_result": "mock_result",
      "parameter_conditions": [
        {
          "eval": {
            "type": "anything"
          },
          "path": "path"
        }
      ],
      "is_error": true
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tools.get("tool_id", {
        environment: "environment",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tools.get(
    tool_id="tool_id",
    environment="environment",
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

	url := "https://api.elevenlabs.io/v1/convai/tools/tool_id?environment=environment"

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

url = URI("https://api.elevenlabs.io/v1/convai/tools/tool_id?environment=environment")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/tools/tool_id?environment=environment")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tools/tool_id?environment=environment');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools/tool_id?environment=environment");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tools/tool_id?environment=environment")! as URL,
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
