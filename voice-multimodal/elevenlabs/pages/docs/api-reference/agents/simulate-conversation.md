---
title: "Simulate conversation"
source: https://elevenlabs.io/docs/api-reference/agents/simulate-conversation.md
path: docs/api-reference/agents/simulate-conversation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Simulate conversation

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/simulate-conversation
Content-Type: application/json

Deprecated. Use the `/v1/convai/agent-testing/create` and `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run simulations. Run a conversation between the agent and a simulated user.

Reference: https://elevenlabs.io/docs/api-reference/agents/simulate-conversation

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
        - subpackage_conversationalAi/agents
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
                $ref: '#/components/schemas/AgentSimulatedChatTestResponseModel'
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
              $ref: >-
                #/components/schemas/Body_Simulates_a_conversation_v1_convai_agents__agent_id__simulate_conversation_post
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
    Verbosity:
      type: string
      enum:
        - auto
        - concise
        - thorough
      title: Verbosity
    OutputFormat:
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
    InteractionBudget:
      type: string
      enum:
        - realtime
        - 5_minutes
        - 10_minutes
        - 1_hour
      title: InteractionBudget
    BehaviorOverride:
      type: object
      properties:
        verbosity:
          oneOf:
            - $ref: '#/components/schemas/Verbosity'
            - type: 'null'
          description: Verbosity override. Underlying default applies when unset.
        output_format:
          oneOf:
            - $ref: '#/components/schemas/OutputFormat'
            - type: 'null'
          description: Output format override. Underlying default applies when unset.
        interaction_budget:
          oneOf:
            - $ref: '#/components/schemas/InteractionBudget'
            - type: 'null'
          description: Interaction budget override. Underlying default applies when unset.
      title: BehaviorOverride
    LLM:
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
        - claude-sonnet-4-5
        - claude-opus-4-7
        - claude-sonnet-4-6
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
      default: gemini-2.5-flash
      title: LLM
    LLMReasoningEffort:
      type: string
      enum:
        - none
        - minimal
        - low
        - medium
        - high
        - xhigh
      title: LLMReasoningEffort
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
      description: Predefined tool call sound types.
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
            How many recent customer messages to include in the guardrail's
            history, plus the agent replies that follow them (and tool calls and
            results when history_include_tool_calls is enabled). Only customer
            messages count toward the limit. 0 (default) shows none; 1 shows the
            customer's latest message onward. When > 0, the guardrail prompt can
            refer to this history as <conversation_history>; the reply under
            evaluation appears as <agent_message> and may repeat at the end of
            the history.
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
    AgentTransfer:
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
      title: AgentTransfer
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
                $ref: '#/components/schemas/AgentTransfer'
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
    SystemToolConfig-Input:
      type: object
      properties:
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
          $ref: '#/components/schemas/ToolInterruptionMode'
          default: allow
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
          $ref: '#/components/schemas/PreToolSpeechMode'
          default: auto
          description: >-
            Controls whether the agent speaks before this tool is called. 'auto'
            (default) decides based on recent tool latency, 'force' always asks
            the agent to speak, 'off' fully opts out regardless of latency.
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
            Predefined tool call sound type to play during tool execution. If
            not specified, no tool call sound will be played.
        tool_call_sound_behavior:
          $ref: '#/components/schemas/ToolCallSoundBehavior'
          default: auto
          description: >-
            Determines when the tool call sound should play. 'auto' only plays
            when there's pre-tool speech, 'always' plays for every tool call.
        tool_error_handling_mode:
          $ref: '#/components/schemas/ToolErrorHandlingMode'
          default: auto
          description: >-
            Controls how tool errors are processed before being shared with the
            agent. 'auto' determines handling based on tool type (summarized for
            native integrations, hide for others), 'summarized' sends an
            LLM-generated summary, 'passthrough' sends the raw error, 'hide'
            does not share the error with the agent.
        params:
          $ref: >-
            #/components/schemas/ToolRequestModelToolConfigDiscriminatorMappingSystemParams
      required:
        - name
        - params
      description: >-
        A system tool is a tool that is used to call a system method in the
        server
      title: SystemToolConfig-Input
    BuiltInTools-Input:
      type: object
      properties:
        end_call:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
          description: The end call tool
        language_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
          description: The language detection tool
        transfer_to_agent:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
          description: The transfer to agent tool
        transfer_to_number:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
          description: The transfer to number tool
        skip_turn:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
          description: The skip turn tool
        play_keypad_touch_tone:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
          description: The play DTMF tool
        voicemail_detection:
          oneOf:
            - $ref: '#/components/schemas/SystemToolConfig-Input'
            - type: 'null'
          description: The voicemail detection tool
      title: BuiltInTools-Input
    KnowledgeBaseDocumentType:
      type: string
      enum:
        - file
        - url
        - text
        - folder
      title: KnowledgeBaseDocumentType
    DocumentUsageModeEnum:
      type: string
      enum:
        - prompt
        - auto
      default: auto
      title: DocumentUsageModeEnum
    KnowledgeBaseLocator:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/KnowledgeBaseDocumentType'
          description: The type of the knowledge base
        name:
          type: string
          description: The name of the knowledge base
        id:
          type: string
          description: The ID of the knowledge base
        usage_mode:
          $ref: '#/components/schemas/DocumentUsageModeEnum'
          default: auto
          description: The usage mode of the knowledge base
      required:
        - type
        - name
        - id
      title: KnowledgeBaseLocator
    ConvAISecretLocator:
      type: object
      properties:
        secret_id:
          type: string
      required:
        - secret_id
      description: Used to reference a secret from the agent's secret store.
      title: ConvAISecretLocator
    ConvAIEnvVarLocator:
      type: object
      properties:
        env_var_label:
          type: string
      required:
        - env_var_label
      description: Used to reference an environment variable by label.
      title: ConvAIEnvVarLocator
    CustomLlmApiKey:
      oneOf:
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIEnvVarLocator'
      description: >-
        The API key for authentication. Either a workspace secret reference
        {'secret_id': '...'} or an environment variable reference
        {'env_var_label': '...'}.
      title: CustomLlmApiKey
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
    CustomLlmAuthConnection:
      oneOf:
        - $ref: '#/components/schemas/AuthConnectionLocator'
        - $ref: '#/components/schemas/EnvironmentAuthConnectionLocator'
      description: >-
        Optional workspace auth connection for authentication. Only auth
        connections that produce an Authorization Bearer token are supported;
        Basic auth, mTLS, custom header, and URL secret auth connections are not
        supported.
      title: CustomLlmAuthConnection
    ConvAIDynamicVariable:
      type: object
      properties:
        variable_name:
          type: string
      required:
        - variable_name
      description: Used to reference a dynamic variable.
      title: ConvAIDynamicVariable
    CustomLlmRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
        - $ref: '#/components/schemas/ConvAIEnvVarLocator'
      title: CustomLlmRequestHeaders
    CustomLLMAPIType:
      type: string
      enum:
        - chat_completions
        - responses
      default: chat_completions
      title: CustomLLMAPIType
    CustomLLM:
      type: object
      properties:
        url:
          type: string
          description: The URL of the Chat Completions compatible endpoint
        model_id:
          type:
            - string
            - 'null'
          description: The model ID to be used if URL serves multiple models
        api_key:
          oneOf:
            - $ref: '#/components/schemas/CustomLlmApiKey'
            - type: 'null'
          description: >-
            The API key for authentication. Either a workspace secret reference
            {'secret_id': '...'} or an environment variable reference
            {'env_var_label': '...'}.
        auth_connection:
          oneOf:
            - $ref: '#/components/schemas/CustomLlmAuthConnection'
            - type: 'null'
          description: >-
            Optional workspace auth connection for authentication. Only auth
            connections that produce an Authorization Bearer token are
            supported; Basic auth, mTLS, custom header, and URL secret auth
            connections are not supported.
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/CustomLlmRequestHeaders'
          description: Headers that should be included in the request
        api_version:
          type:
            - string
            - 'null'
          description: The API version to use for the request
        api_type:
          $ref: '#/components/schemas/CustomLLMAPIType'
          default: chat_completions
          description: The API type to use (chat_completions or responses)
      required:
        - url
      title: CustomLLM
    EmbeddingModelEnum:
      type: string
      enum:
        - e5_mistral_7b_instruct
        - multilingual_e5_large_instruct
      default: e5_mistral_7b_instruct
      title: EmbeddingModelEnum
    RagConfig:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
        embedding_model:
          $ref: '#/components/schemas/EmbeddingModelEnum'
          default: e5_mistral_7b_instruct
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
          type:
            - integer
            - 'null'
          description: >-
            Number of candidates evaluated in ANN vector search. Higher number
            means better results, but higher latency. Minimum recommended value
            is 100. If disabled, the default value is used.
        query_rewrite_prompt_override:
          type:
            - string
            - 'null'
          description: >-
            Custom prompt for rewriting user queries before RAG retrieval. The
            conversation history will be automatically appended at the end. If
            not set, the default prompt will be used.
      title: RagConfig
    PromptAgentApiModelInputBackupLlmConfig:
      oneOf:
        - type: object
          properties:
            preference:
              type: string
              enum:
                - default
              description: 'Discriminator value: default'
          required:
            - preference
          description: BackupLLMDefault variant
        - type: object
          properties:
            preference:
              type: string
              enum:
                - disabled
              description: 'Discriminator value: disabled'
          required:
            - preference
          description: BackupLLMDisabled variant
        - type: object
          properties:
            preference:
              type: string
              enum:
                - override
              description: 'Discriminator value: override'
            order:
              type: array
              items:
                $ref: '#/components/schemas/LLM'
          required:
            - preference
            - order
          description: BackupLLMOverride variant
      discriminator:
        propertyName: preference
      description: >-
        Configuration for backup LLM cascading. Can be disabled, use system
        defaults, or specify custom order.
      title: PromptAgentApiModelInputBackupLlmConfig
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
    McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValueOneOf4Items:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
      title: >-
        McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValueOneOf4Items
    McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValue4:
      type: array
      items:
        $ref: >-
          #/components/schemas/McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValueOneOf4Items
      title: >-
        McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValue4
    McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
        - $ref: >-
            #/components/schemas/McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValue4
      description: The constant value to use
      title: >-
        McpToolConfigOverrideUpdateRequestModelInputOverridesDiscriminatorMappingConstantConstantValue
    ApiIntegrationWebhookOverridesSchemaOverrides:
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
      title: ApiIntegrationWebhookOverridesSchemaOverrides
    ApiIntegrationWebhookOverridesRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
      title: ApiIntegrationWebhookOverridesRequestHeaders
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
    ApiIntegrationWebhookOverrides:
      type: object
      properties:
        schema_overrides:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/ApiIntegrationWebhookOverridesSchemaOverrides'
        request_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/ApiIntegrationWebhookOverridesRequestHeaders'
        response_filter_mode:
          oneOf:
            - $ref: '#/components/schemas/ResponseFilterMode'
            - type: 'null'
        response_filters:
          type:
            - array
            - 'null'
          items:
            type: string
      description: |-
        A whitelist of fields that can be overridden by users when
        configuring an API Integration Webhook Tool.
      title: ApiIntegrationWebhookOverrides
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
    PromptAgentApiModelInputToolsItems:
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
            tool_version:
              type: string
              default: 1.0.0
              description: The version of the API integration tool
            api_integration_id:
              type: string
            api_integration_connection_id:
              type: string
            api_schema_overrides:
              oneOf:
                - $ref: '#/components/schemas/ApiIntegrationWebhookOverrides'
                - type: 'null'
              description: User overrides applied on top of the base api_schema
          required:
            - type
            - name
            - description
            - api_integration_id
            - api_integration_connection_id
          description: ApiIntegrationWebhookToolConfig variant
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
                - smb
              description: 'Discriminator value: smb'
          required:
            - type
          description: smb variant
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
      description: The type of tool
      title: PromptAgentApiModelInputToolsItems
    PromptAgentAPIModel-Input:
      type: object
      properties:
        prompt:
          type: string
          default: ''
          description: The prompt for the agent
        llm:
          $ref: '#/components/schemas/LLM'
          default: gemini-2.5-flash
          description: >-
            The LLM to query with the prompt and the chat history. If using data
            residency, the LLM must be supported in the data residency
            environment
        reasoning_effort:
          oneOf:
            - $ref: '#/components/schemas/LLMReasoningEffort'
            - type: 'null'
          description: Reasoning effort of the model. Only available for some models.
        thinking_budget:
          type:
            - integer
            - 'null'
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
          type:
            - number
            - 'null'
          format: double
          default: 0
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
          $ref: '#/components/schemas/BuiltInTools-Input'
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
            $ref: '#/components/schemas/KnowledgeBaseLocator'
          description: A list of knowledge bases to be used by the agent
        custom_llm:
          oneOf:
            - $ref: '#/components/schemas/CustomLLM'
            - type: 'null'
          description: Definition for a custom LLM if LLM field is set to 'CUSTOM_LLM'
        ignore_default_personality:
          type:
            - boolean
            - 'null'
          default: false
          description: >-
            Whether to remove the default personality lines from the system
            prompt
        rag:
          $ref: '#/components/schemas/RagConfig'
          description: Configuration for RAG
        timezone:
          type:
            - string
            - 'null'
          description: >-
            Timezone for displaying current time in system prompt. If set, the
            current time will be included in the system prompt using this
            timezone. Must be a valid timezone name (e.g., 'America/New_York',
            'Europe/London', 'UTC'). Recommended for accurate time-aware
            responses; without this, the agent has no knowledge of the current
            date/time unless you provide it via dynamic variables or tools,
            which can lead to incorrect or hallucinated time references.
        backup_llm_config:
          $ref: '#/components/schemas/PromptAgentApiModelInputBackupLlmConfig'
          description: >-
            Configuration for backup LLM cascading. Can be disabled, use system
            defaults, or specify custom order.
        cascade_timeout_seconds:
          type: number
          format: double
          default: 8
          description: >-
            Time in seconds before cascading to backup LLM. Must be between 2
            and 15 seconds.
        tools:
          type: array
          items:
            $ref: '#/components/schemas/PromptAgentApiModelInputToolsItems'
          description: >-
            A list of tools that the agent can use over the course of the
            conversation, use tool_ids instead
      title: PromptAgentAPIModel-Input
    AgentConfigAPIModel-Input:
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
          description: Configuration for dynamic variables
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
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/BehaviorOverride'
          description: >-
            Per-channel response behavior overrides for text conversations.
            Built-in channel defaults apply when unset.
        prompt:
          $ref: '#/components/schemas/PromptAgentAPIModel-Input'
          description: The prompt for the agent
      title: AgentConfigAPIModel-Input
    ToolMockConfig:
      type: object
      properties:
        default_return_value:
          type: string
          default: Tool Called.
        default_is_error:
          type: boolean
          default: false
      title: ToolMockConfig
    ConversationHistoryTranscriptCommonModelInputRole:
      type: string
      enum:
        - user
        - agent
      title: ConversationHistoryTranscriptCommonModelInputRole
    AgentMetadata:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
        workflow_node_id:
          type:
            - string
            - 'null'
        version_id:
          type:
            - string
            - 'null'
      required:
        - agent_id
      title: AgentMetadata
    ConversationHistoryMultivoiceMessagePartModel:
      type: object
      properties:
        text:
          type: string
        voice_label:
          type:
            - string
            - 'null'
        time_in_call_secs:
          type:
            - integer
            - 'null'
      required:
        - text
        - voice_label
        - time_in_call_secs
      description: Represents a single voice part of a multi-voice message.
      title: ConversationHistoryMultivoiceMessagePartModel
    ConversationHistoryMultivoiceMessageModel:
      type: object
      properties:
        parts:
          type: array
          items:
            $ref: '#/components/schemas/ConversationHistoryMultivoiceMessagePartModel'
      required:
        - parts
      description: Represents a message from a multi-voice agent.
      title: ConversationHistoryMultivoiceMessageModel
    ToolType:
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
    ConversationHistoryTranscriptToolCallWebhookDetails:
      type: object
      properties:
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
          type:
            - string
            - 'null'
      required:
        - method
        - url
      title: ConversationHistoryTranscriptToolCallWebhookDetails
    ConversationHistoryTranscriptToolCallCommonModelInputToolDetails:
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
                #/components/schemas/ConversationHistoryTranscriptToolCallWebhookDetails
          required:
            - type
            - webhook_details
          description: >-
            ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetails
            variant
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
          description: ConversationHistoryTranscriptToolCallClientDetails variant
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
          description: ConversationHistoryTranscriptToolCallMCPDetails variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
              description: 'Discriminator value: webhook'
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
              type:
                - string
                - 'null'
          required:
            - type
            - method
            - url
          description: ConversationHistoryTranscriptToolCallWebhookDetails variant
      discriminator:
        propertyName: type
      title: ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
    ConversationHistoryTranscriptToolCallCommonModel-Input:
      type: object
      properties:
        type:
          oneOf:
            - $ref: '#/components/schemas/ToolType'
            - type: 'null'
        request_id:
          type: string
        tool_name:
          type: string
        params_as_json:
          type: string
        tool_has_been_called:
          type: boolean
        tool_details:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptToolCallCommonModelInputToolDetails
            - type: 'null'
      required:
        - request_id
        - tool_name
        - params_as_json
        - tool_has_been_called
      title: ConversationHistoryTranscriptToolCallCommonModel-Input
    DynamicVariableUpdateCommonModel:
      type: object
      properties:
        variable_name:
          type: string
        old_value:
          type:
            - string
            - 'null'
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
        - old_value
        - new_value
        - updated_at
        - tool_name
        - tool_request_id
      description: Tracks a dynamic variable update that occurred during tool execution.
      title: DynamicVariableUpdateCommonModel
    ConversationHistoryTranscriptOtherToolsResultCommonModelType:
      type: string
      enum:
        - client
        - webhook
        - mcp
        - code
      title: ConversationHistoryTranscriptOtherToolsResultCommonModelType
    ConversationHistoryTranscriptOtherToolsResultCommonModel:
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
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
        type:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptOtherToolsResultCommonModelType
            - type: 'null'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
      title: ConversationHistoryTranscriptOtherToolsResultCommonModel
    KnowledgeBaseRagToolStatus:
      type: string
      enum:
        - success
        - no_documents
        - no_results
      default: success
      title: KnowledgeBaseRagToolStatus
    TransferToAgentToolResultSuccessModelBranchInfo:
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
          description: TransferBranchInfoDefaultingToMain variant
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
          description: TransferBranchInfoTrafficSplit variant
      discriminator:
        propertyName: branch_reason
      title: TransferToAgentToolResultSuccessModelBranchInfo
    ConversationHistoryTranscriptSystemToolResultCommonModelInputResult:
      oneOf:
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - end_call_success
              default: end_call_success
            status:
              type: string
              enum:
                - success
              default: success
            reason:
              type:
                - string
                - 'null'
            message:
              type:
                - string
                - 'null'
          required:
            - result_type
          description: EndCallToolResultModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - knowledge_base_rag_success
              default: knowledge_base_rag_success
            status:
              $ref: '#/components/schemas/KnowledgeBaseRagToolStatus'
              default: success
            chunk_count:
              type: integer
              default: 0
              description: Number of relevant chunks retrieved
            message:
              type: string
              default: Referenced knowledge base.
              description: Human-readable status for the LLM about the search results
          required:
            - result_type
          description: KnowledgeBaseRagToolResultModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - language_detection_success
              default: language_detection_success
            status:
              type: string
              enum:
                - success
              default: success
            reason:
              type:
                - string
                - 'null'
            language:
              type:
                - string
                - 'null'
          required:
            - result_type
          description: LanguageDetectionToolResultModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - play_dtmf_error
              default: play_dtmf_error
            status:
              type: string
              enum:
                - error
              default: error
            error:
              type: string
            details:
              type:
                - string
                - 'null'
          required:
            - result_type
            - error
          description: PlayDTMFResultErrorModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - play_dtmf_success
              default: play_dtmf_success
            status:
              type: string
              enum:
                - success
              default: success
            dtmf_tones:
              type: string
            reason:
              type:
                - string
                - 'null'
          required:
            - result_type
            - dtmf_tones
          description: PlayDTMFResultSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - skip_turn_success
              default: skip_turn_success
            status:
              type: string
              enum:
                - success
              default: success
            reason:
              type:
                - string
                - 'null'
          required:
            - result_type
          description: SkipTurnToolResponseModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - testing_tool_result
              default: testing_tool_result
            status:
              type: string
              enum:
                - success
              default: success
            reason:
              type: string
              default: Skipping tool call in test mode
          required:
            - result_type
          description: TestToolResultModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_agent_error
              default: transfer_to_agent_error
            status:
              type: string
              enum:
                - error
              default: error
            from_agent:
              type: string
            error:
              type: string
          required:
            - result_type
            - from_agent
            - error
          description: TransferToAgentToolResultErrorModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_agent_success
              default: transfer_to_agent_success
            status:
              type: string
              enum:
                - success
              default: success
            from_agent:
              type: string
            to_agent:
              type: string
            to_node:
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
            branch_info:
              oneOf:
                - $ref: >-
                    #/components/schemas/TransferToAgentToolResultSuccessModelBranchInfo
                - type: 'null'
            preserve_client_tts_overrides:
              type: boolean
              default: false
          required:
            - result_type
            - from_agent
            - to_agent
            - condition
          description: TransferToAgentToolResultSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_error
              default: transfer_to_number_error
            status:
              type: string
              enum:
                - error
              default: error
            error:
              type: string
            details:
              type:
                - string
                - 'null'
          required:
            - result_type
            - error
          description: TransferToNumberResultErrorModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_exotel_success
              default: transfer_to_number_exotel_success
            status:
              type: string
              enum:
                - success
              default: success
            transfer_number:
              type: string
            reason:
              type:
                - string
                - 'null'
            agent_message:
              type:
                - string
                - 'null'
            note:
              type:
                - string
                - 'null'
          required:
            - result_type
            - transfer_number
          description: TransferToNumberResultExotelSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_sip_success
              default: transfer_to_number_sip_success
            status:
              type: string
              enum:
                - success
              default: success
            transfer_number:
              type: string
            reason:
              type:
                - string
                - 'null'
            note:
              type:
                - string
                - 'null'
          required:
            - result_type
            - transfer_number
          description: TransferToNumberResultSipSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_twilio_success
              default: transfer_to_number_twilio_success
            status:
              type: string
              enum:
                - success
              default: success
            transfer_number:
              type: string
            reason:
              type:
                - string
                - 'null'
            client_message:
              type:
                - string
                - 'null'
            agent_message:
              type: string
            conference_name:
              type: string
            post_dial_digits:
              type:
                - string
                - 'null'
            note:
              type:
                - string
                - 'null'
          required:
            - result_type
            - transfer_number
            - agent_message
            - conference_name
          description: TransferToNumberResultTwilioSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - voicemail_detection_success
              default: voicemail_detection_success
            status:
              type: string
              enum:
                - success
              default: success
            voicemail_message:
              type:
                - string
                - 'null'
            reason:
              type:
                - string
                - 'null'
          required:
            - result_type
          description: VoiceMailDetectionResultSuccessModel variant
      discriminator:
        propertyName: result_type
      title: ConversationHistoryTranscriptSystemToolResultCommonModelInputResult
    ConversationHistoryTranscriptSystemToolResultCommonModel-Input:
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
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - system
        result:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModelInputResult
            - type: 'null'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: ConversationHistoryTranscriptSystemToolResultCommonModel-Input
    ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Input:
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
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
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
        ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Input
    WorkflowToolResponseModelInputStepsItemsDiscriminatorMappingNestedToolsResultsItems:
      oneOf:
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModel-Input
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Input
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Input
      title: >-
        WorkflowToolResponseModelInputStepsItemsDiscriminatorMappingNestedToolsResultsItems
    WorkflowToolResponseModelInputStepsItems:
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
          description: WorkflowToolEdgeStepModel variant
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
          description: WorkflowToolMaxIterationsExceededStepModel variant
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
                  #/components/schemas/ConversationHistoryTranscriptToolCallCommonModel-Input
            results:
              type: array
              items:
                $ref: >-
                  #/components/schemas/WorkflowToolResponseModelInputStepsItemsDiscriminatorMappingNestedToolsResultsItems
            is_successful:
              type: boolean
          required:
            - type
            - step_latency_secs
            - node_id
            - requests
            - results
            - is_successful
          description: WorkflowToolNestedToolsStepModel variant
      discriminator:
        propertyName: type
      title: WorkflowToolResponseModelInputStepsItems
    WorkflowToolResponseModel-Input:
      type: object
      properties:
        steps:
          type: array
          items:
            $ref: '#/components/schemas/WorkflowToolResponseModelInputStepsItems'
      description: A common model for workflow tool responses.
      title: WorkflowToolResponseModel-Input
    ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Input:
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
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - workflow
        result:
          oneOf:
            - $ref: '#/components/schemas/WorkflowToolResponseModel-Input'
            - type: 'null'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Input
    ConversationHistoryTranscriptCommonModelInputToolResultsItems:
      oneOf:
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModel-Input
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Input
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Input
      title: ConversationHistoryTranscriptCommonModelInputToolResultsItems
    UserFeedbackScore:
      type: string
      enum:
        - like
        - dislike
      title: UserFeedbackScore
    UserFeedback:
      type: object
      properties:
        score:
          $ref: '#/components/schemas/UserFeedbackScore'
        time_in_call_secs:
          type: integer
      required:
        - score
        - time_in_call_secs
      title: UserFeedback
    MetricRecord:
      type: object
      properties:
        elapsed_time:
          type: number
          format: double
      required:
        - elapsed_time
      title: MetricRecord
    ConversationTurnMetrics:
      type: object
      properties:
        metrics:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/MetricRecord'
        convai_asr_provider:
          type:
            - string
            - 'null'
        convai_tts_model:
          type:
            - string
            - 'null'
        convai_tts_cascade:
          type:
            - string
            - 'null'
      title: ConversationTurnMetrics
    RagChunkMetadata:
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
    RagRetrievalInfo:
      type: object
      properties:
        chunks:
          type: array
          items:
            $ref: '#/components/schemas/RagChunkMetadata'
        embedding_model:
          $ref: '#/components/schemas/EmbeddingModelEnum'
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
    LLMTokensCategoryUsage:
      type: object
      properties:
        tokens:
          type: integer
          default: 0
        price:
          type: number
          format: double
          default: 0
      title: LLMTokensCategoryUsage
    LLMInputOutputTokensUsage:
      type: object
      properties:
        input:
          $ref: '#/components/schemas/LLMTokensCategoryUsage'
        input_cache_read:
          $ref: '#/components/schemas/LLMTokensCategoryUsage'
        input_cache_write:
          $ref: '#/components/schemas/LLMTokensCategoryUsage'
        output_total:
          $ref: '#/components/schemas/LLMTokensCategoryUsage'
      title: LLMInputOutputTokensUsage
    LLMUsage-Input:
      type: object
      properties:
        model_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LLMInputOutputTokensUsage'
      title: LLMUsage-Input
    ConversationReasoningModel:
      type: object
      properties:
        summary:
          type:
            - string
            - 'null'
        provider_redact:
          type: boolean
          default: false
      title: ConversationReasoningModel
    ChatSourceMedium:
      type: string
      enum:
        - audio
        - text
        - image
        - file
      title: ChatSourceMedium
    ConversationHistoryTranscriptCommonModel-Input:
      type: object
      properties:
        role:
          $ref: >-
            #/components/schemas/ConversationHistoryTranscriptCommonModelInputRole
        agent_metadata:
          oneOf:
            - $ref: '#/components/schemas/AgentMetadata'
            - type: 'null'
        message:
          type:
            - string
            - 'null'
        multivoice_message:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryMultivoiceMessageModel'
            - type: 'null'
        tool_calls:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptToolCallCommonModel-Input
        tool_results:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptCommonModelInputToolResultsItems
        feedback:
          oneOf:
            - $ref: '#/components/schemas/UserFeedback'
            - type: 'null'
        llm_override:
          type:
            - string
            - 'null'
        time_in_call_secs:
          type: integer
        conversation_turn_metrics:
          oneOf:
            - $ref: '#/components/schemas/ConversationTurnMetrics'
            - type: 'null'
        rag_retrieval_info:
          oneOf:
            - $ref: '#/components/schemas/RagRetrievalInfo'
            - type: 'null'
        llm_usage:
          oneOf:
            - $ref: '#/components/schemas/LLMUsage-Input'
            - type: 'null'
        interrupted:
          type: boolean
          default: false
        original_message:
          type:
            - string
            - 'null'
        reasoning:
          type: array
          items:
            $ref: '#/components/schemas/ConversationReasoningModel'
        source_medium:
          oneOf:
            - $ref: '#/components/schemas/ChatSourceMedium'
            - type: 'null'
        source_event_id:
          type:
            - integer
            - 'null'
        used_static_kb_document_ids:
          type: array
          items:
            type: string
        user_identifier:
          type:
            - string
            - 'null'
      required:
        - role
        - time_in_call_secs
      title: ConversationHistoryTranscriptCommonModel-Input
    ConversationSimulationSpecification:
      type: object
      properties:
        simulated_user_config:
          $ref: '#/components/schemas/AgentConfigAPIModel-Input'
        tool_mock_config:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ToolMockConfig'
        partial_conversation_history:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptCommonModel-Input
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
    AnalysisScope:
      type: string
      enum:
        - conversation
        - agent
      default: conversation
      title: AnalysisScope
    CriteriaScoringMode:
      type: string
      enum:
        - binary
        - numeric_uniform
      default: binary
      title: CriteriaScoringMode
    PromptEvaluationCriteria:
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
          default: prompt
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
          $ref: '#/components/schemas/AnalysisScope'
          default: conversation
          description: >-
            The scope of transcript context used when evaluating this criterion.
            'conversation' uses the full transcript; 'agent' uses only the
            portion where the defining agent was active.
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
          description: >-
            LLM model to use for this evaluation criteria. If not set, uses
            agent's analysis_llm default.
        scoring_mode:
          $ref: '#/components/schemas/CriteriaScoringMode'
          default: binary
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
          type:
            - string
            - 'null'
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
    Body_Simulates_a_conversation_v1_convai_agents__agent_id__simulate_conversation_post:
      type: object
      properties:
        simulation_specification:
          $ref: '#/components/schemas/ConversationSimulationSpecification'
          description: A specification detailing how the conversation should be simulated
        extra_evaluation_criteria:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/PromptEvaluationCriteria'
          description: A list of evaluation criteria to test
        new_turns_limit:
          type: integer
          default: 10000
          description: >-
            Maximum number of new turns to generate in the conversation
            simulation
      required:
        - simulation_specification
      title: >-
        Body_Simulates_a_conversation_v1_convai_agents__agent_id__simulate_conversation_post
    ConversationHistoryTranscriptResponseModelRole:
      type: string
      enum:
        - user
        - agent
      title: ConversationHistoryTranscriptResponseModelRole
    ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails:
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
                #/components/schemas/ConversationHistoryTranscriptToolCallWebhookDetails
          required:
            - type
            - integration_id
            - credential_id
            - integration_connection_id
            - webhook_details
          description: >-
            ConversationHistoryTranscriptToolCallApiIntegrationWebhookDetails
            variant
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
          description: ConversationHistoryTranscriptToolCallClientDetails variant
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
          description: ConversationHistoryTranscriptToolCallMCPDetails variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - webhook
              description: 'Discriminator value: webhook'
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
              type:
                - string
                - 'null'
          required:
            - type
            - method
            - url
          description: ConversationHistoryTranscriptToolCallWebhookDetails variant
      discriminator:
        propertyName: type
      title: ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails
    ConversationHistoryTranscriptToolCallCommonModel-Output:
      type: object
      properties:
        type:
          oneOf:
            - $ref: '#/components/schemas/ToolType'
            - type: 'null'
        request_id:
          type: string
        tool_name:
          type: string
        params_as_json:
          type: string
        tool_has_been_called:
          type: boolean
        tool_details:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptToolCallCommonModelOutputToolDetails
            - type: 'null'
      required:
        - request_id
        - tool_name
        - params_as_json
        - tool_has_been_called
      title: ConversationHistoryTranscriptToolCallCommonModel-Output
    ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult:
      oneOf:
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - end_call_success
              default: end_call_success
            status:
              type: string
              enum:
                - success
              default: success
            reason:
              type:
                - string
                - 'null'
            message:
              type:
                - string
                - 'null'
          required:
            - result_type
          description: EndCallToolResultModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - knowledge_base_rag_success
              default: knowledge_base_rag_success
            status:
              $ref: '#/components/schemas/KnowledgeBaseRagToolStatus'
              default: success
            chunk_count:
              type: integer
              default: 0
              description: Number of relevant chunks retrieved
            message:
              type: string
              default: Referenced knowledge base.
              description: Human-readable status for the LLM about the search results
          required:
            - result_type
          description: KnowledgeBaseRagToolResultModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - language_detection_success
              default: language_detection_success
            status:
              type: string
              enum:
                - success
              default: success
            reason:
              type:
                - string
                - 'null'
            language:
              type:
                - string
                - 'null'
          required:
            - result_type
          description: LanguageDetectionToolResultModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - play_dtmf_error
              default: play_dtmf_error
            status:
              type: string
              enum:
                - error
              default: error
            error:
              type: string
            details:
              type:
                - string
                - 'null'
          required:
            - result_type
            - error
          description: PlayDTMFResultErrorModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - play_dtmf_success
              default: play_dtmf_success
            status:
              type: string
              enum:
                - success
              default: success
            dtmf_tones:
              type: string
            reason:
              type:
                - string
                - 'null'
          required:
            - result_type
            - dtmf_tones
          description: PlayDTMFResultSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - skip_turn_success
              default: skip_turn_success
            status:
              type: string
              enum:
                - success
              default: success
            reason:
              type:
                - string
                - 'null'
          required:
            - result_type
          description: SkipTurnToolResponseModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - testing_tool_result
              default: testing_tool_result
            status:
              type: string
              enum:
                - success
              default: success
            reason:
              type: string
              default: Skipping tool call in test mode
          required:
            - result_type
          description: TestToolResultModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_agent_error
              default: transfer_to_agent_error
            status:
              type: string
              enum:
                - error
              default: error
            from_agent:
              type: string
            error:
              type: string
          required:
            - result_type
            - from_agent
            - error
          description: TransferToAgentToolResultErrorModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_agent_success
              default: transfer_to_agent_success
            status:
              type: string
              enum:
                - success
              default: success
            from_agent:
              type: string
            to_agent:
              type: string
            to_node:
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
            branch_info:
              oneOf:
                - $ref: >-
                    #/components/schemas/TransferToAgentToolResultSuccessModelBranchInfo
                - type: 'null'
            preserve_client_tts_overrides:
              type: boolean
              default: false
          required:
            - result_type
            - from_agent
            - to_agent
            - condition
          description: TransferToAgentToolResultSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_error
              default: transfer_to_number_error
            status:
              type: string
              enum:
                - error
              default: error
            error:
              type: string
            details:
              type:
                - string
                - 'null'
          required:
            - result_type
            - error
          description: TransferToNumberResultErrorModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_exotel_success
              default: transfer_to_number_exotel_success
            status:
              type: string
              enum:
                - success
              default: success
            transfer_number:
              type: string
            reason:
              type:
                - string
                - 'null'
            agent_message:
              type:
                - string
                - 'null'
            note:
              type:
                - string
                - 'null'
          required:
            - result_type
            - transfer_number
          description: TransferToNumberResultExotelSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_sip_success
              default: transfer_to_number_sip_success
            status:
              type: string
              enum:
                - success
              default: success
            transfer_number:
              type: string
            reason:
              type:
                - string
                - 'null'
            note:
              type:
                - string
                - 'null'
          required:
            - result_type
            - transfer_number
          description: TransferToNumberResultSipSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - transfer_to_number_twilio_success
              default: transfer_to_number_twilio_success
            status:
              type: string
              enum:
                - success
              default: success
            transfer_number:
              type: string
            reason:
              type:
                - string
                - 'null'
            client_message:
              type:
                - string
                - 'null'
            agent_message:
              type: string
            conference_name:
              type: string
            post_dial_digits:
              type:
                - string
                - 'null'
            note:
              type:
                - string
                - 'null'
          required:
            - result_type
            - transfer_number
            - agent_message
            - conference_name
          description: TransferToNumberResultTwilioSuccessModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - voicemail_detection_success
              default: voicemail_detection_success
            status:
              type: string
              enum:
                - success
              default: success
            voicemail_message:
              type:
                - string
                - 'null'
            reason:
              type:
                - string
                - 'null'
          required:
            - result_type
          description: VoiceMailDetectionResultSuccessModel variant
      discriminator:
        propertyName: result_type
      title: ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
    ConversationHistoryTranscriptSystemToolResultCommonModel-Output:
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
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - system
        result:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
            - type: 'null'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: ConversationHistoryTranscriptSystemToolResultCommonModel-Output
    ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Output:
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
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
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
        ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Output
    WorkflowToolResponseModelOutputStepsItemsDiscriminatorMappingNestedToolsResultsItems:
      oneOf:
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModel-Output
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Output
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Output
      title: >-
        WorkflowToolResponseModelOutputStepsItemsDiscriminatorMappingNestedToolsResultsItems
    WorkflowToolResponseModelOutputStepsItems:
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
          description: WorkflowToolEdgeStepModel variant
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
          description: WorkflowToolMaxIterationsExceededStepModel variant
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
                  #/components/schemas/ConversationHistoryTranscriptToolCallCommonModel-Output
            results:
              type: array
              items:
                $ref: >-
                  #/components/schemas/WorkflowToolResponseModelOutputStepsItemsDiscriminatorMappingNestedToolsResultsItems
            is_successful:
              type: boolean
          required:
            - type
            - step_latency_secs
            - node_id
            - requests
            - results
            - is_successful
          description: WorkflowToolNestedToolsStepModel variant
      discriminator:
        propertyName: type
      title: WorkflowToolResponseModelOutputStepsItems
    WorkflowToolResponseModel-Output:
      type: object
      properties:
        steps:
          type: array
          items:
            $ref: '#/components/schemas/WorkflowToolResponseModelOutputStepsItems'
      description: A common model for workflow tool responses.
      title: WorkflowToolResponseModel-Output
    ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Output:
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
            $ref: '#/components/schemas/DynamicVariableUpdateCommonModel'
        type:
          type: string
          enum:
            - workflow
        result:
          oneOf:
            - $ref: '#/components/schemas/WorkflowToolResponseModel-Output'
            - type: 'null'
      required:
        - request_id
        - tool_name
        - result_value
        - is_error
        - tool_has_been_called
        - type
      title: ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Output
    ConversationHistoryTranscriptResponseModelToolResultsItems:
      oneOf:
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptSystemToolResultCommonModel-Output
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModel-Output
        - $ref: >-
            #/components/schemas/ConversationHistoryTranscriptWorkflowToolsResultCommonModel-Output
      title: ConversationHistoryTranscriptResponseModelToolResultsItems
    LLMUsage-Output:
      type: object
      properties:
        model_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LLMInputOutputTokensUsage'
      title: LLMUsage-Output
    ConversationHistoryTranscriptFileInputResponseModel:
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
    ContextualUpdateInfo:
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
    ConversationHistoryTranscriptResponseModel:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/ConversationHistoryTranscriptResponseModelRole'
        agent_metadata:
          oneOf:
            - $ref: '#/components/schemas/AgentMetadata'
            - type: 'null'
        message:
          type:
            - string
            - 'null'
        multivoice_message:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryMultivoiceMessageModel'
            - type: 'null'
        tool_calls:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptToolCallCommonModel-Output
        tool_results:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptResponseModelToolResultsItems
        feedback:
          oneOf:
            - $ref: '#/components/schemas/UserFeedback'
            - type: 'null'
        llm_override:
          type:
            - string
            - 'null'
        time_in_call_secs:
          type: integer
        conversation_turn_metrics:
          oneOf:
            - $ref: '#/components/schemas/ConversationTurnMetrics'
            - type: 'null'
        rag_retrieval_info:
          oneOf:
            - $ref: '#/components/schemas/RagRetrievalInfo'
            - type: 'null'
        llm_usage:
          oneOf:
            - $ref: '#/components/schemas/LLMUsage-Output'
            - type: 'null'
        interrupted:
          type: boolean
          default: false
        original_message:
          type:
            - string
            - 'null'
        reasoning:
          type: array
          items:
            $ref: '#/components/schemas/ConversationReasoningModel'
        source_medium:
          oneOf:
            - $ref: '#/components/schemas/ChatSourceMedium'
            - type: 'null'
        source_event_id:
          type:
            - integer
            - 'null'
        used_static_kb_document_ids:
          type: array
          items:
            type: string
        user_identifier:
          type:
            - string
            - 'null'
        file_input:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryTranscriptFileInputResponseModel
            - type: 'null'
        contextual_update_info:
          oneOf:
            - $ref: '#/components/schemas/ContextualUpdateInfo'
            - type: 'null'
        reasoned:
          type: boolean
          default: false
      required:
        - role
        - time_in_call_secs
      title: ConversationHistoryTranscriptResponseModel
    EvaluationSuccessResult:
      type: string
      enum:
        - success
        - failure
        - unknown
      title: EvaluationSuccessResult
    ConversationHistoryEvaluationCriteriaResultCommonModel:
      type: object
      properties:
        criteria_id:
          type: string
        result:
          $ref: '#/components/schemas/EvaluationSuccessResult'
        rationale:
          type: string
        scoring_mode:
          oneOf:
            - $ref: '#/components/schemas/CriteriaScoringMode'
            - type: 'null'
        score:
          type:
            - integer
            - 'null'
        max_score:
          type:
            - integer
            - 'null'
      required:
        - criteria_id
        - result
        - rationale
      title: ConversationHistoryEvaluationCriteriaResultCommonModel
    DataCollectionResultCommonModel:
      type: object
      properties:
        data_collection_id:
          type: string
        value:
          description: Any type
        json_schema:
          oneOf:
            - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
            - type: 'null'
        rationale:
          type: string
      required:
        - data_collection_id
        - rationale
      title: DataCollectionResultCommonModel
    ScopedAnalysisResult:
      type: object
      properties:
        scope:
          $ref: '#/components/schemas/AnalysisScope'
          description: >-
            The scope of the analysis. 'conversation' uses the full transcript;
            'agent' uses only the portion where the defining agent was active.
        source_agent_id:
          type: string
        source_branch_id:
          type:
            - string
            - 'null'
          description: >-
            Branch of the agent for this scoped block; disambiguates repeated
            agent_id.
        evaluation_criteria_results:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationHistoryEvaluationCriteriaResultCommonModel
        data_collection_results:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/DataCollectionResultCommonModel'
        successful:
          $ref: '#/components/schemas/EvaluationSuccessResult'
        success_score:
          type:
            - number
            - 'null'
          format: double
      required:
        - scope
        - source_agent_id
        - successful
      title: ScopedAnalysisResult
    ConversationHistoryAnalysisCommonModel:
      type: object
      properties:
        evaluation_criteria_results:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/ConversationHistoryEvaluationCriteriaResultCommonModel
        data_collection_results:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/DataCollectionResultCommonModel'
        evaluation_criteria_results_list:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryEvaluationCriteriaResultCommonModel
        data_collection_results_list:
          type: array
          items:
            $ref: '#/components/schemas/DataCollectionResultCommonModel'
        call_successful:
          $ref: '#/components/schemas/EvaluationSuccessResult'
        call_success_score:
          type:
            - number
            - 'null'
          format: double
        transcript_summary:
          type: string
        call_summary_title:
          type:
            - string
            - 'null'
        scoped:
          type: array
          items:
            $ref: '#/components/schemas/ScopedAnalysisResult'
      required:
        - call_successful
        - transcript_summary
      title: ConversationHistoryAnalysisCommonModel
    AgentSimulatedChatTestResponseModel:
      type: object
      properties:
        simulated_conversation:
          type: array
          items:
            $ref: '#/components/schemas/ConversationHistoryTranscriptResponseModel'
        analysis:
          $ref: '#/components/schemas/ConversationHistoryAnalysisCommonModel'
      required:
        - simulated_conversation
        - analysis
      title: AgentSimulatedChatTestResponseModel
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
        "agent_id": "string",
        "branch_id": "string",
        "workflow_node_id": "string",
        "version_id": "string"
      },
      "message": "string",
      "multivoice_message": {
        "parts": [
          {
            "text": "string",
            "voice_label": "string",
            "time_in_call_secs": 1
          }
        ]
      },
      "tool_calls": [
        {
          "request_id": "string",
          "tool_name": "string",
          "params_as_json": "string",
          "tool_has_been_called": true,
          "type": "system",
          "tool_details": {
            "type": "webhook",
            "method": "string",
            "url": "string",
            "body": "string",
            "headers": {},
            "path_params": {},
            "query_params": {}
          }
        }
      ],
      "tool_results": [
        {
          "dynamic_variable_updates": [
            {
              "new_value": "string",
              "old_value": "string",
              "tool_name": "string",
              "tool_request_id": "string",
              "updated_at": 1.1,
              "variable_name": "string"
            }
          ],
          "error_type": "",
          "is_blocked": false,
          "is_error": true,
          "raw_error_message": "",
          "request_id": "string",
          "result_value": "string",
          "tool_has_been_called": true,
          "tool_latency_secs": 0,
          "tool_name": "string",
          "type": "client"
        }
      ],
      "feedback": {
        "score": "like",
        "time_in_call_secs": 1
      },
      "llm_override": "string",
      "conversation_turn_metrics": {
        "metrics": {},
        "convai_asr_provider": "string",
        "convai_tts_model": "string",
        "convai_tts_cascade": "string"
      },
      "rag_retrieval_info": {
        "chunks": [
          {
            "document_id": "string",
            "chunk_id": "string",
            "vector_distance": 1.1
          }
        ],
        "embedding_model": "e5_mistral_7b_instruct",
        "retrieval_query": "string",
        "rag_latency_secs": 1.1,
        "used_chunk_ids": [
          "string"
        ]
      },
      "llm_usage": {
        "model_usage": {}
      },
      "interrupted": false,
      "original_message": "string",
      "reasoning": [
        {
          "summary": "string",
          "provider_redact": false
        }
      ],
      "source_medium": "audio",
      "source_event_id": 1,
      "used_static_kb_document_ids": [
        "string"
      ],
      "user_identifier": "string",
      "file_input": {
        "file_id": "string",
        "original_filename": "string",
        "mime_type": "string",
        "file_url": "string"
      },
      "contextual_update_info": {
        "context_id": "string",
        "is_superseded": false
      },
      "reasoned": false
    }
  ],
  "analysis": {
    "call_successful": "success",
    "transcript_summary": "string",
    "evaluation_criteria_results": {},
    "data_collection_results": {},
    "evaluation_criteria_results_list": [
      {
        "criteria_id": "string",
        "result": "success",
        "rationale": "string",
        "scoring_mode": "binary",
        "score": 1,
        "max_score": 1
      }
    ],
    "data_collection_results_list": [
      {
        "data_collection_id": "string",
        "rationale": "string",
        "value": null,
        "json_schema": {
          "type": "string",
          "description": "A user-provided message"
        }
      }
    ],
    "call_success_score": 1.1,
    "call_summary_title": "string",
    "scoped": [
      {
        "scope": "conversation",
        "source_agent_id": "string",
        "successful": "success",
        "source_branch_id": "string",
        "evaluation_criteria_results": {},
        "data_collection_results": {},
        "success_score": 1.1
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
    await client.conversationalAi.agents.simulateConversation("agent_id", {
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
    agent_id="agent_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/simulate-conversation"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/simulate-conversation")

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

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_id/simulate-conversation")
  .header("Content-Type", "application/json")
  .body("{\n  \"simulation_specification\": {\n    \"simulated_user_config\": {\n      \"first_message\": \"Hello, how can I help you today?\",\n      \"language\": \"en\",\n      \"disable_first_message_interruptions\": false\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/simulate-conversation', [
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/simulate-conversation");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/simulate-conversation")! as URL,
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
