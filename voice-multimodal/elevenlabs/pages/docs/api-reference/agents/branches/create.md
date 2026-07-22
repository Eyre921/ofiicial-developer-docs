---
title: "Create agent branch"
source: https://elevenlabs.io/docs/api-reference/agents/branches/create.md
path: docs/api-reference/agents/branches/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create agent branch

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches
Content-Type: application/json

Create a new branch from a given version of any branch

Reference: https://elevenlabs.io/docs/api-reference/agents/branches/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/branches:
    post:
      operationId: create
      summary: Create A New Branch
      description: Create a new branch from a given version of any branch
      tags:
        - branches
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
                $ref: '#/components/schemas/CreateAgentBranchResponseModel'
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
                #/components/schemas/Body_Create_a_new_branch_v1_convai_agents__agent_id__branches_post
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
    LlmLiteralJsonSchemaPropertyType0:
      type: string
      enum:
        - boolean
        - string
        - integer
        - number
      title: LlmLiteralJsonSchemaPropertyType0
    LlmLiteralJsonSchemaPropertyType:
      oneOf:
        - $ref: '#/components/schemas/LlmLiteralJsonSchemaPropertyType0'
        - type: array
          items:
            type: string
      title: LlmLiteralJsonSchemaPropertyType
    LLMLiteralJsonSchemaProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/LlmLiteralJsonSchemaPropertyType'
        description:
          type: string
        enum:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of allowed string values for string type parameters
      required:
        - type
        - description
      title: LLMLiteralJsonSchemaProperty
    AstllmNodeInput0:
      type: object
      properties:
        type:
          type: string
          enum:
            - llm
          default: llm
        value_schema:
          $ref: '#/components/schemas/LLMLiteralJsonSchemaProperty'
          description: JSON schema describing the value that the LLM should extract.
      required:
        - value_schema
      title: AstllmNodeInput0
    AstllmNodeInput1:
      type: object
      properties:
        type:
          type: string
          enum:
            - llm
          default: llm
        prompt:
          type: string
          description: >-
            The prompt to evaluate to a boolean value. Deprecated. Use a boolean
            schema instead.
      required:
        - prompt
      title: AstllmNodeInput1
    ASTNode-Input:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - add_operator
              description: 'Discriminator value: add_operator'
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTAdditionOperatorNode variant
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
                $ref: '#/components/schemas/ASTNode-Input'
              description: Child nodes of the logical operator.
          required:
            - type
            - children
          description: ASTAndOperatorNode variant
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
          description: ASTBooleanNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - conditional_operator
              description: 'Discriminator value: conditional_operator'
            condition:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Condition deciding which expression should be selected.
            trueExpression:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Expression selected if the condition is true.
            falseExpression:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Expression selected if the condition is false.
          required:
            - type
            - condition
            - trueExpression
            - falseExpression
          description: ASTConditionalOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - div_operator
              description: 'Discriminator value: div_operator'
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTDivisionOperatorNode variant
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
          description: ASTDynamicVariableNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - eq_operator
              description: 'Discriminator value: eq_operator'
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTEqualsOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - gt_operator
              description: 'Discriminator value: gt_operator'
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTGreaterThanOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - gte_operator
              description: 'Discriminator value: gte_operator'
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTGreaterThanOrEqualsOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
          required:
            - type
          description: llm variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - lt_operator
              description: 'Discriminator value: lt_operator'
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTLessThanOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - lte_operator
              description: 'Discriminator value: lte_operator'
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTLessThanOrEqualsOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - mul_operator
              description: 'Discriminator value: mul_operator'
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTMultiplicationOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - neq_operator
              default: neq_operator
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTNotEqualsOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - null_literal
              default: null_literal
          required:
            - type
          description: ASTNullNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - number_literal
              default: number_literal
            value:
              type: number
              format: double
              description: Value of this literal.
          required:
            - type
            - value
          description: ASTNumberNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - or_operator
              default: or_operator
            children:
              type: array
              items:
                $ref: '#/components/schemas/ASTNode-Input'
              description: Child nodes of the logical operator.
          required:
            - type
            - children
          description: ASTOrOperatorNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - string_literal
              default: string_literal
            value:
              type: string
              description: Value of this literal.
          required:
            - type
            - value
          description: ASTStringNode variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - sub_operator
              default: sub_operator
            left:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
          description: ASTSubtractionOperatorNode variant
      discriminator:
        propertyName: type
      title: ASTNode-Input
    WorkflowEdgeModelInputForwardCondition:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - expression
              default: expression
            label:
              type:
                - string
                - 'null'
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            expression:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Expression to evaluate.
          required:
            - type
            - expression
          description: WorkflowExpressionConditionModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - llm
              default: llm
            label:
              type:
                - string
                - 'null'
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            condition:
              type: string
              description: Condition to evaluate
          required:
            - type
            - condition
          description: WorkflowLLMConditionModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - result
              default: result
            label:
              type:
                - string
                - 'null'
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
          description: WorkflowResultConditionModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - unconditional
              default: unconditional
            label:
              type:
                - string
                - 'null'
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
          required:
            - type
          description: WorkflowUnconditionalModel variant
      discriminator:
        propertyName: type
      description: >-
        Condition that must be met for the edge to be traversed in the forward
        direction (source to target).
      title: WorkflowEdgeModelInputForwardCondition
    WorkflowEdgeModelInputBackwardCondition:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - expression
              default: expression
            label:
              type:
                - string
                - 'null'
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            expression:
              $ref: '#/components/schemas/ASTNode-Input'
              description: Expression to evaluate.
          required:
            - type
            - expression
          description: WorkflowExpressionConditionModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - llm
              default: llm
            label:
              type:
                - string
                - 'null'
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
            condition:
              type: string
              description: Condition to evaluate
          required:
            - type
            - condition
          description: WorkflowLLMConditionModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - result
              default: result
            label:
              type:
                - string
                - 'null'
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
          description: WorkflowResultConditionModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - unconditional
              default: unconditional
            label:
              type:
                - string
                - 'null'
              description: >-
                Optional human-readable label for the condition used throughout
                the UI.
          required:
            - type
          description: WorkflowUnconditionalModel variant
      discriminator:
        propertyName: type
      description: >-
        Condition that must be met for the edge to be traversed in the backward
        direction (target to source).
      title: WorkflowEdgeModelInputBackwardCondition
    WorkflowEdgeModel-Input:
      type: object
      properties:
        source:
          type: string
          description: ID of the source node.
        target:
          type: string
          description: ID of the target node.
        forward_condition:
          oneOf:
            - $ref: '#/components/schemas/WorkflowEdgeModelInputForwardCondition'
            - type: 'null'
          description: >-
            Condition that must be met for the edge to be traversed in the
            forward direction (source to target).
        backward_condition:
          oneOf:
            - $ref: '#/components/schemas/WorkflowEdgeModelInputBackwardCondition'
            - type: 'null'
          description: >-
            Condition that must be met for the edge to be traversed in the
            backward direction (target to source).
      required:
        - source
        - target
      title: WorkflowEdgeModel-Input
    Position-Input:
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
      title: Position-Input
    ASRQuality:
      type: string
      enum:
        - high
      default: high
      title: ASRQuality
    ASRProvider:
      type: string
      enum:
        - elevenlabs
        - scribe_realtime
      default: scribe_realtime
      title: ASRProvider
    ASRInputFormat:
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
      title: ASRInputFormat
    ASRConversationalConfigWorkflowOverride:
      type: object
      properties:
        quality:
          oneOf:
            - $ref: '#/components/schemas/ASRQuality'
            - type: 'null'
          description: The quality of the transcription
        provider:
          oneOf:
            - $ref: '#/components/schemas/ASRProvider'
            - type: 'null'
          description: The provider of the transcription service
        user_input_audio_format:
          oneOf:
            - $ref: '#/components/schemas/ASRInputFormat'
            - type: 'null'
          description: The format of the audio to be transcribed
        keywords:
          type:
            - array
            - 'null'
          items:
            type: string
          description: Keywords to boost prediction probability for
      title: ASRConversationalConfigWorkflowOverride
    TurnEagerness:
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
    SpellingPatience:
      type: string
      enum:
        - auto
        - 'off'
      default: auto
      description: >-
        Controls if the agent should be more patient when user is spelling
        numbers and named entities.
      title: SpellingPatience
    TurnModel:
      type: string
      enum:
        - turn_v2
        - turn_v3
      default: turn_v3
      description: Version of the turn detection model to use.
      title: TurnModel
    SoftTimeoutConfigWorkflowOverride:
      type: object
      properties:
        timeout_seconds:
          type:
            - number
            - 'null'
          format: double
          description: >-
            Time in seconds before showing the predefined message while waiting
            for LLM response. Set to -1 to disable.
        message:
          type:
            - string
            - 'null'
          description: >-
            Message to show when the first soft timeout is reached while waiting
            for LLM response. Supports dynamic variables (e.g.,
            {{system__time}}, {{custom_variable}}).
        additional_soft_timeout_messages:
          type:
            - array
            - 'null'
          items:
            type: string
          description: >-
            Extra static filler messages for subsequent soft timeouts in the
            same LLM generation. The first timeout uses `message`. If fewer
            messages are configured than `max_soft_timeouts_per_generation`, the
            last configured message is repeated; otherwise a built-in filler is
            used.
        use_llm_generated_message:
          type:
            - boolean
            - 'null'
          description: >-
            If enabled, the soft timeout message will be generated dynamically
            instead of using the static message.
        randomize_fillers:
          type:
            - boolean
            - 'null'
          description: >-
            If enabled, shuffle the order of static soft timeout messages once
            at the start of each turn. Only applies when
            use_llm_generated_message is false.
        max_soft_timeouts_per_generation:
          type:
            - integer
            - 'null'
          description: >-
            Maximum filler messages while waiting for a single LLM response.
            Fires every timeout_seconds until the LLM streams content or this
            limit is reached.
        llm_generated_message_prompt_override:
          type:
            - string
            - 'null'
          description: >-
            Custom prompt for generating the soft timeout filler message when
            use_llm_generated_message is enabled. Recent conversation context is
            provided as a separate user message. If not set, the default prompt
            will be used. Supports dynamic variables (e.g., {{system__time}},
            {{custom_variable}}).
      title: SoftTimeoutConfigWorkflowOverride
    TurnConfigWorkflowOverride:
      type: object
      properties:
        turn_timeout:
          type:
            - number
            - 'null'
          format: double
          description: Maximum wait time for the user's reply before re-engaging the user
        initial_wait_time:
          type:
            - number
            - 'null'
          format: double
          description: >-
            How long the agent will wait for the user to start the conversation
            if the first message is empty. If not set, uses the regular
            turn_timeout.
        silence_end_call_timeout:
          type:
            - number
            - 'null'
          format: double
          description: >-
            Maximum wait time since the user last spoke before terminating the
            call
        turn_eagerness:
          oneOf:
            - $ref: '#/components/schemas/TurnEagerness'
            - type: 'null'
          description: >-
            Controls how eager the agent is to respond. Low = less eager (waits
            longer), Standard = default eagerness, High = more eager (responds
            sooner)
        spelling_patience:
          oneOf:
            - $ref: '#/components/schemas/SpellingPatience'
            - type: 'null'
          description: >-
            Controls if the agent should be more patient when user is spelling
            numbers and named entities. Auto = model based, Off = never wait
            extra
        speculative_turn:
          type:
            - boolean
            - 'null'
          description: >-
            When enabled, starts generating LLM responses during silence before
            full turn confidence is reached, reducing perceived latency. May
            increase LLM costs.
        retranscribe_on_turn_timeout:
          type:
            - boolean
            - 'null'
          description: >-
            When enabled, if VAD detects no speech, attempts to re-transcribe
            accumulated audio at turn timeout. Disables silence discount billing
            for affected turns.
        turn_model:
          oneOf:
            - $ref: '#/components/schemas/TurnModel'
            - type: 'null'
          description: Version of the turn detection model to use.
        interruption_ignore_terms:
          type:
            - array
            - 'null'
          items:
            type: string
          description: >-
            List of terms that should not trigger an interruption when spoken by
            the user (e.g. 'gotcha', 'understood'). Uses case-insensitive exact
            matching.
        interruption_ignore_term_languages:
          type:
            - array
            - 'null'
          items:
            type: string
          description: >-
            Language codes for which preset ignore-term categories have been
            activated. Stored explicitly so display is not inferred from term
            overlap.
        transcribe_on_disabled_interruptions:
          type:
            - boolean
            - 'null'
          description: >-
            When interruptions are disabled, still transcribe what the user says
            so it can carry into the next turn. When off, user speech during a
            non-interruptible turn is ignored and won't trigger a turn.
        soft_timeout_config:
          oneOf:
            - $ref: '#/components/schemas/SoftTimeoutConfigWorkflowOverride'
            - type: 'null'
          description: >-
            Configuration for soft timeout functionality. Provides immediate
            feedback during longer LLM responses.
      title: TurnConfigWorkflowOverride
    TTSConversationalModel:
      type: string
      enum:
        - eleven_turbo_v2
        - eleven_turbo_v2_5
        - eleven_flash_v2
        - eleven_flash_v2_5
        - eleven_multilingual_v2
        - eleven_v3_conversational
      default: eleven_flash_v2
      title: TTSConversationalModel
    TTSModelFamily:
      type: string
      enum:
        - turbo
        - flash
        - multilingual
        - v3_conversational
      title: TTSModelFamily
    TTSOptimizeStreamingLatency:
      type: string
      enum:
        - '0'
        - '1'
        - '2'
        - '3'
        - '4'
      title: TTSOptimizeStreamingLatency
    SupportedVoice:
      type: object
      properties:
        label:
          type: string
        voice_id:
          type: string
        description:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        model_family:
          oneOf:
            - $ref: '#/components/schemas/TTSModelFamily'
            - type: 'null'
        optimize_streaming_latency:
          oneOf:
            - $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
            - type: 'null'
        stability:
          type:
            - number
            - 'null'
          format: double
        speed:
          type:
            - number
            - 'null'
          format: double
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
      required:
        - label
        - voice_id
      title: SupportedVoice
    SuggestedAudioTag:
      type: object
      properties:
        tag:
          type: string
          description: >-
            Audio tag to use (for best performance, 1-2 words, e.g., 'happy',
            'excited')
        description:
          type:
            - string
            - 'null'
          description: Optional description of when to use this tag
      required:
        - tag
      title: SuggestedAudioTag
    TTSOutputFormat:
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
      title: TTSOutputFormat
    TextNormalisationType:
      type: string
      enum:
        - system_prompt
        - elevenlabs
      default: system_prompt
      description: Method for converting numbers to words before sending to TTS
      title: TextNormalisationType
    PydanticPronunciationDictionaryVersionLocator:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
          description: The ID of the pronunciation dictionary
        version_id:
          type:
            - string
            - 'null'
          description: The ID of the version of the pronunciation dictionary
      required:
        - pronunciation_dictionary_id
        - version_id
      description: >-
        A locator for other documents to be able to reference a specific
        dictionary and it's version.

        This is a pydantic version of
        PronunciationDictionaryVersionLocatorDBModel.

        Required to ensure compat with the rest of the agent data models.
      title: PydanticPronunciationDictionaryVersionLocator
    TTSConversationalConfigWorkflowOverride-Input:
      type: object
      properties:
        model_id:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalModel'
            - type: 'null'
          description: The model to use for TTS
        voice_id:
          type:
            - string
            - 'null'
          description: The voice ID to use for TTS
        supported_voices:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SupportedVoice'
          description: Additional supported voices for the agent
        expressive_mode:
          type:
            - boolean
            - 'null'
          description: >-
            When enabled, applies expressive audio tags prompt. Automatically
            disabled for non-v3 models.
        suggested_audio_tags:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SuggestedAudioTag'
          description: >-
            Suggested audio tags to boost expressive speech (for eleven_v3 and
            eleven_v3_conversational models). The agent can still use other tags
            not listed here.
        agent_output_audio_format:
          oneOf:
            - $ref: '#/components/schemas/TTSOutputFormat'
            - type: 'null'
          description: The audio format to use for TTS
        optimize_streaming_latency:
          oneOf:
            - $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
            - type: 'null'
          description: 'Deprecated: this field is a no-op and is ignored.'
        stability:
          type:
            - number
            - 'null'
          format: double
          description: The stability of generated speech
        speed:
          type:
            - number
            - 'null'
          format: double
          description: The speed of generated speech
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
          description: The similarity boost for generated speech
        text_normalisation_type:
          oneOf:
            - $ref: '#/components/schemas/TextNormalisationType'
            - type: 'null'
          description: >-
            Method for converting numbers to words before converting text to
            speech. If set to SYSTEM_PROMPT, the system prompt will be updated
            to include normalization instructions. If set to ELEVENLABS, the
            text will be normalized after generation, incurring slight
            additional latency.
        pronunciation_dictionary_locators:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/PydanticPronunciationDictionaryVersionLocator'
          description: The pronunciation dictionary locators
        enable_phoneme_tags:
          type:
            - boolean
            - 'null'
          description: >-
            Opt-in to SSML phoneme tag handling for V3 models. When enabled,
            phoneme tags (inline and from pronunciation dictionaries) are parsed
            into inline IPA before being sent to the model.
      title: TTSConversationalConfigWorkflowOverride-Input
    ClientEvent:
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
    FileInputConfigWorkflowOverride:
      type: object
      properties:
        enabled:
          type:
            - boolean
            - 'null'
          description: >-
            When enabled, users may attach images or PDFs in chat when the LLM
            supports multimodal input.
        max_files_per_conversation:
          type:
            - integer
            - 'null'
          description: Maximum number of files that can be uploaded per conversation.
      title: FileInputConfigWorkflowOverride
    BackgroundSoundSourceType:
      type: string
      enum:
        - preset
      description: The type of background sound source.
      title: BackgroundSoundSourceType
    BackgroundSoundPresetId:
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
    BackgroundSoundConfigWorkflowOverride:
      type: object
      properties:
        source_type:
          oneOf:
            - $ref: '#/components/schemas/BackgroundSoundSourceType'
            - type: 'null'
          description: The type of background sound source.
        source_id:
          oneOf:
            - $ref: '#/components/schemas/BackgroundSoundPresetId'
            - type: 'null'
          description: Identifier for the sound source.
        volume:
          type:
            - number
            - 'null'
          format: double
          description: Volume level for background sound (0.01 to 1.0).
        crossfade_loop:
          type:
            - boolean
            - 'null'
          description: >-
            Apply a crossfade at the loop boundary to avoid audible pops when
            the sound loops.
      title: BackgroundSoundConfigWorkflowOverride
    ConversationConfigWorkflowOverride-Input:
      type: object
      properties:
        text_only:
          type:
            - boolean
            - 'null'
          description: >-
            If enabled audio will not be processed and only text will be used,
            use to avoid audio pricing.
        max_duration_seconds:
          type:
            - integer
            - 'null'
          description: The maximum duration of a conversation in seconds
        client_events:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ClientEvent'
          description: The events that will be sent to the client
        file_input:
          oneOf:
            - $ref: '#/components/schemas/FileInputConfigWorkflowOverride'
            - type: 'null'
          description: >-
            Configuration for file input (image/PDF uploads) during
            conversations.
        monitoring_enabled:
          type:
            - boolean
            - 'null'
          description: Enable real-time monitoring of conversations via WebSocket
        monitoring_events:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ClientEvent'
          description: The events that will be sent to monitoring connections.
        background_sound:
          oneOf:
            - $ref: '#/components/schemas/BackgroundSoundConfigWorkflowOverride'
            - type: 'null'
          description: Configuration for background sound during conversations.
        source_attribution:
          type:
            - boolean
            - 'null'
          description: >-
            When enabled and knowledge base content is present, the LLM is
            instructed to report which sources it used.
      title: ConversationConfigWorkflowOverride-Input
    ASRConversationalConfigOverride:
      type: object
      properties:
        keywords:
          type:
            - array
            - 'null'
          items:
            type: string
          description: Keywords to boost prediction probability for
      title: ASRConversationalConfigOverride
    SoftTimeoutConfigOverride:
      type: object
      properties:
        message:
          type:
            - string
            - 'null'
          description: >-
            Message to show when the first soft timeout is reached while waiting
            for LLM response. Supports dynamic variables (e.g.,
            {{system__time}}, {{custom_variable}}).
      title: SoftTimeoutConfigOverride
    TurnConfigOverride:
      type: object
      properties:
        soft_timeout_config:
          oneOf:
            - $ref: '#/components/schemas/SoftTimeoutConfigOverride'
            - type: 'null'
          description: >-
            Configuration for soft timeout functionality. Provides immediate
            feedback during longer LLM responses.
      title: TurnConfigOverride
    TTSConversationalConfigOverride:
      type: object
      properties:
        model_id:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalModel'
            - type: 'null'
          description: The model to use for TTS
        voice_id:
          type:
            - string
            - 'null'
          description: The voice ID to use for TTS
        stability:
          type:
            - number
            - 'null'
          format: double
          description: The stability of generated speech
        speed:
          type:
            - number
            - 'null'
          format: double
          description: The speed of generated speech
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
          description: The similarity boost for generated speech
      title: TTSConversationalConfigOverride
    ConversationConfigOverride:
      type: object
      properties:
        text_only:
          type:
            - boolean
            - 'null'
          description: >-
            If enabled audio will not be processed and only text will be used,
            use to avoid audio pricing.
      title: ConversationConfigOverride
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
      default: gemini-2.5-flash
      title: LLM
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
    PromptAgentAPIModelOverride-Input:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
          description: The prompt for the agent
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
          description: >-
            The LLM to query with the prompt and the chat history. If using data
            residency, the LLM must be supported in the data residency
            environment
        tool_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of IDs of tools used by the agent
        native_mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of Native MCP server ids to be used by the agent
        knowledge_base:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/KnowledgeBaseLocator'
          description: A list of knowledge bases to be used by the agent
      title: PromptAgentAPIModelOverride-Input
    AgentConfigOverride-Input:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
          description: >-
            If non-empty, the first message the agent will say. If empty, the
            agent waits for the user to start the discussion.
        language:
          type:
            - string
            - 'null'
          description: Language of the agent - used for ASR and TTS
        max_conversation_duration_message:
          type:
            - string
            - 'null'
          description: >-
            If non-empty, the message the agent will send when max conversation
            duration is reached.
        prompt:
          oneOf:
            - $ref: '#/components/schemas/PromptAgentAPIModelOverride-Input'
            - type: 'null'
          description: The prompt for the agent
      title: AgentConfigOverride-Input
    ConversationConfigClientOverride-Input:
      type: object
      properties:
        asr:
          oneOf:
            - $ref: '#/components/schemas/ASRConversationalConfigOverride'
            - type: 'null'
          description: Configuration for conversational transcription
        turn:
          oneOf:
            - $ref: '#/components/schemas/TurnConfigOverride'
            - type: 'null'
          description: Configuration for turn detection
        tts:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalConfigOverride'
            - type: 'null'
          description: Configuration for conversational text to speech
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfigOverride'
            - type: 'null'
          description: Configuration for conversational events
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigOverride-Input'
            - type: 'null'
          description: Agent specific configuration
      title: ConversationConfigClientOverride-Input
    LanguagePresetTranslation:
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
    LanguagePreset-Input:
      type: object
      properties:
        overrides:
          $ref: '#/components/schemas/ConversationConfigClientOverride-Input'
          description: The overrides for the language preset
        first_message_translation:
          oneOf:
            - $ref: '#/components/schemas/LanguagePresetTranslation'
            - type: 'null'
          description: The translation of the first message
        soft_timeout_translation:
          oneOf:
            - $ref: '#/components/schemas/LanguagePresetTranslation'
            - type: 'null'
          description: The translation of the soft timeout message
      required:
        - overrides
      title: LanguagePreset-Input
    VADConfigWorkflowOverride:
      type: object
      properties: {}
      title: VADConfigWorkflowOverride
    DynamicVariablesConfigWorkflowOverride:
      type: object
      properties:
        dynamic_variable_placeholders:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
          description: A dictionary of dynamic variable placeholders and their values
      title: DynamicVariablesConfigWorkflowOverride
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
    LLMReasoningEffort:
      type: string
      enum:
        - none
        - minimal
        - low
        - medium
        - high
        - xhigh
        - max
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
    ObjectJsonSchemaPropertyInputPropertyKind:
      type: string
      enum:
        - array
        - object
      default: object
      title: ObjectJsonSchemaPropertyInputPropertyKind
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
    ArrayJsonSchemaPropertyInputPropertyKind:
      type: string
      enum:
        - array
        - object
      default: array
      title: ArrayJsonSchemaPropertyInputPropertyKind
    ArrayJsonSchemaPropertyInputItems:
      oneOf:
        - $ref: '#/components/schemas/LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/ObjectJsonSchemaProperty-Input'
        - $ref: '#/components/schemas/ArrayJsonSchemaProperty-Input'
      description: Schema for array elements.
      title: ArrayJsonSchemaPropertyInputItems
    ArrayJsonSchemaProperty-Input:
      type: object
      properties:
        property_kind:
          $ref: '#/components/schemas/ArrayJsonSchemaPropertyInputPropertyKind'
          default: array
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
          type:
            - array
            - 'null'
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
          default: array
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
        property_kind:
          $ref: '#/components/schemas/ObjectJsonSchemaPropertyInputPropertyKind'
          default: object
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
          type:
            - object
            - 'null'
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
          default: object
        required:
          type: array
          items:
            type: string
        properties:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ObjectJsonSchemaPropertyInput'
        required_constraints:
          oneOf:
            - $ref: '#/components/schemas/RequiredConstraints'
            - type: 'null'
      title: ObjectJsonSchemaProperty-Input
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
    BuiltInToolsWorkflowOverride-Input:
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
      title: BuiltInToolsWorkflowOverride-Input
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
    RagConfigWorkflowOverride:
      type: object
      properties:
        enabled:
          type:
            - boolean
            - 'null'
        embedding_model:
          oneOf:
            - $ref: '#/components/schemas/EmbeddingModelEnum'
            - type: 'null'
        max_vector_distance:
          type:
            - number
            - 'null'
          format: double
          description: Maximum vector distance of retrieved chunks.
        max_documents_length:
          type:
            - integer
            - 'null'
          description: Maximum total length of document chunks retrieved from RAG.
        max_retrieved_rag_chunks_count:
          type:
            - integer
            - 'null'
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
      title: RagConfigWorkflowOverride
    BackupLLMDefault:
      type: object
      properties: {}
      title: BackupLLMDefault
    BackupLLMDisabled:
      type: object
      properties: {}
      title: BackupLLMDisabled
    BackupLLMOverride:
      type: object
      properties:
        order:
          type: array
          items:
            $ref: '#/components/schemas/LLM'
      required:
        - order
      title: BackupLLMOverride
    PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig:
      oneOf:
        - $ref: '#/components/schemas/BackupLLMDefault'
        - $ref: '#/components/schemas/BackupLLMDisabled'
        - $ref: '#/components/schemas/BackupLLMOverride'
      description: >-
        Configuration for backup LLM cascading. Can be disabled, use system
        defaults, or specify custom order.
      title: PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig
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
    PromptAgentApiModelWorkflowOverrideInputToolsItems:
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
      title: PromptAgentApiModelWorkflowOverrideInputToolsItems
    PromptAgentAPIModelWorkflowOverride-Input:
      type: object
      properties:
        prompt:
          type:
            - string
            - 'null'
          description: The prompt for the agent
        llm:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
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
          type:
            - boolean
            - 'null'
          description: >-
            Enable model reasoning summaries. When disabled, we do not request
            summaries from provider if possible for faster TTFB. Not ZRM
            compatible.
        temperature:
          type:
            - number
            - 'null'
          format: double
          description: >-
            The temperature for the LLM. Defaults to 0. Set to null to omit the
            parameter from the LLM request entirely (useful for custom LLMs that
            reject the temperature field).
        max_tokens:
          type:
            - integer
            - 'null'
          description: If greater than 0, maximum number of tokens the LLM can predict
        tool_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of IDs of tools used by the agent
        built_in_tools:
          oneOf:
            - $ref: '#/components/schemas/BuiltInToolsWorkflowOverride-Input'
            - type: 'null'
          description: Built-in system tools to be used by the agent
        mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of MCP server ids to be used by the agent
        native_mcp_server_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of Native MCP server ids to be used by the agent
        knowledge_base:
          type:
            - array
            - 'null'
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
          description: >-
            Whether to remove the default personality lines from the system
            prompt
        rag:
          oneOf:
            - $ref: '#/components/schemas/RagConfigWorkflowOverride'
            - type: 'null'
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
          oneOf:
            - $ref: >-
                #/components/schemas/PromptAgentApiModelWorkflowOverrideInputBackupLlmConfig
            - type: 'null'
          description: >-
            Configuration for backup LLM cascading. Can be disabled, use system
            defaults, or specify custom order.
        cascade_timeout_seconds:
          type:
            - number
            - 'null'
          format: double
          description: >-
            Time in seconds before cascading to backup LLM. Must be between 2
            and 15 seconds.
        tools:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/PromptAgentApiModelWorkflowOverrideInputToolsItems
          description: >-
            A list of tools that the agent can use over the course of the
            conversation, use tool_ids instead
      title: PromptAgentAPIModelWorkflowOverride-Input
    AgentConfigAPIModelWorkflowOverride-Input:
      type: object
      properties:
        first_message:
          type:
            - string
            - 'null'
          description: >-
            If non-empty, the first message the agent will say. If empty, the
            agent waits for the user to start the discussion.
        language:
          type:
            - string
            - 'null'
          description: Language of the agent - used for ASR and TTS
        hinglish_mode:
          type:
            - boolean
            - 'null'
          description: >-
            When enabled and language is Hindi, the agent will respond in
            Hinglish
        dynamic_variables:
          oneOf:
            - $ref: '#/components/schemas/DynamicVariablesConfigWorkflowOverride'
            - type: 'null'
          description: Configuration for dynamic variables
        disable_first_message_interruptions:
          type:
            - boolean
            - 'null'
          description: >-
            If true, the user will not be able to interrupt the agent while the
            first message is being delivered.
        max_conversation_duration_message:
          type:
            - string
            - 'null'
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
          oneOf:
            - $ref: '#/components/schemas/PromptAgentAPIModelWorkflowOverride-Input'
            - type: 'null'
          description: The prompt for the agent
      title: AgentConfigAPIModelWorkflowOverride-Input
    ConversationalConfigAPIModelWorkflowOverride-Input:
      type: object
      properties:
        asr:
          oneOf:
            - $ref: '#/components/schemas/ASRConversationalConfigWorkflowOverride'
            - type: 'null'
          description: Configuration for conversational transcription
        turn:
          oneOf:
            - $ref: '#/components/schemas/TurnConfigWorkflowOverride'
            - type: 'null'
          description: Configuration for turn detection
        tts:
          oneOf:
            - $ref: >-
                #/components/schemas/TTSConversationalConfigWorkflowOverride-Input
            - type: 'null'
          description: Configuration for conversational text to speech
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfigWorkflowOverride-Input'
            - type: 'null'
          description: Configuration for conversational events
        language_presets:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/LanguagePreset-Input'
          description: Language presets for conversations
        vad:
          oneOf:
            - $ref: '#/components/schemas/VADConfigWorkflowOverride'
            - type: 'null'
          description: Configuration for voice activity detection
        agent:
          oneOf:
            - $ref: '#/components/schemas/AgentConfigAPIModelWorkflowOverride-Input'
            - type: 'null'
          description: Agent specific configuration
      title: ConversationalConfigAPIModelWorkflowOverride-Input
    EntryBehavior:
      type: string
      enum:
        - generate_immediately
        - wait_for_user
        - auto
      default: auto
      title: EntryBehavior
    WorkflowPhoneNumberNodeModelInputCustomSipHeadersItems:
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
      title: WorkflowPhoneNumberNodeModelInputCustomSipHeadersItems
    WorkflowPhoneNumberNodeModelInputTransferDestination:
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
      title: WorkflowPhoneNumberNodeModelInputTransferDestination
    WorkflowPhoneNumberNodeModelInputPostDialDigits:
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
      title: WorkflowPhoneNumberNodeModelInputPostDialDigits
    WorkflowToolLocator:
      type: object
      properties:
        tool_id:
          type: string
      required:
        - tool_id
      title: WorkflowToolLocator
    AgentWorkflowRequestModelNodes:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - end
              default: end
            position:
              $ref: '#/components/schemas/Position-Input'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
          description: WorkflowEndNodeModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - override_agent
              default: override_agent
            position:
              $ref: '#/components/schemas/Position-Input'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
            conversation_config:
              $ref: >-
                #/components/schemas/ConversationalConfigAPIModelWorkflowOverride-Input
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
                $ref: '#/components/schemas/KnowledgeBaseLocator'
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
              $ref: '#/components/schemas/EntryBehavior'
              default: auto
              description: >-
                Dictates whether this node should immediately generate a
                response upon entry or wait for the user input. When set to
                "auto", the behavior will be decided based on the type of the
                preceding node: "wait_for_user" after the "say" and "start"
                nodes and "generate_immediately" otherwise.
          required:
            - type
            - label
          description: WorkflowOverrideAgentNodeModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - phone_number
              default: phone_number
            custom_sip_headers:
              type: array
              items:
                $ref: >-
                  #/components/schemas/WorkflowPhoneNumberNodeModelInputCustomSipHeadersItems
              description: >-
                Custom SIP headers to include when transferring the call. Each
                header can be either a static value or a dynamic variable
                reference.
            transfer_destination:
              $ref: >-
                #/components/schemas/WorkflowPhoneNumberNodeModelInputTransferDestination
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
                - $ref: >-
                    #/components/schemas/WorkflowPhoneNumberNodeModelInputPostDialDigits
                - type: 'null'
              description: >-
                DTMF digits to send after call connects (e.g., 'ww1234' for
                extension). Can be either a static value or a dynamic variable
                reference. Use 'w' for 0.5s pause. Only supported for Twilio
                transfers.
            position:
              $ref: '#/components/schemas/Position-Input'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
            - transfer_destination
          description: WorkflowPhoneNumberNodeModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - standalone_agent
              default: standalone_agent
            position:
              $ref: '#/components/schemas/Position-Input'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
            agent_id:
              type:
                - string
                - 'null'
              description: >-
                The ID of the agent to transfer the conversation to. None means
                transfer within the current agent.
            node_id:
              type:
                - string
                - 'null'
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
              type:
                - string
                - 'null'
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
          description: WorkflowStandaloneAgentNodeModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - start
              default: start
            position:
              $ref: '#/components/schemas/Position-Input'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
          description: WorkflowStartNodeModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - tool
              default: tool
            position:
              $ref: '#/components/schemas/Position-Input'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
            tools:
              type: array
              items:
                $ref: '#/components/schemas/WorkflowToolLocator'
              description: >-
                List of tools to execute in parallel. The entire node is
                considered successful if all tools are executed successfully.
          required:
            - type
          description: WorkflowToolNodeModel variant
      discriminator:
        propertyName: type
      title: AgentWorkflowRequestModelNodes
    AgentWorkflowRequestModel:
      type: object
      properties:
        edges:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/WorkflowEdgeModel-Input'
        nodes:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/AgentWorkflowRequestModelNodes'
        prevent_subagent_loops:
          type: boolean
          default: false
          description: Whether to prevent loops in the workflow execution.
      title: AgentWorkflowRequestModel
    Body_Create_a_new_branch_v1_convai_agents__agent_id__branches_post:
      type: object
      properties:
        parent_version_id:
          type: string
          description: ID of the version to branch from
        name:
          type: string
          description: Name of the branch. It is unique within the agent.
        description:
          type: string
          description: Description for the branch
        conversation_config:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
          description: Changes to apply to conversation config
        platform_settings:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
          description: Changes to apply to platform settings
        workflow:
          oneOf:
            - $ref: '#/components/schemas/AgentWorkflowRequestModel'
            - type: 'null'
          description: Updated workflow definition
      required:
        - parent_version_id
        - name
        - description
      title: Body_Create_a_new_branch_v1_convai_agents__agent_id__branches_post
    CreateAgentBranchResponseModel:
      type: object
      properties:
        created_branch_id:
          type: string
          description: ID of the created branch
        created_version_id:
          type: string
          description: ID of the first version on the created branch
      required:
        - created_branch_id
        - created_version_id
      title: CreateAgentBranchResponseModel
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
  "parent_version_id": "string",
  "name": "string",
  "description": "string"
}
```

**Response**

```json
{
  "created_branch_id": "string",
  "created_version_id": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.create("agent_id", {
        parentVersionId: "string",
        name: "string",
        description: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.create(
    agent_id="agent_id",
    parent_version_id="string",
    name="string",
    description="string",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches"

	payload := strings.NewReader("{\n  \"parent_version_id\": \"string\",\n  \"name\": \"string\",\n  \"description\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"parent_version_id\": \"string\",\n  \"name\": \"string\",\n  \"description\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches")
  .header("Content-Type", "application/json")
  .body("{\n  \"parent_version_id\": \"string\",\n  \"name\": \"string\",\n  \"description\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/branches', [
  'body' => '{
  "parent_version_id": "string",
  "name": "string",
  "description": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"parent_version_id\": \"string\",\n  \"name\": \"string\",\n  \"description\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "parent_version_id": "string",
  "name": "string",
  "description": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches")! as URL,
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
