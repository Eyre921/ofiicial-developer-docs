---
title: "Create draft"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/drafts/create.md
path: docs/eleven-agents/api-reference/agents/drafts/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create draft

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/drafts
Content-Type: application/json

Create a new draft for an agent

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/drafts/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/drafts:
    post:
      operationId: create
      summary: Create Agent Draft
      description: Create a new draft for an agent
      tags:
        - drafts
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
        - name: branch_id
          in: query
          description: The ID of the agent branch to use
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
                conversation_config:
                  type: object
                  additionalProperties:
                    description: Any type
                  description: Conversation config for the draft
                platform_settings:
                  type: object
                  additionalProperties:
                    description: Any type
                  description: Platform settings for the draft
                workflow:
                  $ref: '#/components/schemas/type_:AgentWorkflowRequestModel'
                  description: Workflow for the draft
                name:
                  type: string
                  description: Name for the draft
                tags:
                  type: array
                  items:
                    type: string
                  description: Tags to help classify and filter the agent
              required:
                - conversation_config
                - platform_settings
                - workflow
                - name
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
    type_:LlmLiteralJsonSchemaPropertyType:
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
      title: LlmLiteralJsonSchemaPropertyType
    type_:LlmLiteralJsonSchemaProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:LlmLiteralJsonSchemaPropertyType'
        description:
          type: string
        enum:
          type: array
          items:
            type: string
          description: List of allowed string values for string type parameters
      required:
        - type
        - description
      title: LlmLiteralJsonSchemaProperty
    type_:AstllmNodeInputValueSchema:
      type: object
      properties:
        type:
          type: string
          enum:
            - llm
        value_schema:
          $ref: '#/components/schemas/type_:LlmLiteralJsonSchemaProperty'
          description: JSON schema describing the value that the LLM should extract.
      required:
        - value_schema
      title: AstllmNodeInputValueSchema
    type_:AstllmNodeInputPrompt:
      type: object
      properties:
        type:
          type: string
          enum:
            - llm
        prompt:
          type: string
          description: >-
            The prompt to evaluate to a boolean value. Deprecated. Use a boolean
            schema instead.
      required:
        - prompt
      title: AstllmNodeInputPrompt
    type_:AstllmNodeInput:
      oneOf:
        - $ref: '#/components/schemas/type_:AstllmNodeInputValueSchema'
        - $ref: '#/components/schemas/type_:AstllmNodeInputPrompt'
      title: AstllmNodeInput
    type_:AstNodeInput:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - add_operator
              description: 'Discriminator value: add_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - and_operator
              description: 'Discriminator value: and_operator'
            children:
              type: array
              items:
                $ref: '#/components/schemas/type_:AstNodeInput'
              description: Child nodes of the logical operator.
          required:
            - type
            - children
        - type: object
          properties:
            type:
              type: string
              enum:
                - boolean_literal
              description: 'Discriminator value: boolean_literal'
            value:
              type: boolean
              description: Value of this literal.
          required:
            - type
            - value
        - type: object
          properties:
            type:
              type: string
              enum:
                - conditional_operator
              description: 'Discriminator value: conditional_operator'
            condition:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Condition deciding which expression should be selected.
            trueExpression:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Expression selected if the condition is true.
            falseExpression:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Expression selected if the condition is false.
          required:
            - type
            - condition
            - trueExpression
            - falseExpression
        - type: object
          properties:
            type:
              type: string
              enum:
                - div_operator
              description: 'Discriminator value: div_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - dynamic_variable
              description: 'Discriminator value: dynamic_variable'
            name:
              type: string
              description: The name of the dynamic variable.
          required:
            - type
            - name
        - type: object
          properties:
            type:
              type: string
              enum:
                - eq_operator
              description: 'Discriminator value: eq_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - gt_operator
              description: 'Discriminator value: gt_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - gte_operator
              description: 'Discriminator value: gte_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
            value:
              $ref: '#/components/schemas/type_:AstllmNodeInput'
          required:
            - type
            - value
        - type: object
          properties:
            type:
              type: string
              enum:
                - lt_operator
              description: 'Discriminator value: lt_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - lte_operator
              description: 'Discriminator value: lte_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - mul_operator
              description: 'Discriminator value: mul_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - neq_operator
              description: 'Discriminator value: neq_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
        - type: object
          properties:
            type:
              type: string
              enum:
                - null_literal
              description: 'Discriminator value: null_literal'
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - number_literal
              description: 'Discriminator value: number_literal'
            value:
              type: number
              format: double
              description: Value of this literal.
          required:
            - type
            - value
        - type: object
          properties:
            type:
              type: string
              enum:
                - or_operator
              description: 'Discriminator value: or_operator'
            children:
              type: array
              items:
                $ref: '#/components/schemas/type_:AstNodeInput'
              description: Child nodes of the logical operator.
          required:
            - type
            - children
        - type: object
          properties:
            type:
              type: string
              enum:
                - string_literal
              description: 'Discriminator value: string_literal'
            value:
              type: string
              description: Value of this literal.
          required:
            - type
            - value
        - type: object
          properties:
            type:
              type: string
              enum:
                - sub_operator
              description: 'Discriminator value: sub_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
      discriminator:
        propertyName: type
      title: AstNodeInput
    type_:WorkflowEdgeModelInputForwardCondition:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - expression
              description: 'Discriminator value: expression'
            label:
              type: string
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            expression:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Expression to evaluate.
          required:
            - type
            - expression
        - type: object
          properties:
            type:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
            label:
              type: string
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            condition:
              type: string
              description: Condition to evaluate
          required:
            - type
            - condition
        - type: object
          properties:
            type:
              type: string
              enum:
                - result
              description: 'Discriminator value: result'
            label:
              type: string
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            successful:
              type: boolean
              description: >-
                Whether all tools in the previously executed tool node were
                executed successfully.
          required:
            - type
            - successful
        - type: object
          properties:
            type:
              type: string
              enum:
                - unconditional
              description: 'Discriminator value: unconditional'
            label:
              type: string
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
          required:
            - type
      discriminator:
        propertyName: type
      title: WorkflowEdgeModelInputForwardCondition
    type_:WorkflowEdgeModelInputBackwardCondition:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - expression
              description: 'Discriminator value: expression'
            label:
              type: string
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            expression:
              $ref: '#/components/schemas/type_:AstNodeInput'
              description: Expression to evaluate.
          required:
            - type
            - expression
        - type: object
          properties:
            type:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
            label:
              type: string
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            condition:
              type: string
              description: Condition to evaluate
          required:
            - type
            - condition
        - type: object
          properties:
            type:
              type: string
              enum:
                - result
              description: 'Discriminator value: result'
            label:
              type: string
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            successful:
              type: boolean
              description: >-
                Whether all tools in the previously executed tool node were
                executed successfully.
          required:
            - type
            - successful
        - type: object
          properties:
            type:
              type: string
              enum:
                - unconditional
              description: 'Discriminator value: unconditional'
            label:
              type: string
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
          required:
            - type
      discriminator:
        propertyName: type
      title: WorkflowEdgeModelInputBackwardCondition
    type_:WorkflowEdgeModelInput:
      type: object
      properties:
        source:
          type: string
          description: ID of the source node.
        target:
          type: string
          description: ID of the target node.
        forward_condition:
          $ref: '#/components/schemas/type_:WorkflowEdgeModelInputForwardCondition'
          description: >-
            Condition that must be met for the edge to be traversed in the
            forward direction (source to target).
        backward_condition:
          $ref: '#/components/schemas/type_:WorkflowEdgeModelInputBackwardCondition'
          description: >-
            Condition that must be met for the edge to be traversed in the
            backward direction (target to source).
      required:
        - source
        - target
      title: WorkflowEdgeModelInput
    type_:PositionInput:
      type: object
      properties:
        x:
          type: number
          format: double
          default: 0
        'y':
          type: number
          format: double
          default: 0
      title: PositionInput
    type_:AsrQuality:
      type: string
      enum:
        - high
      title: AsrQuality
    type_:AsrProvider:
      type: string
      enum:
        - elevenlabs
        - scribe_realtime
      default: scribe_realtime
      title: AsrProvider
    type_:AsrInputFormat:
      type: string
      enum:
        - pcm_8000
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_44100
        - pcm_48000
        - ulaw_8000
      default: pcm_16000
      title: AsrInputFormat
    type_:AsrConversationalConfigWorkflowOverride:
      type: object
      properties:
        quality:
          $ref: '#/components/schemas/type_:AsrQuality'
          description: The quality of the transcription
        provider:
          $ref: '#/components/schemas/type_:AsrProvider'
          description: The provider of the transcription service
        user_input_audio_format:
          $ref: '#/components/schemas/type_:AsrInputFormat'
          description: The format of the audio to be transcribed
        keywords:
          type: array
          items:
            type: string
          description: Keywords to boost prediction probability for
      title: AsrConversationalConfigWorkflowOverride
    type_:TurnEagerness:
      type: string
      enum:
        - patient
        - normal
        - eager
      default: normal
      description: >-
        Agent's eagerness to respond. Higher values make agent wait for higher
        turn probability.
      title: TurnEagerness
    type_:SpellingPatience:
      type: string
      enum:
        - auto
        - 'off'
      default: auto
      description: >-
        Controls if the agent should be more patient when user is spelling
        numbers and named entities.
      title: SpellingPatience
    type_:TurnModel:
      type: string
      enum:
        - turn_v2
        - turn_v3
      default: turn_v3
      description: Version of the turn detection model to use.
      title: TurnModel
    type_:SoftTimeoutConfigWorkflowOverride:
      type: object
      properties:
        timeout_seconds:
          type: number
          format: double
          description: >-
            Time in seconds before showing the predefined message while waiting
            for LLM response. Set to -1 to disable.
        message:
          type: string
          description: >-
            Message to show when the first soft timeout is reached while waiting
            for LLM response. Supports dynamic variables (e.g.,
            {{system__time}}, {{custom_variable}}).
        additional_soft_timeout_messages:
          type: array
          items:
            type: string
          description: >-
            Extra static filler messages for subsequent soft timeouts in the
            same LLM generation. The first timeout uses `message`. If fewer
            messages are configured than `max_soft_timeouts_per_generation`, the
            last configured message is repeated; otherwise a built-in filler is
            used.
        use_llm_generated_message:
          type: boolean
          description: >-
            If enabled, the soft timeout message will be generated dynamically
            instead of using the static message.
        randomize_fillers:
          type: boolean
          description: >-
            If enabled, shuffle the order of static soft timeout messages once
            at the start of each turn. Only applies when
            use_llm_generated_message is false.
        max_soft_timeouts_per_generation:
          type: integer
          description: >-
            Maximum filler messages while waiting for a single LLM response.
            Fires every timeout_seconds until the LLM streams content or this
            limit is reached.
        llm_generated_message_prompt_override:
          type: string
          description: >-
            Custom prompt for generating the soft timeout filler message when
            use_llm_generated_message is enabled. Recent conversation context is
            provided as a separate user message. If not set, the default prompt
            will be used. Supports dynamic variables (e.g., {{system__time}},
            {{custom_variable}}).
      title: SoftTimeoutConfigWorkflowOverride
    type_:TurnConfigWorkflowOverride:
      type: object
      properties:
        turn_timeout:
          type: number
          format: double
          description: Maximum wait time for the user's reply before re-engaging the user
        initial_wait_time:
          type: number
          format: double
          description: >-
            How long the agent will wait for the user to start the conversation
            if the first message is empty. If not set, uses the regular
            turn_timeout.
        silence_end_call_timeout:
          type: number
          format: double
          description: >-
            Maximum wait time since the user last spoke before terminating the
            call
        turn_eagerness:
          $ref: '#/components/schemas/type_:TurnEagerness'
          description: >-
            Controls how eager the agent is to respond. Low = less eager (waits
            longer), Standard = default eagerness, High = more eager (responds
            sooner)
        spelling_patience:
          $ref: '#/components/schemas/type_:SpellingPatience'
          description: >-
            Controls if the agent should be more patient when user is spelling
            numbers and named entities. Auto = model based, Off = never wait
            extra
        speculative_turn:
          type: boolean
          description: >-
            When enabled, starts generating LLM responses during silence before
            full turn confidence is reached, reducing perceived latency. May
            increase LLM costs.
        retranscribe_on_turn_timeout:
          type: boolean
          description: >-
            When enabled, if VAD detects no speech, attempts to re-transcribe
            accumulated audio at turn timeout. Disables silence discount billing
            for affected turns.
        turn_model:
          $ref: '#/components/schemas/type_:TurnModel'
          description: Version of the turn detection model to use.
        interruption_ignore_terms:
          type: array
          items:
            type: string
          description: >-
            List of terms that should not trigger an interruption when spoken by
            the user (e.g. 'gotcha', 'understood'). Uses case-insensitive exact
            matching.
        transcribe_on_disabled_interruptions:
          type: boolean
          description: >-
            When interruptions are disabled, still transcribe what the user says
            so it can carry into the next turn. When off, user speech during a
            non-interruptible turn is ignored and won't trigger a turn.
        soft_timeout_config:
          $ref: '#/components/schemas/type_:SoftTimeoutConfigWorkflowOverride'
          description: >-
            Configuration for soft timeout functionality. Provides immediate
            feedback during longer LLM responses.
      title: TurnConfigWorkflowOverride
    type_:TtsConversationalModel:
      type: string
      enum:
        - eleven_turbo_v2
        - eleven_turbo_v2_5
        - eleven_flash_v2
        - eleven_flash_v2_5
        - eleven_multilingual_v2
        - eleven_v3_conversational
      default: eleven_flash_v2
      title: TtsConversationalModel
    type_:TtsModelFamily:
      type: string
      enum:
        - turbo
        - flash
        - multilingual
        - v3_conversational
      title: TtsModelFamily
    type_:TtsOptimizeStreamingLatency:
      type: integer
      title: TtsOptimizeStreamingLatency
    type_:SupportedVoice:
      type: object
      properties:
        label:
          type: string
        voice_id:
          type: string
        description:
          type: string
        language:
          type: string
        model_family:
          $ref: '#/components/schemas/type_:TtsModelFamily'
        optimize_streaming_latency:
          $ref: '#/components/schemas/type_:TtsOptimizeStreamingLatency'
        stability:
          type: number
          format: double
        speed:
          type: number
          format: double
        similarity_boost:
          type: number
          format: double
      required:
        - label
        - voice_id
      title: SupportedVoice
    type_:SuggestedAudioTag:
      type: object
      properties:
        tag:
          type: string
          description: >-
            Audio tag to use (for best performance, 1-2 words, e.g., 'happy',
            'excited')
        description:
          type: string
          description: Optional description of when to use this tag
      required:
        - tag
      title: SuggestedAudioTag
    type_:TtsOutputFormat:
      type: string
      enum:
        - pcm_8000
        - pcm_16000
        - pcm_22050
        - pcm_24000
        - pcm_44100
        - pcm_48000
        - ulaw_8000
      default: pcm_16000
      title: TtsOutputFormat
    type_:TextNormalisationType:
      type: string
      enum:
        - system_prompt
        - elevenlabs
      default: system_prompt
      description: Method for converting numbers to words before sending to TTS
      title: TextNormalisationType
    type_:PydanticPronunciationDictionaryVersionLocator:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
          description: The ID of the pronunciation dictionary
        version_id:
          type: string
          description: The ID of the version of the pronunciation dictionary
      required:
        - pronunciation_dictionary_id
      description: >-
        A locator for other documents to be able to reference a specific
        dictionary and it's version.

        This is a pydantic version of
        PronunciationDictionaryVersionLocatorDBModel.

        Required to ensure compat with the rest of the agent data models.
      title: PydanticPronunciationDictionaryVersionLocator
    type_:TtsConversationalConfigWorkflowOverrideInput:
      type: object
      properties:
        model_id:
          $ref: '#/components/schemas/type_:TtsConversationalModel'
          description: The model to use for TTS
        voice_id:
          type: string
          description: The voice ID to use for TTS
        supported_voices:
          type: array
          items:
            $ref: '#/components/schemas/type_:SupportedVoice'
          description: Additional supported voices for the agent
        expressive_mode:
          type: boolean
          description: >-
            When enabled, applies expressive audio tags prompt. Automatically
            disabled for non-v3 models.
        suggested_audio_tags:
          type: array
          items:
            $ref: '#/components/schemas/type_:SuggestedAudioTag'
          description: >-
            Suggested audio tags to boost expressive speech (for eleven_v3 and
            eleven_v3_conversational models). The agent can still use other tags
            not listed here.
        agent_output_audio_format:
          $ref: '#/components/schemas/type_:TtsOutputFormat'
          description: The audio format to use for TTS
        optimize_streaming_latency:
          $ref: '#/components/schemas/type_:TtsOptimizeStreamingLatency'
          description: The optimization for streaming latency
        stability:
          type: number
          format: double
          description: The stability of generated speech
        speed:
          type: number
          format: double
          description: The speed of generated speech
        similarity_boost:
          type: number
          format: double
          description: The similarity boost for generated speech
        text_normalisation_type:
          $ref: '#/components/schemas/type_:TextNormalisationType'
          description: >-
            Method for converting numbers to words before converting text to
            speech. If set to SYSTEM_PROMPT, the system prompt will be updated
            to include normalization instructions. If set to ELEVENLABS, the
            text will be normalized after generation, incurring slight
            additional latency.
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:PydanticPronunciationDictionaryVersionLocator
          description: The pronunciation dictionary locators
        enable_phoneme_tags:
          type: boolean
          description: >-
            Opt-in to SSML phoneme tag handling for V3 models. When enabled,
            phoneme tags (inline and from pronunciation dictionaries) are parsed
            into inline IPA before being sent to the model.
      title: TtsConversationalConfigWorkflowOverrideInput
    type_:ClientEvent:
      type: string
      enum:
        - conversation_initiation_metadata
        - asr_initiation_metadata
        - ping
        - audio
        - interruption
        - user_transcript
        - tentative_user_transcript
        - agent_response
        - agent_response_correction
        - client_tool_call
        - mcp_tool_call
        - mcp_connection_status
        - agent_tool_request
        - agent_tool_response
        - agent_tool_response_full_payload
        - agent_response_metadata
        - vad_score
        - agent_chat_response_part
        - client_error
        - guardrail_triggered
        - dtmf_request
        - agent_response_complete
        - internal_turn_probability
        - internal_tentative_agent_response
      title: ClientEvent
    type_:FileInputConfigWorkflowOverride:
      type: object
      properties:
        enabled:
          type: boolean
          description: >-
            When enabled, users may attach images or PDFs in chat when the LLM
            supports multimodal input.
        max_files_per_conversation:
          type: integer
          description: Maximum number of files that can be uploaded per conversation.
      title: FileInputConfigWorkflowOverride
    type_:BackgroundSoundSourceType:
      type: string
      enum:
        - preset
      description: The type of background sound source.
      title: BackgroundSoundSourceType
    type_:BackgroundSoundPresetId:
      type: string
      enum:
        - office2
        - office1
        - restaurant
        - city
        - typing
        - elevator1
        - elevator2
        - elevator3
        - elevator4
      description: Predefined background sound preset identifiers.
      title: BackgroundSoundPresetId
    type_:BackgroundSoundConfigWorkflowOverride:
      type: object
      properties:
        source_type:
          $ref: '#/components/schemas/type_:BackgroundSoundSourceType'
          description: The type of background sound source.
        source_id:
          $ref: '#/components/schemas/type_:BackgroundSoundPresetId'
          description: Identifier for the sound source.
        volume:
          type: number
          format: double
          description: Volume level for background sound (0.01 to 1.0).
        crossfade_loop:
          type: boolean
          description: >-
            Apply a crossfade at the loop boundary to avoid audible pops when
            the sound loops.
      title: BackgroundSoundConfigWorkflowOverride
    type_:ConversationConfigWorkflowOverrideInput:
      type: object
      properties:
        text_only:
          type: boolean
          description: >-
            If enabled audio will not be processed and only text will be used,
            use to avoid audio pricing.
        max_duration_seconds:
          type: integer
          description: The maximum duration of a conversation in seconds
        client_events:
          type: array
          items:
            $ref: '#/components/schemas/type_:ClientEvent'
          description: The events that will be sent to the client
        file_input:
          $ref: '#/components/schemas/type_:FileInputConfigWorkflowOverride'
          description: >-
            Configuration for file input (image/PDF uploads) during
            conversations.
        monitoring_enabled:
          type: boolean
          description: Enable real-time monitoring of conversations via WebSocket
        monitoring_events:
          type: array
          items:
            $ref: '#/components/schemas/type_:ClientEvent'
          description: The events that will be sent to monitoring connections.
        background_sound:
          $ref: '#/components/schemas/type_:BackgroundSoundConfigWorkflowOverride'
          description: Configuration for background sound during conversations.
        source_attribution:
          type: boolean
          description: >-
            When enabled and knowledge base content is present, the LLM is
            instructed to report which sources it used.
      title: ConversationConfigWorkflowOverrideInput
    type_:AsrConversationalConfigOverride:
      type: object
      properties:
        keywords:
          type: array
          items:
            type: string
          description: Keywords to boost prediction probability for
      title: AsrConversationalConfigOverride
    type_:SoftTimeoutConfigOverride:
      type: object
      properties:
        message:
          type: string
          description: >-
            Message to show when the first soft timeout is reached while waiting
            for LLM response. Supports dynamic variables (e.g.,
            {{system__time}}, {{custom_variable}}).
      title: SoftTimeoutConfigOverride
    type_:TurnConfigOverride:
      type: object
      properties:
        soft_timeout_config:
          $ref: '#/components/schemas/type_:SoftTimeoutConfigOverride'
          description: >-
            Configuration for soft timeout functionality. Provides immediate
            feedback during longer LLM responses.
      title: TurnConfigOverride
    type_:TtsConversationalConfigOverride:
      type: object
      properties:
        voice_id:
          type: string
          description: The voice ID to use for TTS
        stability:
          type: number
          format: double
          description: The stability of generated speech
        speed:
          type: number
          format: double
          description: The speed of generated speech
        similarity_boost:
          type: number
          format: double
          description: The similarity boost for generated speech
      title: TtsConversationalConfigOverride
    type_:ConversationConfigOverride:
      type: object
      properties:
        text_only:
          type: boolean
          description: >-
            If enabled audio will not be processed and only text will be used,
            use to avoid audio pricing.
      title: ConversationConfigOverride
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
      title: Llm
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
    type_:PromptAgentApiModelOverrideInput:
      type: object
      properties:
        prompt:
          type: string
          description: The prompt for the agent
        llm:
          $ref: '#/components/schemas/type_:Llm'
          description: >-
            The LLM to query with the prompt and the chat history. If using data
            residency, the LLM must be supported in the data residency
            environment
        tool_ids:
          type: array
          items:
            type: string
          description: A list of IDs of tools used by the agent
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
      title: PromptAgentApiModelOverrideInput
    type_:AgentConfigOverrideInput:
      type: object
      properties:
        first_message:
          type: string
          description: >-
            If non-empty, the first message the agent will say. If empty, the
            agent waits for the user to start the discussion.
        language:
          type: string
          description: Language of the agent - used for ASR and TTS
        max_conversation_duration_message:
          type: string
          description: >-
            If non-empty, the message the agent will send when max conversation
            duration is reached.
        prompt:
          $ref: '#/components/schemas/type_:PromptAgentApiModelOverrideInput'
          description: The prompt for the agent
      title: AgentConfigOverrideInput
    type_:ConversationConfigClientOverrideInput:
      type: object
      properties:
        asr:
          $ref: '#/components/schemas/type_:AsrConversationalConfigOverride'
          description: Configuration for conversational transcription
        turn:
          $ref: '#/components/schemas/type_:TurnConfigOverride'
          description: Configuration for turn detection
        tts:
          $ref: '#/components/schemas/type_:TtsConversationalConfigOverride'
          description: Configuration for conversational text to speech
        conversation:
          $ref: '#/components/schemas/type_:ConversationConfigOverride'
          description: Configuration for conversational events
        agent:
          $ref: '#/components/schemas/type_:AgentConfigOverrideInput'
          description: Agent specific configuration
      title: ConversationConfigClientOverrideInput
    type_:LanguagePresetTranslation:
      type: object
      properties:
        source_hash:
          type: string
        text:
          type: string
      required:
        - source_hash
        - text
      title: LanguagePresetTranslation
    type_:LanguagePresetInput:
      type: object
      properties:
        overrides:
          $ref: '#/components/schemas/type_:ConversationConfigClientOverrideInput'
          description: The overrides for the language preset
        first_message_translation:
          $ref: '#/components/schemas/type_:LanguagePresetTranslation'
          description: The translation of the first message
        soft_timeout_translation:
          $ref: '#/components/schemas/type_:LanguagePresetTranslation'
          description: The translation of the soft timeout message
      required:
        - overrides
      title: LanguagePresetInput
    type_:VadConfigWorkflowOverride:
      type: object
      properties: {}
      title: VadConfigWorkflowOverride
    type_:DynamicVariablesConfigWorkflowOverride:
      type: object
      properties:
        dynamic_variable_placeholders:
          type: object
          additionalProperties:
            description: Any type
          description: A dictionary of dynamic variable placeholders and their values
      title: DynamicVariablesConfigWorkflowOverride
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
    type_:LlmReasoningEffort:
      type: string
      enum:
        - none
        - minimal
        - low
        - medium
        - high
        - xhigh
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
      description: Predefined tool call sound types.
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
            How many recent customer messages to include in the guardrail's
            history, plus the agent replies that follow them (and tool calls and
            results when history_include_tool_calls is enabled). Only customer
            messages count toward the limit. 0 (default) shows none; 1 shows the
            customer's latest message onward. When > 0, the guardrail prompt can
            refer to this history as <conversation_history>; the reply under
            evaluation appears as <agent_message> and may repeat at the end of
            the history.
        trigger_action:
          $ref: '#/components/schemas/type_:CustomGuardrailConfigTriggerAction'
      required:
        - name
        - prompt
      description: Single custom guardrail configuration
      title: CustomGuardrailConfig
    type_:ProcedureAtVersionInput:
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
      title: ProcedureAtVersionInput
    type_:AgentTransfer:
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
      title: AgentTransfer
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
    type_:SystemToolConfigInputParams:
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
                $ref: '#/components/schemas/type_:ProcedureAtVersionInput'
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
                $ref: '#/components/schemas/type_:ProcedureAtVersionInput'
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
                $ref: '#/components/schemas/type_:AgentTransfer'
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
      title: SystemToolConfigInputParams
    type_:SystemToolConfigInput:
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
          $ref: '#/components/schemas/type_:SystemToolConfigInputParams'
      required:
        - name
        - params
      description: >-
        A system tool is a tool that is used to call a system method in the
        server
      title: SystemToolConfigInput
    type_:BuiltInToolsWorkflowOverrideInput:
      type: object
      properties:
        end_call:
          $ref: '#/components/schemas/type_:SystemToolConfigInput'
          description: The end call tool
        language_detection:
          $ref: '#/components/schemas/type_:SystemToolConfigInput'
          description: The language detection tool
        transfer_to_agent:
          $ref: '#/components/schemas/type_:SystemToolConfigInput'
          description: The transfer to agent tool
        transfer_to_number:
          $ref: '#/components/schemas/type_:SystemToolConfigInput'
          description: The transfer to number tool
        skip_turn:
          $ref: '#/components/schemas/type_:SystemToolConfigInput'
          description: The skip turn tool
        play_keypad_touch_tone:
          $ref: '#/components/schemas/type_:SystemToolConfigInput'
          description: The play DTMF tool
        voicemail_detection:
          $ref: '#/components/schemas/type_:SystemToolConfigInput'
          description: The voicemail detection tool
      title: BuiltInToolsWorkflowOverrideInput
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
          description: The API type to use (chat_completions or responses)
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
    type_:RagConfigWorkflowOverride:
      type: object
      properties:
        enabled:
          type: boolean
        embedding_model:
          $ref: '#/components/schemas/type_:EmbeddingModelEnum'
        max_vector_distance:
          type: number
          format: double
          description: Maximum vector distance of retrieved chunks.
        max_documents_length:
          type: integer
          description: Maximum total length of document chunks retrieved from RAG.
        max_retrieved_rag_chunks_count:
          type: integer
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
      title: RagConfigWorkflowOverride
    type_:BackupLlmDefault:
      type: object
      properties:
        preference:
          type: string
          enum:
            - default
      title: BackupLlmDefault
    type_:BackupLlmDisabled:
      type: object
      properties:
        preference:
          type: string
          enum:
            - disabled
      title: BackupLlmDisabled
    type_:BackupLlmOverride:
      type: object
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
        - order
      title: BackupLlmOverride
    type_:PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig:
      oneOf:
        - $ref: '#/components/schemas/type_:BackupLlmDefault'
        - $ref: '#/components/schemas/type_:BackupLlmDisabled'
        - $ref: '#/components/schemas/type_:BackupLlmOverride'
      description: >-
        Configuration for backup LLM cascading. Can be disabled, use system
        defaults, or specify custom order.
      title: PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig
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
    type_:ConstantSchemaOverrideConstantValueFourItem:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
      title: ConstantSchemaOverrideConstantValueFourItem
    type_:ConstantSchemaOverrideConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
        - type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConstantSchemaOverrideConstantValueFourItem
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
    type_:ArrayJsonSchemaPropertyInputItems:
      oneOf:
        - $ref: '#/components/schemas/type_:LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyInput'
        - $ref: '#/components/schemas/type_:ArrayJsonSchemaPropertyInput'
      description: Schema for array elements.
      title: ArrayJsonSchemaPropertyInputItems
    type_:ArrayJsonSchemaPropertyInputConstantValueItem:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
      title: ArrayJsonSchemaPropertyInputConstantValueItem
    type_:ArrayJsonSchemaPropertyInput:
      type: object
      properties:
        type:
          type: string
          enum:
            - array
        description:
          type: string
          default: ''
        items:
          $ref: '#/components/schemas/type_:ArrayJsonSchemaPropertyInputItems'
          description: Schema for array elements.
        dynamic_variable:
          type: string
          default: ''
          description: >-
            When set, the entire array is populated from this dynamic variable
            at runtime. Mutually exclusive with description (LLM-provided
            array), constant_value, and is_omitted.
        constant_value:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ArrayJsonSchemaPropertyInputConstantValueItem
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
      title: ArrayJsonSchemaPropertyInput
    type_:ObjectJsonSchemaPropertyInputPropertiesValue:
      oneOf:
        - $ref: '#/components/schemas/type_:LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyInput'
        - $ref: '#/components/schemas/type_:ArrayJsonSchemaPropertyInput'
      title: ObjectJsonSchemaPropertyInputPropertiesValue
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
    type_:ObjectJsonSchemaPropertyInput:
      type: object
      properties:
        type:
          type: string
          enum:
            - object
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
            $ref: >-
              #/components/schemas/type_:ObjectJsonSchemaPropertyInputPropertiesValue
        required_constraints:
          $ref: '#/components/schemas/type_:RequiredConstraints'
      title: ObjectJsonSchemaPropertyInput
    type_:WebhookToolApiSchemaConfigInputRequestHeadersValue:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
        - $ref: '#/components/schemas/type_:ConvAiDynamicVariable'
        - $ref: '#/components/schemas/type_:ConvAiEnvVarLocator'
      title: WebhookToolApiSchemaConfigInputRequestHeadersValue
    type_:WebhookToolApiSchemaConfigInputMethod:
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
    type_:WebhookToolApiSchemaConfigInputContentType:
      type: string
      enum:
        - application/json
        - application/x-www-form-urlencoded
      default: application/json
      description: >-
        Content type for the request body. Only applies to POST/PUT/PATCH
        requests.
      title: WebhookToolApiSchemaConfigInputContentType
    type_:WebhookToolApiSchemaConfigInputAuthConnection:
      oneOf:
        - $ref: '#/components/schemas/type_:AuthConnectionLocator'
        - $ref: '#/components/schemas/type_:EnvironmentAuthConnectionLocator'
      description: Optional auth connection to use for authentication with this webhook
      title: WebhookToolApiSchemaConfigInputAuthConnection
    type_:WebhookToolApiSchemaConfigInput:
      type: object
      properties:
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:WebhookToolApiSchemaConfigInputRequestHeadersValue
          description: Headers that should be included in the request
        url:
          type: string
          description: >-
            The URL that the webhook will be sent to. May include path
            parameters, e.g. https://example.com/agents/{agent_id}
        method:
          $ref: '#/components/schemas/type_:WebhookToolApiSchemaConfigInputMethod'
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
          $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyInput'
          description: >-
            Schema for the body parameters, if any. Used for POST/PATCH/PUT
            requests. The schema should be an object which will be sent as the
            json body
        response_body_schema:
          $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyInput'
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
            #/components/schemas/type_:WebhookToolApiSchemaConfigInputContentType
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
            #/components/schemas/type_:WebhookToolApiSchemaConfigInputAuthConnection
          description: Optional auth connection to use for authentication with this webhook
      required:
        - url
      title: WebhookToolApiSchemaConfigInput
    type_:PromptAgentApiModelWorkflowOverrideInputToolsItem:
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
              $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyInput'
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
              $ref: '#/components/schemas/type_:SystemToolConfigInputParams'
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
                complete. Must be between 5 and 120 seconds (inclusive).
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
              $ref: '#/components/schemas/type_:WebhookToolApiSchemaConfigInput'
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
      title: PromptAgentApiModelWorkflowOverrideInputToolsItem
    type_:PromptAgentApiModelWorkflowOverrideInput:
      type: object
      properties:
        prompt:
          type: string
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
          description: If greater than 0, maximum number of tokens the LLM can predict
        tool_ids:
          type: array
          items:
            type: string
          description: A list of IDs of tools used by the agent
        built_in_tools:
          $ref: '#/components/schemas/type_:BuiltInToolsWorkflowOverrideInput'
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
          $ref: '#/components/schemas/type_:RagConfigWorkflowOverride'
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
          $ref: >-
            #/components/schemas/type_:PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig
          description: >-
            Configuration for backup LLM cascading. Can be disabled, use system
            defaults, or specify custom order.
        cascade_timeout_seconds:
          type: number
          format: double
          description: >-
            Time in seconds before cascading to backup LLM. Must be between 2
            and 15 seconds.
        tools:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:PromptAgentApiModelWorkflowOverrideInputToolsItem
          description: >-
            A list of tools that the agent can use over the course of the
            conversation, use tool_ids instead
      title: PromptAgentApiModelWorkflowOverrideInput
    type_:AgentConfigApiModelWorkflowOverrideInput:
      type: object
      properties:
        first_message:
          type: string
          description: >-
            If non-empty, the first message the agent will say. If empty, the
            agent waits for the user to start the discussion.
        language:
          type: string
          description: Language of the agent - used for ASR and TTS
        hinglish_mode:
          type: boolean
          description: >-
            When enabled and language is Hindi, the agent will respond in
            Hinglish
        dynamic_variables:
          $ref: '#/components/schemas/type_:DynamicVariablesConfigWorkflowOverride'
          description: Configuration for dynamic variables
        disable_first_message_interruptions:
          type: boolean
          description: >-
            If true, the user will not be able to interrupt the agent while the
            first message is being delivered.
        max_conversation_duration_message:
          type: string
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
          $ref: '#/components/schemas/type_:PromptAgentApiModelWorkflowOverrideInput'
          description: The prompt for the agent
      title: AgentConfigApiModelWorkflowOverrideInput
    type_:ConversationalConfigApiModelWorkflowOverrideInput:
      type: object
      properties:
        asr:
          $ref: '#/components/schemas/type_:AsrConversationalConfigWorkflowOverride'
          description: Configuration for conversational transcription
        turn:
          $ref: '#/components/schemas/type_:TurnConfigWorkflowOverride'
          description: Configuration for turn detection
        tts:
          $ref: >-
            #/components/schemas/type_:TtsConversationalConfigWorkflowOverrideInput
          description: Configuration for conversational text to speech
        conversation:
          $ref: '#/components/schemas/type_:ConversationConfigWorkflowOverrideInput'
          description: Configuration for conversational events
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:LanguagePresetInput'
          description: Language presets for conversations
        vad:
          $ref: '#/components/schemas/type_:VadConfigWorkflowOverride'
          description: Configuration for voice activity detection
        agent:
          $ref: '#/components/schemas/type_:AgentConfigApiModelWorkflowOverrideInput'
          description: Agent specific configuration
      title: ConversationalConfigApiModelWorkflowOverrideInput
    type_:EntryBehavior:
      type: string
      enum:
        - generate_immediately
        - wait_for_user
        - auto
      default: auto
      title: EntryBehavior
    type_:WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem:
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
      title: WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem
    type_:WorkflowPhoneNumberNodeModelInputTransferDestination:
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
      title: WorkflowPhoneNumberNodeModelInputTransferDestination
    type_:WorkflowPhoneNumberNodeModelInputPostDialDigits:
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
      title: WorkflowPhoneNumberNodeModelInputPostDialDigits
    type_:WorkflowToolLocator:
      type: object
      properties:
        tool_id:
          type: string
      required:
        - tool_id
      title: WorkflowToolLocator
    type_:AgentWorkflowRequestModelNodesValue:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - end
              description: 'Discriminator value: end'
            position:
              $ref: '#/components/schemas/type_:PositionInput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - override_agent
              description: 'Discriminator value: override_agent'
            position:
              $ref: '#/components/schemas/type_:PositionInput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
            conversation_config:
              $ref: >-
                #/components/schemas/type_:ConversationalConfigApiModelWorkflowOverrideInput
              description: >-
                Configuration overrides applied while the subagent is conducting
                the conversation.
            additional_prompt:
              type: string
              description: >-
                Specific goal for this subagent. It will be added to the system
                prompt and can be used to further refine the agent's behavior in
                this specific context.
            additional_knowledge_base:
              type: array
              items:
                $ref: '#/components/schemas/type_:KnowledgeBaseLocator'
              description: >-
                Additional knowledge base documents that the subagent has access
                to. These will be used in addition to the main agent's
                documents.
            additional_tool_ids:
              type: array
              items:
                type: string
              description: >-
                IDs of additional tools that the subagent has access to. These
                will be used in addition to the main agent's tools.
            label:
              type: string
              description: Human-readable label for the node used throughout the UI.
            entry_behavior:
              $ref: '#/components/schemas/type_:EntryBehavior'
              description: >-
                Dictates whether this node should immediately generate a
                response upon entry or wait for the user input. When set to
                "auto", the behavior will be decided based on the type of the
                preceding node: "wait_for_user" after the "say" and "start"
                nodes and "generate_immediately" otherwise.
          required:
            - type
            - label
        - type: object
          properties:
            type:
              type: string
              enum:
                - phone_number
              description: 'Discriminator value: phone_number'
            custom_sip_headers:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:WorkflowPhoneNumberNodeModelInputCustomSipHeadersItem
              description: >-
                Custom SIP headers to include when transferring the call. Each
                header can be either a static value or a dynamic variable
                reference.
            transfer_destination:
              $ref: >-
                #/components/schemas/type_:WorkflowPhoneNumberNodeModelInputTransferDestination
            transfer_type:
              $ref: '#/components/schemas/type_:TransferTypeEnum'
            uui:
              $ref: '#/components/schemas/type_:UuiTransferConfig'
              description: >-
                User-to-User Information (RFC 7433) to attach to SIP REFER
                transfers. Carries call context such as CRM identifiers or
                escalation reason across the transfer boundary.
            post_dial_digits:
              $ref: >-
                #/components/schemas/type_:WorkflowPhoneNumberNodeModelInputPostDialDigits
              description: >-
                DTMF digits to send after call connects (e.g., 'ww1234' for
                extension). Can be either a static value or a dynamic variable
                reference. Use 'w' for 0.5s pause. Only supported for Twilio
                transfers.
            position:
              $ref: '#/components/schemas/type_:PositionInput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
            - transfer_destination
        - type: object
          properties:
            type:
              type: string
              enum:
                - standalone_agent
              description: 'Discriminator value: standalone_agent'
            position:
              $ref: '#/components/schemas/type_:PositionInput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
            agent_id:
              type: string
              description: >-
                The ID of the agent to transfer the conversation to. None means
                transfer within the current agent.
            node_id:
              type: string
              description: >-
                Optional target node ID in the destination agent's workflow.
                When set, the transfer starts at this node instead of the
                default entry node.
            delay_ms:
              type: integer
              default: 0
              description: >-
                Artificial delay in milliseconds applied before transferring the
                conversation.
            transfer_message:
              type: string
              description: >-
                Optional message sent to the user before the transfer is
                initiated.
            enable_transferred_agent_first_message:
              type: boolean
              default: false
              description: >-
                Whether to enable the transferred agent to send its configured
                first message after the transfer.
            preserve_client_tts_overrides:
              type: boolean
              default: false
              description: >-
                Defines whether TTS client overrides should be carried over to
                the transferred agent.
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - start
              description: 'Discriminator value: start'
            position:
              $ref: '#/components/schemas/type_:PositionInput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - tool
              description: 'Discriminator value: tool'
            position:
              $ref: '#/components/schemas/type_:PositionInput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
            tools:
              type: array
              items:
                $ref: '#/components/schemas/type_:WorkflowToolLocator'
              description: >-
                List of tools to execute in parallel. The entire node is
                considered successful if all tools are executed successfully.
          required:
            - type
      discriminator:
        propertyName: type
      title: AgentWorkflowRequestModelNodesValue
    type_:AgentWorkflowRequestModel:
      type: object
      properties:
        edges:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:WorkflowEdgeModelInput'
        nodes:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:AgentWorkflowRequestModelNodesValue'
        prevent_subagent_loops:
          type: boolean
          default: false
          description: Whether to prevent loops in the workflow execution.
      title: AgentWorkflowRequestModel
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
  "conversation_config": {
    "key": "value"
  },
  "platform_settings": {
    "key": "value"
  },
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_end": {
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_phone": {
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      }
    },
    "nodes": {
      "entry_node": {
        "type": "end"
      },
      "failure_node": {
        "type": "end"
      },
      "start_node": {
        "type": "end"
      },
      "success_conversation": {
        "type": "end"
      },
      "success_end": {
        "type": "end"
      },
      "success_phone": {
        "type": "end"
      },
      "success_transfer": {
        "type": "end"
      },
      "tool_node_a": {
        "type": "end"
      },
      "tool_node_b": {
        "type": "end"
      }
    }
  },
  "name": "name"
}
```

**Response**

```json
{
  "key": "value"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.drafts.create("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        branchId: "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        conversationConfig: {
            "key": "value",
        },
        platformSettings: {
            "key": "value",
        },
        workflow: {
            edges: {
                "entry_to_tool_a": {
                    source: "entry_node",
                    target: "tool_node_a",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "start_to_entry": {
                    source: "start_node",
                    target: "entry_node",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_a_to_failure": {
                    source: "tool_node_a",
                    target: "failure_node",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_a_to_tool_b": {
                    source: "tool_node_a",
                    target: "tool_node_b",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_b_to_agent_transfer": {
                    source: "tool_node_b",
                    target: "success_transfer",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_b_to_conversation": {
                    source: "tool_node_b",
                    target: "success_conversation",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_b_to_end": {
                    source: "tool_node_b",
                    target: "success_end",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
                "tool_b_to_phone": {
                    source: "tool_node_b",
                    target: "success_phone",
                    forwardCondition: {
                        type: "expression",
                        expression: {
                            type: "and_operator",
                            children: [],
                        },
                    },
                },
            },
            nodes: {
                "entry_node": {
                    type: "end",
                },
                "failure_node": {
                    type: "end",
                },
                "start_node": {
                    type: "end",
                },
                "success_conversation": {
                    type: "end",
                },
                "success_end": {
                    type: "end",
                },
                "success_phone": {
                    type: "end",
                },
                "success_transfer": {
                    type: "end",
                },
                "tool_node_a": {
                    type: "end",
                },
                "tool_node_b": {
                    type: "end",
                },
            },
        },
        name: "name",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, AgentWorkflowRequestModel, WorkflowEdgeModelInput, WorkflowEdgeModelInputForwardCondition_Expression, AstNodeInput_AndOperator, AgentWorkflowRequestModelNodesValue_End

client = ElevenLabs()

client.conversational_ai.agents.drafts.create(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
    conversation_config={
        "key": "value"
    },
    platform_settings={
        "key": "value"
    },
    workflow=AgentWorkflowRequestModel(
        edges={
            "entry_to_tool_a": WorkflowEdgeModelInput(
                source="entry_node",
                target="tool_node_a",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "start_to_entry": WorkflowEdgeModelInput(
                source="start_node",
                target="entry_node",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_a_to_failure": WorkflowEdgeModelInput(
                source="tool_node_a",
                target="failure_node",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_a_to_tool_b": WorkflowEdgeModelInput(
                source="tool_node_a",
                target="tool_node_b",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_b_to_agent_transfer": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_transfer",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_b_to_conversation": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_conversation",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_b_to_end": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_end",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            ),
            "tool_b_to_phone": WorkflowEdgeModelInput(
                source="tool_node_b",
                target="success_phone",
                forward_condition=WorkflowEdgeModelInputForwardCondition_Expression(
                    expression=AstNodeInput_AndOperator(
                        children=[],
                    ),
                ),
            )
        },
        nodes={
            "entry_node": AgentWorkflowRequestModelNodesValue_End(),
            "failure_node": AgentWorkflowRequestModelNodesValue_End(),
            "start_node": AgentWorkflowRequestModelNodesValue_End(),
            "success_conversation": AgentWorkflowRequestModelNodesValue_End(),
            "success_end": AgentWorkflowRequestModelNodesValue_End(),
            "success_phone": AgentWorkflowRequestModelNodesValue_End(),
            "success_transfer": AgentWorkflowRequestModelNodesValue_End(),
            "tool_node_a": AgentWorkflowRequestModelNodesValue_End(),
            "tool_node_b": AgentWorkflowRequestModelNodesValue_End()
        },
    ),
    name="name",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj"

	payload := strings.NewReader("{\n  \"conversation_config\": {\n    \"key\": \"value\"\n  },\n  \"platform_settings\": {\n    \"key\": \"value\"\n  },\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"type\": \"end\"\n      },\n      \"failure_node\": {\n        \"type\": \"end\"\n      },\n      \"start_node\": {\n        \"type\": \"end\"\n      },\n      \"success_conversation\": {\n        \"type\": \"end\"\n      },\n      \"success_end\": {\n        \"type\": \"end\"\n      },\n      \"success_phone\": {\n        \"type\": \"end\"\n      },\n      \"success_transfer\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_a\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_b\": {\n        \"type\": \"end\"\n      }\n    }\n  },\n  \"name\": \"name\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"conversation_config\": {\n    \"key\": \"value\"\n  },\n  \"platform_settings\": {\n    \"key\": \"value\"\n  },\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"type\": \"end\"\n      },\n      \"failure_node\": {\n        \"type\": \"end\"\n      },\n      \"start_node\": {\n        \"type\": \"end\"\n      },\n      \"success_conversation\": {\n        \"type\": \"end\"\n      },\n      \"success_end\": {\n        \"type\": \"end\"\n      },\n      \"success_phone\": {\n        \"type\": \"end\"\n      },\n      \"success_transfer\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_a\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_b\": {\n        \"type\": \"end\"\n      }\n    }\n  },\n  \"name\": \"name\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")
  .header("Content-Type", "application/json")
  .body("{\n  \"conversation_config\": {\n    \"key\": \"value\"\n  },\n  \"platform_settings\": {\n    \"key\": \"value\"\n  },\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"type\": \"end\"\n      },\n      \"failure_node\": {\n        \"type\": \"end\"\n      },\n      \"start_node\": {\n        \"type\": \"end\"\n      },\n      \"success_conversation\": {\n        \"type\": \"end\"\n      },\n      \"success_end\": {\n        \"type\": \"end\"\n      },\n      \"success_phone\": {\n        \"type\": \"end\"\n      },\n      \"success_transfer\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_a\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_b\": {\n        \"type\": \"end\"\n      }\n    }\n  },\n  \"name\": \"name\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj', [
  'body' => '{
  "conversation_config": {
    "key": "value"
  },
  "platform_settings": {
    "key": "value"
  },
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_end": {
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      },
      "tool_b_to_phone": {
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          }
        }
      }
    },
    "nodes": {
      "entry_node": {
        "type": "end"
      },
      "failure_node": {
        "type": "end"
      },
      "start_node": {
        "type": "end"
      },
      "success_conversation": {
        "type": "end"
      },
      "success_end": {
        "type": "end"
      },
      "success_phone": {
        "type": "end"
      },
      "success_transfer": {
        "type": "end"
      },
      "tool_node_a": {
        "type": "end"
      },
      "tool_node_b": {
        "type": "end"
      }
    }
  },
  "name": "name"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"conversation_config\": {\n    \"key\": \"value\"\n  },\n  \"platform_settings\": {\n    \"key\": \"value\"\n  },\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"type\": \"expression\",\n          \"expression\": {\n            \"type\": \"and_operator\",\n            \"children\": []\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"type\": \"end\"\n      },\n      \"failure_node\": {\n        \"type\": \"end\"\n      },\n      \"start_node\": {\n        \"type\": \"end\"\n      },\n      \"success_conversation\": {\n        \"type\": \"end\"\n      },\n      \"success_end\": {\n        \"type\": \"end\"\n      },\n      \"success_phone\": {\n        \"type\": \"end\"\n      },\n      \"success_transfer\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_a\": {\n        \"type\": \"end\"\n      },\n      \"tool_node_b\": {\n        \"type\": \"end\"\n      }\n    }\n  },\n  \"name\": \"name\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "conversation_config": ["key": "value"],
  "platform_settings": ["key": "value"],
  "workflow": [
    "edges": [
      "entry_to_tool_a": [
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "start_to_entry": [
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_a_to_failure": [
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_a_to_tool_b": [
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_b_to_agent_transfer": [
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_b_to_conversation": [
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_b_to_end": [
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ],
      "tool_b_to_phone": [
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": [
          "type": "expression",
          "expression": [
            "type": "and_operator",
            "children": []
          ]
        ]
      ]
    ],
    "nodes": [
      "entry_node": ["type": "end"],
      "failure_node": ["type": "end"],
      "start_node": ["type": "end"],
      "success_conversation": ["type": "end"],
      "success_end": ["type": "end"],
      "success_phone": ["type": "end"],
      "success_transfer": ["type": "end"],
      "tool_node_a": ["type": "end"],
      "tool_node_b": ["type": "end"]
    ]
  ],
  "name": "name"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/drafts?branch_id=agtbrch_8901k4t9z5defmb8vh3e9361y7nj")! as URL,
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
