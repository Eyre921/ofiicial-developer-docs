---
title: "Update tool"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/update.md
path: docs/eleven-agents/api-reference/tools/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update tool

PATCH https://api.elevenlabs.io/v1/convai/tools/{tool_id}
Content-Type: application/json

Update tool that is available in the workspace.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `tool_id` (string, required) — ID of the requested tool.

### Body (application/json)

This endpoint expects a ToolRequestModel.

- `tool_config` (ToolRequestModelToolConfig, required) — Configuration for the tool
- `response_mocks` (list of ToolResponseMockConfigInput, optional) — Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.

## Response

### 200

Successful Response

- `id` (string, required)
- `tool_config` (ToolResponseModelToolConfig, required) — The type of tool
- `access_info` (ResourceAccessInfo, required)
- `usage_stats` (ToolUsageStatsResponseModel, required)
- `response_mocks` (list of ToolResponseMockConfigOutput, optional) — Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.

## Errors

### 422 Tools Update Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ToolRequestModelToolConfig

Configuration for the tool

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

### ToolResponseMockConfigInput

- `mock_result` (string, required) — The return value the LLM sees when this mock is active.
- `parameter_conditions` (list of UnitTestToolCallParameter, optional) — If the list is empty, the mock will always activate.
- `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.

### ToolResponseModelToolConfig

The type of tool

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

### ToolUsageStatsResponseModel

- `avg_latency_secs` (double, required)
- `total_calls` (integer, optional, default: 0) — The total number of calls to the tool

### ToolResponseMockConfigOutput

- `mock_result` (string, required) — The return value the LLM sees when this mock is active.
- `parameter_conditions` (list of UnitTestToolCallParameter, optional) — If the list is empty, the mock will always activate.
- `is_error` (boolean, optional, default: false) — If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

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

### UnitTestToolCallParameter

- `eval` (UnitTestToolCallParameterEval, required)
- `path` (string, required)

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

### ValidationErrorLocItem

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

### UnitTestToolCallParameterEval

- `type`: `anything`
- `type`: `exact`
  - `expected_value` (string, required) — The exact string value that the parameter must match.
- `type`: `llm`
  - `description` (string, required) — A description of the evaluation strategy to use for the test.
- `type`: `regex`
  - `pattern` (string, required) — A regex pattern to match the agent's response against.

### ObjectJsonSchemaPropertyOutputPropertiesValue

### AgentTransferOutput

- `condition` (string, required)
- `agent_id` (string, optional)
- `node_id` (string, optional)
- `delay_ms` (integer, optional, default: 0)
- `transfer_message` (string, optional)
- `enable_transferred_agent_first_message` (boolean, optional, default: false)
- `is_workflow_node_transfer` (boolean, optional, default: false)
- `preserve_client_tts_overrides` (boolean, optional, default: false) — Defines whether TTS client overrides should be carried over to the transferred agent.

### WebhookToolApiSchemaConfigOutputRequestHeadersValue

### QueryParamsJsonSchemaOutput

- `properties` (map from string to LiteralJsonSchemaProperty, required)
- `required` (list of string, optional)

### WebhookToolApiSchemaConfigOutputAuthConnection

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

### UuiTransferConfig

User-to-User Information envelope for SIP REFER transfers (RFC 7433). Outbound payloads are hex-encoded (the only encoding RFC 7433 defines). The protocol discriminator axis lets per-platform formats (Talkdesk, Genesys, ...) be expressed by configuration rather than scattered transfer flags. Further axes (ASCII encoding, header name, purpose/content parameters) can be added here without touching the transfer model.

- `data` (string, required) — UUI payload to send on SIP REFER transfers. Supports inline dynamic variables and is hex-encoded at transfer time.
- `protocol_discriminator` (string, optional) — Optional one-octet protocol discriminator (two hex digits, e.g. '00'). Required by platforms such as Genesys Cloud, which otherwise strip the first octet of the payload. Leave unset for platforms like Talkdesk that expect a bare hex payload.
- `protocol_discriminator_mode` (enum, optional, default: prefix) — How to attach protocol\_discriminator. 'prefix' prepends the octet to the hex payload (User-to-User=XX\<hex>;encoding=hex). 'pd\_parameter' sends it as a separate parameter (User-to-User=\<hex>;pd=XX;encoding=hex). Ignored when protocol\_discriminator is unset.
  - Allowed values: `prefix`, `pd_parameter`

### PhoneNumberTransferPostDialDigits

- `type`: `dynamic`
  - `value` (string, required) — The dynamic variable name to resolve
- `type`: `static`
  - `value` (string, required) — DTMF digits to send after call connects (e.g., 'ww1234' for extension)

### ConvAiSecretLocator

Used to reference a secret from the agent's secret store.

- `secret_id` (string, required)

### ConvAiDynamicVariable

Used to reference a dynamic variable.

- `variable_name` (string, required)

### ConvAiEnvVarLocator

Used to reference an environment variable by label.

- `env_var_label` (string, required)

### LiteralJsonSchemaPropertyType

### AllowedValues

- `dynamic_variable` (string, required) — Name of a dynamic variable that must resolve to a JSON array of permitted values, e.g. ["ws_alpha", "ws_beta"]. System variables work only if they resolve to a list.

### LiteralJsonSchemaPropertyConstantValue

A constant value to use for this property. Mutually exclusive with description, dynamic_variable, is_system_provided, and is_omitted.

### AuthConnectionLocator

Used to reference an auth connection from the workspace's auth connection store.

- `auth_connection_id` (string, required)

### EnvironmentAuthConnectionLocator

References an environment variable of type 'auth_connection' by label. At runtime, resolves to the auth connection for the current environment, falling back to the default environment.

- `env_var_label` (string, required)

### ArrayJsonSchemaPropertyOutput

- `description` (string, optional, default: )
- `dynamic_variable` (string, optional, default: ) — When set, the entire parameter is populated from this dynamic variable at runtime. Mutually exclusive with description (LLM-provided value), constant_value, and is_omitted.
- `constant_value` (list of any, optional) — When set, the entire array uses this constant value at runtime. Mutually exclusive with description (LLM-provided array), dynamic_variable, and is_omitted.
- `is_omitted` (boolean, optional, default: false) — If true, this parameter will be completely omitted from the request. Only valid for optional parameters. Mutually exclusive with description, dynamic_variable, and constant_value.
- `type` ("array", optional)
- `items` (ArrayJsonSchemaPropertyOutputItems, optional) — Schema for array elements.

### ArrayJsonSchemaPropertyInputItems

Schema for array elements.

### ArrayJsonSchemaPropertyOutputItems

Schema for array elements.

## Examples

**Request**

```json
{
  "tool_config": {
    "type": "client",
    "description": "description",
    "name": "name",
    "expects_response": false
  }
}
```

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
    await client.conversationalAi.tools.update("tool_id", {
        toolConfig: {
            type: "client",
            name: "name",
            description: "description",
            expectsResponse: false,
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, ToolRequestModel, ToolRequestModelToolConfig_Client

client = ElevenLabs()

client.conversational_ai.tools.update(
    tool_id="tool_id",
    request=ToolRequestModel(
        tool_config=ToolRequestModelToolConfig_Client(
            name="name",
            description="description",
            expects_response=False,
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

	url := "https://api.elevenlabs.io/v1/convai/tools/tool_id"

	payload := strings.NewReader("{\n  \"tool_config\": {\n    \"type\": \"client\",\n    \"description\": \"description\",\n    \"name\": \"name\",\n    \"expects_response\": false\n  }\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/tools/tool_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tool_config\": {\n    \"type\": \"client\",\n    \"description\": \"description\",\n    \"name\": \"name\",\n    \"expects_response\": false\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/tools/tool_id")
  .header("Content-Type", "application/json")
  .body("{\n  \"tool_config\": {\n    \"type\": \"client\",\n    \"description\": \"description\",\n    \"name\": \"name\",\n    \"expects_response\": false\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/tools/tool_id', [
  'body' => '{
  "tool_config": {
    "type": "client",
    "description": "description",
    "name": "name",
    "expects_response": false
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools/tool_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tool_config\": {\n    \"type\": \"client\",\n    \"description\": \"description\",\n    \"name\": \"name\",\n    \"expects_response\": false\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["tool_config": [
    "type": "client",
    "description": "description",
    "name": "name",
    "expects_response": false
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tools/tool_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
