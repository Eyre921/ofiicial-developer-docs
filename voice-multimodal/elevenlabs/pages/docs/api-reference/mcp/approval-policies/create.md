---
title: "Create MCP server tool approval"
source: https://elevenlabs.io/docs/api-reference/mcp/approval-policies/create.md
path: docs/api-reference/mcp/approval-policies/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create MCP server tool approval

POST https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-approvals
Content-Type: application/json

Add approval for a specific MCP tool when using per-tool approval mode.

Reference: https://elevenlabs.io/docs/api-reference/mcp/approval-policies/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals:
    post:
      operationId: create
      summary: Create Mcp Server Tool Approval
      description: Add approval for a specific MCP tool when using per-tool approval mode.
      tags:
        - toolApprovals
      parameters:
        - name: mcp_server_id
          in: path
          description: ID of the MCP Server.
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/MCPServerResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MCPToolAddApprovalRequestModel'
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
    MCPToolApprovalPolicy:
      type: string
      enum:
        - auto_approved
        - requires_approval
      default: requires_approval
      description: Defines the tool-level approval policy.
      title: MCPToolApprovalPolicy
    MCPToolAddApprovalRequestModel:
      type: object
      properties:
        tool_name:
          type: string
          description: The name of the MCP tool
        tool_description:
          type: string
          description: The description of the MCP tool
        input_schema:
          type: object
          additionalProperties:
            description: Any type
          description: >-
            The input schema of the MCP tool (the schema defined on the MCP
            server before ElevenLabs does any extra processing)
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
          default: requires_approval
          description: The tool-level approval policy
      required:
        - tool_name
        - tool_description
      description: Request model for adding approval for a single MCP tool.
      title: MCPToolAddApprovalRequestModel
    MCPApprovalPolicy:
      type: string
      enum:
        - auto_approve_all
        - require_approval_all
        - require_approval_per_tool
      default: require_approval_all
      description: Defines the MCP server-level approval policy for tool execution.
      title: MCPApprovalPolicy
    MCPToolApprovalHash:
      type: object
      properties:
        tool_name:
          type: string
          description: The name of the MCP tool
        tool_hash:
          type: string
          description: SHA256 hash of the tool's parameters and description
        approval_policy:
          $ref: '#/components/schemas/MCPToolApprovalPolicy'
          default: requires_approval
          description: The approval policy for this tool
      required:
        - tool_name
        - tool_hash
      description: Model for storing tool approval hashes for per-tool approval.
      title: MCPToolApprovalHash
    MCPServerTransport:
      type: string
      enum:
        - SSE
        - STREAMABLE_HTTP
      default: SSE
      description: Supported MCP server transport types.
      title: MCPServerTransport
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      description: Used to reference a secret from the agent's secret store.
      title: ConvAISecretLocator
    McpServerConfigOutputUrl:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
      description: >-
        The URL of the MCP server, if this contains a secret please store as a
        workspace secret, otherwise store as a plain string. Must use https
      title: McpServerConfigOutputUrl
    ConvAIUserSecretDBModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        encrypted_value:
          type: string
        nonce:
          type: string
      required:
        - id
        - name
        - encrypted_value
        - nonce
      description: >-
        User-specific secret model that are not shared with other users in a
        workspace.
      title: ConvAIUserSecretDBModel
    McpServerConfigOutputSecretToken:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIUserSecretDBModel'
      description: >-
        The secret token (Authorization header) stored as a workspace secret or
        in-place secret
      title: McpServerConfigOutputSecretToken
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
      description: Used to reference a dynamic variable.
      title: ConvAIDynamicVariable
    ConvAIEnvVarLocator:
      type: object
      properties:
        env_var_label:
          type: string
      required:
        - env_var_label
      description: Used to reference an environment variable by label.
      title: ConvAIEnvVarLocator
    McpServerConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
        - $ref: '#/components/schemas/ConvAIEnvVarLocator'
      title: McpServerConfigOutputRequestHeaders
    AuthConnectionLocator:
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
    EnvironmentAuthConnectionLocator:
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
    McpServerConfigOutputAuthConnection:
      oneOf:
        - $ref: '#/components/schemas/AuthConnectionLocator'
        - $ref: '#/components/schemas/EnvironmentAuthConnectionLocator'
      description: Optional auth connection to use for authentication with this MCP server
      title: McpServerConfigOutputAuthConnection
    PreToolSpeechMode:
      type: string
      enum:
        - auto
        - force
        - 'off'
      default: auto
      title: PreToolSpeechMode
    ToolInterruptionMode:
      type: string
      enum:
        - allow
        - disable_during_tool
        - disable_during_tool_and_turn
      default: allow
      title: ToolInterruptionMode
    ToolCallSoundType:
      type: string
      enum:
        - typing
        - elevator1
        - elevator2
        - elevator3
        - elevator4
      description: Predefined tool call sounds; ``None`` means no sound.
      title: ToolCallSoundType
    ToolCallSoundBehavior:
      type: string
      enum:
        - auto
        - always
      default: auto
      description: Determines how the tool call sound should be played.
      title: ToolCallSoundBehavior
    ToolExecutionMode:
      type: string
      enum:
        - immediate
        - post_tool_speech
        - async
      default: immediate
      title: ToolExecutionMode
    McpToolConfigOverrideOutputToolCallSound:
      oneOf:
        - $ref: '#/components/schemas/ToolCallSoundType'
        - type: string
          enum:
            - 'off'
      description: >-
        Overrides the server's tool_call_sound setting for this tool. A sound
        name plays that sound; 'off' overrides to no sound (silence); null means
        do not override (inherit the server default).
      title: McpToolConfigOverrideOutputToolCallSound
    DynamicVariableAssignment:
      type: object
      properties:
        source:
          type: string
          enum:
            - response
          default: response
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
    McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValue:
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
      title: >-
        McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValue
    McpToolConfigOverrideOutputInputOverrides:
      oneOf:
        - type: object
          properties:
            source:
              type: string
              enum:
                - constant
              description: 'Discriminator value: constant'
            constant_value:
              $ref: >-
                #/components/schemas/McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValue
              description: The constant value to use
          required:
            - source
            - constant_value
          description: ConstantSchemaOverride variant
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
          description: DynamicVariableSchemaOverride variant
        - type: object
          properties:
            source:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
            prompt:
              type:
                - string
                - 'null'
              description: >-
                Prompt override for the LLM. If not provided, the original
                schema description is used.
          required:
            - source
          description: LLMSchemaOverride variant
        - type: object
          properties:
            source:
              type: string
              enum:
                - omit
              default: omit
          required:
            - source
          description: OmitSchemaOverride variant
      discriminator:
        propertyName: source
      title: McpToolConfigOverrideOutputInputOverrides
    UnitTestToolCallParameterEval:
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
          description: MatchAnythingParameterEvaluationStrategy variant
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
          description: ExactParameterEvaluationStrategy variant
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
          description: LLMParameterEvaluationStrategy variant
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
          description: RegexParameterEvaluationStrategy variant
      discriminator:
        propertyName: type
      title: UnitTestToolCallParameterEval
    UnitTestToolCallParameter:
      type: object
      properties:
        eval:
          $ref: '#/components/schemas/UnitTestToolCallParameterEval'
        path:
          type: string
      required:
        - eval
        - path
      title: UnitTestToolCallParameter
    ToolResponseMockConfig-Output:
      type: object
      properties:
        parameter_conditions:
          type: array
          items:
            $ref: '#/components/schemas/UnitTestToolCallParameter'
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
      title: ToolResponseMockConfig-Output
    MCPToolConfigOverride-Output:
      type: object
      properties:
        tool_name:
          type: string
          description: The name of the MCP tool
        force_pre_tool_speech:
          type:
            - boolean
            - 'null'
          description: >-
            DEPRECATED: use `pre_tool_speech` instead. If set, overrides the
            server's force_pre_tool_speech setting for this tool.
        pre_tool_speech:
          oneOf:
            - $ref: '#/components/schemas/PreToolSpeechMode'
            - type: 'null'
          description: >-
            If set, overrides the server's pre_tool_speech setting for this
            tool.
        disable_interruptions:
          type:
            - boolean
            - 'null'
          description: >-
            DEPRECATED: use `interruption_mode` instead. If set, overrides the
            server's disable_interruptions setting for this tool.
        interruption_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolInterruptionMode'
            - type: 'null'
          description: >-
            If set, overrides the server's interruption_mode setting for this
            tool.
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/McpToolConfigOverrideOutputToolCallSound'
            - type: 'null'
          description: >-
            Overrides the server's tool_call_sound setting for this tool. A
            sound name plays that sound; 'off' overrides to no sound (silence);
            null means do not override (inherit the server default).
        tool_call_sound_behavior:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundBehavior'
            - type: 'null'
          description: >-
            If set, overrides the server's tool_call_sound_behavior setting for
            this tool
        execution_mode:
          oneOf:
            - $ref: '#/components/schemas/ToolExecutionMode'
            - type: 'null'
          description: If set, overrides the server's execution_mode setting for this tool
        response_timeout_secs:
          type:
            - integer
            - 'null'
          description: >-
            If set, overrides the server's response timeout for this MCP tool
            (seconds).
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/DynamicVariableAssignment'
          description: Dynamic variable assignments for this MCP tool
        input_overrides:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/McpToolConfigOverrideOutputInputOverrides'
          description: Mapping of json path to input override configuration
        response_mocks:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ToolResponseMockConfig-Output'
          description: >-
            Mock responses with optional parameter conditions. Evaluated
            top-to-bottom; first match wins.
      required:
        - tool_name
      title: MCPToolConfigOverride-Output
    MCPServerConfig-Output:
      type: object
      properties:
        approval_policy:
          $ref: '#/components/schemas/MCPApprovalPolicy'
          default: require_approval_all
        tool_approval_hashes:
          type: array
          items:
            $ref: '#/components/schemas/MCPToolApprovalHash'
          description: >-
            List of tool approval hashes for per-tool approval when
            approval_policy is REQUIRE_APPROVAL_PER_TOOL
        transport:
          $ref: '#/components/schemas/MCPServerTransport'
          default: SSE
          description: The transport type used to connect to the MCP server
        url:
          $ref: '#/components/schemas/McpServerConfigOutputUrl'
          description: >-
            The URL of the MCP server, if this contains a secret please store as
            a workspace secret, otherwise store as a plain string. Must use
            https
        secret_token:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputSecretToken'
            - type: 'null'
          description: >-
            The secret token (Authorization header) stored as a workspace secret
            or in-place secret
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/McpServerConfigOutputRequestHeaders'
          description: The headers included in the request
        auth_connection:
          oneOf:
            - $ref: '#/components/schemas/McpServerConfigOutputAuthConnection'
            - type: 'null'
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
          $ref: '#/components/schemas/PreToolSpeechMode'
          default: auto
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
          $ref: '#/components/schemas/ToolInterruptionMode'
          default: allow
          description: >-
            Controls whether the user can interrupt the agent around this tool
            call. 'allow' (default) lets the user interrupt at any time,
            'disable_during_tool' suppresses interruptions only while the tool
            is running, 'disable_during_tool_and_turn' suppresses interruptions
            while the tool runs and for the agent response that follows it.
            Applies to every tool from this MCP server unless overridden per
            tool.
        tool_call_sound:
          oneOf:
            - $ref: '#/components/schemas/ToolCallSoundType'
            - type: 'null'
          description: >-
            Predefined tool call sound type to play during tool execution for
            all tools from this MCP server
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
          default: auto
          description: >-
            Determines when the tool call sound should play for all tools from
            this MCP server
        execution_mode:
          $ref: '#/components/schemas/ToolExecutionMode'
          default: immediate
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
            $ref: '#/components/schemas/MCPToolConfigOverride-Output'
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
      title: MCPServerConfig-Output
    ResourceAccessInfoRole:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The role of the user making the request
      title: ResourceAccessInfoRole
    ResourceAccessInfoAnonymousAccessLevelOverride:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: >-
        The access level for anonymous users. If None, the resource is not
        shared publicly.
      title: ResourceAccessInfoAnonymousAccessLevelOverride
    ResourceAccessInfoAccessSource:
      type: string
      enum:
        - creator
        - explicit
        - workspace_admin
        - workspace_default
      description: >-
        Why the requesting user has access to this resource. 'creator' = caller
        is the owner. 'explicit' = caller (or one of their workspace groups) is
        listed in role_to_group_ids beyond the workspace-wide everyone group.
        'workspace_default' = the workspace-wide everyone group is listed in
        role_to_group_ids (every non-anon workspace member, including admins,
        sees this resource). 'workspace_admin' = caller is a workspace admin and
        the admin seat is the *only* path to access; reserved for docs nobody
        else can see. Lets the UI disclose why an admin-bypass viewer sees a doc
        that wasn't explicitly shared with them.
      title: ResourceAccessInfoAccessSource
    ResourceAccessInfo:
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
          $ref: '#/components/schemas/ResourceAccessInfoRole'
          description: The role of the user making the request
        anonymous_access_level_override:
          oneOf:
            - $ref: >-
                #/components/schemas/ResourceAccessInfoAnonymousAccessLevelOverride
            - type: 'null'
          description: >-
            The access level for anonymous users. If None, the resource is not
            shared publicly.
        access_source:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfoAccessSource'
            - type: 'null'
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
    V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: >-
        V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel
    McpServerResponseModelDependentAgentsItems:
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
                #/components/schemas/V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
          description: DependentAvailableAgentIdentifier variant
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
          description: |-
            A model that represents an agent dependent on a knowledge base/tools
            to which the user has no direct access.
      discriminator:
        propertyName: type
      title: McpServerResponseModelDependentAgentsItems
    MCPServerMetadataResponseModel:
      type: object
      properties:
        created_at:
          type: integer
        owner_user_id:
          type:
            - string
            - 'null'
      required:
        - created_at
      title: MCPServerMetadataResponseModel
    MCPServerResponseModel:
      type: object
      properties:
        id:
          type: string
        config:
          $ref: '#/components/schemas/MCPServerConfig-Output'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
          description: The access information of the MCP Server
        dependent_agents:
          type: array
          items:
            $ref: '#/components/schemas/McpServerResponseModelDependentAgentsItems'
          description: List of agents that depend on this MCP Server.
        metadata:
          $ref: '#/components/schemas/MCPServerMetadataResponseModel'
          description: The metadata of the MCP Server
      required:
        - id
        - config
        - metadata
      description: Response model representing an MCP Server configuration.
      title: MCPServerResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

## Examples



**Request**

```json
{
  "tool_name": "string",
  "tool_description": "string"
}
```

**Response**

```json
{
  "id": "string",
  "config": {
    "url": "string",
    "name": "string",
    "approval_policy": "require_approval_all",
    "tool_approval_hashes": [
      {
        "tool_name": "string",
        "tool_hash": "string",
        "approval_policy": "requires_approval"
      }
    ],
    "transport": "SSE",
    "secret_token": {
      "secret_id": "string"
    },
    "request_headers": {},
    "auth_connection": {
      "auth_connection_id": "string"
    },
    "description": "",
    "pre_tool_speech": "auto",
    "interruption_mode": "allow",
    "tool_call_sound": "typing",
    "tool_call_sound_behavior": "auto",
    "execution_mode": "immediate",
    "response_timeout_secs": 30,
    "tool_config_overrides": [
      {
        "tool_name": "string",
        "pre_tool_speech": "auto",
        "interruption_mode": "allow",
        "tool_call_sound": "typing",
        "tool_call_sound_behavior": "auto",
        "execution_mode": "immediate",
        "response_timeout_secs": 1,
        "assignments": [
          {
            "dynamic_variable": "string",
            "value_path": "string",
            "source": "response",
            "sanitize": false,
            "preserve_native_type": false
          }
        ],
        "input_overrides": {},
        "response_mocks": [
          {
            "mock_result": "string",
            "parameter_conditions": [
              {
                "eval": {
                  "description": "string",
                  "type": "string"
                },
                "path": "string"
              }
            ],
            "is_error": false
          }
        ],
        "force_pre_tool_speech": true,
        "disable_interruptions": true
      }
    ],
    "disable_compression": false,
    "force_pre_tool_speech": false,
    "disable_interruptions": false
  },
  "metadata": {
    "created_at": 1,
    "owner_user_id": "string"
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "access_source": "creator"
  },
  "dependent_agents": [
    {
      "type": "available",
      "access_level": "admin",
      "created_at_unix_secs": 1,
      "id": "string",
      "name": "string",
      "referenced_resource_ids": [
        "string"
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
    await client.conversationalAi.mcpServers.toolApprovals.create("mcp_server_id", {
        toolName: "string",
        toolDescription: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tool_approvals.create(
    mcp_server_id="mcp_server_id",
    tool_name="string",
    tool_description="string",
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

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals"

	payload := strings.NewReader("{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")
  .header("Content-Type", "application/json")
  .body("{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals', [
  'body' => '{
  "tool_name": "string",
  "tool_description": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "tool_name": "string",
  "tool_description": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")! as URL,
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
