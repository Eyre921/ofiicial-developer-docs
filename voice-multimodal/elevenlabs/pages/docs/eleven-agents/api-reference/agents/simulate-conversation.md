---
title: "Simulate conversation"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/simulate-conversation.md
path: docs/eleven-agents/api-reference/agents/simulate-conversation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Simulate conversation

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/simulate-conversation
Content-Type: application/json

Deprecated. Use the `/v1/convai/agent-testing/create` and `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run simulations. Run a conversation between the agent and a simulated user.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/simulate-conversation

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/simulate-conversation:
    post:
      operationId: simulate_conversation
      summary: Simulates A Conversation
      description: >-
        Deprecated. Use the `/v1/convai/agent-testing/create` and
        `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run
        simulations. Run a conversation between the agent and a simulated user.
      tags:
        - agents
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
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
                $ref: '#/components/schemas/type_:AgentSimulatedChatTestResponseModel'
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
                simulation_specification:
                  $ref: >-
                    #/components/schemas/type_:ConversationSimulationSpecification
                  description: >-
                    A specification detailing how the conversation should be
                    simulated
                extra_evaluation_criteria:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_:PromptEvaluationCriteria'
                  description: A list of evaluation criteria to test
                new_turns_limit:
                  type: integer
                  default: 10000
                  description: >-
                    Maximum number of new turns to generate in the conversation
                    simulation
              required:
                - simulation_specification
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
    type_:Verbosity:
      type: string
      enum:
        - auto
        - concise
        - thorough
      title: Verbosity
    type_:OutputFormat:
      type: string
      enum:
        - mp3_22050_32
        - mp3_44100_32
        - mp3_44100_64
        - mp3_44100_96
        - mp3_44100_128
        - mp3_44100_192
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_44100
        - ulaw_8000
      title: OutputFormat
    type_:InteractionBudget:
      type: string
      enum:
        - realtime
        - 5_minutes
        - 10_minutes
        - 1_hour
      title: InteractionBudget
    type_:BehaviorOverride:
      type: object
      properties:
        verbosity:
          $ref: '#/components/schemas/type_:Verbosity'
          description: Verbosity override. Underlying default applies when unset.
        output_format:
          $ref: '#/components/schemas/type_:OutputFormat'
          description: Output format override. Underlying default applies when unset.
        interaction_budget:
          $ref: '#/components/schemas/type_:InteractionBudget'
          description: Interaction budget override. Underlying default applies when unset.
      title: BehaviorOverride
    type_:Llm:
      type: string
      enum:
        - gpt-4o-mini
        - gpt-4o
        - gpt-4
        - gpt-4-turbo
        - gpt-4.1
        - gpt-4.1-mini
        - gpt-4.1-nano
        - gpt-5
        - gpt-5.1
        - gpt-5.2
        - gpt-5.2-chat-latest
        - gpt-5.4
        - gpt-5.4-mini
        - gpt-5.4-nano
        - gpt-5.5
        - gpt-5.6-sol
        - gpt-5.6-terra
        - gpt-5.6-luna
        - gpt-5-mini
        - gpt-5-nano
        - gpt-3.5-turbo
        - gemini-1.5-pro
        - gemini-1.5-flash
        - gemini-2.0-flash
        - gemini-2.0-flash-lite
        - gemini-2.5-flash-lite
        - gemini-2.5-flash
        - gemini-3-pro-preview
        - gemini-3-flash-preview
        - gemini-3.1-pro-preview
        - gemini-3.1-flash-lite-preview
        - gemini-3.1-flash-lite
        - gemini-3.5-flash
        - gemini-3.5-flash-lite
        - claude-sonnet-4-5
        - claude-opus-4-7
        - claude-opus-4-8
        - claude-sonnet-4-6
        - claude-sonnet-5
        - claude-sonnet-4
        - claude-haiku-4-5
        - claude-3-7-sonnet
        - claude-3-5-sonnet
        - claude-3-5-sonnet-v1
        - claude-3-haiku
        - grok-beta
        - custom-llm
        - qwen3-4b
        - qwen3-30b-a3b
        - qwen36-35b-a3b
        - qwen35-397b-a17b
        - gpt-oss-20b
        - gpt-oss-120b
        - glm-45-air-fp8
        - gemini-2.5-flash-preview-09-2025
        - gemini-2.5-flash-lite-preview-09-2025
        - gemini-2.5-flash-preview-05-20
        - gemini-2.5-flash-preview-04-17
        - gemini-2.5-flash-lite-preview-06-17
        - gemini-2.0-flash-lite-001
        - gemini-2.0-flash-001
        - gemini-1.5-flash-002
        - gemini-1.5-flash-001
        - gemini-1.5-pro-002
        - gemini-1.5-pro-001
        - claude-sonnet-4@20250514
        - claude-sonnet-4-5@20250929
        - claude-haiku-4-5@20251001
        - claude-3-7-sonnet@20250219
        - claude-3-5-sonnet@20240620
        - claude-3-5-sonnet-v2@20241022
        - claude-3-haiku@20240307
        - gpt-5-2025-08-07
        - gpt-5.1-2025-11-13
        - gpt-5.2-2025-12-11
        - gpt-5.4-2026-03-05
        - gpt-5.4-mini-2026-03-17
        - gpt-5.4-nano-2026-03-17
        - gpt-5.5-2026-04-23
        - gpt-5-mini-2025-08-07
        - gpt-5-nano-2025-08-07
        - gpt-4.1-2025-04-14
        - gpt-4.1-mini-2025-04-14
        - gpt-4.1-nano-2025-04-14
        - gpt-4o-mini-2024-07-18
        - gpt-4o-2024-11-20
        - gpt-4o-2024-08-06
        - gpt-4o-2024-05-13
        - gpt-4-0613
        - gpt-4-0314
        - gpt-4-turbo-2024-04-09
        - gpt-3.5-turbo-0125
        - gpt-3.5-turbo-1106
        - watt-tool-8b
        - watt-tool-70b
      title: Llm
    type_:LlmReasoningEffort:
      type: string
      enum:
        - none
        - minimal
        - low
        - medium
        - high
        - xhigh
        - max
      title: LlmReasoningEffort
    type_:ToolInterruptionMode:
      type: string
      enum:
        - allow
        - disable_during_tool
        - disable_during_tool_and_turn
      default: allow
      title: ToolInterruptionMode
    type_:PreToolSpeechMode:
      type: string
      enum:
        - auto
        - force
        - 'off'
      default: auto
      title: PreToolSpeechMode
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
    type_:ToolCallSoundBehavior:
      type: string
      enum:
        - auto
        - always
      default: auto
      description: Determines how the tool call sound should be played.
      title: ToolCallSoundBehavior
    type_:ToolErrorHandlingMode:
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
    type_:ProcedureType:
      type: string
      enum:
        - free_form
        - deterministic
      default: free_form
      title: ProcedureType
    type_:GuardrailExecutionMode:
      type: string
      enum:
        - streaming
        - blocking
      default: streaming
      title: GuardrailExecutionMode
    type_:CustomGuardrailConfigModel:
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
    type_:CustomGuardrailConfigTriggerAction:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - end_call
              description: 'Discriminator value: end_call'
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - retry
              description: 'Discriminator value: retry'
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
      discriminator:
        propertyName: type
      title: CustomGuardrailConfigTriggerAction
    type_:CustomGuardrailConfig:
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
          $ref: '#/components/schemas/type_:GuardrailExecutionMode'
        model:
          $ref: '#/components/schemas/type_:CustomGuardrailConfigModel'
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
          $ref: '#/components/schemas/type_:CustomGuardrailConfigTriggerAction'
        evaluate_full_response_only:
          type: boolean
          default: false
          description: >-
            Evaluate once against the complete non-TTS response instead of
            cumulative partials. Requires blocking mode.
      required:
        - name
        - prompt
      description: Single custom guardrail configuration
      title: CustomGuardrailConfig
    type_:ProcedureAtVersionOutput:
      type: object
      properties:
        procedure_id:
          type: string
          description: Procedure ID
        name:
          type: string
          description: Procedure name
        type:
          $ref: '#/components/schemas/type_:ProcedureType'
        trigger:
          type: string
          default: ''
          description: >-
            When the agent should use this procedure. Empty string means this is
            a sub-procedure that should only start when another procedure
            references it.
        referenced_tool_ids:
          type: array
          items:
            type: string
          description: Tool IDs referenced in the procedure content
        referenced_kb_ids:
          type: array
          items:
            type: string
          description: Knowledge base IDs referenced in the procedure content
        referenced_procedure_ids:
          type: array
          items:
            type: string
          description: Procedure IDs referenced in the procedure content
        referenced_dynamic_variables:
          type: array
          items:
            type: string
          description: Dynamic variable names used in the procedure content
        content:
          type: string
          description: Procedure content
        guardrails:
          type: array
          items:
            $ref: '#/components/schemas/type_:CustomGuardrailConfig'
        agent_id:
          type: string
          description: Agent ID of the procedure
        version_id:
          type: string
          description: >-
            Version ID of a version of the procedure. None for a procedure never
            versioned.
      required:
        - procedure_id
        - name
        - content
        - agent_id
      title: ProcedureAtVersionOutput
    type_:SearchStrategy:
      type: string
      enum:
        - cat
        - keyword
        - semantic
        - ls
      title: SearchStrategy
    type_:LiteralJsonSchemaPropertyType:
      oneOf:
        - type: string
          enum:
            - boolean
        - type: string
          enum:
            - string
        - type: string
          enum:
            - integer
        - type: string
          enum:
            - number
        - type: array
          items:
            type: string
      title: LiteralJsonSchemaPropertyType
    type_:LiteralJsonSchemaPropertyConstantValue:
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
    type_:LiteralJsonSchemaProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:LiteralJsonSchemaPropertyType'
        description:
          type: string
          default: ''
          description: >-
            The description of the property. When set, the LLM will provide the
            value based on this description. Mutually exclusive with
            dynamic_variable, is_system_provided, constant_value, and
            is_omitted.
        enum:
          type: array
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
          $ref: '#/components/schemas/type_:LiteralJsonSchemaPropertyConstantValue'
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
    type_:ArrayJsonSchemaPropertyOutputItems:
      oneOf:
        - $ref: '#/components/schemas/type_:LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyOutput'
        - $ref: '#/components/schemas/type_:ArrayJsonSchemaPropertyOutput'
      description: Schema for array elements.
      title: ArrayJsonSchemaPropertyOutputItems
    type_:ArrayJsonSchemaPropertyOutput:
      type: object
      properties:
        description:
          type: string
          default: ''
        dynamic_variable:
          type: string
          default: ''
          description: >-
            When set, the entire parameter is populated from this dynamic
            variable at runtime. Mutually exclusive with description
            (LLM-provided value), constant_value, and is_omitted.
        constant_value:
          type: array
          items:
            description: Any type
          description: >-
            When set, the entire array uses this constant value at runtime.
            Mutually exclusive with description (LLM-provided array),
            dynamic_variable, and is_omitted.
        is_omitted:
          type: boolean
          default: false
          description: >-
            If true, this parameter will be completely omitted from the request.
            Only valid for optional parameters. Mutually exclusive with
            description, dynamic_variable, and constant_value.
        type:
          type: string
          enum:
            - array
        items:
          $ref: '#/components/schemas/type_:ArrayJsonSchemaPropertyOutputItems'
          description: Schema for array elements.
      title: ArrayJsonSchemaPropertyOutput
    type_:ObjectJsonSchemaPropertyOutputPropertiesValue:
      oneOf:
        - $ref: '#/components/schemas/type_:LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyOutput'
        - $ref: '#/components/schemas/type_:ArrayJsonSchemaPropertyOutput'
      title: ObjectJsonSchemaPropertyOutputPropertiesValue
    type_:RequiredConstraint:
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
    type_:RequiredConstraints:
      type: object
      properties:
        any_of:
          type: array
          items:
            $ref: '#/components/schemas/type_:RequiredConstraint'
        all_of:
          type: array
          items:
            $ref: '#/components/schemas/type_:RequiredConstraint'
      description: >-
        Wrapper for anyOf/allOf composition constraints scoped to required
        fields.
      title: RequiredConstraints
    type_:ObjectJsonSchemaPropertyOutput:
      type: object
      properties:
        description:
          type: string
          default: ''
        dynamic_variable:
          type: string
          default: ''
          description: >-
            When set, the entire parameter is populated from this dynamic
            variable at runtime. Mutually exclusive with description
            (LLM-provided value), constant_value, and is_omitted.
        constant_value:
          type: object
          additionalProperties:
            description: Any type
          description: >-
            When set, the entire object uses this constant JSON value at
            runtime. Mutually exclusive with description (LLM-provided object),
            dynamic_variable, and is_omitted.
        is_omitted:
          type: boolean
          default: false
          description: >-
            If true, this parameter will be completely omitted from the request.
            Only valid for optional parameters. Mutually exclusive with
            description, dynamic_variable, and constant_value.
        type:
          type: string
          enum:
            - object
        required:
          type: array
          items:
            type: string
        properties:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:ObjectJsonSchemaPropertyOutputPropertiesValue
        required_constraints:
          $ref: '#/components/schemas/type_:RequiredConstraints'
      title: ObjectJsonSchemaPropertyOutput
    type_:SubAgentOutput:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type: string
        description:
          type: string
        parameters:
          $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyOutput'
      required:
        - agent_id
        - description
      title: SubAgentOutput
    type_:AgentTransferOutput:
      type: object
      properties:
        agent_id:
          type: string
        node_id:
          type: string
        condition:
          type: string
        delay_ms:
          type: integer
          default: 0
        transfer_message:
          type: string
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
      title: AgentTransferOutput
    type_:PhoneNumberTransferCustomSipHeadersItem:
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
      discriminator:
        propertyName: type
      title: PhoneNumberTransferCustomSipHeadersItem
    type_:PhoneNumberTransferTransferDestination:
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
      discriminator:
        propertyName: type
      title: PhoneNumberTransferTransferDestination
    type_:TransferTypeEnum:
      type: string
      enum:
        - blind
        - conference
        - sip_refer
      default: conference
      title: TransferTypeEnum
    type_:UuiTransferConfigProtocolDiscriminatorMode:
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
    type_:UuiTransferConfig:
      type: object
      properties:
        data:
          type: string
          description: >-
            UUI payload to send on SIP REFER transfers. Supports inline dynamic
            variables and is hex-encoded at transfer time.
        protocol_discriminator:
          type: string
          description: >-
            Optional one-octet protocol discriminator (two hex digits, e.g.
            '00'). Required by platforms such as Genesys Cloud, which otherwise
            strip the first octet of the payload. Leave unset for platforms like
            Talkdesk that expect a bare hex payload.
        protocol_discriminator_mode:
          $ref: >-
            #/components/schemas/type_:UuiTransferConfigProtocolDiscriminatorMode
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
      title: UuiTransferConfig
    type_:PhoneNumberTransferPostDialDigits:
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
      discriminator:
        propertyName: type
      title: PhoneNumberTransferPostDialDigits
    type_:PhoneNumberTransfer:
      type: object
      properties:
        custom_sip_headers:
          type: array
          items:
            $ref: '#/components/schemas/type_:PhoneNumberTransferCustomSipHeadersItem'
          description: >-
            Custom SIP headers to include when transferring the call. Each
            header can be either a static value or a dynamic variable reference.
        transfer_destination:
          $ref: '#/components/schemas/type_:PhoneNumberTransferTransferDestination'
        transfer_type:
          $ref: '#/components/schemas/type_:TransferTypeEnum'
        uui:
          $ref: '#/components/schemas/type_:UuiTransferConfig'
          description: >-
            User-to-User Information (RFC 7433) to attach to SIP REFER
            transfers. Carries call context such as CRM identifiers or
            escalation reason across the transfer boundary.
        post_dial_digits:
          $ref: '#/components/schemas/type_:PhoneNumberTransferPostDialDigits'
          description: >-
            DTMF digits to send after call connects (e.g., 'ww1234' for
            extension). Can be either a static value or a dynamic variable
            reference. Use 'w' for 0.5s pause. Only supported for Twilio
            transfers.
        phone_number:
          type: string
        condition:
          type: string
      required:
        - transfer_destination
        - condition
      title: PhoneNumberTransfer
    type_:SystemToolConfigOutputParams:
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
                $ref: '#/components/schemas/type_:ProcedureAtVersionOutput'
          required:
            - system_tool_type
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - knowledge_base
              description: 'Discriminator value: knowledge_base'
            enabled_strategies:
              type: array
              items:
                $ref: '#/components/schemas/type_:SearchStrategy'
          required:
            - system_tool_type
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - knowledge_base_rag
              description: 'Discriminator value: knowledge_base_rag'
          required:
            - system_tool_type
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - language_detection
              description: 'Discriminator value: language_detection'
            only_at_conversation_start:
              type: boolean
              default: false
              description: >-
                If no language switch happens in the first 2 user turns, later
                attempts fail and the conversation stays in the current
                language. If the language switches during those turns, later
                switching stays available. Enable to reduce the possibility of
                false switching.
          required:
            - system_tool_type
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
                $ref: '#/components/schemas/type_:SubAgentOutput'
          required:
            - system_tool_type
            - agents
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - skip_turn
              description: 'Discriminator value: skip_turn'
          required:
            - system_tool_type
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
                $ref: '#/components/schemas/type_:ProcedureAtVersionOutput'
          required:
            - system_tool_type
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - transfer_to_agent
              description: 'Discriminator value: transfer_to_agent'
            transfers:
              type: array
              items:
                $ref: '#/components/schemas/type_:AgentTransferOutput'
          required:
            - system_tool_type
            - transfers
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - transfer_to_number
              description: 'Discriminator value: transfer_to_number'
            transfers:
              type: array
              items:
                $ref: '#/components/schemas/type_:PhoneNumberTransfer'
            enable_client_message:
              type: boolean
              default: true
              description: >-
                Whether to play a message to the client while they wait for
                transfer. Defaults to true for backward compatibility.
          required:
            - system_tool_type
            - transfers
        - type: object
          properties:
            system_tool_type:
              type: string
              enum:
                - voicemail_detection
              description: 'Discriminator value: voicemail_detection'
            voicemail_message:
              type: string
              description: >-
                Optional message to leave on voicemail when detected. If not
                provided, the call will end immediately when voicemail is
                detected. Supports dynamic variables (e.g., {{system__time}},
                {{system__call_duration_secs}}, {{custom_variable}}).
          required:
            - system_tool_type
      discriminator:
        propertyName: system_tool_type
      title: SystemToolConfigOutputParams
    type_:SystemToolConfigOutput:
      type: object
      properties:
        type:
          type: string
          enum:
            - system
          description: The type of tool
        name:
          type: string
        description:
          type: string
          default: ''
          description: >-
            Description of when the tool should be used and what it does. Leave
            empty to use the default description that's optimized for the
            specific tool type.
        response_timeout_secs:
          type: integer
          default: 20
          description: The maximum time in seconds to wait for the tool call to complete.
        disable_interruptions:
          type: boolean
          default: false
          description: >-
            DEPRECATED: use `interruption_mode` instead. If true, the user will
            not be able to interrupt the agent while this tool is running.
        interruption_mode:
          $ref: '#/components/schemas/type_:ToolInterruptionMode'
          description: >-
            Controls whether the user can interrupt the agent around this tool
            call. 'allow' (default) lets the user interrupt at any time,
            'disable_during_tool' suppresses interruptions only while the tool
            is running, 'disable_during_tool_and_turn' suppresses interruptions
            while the tool runs and for the agent response that follows it.
        force_pre_tool_speech:
          type: boolean
          default: false
          description: >-
            DEPRECATED: use `pre_tool_speech` instead. If true, the agent will
            speak before the tool call.
        pre_tool_speech:
          $ref: '#/components/schemas/type_:PreToolSpeechMode'
          description: >-
            Controls whether the agent speaks before this tool is called. 'auto'
            (default) decides based on recent tool latency, 'force' always asks
            the agent to speak, 'off' fully opts out regardless of latency.
        assignments:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableAssignment'
          description: >-
            Configuration for extracting values from tool responses and
            assigning them to dynamic variables
        tool_call_sound:
          $ref: '#/components/schemas/type_:ToolCallSoundType'
          description: >-
            Predefined tool call sound type to play during tool execution. If
            not specified, no tool call sound will be played.
        tool_call_sound_behavior:
          $ref: '#/components/schemas/type_:ToolCallSoundBehavior'
          description: >-
            Determines when the tool call sound should play. 'auto' only plays
            when there's pre-tool speech, 'always' plays for every tool call.
        tool_error_handling_mode:
          $ref: '#/components/schemas/type_:ToolErrorHandlingMode'
          description: >-
            Controls how tool errors are processed before being shared with the
            agent. 'auto' determines handling based on tool type (summarized for
            native integrations, hide for others), 'summarized' sends an
            LLM-generated summary, 'passthrough' sends the raw error, 'hide'
            does not share the error with the agent.
        params:
          $ref: '#/components/schemas/type_:SystemToolConfigOutputParams'
      required:
        - name
        - params
      description: >-
        A system tool is a tool that is used to call a system method in the
        server
      title: SystemToolConfigOutput
    type_:BuiltInToolsOutput:
      type: object
      properties:
        end_call:
          $ref: '#/components/schemas/type_:SystemToolConfigOutput'
          description: The end call tool
        language_detection:
          $ref: '#/components/schemas/type_:SystemToolConfigOutput'
          description: The language detection tool
        transfer_to_agent:
          $ref: '#/components/schemas/type_:SystemToolConfigOutput'
          description: The transfer to agent tool
        transfer_to_number:
          $ref: '#/components/schemas/type_:SystemToolConfigOutput'
          description: The transfer to number tool
        skip_turn:
          $ref: '#/components/schemas/type_:SystemToolConfigOutput'
          description: The skip turn tool
        play_keypad_touch_tone:
          $ref: '#/components/schemas/type_:SystemToolConfigOutput'
          description: The play DTMF tool
        voicemail_detection:
          $ref: '#/components/schemas/type_:SystemToolConfigOutput'
          description: The voicemail detection tool
      title: BuiltInToolsOutput
    type_:KnowledgeBaseDocumentType:
      type: string
      enum:
        - file
        - url
        - text
        - folder
      title: KnowledgeBaseDocumentType
    type_:DocumentUsageModeEnum:
      type: string
      enum:
        - prompt
        - auto
      default: auto
      title: DocumentUsageModeEnum
    type_:KnowledgeBaseLocator:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:KnowledgeBaseDocumentType'
          description: The type of the knowledge base
        name:
          type: string
          description: The name of the knowledge base
        id:
          type: string
          description: The ID of the knowledge base
        usage_mode:
          $ref: '#/components/schemas/type_:DocumentUsageModeEnum'
          description: The usage mode of the knowledge base
      required:
        - type
        - name
        - id
      title: KnowledgeBaseLocator
    type_:ConvAiSecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      description: Used to reference a secret from the agent's secret store.
      title: ConvAiSecretLocator
    type_:ConvAiEnvVarLocator:
      type: object
      properties:
        env_var_label:
          type: string
      required:
        - env_var_label
      description: Used to reference an environment variable by label.
      title: ConvAiEnvVarLocator
    type_:CustomLlmApiKey:
      oneOf:
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
        - $ref: '#/components/schemas/type_:ConvAiEnvVarLocator'
      description: >-
        The API key for authentication. Either a workspace secret reference
        {'secret_id': '...'} or an environment variable reference
        {'env_var_label': '...'}.
      title: CustomLlmApiKey
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
    type_:CustomLlmAuthConnection:
      oneOf:
        - $ref: '#/components/schemas/type_:AuthConnectionLocator'
        - $ref: '#/components/schemas/type_:EnvironmentAuthConnectionLocator'
      description: >-
        Optional workspace auth connection for authentication. Only auth
        connections that produce an Authorization Bearer token are supported;
        Basic auth, mTLS, custom header, and URL secret auth connections are not
        supported.
      title: CustomLlmAuthConnection
    type_:ConvAiDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
      description: Used to reference a dynamic variable.
      title: ConvAiDynamicVariable
    type_:CustomLlmRequestHeadersValue:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
        - $ref: '#/components/schemas/type_:ConvAiDynamicVariable'
        - $ref: '#/components/schemas/type_:ConvAiEnvVarLocator'
      title: CustomLlmRequestHeadersValue
    type_:CustomLlmapiType:
      type: string
      enum:
        - chat_completions
        - responses
        - websocket
      default: chat_completions
      title: CustomLlmapiType
    type_:CustomLlm:
      type: object
      properties:
        url:
          type: string
          description: The URL of the Chat Completions compatible endpoint
        model_id:
          type: string
          description: The model ID to be used if URL serves multiple models
        api_key:
          $ref: '#/components/schemas/type_:CustomLlmApiKey'
          description: >-
            The API key for authentication. Either a workspace secret reference
            {'secret_id': '...'} or an environment variable reference
            {'env_var_label': '...'}.
        auth_connection:
          $ref: '#/components/schemas/type_:CustomLlmAuthConnection'
          description: >-
            Optional workspace auth connection for authentication. Only auth
            connections that produce an Authorization Bearer token are
            supported; Basic auth, mTLS, custom header, and URL secret auth
            connections are not supported.
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:CustomLlmRequestHeadersValue'
          description: Headers that should be included in the request
        api_version:
          type: string
          description: The API version to use for the request
        api_type:
          $ref: '#/components/schemas/type_:CustomLlmapiType'
          description: The API type to use (chat_completions, responses or websocket)
      required:
        - url
      title: CustomLlm
    type_:EmbeddingModelEnum:
      type: string
      enum:
        - e5_mistral_7b_instruct
        - multilingual_e5_large_instruct
      default: e5_mistral_7b_instruct
      title: EmbeddingModelEnum
    type_:RagConfigOutput:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
        embedding_model:
          $ref: '#/components/schemas/type_:EmbeddingModelEnum'
        max_vector_distance:
          type: number
          format: double
          default: 0.6
          description: Maximum vector distance of retrieved chunks.
        max_documents_length:
          type: integer
          default: 50000
          description: Maximum total length of document chunks retrieved from RAG.
        max_retrieved_rag_chunks_count:
          type: integer
          default: 20
          description: >-
            Maximum number of RAG document chunks to initially retrieve from the
            vector store. These are then further filtered by vector distance and
            total length.
        num_candidates:
          type: integer
          description: >-
            Number of candidates evaluated in ANN vector search. Higher number
            means better results, but higher latency. Minimum recommended value
            is 100. If disabled, the default value is used.
        query_rewrite_prompt_override:
          type: string
          description: >-
            Custom prompt for rewriting user queries before RAG retrieval. The
            conversation history will be automatically appended at the end. If
            not set, the default prompt will be used.
      title: RagConfigOutput
    type_:PromptAgentApiModelOutputBackupLlmConfig:
      oneOf:
        - type: object
          properties:
            preference:
              type: string
              enum:
                - default
          required:
            - preference
        - type: object
          properties:
            preference:
              type: string
              enum:
                - disabled
          required:
            - preference
        - type: object
          properties:
            preference:
              type: string
              enum:
                - override
            order:
              type: array
              items:
                $ref: '#/components/schemas/type_:Llm'
          required:
            - preference
            - order
      discriminator:
        propertyName: preference
      description: >-
        Configuration for backup LLM cascading. Can be disabled, use system
        defaults, or specify custom order.
      title: PromptAgentApiModelOutputBackupLlmConfig
    type_:DynamicVariablesConfig:
      type: object
      properties:
        dynamic_variable_placeholders:
          type: object
          additionalProperties:
            description: Any type
          description: A dictionary of dynamic variable placeholders and their values
      title: DynamicVariablesConfig
    type_:ToolExecutionMode:
      type: string
      enum:
        - immediate
        - post_tool_speech
        - async
      default: immediate
      title: ToolExecutionMode
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
    type_:ApiIntegrationWebhookOverridesSchemaOverridesValue:
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
      title: ApiIntegrationWebhookOverridesSchemaOverridesValue
    type_:ApiIntegrationWebhookOverridesRequestHeadersValue:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/type_:ConvAiDynamicVariable'
      title: ApiIntegrationWebhookOverridesRequestHeadersValue
    type_:ResponseFilterMode:
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
    type_:ApiIntegrationWebhookOverrides:
      type: object
      properties:
        schema_overrides:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:ApiIntegrationWebhookOverridesSchemaOverridesValue
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:ApiIntegrationWebhookOverridesRequestHeadersValue
        response_filter_mode:
          $ref: '#/components/schemas/type_:ResponseFilterMode'
        response_filters:
          type: array
          items:
            type: string
      description: |-
        A whitelist of fields that can be overridden by users when
        configuring an API Integration Webhook Tool.
      title: ApiIntegrationWebhookOverrides
    type_:WebhookToolApiSchemaConfigOutputRequestHeadersValue:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
        - $ref: '#/components/schemas/type_:ConvAiDynamicVariable'
        - $ref: '#/components/schemas/type_:ConvAiEnvVarLocator'
      title: WebhookToolApiSchemaConfigOutputRequestHeadersValue
    type_:WebhookToolApiSchemaConfigOutputMethod:
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
    type_:QueryParamsJsonSchema:
      type: object
      properties:
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:LiteralJsonSchemaProperty'
        required:
          type: array
          items:
            type: string
      required:
        - properties
      title: QueryParamsJsonSchema
    type_:ResponseFilter:
      type: object
      properties:
        mode:
          $ref: '#/components/schemas/type_:ResponseFilterMode'
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
          description: >-
            Content type for response filtering. Only 'application/json'
            responses are filtered.
      description: >-
        Configuration for filtering tool responses before they are visible to
        the agent.
      title: ResponseFilter
    type_:WebhookToolApiSchemaConfigOutputContentType:
      type: string
      enum:
        - application/json
        - application/x-www-form-urlencoded
      default: application/json
      description: >-
        Content type for the request body. Only applies to POST/PUT/PATCH
        requests.
      title: WebhookToolApiSchemaConfigOutputContentType
    type_:WebhookToolApiSchemaConfigOutputAuthConnection:
      oneOf:
        - $ref: '#/components/schemas/type_:AuthConnectionLocator'
        - $ref: '#/components/schemas/type_:EnvironmentAuthConnectionLocator'
      description: Optional auth connection to use for authentication with this webhook
      title: WebhookToolApiSchemaConfigOutputAuthConnection
    type_:WebhookToolApiSchemaConfigOutput:
      type: object
      properties:
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:WebhookToolApiSchemaConfigOutputRequestHeadersValue
          description: Headers that should be included in the request
        url:
          type: string
          description: >-
            The URL that the webhook will be sent to. May include path
            parameters, e.g. https://example.com/agents/{agent_id}
        method:
          $ref: '#/components/schemas/type_:WebhookToolApiSchemaConfigOutputMethod'
          default: GET
          description: The HTTP method to use for the webhook
        path_params_schema:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:LiteralJsonSchemaProperty'
          description: >-
            Schema for path parameters, if any. The keys should match the
            placeholders in the URL.
        query_params_schema:
          $ref: '#/components/schemas/type_:QueryParamsJsonSchema'
          description: >-
            Schema for any query params, if any. These will be added to end of
            the URL as query params. Note: properties in a query param must all
            be literal types
        request_body_schema:
          $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyOutput'
          description: >-
            Schema for the body parameters, if any. Used for POST/PATCH/PUT
            requests. The schema should be an object which will be sent as the
            json body
        response_body_schema:
          $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyOutput'
          description: >-
            Schema describing the expected response body structure. For
            documentation only; not surfaced to the LLM.
        response_filter:
          $ref: '#/components/schemas/type_:ResponseFilter'
          description: >-
            Optional allow-list filter applied to the response before the LLM
            sees it, so large responses don't pollute the context. Defaults to
            the full response.
        content_type:
          $ref: >-
            #/components/schemas/type_:WebhookToolApiSchemaConfigOutputContentType
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
          $ref: >-
            #/components/schemas/type_:WebhookToolApiSchemaConfigOutputAuthConnection
          description: Optional auth connection to use for authentication with this webhook
      required:
        - url
      title: WebhookToolApiSchemaConfigOutput
    type_:PromptAgentApiModelOutputToolsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - api_integration_webhook
              description: 'Discriminator value: api_integration_webhook'
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
                complete. Must be between 5 and 300 seconds (inclusive).
            disable_interruptions:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `interruption_mode` instead. If true, the user
                will not be able to interrupt the agent while this tool is
                running.
            interruption_mode:
              $ref: '#/components/schemas/type_:ToolInterruptionMode'
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
              $ref: '#/components/schemas/type_:PreToolSpeechMode'
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/type_:DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              $ref: '#/components/schemas/type_:ToolCallSoundType'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/type_:ToolCallSoundBehavior'
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/type_:ToolErrorHandlingMode'
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            dynamic_variables:
              $ref: '#/components/schemas/type_:DynamicVariablesConfig'
              description: Configuration for dynamic variables
            execution_mode:
              $ref: '#/components/schemas/type_:ToolExecutionMode'
              description: >-
                Determines when and how the tool executes: 'immediate' executes
                the tool right away when requested by the LLM,
                'post_tool_speech' waits for the agent to finish speaking before
                executing, 'async' runs the tool in the background without
                blocking - best for long-running operations.
            tool_version:
              type: string
              default: 1.0.0
              description: The version of the API integration tool
            api_integration_id:
              type: string
            api_integration_connection_id:
              type: string
            api_schema_overrides:
              $ref: '#/components/schemas/type_:ApiIntegrationWebhookOverrides'
              description: User overrides applied on top of the base api_schema
          required:
            - type
            - name
            - description
            - response_timeout_secs
            - disable_interruptions
            - interruption_mode
            - force_pre_tool_speech
            - pre_tool_speech
            - assignments
            - tool_call_sound_behavior
            - tool_error_handling_mode
            - dynamic_variables
            - execution_mode
            - tool_version
            - api_integration_id
            - api_integration_connection_id
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
              $ref: '#/components/schemas/type_:ToolInterruptionMode'
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
              $ref: '#/components/schemas/type_:PreToolSpeechMode'
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/type_:DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              $ref: '#/components/schemas/type_:ToolCallSoundType'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/type_:ToolCallSoundBehavior'
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/type_:ToolErrorHandlingMode'
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            parameters:
              $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyOutput'
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
              $ref: '#/components/schemas/type_:DynamicVariablesConfig'
              description: Configuration for dynamic variables
            execution_mode:
              $ref: '#/components/schemas/type_:ToolExecutionMode'
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
        - type: object
          properties:
            type:
              type: string
              enum:
                - mcp
              description: 'Discriminator value: mcp'
            value:
              description: Any type
          required:
            - type
            - value
        - type: object
          properties:
            type:
              type: string
              enum:
                - smb
              description: 'Discriminator value: smb'
            value:
              description: Any type
          required:
            - type
            - value
        - type: object
          properties:
            type:
              type: string
              enum:
                - system
              description: The type of tool
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
              $ref: '#/components/schemas/type_:ToolInterruptionMode'
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
              $ref: '#/components/schemas/type_:PreToolSpeechMode'
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/type_:DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              $ref: '#/components/schemas/type_:ToolCallSoundType'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/type_:ToolCallSoundBehavior'
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/type_:ToolErrorHandlingMode'
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            params:
              $ref: '#/components/schemas/type_:SystemToolConfigOutputParams'
          required:
            - type
            - name
            - params
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
              description: 'Discriminator value: webhook'
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
                complete. Must be between 5 and 300 seconds (inclusive).
            disable_interruptions:
              type: boolean
              default: false
              description: >-
                DEPRECATED: use `interruption_mode` instead. If true, the user
                will not be able to interrupt the agent while this tool is
                running.
            interruption_mode:
              $ref: '#/components/schemas/type_:ToolInterruptionMode'
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
              $ref: '#/components/schemas/type_:PreToolSpeechMode'
              description: >-
                Controls whether the agent speaks before this tool is called.
                'auto' (default) decides based on recent tool latency, 'force'
                always asks the agent to speak, 'off' fully opts out regardless
                of latency.
            assignments:
              type: array
              items:
                $ref: '#/components/schemas/type_:DynamicVariableAssignment'
              description: >-
                Configuration for extracting values from tool responses and
                assigning them to dynamic variables
            tool_call_sound:
              $ref: '#/components/schemas/type_:ToolCallSoundType'
              description: >-
                Predefined tool call sound type to play during tool execution.
                If not specified, no tool call sound will be played.
            tool_call_sound_behavior:
              $ref: '#/components/schemas/type_:ToolCallSoundBehavior'
              description: >-
                Determines when the tool call sound should play. 'auto' only
                plays when there's pre-tool speech, 'always' plays for every
                tool call.
            tool_error_handling_mode:
              $ref: '#/components/schemas/type_:ToolErrorHandlingMode'
              description: >-
                Controls how tool errors are processed before being shared with
                the agent. 'auto' determines handling based on tool type
                (summarized for native integrations, hide for others),
                'summarized' sends an LLM-generated summary, 'passthrough' sends
                the raw error, 'hide' does not share the error with the agent.
            dynamic_variables:
              $ref: '#/components/schemas/type_:DynamicVariablesConfig'
              description: Configuration for dynamic variables
            execution_mode:
              $ref: '#/components/schemas/type_:ToolExecutionMode'
              description: >-
                Determines when and how the tool executes: 'immediate' executes
                the tool right away when requested by the LLM,
                'post_tool_speech' waits for the agent to finish speaking before
                executing, 'async' runs the tool in the background without
                blocking - best for long-running operations.
            api_schema:
              $ref: '#/components/schemas/type_:WebhookToolApiSchemaConfigOutput'
              description: >-
                The schema for the outgoing webhoook, including parameters and
                URL specification
          required:
            - type
            - name
            - description
            - api_schema
      discriminator:
        propertyName: type
      description: The type of tool
      title: PromptAgentApiModelOutputToolsItem
    type_:PromptAgentApiModelOutput:
      type: object
      properties:
        prompt:
          type: string
          default: ''
          description: The prompt for the agent
        llm:
          $ref: '#/components/schemas/type_:Llm'
          description: >-
            The LLM to query with the prompt and the chat history. If using data
            residency, the LLM must be supported in the data residency
            environment
        reasoning_effort:
          $ref: '#/components/schemas/type_:LlmReasoningEffort'
          description: Reasoning effort of the model. Only available for some models.
        thinking_budget:
          type: integer
          description: >-
            Max number of tokens used for thinking. Use 0 to turn off if
            supported by the model.
        enable_reasoning_summary:
          type: boolean
          default: false
          description: >-
            Enable model reasoning summaries. When disabled, we do not request
            summaries from provider if possible for faster TTFB. Not ZRM
            compatible.
        temperature:
          type: number
          format: double
          description: >-
            The temperature for the LLM. Defaults to 0. Set to null to omit the
            parameter from the LLM request entirely (useful for custom LLMs that
            reject the temperature field).
        max_tokens:
          type: integer
          default: -1
          description: If greater than 0, maximum number of tokens the LLM can predict
        tool_ids:
          type: array
          items:
            type: string
          description: A list of IDs of tools used by the agent
        built_in_tools:
          $ref: '#/components/schemas/type_:BuiltInToolsOutput'
          description: Built-in system tools to be used by the agent
        mcp_server_ids:
          type: array
          items:
            type: string
          description: A list of MCP server ids to be used by the agent
        native_mcp_server_ids:
          type: array
          items:
            type: string
          description: A list of Native MCP server ids to be used by the agent
        knowledge_base:
          type: array
          items:
            $ref: '#/components/schemas/type_:KnowledgeBaseLocator'
          description: A list of knowledge bases to be used by the agent
        custom_llm:
          $ref: '#/components/schemas/type_:CustomLlm'
          description: Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
        ignore_default_personality:
          type: boolean
          description: >-
            Whether to remove the default personality lines from the system
            prompt
        rag:
          $ref: '#/components/schemas/type_:RagConfigOutput'
          description: Configuration for RAG
        timezone:
          type: string
          description: >-
            Timezone for displaying current time in system prompt. If set, the
            current time will be included in the system prompt using this
            timezone. Must be a valid timezone name (e.g., 'America/New_York',
            'Europe/London', 'UTC'). Recommended for accurate time-aware
            responses; without this, the agent has no knowledge of the current
            date/time unless you provide it via dynamic variables or tools,
            which can lead to incorrect or hallucinated time references.
        backup_llm_config:
          $ref: '#/components/schemas/type_:PromptAgentApiModelOutputBackupLlmConfig'
          description: >-
            Configuration for backup LLM cascading. Can be disabled, use system
            defaults, or specify custom order.
        cascade_timeout_seconds:
          type: number
          format: double
          default: 4
          description: >-
            Time in seconds before cascading to backup LLM. Must be between 2
            and 15 seconds.
        tools:
          type: array
          items:
            $ref: '#/components/schemas/type_:PromptAgentApiModelOutputToolsItem'
          description: >-
            A list of tools that the agent can use over the course of the
            conversation, use tool_ids instead
      title: PromptAgentApiModelOutput
    type_:AgentConfig:
      type: object
      properties:
        first_message:
          type: string
          default: ''
          description: >-
            If non-empty, the first message the agent will say. If empty, the
            agent waits for the user to start the discussion.
        language:
          type: string
          default: en
          description: Language of the agent - used for ASR and TTS
        hinglish_mode:
          type: boolean
          default: false
          description: >-
            When enabled and language is Hindi, the agent will respond in
            Hinglish
        dynamic_variables:
          description: Any type
        disable_first_message_interruptions:
          type: boolean
          default: false
          description: >-
            If true, the user will not be able to interrupt the agent while the
            first message is being delivered.
        max_conversation_duration_message:
          type: string
          default: ''
          description: >-
            If non-empty, the message the agent will send when max conversation
            duration is reached.
        text_behavior_overrides:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:BehaviorOverride'
          description: >-
            Per-channel response behavior overrides for text conversations.
            Built-in channel defaults apply when unset.
        prompt:
          $ref: '#/components/schemas/type_:PromptAgentApiModelOutput'
          description: The prompt for the agent
      title: AgentConfig
    type_:ToolMockConfig:
      type: object
      properties:
        default_return_value:
          type: string
          default: Tool Called.
        default_is_error:
          type: boolean
          default: false
      title: ToolMockConfig
    type_:ConversationHistoryTranscriptCommonModelInputRole:
      type: string
      enum:
        - user
        - agent
      title: ConversationHistoryTranscriptCommonModelInputRole
    type_:AgentMetadata:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type: string
        workflow_node_id:
          type: string
        version_id:
          type: string
      required:
        - agent_id
      title: AgentMetadata
    type_:ConversationHistoryMultivoiceMessagePartModel:
      type: object
      properties:
        text:
          type: string
        voice_label:
          type: string
        time_in_call_secs:
          type: integer
      required:
        - text
      description: Represents a single voice part of a multi-voice message.
      title: ConversationHistoryMultivoiceMessagePartModel
    type_:ConversationHistoryMultivoiceMessageModel:
      type: object
      properties:
        parts:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryMultivoiceMessagePartModel
      required:
        - parts
      description: Represents a message from a multi-voice agent.
      title: ConversationHistoryMultivoiceMessageModel
    type_:ToolType:
      type: string
      enum:
        - system
        - webhook
        - client
        - mcp
        - workflow
        - api_integration_webhook
        - api_integration_mcp
        - smb
      title: ToolType
    type_:ConversationHistoryTranscriptToolCallWebhookDetails:
      type: object
      properties:
        type:
          type: string
          enum:
            - webhook
        method:
          type: string
        url:
          type: string
        headers:
          type: object
          additionalProperties:
            type: string
        path_params:
          type: object
          additionalProperties:
            type: string
        query_params:
          type: object
          additionalProperties:
            type: string
        body:
          type: string
      required:
        - method
        - url
      title: ConversationHistoryTranscriptToolCallWebhookDetails
    type_:ConversationHistoryTranscriptToolCallCommonModelInputToolDetails:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - api_integration_webhook
              description: 'Discriminator value: api_integration_webhook'
            integration_id:
              type: string
              default: ''
            credential_id:
              type: string
              default: ''
            integration_connection_id:
              type: string
              default: ''
            webhook_details:
              $ref: >-
                #/components/schemas/type_:ConversationHistoryTranscriptToolCallWebhookDetails
          required:
            - type
            - webhook_details
        - type: object
          properties:
            type:
              type: string
              enum:
                - client
              description: 'Discriminator value: client'
            parameters:
              type: string
          required:
            - type
            - parameters
        - type: object
          properties:
            type:
              type: string
              enum:
                - mcp
              description: 'Discriminator value: mcp'
            mcp_server_id:
              type: string
            mcp_server_name:
              type: string
            integration_type:
              type: string
            parameters:
              type: object
              additionalProperties:
                type: string
            approval_policy:
              type: string
            requires_approval:
              type: boolean
              default: false
            mcp_tool_name:
              type: string
              default: ''
            mcp_tool_description:
              type: string
              default: ''
          required:
            - type
            - mcp_server_id
            - mcp_server_name
            - integration_type
            - approval_policy
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
            method:
              type: string
            url:
              type: string
            headers:
              type: object
              additionalProperties:
                type: string
            path_params:
              type: object
              additionalProperties:
                type: string
            query_params:
              type: object
              additionalProperties:
                type: string
            body:
              type: string
          required:
            - type
            - method
            - url
      discriminator:
        propertyName: type
      title: ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
    type_:ConversationHistoryTranscriptToolCallCommonModelInput:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:ToolType'
        request_id:
          type: string
        tool_name:
          type: string
        params_as_json:
          type: string
        tool_has_been_called:
          type: boolean
        tool_details:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
      required:
        - request_id
        - tool_name
        - params_as_json
        - tool_has_been_called
      title: ConversationHistoryTranscriptToolCallCommonModelInput
    type_:DynamicVariableUpdateCommonModel:
      type: object
      properties:
        variable_name:
          type: string
        old_value:
          type: string
        new_value:
          type: string
        updated_at:
          type: number
          format: double
        tool_name:
          type: string
        tool_request_id:
          type: string
      required:
        - variable_name
        - new_value
        - updated_at
        - tool_name
        - tool_request_id
      description: Tracks a dynamic variable update that occurred during tool execution.
      title: DynamicVariableUpdateCommonModel
    type_:ConversationHistoryTranscriptOtherToolsResultCommonModelType:
      type: string
      enum:
        - client
        - webhook
        - mcp
        - code
      title: ConversationHistoryTranscriptOtherToolsResultCommonModelType
    type_:ConversationHistoryTranscriptOtherToolsResultCommonModel:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        is_blocked:
          type: boolean
          default: false
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
          default: 0
        error_type:
          type: string
          default: ''
        raw_error_message:
          type: string
          default: ''
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableUpdateCommonModel'
        type:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptOtherToolsResultCommonModelType
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
      title: ConversationHistoryTranscriptOtherToolsResultCommonModel
    type_:KnowledgeBaseRagToolStatus:
      type: string
      enum:
        - success
        - no_documents
        - no_results
      default: success
      title: KnowledgeBaseRagToolStatus
    type_:KnowledgeBaseRagChunkModel:
      type: object
      properties:
        chunk_id:
          type: string
        document_id:
          type: string
        content:
          type: string
      required:
        - chunk_id
        - document_id
        - content
      title: KnowledgeBaseRagChunkModel
    type_:KnowledgeBaseToolStatus:
      type: string
      enum:
        - success
        - no_matching_documents
        - no_results
      default: success
      title: KnowledgeBaseToolStatus
    type_:TransferToAgentToolResultSuccessModelInputBranchInfo:
      oneOf:
        - type: object
          properties:
            branch_reason:
              type: string
              enum:
                - defaulting_to_main
              description: 'Discriminator value: defaulting_to_main'
            branch_id:
              type: string
          required:
            - branch_reason
            - branch_id
        - type: object
          properties:
            branch_reason:
              type: string
              enum:
                - traffic_split
              description: 'Discriminator value: traffic_split'
            branch_id:
              type: string
            traffic_percentage:
              type: number
              format: double
          required:
            - branch_reason
            - branch_id
            - traffic_percentage
      discriminator:
        propertyName: branch_reason
      title: TransferToAgentToolResultSuccessModelInputBranchInfo
    type_:ConversationHistoryTranscriptSystemToolResultCommonModelInputResult:
      oneOf:
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - dummy
              description: 'Discriminator value: dummy'
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - end_call_success
              description: 'Discriminator value: end_call_success'
            status:
              type: string
              enum:
                - success
            reason:
              type: string
            message:
              type: string
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - knowledge_base_rag_success
              description: 'Discriminator value: knowledge_base_rag_success'
            status:
              $ref: '#/components/schemas/type_:KnowledgeBaseRagToolStatus'
            chunk_count:
              type: integer
              default: 0
              description: Number of relevant chunks retrieved
            message:
              type: string
              default: Referenced knowledge base.
              description: Human-readable status for the LLM about the search results
            chunks:
              type: array
              items:
                $ref: '#/components/schemas/type_:KnowledgeBaseRagChunkModel'
              description: >-
                Retrieved chunks; populated only in the
                rag-result-in-tool-result mode
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - knowledge_base_success
              description: 'Discriminator value: knowledge_base_success'
            status:
              $ref: '#/components/schemas/type_:KnowledgeBaseToolStatus'
            chunk_count:
              type: integer
              default: 0
            message:
              type: string
              default: Referenced knowledge base.
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - language_detection_success
              description: 'Discriminator value: language_detection_success'
            status:
              type: string
              enum:
                - success
            reason:
              type: string
            language:
              type: string
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - play_dtmf_error
              description: 'Discriminator value: play_dtmf_error'
            status:
              type: string
              enum:
                - error
            error:
              type: string
            details:
              type: string
          required:
            - result_type
            - error
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - play_dtmf_success
              description: 'Discriminator value: play_dtmf_success'
            status:
              type: string
              enum:
                - success
            dtmf_tones:
              type: string
            reason:
              type: string
          required:
            - result_type
            - dtmf_tones
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - skip_turn_success
              description: 'Discriminator value: skip_turn_success'
            status:
              type: string
              enum:
                - success
            reason:
              type: string
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - testing_tool_result
              description: 'Discriminator value: testing_tool_result'
            status:
              type: string
              enum:
                - success
            reason:
              type: string
              default: Skipping tool call in test mode
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_agent_error
              description: 'Discriminator value: transfer_to_agent_error'
            status:
              type: string
              enum:
                - error
            from_agent:
              type: string
            error:
              type: string
          required:
            - result_type
            - from_agent
            - error
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_agent_success
              description: 'Discriminator value: transfer_to_agent_success'
            status:
              type: string
              enum:
                - success
            from_agent:
              type: string
            to_agent:
              type: string
            to_node:
              type: string
            condition:
              type: string
            delay_ms:
              type: integer
              default: 0
            transfer_message:
              type: string
            enable_transferred_agent_first_message:
              type: boolean
              default: false
            branch_info:
              $ref: >-
                #/components/schemas/type_:TransferToAgentToolResultSuccessModelInputBranchInfo
            preserve_client_tts_overrides:
              type: boolean
              default: false
          required:
            - result_type
            - from_agent
            - to_agent
            - condition
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_error
              description: 'Discriminator value: transfer_to_number_error'
            status:
              type: string
              enum:
                - error
            error:
              type: string
            details:
              type: string
          required:
            - result_type
            - error
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_exotel_success
              description: 'Discriminator value: transfer_to_number_exotel_success'
            status:
              type: string
              enum:
                - success
            transfer_number:
              type: string
            reason:
              type: string
            agent_message:
              type: string
            note:
              type: string
          required:
            - result_type
            - transfer_number
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_sip_success
              description: 'Discriminator value: transfer_to_number_sip_success'
            status:
              type: string
              enum:
                - success
            transfer_number:
              type: string
            reason:
              type: string
            note:
              type: string
          required:
            - result_type
            - transfer_number
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_twilio_success
              description: 'Discriminator value: transfer_to_number_twilio_success'
            status:
              type: string
              enum:
                - success
            transfer_number:
              type: string
            reason:
              type: string
            client_message:
              type: string
            agent_message:
              type: string
            conference_name:
              type: string
            post_dial_digits:
              type: string
            note:
              type: string
          required:
            - result_type
            - transfer_number
            - agent_message
            - conference_name
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - voicemail_detection_success
              description: 'Discriminator value: voicemail_detection_success'
            status:
              type: string
              enum:
                - success
            voicemail_message:
              type: string
            reason:
              type: string
          required:
            - result_type
      discriminator:
        propertyName: result_type
      title: ConversationHistoryTranscriptSystemToolResultCommonModelInputResult
    type_:ConversationHistoryTranscriptSystemToolResultCommonModelInput:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        is_blocked:
          type: boolean
          default: false
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
          default: 0
        error_type:
          type: string
          default: ''
        raw_error_message:
          type: string
          default: ''
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - system
        result:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptSystemToolResultCommonModelInputResult
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: ConversationHistoryTranscriptSystemToolResultCommonModelInput
    type_:ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelInput:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        is_blocked:
          type: boolean
          default: false
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
          default: 0
        error_type:
          type: string
          default: ''
        raw_error_message:
          type: string
          default: ''
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - api_integration_webhook
        integration_id:
          type: string
          default: ''
        credential_id:
          type: string
          default: ''
        integration_connection_id:
          type: string
          default: ''
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: >-
        ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelInput
    type_:WorkflowToolNestedToolsStepModelInputResultsItem:
      oneOf:
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptSystemToolResultCommonModelInput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelInput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptWorkflowToolsResultCommonModelInput
      title: WorkflowToolNestedToolsStepModelInputResultsItem
    type_:WorkflowToolResponseModelInputStepsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - edge
              description: 'Discriminator value: edge'
            step_latency_secs:
              type: number
              format: double
            edge_id:
              type: string
            target_node_id:
              type: string
          required:
            - type
            - step_latency_secs
            - edge_id
            - target_node_id
        - type: object
          properties:
            type:
              type: string
              enum:
                - max_iterations_exceeded
              description: 'Discriminator value: max_iterations_exceeded'
            step_latency_secs:
              type: number
              format: double
            max_iterations:
              type: integer
          required:
            - type
            - step_latency_secs
            - max_iterations
        - type: object
          properties:
            type:
              type: string
              enum:
                - nested_tools
              description: 'Discriminator value: nested_tools'
            step_latency_secs:
              type: number
              format: double
            node_id:
              type: string
            requests:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:ConversationHistoryTranscriptToolCallCommonModelInput
            results:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:WorkflowToolNestedToolsStepModelInputResultsItem
            is_successful:
              type: boolean
          required:
            - type
            - step_latency_secs
            - node_id
            - requests
            - results
            - is_successful
      discriminator:
        propertyName: type
      title: WorkflowToolResponseModelInputStepsItem
    type_:WorkflowToolResponseModelInput:
      type: object
      properties:
        steps:
          type: array
          items:
            $ref: '#/components/schemas/type_:WorkflowToolResponseModelInputStepsItem'
      description: A common model for workflow tool responses.
      title: WorkflowToolResponseModelInput
    type_:ConversationHistoryTranscriptWorkflowToolsResultCommonModelInput:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        is_blocked:
          type: boolean
          default: false
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
          default: 0
        error_type:
          type: string
          default: ''
        raw_error_message:
          type: string
          default: ''
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - workflow
        result:
          $ref: '#/components/schemas/type_:WorkflowToolResponseModelInput'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: ConversationHistoryTranscriptWorkflowToolsResultCommonModelInput
    type_:ConversationHistoryTranscriptCommonModelInputToolResultsItem:
      oneOf:
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptSystemToolResultCommonModelInput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelInput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptWorkflowToolsResultCommonModelInput
      title: ConversationHistoryTranscriptCommonModelInputToolResultsItem
    type_:UserFeedbackScore:
      type: string
      enum:
        - like
        - dislike
      title: UserFeedbackScore
    type_:UserFeedback:
      type: object
      properties:
        score:
          $ref: '#/components/schemas/type_:UserFeedbackScore'
        time_in_call_secs:
          type: integer
      required:
        - score
        - time_in_call_secs
      title: UserFeedback
    type_:MetricRecord:
      type: object
      properties:
        elapsed_time:
          type: number
          format: double
      required:
        - elapsed_time
      title: MetricRecord
    type_:ConversationTurnMetrics:
      type: object
      properties:
        metrics:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:MetricRecord'
        convai_asr_provider:
          type: string
        convai_tts_model:
          type: string
        convai_tts_cascade:
          type: string
      title: ConversationTurnMetrics
    type_:RagChunkMetadata:
      type: object
      properties:
        document_id:
          type: string
        chunk_id:
          type: string
        vector_distance:
          type: number
          format: double
      required:
        - document_id
        - chunk_id
        - vector_distance
      title: RagChunkMetadata
    type_:RagRetrievalInfo:
      type: object
      properties:
        chunks:
          type: array
          items:
            $ref: '#/components/schemas/type_:RagChunkMetadata'
        embedding_model:
          $ref: '#/components/schemas/type_:EmbeddingModelEnum'
        retrieval_query:
          type: string
        rag_latency_secs:
          type: number
          format: double
        used_chunk_ids:
          type: array
          items:
            type: string
      required:
        - chunks
        - embedding_model
        - retrieval_query
        - rag_latency_secs
      title: RagRetrievalInfo
    type_:LlmTokensCategoryUsage:
      type: object
      properties:
        tokens:
          type: integer
          default: 0
        price:
          type: number
          format: double
          default: 0
      title: LlmTokensCategoryUsage
    type_:LlmInputOutputTokensUsage:
      type: object
      properties:
        input:
          $ref: '#/components/schemas/type_:LlmTokensCategoryUsage'
        input_cache_read:
          $ref: '#/components/schemas/type_:LlmTokensCategoryUsage'
        input_cache_write:
          $ref: '#/components/schemas/type_:LlmTokensCategoryUsage'
        output_total:
          $ref: '#/components/schemas/type_:LlmTokensCategoryUsage'
      title: LlmInputOutputTokensUsage
    type_:LlmUsageInput:
      type: object
      properties:
        model_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:LlmInputOutputTokensUsage'
      title: LlmUsageInput
    type_:ConversationReasoningModel:
      type: object
      properties:
        summary:
          type: string
        provider_redact:
          type: boolean
          default: false
      title: ConversationReasoningModel
    type_:ChatSourceMedium:
      type: string
      enum:
        - audio
        - text
        - image
        - file
      title: ChatSourceMedium
    type_:GuardrailType:
      type: string
      enum:
        - custom
        - prompt_injection
        - self_harm_intent
        - violence_graphic
        - sexual
        - violence
        - harassment
        - sexual_minors
        - self_harm
        - self_harm_instructions
        - harassment_threatening
        - hate
        - hate_threatening
        - profanity
        - religion_or_politics
        - medical_and_legal
        - guardrail
      title: GuardrailType
    type_:TriggeredGuardrailCommonModel:
      type: object
      properties:
        guardrail_type:
          $ref: '#/components/schemas/type_:GuardrailType'
        guardrail_name:
          type: string
      required:
        - guardrail_type
      title: TriggeredGuardrailCommonModel
    type_:ConversationHistoryTranscriptCommonModelInput:
      type: object
      properties:
        role:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptCommonModelInputRole
        agent_metadata:
          $ref: '#/components/schemas/type_:AgentMetadata'
        message:
          type: string
        multivoice_message:
          $ref: '#/components/schemas/type_:ConversationHistoryMultivoiceMessageModel'
        tool_calls:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptToolCallCommonModelInput
        tool_results:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptCommonModelInputToolResultsItem
        feedback:
          $ref: '#/components/schemas/type_:UserFeedback'
        llm_override:
          type: string
        time_in_call_secs:
          type: integer
        conversation_turn_metrics:
          $ref: '#/components/schemas/type_:ConversationTurnMetrics'
        rag_retrieval_info:
          $ref: '#/components/schemas/type_:RagRetrievalInfo'
        llm_usage:
          $ref: '#/components/schemas/type_:LlmUsageInput'
        interrupted:
          type: boolean
          default: false
        ignored_as_backchannel:
          type: boolean
          default: false
        original_message:
          type: string
        reasoning:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConversationReasoningModel'
        source_medium:
          $ref: '#/components/schemas/type_:ChatSourceMedium'
        source_event_id:
          type: integer
        used_static_kb_document_ids:
          type: array
          items:
            type: string
        user_identifier:
          type: string
        id:
          type: string
        triggered_guardrails:
          type: array
          items:
            $ref: '#/components/schemas/type_:TriggeredGuardrailCommonModel'
      required:
        - role
        - time_in_call_secs
      title: ConversationHistoryTranscriptCommonModelInput
    type_:ConversationSimulationSpecification:
      type: object
      properties:
        simulated_user_config:
          $ref: '#/components/schemas/type_:AgentConfig'
        tool_mock_config:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:ToolMockConfig'
        partial_conversation_history:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptCommonModelInput
          description: >-
            A partial conversation history to start the simulation from. If
            empty, simulation starts fresh.
        dynamic_variables:
          type: object
          additionalProperties:
            description: Any type
      required:
        - simulated_user_config
      description: >-
        A specification that will be used to simulate a conversation between an
        agent and an AI user.
      title: ConversationSimulationSpecification
    type_:AnalysisScope:
      type: string
      enum:
        - conversation
        - agent
      default: conversation
      title: AnalysisScope
    type_:CriteriaScoringMode:
      type: string
      enum:
        - binary
        - numeric_uniform
      default: binary
      title: CriteriaScoringMode
    type_:PromptEvaluationCriteria:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier for the evaluation criteria
        name:
          type: string
        type:
          type: string
          enum:
            - prompt
          description: The type of evaluation criteria
        conversation_goal_prompt:
          type: string
          description: The prompt that the agent should use to evaluate the conversation
        use_knowledge_base:
          type: boolean
          default: false
          description: >-
            When evaluating the prompt, should the agent's knowledge base be
            used.
        scope:
          $ref: '#/components/schemas/type_:AnalysisScope'
          description: >-
            The scope of transcript context used when evaluating this criterion.
            'conversation' uses the full transcript; 'agent' uses only the
            portion where the defining agent was active.
        llm:
          $ref: '#/components/schemas/type_:Llm'
          description: >-
            LLM model to use for this evaluation criteria. If not set, uses
            agent's analysis_llm default.
        scoring_mode:
          $ref: '#/components/schemas/type_:CriteriaScoringMode'
          description: >-
            How this criterion is scored. 'binary' resolves to
            success/failure/unknown. 'numeric_uniform' returns a number on the
            [0, max_score] scale which is normalized into the aggregate
            conversation success percentage.
        max_score:
          type: integer
          default: 100
          description: >-
            Maximum value of the numeric score scale (minimum is always 0). Only
            used when scoring_mode is 'numeric_uniform'.
        score_instructions:
          type: string
          description: >-
            Optional free-text instructions describing how to assign values on
            the numeric scale. Only used when scoring_mode is 'numeric_uniform'.
      required:
        - id
        - name
        - conversation_goal_prompt
      description: >-
        An evaluation using the transcript and a prompt for a yes/no achieved
        answer
      title: PromptEvaluationCriteria
    type_:ConversationHistoryTranscriptResponseModelRole:
      type: string
      enum:
        - user
        - agent
      title: ConversationHistoryTranscriptResponseModelRole
    type_:ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - api_integration_webhook
              description: 'Discriminator value: api_integration_webhook'
            integration_id:
              type: string
              default: ''
            credential_id:
              type: string
              default: ''
            integration_connection_id:
              type: string
              default: ''
            webhook_details:
              $ref: >-
                #/components/schemas/type_:ConversationHistoryTranscriptToolCallWebhookDetails
          required:
            - type
            - integration_id
            - credential_id
            - integration_connection_id
            - webhook_details
        - type: object
          properties:
            type:
              type: string
              enum:
                - client
              description: 'Discriminator value: client'
            parameters:
              type: string
          required:
            - type
            - parameters
        - type: object
          properties:
            type:
              type: string
              enum:
                - mcp
              description: 'Discriminator value: mcp'
            mcp_server_id:
              type: string
            mcp_server_name:
              type: string
            integration_type:
              type: string
            parameters:
              type: object
              additionalProperties:
                type: string
            approval_policy:
              type: string
            requires_approval:
              type: boolean
              default: false
            mcp_tool_name:
              type: string
              default: ''
            mcp_tool_description:
              type: string
              default: ''
          required:
            - type
            - mcp_server_id
            - mcp_server_name
            - integration_type
            - approval_policy
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
            method:
              type: string
            url:
              type: string
            headers:
              type: object
              additionalProperties:
                type: string
            path_params:
              type: object
              additionalProperties:
                type: string
            query_params:
              type: object
              additionalProperties:
                type: string
            body:
              type: string
          required:
            - type
            - method
            - url
      discriminator:
        propertyName: type
      title: ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails
    type_:ConversationHistoryTranscriptToolCallCommonModelOutput:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:ToolType'
        request_id:
          type: string
        tool_name:
          type: string
        params_as_json:
          type: string
        tool_has_been_called:
          type: boolean
        tool_details:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails
      required:
        - request_id
        - tool_name
        - params_as_json
        - tool_has_been_called
      title: ConversationHistoryTranscriptToolCallCommonModelOutput
    type_:TransferToAgentToolResultSuccessModelOutputBranchInfo:
      oneOf:
        - type: object
          properties:
            branch_reason:
              type: string
              enum:
                - defaulting_to_main
              description: 'Discriminator value: defaulting_to_main'
            branch_id:
              type: string
          required:
            - branch_reason
            - branch_id
        - type: object
          properties:
            branch_reason:
              type: string
              enum:
                - traffic_split
              description: 'Discriminator value: traffic_split'
            branch_id:
              type: string
            traffic_percentage:
              type: number
              format: double
          required:
            - branch_reason
            - branch_id
            - traffic_percentage
      discriminator:
        propertyName: branch_reason
      title: TransferToAgentToolResultSuccessModelOutputBranchInfo
    type_:ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult:
      oneOf:
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - dummy
              description: 'Discriminator value: dummy'
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - end_call_success
              description: 'Discriminator value: end_call_success'
            status:
              type: string
              enum:
                - success
            reason:
              type: string
            message:
              type: string
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - knowledge_base_rag_success
              description: 'Discriminator value: knowledge_base_rag_success'
            status:
              $ref: '#/components/schemas/type_:KnowledgeBaseRagToolStatus'
            chunk_count:
              type: integer
              default: 0
              description: Number of relevant chunks retrieved
            message:
              type: string
              default: Referenced knowledge base.
              description: Human-readable status for the LLM about the search results
            chunks:
              type: array
              items:
                $ref: '#/components/schemas/type_:KnowledgeBaseRagChunkModel'
              description: >-
                Retrieved chunks; populated only in the
                rag-result-in-tool-result mode
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - knowledge_base_success
              description: 'Discriminator value: knowledge_base_success'
            status:
              $ref: '#/components/schemas/type_:KnowledgeBaseToolStatus'
            chunk_count:
              type: integer
              default: 0
            message:
              type: string
              default: Referenced knowledge base.
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - language_detection_success
              description: 'Discriminator value: language_detection_success'
            status:
              type: string
              enum:
                - success
            reason:
              type: string
            language:
              type: string
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - play_dtmf_error
              description: 'Discriminator value: play_dtmf_error'
            status:
              type: string
              enum:
                - error
            error:
              type: string
            details:
              type: string
          required:
            - result_type
            - error
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - play_dtmf_success
              description: 'Discriminator value: play_dtmf_success'
            status:
              type: string
              enum:
                - success
            dtmf_tones:
              type: string
            reason:
              type: string
          required:
            - result_type
            - dtmf_tones
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - skip_turn_success
              description: 'Discriminator value: skip_turn_success'
            status:
              type: string
              enum:
                - success
            reason:
              type: string
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - testing_tool_result
              description: 'Discriminator value: testing_tool_result'
            status:
              type: string
              enum:
                - success
            reason:
              type: string
              default: Skipping tool call in test mode
          required:
            - result_type
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_agent_error
              description: 'Discriminator value: transfer_to_agent_error'
            status:
              type: string
              enum:
                - error
            from_agent:
              type: string
            error:
              type: string
          required:
            - result_type
            - from_agent
            - error
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_agent_success
              description: 'Discriminator value: transfer_to_agent_success'
            status:
              type: string
              enum:
                - success
            from_agent:
              type: string
            to_agent:
              type: string
            to_node:
              type: string
            condition:
              type: string
            delay_ms:
              type: integer
              default: 0
            transfer_message:
              type: string
            enable_transferred_agent_first_message:
              type: boolean
              default: false
            branch_info:
              $ref: >-
                #/components/schemas/type_:TransferToAgentToolResultSuccessModelOutputBranchInfo
            preserve_client_tts_overrides:
              type: boolean
              default: false
          required:
            - result_type
            - from_agent
            - to_agent
            - condition
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_error
              description: 'Discriminator value: transfer_to_number_error'
            status:
              type: string
              enum:
                - error
            error:
              type: string
            details:
              type: string
          required:
            - result_type
            - error
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_exotel_success
              description: 'Discriminator value: transfer_to_number_exotel_success'
            status:
              type: string
              enum:
                - success
            transfer_number:
              type: string
            reason:
              type: string
            agent_message:
              type: string
            note:
              type: string
          required:
            - result_type
            - transfer_number
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_sip_success
              description: 'Discriminator value: transfer_to_number_sip_success'
            status:
              type: string
              enum:
                - success
            transfer_number:
              type: string
            reason:
              type: string
            note:
              type: string
          required:
            - result_type
            - transfer_number
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_twilio_success
              description: 'Discriminator value: transfer_to_number_twilio_success'
            status:
              type: string
              enum:
                - success
            transfer_number:
              type: string
            reason:
              type: string
            client_message:
              type: string
            agent_message:
              type: string
            conference_name:
              type: string
            post_dial_digits:
              type: string
            note:
              type: string
          required:
            - result_type
            - transfer_number
            - agent_message
            - conference_name
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - voicemail_detection_success
              description: 'Discriminator value: voicemail_detection_success'
            status:
              type: string
              enum:
                - success
            voicemail_message:
              type: string
            reason:
              type: string
          required:
            - result_type
      discriminator:
        propertyName: result_type
      title: ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
    type_:ConversationHistoryTranscriptSystemToolResultCommonModelOutput:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        is_blocked:
          type: boolean
          default: false
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
          default: 0
        error_type:
          type: string
          default: ''
        raw_error_message:
          type: string
          default: ''
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - system
        result:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: ConversationHistoryTranscriptSystemToolResultCommonModelOutput
    type_:ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        is_blocked:
          type: boolean
          default: false
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
          default: 0
        error_type:
          type: string
          default: ''
        raw_error_message:
          type: string
          default: ''
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - api_integration_webhook
        integration_id:
          type: string
          default: ''
        credential_id:
          type: string
          default: ''
        integration_connection_id:
          type: string
          default: ''
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - is_blocked
        - tool_has_been_called
        - tool_latency_secs
        - error_type
        - raw_error_message
        - dynamic_variable_updates
        - type
        - integration_id
        - credential_id
        - integration_connection_id
      title: >-
        ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput
    type_:WorkflowToolNestedToolsStepModelOutputResultsItem:
      oneOf:
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptSystemToolResultCommonModelOutput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput
      title: WorkflowToolNestedToolsStepModelOutputResultsItem
    type_:WorkflowToolResponseModelOutputStepsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - edge
              description: 'Discriminator value: edge'
            step_latency_secs:
              type: number
              format: double
            edge_id:
              type: string
            target_node_id:
              type: string
          required:
            - type
            - step_latency_secs
            - edge_id
            - target_node_id
        - type: object
          properties:
            type:
              type: string
              enum:
                - max_iterations_exceeded
              description: 'Discriminator value: max_iterations_exceeded'
            step_latency_secs:
              type: number
              format: double
            max_iterations:
              type: integer
          required:
            - type
            - step_latency_secs
            - max_iterations
        - type: object
          properties:
            type:
              type: string
              enum:
                - nested_tools
              description: 'Discriminator value: nested_tools'
            step_latency_secs:
              type: number
              format: double
            node_id:
              type: string
            requests:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:ConversationHistoryTranscriptToolCallCommonModelOutput
            results:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:WorkflowToolNestedToolsStepModelOutputResultsItem
            is_successful:
              type: boolean
          required:
            - type
            - step_latency_secs
            - node_id
            - requests
            - results
            - is_successful
      discriminator:
        propertyName: type
      title: WorkflowToolResponseModelOutputStepsItem
    type_:WorkflowToolResponseModelOutput:
      type: object
      properties:
        steps:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:WorkflowToolResponseModelOutputStepsItem
      description: A common model for workflow tool responses.
      title: WorkflowToolResponseModelOutput
    type_:ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput:
      type: object
      properties:
        request_id:
          type: string
        tool_name:
          type: string
        result_value:
          type: string
        is_error:
          type: boolean
        is_blocked:
          type: boolean
          default: false
        tool_has_been_called:
          type: boolean
        tool_latency_secs:
          type: number
          format: double
          default: 0
        error_type:
          type: string
          default: ''
        raw_error_message:
          type: string
          default: ''
        dynamic_variable_updates:
          type: array
          items:
            $ref: '#/components/schemas/type_:DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - workflow
        result:
          $ref: '#/components/schemas/type_:WorkflowToolResponseModelOutput'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput
    type_:ConversationHistoryTranscriptResponseModelToolResultsItem:
      oneOf:
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptSystemToolResultCommonModelOutput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput
      title: ConversationHistoryTranscriptResponseModelToolResultsItem
    type_:LlmUsageOutput:
      type: object
      properties:
        model_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:LlmInputOutputTokensUsage'
      title: LlmUsageOutput
    type_:ConversationHistoryTranscriptFileInputResponseModel:
      type: object
      properties:
        file_id:
          type: string
        original_filename:
          type: string
        mime_type:
          type: string
        file_url:
          type: string
      required:
        - file_id
        - original_filename
        - mime_type
        - file_url
      title: ConversationHistoryTranscriptFileInputResponseModel
    type_:ContextualUpdateInfo:
      type: object
      properties:
        context_id:
          type: string
          description: Client-supplied identifier grouping related contextual updates.
        is_superseded:
          type: boolean
          default: false
          description: >-
            True when this contextual update has been replaced by a newer update
            with the same context_id.
      required:
        - context_id
      title: ContextualUpdateInfo
    type_:ConversationHistoryTranscriptResponseModel:
      type: object
      properties:
        role:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptResponseModelRole
        agent_metadata:
          $ref: '#/components/schemas/type_:AgentMetadata'
        message:
          type: string
        multivoice_message:
          $ref: '#/components/schemas/type_:ConversationHistoryMultivoiceMessageModel'
        tool_calls:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptToolCallCommonModelOutput
        tool_results:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptResponseModelToolResultsItem
        feedback:
          $ref: '#/components/schemas/type_:UserFeedback'
        llm_override:
          type: string
        time_in_call_secs:
          type: integer
        conversation_turn_metrics:
          $ref: '#/components/schemas/type_:ConversationTurnMetrics'
        rag_retrieval_info:
          $ref: '#/components/schemas/type_:RagRetrievalInfo'
        llm_usage:
          $ref: '#/components/schemas/type_:LlmUsageOutput'
        interrupted:
          type: boolean
          default: false
        ignored_as_backchannel:
          type: boolean
          default: false
        original_message:
          type: string
        reasoning:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConversationReasoningModel'
        source_medium:
          $ref: '#/components/schemas/type_:ChatSourceMedium'
        source_event_id:
          type: integer
        used_static_kb_document_ids:
          type: array
          items:
            type: string
        user_identifier:
          type: string
        id:
          type: string
        triggered_guardrails:
          type: array
          items:
            $ref: '#/components/schemas/type_:TriggeredGuardrailCommonModel'
        file_input:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptFileInputResponseModel
        contextual_update_info:
          $ref: '#/components/schemas/type_:ContextualUpdateInfo'
        reasoned:
          type: boolean
          default: false
      required:
        - role
        - time_in_call_secs
      title: ConversationHistoryTranscriptResponseModel
    type_:EvaluationSuccessResult:
      type: string
      enum:
        - success
        - failure
        - unknown
      title: EvaluationSuccessResult
    type_:ConversationHistoryEvaluationCriteriaResultCommonModel:
      type: object
      properties:
        criteria_id:
          type: string
        result:
          $ref: '#/components/schemas/type_:EvaluationSuccessResult'
        rationale:
          type: string
        scoring_mode:
          $ref: '#/components/schemas/type_:CriteriaScoringMode'
        score:
          type: integer
        max_score:
          type: integer
      required:
        - criteria_id
        - result
        - rationale
      title: ConversationHistoryEvaluationCriteriaResultCommonModel
    type_:DataCollectionResultCommonModel:
      type: object
      properties:
        data_collection_id:
          type: string
        value:
          description: Any type
        json_schema:
          $ref: '#/components/schemas/type_:LiteralJsonSchemaProperty'
        rationale:
          type: string
      required:
        - data_collection_id
        - rationale
      title: DataCollectionResultCommonModel
    type_:ScopedAnalysisResult:
      type: object
      properties:
        scope:
          $ref: '#/components/schemas/type_:AnalysisScope'
          description: >-
            The scope of the analysis. 'conversation' uses the full transcript;
            'agent' uses only the portion where the defining agent was active.
        source_agent_id:
          type: string
        source_branch_id:
          type: string
          description: >-
            Branch of the agent for this scoped block; disambiguates repeated
            agent_id.
        evaluation_criteria_results:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryEvaluationCriteriaResultCommonModel
        data_collection_results:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:DataCollectionResultCommonModel'
        successful:
          $ref: '#/components/schemas/type_:EvaluationSuccessResult'
        success_score:
          type: number
          format: double
      required:
        - scope
        - source_agent_id
        - successful
      title: ScopedAnalysisResult
    type_:ConversationHistoryAnalysisCommonModel:
      type: object
      properties:
        evaluation_criteria_results:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryEvaluationCriteriaResultCommonModel
        data_collection_results:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:DataCollectionResultCommonModel'
        evaluation_criteria_results_list:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryEvaluationCriteriaResultCommonModel
        data_collection_results_list:
          type: array
          items:
            $ref: '#/components/schemas/type_:DataCollectionResultCommonModel'
        call_successful:
          $ref: '#/components/schemas/type_:EvaluationSuccessResult'
        call_success_score:
          type: number
          format: double
        transcript_summary:
          type: string
        call_summary_title:
          type: string
        scoped:
          type: array
          items:
            $ref: '#/components/schemas/type_:ScopedAnalysisResult'
      required:
        - call_successful
        - transcript_summary
      title: ConversationHistoryAnalysisCommonModel
    type_:AgentSimulatedChatTestResponseModel:
      type: object
      properties:
        simulated_conversation:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptResponseModel
        analysis:
          $ref: '#/components/schemas/type_:ConversationHistoryAnalysisCommonModel'
      required:
        - simulated_conversation
        - analysis
      title: AgentSimulatedChatTestResponseModel
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

**Response**

```json
{
  "simulated_conversation": [
    {
      "role": "user",
      "time_in_call_secs": 1,
      "agent_metadata": {
        "agent_id": "agent_id"
      },
      "message": "message",
      "multivoice_message": {
        "parts": [
          {
            "text": "text",
            "voice_label": null,
            "time_in_call_secs": null
          }
        ]
      },
      "tool_calls": [
        {
          "request_id": "request_id",
          "tool_name": "tool_name",
          "params_as_json": "params_as_json",
          "tool_has_been_called": true
        }
      ],
      "tool_results": [
        {
          "is_error": true,
          "request_id": "request_id",
          "result_value": "result_value",
          "tool_has_been_called": true,
          "tool_name": "tool_name"
        }
      ],
      "feedback": {
        "score": "like",
        "time_in_call_secs": 1
      },
      "llm_override": "llm_override",
      "rag_retrieval_info": {
        "chunks": [
          {
            "document_id": "document_id",
            "chunk_id": "chunk_id",
            "vector_distance": 1.1
          }
        ],
        "embedding_model": "e5_mistral_7b_instruct",
        "retrieval_query": "retrieval_query",
        "rag_latency_secs": 1.1
      },
      "interrupted": true,
      "ignored_as_backchannel": true,
      "original_message": "original_message",
      "reasoning": [
        {}
      ],
      "source_medium": "audio",
      "source_event_id": 1,
      "used_static_kb_document_ids": [
        "used_static_kb_document_ids"
      ],
      "user_identifier": "user_identifier",
      "id": "id",
      "triggered_guardrails": [
        {
          "guardrail_type": "custom"
        }
      ],
      "file_input": {
        "file_id": "file_id",
        "original_filename": "original_filename",
        "mime_type": "mime_type",
        "file_url": "file_url"
      },
      "contextual_update_info": {
        "context_id": "context_id"
      },
      "reasoned": true
    }
  ],
  "analysis": {
    "call_successful": "success",
    "transcript_summary": "transcript_summary",
    "evaluation_criteria_results": {
      "key": {
        "criteria_id": "criteria_id",
        "result": "success",
        "rationale": "rationale"
      }
    },
    "data_collection_results": {
      "key": {
        "data_collection_id": "data_collection_id",
        "rationale": "rationale",
        "json_schema": {
          "type": "string",
          "description": "A user-provided message"
        }
      }
    },
    "evaluation_criteria_results_list": [
      {
        "criteria_id": "criteria_id",
        "result": "success",
        "rationale": "rationale"
      }
    ],
    "data_collection_results_list": [
      {
        "data_collection_id": "data_collection_id",
        "rationale": "rationale",
        "json_schema": {
          "type": "string",
          "description": "A user-provided message"
        }
      }
    ],
    "call_success_score": 1.1,
    "call_summary_title": "call_summary_title",
    "scoped": [
      {
        "scope": "conversation",
        "source_agent_id": "source_agent_id",
        "successful": "success"
      }
    ]
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.simulateConversation("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
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

client.conversational_ai.agents.simulate_conversation(
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation")

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

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation")
  .header("Content-Type", "application/json")
  .body("{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation', [
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/simulate-conversation")! as URL,
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
