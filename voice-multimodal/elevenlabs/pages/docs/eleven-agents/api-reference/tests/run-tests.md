---
title: "Run tests on agent"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/run-tests.md
path: docs/eleven-agents/api-reference/tests/run-tests
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Run tests on agent

POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/run-tests
Content-Type: application/json

Run selected tests on the agent with provided configuration. If the agent configuration is provided, it will be used to override default agent configuration.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/run-tests

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/run-tests:
    post:
      operationId: run_tests
      summary: Run Tests On The Agent
      description: >-
        Run selected tests on the agent with provided configuration. If the
        agent configuration is provided, it will be used to override default
        agent configuration.
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
                $ref: '#/components/schemas/type_:GetTestSuiteInvocationResponseModel'
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
                tests:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_:SingleTestRunRequestModel'
                  description: List of tests to run on the agent
                agent_config_override:
                  $ref: >-
                    #/components/schemas/type_:AdhocAgentConfigOverrideForTestRequestModel
                  description: >-
                    Configuration overrides to use for testing. If not provided,
                    the agent's default configuration will be used.
                branch_id:
                  type: string
                  description: >-
                    ID of the branch to run the tests on. If not provided, the
                    tests will be run on the agent default configuration.
                repeat_count:
                  type: integer
                  default: 1
                  description: >-
                    Number of times to run each test. When greater than 1,
                    results are grouped and summarized.
              required:
                - tests
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
    type_:SingleTestRunRequestModel:
      type: object
      properties:
        test_id:
          type: string
          description: ID of the test to run
        workflow_node_id:
          type: string
          description: >-
            ID of the workflow node to run the test on. If not provided, the
            test will be run on the agent's default workflow node.
        root_folder_id:
          type: string
          description: >-
            ID of the root folder to run the test on. If not provided, the test
            will be run on the agent's default folder.
        root_folder_name:
          type: string
          description: >-
            Name of the root folder to run the test on. If not provided, the
            test will be run on the agent's default folder.
      required:
        - test_id
      title: SingleTestRunRequestModel
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
    type_:AsrConversationalConfig:
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
      title: AsrConversationalConfig
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
    type_:SoftTimeoutConfig:
      type: object
      properties:
        timeout_seconds:
          type: number
          format: double
          default: -1
          description: >-
            Time in seconds before showing the predefined message while waiting
            for LLM response. Set to -1 to disable.
        message:
          type: string
          default: Hhmmmm...yeah.
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
          default: false
          description: >-
            If enabled, the soft timeout message will be generated dynamically
            instead of using the static message.
        randomize_fillers:
          type: boolean
          default: false
          description: >-
            If enabled, shuffle the order of static soft timeout messages once
            at the start of each turn. Only applies when
            use_llm_generated_message is false.
        max_soft_timeouts_per_generation:
          type: integer
          default: 1
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
      description: >-
        Configuration for soft timeout functionality during LLM response
        generation.
      title: SoftTimeoutConfig
    type_:TurnConfig:
      type: object
      properties:
        turn_timeout:
          type: number
          format: double
          default: 7
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
          default: -1
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
          default: false
          description: >-
            When enabled, starts generating LLM responses during silence before
            full turn confidence is reached, reducing perceived latency. May
            increase LLM costs.
        retranscribe_on_turn_timeout:
          type: boolean
          default: false
          description: >-
            When enabled, if VAD detects no speech, attempts to re-transcribe
            accumulated audio at turn timeout. Disables silence discount billing
            for affected turns.
        turn_model:
          $ref: '#/components/schemas/type_:TurnModel'
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
          default: false
          description: >-
            When interruptions are disabled, still transcribe what the user says
            so it can carry into the next turn. When off, user speech during a
            non-interruptible turn is ignored and won't trigger a turn.
        soft_timeout_config:
          $ref: '#/components/schemas/type_:SoftTimeoutConfig'
          description: >-
            Configuration for soft timeout functionality. Provides immediate
            feedback during longer LLM responses.
      title: TurnConfig
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
    type_:TtsConversationalConfigOutput:
      type: object
      properties:
        model_id:
          $ref: '#/components/schemas/type_:TtsConversationalModel'
          description: The model to use for TTS
        voice_id:
          type: string
          default: cjVigY5qzO86Huf0OWal
          description: The voice ID to use for TTS
        supported_voices:
          type: array
          items:
            $ref: '#/components/schemas/type_:SupportedVoice'
          description: Additional supported voices for the agent
        expressive_mode:
          type: boolean
          default: true
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
          default: 0.5
          description: The stability of generated speech
        speed:
          type: number
          format: double
          default: 1
          description: The speed of generated speech
        similarity_boost:
          type: number
          format: double
          default: 0.8
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
          default: false
          description: >-
            Opt-in to SSML phoneme tag handling for V3 models. When enabled,
            phoneme tags (inline and from pronunciation dictionaries) are parsed
            into inline IPA before being sent to the model.
      title: TtsConversationalConfigOutput
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
    type_:FileInputConfig:
      type: object
      properties:
        enabled:
          type: boolean
          default: true
          description: >-
            When enabled, users may attach images or PDFs in chat when the LLM
            supports multimodal input.
        max_files_per_conversation:
          type: integer
          default: 10
          description: Maximum number of files that can be uploaded per conversation.
      title: FileInputConfig
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
    type_:BackgroundSoundConfig:
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
          default: 0.6
          description: Volume level for background sound (0.01 to 1.0).
        crossfade_loop:
          type: boolean
          default: false
          description: >-
            Apply a crossfade at the loop boundary to avoid audible pops when
            the sound loops.
      title: BackgroundSoundConfig
    type_:ConversationConfigOutput:
      type: object
      properties:
        text_only:
          type: boolean
          default: false
          description: >-
            If enabled audio will not be processed and only text will be used,
            use to avoid audio pricing.
        max_duration_seconds:
          type: integer
          default: 600
          description: The maximum duration of a conversation in seconds
        client_events:
          type: array
          items:
            $ref: '#/components/schemas/type_:ClientEvent'
          description: The events that will be sent to the client
        file_input:
          $ref: '#/components/schemas/type_:FileInputConfig'
          description: >-
            Configuration for file input (image/PDF uploads) during
            conversations.
        monitoring_enabled:
          type: boolean
          default: false
          description: Enable real-time monitoring of conversations via WebSocket
        monitoring_events:
          type: array
          items:
            $ref: '#/components/schemas/type_:ClientEvent'
          description: The events that will be sent to monitoring connections.
        background_sound:
          $ref: '#/components/schemas/type_:BackgroundSoundConfig'
          description: Configuration for background sound during conversations.
        source_attribution:
          type: boolean
          default: false
          description: >-
            When enabled and knowledge base content is present, the LLM is
            instructed to report which sources it used.
      title: ConversationConfigOutput
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
    type_:PromptAgentApiModelOverrideOutput:
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
      title: PromptAgentApiModelOverrideOutput
    type_:AgentConfigOverrideOutput:
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
          $ref: '#/components/schemas/type_:PromptAgentApiModelOverrideOutput'
          description: The prompt for the agent
      title: AgentConfigOverrideOutput
    type_:ConversationConfigClientOverrideOutput:
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
          $ref: '#/components/schemas/type_:AgentConfigOverrideOutput'
          description: Agent specific configuration
      title: ConversationConfigClientOverrideOutput
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
    type_:LanguagePresetOutput:
      type: object
      properties:
        overrides:
          $ref: '#/components/schemas/type_:ConversationConfigClientOverrideOutput'
          description: The overrides for the language preset
        first_message_translation:
          $ref: '#/components/schemas/type_:LanguagePresetTranslation'
          description: The translation of the first message
        soft_timeout_translation:
          $ref: '#/components/schemas/type_:LanguagePresetTranslation'
          description: The translation of the soft timeout message
      required:
        - overrides
      title: LanguagePresetOutput
    type_:VadConfig:
      type: object
      properties: {}
      title: VadConfig
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
    type_:RagConfig:
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
      title: RagConfig
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
    type_:ArrayJsonSchemaPropertyOutputItems:
      oneOf:
        - $ref: '#/components/schemas/type_:LiteralJsonSchemaProperty'
        - $ref: '#/components/schemas/type_:ObjectJsonSchemaPropertyOutput'
        - $ref: '#/components/schemas/type_:ArrayJsonSchemaPropertyOutput'
      description: Schema for array elements.
      title: ArrayJsonSchemaPropertyOutputItems
    type_:ArrayJsonSchemaPropertyOutputConstantValueItem:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
      title: ArrayJsonSchemaPropertyOutputConstantValueItem
    type_:ArrayJsonSchemaPropertyOutput:
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
          $ref: '#/components/schemas/type_:ArrayJsonSchemaPropertyOutputItems'
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
              #/components/schemas/type_:ArrayJsonSchemaPropertyOutputConstantValueItem
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
              #/components/schemas/type_:ObjectJsonSchemaPropertyOutputPropertiesValue
        required_constraints:
          $ref: '#/components/schemas/type_:RequiredConstraints'
      title: ObjectJsonSchemaPropertyOutput
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
          $ref: '#/components/schemas/type_:RagConfig'
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
          default: 8
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
    type_:ConversationalConfig:
      type: object
      properties:
        asr:
          $ref: '#/components/schemas/type_:AsrConversationalConfig'
          description: Configuration for conversational transcription
        turn:
          $ref: '#/components/schemas/type_:TurnConfig'
          description: Configuration for turn detection
        tts:
          $ref: '#/components/schemas/type_:TtsConversationalConfigOutput'
          description: Configuration for conversational text to speech
        conversation:
          $ref: '#/components/schemas/type_:ConversationConfigOutput'
          description: Configuration for conversational events
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:LanguagePresetOutput'
          description: Language presets for conversations
        vad:
          $ref: '#/components/schemas/type_:VadConfig'
          description: Configuration for voice activity detection
        agent:
          $ref: '#/components/schemas/type_:AgentConfig'
          description: Agent specific configuration
      title: ConversationalConfig
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
    type_:EvaluationSettingsInput:
      type: object
      properties:
        criteria:
          type: array
          items:
            $ref: '#/components/schemas/type_:PromptEvaluationCriteria'
          description: Individual criteria that the agent should be evaluated against
      description: >-
        Settings to evaluate an agent's performance.

        Agents are evaluated against a set of criteria, with success being
        defined as meeting some combination of those criteria.
      title: EvaluationSettingsInput
    type_:EmbedVariant:
      type: string
      enum:
        - tiny
        - compact
        - full
        - expandable
      default: full
      title: EmbedVariant
    type_:WidgetPlacement:
      type: string
      enum:
        - top-left
        - top
        - top-right
        - bottom-left
        - bottom
        - bottom-right
      default: bottom-right
      title: WidgetPlacement
    type_:WidgetExpandable:
      type: string
      enum:
        - never
        - mobile
        - desktop
        - always
      default: never
      title: WidgetExpandable
    type_:WidgetConfigAvatar:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - orb
              description: 'Discriminator value: orb'
            color_1:
              type: string
              default: '#2792dc'
              description: The first color of the avatar
            color_2:
              type: string
              default: '#9ce6e6'
              description: The second color of the avatar
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - url
              description: 'Discriminator value: url'
            custom_url:
              type: string
              default: ''
              description: The custom URL of the avatar
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - image
              description: 'Discriminator value: image'
            url:
              type: string
              default: ''
              description: The URL of the avatar
          required:
            - type
      discriminator:
        propertyName: type
      description: The avatar of the widget
      title: WidgetConfigAvatar
    type_:WidgetFeedbackMode:
      type: string
      enum:
        - none
        - during
        - end
      default: none
      title: WidgetFeedbackMode
    type_:WidgetEndFeedbackType:
      type: string
      enum:
        - rating
      title: WidgetEndFeedbackType
    type_:WidgetEndFeedbackConfig:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:WidgetEndFeedbackType'
          description: The type of feedback to collect at the end of the conversation
      title: WidgetEndFeedbackConfig
    type_:AllowlistItem:
      type: object
      properties:
        hostname:
          type: string
          description: The hostname of the allowed origin
      required:
        - hostname
      title: AllowlistItem
    type_:WidgetConfigSyntaxHighlightTheme:
      type: string
      enum:
        - light
        - dark
      title: WidgetConfigSyntaxHighlightTheme
    type_:WidgetTextContents:
      type: object
      properties:
        main_label:
          type: string
          description: Call to action displayed inside the compact and full variants.
        start_call:
          type: string
          description: Text and ARIA label for the start call button.
        start_chat:
          type: string
          description: Text and ARIA label for the start chat button (text only)
        new_call:
          type: string
          description: >-
            Text and ARIA label for the new call button. Displayed when the
            caller already finished at least one call in order ot start the next
            one.
        end_call:
          type: string
          description: Text and ARIA label for the end call button.
        mute_microphone:
          type: string
          description: ARIA label for the mute microphone button.
        change_language:
          type: string
          description: ARIA label for the change language dropdown.
        collapse:
          type: string
          description: ARIA label for the collapse button.
        expand:
          type: string
          description: ARIA label for the expand button.
        copied:
          type: string
          description: Text displayed when the user copies a value using the copy button.
        accept_terms:
          type: string
          description: Text and ARIA label for the accept terms button.
        dismiss_terms:
          type: string
          description: Text and ARIA label for the cancel terms button.
        listening_status:
          type: string
          description: Status displayed when the agent is listening.
        speaking_status:
          type: string
          description: Status displayed when the agent is speaking.
        connecting_status:
          type: string
          description: Status displayed when the agent is connecting.
        chatting_status:
          type: string
          description: Status displayed when the agent is chatting (text only)
        input_label:
          type: string
          description: ARIA label for the text message input.
        input_placeholder:
          type: string
          description: Placeholder text for the text message input.
        input_placeholder_text_only:
          type: string
          description: Placeholder text for the text message input (text only)
        input_placeholder_new_conversation:
          type: string
          description: >-
            Placeholder text for the text message input when starting a new
            conversation (text only)
        user_ended_conversation:
          type: string
          description: Information message displayed when the user ends the conversation.
        agent_ended_conversation:
          type: string
          description: Information message displayed when the agent ends the conversation.
        conversation_id:
          type: string
          description: Text label used next to the conversation ID.
        error_occurred:
          type: string
          description: Text label used when an error occurs.
        copy_id:
          type: string
          description: Text and ARIA label used for the copy ID button.
        initiate_feedback:
          type: string
          description: Text displayed to prompt the user for feedback.
        request_follow_up_feedback:
          type: string
          description: Text displayed to request additional feedback details.
        thanks_for_feedback:
          type: string
          description: Text displayed to thank the user for providing feedback.
        thanks_for_feedback_details:
          type: string
          description: Additional text displayed explaining the value of user feedback.
        follow_up_feedback_placeholder:
          type: string
          description: Placeholder text for the follow-up feedback input field.
        submit:
          type: string
          description: Text and ARIA label for the submit button.
        go_back:
          type: string
          description: Text and ARIA label for the go back button.
        send_message:
          type: string
          description: Text and ARIA label for the send message button.
        text_mode:
          type: string
          description: Text and ARIA label for the switch to text mode button.
        voice_mode:
          type: string
          description: Text and ARIA label for the switch to voice mode button.
        switched_to_text_mode:
          type: string
          description: Toast notification displayed when switching to text mode.
        switched_to_voice_mode:
          type: string
          description: Toast notification displayed when switching to voice mode.
        copy:
          type: string
          description: Text and ARIA label for the copy button.
        download:
          type: string
          description: Text and ARIA label for the download button.
        wrap:
          type: string
          description: Text and ARIA label for the wrap toggle button.
        agent_working:
          type: string
          description: Status text displayed when the agent is processing a tool call.
        agent_done:
          type: string
          description: >-
            Status text displayed when the agent finishes processing a tool
            call.
        agent_error:
          type: string
          description: >-
            Status text displayed when the agent encounters an error during a
            tool call.
      title: WidgetTextContents
    type_:WidgetStyles:
      type: object
      properties:
        base:
          type: string
          description: The base background color.
        base_hover:
          type: string
          description: The color of the base background when hovered.
        base_active:
          type: string
          description: The color of the base background when active (clicked).
        base_border:
          type: string
          description: The color of the border against the base background.
        base_subtle:
          type: string
          description: The color of subtle text against the base background.
        base_primary:
          type: string
          description: The color of primary text against the base background.
        base_error:
          type: string
          description: The color of error text against the base background.
        accent:
          type: string
          description: The accent background color.
        accent_hover:
          type: string
          description: The color of the accent background when hovered.
        accent_active:
          type: string
          description: The color of the accent background when active (clicked).
        accent_border:
          type: string
          description: The color of the border against the accent background.
        accent_subtle:
          type: string
          description: The color of subtle text against the accent background.
        accent_primary:
          type: string
          description: The color of primary text against the accent background.
        overlay_padding:
          type: number
          format: double
          description: The padding around the edges of the viewport.
        button_radius:
          type: number
          format: double
          description: The radius of the buttons.
        input_radius:
          type: number
          format: double
          description: The radius of the input fields.
        bubble_radius:
          type: number
          format: double
          description: The radius of the chat bubbles.
        sheet_radius:
          type: number
          format: double
          description: The default radius of sheets.
        compact_sheet_radius:
          type: number
          format: double
          description: The radius of the sheet in compact mode.
        dropdown_sheet_radius:
          type: number
          format: double
          description: The radius of the dropdown sheet.
      title: WidgetStyles
    type_:WidgetTermsTranslation:
      type: object
      properties:
        source_hash:
          type: string
        text:
          type: string
      required:
        - source_hash
        - text
      title: WidgetTermsTranslation
    type_:WidgetLanguagePreset:
      type: object
      properties:
        text_contents:
          $ref: '#/components/schemas/type_:WidgetTextContents'
          description: The text contents for the selected language
        terms_text:
          type: string
          description: The text to display for terms and conditions in this language
        terms_html:
          type: string
          description: The HTML to display for terms and conditions in this language
        terms_key:
          type: string
          description: The key to display for terms and conditions in this language
        terms_translation:
          $ref: '#/components/schemas/type_:WidgetTermsTranslation'
          description: The translation cache for the terms
      title: WidgetLanguagePreset
    type_:WidgetConfig:
      type: object
      properties:
        variant:
          $ref: '#/components/schemas/type_:EmbedVariant'
          description: The variant of the widget
        placement:
          $ref: '#/components/schemas/type_:WidgetPlacement'
          description: The placement of the widget on the screen
        expandable:
          $ref: '#/components/schemas/type_:WidgetExpandable'
          description: Whether the widget is expandable
        avatar:
          $ref: '#/components/schemas/type_:WidgetConfigAvatar'
          description: The avatar of the widget
        feedback_mode:
          $ref: '#/components/schemas/type_:WidgetFeedbackMode'
          description: The feedback mode of the widget
        end_feedback:
          $ref: '#/components/schemas/type_:WidgetEndFeedbackConfig'
          description: Configuration for feedback collected at the end of the conversation
        bg_color:
          type: string
          default: '#ffffff'
          description: The background color of the widget
        text_color:
          type: string
          default: '#000000'
          description: The text color of the widget
        btn_color:
          type: string
          default: '#000000'
          description: The button color of the widget
        btn_text_color:
          type: string
          default: '#ffffff'
          description: The button text color of the widget
        border_color:
          type: string
          default: '#e1e1e1'
          description: The border color of the widget
        focus_color:
          type: string
          default: '#000000'
          description: The focus color of the widget
        border_radius:
          type: integer
          description: The border radius of the widget
        btn_radius:
          type: integer
          description: The button radius of the widget
        action_text:
          type: string
          description: The action text of the widget
        start_call_text:
          type: string
          description: The start call text of the widget
        end_call_text:
          type: string
          description: The end call text of the widget
        expand_text:
          type: string
          description: The expand text of the widget
        listening_text:
          type: string
          description: The text to display when the agent is listening
        speaking_text:
          type: string
          description: The text to display when the agent is speaking
        shareable_page_text:
          type: string
          description: The text to display when sharing
        shareable_page_show_terms:
          type: boolean
          default: true
          description: Whether to show terms and conditions on the shareable page
        terms_text:
          type: string
          description: The text to display for terms and conditions
        terms_html:
          type: string
          description: The HTML to display for terms and conditions
        terms_key:
          type: string
          description: The key to display for terms and conditions
        show_avatar_when_collapsed:
          type: boolean
          description: Whether to show the avatar when the widget is collapsed
        disable_banner:
          type: boolean
          default: false
          description: Whether to disable the banner
        override_link:
          type: string
          description: The override link for the widget
        markdown_link_allowed_hosts:
          type: array
          items:
            $ref: '#/components/schemas/type_:AllowlistItem'
          description: >-
            List of allowed hostnames for clickable markdown links. Use {
            hostname: '*' } to allow any domain. Empty means no links are
            allowed.
        markdown_link_include_www:
          type: boolean
          default: true
          description: Whether to automatically include www. variants of allowed hosts
        markdown_link_allow_http:
          type: boolean
          default: true
          description: Whether to allow http:// in addition to https:// for allowed hosts
        mic_muting_enabled:
          type: boolean
          default: false
          description: Whether to enable mic muting
        transcript_enabled:
          type: boolean
          default: false
          description: >-
            Whether the widget should show the conversation transcript as it
            goes on
        text_input_enabled:
          type: boolean
          default: true
          description: Whether the user should be able to send text messages
        conversation_mode_toggle_enabled:
          type: boolean
          default: false
          description: Whether to enable the conversation mode toggle in the widget
        default_expanded:
          type: boolean
          default: false
          description: Whether the widget should be expanded by default
        always_expanded:
          type: boolean
          default: false
          description: Whether the widget should always be expanded
        dismissible:
          type: boolean
          default: false
          description: Whether the widget can be dismissed by the user
        show_agent_status:
          type: boolean
          default: false
          description: Whether to show agent working/done/error status during tool use
        show_conversation_id:
          type: boolean
          default: true
          description: Whether to show the conversation ID after disconnection.
        strip_audio_tags:
          type: boolean
          default: true
          description: Whether to strip audio markup from messages.
        syntax_highlight_theme:
          $ref: '#/components/schemas/type_:WidgetConfigSyntaxHighlightTheme'
          description: >-
            Theme for code block syntax highlighting. Defaults to auto-detection
            by the widget when not set.
        text_contents:
          $ref: '#/components/schemas/type_:WidgetTextContents'
          description: Text contents of the widget
        styles:
          $ref: '#/components/schemas/type_:WidgetStyles'
          description: Styles for the widget
        language_selector:
          type: boolean
          default: false
          description: Whether to show the language selector
        supports_text_only:
          type: boolean
          default: true
          description: Whether the widget can switch to text only mode
        custom_avatar_path:
          type: string
          description: The custom avatar path
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:WidgetLanguagePreset'
          description: Language presets for the widget
      title: WidgetConfig
    type_:AnalysisPropertyType:
      type: string
      enum:
        - boolean
        - string
        - integer
        - number
      title: AnalysisPropertyType
    type_:AnalysisPropertyConstantValue:
      oneOf:
        - type: string
        - type: integer
        - type: number
          format: double
        - type: boolean
      description: >-
        A constant value to use for this property. Mutually exclusive with
        description, dynamic_variable, is_system_provided, and is_omitted.
      title: AnalysisPropertyConstantValue
    type_:AnalysisProperty:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:AnalysisPropertyType'
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
          $ref: '#/components/schemas/type_:AnalysisPropertyConstantValue'
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
        llm:
          $ref: '#/components/schemas/type_:Llm'
          description: >-
            LLM model to use for this analysis item. If not set, uses agent's
            analysis_llm default.
      required:
        - type
      description: >-
        Data collection property with optional per-item LLM override for
        post-call analysis.


        TODO: migrate to composition (value_schema: LiteralJsonSchemaProperty +
        llm) instead of

        inheritance, so this generalizes cleanly to object/array schemas in the
        future.
      title: AnalysisProperty
    type_:AsrConversationalConfigOverrideConfig:
      type: object
      properties:
        keywords:
          type: boolean
          default: false
          description: Whether to allow overriding the keywords field.
      title: AsrConversationalConfigOverrideConfig
    type_:SoftTimeoutConfigOverrideConfig:
      type: object
      properties:
        message:
          type: boolean
          default: false
          description: Whether to allow overriding the message field.
      title: SoftTimeoutConfigOverrideConfig
    type_:TurnConfigOverrideConfig:
      type: object
      properties:
        soft_timeout_config:
          $ref: '#/components/schemas/type_:SoftTimeoutConfigOverrideConfig'
          description: Configures overrides for nested fields.
      title: TurnConfigOverrideConfig
    type_:TtsConversationalConfigOverrideConfig:
      type: object
      properties:
        voice_id:
          type: boolean
          default: false
          description: Whether to allow overriding the voice_id field.
        stability:
          type: boolean
          default: false
          description: Whether to allow overriding the stability field.
        speed:
          type: boolean
          default: false
          description: Whether to allow overriding the speed field.
        similarity_boost:
          type: boolean
          default: false
          description: Whether to allow overriding the similarity_boost field.
      title: TtsConversationalConfigOverrideConfig
    type_:ConversationConfigOverrideConfig:
      type: object
      properties:
        text_only:
          type: boolean
          default: false
          description: Whether to allow overriding the text_only field.
      title: ConversationConfigOverrideConfig
    type_:PromptAgentApiModelOverrideConfig:
      type: object
      properties:
        prompt:
          type: boolean
          default: false
          description: Whether to allow overriding the prompt field.
        llm:
          type: boolean
          default: false
          description: Whether to allow overriding the llm field.
        tool_ids:
          type: boolean
          default: false
          description: Whether to allow overriding the tool_ids field.
        native_mcp_server_ids:
          type: boolean
          default: false
          description: Whether to allow overriding the native_mcp_server_ids field.
        knowledge_base:
          type: boolean
          default: false
          description: Whether to allow overriding the knowledge_base field.
      title: PromptAgentApiModelOverrideConfig
    type_:AgentConfigOverrideConfig:
      type: object
      properties:
        first_message:
          type: boolean
          default: false
          description: Whether to allow overriding the first_message field.
        language:
          type: boolean
          default: false
          description: Whether to allow overriding the language field.
        max_conversation_duration_message:
          type: boolean
          default: false
          description: >-
            Whether to allow overriding the max_conversation_duration_message
            field.
        prompt:
          $ref: '#/components/schemas/type_:PromptAgentApiModelOverrideConfig'
          description: Configures overrides for nested fields.
      title: AgentConfigOverrideConfig
    type_:ConversationConfigClientOverrideConfigInput:
      type: object
      properties:
        asr:
          $ref: '#/components/schemas/type_:AsrConversationalConfigOverrideConfig'
          description: Configures overrides for nested fields.
        turn:
          $ref: '#/components/schemas/type_:TurnConfigOverrideConfig'
          description: Configures overrides for nested fields.
        tts:
          $ref: '#/components/schemas/type_:TtsConversationalConfigOverrideConfig'
          description: Configures overrides for nested fields.
        conversation:
          $ref: '#/components/schemas/type_:ConversationConfigOverrideConfig'
          description: Configures overrides for nested fields.
        agent:
          $ref: '#/components/schemas/type_:AgentConfigOverrideConfig'
          description: Configures overrides for nested fields.
      title: ConversationConfigClientOverrideConfigInput
    type_:ConversationInitiationClientDataConfigInput:
      type: object
      properties:
        conversation_config_override:
          $ref: >-
            #/components/schemas/type_:ConversationConfigClientOverrideConfigInput
          description: Overrides for the conversation configuration
        custom_llm_extra_body:
          type: boolean
          default: false
          description: Whether to include custom LLM extra body
        enable_conversation_initiation_client_data_from_webhook:
          type: boolean
          default: false
          description: Whether to enable conversation initiation client data from webhooks
        enable_starting_workflow_node_id_from_client:
          type: boolean
          default: false
          description: >-
            Whether clients may pass starting_workflow_node_id in initiation
            client data; if false, sending it fails conversation start.
      title: ConversationInitiationClientDataConfigInput
    type_:ConversationInitiationClientDataWebhookRequestHeadersValue:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/type_:ConvAiSecretLocator'
      title: ConversationInitiationClientDataWebhookRequestHeadersValue
    type_:ConversationInitiationClientDataWebhook:
      type: object
      properties:
        url:
          type: string
          description: The URL to send the webhook to
        request_headers:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/type_:ConversationInitiationClientDataWebhookRequestHeadersValue
          description: The headers to send with the webhook request
      required:
        - url
        - request_headers
      title: ConversationInitiationClientDataWebhook
    type_:WebhookEventType:
      type: string
      enum:
        - transcript
        - audio
        - call_initiation_failure
        - unredacted_transcript
        - unredacted_audio
      title: WebhookEventType
    type_:WebhookTranscriptFormat:
      type: string
      enum:
        - json
        - opentelemetry
      default: json
      title: WebhookTranscriptFormat
    type_:ConvAiWebhooks:
      type: object
      properties:
        post_call_webhook_id:
          type: string
        events:
          type: array
          items:
            $ref: '#/components/schemas/type_:WebhookEventType'
          description: >-
            List of event types to send via webhook. Options: transcript, audio,
            call_initiation_failure, unredacted_transcript, unredacted_audio.
        transcript_format:
          $ref: '#/components/schemas/type_:WebhookTranscriptFormat'
          description: Format for transcript webhooks.
        send_audio:
          type: boolean
          description: >-
            DEPRECATED: Use 'events' field instead. Whether to send audio data
            with post-call webhooks for ConvAI conversations
      title: ConvAiWebhooks
    type_:AgentWorkspaceOverridesInput:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          $ref: '#/components/schemas/type_:ConversationInitiationClientDataWebhook'
          description: The webhook to send conversation initiation client data to
        webhooks:
          $ref: '#/components/schemas/type_:ConvAiWebhooks'
      title: AgentWorkspaceOverridesInput
    type_:AttachedTestModel:
      type: object
      properties:
        test_id:
          type: string
        workflow_node_id:
          type: string
      required:
        - test_id
      title: AttachedTestModel
    type_:AgentTestingSettings:
      type: object
      properties:
        attached_tests:
          type: array
          items:
            $ref: '#/components/schemas/type_:AttachedTestModel'
          description: List of test IDs that should be run for this agent
      description: Settings for agent testing configuration.
      title: AgentTestingSettings
    type_:FocusGuardrail:
      type: object
      properties:
        is_enabled:
          type: boolean
          default: false
      title: FocusGuardrail
    type_:PromptInjectionGuardrail:
      type: object
      properties:
        is_enabled:
          type: boolean
          default: false
      title: PromptInjectionGuardrail
    type_:ContentThresholdGuardrailThreshold:
      oneOf:
        - type: number
          format: double
        - type: string
          enum:
            - low
        - type: string
          enum:
            - medium
        - type: string
          enum:
            - high
      title: ContentThresholdGuardrailThreshold
    type_:ContentThresholdGuardrail:
      type: object
      properties:
        is_enabled:
          type: boolean
          default: false
        threshold:
          $ref: '#/components/schemas/type_:ContentThresholdGuardrailThreshold'
      title: ContentThresholdGuardrail
    type_:ContentConfig:
      type: object
      properties:
        sexual:
          $ref: '#/components/schemas/type_:ContentThresholdGuardrail'
        violence:
          $ref: '#/components/schemas/type_:ContentThresholdGuardrail'
        harassment:
          $ref: '#/components/schemas/type_:ContentThresholdGuardrail'
        self_harm:
          $ref: '#/components/schemas/type_:ContentThresholdGuardrail'
        profanity:
          $ref: '#/components/schemas/type_:ContentThresholdGuardrail'
        religion_or_politics:
          $ref: '#/components/schemas/type_:ContentThresholdGuardrail'
        medical_and_legal_information:
          $ref: '#/components/schemas/type_:ContentThresholdGuardrail'
      title: ContentConfig
    type_:ContentGuardrailInputTriggerAction:
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
      title: ContentGuardrailInputTriggerAction
    type_:ContentGuardrailInput:
      type: object
      properties:
        execution_mode:
          $ref: '#/components/schemas/type_:GuardrailExecutionMode'
        config:
          $ref: '#/components/schemas/type_:ContentConfig'
        trigger_action:
          $ref: '#/components/schemas/type_:ContentGuardrailInputTriggerAction'
      title: ContentGuardrailInput
    type_:CustomGuardrailsConfigInput:
      type: object
      properties:
        configs:
          type: array
          items:
            $ref: '#/components/schemas/type_:CustomGuardrailConfig'
      description: Config container for custom guardrails list
      title: CustomGuardrailsConfigInput
    type_:CustomGuardrailInput:
      type: object
      properties:
        config:
          $ref: '#/components/schemas/type_:CustomGuardrailsConfigInput'
      description: Container for custom guardrails, matching ModerationGuardrail pattern
      title: CustomGuardrailInput
    type_:GuardrailsV1Input:
      type: object
      properties:
        version:
          type: string
          enum:
            - '1'
        focus:
          $ref: '#/components/schemas/type_:FocusGuardrail'
        prompt_injection:
          $ref: '#/components/schemas/type_:PromptInjectionGuardrail'
        content:
          $ref: '#/components/schemas/type_:ContentGuardrailInput'
        custom:
          $ref: '#/components/schemas/type_:CustomGuardrailInput'
      title: GuardrailsV1Input
    type_:AuthSettings:
      type: object
      properties:
        enable_auth:
          type: boolean
          default: false
          description: >-
            If set to true, starting a conversation with an agent will require a
            signed token
        allowlist:
          type: array
          items:
            $ref: '#/components/schemas/type_:AllowlistItem'
          description: >-
            A list of hosts that are allowed to start conversations with the
            agent
        require_origin_header:
          type: boolean
          default: false
          description: >-
            When enabled, connections with no origin header will be rejected. If
            the allowlist is empty, this option has no effect.
        shareable_token:
          type: string
          description: >-
            A shareable token that can be used to start a conversation with the
            agent
      title: AuthSettings
    type_:AgentCallLimits:
      type: object
      properties:
        agent_concurrency_limit:
          type: integer
          default: -1
          description: >-
            The maximum number of concurrent conversations. -1 indicates that
            there is no maximum
        daily_limit:
          type: integer
          default: 100000
          description: The maximum number of conversations per day
        bursting_enabled:
          type: boolean
          default: true
          description: >-
            Whether to enable bursting. If true, exceeding workspace concurrency
            limit will be allowed up to 3 times the limit. Calls will be charged
            at double rate when exceeding the limit.
      title: AgentCallLimits
    type_:ConfigEntityType:
      type: string
      enum:
        - name
        - name.name_given
        - name.name_family
        - name.name_other
        - email_address
        - contact_number
        - dob
        - age
        - religious_belief
        - political_opinion
        - sexual_orientation
        - ethnicity_race
        - marital_status
        - occupation
        - physical_attribute
        - language
        - username
        - password
        - url
        - organization
        - financial_id
        - financial_id.payment_card
        - financial_id.payment_card.payment_card_number
        - financial_id.payment_card.payment_card_expiration_date
        - financial_id.payment_card.payment_card_cvv
        - financial_id.bank_account
        - financial_id.bank_account.bank_account_number
        - financial_id.bank_account.bank_routing_number
        - financial_id.bank_account.swift_bic_code
        - financial_id.financial_id_other
        - location
        - location.location_address
        - location.location_city
        - location.location_postal_code
        - location.location_coordinate
        - location.location_state
        - location.location_country
        - location.location_other
        - date
        - date_interval
        - unique_id
        - unique_id.government_issued_id
        - unique_id.account_number
        - unique_id.vehicle_id
        - unique_id.healthcare_number
        - unique_id.healthcare_number.medical_record_number
        - unique_id.healthcare_number.health_plan_beneficiary_number
        - unique_id.device_id
        - unique_id.unique_id_other
        - medical
        - medical.medical_condition
        - medical.medication
        - medical.medical_procedure
        - medical.medical_measurement
        - medical.medical_other
      description: >-
        Entity types for the API configuration.


        This enum contains all valid entity type configurations that users can
        specify:

        - Parent types (e.g., "name", "financial_id") that expand to all
        subtypes

        - Specific subtypes using dot notation (e.g., "name.full_name")

        - Standalone terminal types (e.g., "email_address")


        When converted for service use, parent types expand to all their
        terminal subtypes.
      title: ConfigEntityType
    type_:ConversationHistoryRedactionConfig:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
          description: Whether conversation history redaction is enabled
        entities:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConfigEntityType'
          description: >-
            The entities to redact from the conversation transcript, audio and
            analysis. Use top-level types like 'name', 'email_address', or dot
            notation for specific subtypes like 'name.full_name'.
      title: ConversationHistoryRedactionConfig
    type_:PrivacyConfigInput:
      type: object
      properties:
        record_voice:
          type: boolean
          default: true
          description: Whether to record the conversation
        retention_days:
          type: integer
          default: -1
          description: >-
            The number of days to retain the conversation. -1 indicates there is
            no retention limit
        delete_transcript_and_pii:
          type: boolean
          default: false
          description: Whether to delete the transcript and PII
        delete_audio:
          type: boolean
          default: false
          description: Whether to delete the audio
        apply_to_existing_conversations:
          type: boolean
          default: false
          description: Whether to apply the privacy settings to existing conversations
        zero_retention_mode:
          type: boolean
          default: false
          description: Whether to enable zero retention mode - no PII data is stored
        conversation_history_redaction:
          $ref: '#/components/schemas/type_:ConversationHistoryRedactionConfig'
          description: Config for PII redaction in the conversation history
      title: PrivacyConfigInput
    type_:AgentTrustContext:
      type: string
      enum:
        - unknown
        - low
        - high
      default: unknown
      description: >-
        The trust context in which the agent operates.


        UNKNOWN: not yet classified (existing agents created before this
        feature).

        LOW: serves untrusted external participants (e.g. customer support,
        sales) —
             outputs should be vetted and tool access scoped.
        HIGH: serves the owner (e.g. personal assistant) — full tool access is
        appropriate.
      title: AgentTrustContext
    type_:TopicDiscoverySettings:
      type: object
      properties: {}
      description: |-
        Per-agent topic-discovery configuration. Cadence and analysis window are
        managed internally; this only exposes the customer-facing on/off toggle.
      title: TopicDiscoverySettings
    type_:AgentPlatformSettingsRequestModel:
      type: object
      properties:
        evaluation:
          $ref: '#/components/schemas/type_:EvaluationSettingsInput'
          description: Settings for evaluation
        widget:
          $ref: '#/components/schemas/type_:WidgetConfig'
          description: Configuration for the widget
        data_collection:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:AnalysisProperty'
          description: Data collection settings
        data_collection_scopes:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:AnalysisScope'
          description: >-
            Scope per data collection item ID. Missing keys default to
            conversation scope.
        overrides:
          $ref: >-
            #/components/schemas/type_:ConversationInitiationClientDataConfigInput
          description: Additional overrides for the agent during conversation initiation
        workspace_overrides:
          $ref: '#/components/schemas/type_:AgentWorkspaceOverridesInput'
          description: Workspace overrides for the agent
        testing:
          $ref: '#/components/schemas/type_:AgentTestingSettings'
          description: Testing configuration for the agent
        archived:
          type: boolean
          default: false
          description: Whether the agent is archived
        guardrails:
          $ref: '#/components/schemas/type_:GuardrailsV1Input'
          description: Guardrails configuration for the agent
        summary_language:
          type: string
          description: >-
            Language for all conversation analysis outputs (summaries, titles,
            evaluation rationales, data collection rationales). If not set, the
            language will be inferred from the conversation. Must be one of the
            supported conversation languages.
        auth:
          $ref: '#/components/schemas/type_:AuthSettings'
          description: Settings for authentication
        call_limits:
          $ref: '#/components/schemas/type_:AgentCallLimits'
          description: Call limits for the agent
        privacy:
          $ref: '#/components/schemas/type_:PrivacyConfigInput'
          description: Privacy settings for the agent
        trust_context:
          $ref: '#/components/schemas/type_:AgentTrustContext'
          description: The trust context in which the agent operates.
        analysis_llm:
          $ref: '#/components/schemas/type_:Llm'
          description: >-
            Default LLM model for post-call analysis (evaluation and data
            collection)
        topic_discovery:
          $ref: '#/components/schemas/type_:TopicDiscoverySettings'
          description: Per-agent topic discovery configuration
      title: AgentPlatformSettingsRequestModel
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
    type_:AdhocAgentConfigOverrideForTestRequestModel:
      type: object
      properties:
        conversation_config:
          $ref: '#/components/schemas/type_:ConversationalConfig'
        platform_settings:
          $ref: '#/components/schemas/type_:AgentPlatformSettingsRequestModel'
        workflow:
          $ref: '#/components/schemas/type_:AgentWorkflowRequestModel'
      required:
        - conversation_config
        - platform_settings
      title: AdhocAgentConfigOverrideForTestRequestModel
    type_:BucketingStatus:
      type: string
      enum:
        - pending
        - completed
        - failed
      title: BucketingStatus
    type_:TestRunStatus:
      type: string
      enum:
        - pending
        - passed
        - failed
      title: TestRunStatus
    type_:TestRunResultBucket:
      type: object
      properties:
        test_run_ids:
          type: array
          items:
            type: string
        title:
          type: string
          description: Short one-line title for this bucket
        reason:
          type: string
          description: Short summary of why the test runs in this bucket passed or failed
        status:
          $ref: '#/components/schemas/type_:TestRunStatus'
      required:
        - test_run_ids
        - title
        - reason
        - status
      title: TestRunResultBucket
    type_:TestRunResultSummary:
      type: object
      properties:
        test_id:
          type: string
        test_name:
          type: string
        workflow_node_id:
          type: string
        buckets:
          type: array
          items:
            $ref: '#/components/schemas/type_:TestRunResultBucket'
      required:
        - test_id
        - test_name
        - buckets
      title: TestRunResultSummary
    type_:ConversationHistoryTranscriptCommonModelOutputRole:
      type: string
      enum:
        - user
        - agent
      title: ConversationHistoryTranscriptCommonModelOutputRole
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
    type_:TransferToAgentToolResultSuccessModelBranchInfo:
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
      title: TransferToAgentToolResultSuccessModelBranchInfo
    type_:ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult:
      oneOf:
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
                #/components/schemas/type_:TransferToAgentToolResultSuccessModelBranchInfo
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
    type_:ConversationHistoryTranscriptCommonModelOutputToolResultsItem:
      oneOf:
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptOtherToolsResultCommonModel
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptSystemToolResultCommonModelOutput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput
        - $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput
      title: ConversationHistoryTranscriptCommonModelOutputToolResultsItem
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
    type_:LlmUsageOutput:
      type: object
      properties:
        model_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:LlmInputOutputTokensUsage'
      title: LlmUsageOutput
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
    type_:ConversationHistoryTranscriptCommonModelOutput:
      type: object
      properties:
        role:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryTranscriptCommonModelOutputRole
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
              #/components/schemas/type_:ConversationHistoryTranscriptCommonModelOutputToolResultsItem
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
      required:
        - role
        - time_in_call_secs
      title: ConversationHistoryTranscriptCommonModelOutput
    type_:TestFromConversationMetadataOutput:
      type: object
      properties:
        conversation_id:
          type: string
        agent_id:
          type: string
        branch_id:
          type: string
        workflow_node_id:
          type: string
        original_agent_reply:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptCommonModelOutput
          default: []
      required:
        - conversation_id
        - agent_id
      title: TestFromConversationMetadataOutput
    type_:ConversationInitiationSource:
      type: string
      enum:
        - unknown
        - android_sdk
        - node_js_sdk
        - react_native_sdk
        - react_sdk
        - js_sdk
        - python_sdk
        - widget
        - sip_trunk
        - twilio
        - exotel
        - genesys
        - swift_sdk
        - whatsapp
        - twilio_sms
        - flutter_sdk
        - zendesk_integration
        - slack_integration
        - telegram_integration
        - intercom_integration
        - freshdesk_integration
        - template_preview
        - genesys_bot_connector
      default: unknown
      description: Enum representing the possible sources for conversation initiation.
      title: ConversationInitiationSource
    type_:AgentSuccessfulResponseExample:
      type: object
      properties:
        response:
          type: string
        type:
          type: string
          enum:
            - success
      required:
        - response
        - type
      title: AgentSuccessfulResponseExample
    type_:AgentFailureResponseExample:
      type: object
      properties:
        response:
          type: string
        type:
          type: string
          enum:
            - failure
      required:
        - response
        - type
      title: AgentFailureResponseExample
    type_:MockingStrategy:
      type: string
      enum:
        - all
        - selected
        - none
      default: none
      title: MockingStrategy
    type_:MockNoMatchBehavior:
      type: string
      enum:
        - call_real_tool
        - raise_error
      default: raise_error
      title: MockNoMatchBehavior
    type_:SimulationToolMockBehaviorConfig:
      type: object
      properties:
        mocking_strategy:
          $ref: '#/components/schemas/type_:MockingStrategy'
          description: >-
            Which tools to mock: 'all' mocks every mockable tool, 'selected'
            mocks only those in mocked_tool_names/mocked_tool_ids, 'none'
            disables mocking.
        fallback_strategy:
          $ref: '#/components/schemas/type_:MockNoMatchBehavior'
          description: Behavior when no mock matches a tool call.
        mocked_tool_ids:
          type: array
          items:
            type: string
          description: >-
            Tool IDs to mock. Resolved to tool names before being passed to the
            orchestrator.
      description: >-
        Simulation/preview-side config: tools are identified by IDs, resolved to
        names at runtime.
      title: SimulationToolMockBehaviorConfig
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
    type_:ReferencedToolCommonModelType:
      type: string
      enum:
        - system
        - webhook
        - client
        - workflow
        - api_integration_webhook
        - mcp
        - code
      description: The type of the tool
      title: ReferencedToolCommonModelType
    type_:ReferencedToolCommonModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the tool
        type:
          $ref: '#/components/schemas/type_:ReferencedToolCommonModelType'
          description: The type of the tool
      required:
        - id
        - type
      description: Reference to a tool for unit test evaluation.
      title: ReferencedToolCommonModel
    type_:UnitTestWorkflowNodeTransitionEvaluationNodeId:
      type: object
      properties:
        type:
          type: string
          enum:
            - node_id
        agent_id:
          type: string
          description: The ID of the agent whose workflow contains the target node.
        target_node_id:
          type: string
          description: The ID of the workflow node that the agent should transition to.
      required:
        - agent_id
        - target_node_id
      title: UnitTestWorkflowNodeTransitionEvaluationNodeId
    type_:UnitTestToolCallEvaluationModelOutput:
      type: object
      properties:
        parameters:
          type: array
          items:
            $ref: '#/components/schemas/type_:UnitTestToolCallParameter'
          description: >-
            Parameters to evaluate for the agent's tool call. If empty, the tool
            call parameters are not evaluated.
        referenced_tool:
          $ref: '#/components/schemas/type_:ReferencedToolCommonModel'
          description: The tool to evaluate a call against.
        verify_absence:
          type: boolean
          default: false
          description: Whether to verify that the tool was NOT called.
        workflow_node_transition:
          $ref: >-
            #/components/schemas/type_:UnitTestWorkflowNodeTransitionEvaluationNodeId
          description: >-
            Configuration for testing workflow node transitions. When set, the
            test will verify the agent transitions to the specified workflow
            node.
      title: UnitTestToolCallEvaluationModelOutput
    type_:UnitTestRunResponseModelTestInfo:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - llm
              description: 'Discriminator value: llm'
            from_conversation_metadata:
              $ref: '#/components/schemas/type_:TestFromConversationMetadataOutput'
              description: >-
                Metadata of a conversation this test was created from (if
                applicable).
            dynamic_variables:
              type: object
              additionalProperties:
                description: Any type
              description: Dynamic variables to replace in the agent config during testing
            chat_history:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:ConversationHistoryTranscriptCommonModelOutput
            conversation_initiation_source:
              $ref: '#/components/schemas/type_:ConversationInitiationSource'
              description: >-
                Simulate the test as if the conversation originated from this
                channel.
            success_condition:
              type: string
              default: ''
              description: >-
                A prompt that evaluates whether the agent's response is
                successful. Should return True or False.
            success_examples:
              type: array
              items:
                $ref: '#/components/schemas/type_:AgentSuccessfulResponseExample'
              description: >-
                Non-empty list of example responses that should be considered
                successful
            failure_examples:
              type: array
              items:
                $ref: '#/components/schemas/type_:AgentFailureResponseExample'
              description: >-
                Non-empty list of example responses that should be considered
                failures
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - simulation
              description: 'Discriminator value: simulation'
            from_conversation_metadata:
              $ref: '#/components/schemas/type_:TestFromConversationMetadataOutput'
              description: >-
                Metadata of a conversation this test was created from (if
                applicable).
            dynamic_variables:
              type: object
              additionalProperties:
                description: Any type
              description: Dynamic variables to replace in the agent config during testing
            chat_history:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:ConversationHistoryTranscriptCommonModelOutput
            conversation_initiation_source:
              $ref: '#/components/schemas/type_:ConversationInitiationSource'
              description: >-
                Simulate the test as if the conversation originated from this
                channel.
            success_condition:
              type: string
              description: >-
                Deprecated legacy single success criterion. Use
                success_conditions instead. At least one of success_condition or
                success_conditions is required.
            success_conditions:
              type: array
              items:
                type: string
              description: >-
                List of prompts that evaluate whether the simulation was
                successful. If provided, all criteria are evaluated and merged
                into a final result. Capped at the maximum number of evaluation
                criteria.
            simulation_scenario:
              type: string
              default: ''
              description: >-
                Description of the simulation scenario and user persona for
                simulation tests.
            simulation_max_turns:
              type: integer
              default: 5
              description: Maximum number of conversation turns for simulation tests.
            simulation_environment:
              type: string
              description: >-
                The environment to use when running this simulation test. If not
                provided, defaults to 'production'.
            tool_mock_config:
              $ref: '#/components/schemas/type_:SimulationToolMockBehaviorConfig'
              description: Configuration for which tools to mock and fallback behavior.
            evaluation_model:
              $ref: '#/components/schemas/type_:Llm'
              description: >-
                LLM model to use for evaluating simulation results. Defaults to
                Claude Sonnet 4.6.
            simulated_user_model:
              $ref: '#/components/schemas/type_:Llm'
              description: LLM model for the simulated user. Defaults to Claude Sonnet 4.6.
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - tool
              description: 'Discriminator value: tool'
            from_conversation_metadata:
              $ref: '#/components/schemas/type_:TestFromConversationMetadataOutput'
              description: >-
                Metadata of a conversation this test was created from (if
                applicable).
            dynamic_variables:
              type: object
              additionalProperties:
                description: Any type
              description: Dynamic variables to replace in the agent config during testing
            chat_history:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:ConversationHistoryTranscriptCommonModelOutput
            conversation_initiation_source:
              $ref: '#/components/schemas/type_:ConversationInitiationSource'
              description: >-
                Simulate the test as if the conversation originated from this
                channel.
            tool_call_parameters:
              $ref: '#/components/schemas/type_:UnitTestToolCallEvaluationModelOutput'
              description: >-
                How to evaluate the agent's tool call (if any). If empty, the
                tool call is not evaluated.
            check_any_tool_matches:
              type: boolean
              description: >-
                If set to True this test will pass if any tool call returned by
                the LLM matches the criteria. Otherwise it will fail if more
                than one tool is returned by the agent.
          required:
            - type
      discriminator:
        propertyName: type
      title: UnitTestRunResponseModelTestInfo
    type_:EvaluationSuccessResult:
      type: string
      enum:
        - success
        - failure
        - unknown
      title: EvaluationSuccessResult
    type_:TestConditionRationaleCommonModel:
      type: object
      properties:
        messages:
          type: array
          items:
            type: string
          description: List of individual parameter evaluation messages or reasons
        summary:
          type: string
          default: ''
          description: High-level summary of the evaluation result
      description: >-
        Structured rationale for test condition results containing individual
        failure/success reasons.
      title: TestConditionRationaleCommonModel
    type_:TestConditionResultCommonModel:
      type: object
      properties:
        result:
          $ref: '#/components/schemas/type_:EvaluationSuccessResult'
        rationale:
          $ref: '#/components/schemas/type_:TestConditionRationaleCommonModel'
      required:
        - result
      title: TestConditionResultCommonModel
    type_:TestRunMetadataTestType:
      type: string
      enum:
        - llm
        - tool_call
        - simulation
      default: llm
      title: TestRunMetadataTestType
    type_:TestRunMetadata:
      type: object
      properties:
        workspace_id:
          type: string
        test_name:
          type: string
        ran_by_user_email:
          type: string
        test_type:
          $ref: '#/components/schemas/type_:TestRunMetadataTestType'
          default: llm
      required:
        - workspace_id
        - test_name
        - ran_by_user_email
      title: TestRunMetadata
    type_:UnitTestRunResponseModel:
      type: object
      properties:
        test_run_id:
          type: string
        test_info:
          $ref: '#/components/schemas/type_:UnitTestRunResponseModelTestInfo'
        test_invocation_id:
          type: string
        agent_id:
          type: string
        branch_id:
          type: string
        workflow_node_id:
          type: string
        status:
          $ref: '#/components/schemas/type_:TestRunStatus'
        agent_responses:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptCommonModelOutput
        test_id:
          type: string
        test_name:
          type: string
          default: Unknown Test
        condition_result:
          $ref: '#/components/schemas/type_:TestConditionResultCommonModel'
        last_updated_at_unix:
          type: integer
        metadata:
          $ref: '#/components/schemas/type_:TestRunMetadata'
        root_folder_id:
          type: string
        root_folder_name:
          type: string
        environment:
          type: string
      required:
        - test_run_id
        - test_invocation_id
        - agent_id
        - status
        - test_id
      title: UnitTestRunResponseModel
    type_:GetTestSuiteInvocationResponseModel:
      type: object
      properties:
        id:
          type: string
        agent_id:
          type: string
        branch_id:
          type: string
        created_at:
          type: integer
        folder_id:
          type: string
        repeat_count:
          type: integer
          default: 1
        bucketing_status:
          $ref: '#/components/schemas/type_:BucketingStatus'
          description: >-
            None when repeat_count==1 (no bucketing). Otherwise tracks bucketing
            lifecycle.
        result_groups:
          type: array
          items:
            $ref: '#/components/schemas/type_:TestRunResultSummary'
        test_runs:
          type: array
          items:
            $ref: '#/components/schemas/type_:UnitTestRunResponseModel'
      required:
        - id
        - test_runs
      title: GetTestSuiteInvocationResponseModel
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
  "tests": [
    {
      "test_id": "test_id"
    }
  ]
}
```

**Response**

```json
{
  "id": "id",
  "test_runs": [
    {
      "test_run_id": "test_run_id",
      "test_invocation_id": "test_invocation_id",
      "agent_id": "agent_id",
      "status": "pending",
      "test_id": "test_id",
      "test_info": {
        "type": "llm"
      },
      "branch_id": "branch_id",
      "workflow_node_id": "workflow_node_id",
      "agent_responses": [
        {
          "role": "user",
          "time_in_call_secs": 1
        }
      ],
      "test_name": "test_name",
      "condition_result": {
        "result": "success"
      },
      "last_updated_at_unix": 1,
      "metadata": {
        "workspace_id": "workspace_id",
        "test_name": "test_name",
        "ran_by_user_email": "ran_by_user_email"
      },
      "root_folder_id": "root_folder_id",
      "root_folder_name": "root_folder_name",
      "environment": "environment"
    }
  ],
  "agent_id": "agent_id",
  "branch_id": "branch_id",
  "created_at": 1,
  "folder_id": "folder_id",
  "repeat_count": 1,
  "bucketing_status": "pending",
  "result_groups": [
    {
      "test_id": "test_id",
      "test_name": "test_name",
      "buckets": [
        {
          "test_run_ids": [
            "test_run_ids"
          ],
          "title": "title",
          "reason": "reason",
          "status": "pending"
        }
      ],
      "workflow_node_id": "workflow_node_id"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.runTests("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        tests: [
            {
                testId: "test_id",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, SingleTestRunRequestModel

client = ElevenLabs()

client.conversational_ai.agents.run_tests(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    tests=[
        SingleTestRunRequestModel(
            test_id="test_id",
        )
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests"

	payload := strings.NewReader("{\n  \"tests\": [\n    {\n      \"test_id\": \"test_id\"\n    }\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tests\": [\n    {\n      \"test_id\": \"test_id\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests")
  .header("Content-Type", "application/json")
  .body("{\n  \"tests\": [\n    {\n      \"test_id\": \"test_id\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests', [
  'body' => '{
  "tests": [
    {
      "test_id": "test_id"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tests\": [\n    {\n      \"test_id\": \"test_id\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["tests": [["test_id": "test_id"]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/run-tests")! as URL,
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
