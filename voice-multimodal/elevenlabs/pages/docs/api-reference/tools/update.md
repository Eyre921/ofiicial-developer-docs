---
title: "Update tool"
source: https://elevenlabs.io/docs/api-reference/tools/update.md
path: docs/api-reference/tools/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update tool

PATCH https://api.elevenlabs.io/v1/convai/tools/{tool_id}
Content-Type: application/json

Update tool that is available in the workspace.

Reference: https://elevenlabs.io/docs/api-reference/tools/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/tools/{tool_id}:
    patch:
      operationId: update
      summary: Update Tool
      description: Update tool that is available in the workspace.
      tags:
        - tools
      parameters:
        - name: tool_id
          in: path
          description: ID of the requested tool.
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
                $ref: '#/components/schemas/ToolResponseModel'
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
              $ref: '#/components/schemas/ToolRequestModel'
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
    ToolInterruptionMode:
      type: string
      enum:
        - allow
        - disable_during_tool
        - disable_during_tool_and_turn
      default: allow
      title: ToolInterruptionMode
    PreToolSpeechMode:
      type: string
      enum:
        - auto
        - force
        - 'off'
      default: auto
      title: PreToolSpeechMode
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
    ToolErrorHandlingMode:
      type: string
      enum:
        - auto
        - summarized
        - passthrough
        - hide
      default: auto
      description: >-
        Controls how tool errors are processed before being shared with the
        agent.
      title: ToolErrorHandlingMode
    LiteralJsonSchemaPropertyType0:
      type: string
      enum:
        - boolean
        - string
        - integer
        - number
      title: LiteralJsonSchemaPropertyType0
    LiteralJsonSchemaPropertyType:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaPropertyType0'
        - type: array
          items:
            type: string
      title: LiteralJsonSchemaPropertyType
    LiteralJsonSchemaPropertyConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
      description: >-
        A constant value to use for this property. Mutually exclusive with
        description, dynamic_variable, is_system_provided, and is_omitted.
      title: LiteralJsonSchemaPropertyConstantValue
    LiteralJsonSchemaProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyType'
        description:
          type: string
          default: ''
          description: >-
            The description of the property. When set, the LLM will provide the
            value based on this description. Mutually exclusive with
            dynamic_variable, is_system_provided, constant_value, and
            is_omitted.
        enum:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of allowed string values for string type parameters
        is_system_provided:
          type: boolean
          default: false
          description: >-
            If true, the value will be populated by the system at runtime. Used
            by API Integration Webhook tools for templating. Mutually exclusive
            with description, dynamic_variable, constant_value, and is_omitted.
        dynamic_variable:
          type: string
          default: ''
          description: >-
            The name of the dynamic variable to use for this property's value.
            Mutually exclusive with description, is_system_provided,
            constant_value, and is_omitted.
        allowed_values_dynamic_variable:
          type: string
          default: ''
          description: >-
            When set, the LLM provides the value but the runtime rejects any
            value not present in the list held by this dynamic variable. Use to
            let the LLM pick from a server-verified set (e.g. the IDs the
            current user is allowed to access). Requires description; mutually
            exclusive with dynamic_variable, is_system_provided, constant_value,
            and is_omitted.
        constant_value:
          $ref: '#/components/schemas/LiteralJsonSchemaPropertyConstantValue'
          default: ''
          description: >-
            A constant value to use for this property. Mutually exclusive with
            description, dynamic_variable, is_system_provided, and is_omitted.
        is_omitted:
          type: boolean
          default: false
          description: >-
            If true, this parameter will be completely omitted from the request.
            Only valid for optional parameters. Mutually exclusive with
            description, dynamic_variable, is_system_provided, and
            constant_value.
      required:
        - type
      description: >-
        Schema property for literal JSON types. IMPORTANT: Only ONE of the
        following fields can be set: description (LLM provides value),
        dynamic_variable (value from variable), is_system_provided (system
        provides value), constant_value (fixed value), or is_omitted (parameter
        is omitted). These are mutually exclusive.
      title: LiteralJsonSchemaProperty
    ArrayJsonSchemaPropertyInputItems:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Input'
      description: Schema for array elements.
      title: ArrayJsonSchemaPropertyInputItems
    ArrayJsonSchemaPropertyInputConstantValueItems:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
      title: ArrayJsonSchemaPropertyInputConstantValueItems
    ArrayJsonSchemaProperty-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - array
          default: array
        description:
          type: string
          default: ''
        items:
          $ref: '#/components/schemas/ArrayJsonSchemaPropertyInputItems'
          default:
            allowed_values_dynamic_variable: ''
            constant_value: ''
            description: Array element
            dynamic_variable: ''
            is_omitted: false
            is_system_provided: false
            type: string
          description: Schema for array elements.
        dynamic_variable:
          type: string
          default: ''
          description: >-
            When set, the entire array is populated from this dynamic variable
            at runtime. Mutually exclusive with description (LLM-provided
            array), constant_value, and is_omitted.
        constant_value:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/ArrayJsonSchemaPropertyInputConstantValueItems
          description: >-
            When set, the entire array uses this constant value at runtime.
            Mutually exclusive with description (LLM-provided array),
            dynamic_variable, and is_omitted.
        is_omitted:
          type: boolean
          default: false
          description: >-
            If true, this array parameter will be completely omitted from the
            request. Only valid for optional parameters. Mutually exclusive with
            description, dynamic_variable, and constant_value.
      title: ArrayJsonSchemaProperty-Input
    ObjectJsonSchemaPropertyInput:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Input'
      title: ObjectJsonSchemaPropertyInput
    RequiredConstraint:
      type: object
      properties:
        required:
          type: array
          items:
            type: string
      required:
        - required
      description: A set of fields that must all be present to satisfy this constraint.
      title: RequiredConstraint
    RequiredConstraints:
      type: object
      properties:
        any_of:
          type: array
          items:
            $ref: '#/components/schemas/RequiredConstraint'
        all_of:
          type: array
          items:
            $ref: '#/components/schemas/RequiredConstraint'
      description: >-
        Wrapper for anyOf/allOf composition constraints scoped to required
        fields.
      title: RequiredConstraints
    ObjectJsonSchemaProperty-Input:
      type: object
      properties:
        type:
          type: string
          enum:
            - object
          default: object
        required:
          type: array
          items:
            type: string
        description:
          type: string
          default: ''
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ObjectJsonSchemaPropertyInput'
        required_constraints:
          oneOf:
            - $ref: '#/components/schemas/RequiredConstraints'
            - type: 'null'
      title: ObjectJsonSchemaProperty-Input
    DynamicVariablesConfig:
      type: object
      properties:
        dynamic_variable_placeholders:
          type: object
          additionalProperties:
            description: Any type
          description: A dictionary of dynamic variable placeholders and their values
      title: DynamicVariablesConfig
    ToolExecutionMode:
      type: string
      enum:
        - immediate
        - post_tool_speech
        - async
      default: immediate
      title: ToolExecutionMode
    ProcedureType:
      type: string
      enum:
        - free_form
        - deterministic
      default: free_form
      title: ProcedureType
    GuardrailExecutionMode:
      type: string
      enum:
        - streaming
        - blocking
      default: streaming
      title: GuardrailExecutionMode
    CustomGuardrailConfigModel:
      type: string
      enum:
        - gemini-2.5-flash-lite
        - gemini-2.5-flash
        - gemini-3.1-flash-lite
        - gemini-3.5-flash
        - claude-haiku-4-5
        - claude-sonnet-4-6
        - gpt-5.4-nano
        - gpt-5.4-mini
      default: gemini-2.5-flash-lite
      description: LLM model to use for custom guardrail evaluation
      title: CustomGuardrailConfigModel
    CustomGuardrailConfigTriggerAction:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - end_call
              default: end_call
          required:
            - type
          description: EndCallTriggerAction variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - retry
              default: retry
            feedback:
              type: string
              default: >-
                Your response was blocked by a guardrail that blocks content
                that matches this condition/category: '{{trigger_reason}}'
                During your next turn you must tell the user "I'm sorry but I
                can't answer that question, would you like to know something
                else?".
              description: >-
                Custom feedback to inject into the agent when retrying after
                guardrail trigger.
          required:
            - type
          description: RetryTriggerAction variant
      discriminator:
        propertyName: type
      title: CustomGuardrailConfigTriggerAction
    CustomGuardrailConfig:
      type: object
      properties:
        is_enabled:
          type: boolean
          default: false
        name:
          type: string
          description: User-facing name for this guardrail
        prompt:
          type: string
          description: >-
            Instruction describing what to block, e.g. 'don't talk about
            politics'
        execution_mode:
          $ref: '#/components/schemas/GuardrailExecutionMode'
          default: streaming
        model:
          $ref: '#/components/schemas/CustomGuardrailConfigModel'
          default: gemini-2.5-flash-lite
          description: LLM model to use for custom guardrail evaluation
        history_message_count:
          type: integer
          default: 0
          description: >-
            How much recent history the guardrail sees before the reply it
            evaluates, counted in user messages (the agent replies between them
            are included too). The guardrail always gets a single
            <conversation_history> transcript ending in the evaluated reply,
            marked 'AGENT [current reply]:'. 0 (default) adds no prior history
            (just that line); 1 adds the latest user message onward.
        trigger_action:
          $ref: '#/components/schemas/CustomGuardrailConfigTriggerAction'
      required:
        - name
        - prompt
      description: Single custom guardrail configuration
      title: CustomGuardrailConfig
    ProcedureAtVersion-Input:
      type: object
      properties:
        procedure_id:
          type: string
          description: Procedure ID
        name:
          type: string
          description: Procedure name
        type:
          $ref: '#/components/schemas/ProcedureType'
          default: free_form
        content:
          type: string
          description: Procedure content
        guardrails:
          type: array
          items:
            $ref: '#/components/schemas/CustomGuardrailConfig'
        agent_id:
          type: string
          description: Agent ID of the procedure
        version_id:
          type:
            - string
            - 'null'
          description: >-
            Version ID of a version of the procedure. None for a procedure never
            versioned.
      required:
        - procedure_id
        - name
        - content
        - agent_id
      title: ProcedureAtVersion-Input
    SubAgent-Input:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
        description:
          type: string
        parameters:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
            - type: 'null'
      required:
        - agent_id
        - description
      title: SubAgent-Input
    AgentTransfer-Input:
      type: object
      properties:
        agent_id:
          type:
            - string
            - 'null'
        node_id:
          type:
            - string
            - 'null'
        condition:
          type: string
        delay_ms:
          type: integer
          default: 0
        transfer_message:
          type:
            - string
            - 'null'
        enable_transferred_agent_first_message:
          type: boolean
          default: false
        is_workflow_node_transfer:
          type: boolean
          default: false
        preserve_client_tts_overrides:
          type: boolean
          default: false
          description: >-
            Defines whether TTS client overrides should be carried over to the
            transferred agent.
      required:
        - condition
      title: AgentTransfer-Input
    PhoneNumberTransferCustomSipHeadersItems:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - dynamic
              description: 'Discriminator value: dynamic'
            key:
              type: string
              description: The SIP header name (e.g., 'X-Customer-ID')
            value:
              type: string
              description: The dynamic variable name to resolve
          required:
            - type
            - key
            - value
          description: >-
            Custom SIP header for phone transfers with a dynamic variable
            reference.

            The value is a variable name that will be resolved at runtime.

            Value is not validated here since it will be substituted with actual
            value later.
        - type: object
          properties:
            type:
              type: string
              enum:
                - static
              description: 'Discriminator value: static'
            key:
              type: string
              description: The SIP header name (e.g., 'X-Customer-ID')
            value:
              type: string
              description: The header value
          required:
            - type
            - key
            - value
          description: >-
            Custom SIP header for phone transfers with a static (validated)
            value.
      discriminator:
        propertyName: type
      title: PhoneNumberTransferCustomSipHeadersItems
    PhoneNumberTransferTransferDestination:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - phone
              description: 'Discriminator value: phone'
            phone_number:
              type: string
          required:
            - type
            - phone_number
          description: PhoneNumberTransferDestination variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - phone_dynamic_variable
              description: 'Discriminator value: phone_dynamic_variable'
            phone_number:
              type: string
          required:
            - type
            - phone_number
          description: PhoneNumberDynamicVariableTransferDestination variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - sip_uri
              description: 'Discriminator value: sip_uri'
            sip_uri:
              type: string
          required:
            - type
            - sip_uri
          description: SIPUriTransferDestination variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - sip_uri_dynamic_variable
              description: 'Discriminator value: sip_uri_dynamic_variable'
            sip_uri:
              type: string
          required:
            - type
            - sip_uri
          description: SIPUriDynamicVariableTransferDestination variant
      discriminator:
        propertyName: type
      title: PhoneNumberTransferTransferDestination
    TransferTypeEnum:
      type: string
      enum:
        - blind
        - conference
        - sip_refer
      default: conference
      title: TransferTypeEnum
    UuiTransferConfigProtocolDiscriminatorMode:
      type: string
      enum:
        - prefix
        - pd_parameter
      default: prefix
      description: >-
        How to attach protocol_discriminator. 'prefix' prepends the octet to the
        hex payload (User-to-User=XX<hex>;encoding=hex). 'pd_parameter' sends it
        as a separate parameter (User-to-User=<hex>;pd=XX;encoding=hex). Ignored
        when protocol_discriminator is unset.
      title: UuiTransferConfigProtocolDiscriminatorMode
    UUITransferConfig:
      type: object
      properties:
        data:
          type: string
          description: >-
            UUI payload to send on SIP REFER transfers. Supports inline dynamic
            variables and is hex-encoded at transfer time.
        protocol_discriminator:
          type:
            - string
            - 'null'
          description: >-
            Optional one-octet protocol discriminator (two hex digits, e.g.
            '00'). Required by platforms such as Genesys Cloud, which otherwise
            strip the first octet of the payload. Leave unset for platforms like
            Talkdesk that expect a bare hex payload.
        protocol_discriminator_mode:
          $ref: '#/components/schemas/UuiTransferConfigProtocolDiscriminatorMode'
          default: prefix
          description: >-
            How to attach protocol_discriminator. 'prefix' prepends the octet to
            the hex payload (User-to-User=XX<hex>;encoding=hex). 'pd_parameter'
            sends it as a separate parameter
            (User-to-User=<hex>;pd=XX;encoding=hex). Ignored when
            protocol_discriminator is unset.
      required:
        - data
      description: >-
        User-to-User Information envelope for SIP REFER transfers (RFC 7433).


        Outbound payloads are hex-encoded (the only encoding RFC 7433 defines).
        The

        protocol discriminator axis lets per-platform formats (Talkdesk,
        Genesys, ...)

        be expressed by configuration rather than scattered transfer flags.
        Further

        axes (ASCII encoding, header name, purpose/content parameters) can be
        added

        here without touching the transfer model.
      title: UUITransferConfig
    PhoneNumberTransferPostDialDigits:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - dynamic
              description: 'Discriminator value: dynamic'
            value:
              type: string
              description: The dynamic variable name to resolve
          required:
            - type
            - value
          description: PostDialDigitsDynamicVariable variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - static
              description: 'Discriminator value: static'
            value:
              type: string
              description: >-
                DTMF digits to send after call connects (e.g., 'ww1234' for
                extension)
          required:
            - type
            - value
          description: PostDialDigitsStatic variant
      discriminator:
        propertyName: type
      description: >-
        DTMF digits to send after call connects (e.g., 'ww1234' for extension).
        Can be either a static value or a dynamic variable reference. Use 'w'
        for 0.5s pause. Only supported for Twilio transfers.
      title: PhoneNumberTransferPostDialDigits
    PhoneNumberTransfer:
      type: object
      properties:
        custom_sip_headers:
          type: array
          items:
            $ref: '#/components/schemas/PhoneNumberTransferCustomSipHeadersItems'
          description: >-
            Custom SIP headers to include when transferring the call. Each
            header can be either a static value or a dynamic variable reference.
        transfer_destination:
          $ref: '#/components/schemas/PhoneNumberTransferTransferDestination'
        transfer_type:
          $ref: '#/components/schemas/TransferTypeEnum'
          default: conference
        uui:
          oneOf:
            - $ref: '#/components/schemas/UUITransferConfig'
            - type: 'null'
          description: >-
            User-to-User Information (RFC 7433) to attach to SIP REFER
            transfers. Carries call context such as CRM identifiers or
            escalation reason across the transfer boundary.
        post_dial_digits:
          oneOf:
            - $ref: '#/components/schemas/PhoneNumberTransferPostDialDigits'
            - type: 'null'
          description: >-
            DTMF digits to send after call connects (e.g., 'ww1234' for
            extension). Can be either a static value or a dynamic variable
            reference. Use 'w' for 0.5s pause. Only supported for Twilio
            transfers.
        phone_number:
          type:
            - string
            - 'null'
        condition:
          type: string
      required:
        - transfer_destination
        - condition
      title: PhoneNumberTransfer
    ToolRequestModelToolConfigDiscriminatorMappingSystemParams:
      oneOf:
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - end_call
              description: 'Discriminator value: end_call'
          required:
            - system_tool_type
          description: EndCallToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - end_procedure
              description: 'Discriminator value: end_procedure'
            procedures:
              type: object
              additionalProperties:
                $ref: '#/components/schemas/ProcedureAtVersion-Input'
          required:
            - system_tool_type
          description: EndProcedureToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - knowledge_base_rag
              description: 'Discriminator value: knowledge_base_rag'
          required:
            - system_tool_type
          description: KnowledgeBaseRagToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - language_detection
              description: 'Discriminator value: language_detection'
          required:
            - system_tool_type
          description: LanguageDetectionToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - play_keypad_touch_tone
              description: 'Discriminator value: play_keypad_touch_tone'
            use_out_of_band_dtmf:
              type: boolean
              default: true
              description: >-
                Send DTMF tones as out-of-band RTP events (RFC 4733) instead of
                in-band audio. Only effective for SIP trunk imported numbers.
            suppress_turn_after_dtmf:
              type: boolean
              default: false
              description: >-
                If true, the agent will not generate further speech after
                playing DTMF tones. This prevents the agent's speech from
                interfering with IVR systems.
          required:
            - system_tool_type
          description: >-
            Allows the agent to play DTMF tones during a phone call.


            This tool can be used to interact with automated phone systems, such
            as

            navigating phone menus, entering extensions, or inputting numeric
            codes.
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - run_subagent
              description: 'Discriminator value: run_subagent'
            agents:
              type: array
              items:
                $ref: '#/components/schemas/SubAgent-Input'
          required:
            - system_tool_type
            - agents
          description: RunSubagentToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - skip_turn
              description: 'Discriminator value: skip_turn'
          required:
            - system_tool_type
          description: >-
            Allows the agent to explicitly skip its turn.


            This tool should be invoked by the LLM when the user indicates they
            would like

            to think or take a short pause before continuing the
            conversation—e.g. when

            they say: "Give me a second", "Let me think", or "One moment
            please".  After

            calling this tool, the assistant should not speak until the user
            speaks

            again, or another normal turn-taking condition is met.  The tool
            itself has

            no parameters and performs no side-effects other than informing the
            backend

            that the current turn generation is complete.
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - start_procedure
              description: 'Discriminator value: start_procedure'
            procedures:
              type: object
              additionalProperties:
                $ref: '#/components/schemas/ProcedureAtVersion-Input'
          required:
            - system_tool_type
          description: StartProcedureToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - transfer_to_agent
              default: transfer_to_agent
            transfers:
              type: array
              items:
                $ref: '#/components/schemas/AgentTransfer-Input'
          required:
            - system_tool_type
            - transfers
          description: TransferToAgentToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - transfer_to_number
              default: transfer_to_number
            transfers:
              type: array
              items:
                $ref: '#/components/schemas/PhoneNumberTransfer'
            enable_client_message:
              type: boolean
              default: true
              description: >-
                Whether to play a message to the client while they wait for
                transfer. Defaults to true for backward compatibility.
          required:
            - system_tool_type
            - transfers
          description: TransferToNumberToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - voicemail_detection
              default: voicemail_detection
            voicemail_message:
              type:
                - string
                - 'null'
              description: >-
                Optional message to leave on voicemail when detected. If not
                provided, the call will end immediately when voicemail is
                detected. Supports dynamic variables (e.g., {{system__time}},
                {{system__call_duration_secs}}, {{custom_variable}}).
          required:
            - system_tool_type
          description: >-
            Allows the agent to detect when a voicemail system is encountered.


            This tool should be invoked by the LLM when it detects that the call
            has been

            answered by a voicemail system rather than a human. If a voicemail
            message

            is configured, it will be played; otherwise the call will end
            immediately.
      discriminator:
        propertyName: system_tool_type
      title: ToolRequestModelToolConfigDiscriminatorMappingSystemParams
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      description: Used to reference a secret from the agent's secret store.
      title: ConvAISecretLocator
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
    WebhookToolApiSchemaConfigInputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
        - $ref: '#/components/schemas/ConvAIEnvVarLocator'
      title: WebhookToolApiSchemaConfigInputRequestHeaders
    WebhookToolApiSchemaConfigInputMethod:
      type: string
      enum:
        - GET
        - POST
        - PUT
        - PATCH
        - DELETE
      default: GET
      description: The HTTP method to use for the webhook
      title: WebhookToolApiSchemaConfigInputMethod
    QueryParamsJsonSchema:
      type: object
      properties:
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        required:
          type: array
          items:
            type: string
      required:
        - properties
      title: QueryParamsJsonSchema
    ResponseFilterMode:
      type: string
      enum:
        - all
        - allow
        - hide_all
      default: all
      description: >-
        Controls how tool responses are filtered before being visible to the
        agent.
      title: ResponseFilterMode
    ResponseFilter:
      type: object
      properties:
        mode:
          $ref: '#/components/schemas/ResponseFilterMode'
          default: all
          description: >-
            Controls how tool responses are filtered. 'all' returns entire
            response, 'allow' returns only specified paths, 'hide_all' hides the
            entire response.
        filters:
          type: array
          items:
            type: string
          description: >-
            Dot notation paths to include when mode is 'allow' (e.g.,
            ['ticket.id', 'ticket.status']).
        content_type:
          type: string
          enum:
            - application/json
          default: application/json
          description: >-
            Content type for response filtering. Only 'application/json'
            responses are filtered.
      description: >-
        Configuration for filtering tool responses before they are visible to
        the agent.
      title: ResponseFilter
    WebhookToolApiSchemaConfigInputContentType:
      type: string
      enum:
        - application/json
        - application/x-www-form-urlencoded
      default: application/json
      description: >-
        Content type for the request body. Only applies to POST/PUT/PATCH
        requests.
      title: WebhookToolApiSchemaConfigInputContentType
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
    WebhookToolApiSchemaConfigInputAuthConnection:
      oneOf:
        - $ref: '#/components/schemas/AuthConnectionLocator'
        - $ref: '#/components/schemas/EnvironmentAuthConnectionLocator'
      description: Optional auth connection to use for authentication with this webhook
      title: WebhookToolApiSchemaConfigInputAuthConnection
    WebhookToolApiSchemaConfig-Input:
      type: object
      properties:
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WebhookToolApiSchemaConfigInputRequestHeaders'
          description: Headers that should be included in the request
        url:
          type: string
          description: >-
            The URL that the webhook will be sent to. May include path
            parameters, e.g. https://example.com/agents/{agent_id}
        method:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfigInputMethod'
          default: GET
          description: The HTTP method to use for the webhook
        path_params_schema:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
          description: >-
            Schema for path parameters, if any. The keys should match the
            placeholders in the URL.
        query_params_schema:
          oneOf:
            - $ref: '#/components/schemas/QueryParamsJsonSchema'
            - type: 'null'
          description: >-
            Schema for any query params, if any. These will be added to end of
            the URL as query params. Note: properties in a query param must all
            be literal types
        request_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
            - type: 'null'
          description: >-
            Schema for the body parameters, if any. Used for POST/PATCH/PUT
            requests. The schema should be an object which will be sent as the
            json body
        response_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
            - type: 'null'
          description: >-
            Schema describing the expected response body structure. For
            documentation only; not surfaced to the LLM.
        response_filter:
          oneOf:
            - $ref: '#/components/schemas/ResponseFilter'
            - type: 'null'
          description: >-
            Optional allow-list filter applied to the response before the LLM
            sees it, so large responses don't pollute the context. Defaults to
            the full response.
        content_type:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfigInputContentType'
          default: application/json
          description: >-
            Content type for the request body. Only applies to POST/PUT/PATCH
            requests.
        auth_resolved_params:
          type: array
          items:
            type: string
          description: >-
            URL placeholders resolved from the auth connection (e.g. secrets
            injected via UrlSecretAuthConnection) rather than from
            path_params_schema.
        auth_connection:
          oneOf:
            - $ref: >-
                #/components/schemas/WebhookToolApiSchemaConfigInputAuthConnection
            - type: 'null'
          description: Optional auth connection to use for authentication with this webhook
      required:
        - url
      title: WebhookToolApiSchemaConfig-Input
    ToolRequestModelToolConfig:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - client
              description: 'Discriminator value: client'
            name:
              type: string
            description:
              type: string
              description: Description of when the tool should be used and what it does.
            response_timeout_secs:
              type: integer
              default: 20
              description: >-
                The maximum time in seconds to wait for the tool call to
                complete. Must be between 1 and 120 seconds (inclusive).
            disable_interruptions:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `interruption_mode` instead. If true, the user
                will not be able to interrupt the agent while this tool is
                running.
            interruption_mode:
              $ref: '#/components/schemas/ToolInterruptionMode'
              default: allow
              description: >-
                Controls whether the user can interrupt the agent around this
                tool call. 'allow' (default) lets the user interrupt at any
                time, 'disable_during_tool' suppresses interruptions only while
                the tool is running, 'disable_during_tool_and_turn' suppresses
                interruptions while the tool runs and for the agent response
                that follows it.
            force_pre_tool_speech:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `pre_tool_speech` instead. If true, the agent
                will speak before the tool call.
            pre_tool_speech:
              $ref: '#/components/schemas/PreToolSpeechMode'
              default: auto
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              oneOf:
                - $ref: '#/components/schemas/ToolCallSoundType'
                - type: 'null'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/ToolCallSoundBehavior'
              default: auto
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/ToolErrorHandlingMode'
              default: auto
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            parameters:
              oneOf:
                - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
                - type: 'null'
              description: Schema for any parameters to pass to the client
            expects_response:
              type: boolean
              default: false
              description: >-
                If true, calling this tool should block the conversation until
                the client responds with some response which is passed to the
                llm. If false then we will continue the conversation without
                waiting for the client to respond, this is useful to show
                content to a user but not block the conversation
            dynamic_variables:
              $ref: '#/components/schemas/DynamicVariablesConfig'
              description: Configuration for dynamic variables
            execution_mode:
              $ref: '#/components/schemas/ToolExecutionMode'
              default: immediate
              description: >-
                Determines when and how the tool executes: 'immediate' executes
                the tool right away when requested by the LLM,
                'post_tool_speech' waits for the agent to finish speaking before
                executing, 'async' runs the tool in the background without
                blocking - best for long-running operations.
          required:
            - type
            - name
            - description
          description: >-
            A client tool is one that sends an event to the user's client to
            trigger something client side
        - type: object
          properties:
            type:
              type: string
              enum:
                - mcp
              description: 'Discriminator value: mcp'
          required:
            - type
          description: mcp variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - system
              description: 'Discriminator value: system'
            name:
              type: string
            description:
              type: string
              default: ''
              description: >-
                Description of when the tool should be used and what it does.
                Leave empty to use the default description that's optimized for
                the specific tool type.
            response_timeout_secs:
              type: integer
              default: 20
              description: >-
                The maximum time in seconds to wait for the tool call to
                complete.
            disable_interruptions:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `interruption_mode` instead. If true, the user
                will not be able to interrupt the agent while this tool is
                running.
            interruption_mode:
              $ref: '#/components/schemas/ToolInterruptionMode'
              default: allow
              description: >-
                Controls whether the user can interrupt the agent around this
                tool call. 'allow' (default) lets the user interrupt at any
                time, 'disable_during_tool' suppresses interruptions only while
                the tool is running, 'disable_during_tool_and_turn' suppresses
                interruptions while the tool runs and for the agent response
                that follows it.
            force_pre_tool_speech:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `pre_tool_speech` instead. If true, the agent
                will speak before the tool call.
            pre_tool_speech:
              $ref: '#/components/schemas/PreToolSpeechMode'
              default: auto
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              oneOf:
                - $ref: '#/components/schemas/ToolCallSoundType'
                - type: 'null'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/ToolCallSoundBehavior'
              default: auto
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/ToolErrorHandlingMode'
              default: auto
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            params:
              $ref: >-
                #/components/schemas/ToolRequestModelToolConfigDiscriminatorMappingSystemParams
          required:
            - type
            - name
            - params
          description: >-
            A system tool is a tool that is used to call a system method in the
            server
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
              default: webhook
              description: The type of tool
            name:
              type: string
            description:
              type: string
              description: Description of when the tool should be used and what it does.
            response_timeout_secs:
              type: integer
              default: 20
              description: >-
                The maximum time in seconds to wait for the tool call to
                complete. Must be between 5 and 120 seconds (inclusive).
            disable_interruptions:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `interruption_mode` instead. If true, the user
                will not be able to interrupt the agent while this tool is
                running.
            interruption_mode:
              $ref: '#/components/schemas/ToolInterruptionMode'
              default: allow
              description: >-
                Controls whether the user can interrupt the agent around this
                tool call. 'allow' (default) lets the user interrupt at any
                time, 'disable_during_tool' suppresses interruptions only while
                the tool is running, 'disable_during_tool_and_turn' suppresses
                interruptions while the tool runs and for the agent response
                that follows it.
            force_pre_tool_speech:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `pre_tool_speech` instead. If true, the agent
                will speak before the tool call.
            pre_tool_speech:
              $ref: '#/components/schemas/PreToolSpeechMode'
              default: auto
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              oneOf:
                - $ref: '#/components/schemas/ToolCallSoundType'
                - type: 'null'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/ToolCallSoundBehavior'
              default: auto
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/ToolErrorHandlingMode'
              default: auto
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            dynamic_variables:
              $ref: '#/components/schemas/DynamicVariablesConfig'
              description: Configuration for dynamic variables
            execution_mode:
              $ref: '#/components/schemas/ToolExecutionMode'
              default: immediate
              description: >-
                Determines when and how the tool executes: 'immediate' executes
                the tool right away when requested by the LLM,
                'post_tool_speech' waits for the agent to finish speaking before
                executing, 'async' runs the tool in the background without
                blocking - best for long-running operations.
            api_schema:
              $ref: '#/components/schemas/WebhookToolApiSchemaConfig-Input'
              description: >-
                The schema for the outgoing webhoook, including parameters and
                URL specification
          required:
            - type
            - name
            - description
            - api_schema
          description: >-
            A webhook tool is a tool that calls an external webhook from our
            server
      discriminator:
        propertyName: type
      description: Configuration for the tool
      title: ToolRequestModelToolConfig
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
    ToolResponseMockConfig-Input:
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
      required:
        - mock_result
      title: ToolResponseMockConfig-Input
    ToolRequestModel:
      type: object
      properties:
        tool_config:
          $ref: '#/components/schemas/ToolRequestModelToolConfig'
          description: Configuration for the tool
        response_mocks:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ToolResponseMockConfig-Input'
          description: >-
            Mock responses with optional parameter conditions. Evaluated
            top-to-bottom; first match wins.
      required:
        - tool_config
      title: ToolRequestModel
    ArrayJsonSchemaPropertyOutputItems:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Output'
      description: Schema for array elements.
      title: ArrayJsonSchemaPropertyOutputItems
    ArrayJsonSchemaPropertyOutputConstantValueItems:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
      title: ArrayJsonSchemaPropertyOutputConstantValueItems
    ArrayJsonSchemaProperty-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - array
          default: array
        description:
          type: string
          default: ''
        items:
          $ref: '#/components/schemas/ArrayJsonSchemaPropertyOutputItems'
          default:
            allowed_values_dynamic_variable: ''
            constant_value: ''
            description: Array element
            dynamic_variable: ''
            is_omitted: false
            is_system_provided: false
            type: string
          description: Schema for array elements.
        dynamic_variable:
          type: string
          default: ''
          description: >-
            When set, the entire array is populated from this dynamic variable
            at runtime. Mutually exclusive with description (LLM-provided
            array), constant_value, and is_omitted.
        constant_value:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/ArrayJsonSchemaPropertyOutputConstantValueItems
          description: >-
            When set, the entire array uses this constant value at runtime.
            Mutually exclusive with description (LLM-provided array),
            dynamic_variable, and is_omitted.
        is_omitted:
          type: boolean
          default: false
          description: >-
            If true, this array parameter will be completely omitted from the
            request. Only valid for optional parameters. Mutually exclusive with
            description, dynamic_variable, and constant_value.
      title: ArrayJsonSchemaProperty-Output
    ObjectJsonSchemaPropertyOutput:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Output'
      title: ObjectJsonSchemaPropertyOutput
    ObjectJsonSchemaProperty-Output:
      type: object
      properties:
        type:
          type: string
          enum:
            - object
          default: object
        required:
          type: array
          items:
            type: string
        description:
          type: string
          default: ''
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ObjectJsonSchemaPropertyOutput'
        required_constraints:
          oneOf:
            - $ref: '#/components/schemas/RequiredConstraints'
            - type: 'null'
      title: ObjectJsonSchemaProperty-Output
    ProcedureAtVersion-Output:
      type: object
      properties:
        procedure_id:
          type: string
          description: Procedure ID
        name:
          type: string
          description: Procedure name
        type:
          $ref: '#/components/schemas/ProcedureType'
          default: free_form
        content:
          type: string
          description: Procedure content
        guardrails:
          type: array
          items:
            $ref: '#/components/schemas/CustomGuardrailConfig'
        agent_id:
          type: string
          description: Agent ID of the procedure
        version_id:
          type:
            - string
            - 'null'
          description: >-
            Version ID of a version of the procedure. None for a procedure never
            versioned.
      required:
        - procedure_id
        - name
        - content
        - agent_id
      title: ProcedureAtVersion-Output
    SubAgent-Output:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
        description:
          type: string
        parameters:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
            - type: 'null'
      required:
        - agent_id
        - description
      title: SubAgent-Output
    AgentTransfer-Output:
      type: object
      properties:
        agent_id:
          type:
            - string
            - 'null'
        node_id:
          type:
            - string
            - 'null'
        condition:
          type: string
        delay_ms:
          type: integer
          default: 0
        transfer_message:
          type:
            - string
            - 'null'
        enable_transferred_agent_first_message:
          type: boolean
          default: false
        is_workflow_node_transfer:
          type: boolean
          default: false
        preserve_client_tts_overrides:
          type: boolean
          default: false
          description: >-
            Defines whether TTS client overrides should be carried over to the
            transferred agent.
      required:
        - condition
      title: AgentTransfer-Output
    ToolResponseModelToolConfigDiscriminatorMappingSystemParams:
      oneOf:
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - end_call
              description: 'Discriminator value: end_call'
          required:
            - system_tool_type
          description: EndCallToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - end_procedure
              description: 'Discriminator value: end_procedure'
            procedures:
              type: object
              additionalProperties:
                $ref: '#/components/schemas/ProcedureAtVersion-Output'
          required:
            - system_tool_type
          description: EndProcedureToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - knowledge_base_rag
              description: 'Discriminator value: knowledge_base_rag'
          required:
            - system_tool_type
          description: KnowledgeBaseRagToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - language_detection
              description: 'Discriminator value: language_detection'
          required:
            - system_tool_type
          description: LanguageDetectionToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - play_keypad_touch_tone
              description: 'Discriminator value: play_keypad_touch_tone'
            use_out_of_band_dtmf:
              type: boolean
              default: true
              description: >-
                Send DTMF tones as out-of-band RTP events (RFC 4733) instead of
                in-band audio. Only effective for SIP trunk imported numbers.
            suppress_turn_after_dtmf:
              type: boolean
              default: false
              description: >-
                If true, the agent will not generate further speech after
                playing DTMF tones. This prevents the agent's speech from
                interfering with IVR systems.
          required:
            - system_tool_type
          description: >-
            Allows the agent to play DTMF tones during a phone call.


            This tool can be used to interact with automated phone systems, such
            as

            navigating phone menus, entering extensions, or inputting numeric
            codes.
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - run_subagent
              description: 'Discriminator value: run_subagent'
            agents:
              type: array
              items:
                $ref: '#/components/schemas/SubAgent-Output'
          required:
            - system_tool_type
            - agents
          description: RunSubagentToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - skip_turn
              description: 'Discriminator value: skip_turn'
          required:
            - system_tool_type
          description: >-
            Allows the agent to explicitly skip its turn.


            This tool should be invoked by the LLM when the user indicates they
            would like

            to think or take a short pause before continuing the
            conversation—e.g. when

            they say: "Give me a second", "Let me think", or "One moment
            please".  After

            calling this tool, the assistant should not speak until the user
            speaks

            again, or another normal turn-taking condition is met.  The tool
            itself has

            no parameters and performs no side-effects other than informing the
            backend

            that the current turn generation is complete.
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - start_procedure
              description: 'Discriminator value: start_procedure'
            procedures:
              type: object
              additionalProperties:
                $ref: '#/components/schemas/ProcedureAtVersion-Output'
          required:
            - system_tool_type
          description: StartProcedureToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - transfer_to_agent
              default: transfer_to_agent
            transfers:
              type: array
              items:
                $ref: '#/components/schemas/AgentTransfer-Output'
          required:
            - system_tool_type
            - transfers
          description: TransferToAgentToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - transfer_to_number
              default: transfer_to_number
            transfers:
              type: array
              items:
                $ref: '#/components/schemas/PhoneNumberTransfer'
            enable_client_message:
              type: boolean
              default: true
              description: >-
                Whether to play a message to the client while they wait for
                transfer. Defaults to true for backward compatibility.
          required:
            - system_tool_type
            - transfers
          description: TransferToNumberToolConfig variant
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - voicemail_detection
              default: voicemail_detection
            voicemail_message:
              type:
                - string
                - 'null'
              description: >-
                Optional message to leave on voicemail when detected. If not
                provided, the call will end immediately when voicemail is
                detected. Supports dynamic variables (e.g., {{system__time}},
                {{system__call_duration_secs}}, {{custom_variable}}).
          required:
            - system_tool_type
          description: >-
            Allows the agent to detect when a voicemail system is encountered.


            This tool should be invoked by the LLM when it detects that the call
            has been

            answered by a voicemail system rather than a human. If a voicemail
            message

            is configured, it will be played; otherwise the call will end
            immediately.
      discriminator:
        propertyName: system_tool_type
      title: ToolResponseModelToolConfigDiscriminatorMappingSystemParams
    WebhookToolApiSchemaConfigOutputRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
        - $ref: '#/components/schemas/ConvAIEnvVarLocator'
      title: WebhookToolApiSchemaConfigOutputRequestHeaders
    WebhookToolApiSchemaConfigOutputMethod:
      type: string
      enum:
        - GET
        - POST
        - PUT
        - PATCH
        - DELETE
      default: GET
      description: The HTTP method to use for the webhook
      title: WebhookToolApiSchemaConfigOutputMethod
    WebhookToolApiSchemaConfigOutputContentType:
      type: string
      enum:
        - application/json
        - application/x-www-form-urlencoded
      default: application/json
      description: >-
        Content type for the request body. Only applies to POST/PUT/PATCH
        requests.
      title: WebhookToolApiSchemaConfigOutputContentType
    WebhookToolApiSchemaConfigOutputAuthConnection:
      oneOf:
        - $ref: '#/components/schemas/AuthConnectionLocator'
        - $ref: '#/components/schemas/EnvironmentAuthConnectionLocator'
      description: Optional auth connection to use for authentication with this webhook
      title: WebhookToolApiSchemaConfigOutputAuthConnection
    WebhookToolApiSchemaConfig-Output:
      type: object
      properties:
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/WebhookToolApiSchemaConfigOutputRequestHeaders
          description: Headers that should be included in the request
        url:
          type: string
          description: >-
            The URL that the webhook will be sent to. May include path
            parameters, e.g. https://example.com/agents/{agent_id}
        method:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfigOutputMethod'
          default: GET
          description: The HTTP method to use for the webhook
        path_params_schema:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LiteralJsonSchemaProperty'
          description: >-
            Schema for path parameters, if any. The keys should match the
            placeholders in the URL.
        query_params_schema:
          oneOf:
            - $ref: '#/components/schemas/QueryParamsJsonSchema'
            - type: 'null'
          description: >-
            Schema for any query params, if any. These will be added to end of
            the URL as query params. Note: properties in a query param must all
            be literal types
        request_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
            - type: 'null'
          description: >-
            Schema for the body parameters, if any. Used for POST/PATCH/PUT
            requests. The schema should be an object which will be sent as the
            json body
        response_body_schema:
          oneOf:
            - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
            - type: 'null'
          description: >-
            Schema describing the expected response body structure. For
            documentation only; not surfaced to the LLM.
        response_filter:
          oneOf:
            - $ref: '#/components/schemas/ResponseFilter'
            - type: 'null'
          description: >-
            Optional allow-list filter applied to the response before the LLM
            sees it, so large responses don't pollute the context. Defaults to
            the full response.
        content_type:
          $ref: '#/components/schemas/WebhookToolApiSchemaConfigOutputContentType'
          default: application/json
          description: >-
            Content type for the request body. Only applies to POST/PUT/PATCH
            requests.
        auth_resolved_params:
          type: array
          items:
            type: string
          description: >-
            URL placeholders resolved from the auth connection (e.g. secrets
            injected via UrlSecretAuthConnection) rather than from
            path_params_schema.
        auth_connection:
          oneOf:
            - $ref: >-
                #/components/schemas/WebhookToolApiSchemaConfigOutputAuthConnection
            - type: 'null'
          description: Optional auth connection to use for authentication with this webhook
      required:
        - url
      title: WebhookToolApiSchemaConfig-Output
    ToolResponseModelToolConfig:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - client
              description: 'Discriminator value: client'
            name:
              type: string
            description:
              type: string
              description: Description of when the tool should be used and what it does.
            response_timeout_secs:
              type: integer
              default: 20
              description: >-
                The maximum time in seconds to wait for the tool call to
                complete. Must be between 1 and 120 seconds (inclusive).
            disable_interruptions:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `interruption_mode` instead. If true, the user
                will not be able to interrupt the agent while this tool is
                running.
            interruption_mode:
              $ref: '#/components/schemas/ToolInterruptionMode'
              default: allow
              description: >-
                Controls whether the user can interrupt the agent around this
                tool call. 'allow' (default) lets the user interrupt at any
                time, 'disable_during_tool' suppresses interruptions only while
                the tool is running, 'disable_during_tool_and_turn' suppresses
                interruptions while the tool runs and for the agent response
                that follows it.
            force_pre_tool_speech:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `pre_tool_speech` instead. If true, the agent
                will speak before the tool call.
            pre_tool_speech:
              $ref: '#/components/schemas/PreToolSpeechMode'
              default: auto
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              oneOf:
                - $ref: '#/components/schemas/ToolCallSoundType'
                - type: 'null'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/ToolCallSoundBehavior'
              default: auto
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/ToolErrorHandlingMode'
              default: auto
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            parameters:
              oneOf:
                - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Output'
                - type: 'null'
              description: Schema for any parameters to pass to the client
            expects_response:
              type: boolean
              default: false
              description: >-
                If true, calling this tool should block the conversation until
                the client responds with some response which is passed to the
                llm. If false then we will continue the conversation without
                waiting for the client to respond, this is useful to show
                content to a user but not block the conversation
            dynamic_variables:
              $ref: '#/components/schemas/DynamicVariablesConfig'
              description: Configuration for dynamic variables
            execution_mode:
              $ref: '#/components/schemas/ToolExecutionMode'
              default: immediate
              description: >-
                Determines when and how the tool executes: 'immediate' executes
                the tool right away when requested by the LLM,
                'post_tool_speech' waits for the agent to finish speaking before
                executing, 'async' runs the tool in the background without
                blocking - best for long-running operations.
          required:
            - type
            - name
            - description
          description: >-
            A client tool is one that sends an event to the user's client to
            trigger something client side
        - type: object
          properties:
            type:
              type: string
              enum:
                - mcp
              description: 'Discriminator value: mcp'
          required:
            - type
          description: mcp variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - system
              description: 'Discriminator value: system'
            name:
              type: string
            description:
              type: string
              default: ''
              description: >-
                Description of when the tool should be used and what it does.
                Leave empty to use the default description that's optimized for
                the specific tool type.
            response_timeout_secs:
              type: integer
              default: 20
              description: >-
                The maximum time in seconds to wait for the tool call to
                complete.
            disable_interruptions:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `interruption_mode` instead. If true, the user
                will not be able to interrupt the agent while this tool is
                running.
            interruption_mode:
              $ref: '#/components/schemas/ToolInterruptionMode'
              default: allow
              description: >-
                Controls whether the user can interrupt the agent around this
                tool call. 'allow' (default) lets the user interrupt at any
                time, 'disable_during_tool' suppresses interruptions only while
                the tool is running, 'disable_during_tool_and_turn' suppresses
                interruptions while the tool runs and for the agent response
                that follows it.
            force_pre_tool_speech:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `pre_tool_speech` instead. If true, the agent
                will speak before the tool call.
            pre_tool_speech:
              $ref: '#/components/schemas/PreToolSpeechMode'
              default: auto
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              oneOf:
                - $ref: '#/components/schemas/ToolCallSoundType'
                - type: 'null'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/ToolCallSoundBehavior'
              default: auto
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/ToolErrorHandlingMode'
              default: auto
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            params:
              $ref: >-
                #/components/schemas/ToolResponseModelToolConfigDiscriminatorMappingSystemParams
          required:
            - type
            - name
            - params
          description: >-
            A system tool is a tool that is used to call a system method in the
            server
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
              default: webhook
              description: The type of tool
            name:
              type: string
            description:
              type: string
              description: Description of when the tool should be used and what it does.
            response_timeout_secs:
              type: integer
              default: 20
              description: >-
                The maximum time in seconds to wait for the tool call to
                complete. Must be between 5 and 120 seconds (inclusive).
            disable_interruptions:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `interruption_mode` instead. If true, the user
                will not be able to interrupt the agent while this tool is
                running.
            interruption_mode:
              $ref: '#/components/schemas/ToolInterruptionMode'
              default: allow
              description: >-
                Controls whether the user can interrupt the agent around this
                tool call. 'allow' (default) lets the user interrupt at any
                time, 'disable_during_tool' suppresses interruptions only while
                the tool is running, 'disable_during_tool_and_turn' suppresses
                interruptions while the tool runs and for the agent response
                that follows it.
            force_pre_tool_speech:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `pre_tool_speech` instead. If true, the agent
                will speak before the tool call.
            pre_tool_speech:
              $ref: '#/components/schemas/PreToolSpeechMode'
              default: auto
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              oneOf:
                - $ref: '#/components/schemas/ToolCallSoundType'
                - type: 'null'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/ToolCallSoundBehavior'
              default: auto
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/ToolErrorHandlingMode'
              default: auto
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            dynamic_variables:
              $ref: '#/components/schemas/DynamicVariablesConfig'
              description: Configuration for dynamic variables
            execution_mode:
              $ref: '#/components/schemas/ToolExecutionMode'
              default: immediate
              description: >-
                Determines when and how the tool executes: 'immediate' executes
                the tool right away when requested by the LLM,
                'post_tool_speech' waits for the agent to finish speaking before
                executing, 'async' runs the tool in the background without
                blocking - best for long-running operations.
            api_schema:
              $ref: '#/components/schemas/WebhookToolApiSchemaConfig-Output'
              description: >-
                The schema for the outgoing webhoook, including parameters and
                URL specification
          required:
            - type
            - name
            - description
            - api_schema
          description: >-
            A webhook tool is a tool that calls an external webhook from our
            server
      discriminator:
        propertyName: type
      description: The type of tool
      title: ToolResponseModelToolConfig
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
    ToolUsageStatsResponseModel:
      type: object
      properties:
        total_calls:
          type: integer
          default: 0
          description: The total number of calls to the tool
        avg_latency_secs:
          type: number
          format: double
      required:
        - avg_latency_secs
      title: ToolUsageStatsResponseModel
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
      required:
        - mock_result
      title: ToolResponseMockConfig-Output
    ToolResponseModel:
      type: object
      properties:
        id:
          type: string
        tool_config:
          $ref: '#/components/schemas/ToolResponseModelToolConfig'
          description: The type of tool
        access_info:
          $ref: '#/components/schemas/ResourceAccessInfo'
        usage_stats:
          $ref: '#/components/schemas/ToolUsageStatsResponseModel'
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
        - id
        - tool_config
        - access_info
        - usage_stats
      title: ToolResponseModel
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
  "tool_config": {
    "type": "system",
    "name": "end_call",
    "params": {
      "system_tool_type": "end_call"
    },
    "description": ""
  }
}
```

**Response**

```json
{
  "id": "string",
  "tool_config": {
    "type": "system",
    "name": "end_call",
    "params": {
      "system_tool_type": "end_call"
    },
    "description": ""
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "access_source": "creator"
  },
  "usage_stats": {
    "avg_latency_secs": 1.1,
    "total_calls": 0
  },
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
    await client.conversationalAi.tools.update("tool_id", {
        toolConfig: {
            type: "system",
            name: "end_call",
            params: {
                systemToolType: "end_call",
            },
            description: "",
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, ToolRequestModel, ToolRequestModelToolConfig_System, SystemToolConfigInputParams_EndCall

client = ElevenLabs()

client.conversational_ai.tools.update(
    tool_id="tool_id",
    request=ToolRequestModel(
        tool_config=ToolRequestModelToolConfig_System(
            name="end_call",
            params=SystemToolConfigInputParams_EndCall(),
            description="",
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

	payload := strings.NewReader("{\n  \"tool_config\": {\n    \"type\": \"system\",\n    \"name\": \"end_call\",\n    \"params\": {\n      \"system_tool_type\": \"end_call\"\n    },\n    \"description\": \"\"\n  }\n}")

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
request.body = "{\n  \"tool_config\": {\n    \"type\": \"system\",\n    \"name\": \"end_call\",\n    \"params\": {\n      \"system_tool_type\": \"end_call\"\n    },\n    \"description\": \"\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/tools/tool_id")
  .header("Content-Type", "application/json")
  .body("{\n  \"tool_config\": {\n    \"type\": \"system\",\n    \"name\": \"end_call\",\n    \"params\": {\n      \"system_tool_type\": \"end_call\"\n    },\n    \"description\": \"\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/tools/tool_id', [
  'body' => '{
  "tool_config": {
    "type": "system",
    "name": "end_call",
    "params": {
      "system_tool_type": "end_call"
    },
    "description": ""
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
request.AddParameter("application/json", "{\n  \"tool_config\": {\n    \"type\": \"system\",\n    \"name\": \"end_call\",\n    \"params\": {\n      \"system_tool_type\": \"end_call\"\n    },\n    \"description\": \"\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["tool_config": [
    "type": "system",
    "name": "end_call",
    "params": ["system_tool_type": "end_call"],
    "description": ""
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
