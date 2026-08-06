---
title: "Update configuration override"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/tool-configuration/update.md
path: docs/eleven-agents/api-reference/mcp/tool-configuration/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update configuration override

PATCH https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}
Content-Type: application/json

Update configuration overrides for a specific MCP tool.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/tool-configuration/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}:
    patch:
      operationId: update
      summary: Update Mcp Tool Configuration Override
      description: Update configuration overrides for a specific MCP tool.
      tags:
        - toolConfigs
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
        - name: tool_name
          in: path
          description: Name of the MCP tool to update config overrides for.
          required: true
          schema:
            type: string
        - name: environment
          in: query
          description: >-
            Environment whose values are used when the MCP server URL, headers,
            or auth connection reference environment variables. Mirrors the
            environment a conversation would run in; defaults to production.
          required: false
          schema:
            type: string
            default: production
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:McpServerResponseModel'
        '404':
          description: Tool config override not found
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                force_pre_tool_speech:
                  type: boolean
                  description: >-
                    DEPRECATED: use `pre_tool_speech` instead. If set, overrides
                    the server's force_pre_tool_speech setting for this tool.
                pre_tool_speech:
                  $ref: '#/components/schemas/type_:PreToolSpeechMode'
                  description: >-
                    If set, overrides the server's pre_tool_speech setting for
                    this tool.
                disable_interruptions:
                  type: boolean
                  description: >-
                    DEPRECATED: use `interruption_mode` instead. If set,
                    overrides the server's disable_interruptions setting for
                    this tool.
                interruption_mode:
                  $ref: '#/components/schemas/type_:ToolInterruptionMode'
                  description: >-
                    If set, overrides the server's interruption_mode setting for
                    this tool.
                tool_call_sound:
                  $ref: >-
                    #/components/schemas/type_conversationalAi/mcpServers/toolConfigs:McpToolConfigOverrideUpdateRequestModelToolCallSound
                  description: >-
                    Overrides the server's tool_call_sound setting for this
                    tool. A sound name plays that sound; 'off' overrides to no
                    sound (silence); null means do not override (inherit the
                    server default).
                tool_call_sound_behavior:
                  $ref: '#/components/schemas/type_:ToolCallSoundBehavior'
                  description: >-
                    If set, overrides the server's tool_call_sound_behavior
                    setting for this tool
                execution_mode:
                  $ref: '#/components/schemas/type_:ToolExecutionMode'
                  description: >-
                    If set, overrides the server's execution_mode setting for
                    this tool
                response_timeout_secs:
                  type: integer
                  description: >-
                    If set, overrides the server's response timeout for this MCP
                    tool.
                assignments:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_:DynamicVariableAssignment'
                  description: Dynamic variable assignments for this MCP tool
                input_overrides:
                  type: object
                  additionalProperties:
                    $ref: >-
                      #/components/schemas/type_conversationalAi/mcpServers/toolConfigs:McpToolConfigOverrideUpdateRequestModelInputOverridesValue
                  description: Mapping of json path to input override configuration
                response_mocks:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_:ToolResponseMockConfigInput'
                  description: >-
                    Mock responses with optional parameter conditions. Evaluated
                    top-to-bottom; first match wins.
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    type_:PreToolSpeechMode:
      type: string
      enum:
        - auto
        - force
        - 'off'
      default: auto
      title: PreToolSpeechMode
    type_:ToolInterruptionMode:
      type: string
      enum:
        - allow
        - disable_during_tool
        - disable_during_tool_and_turn
      default: allow
      title: ToolInterruptionMode
    type_:ToolCallSoundType:
      type: string
      enum:
        - typing
        - elevator1
        - elevator2
        - elevator3
        - elevator4
      description: Predefined tool call sounds; ``None`` means no sound.
      title: ToolCallSoundType
    type_conversationalAi/mcpServers/toolConfigs:McpToolConfigOverrideUpdateRequestModelToolCallSound:
      oneOf:
        - $ref: '#/components/schemas/type_:ToolCallSoundType'
        - type: string
          enum:
            - 'off'
      description: >-
        Overrides the server's tool_call_sound setting for this tool. A sound
        name plays that sound; 'off' overrides to no sound (silence); null means
        do not override (inherit the server default).
      title: McpToolConfigOverrideUpdateRequestModelToolCallSound
    type_:ToolCallSoundBehavior:
      type: string
      enum:
        - auto
        - always
      default: auto
      description: Determines how the tool call sound should be played.
      title: ToolCallSoundBehavior
    type_:ToolExecutionMode:
      type: string
      enum:
        - immediate
        - post_tool_speech
        - async
      default: immediate
      title: ToolExecutionMode
    type_:DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - response
          description: >-
            The source to extract the value from. Currently only 'response' is
            supported.
        dynamic_variable:
          type: string
          description: The name of the dynamic variable to assign the extracted value to
        value_path:
          type: string
          description: >-
            Dot notation path to extract the value from the source (e.g.,
            'user.name' or 'data.0.id')
        sanitize:
          type: boolean
          default: false
          description: >-
            If true, this assignment's value will be removed from the tool
            response before sending to the LLM and transcript, but still
            processed for variable assignment.
        preserve_native_type:
          type: boolean
          default: false
          description: >-
            If true, non-scalar values (lists, objects) extracted from the tool
            response are stored as their native type instead of being
            stringified to JSON. Enable this to use extracted arrays directly as
            list dynamic variables.
      required:
        - dynamic_variable
        - value_path
      description: >-
        Configuration for extracting values from tool responses and assigning
        them to dynamic variables.
      title: DynamicVariableAssignment
    type_:ConstantSchemaOverrideConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            description: Any type
        - type: object
          additionalProperties:
            description: Any type
      description: The constant value to use
      title: ConstantSchemaOverrideConstantValue
    type_conversationalAi/mcpServers/toolConfigs:McpToolConfigOverrideUpdateRequestModelInputOverridesValue:
      oneOf:
        - type: object
          properties:
            source:
              type: string
              enum:
                - constant
              description: 'Discriminator value: constant'
            constant_value:
              $ref: '#/components/schemas/type_:ConstantSchemaOverrideConstantValue'
              description: The constant value to use
          required:
            - source
            - constant_value
        - type: object
          properties:
            source:
              type: string
              enum:
                - dynamic_variable
              description: 'Discriminator value: dynamic_variable'
            dynamic_variable:
              type: string
              description: The name of the dynamic variable to use
          required:
            - source
            - dynamic_variable
        - type: object
          properties:
            source:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
            prompt:
              type: string
              description: >-
                Prompt override for the LLM. If not provided, the original
                schema description is used.
          required:
            - source
        - type: object
          properties:
            source:
              type: string
              enum:
                - omit
              description: 'Discriminator value: omit'
          required:
            - source
      discriminator:
        propertyName: source
      title: McpToolConfigOverrideUpdateRequestModelInputOverridesValue
    type_:UnitTestToolCallParameterEval:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - anything
              description: 'Discriminator value: anything'
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - exact
              description: 'Discriminator value: exact'
            expected_value:
              type: string
              description: The exact string value that the parameter must match.
          required:
            - type
            - expected_value
        - type: object
          properties:
            type:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
            description:
              type: string
              description: A description of the evaluation strategy to use for the test.
          required:
            - type
            - description
        - type: object
          properties:
            type:
              type: string
              enum:
                - regex
              description: 'Discriminator value: regex'
            pattern:
              type: string
              description: A regex pattern to match the agent's response against.
          required:
            - type
            - pattern
      discriminator:
        propertyName: type
      title: UnitTestToolCallParameterEval
    type_:UnitTestToolCallParameter:
      type: object
      properties:
        eval:
          $ref: '#/components/schemas/type_:UnitTestToolCallParameterEval'
        path:
          type: string
      required:
        - eval
        - path
      title: UnitTestToolCallParameter
    type_:ToolResponseMockConfigInput:
      type: object
      properties:
        parameter_conditions:
          type: array
          items:
            $ref: '#/components/schemas/type_:UnitTestToolCallParameter'
          description: If the list is empty, the mock will always activate.
        mock_result:
          type: string
          description: The return value the LLM sees when this mock is active.
        is_error:
          type: boolean
          default: false
          description: >-
            If true, the mock result is surfaced to the LLM as a tool error
            rather than a successful result.
      required:
        - mock_result
      title: ToolResponseMockConfigInput
    type_:McpApprovalPolicy:
      type: string
      enum:
        - auto_approve_all
        - require_approval_all
        - require_approval_per_tool
      default: require_approval_all
      description: Defines the MCP server-level approval policy for tool execution.
      title: McpApprovalPolicy
    type_:McpToolApprovalPolicy:
      type: string
      enum:
        - auto_approved
        - requires_approval
      default: requires_approval
      description: Defines the tool-level approval policy.
      title: McpToolApprovalPolicy
    type_:McpToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
          description: The name of the MCP tool
        tool_hash:
          type: string
          description: SHA256 hash of the tool's parameters and description
        approval_policy:
          $ref: '#/components/schemas/type_:McpToolApprovalPolicy'
          description: The approval policy for this tool
      required:
        - tool_name
        - tool_hash
      description: Model for storing tool approval hashes for per-tool approval.
      title: McpToolApprovalHash
    type_:McpServerTransport:
      type: string
      enum:
        - SSE
        - STREAMABLE_HTTP
      default: SSE
      description: Supported MCP server transport types.
      title: McpServerTransport
    type_:ConvAiSecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      description: Used to reference a secret from the agent's secret store.
      title: ConvAiSecretLocator
    type_:McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
      description: >-
        The URL of the MCP server, if this contains a secret please store as a
        workspace secret, otherwise store as a plain string. Must use https
      title: McpServerConfigOutputUrl
    type_:ConvAiUserSecretDbModel:
      type: object
      properties:
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
        id:
          type: string
      required:
        - name
        - encrypted_value
        - nonce
        - id
      description: >-
        User-specific secret model that are not shared with other users in a
        workspace.
      title: ConvAiUserSecretDbModel
    type_:McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
        - $ref: '#/components/schemas/type_:ConvAiUserSecretDbModel'
      description: >-
        The secret token (Authorization header) stored as a workspace secret or
        in-place secret
      title: McpServerConfigOutputSecretToken
    type_:ConvAiDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
      description: Used to reference a dynamic variable.
      title: ConvAiDynamicVariable
    type_:ConvAiEnvVarLocator:
      type: object
      properties:
        env_var_label:
          type: string
      required:
        - env_var_label
      description: Used to reference an environment variable by label.
      title: ConvAiEnvVarLocator
    type_:McpServerConfigOutputRequestHeadersValue:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
        - $ref: '#/components/schemas/type_:ConvAiDynamicVariable'
        - $ref: '#/components/schemas/type_:ConvAiEnvVarLocator'
      title: McpServerConfigOutputRequestHeadersValue
    type_:McpServerConfigOutputRequestMetaValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
        - $ref: '#/components/schemas/type_:ConvAiDynamicVariable'
        - $ref: '#/components/schemas/type_:ConvAiEnvVarLocator'
      title: McpServerConfigOutputRequestMetaValue
    type_:AuthConnectionLocator:
      type: object
      properties:
        auth_connection_id:
          type: string
      required:
        - auth_connection_id
      description: >-
        Used to reference an auth connection from the workspace's auth
        connection store.
      title: AuthConnectionLocator
    type_:EnvironmentAuthConnectionLocator:
      type: object
      properties:
        env_var_label:
          type: string
      required:
        - env_var_label
      description: |-
        References an environment variable of type 'auth_connection' by label.
        At runtime, resolves to the auth connection for the current environment,
        falling back to the default environment.
      title: EnvironmentAuthConnectionLocator
    type_:McpServerConfigOutputAuthConnection:
      oneOf:
        - $ref: '#/components/schemas/type_:AuthConnectionLocator'
        - $ref: '#/components/schemas/type_:EnvironmentAuthConnectionLocator'
      description: Optional auth connection to use for authentication with this MCP server
      title: McpServerConfigOutputAuthConnection
    type_:McpToolConfigOverrideOutputToolCallSound:
      oneOf:
        - $ref: '#/components/schemas/type_:ToolCallSoundType'
        - type: string
          enum:
            - 'off'
      description: >-
        Overrides the server's tool_call_sound setting for this tool. A sound
        name plays that sound; 'off' overrides to no sound (silence); null means
        do not override (inherit the server default).
      title: McpToolConfigOverrideOutputToolCallSound
    type_:McpToolConfigOverrideOutputInputOverridesValue:
      oneOf:
        - type: object
          properties:
            source:
              type: string
              enum:
                - constant
              description: 'Discriminator value: constant'
            constant_value:
              $ref: '#/components/schemas/type_:ConstantSchemaOverrideConstantValue'
              description: The constant value to use
          required:
            - source
            - constant_value
        - type: object
          properties:
            source:
              type: string
              enum:
                - dynamic_variable
              description: 'Discriminator value: dynamic_variable'
            dynamic_variable:
              type: string
              description: The name of the dynamic variable to use
          required:
            - source
            - dynamic_variable
        - type: object
          properties:
            source:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
            prompt:
              type: string
              description: >-
                Prompt override for the LLM. If not provided, the original
                schema description is used.
          required:
            - source
        - type: object
          properties:
            source:
              type: string
              enum:
                - omit
              description: 'Discriminator value: omit'
          required:
            - source
      discriminator:
        propertyName: source
      title: McpToolConfigOverrideOutputInputOverridesValue
    type_:ToolResponseMockConfigOutput:
      type: object
      properties:
        parameter_conditions:
          type: array
          items:
            $ref: '#/components/schemas/type_:UnitTestToolCallParameter'
          description: If the list is empty, the mock will always activate.
        mock_result:
          type: string
          description: The return value the LLM sees when this mock is active.
        is_error:
          type: boolean
          default: false
          description: >-
            If true, the mock result is surfaced to the LLM as a tool error
            rather than a successful result.
      required:
        - mock_result
      title: ToolResponseMockConfigOutput
    type_:McpToolConfigOverrideOutput:
      type: object
      properties:
        tool_name:
          type: string
          description: The name of the MCP tool
        force_pre_tool_speech:
          type: boolean
          description: >-
            DEPRECATED: use `pre_tool_speech` instead. If set, overrides the
            server's force_pre_tool_speech setting for this tool.
        pre_tool_speech:
          $ref: '#/components/schemas/type_:PreToolSpeechMode'
          description: >-
            If set, overrides the server's pre_tool_speech setting for this
            tool.
        disable_interruptions:
          type: boolean
          description: >-
            DEPRECATED: use `interruption_mode` instead. If set, overrides the
            server's disable_interruptions setting for this tool.
        interruption_mode:
          $ref: '#/components/schemas/type_:ToolInterruptionMode'
          description: >-
            If set, overrides the server's interruption_mode setting for this
            tool.
        tool_call_sound:
          $ref: '#/components/schemas/type_:McpToolConfigOverrideOutputToolCallSound'
          description: >-
            Overrides the server's tool_call_sound setting for this tool. A
            sound name plays that sound; 'off' overrides to no sound (silence);
            null means do not override (inherit the server default).
        tool_call_sound_behavior:
          $ref: '#/components/schemas/type_:ToolCallSoundBehavior'
          description: >-
            If set, overrides the server's tool_call_sound_behavior setting for
            this tool
        execution_mode:
          $ref: '#/components/schemas/type_:ToolExecutionMode'
          description: If set, overrides the server's execution_mode setting for this tool
        response_timeout_secs:
          type: integer
          description: >-
            If set, overrides the server's response timeout for this MCP tool
            (seconds).
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableAssignment'
          description: Dynamic variable assignments for this MCP tool
        input_overrides:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:McpToolConfigOverrideOutputInputOverridesValue
          description: Mapping of json path to input override configuration
        response_mocks:
          type: array
          items:
            $ref: '#/components/schemas/type_:ToolResponseMockConfigOutput'
          description: >-
            Mock responses with optional parameter conditions. Evaluated
            top-to-bottom; first match wins.
      required:
        - tool_name
      title: McpToolConfigOverrideOutput
    type_:McpServerConfigOutput:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/type_:McpApprovalPolicy'
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/type_:McpToolApprovalHash'
          description: >-
            List of tool approval hashes for per-tool approval when
            approval_policy is REQUIRE_APPROVAL_PER_TOOL
        transport:
          $ref: '#/components/schemas/type_:McpServerTransport'
          description: The transport type used to connect to the MCP server
        url:
          $ref: '#/components/schemas/type_:McpServerConfigOutputUrl'
          description: >-
            The URL of the MCP server, if this contains a secret please store as
            a workspace secret, otherwise store as a plain string. Must use
            https
        secret_token:
          $ref: '#/components/schemas/type_:McpServerConfigOutputSecretToken'
          description: >-
            The secret token (Authorization header) stored as a workspace secret
            or in-place secret
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:McpServerConfigOutputRequestHeadersValue
          description: The headers included in the request
        request_meta:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:McpServerConfigOutputRequestMetaValue'
          description: >-
            Entries sent in the MCP `_meta` field of tools/call requests. Values
            may be JSON scalars, or references to a workspace secret, dynamic
            variable, or environment variable resolved per call.
        auth_connection:
          $ref: '#/components/schemas/type_:McpServerConfigOutputAuthConnection'
          description: >-
            Optional auth connection to use for authentication with this MCP
            server
        name:
          type: string
        description:
          type: string
          default: ''
        force_pre_tool_speech:
          type: boolean
          default: false
          description: >-
            DEPRECATED: use `pre_tool_speech` instead. If true, all tools from
            this MCP server will require pre-tool execution speech.
        pre_tool_speech:
          $ref: '#/components/schemas/type_:PreToolSpeechMode'
          description: >-
            Controls whether the agent speaks before this tool is called. 'auto'
            (default) decides based on recent tool latency, 'force' always asks
            the agent to speak, 'off' fully opts out regardless of latency.
            Applies to every tool from this MCP server unless overridden per
            tool.
        disable_interruptions:
          type: boolean
          default: false
          description: >-
            DEPRECATED: use `interruption_mode` instead. If true, the user will
            not be able to interrupt the agent while any tool from this MCP
            server is running.
        interruption_mode:
          $ref: '#/components/schemas/type_:ToolInterruptionMode'
          description: >-
            Controls whether the user can interrupt the agent around this tool
            call. 'allow' (default) lets the user interrupt at any time,
            'disable_during_tool' suppresses interruptions only while the tool
            is running, 'disable_during_tool_and_turn' suppresses interruptions
            while the tool runs and for the agent response that follows it.
            Applies to every tool from this MCP server unless overridden per
            tool.
        tool_call_sound:
          $ref: '#/components/schemas/type_:ToolCallSoundType'
          description: >-
            Predefined tool call sound type to play during tool execution for
            all tools from this MCP server
        tool_call_sound_behavior:
          $ref: '#/components/schemas/type_:ToolCallSoundBehavior'
          description: >-
            Determines when the tool call sound should play for all tools from
            this MCP server
        execution_mode:
          $ref: '#/components/schemas/type_:ToolExecutionMode'
          description: >-
            Determines when and how all tools from this MCP server execute:
            'immediate' executes the tool right away when requested by the LLM,
            'post_tool_speech' waits for the agent to finish speaking before
            executing, 'async' runs the tool in the background without blocking
            - best for long-running operations.
        response_timeout_secs:
          type: integer
          default: 30
          description: >-
            The maximum time in seconds to wait for each MCP tool call to
            complete. Must be between 5 and 300 seconds (inclusive).
        tool_config_overrides:
          type: array
          items:
            $ref: '#/components/schemas/type_:McpToolConfigOverrideOutput'
          description: >-
            List of per-tool configuration overrides that override the
            server-level defaults for specific tools
        disable_compression:
          type: boolean
          default: false
          description: >-
            Whether to disable HTTP compression for this MCP server. Enable this
            if the server does not support compressed responses.
      required:
        - url
        - name
      title: McpServerConfigOutput
    type_:ResourceAccessInfoRole:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The role of the user making the request
      title: ResourceAccessInfoRole
    type_:ResourceAccessInfoAnonymousAccessLevelOverride:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: ResourceAccessInfoAnonymousAccessLevelOverride
    type_:ResourceAccessInfoAccessSource:
      type: string
      enum:
        - creator
        - explicit
        - workspace_admin
        - workspace_default
      title: ResourceAccessInfoAccessSource
    type_:ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
          description: Whether the user making the request is the creator of the agent
        creator_name:
          type: string
          description: Name of the agent's creator
        creator_email:
          type: string
          description: Email of the agent's creator
        role:
          $ref: '#/components/schemas/type_:ResourceAccessInfoRole'
          description: The role of the user making the request
        anonymous_access_level_override:
          $ref: >-
            #/components/schemas/type_:ResourceAccessInfoAnonymousAccessLevelOverride
          description: >-
            The access level for anonymous users. If None, the resource is not
            shared publicly.
        access_source:
          $ref: '#/components/schemas/type_:ResourceAccessInfoAccessSource'
          description: >-
            Why the requesting user has access to this resource. 'creator' =
            caller is the owner. 'explicit' = caller (or one of their workspace
            groups) is listed in role_to_group_ids beyond the workspace-wide
            everyone group. 'workspace_default' = the workspace-wide everyone
            group is listed in role_to_group_ids (every non-anon workspace
            member, including admins, sees this resource). 'workspace_admin' =
            caller is a workspace admin and the admin seat is the *only* path to
            access; reserved for docs nobody else can see. Lets the UI disclose
            why an admin-bypass viewer sees a doc that wasn't explicitly shared
            with them.
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
      title: ResourceAccessInfo
    type_:DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableAgentIdentifierAccessLevel
    type_:McpServerResponseModelDependentAgentsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              description: 'Discriminator value: available'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/type_:DependentAvailableAgentIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              description: 'Discriminator value: unknown'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
          required:
            - type
            - id
      discriminator:
        propertyName: type
      title: McpServerResponseModelDependentAgentsItem
    type_:McpServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type: string
      required:
        - created_at
      title: McpServerMetadataResponseModel
    type_:McpServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/type_:McpServerConfigOutput'
        access_info:
          $ref: '#/components/schemas/type_:ResourceAccessInfo'
          description: The access information of the MCP Server
        dependent_agents:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:McpServerResponseModelDependentAgentsItem
          description: List of agents that depend on this MCP Server.
        metadata:
          $ref: '#/components/schemas/type_:McpServerMetadataResponseModel'
          description: The metadata of the MCP Server
      required:
        - id
        - config
        - metadata
      description: Response model representing an MCP Server configuration.
      title: McpServerResponseModel
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "id": "id",
  "config": {
    "url": "url",
    "name": "name",
    "approval_policy": "auto_approve_all",
    "tool_approval_hashes": [
      {
        "tool_name": "tool_name",
        "tool_hash": "tool_hash"
      }
    ],
    "transport": "SSE",
    "secret_token": {
      "secret_id": "secret_id"
    },
    "request_headers": {
      "key": "value"
    },
    "request_meta": {
      "key": "value"
    },
    "auth_connection": {
      "auth_connection_id": "auth_connection_id"
    },
    "description": "description",
    "pre_tool_speech": "auto",
    "interruption_mode": "allow",
    "tool_call_sound": "typing",
    "tool_call_sound_behavior": "auto",
    "execution_mode": "immediate",
    "response_timeout_secs": 1,
    "tool_config_overrides": [
      {
        "tool_name": "tool_name",
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
    ],
    "disable_compression": true
  },
  "metadata": {
    "created_at": 1,
    "owner_user_id": "owner_user_id"
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "anonymous_access_level_override": "admin",
    "access_source": "creator"
  },
  "dependent_agents": [
    {
      "type": "available",
      "access_level": "admin",
      "created_at_unix_secs": 1,
      "id": "id",
      "name": "name",
      "referenced_resource_ids": [
        "referenced_resource_ids"
      ]
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.toolConfigs.update("mcp_server_id", "tool_name", {
        environment: "environment",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tool_configs.update(
    mcp_server_id="mcp_server_id",
    tool_name="tool_name",
    environment="environment",
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

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name?environment=environment"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name?environment=environment")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name?environment=environment")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name?environment=environment', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name?environment=environment");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name?environment=environment")! as URL,
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
