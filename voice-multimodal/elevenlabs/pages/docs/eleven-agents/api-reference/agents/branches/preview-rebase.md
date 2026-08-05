---
title: "Preview rebased configuration"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/preview-rebase.md
path: docs/eleven-agents/api-reference/agents/branches/preview-rebase
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Preview rebased configuration

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}/rebase-preview

Returns the result of rebasing the branch onto main without performing the rebase. Useful for showing an accurate diff before confirming.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/preview-rebase

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase-preview:
    get:
      operationId: preview_rebase
      summary: Preview Rebased Configuration
      description: >-
        Returns the result of rebasing the branch onto main without performing
        the rebase. Useful for showing an accurate diff before confirming.
      tags:
        - branches
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
        - name: branch_id
          in: path
          description: Unique identifier for the source branch to merge from.
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
                $ref: '#/components/schemas/type_:MergePreviewResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
        interruption_ignore_term_languages:
          type: array
          items:
            type: string
          description: >-
            Language codes for which preset ignore-term categories have been
            activated. Stored explicitly so display is not inferred from term
            overlap.
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
          description: 'Deprecated: this field is a no-op and is ignored.'
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
          default: true
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
        max_files_in_memory:
          type: integer
          default: 10
          description: >-
            Number of most-recent files kept in memory during a conversation.
            Older files are summarized and their bytes freed.
        max_files_per_conversation:
          type: integer
          default: 10
          description: >-
            Total files a user can upload in one conversation. Uploads are
            billed per file. Use -1 for no limit, or a value >=
            max_files_in_memory.
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
        model_id:
          $ref: '#/components/schemas/type_:TtsConversationalModel'
          description: The model to use for TTS
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
    type_:AgentMetadataResponseModel:
      type: object
      properties:
        created_at_unix_secs:
          type: integer
          description: The creation time of the agent in unix seconds
        updated_at_unix_secs:
          type: integer
          description: The last update time of the agent in unix seconds
      required:
        - created_at_unix_secs
        - updated_at_unix_secs
      title: AgentMetadataResponseModel
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
    type_:EvaluationSettingsOutput:
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
      title: EvaluationSettingsOutput
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
        attach_file:
          type: string
          description: Text and ARIA label for the attach file button.
        remove_file:
          type: string
          description: ARIA label for the remove file button.
        file_upload_error:
          type: string
          description: Error message displayed when a file fails to upload.
        file_type_unsupported:
          type: string
          description: >-
            Error message displayed when an unsupported file type is selected.
            Followed by the list of accepted types.
        file_too_large:
          type: string
          description: Error message displayed when a file exceeds the maximum size limit.
        file_limit_reached:
          type: string
          description: >-
            Error message displayed when the maximum number of files for a
            conversation is reached.
        typing_indicator:
          type: string
          description: Status text displayed while the agent is typing.
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
    type_:WidgetTextContentsTranslation:
      type: object
      properties:
        source:
          type: object
          additionalProperties:
            type: string
          description: The source text each translated field was derived from
        text:
          type: object
          additionalProperties:
            type: string
          description: The last auto-translated output for each translated field
      title: WidgetTextContentsTranslation
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
        text_contents_translation:
          $ref: '#/components/schemas/type_:WidgetTextContentsTranslation'
          description: The translation cache for the text contents
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
        show_resize_button:
          type: boolean
          default: true
          description: Whether to show the resize button
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
    type_:AttachedSystemEvaluationRefAnalysisItemId:
      type: string
      enum:
        - __system_eval_criteria_sentiment
        - __system_eval_criteria_frustration
      description: Id of the referenced built-in system evaluation.
      title: AttachedSystemEvaluationRefAnalysisItemId
    type_:AgentAnalysisItemsOutputEvaluationCriteriaItem:
      oneOf:
        - type: object
          properties:
            source:
              type: string
              enum:
                - system
              description: 'Discriminator value: system'
            analysis_item_id:
              $ref: >-
                #/components/schemas/type_:AttachedSystemEvaluationRefAnalysisItemId
              description: Id of the referenced built-in system evaluation.
            scope:
              $ref: '#/components/schemas/type_:AnalysisScope'
              description: >-
                Transcript context ('conversation' or 'agent') used when running
                this item.
            weight:
              type: number
              format: double
              description: Optional relative weight for aggregate scoring.
          required:
            - source
            - analysis_item_id
        - type: object
          properties:
            source:
              type: string
              enum:
                - user
              description: 'Discriminator value: user'
            analysis_item_id:
              type: string
              description: Id of the referenced user evaluation item.
            version_id:
              type: string
              description: >-
                Primary item version whose result feeds scoring. None tracks the
                item's latest published version.
            additional_version_ids:
              type: array
              items:
                type: string
              description: >-
                Extra item versions to also run for comparison (A/B). These are
                executed and stored but excluded from scoring; the primary
                version_id is the one that scores.
            scope:
              $ref: '#/components/schemas/type_:AnalysisScope'
              description: >-
                Transcript context ('conversation' or 'agent') used when running
                this item.
            weight:
              type: number
              format: double
              description: Optional relative weight for aggregate scoring.
          required:
            - source
            - analysis_item_id
      discriminator:
        propertyName: source
      title: AgentAnalysisItemsOutputEvaluationCriteriaItem
    type_:AgentAnalysisItemsOutputDataCollectionItem:
      oneOf:
        - type: object
          properties:
            source:
              type: string
              enum:
                - system
              description: 'Discriminator value: system'
            analysis_item_id:
              type: string
              enum:
                - __system_data_collection_topic
              description: Id of the referenced built-in system data-collection item.
            scope:
              $ref: '#/components/schemas/type_:AnalysisScope'
              description: >-
                Transcript context ('conversation' or 'agent') used when running
                this item.
          required:
            - source
            - analysis_item_id
        - type: object
          properties:
            source:
              type: string
              enum:
                - user
              description: 'Discriminator value: user'
            analysis_item_id:
              type: string
              description: Id of the referenced user data-collection item.
            version_id:
              type: string
              description: >-
                Pinned item version. None tracks the item's latest published
                version.
            scope:
              $ref: '#/components/schemas/type_:AnalysisScope'
              description: >-
                Transcript context ('conversation' or 'agent') used when running
                this item.
          required:
            - source
            - analysis_item_id
      discriminator:
        propertyName: source
      title: AgentAnalysisItemsOutputDataCollectionItem
    type_:AgentAnalysisItemsOutput:
      type: object
      properties:
        evaluation_criteria:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:AgentAnalysisItemsOutputEvaluationCriteriaItem
        data_collection:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:AgentAnalysisItemsOutputDataCollectionItem
      title: AgentAnalysisItemsOutput
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
        model_id:
          type: boolean
          default: false
          description: Whether to allow overriding the model_id field.
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
    type_:ConversationConfigClientOverrideConfigOutput:
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
      title: ConversationConfigClientOverrideConfigOutput
    type_:ConversationInitiationClientDataConfigOutput:
      type: object
      properties:
        conversation_config_override:
          $ref: >-
            #/components/schemas/type_:ConversationConfigClientOverrideConfigOutput
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
      title: ConversationInitiationClientDataConfigOutput
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
    type_:AgentWorkspaceOverridesOutput:
      type: object
      properties:
        conversation_initiation_client_data_webhook:
          $ref: '#/components/schemas/type_:ConversationInitiationClientDataWebhook'
          description: The webhook to send conversation initiation client data to
        webhooks:
          $ref: '#/components/schemas/type_:ConvAiWebhooks'
      title: AgentWorkspaceOverridesOutput
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
    type_:ContentGuardrailOutputTriggerAction:
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
      title: ContentGuardrailOutputTriggerAction
    type_:ContentGuardrailOutput:
      type: object
      properties:
        execution_mode:
          $ref: '#/components/schemas/type_:GuardrailExecutionMode'
        config:
          $ref: '#/components/schemas/type_:ContentConfig'
        trigger_action:
          $ref: '#/components/schemas/type_:ContentGuardrailOutputTriggerAction'
      title: ContentGuardrailOutput
    type_:CustomGuardrailsConfigOutput:
      type: object
      properties:
        configs:
          type: array
          items:
            $ref: '#/components/schemas/type_:CustomGuardrailConfig'
      description: Config container for custom guardrails list
      title: CustomGuardrailsConfigOutput
    type_:CustomGuardrailOutput:
      type: object
      properties:
        config:
          $ref: '#/components/schemas/type_:CustomGuardrailsConfigOutput'
      description: Container for custom guardrails, matching ModerationGuardrail pattern
      title: CustomGuardrailOutput
    type_:GuardrailsV1Output:
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
          $ref: '#/components/schemas/type_:ContentGuardrailOutput'
        custom:
          $ref: '#/components/schemas/type_:CustomGuardrailOutput'
      title: GuardrailsV1Output
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
    type_:PrivacyConfigOutput:
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
      title: PrivacyConfigOutput
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
    type_:SentimentAnalysisSettings:
      type: object
      properties: {}
      title: SentimentAnalysisSettings
    type_:SafetyResponseModel:
      type: object
      properties:
        is_blocked_ivc:
          type: boolean
          default: false
        is_blocked_non_ivc:
          type: boolean
          default: false
        ignore_safety_evaluation:
          type: boolean
          default: false
      title: SafetyResponseModel
    type_:AgentPlatformSettingsResponseModel:
      type: object
      properties:
        evaluation:
          $ref: '#/components/schemas/type_:EvaluationSettingsOutput'
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
        analysis_items:
          $ref: '#/components/schemas/type_:AgentAnalysisItemsOutput'
          description: >-
            Evaluation + data-collection items attached by reference. None means
            the agent has not been migrated onto analysis items yet (distinct
            from an empty, migrated set); reads fall back to the legacy
            evaluation/data_collection fields in that case.
        overrides:
          $ref: >-
            #/components/schemas/type_:ConversationInitiationClientDataConfigOutput
          description: Additional overrides for the agent during conversation initiation
        workspace_overrides:
          $ref: '#/components/schemas/type_:AgentWorkspaceOverridesOutput'
          description: Workspace overrides for the agent
        testing:
          $ref: '#/components/schemas/type_:AgentTestingSettings'
          description: Testing configuration for the agent
        archived:
          type: boolean
          default: false
          description: Whether the agent is archived
        guardrails:
          $ref: '#/components/schemas/type_:GuardrailsV1Output'
          description: Guardrails configuration for the agent
        summary_language:
          type: string
          description: >-
            Language for all conversation analysis outputs (summaries, titles,
            evaluation rationales, data collection rationales). If not set, the
            language will be inferred from the conversation. Must be one of the
            supported conversation languages.
        auto_translate_transcript_to_app_language:
          type: boolean
          description: >-
            When enabled, a conversation transcript is automatically translated
            to the viewer's application language when they open the transcript
            page. If not set or false, transcripts are shown in their original
            language unless the viewer manually selects a translation.
        auth:
          $ref: '#/components/schemas/type_:AuthSettings'
          description: Settings for authentication
        call_limits:
          $ref: '#/components/schemas/type_:AgentCallLimits'
          description: Call limits for the agent
        privacy:
          $ref: '#/components/schemas/type_:PrivacyConfigOutput'
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
        sentiment_analysis:
          $ref: '#/components/schemas/type_:SentimentAnalysisSettings'
          description: Per-agent post-call sentiment analysis configuration
        safety:
          $ref: '#/components/schemas/type_:SafetyResponseModel'
      title: AgentPlatformSettingsResponseModel
    type_:PhoneNumberAgentInfo:
      type: object
      properties:
        agent_id:
          type: string
          description: The ID of the agent
        agent_name:
          type: string
          description: The name of the agent
        environment:
          type: string
          description: >-
            Environment to use for resolving environment variables on calls to
            this number.
        branch_id:
          type: string
          description: Agent branch to use for calls to this number.
      required:
        - agent_id
        - agent_name
      title: PhoneNumberAgentInfo
    type_:SipTrunkTransportEnum:
      type: string
      enum:
        - auto
        - udp
        - tcp
        - tls
      default: auto
      title: SipTrunkTransportEnum
    type_:SipMediaEncryptionEnum:
      type: string
      enum:
        - disabled
        - allowed
        - required
      default: allowed
      title: SipMediaEncryptionEnum
    type_:MediaCodec:
      type: string
      enum:
        - G722/8000
        - PCMU/8000
        - PCMA/8000
      title: MediaCodec
    type_:GetPhoneNumberOutboundSipTrunkConfigResponseModel:
      type: object
      properties:
        address:
          type: string
          description: Hostname or IP the SIP INVITE is sent to
        transport:
          $ref: '#/components/schemas/type_:SipTrunkTransportEnum'
          description: Protocol to use for SIP transport
        media_encryption:
          $ref: '#/components/schemas/type_:SipMediaEncryptionEnum'
          description: Whether or not to encrypt media (data layer).
        headers:
          type: object
          additionalProperties:
            type: string
          description: SIP headers for INVITE request
        attributes_to_headers:
          type: object
          additionalProperties:
            type: string
          description: >-
            Map of dynamic variable name to header name for
            attributes_to_headers
        has_auth_credentials:
          type: boolean
          description: Whether authentication credentials are configured
        username:
          type: string
          description: SIP trunk username (if available)
        has_outbound_trunk:
          type: boolean
          default: false
          description: Whether a LiveKit SIP outbound trunk is configured
        enabled_codecs:
          type: array
          items:
            $ref: '#/components/schemas/type_:MediaCodec'
          description: >-
            Media codecs that are offered in the SDP for outbound calls. If
            empty, all supported codecs are offered.
      required:
        - address
        - transport
        - media_encryption
        - has_auth_credentials
      description: SIP Trunk configuration details for a phone number
      title: GetPhoneNumberOutboundSipTrunkConfigResponseModel
    type_:GetPhoneNumberInboundSipTrunkConfigResponseModel:
      type: object
      properties:
        allowed_addresses:
          type: array
          items:
            type: string
          description: >-
            List of IP addresses that are allowed to use the trunk. Each item in
            the list can be an individual IP address or a Classless Inter-Domain
            Routing notation representing a CIDR block.
        allowed_numbers:
          type: array
          items:
            type: string
          description: List of phone numbers that are allowed to use the trunk.
        media_encryption:
          $ref: '#/components/schemas/type_:SipMediaEncryptionEnum'
        has_auth_credentials:
          type: boolean
          description: Whether authentication credentials are configured
        username:
          type: string
          description: SIP trunk username (if available)
        remote_domains:
          type: array
          items:
            type: string
          description: Domains of remote SIP servers used to validate TLS certificates.
        attributes_to_headers:
          type: object
          additionalProperties:
            type: string
          description: >-
            Map of dynamic variable name to header name for
            attributes_to_headers
      required:
        - allowed_addresses
        - media_encryption
        - has_auth_credentials
      title: GetPhoneNumberInboundSipTrunkConfigResponseModel
    type_:LivekitStackType:
      type: string
      enum:
        - standard
        - static
      default: standard
      title: LivekitStackType
    type_:MergePreviewResponseModelPhoneNumbersItem:
      oneOf:
        - type: object
          properties:
            provider:
              type: string
              enum:
                - exotel
              description: 'Discriminator value: exotel'
            phone_number:
              type: string
              description: Phone number
            label:
              type: string
              description: Label for the phone number
            supports_inbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports inbound calls
            supports_outbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports outbound calls
            phone_number_id:
              type: string
              description: The ID of the phone number
            assigned_agent:
              $ref: '#/components/schemas/type_:PhoneNumberAgentInfo'
              description: The agent that is assigned to the phone number
          required:
            - provider
            - phone_number
            - label
            - phone_number_id
        - type: object
          properties:
            provider:
              type: string
              enum:
                - sip_trunk
              description: 'Discriminator value: sip_trunk'
            phone_number:
              type: string
              description: Phone number
            label:
              type: string
              description: Label for the phone number
            supports_inbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports inbound calls
            supports_outbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports outbound calls
            phone_number_id:
              type: string
              description: The ID of the phone number
            assigned_agent:
              $ref: '#/components/schemas/type_:PhoneNumberAgentInfo'
              description: The agent that is assigned to the phone number
            provider_config:
              $ref: >-
                #/components/schemas/type_:GetPhoneNumberOutboundSipTrunkConfigResponseModel
            outbound_trunk:
              $ref: >-
                #/components/schemas/type_:GetPhoneNumberOutboundSipTrunkConfigResponseModel
              description: Configuration of the Outbound SIP trunk - if configured.
            inbound_trunk:
              $ref: >-
                #/components/schemas/type_:GetPhoneNumberInboundSipTrunkConfigResponseModel
              description: Configuration of the Inbound SIP trunk - if configured.
            livekit_stack:
              $ref: '#/components/schemas/type_:LivekitStackType'
              description: Type of Livekit stack used for this number.
            store_sip_messages:
              type: boolean
              default: true
              description: Whether to store SIP messages for this phone number.
          required:
            - provider
            - phone_number
            - label
            - phone_number_id
            - livekit_stack
        - type: object
          properties:
            provider:
              type: string
              enum:
                - twilio
              description: 'Discriminator value: twilio'
            phone_number:
              type: string
              description: Phone number
            label:
              type: string
              description: Label for the phone number
            supports_inbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports inbound calls
            supports_outbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports outbound calls
            phone_number_id:
              type: string
              description: The ID of the phone number
            assigned_agent:
              $ref: '#/components/schemas/type_:PhoneNumberAgentInfo'
              description: The agent that is assigned to the phone number
          required:
            - provider
            - phone_number
            - label
            - phone_number_id
      discriminator:
        propertyName: provider
      title: MergePreviewResponseModelPhoneNumbersItem
    type_:GetWhatsAppAccountResponse:
      type: object
      properties:
        business_account_id:
          type: string
        phone_number_id:
          type: string
        business_account_name:
          type: string
        phone_number_name:
          type: string
        phone_number:
          type: string
        assigned_agent_id:
          type: string
        enable_messaging:
          type: boolean
          default: true
        enable_audio_message_response:
          type: boolean
          default: true
        enable_typing_indicator:
          type: boolean
          default: true
        assigned_agent_name:
          type: string
        is_token_expired:
          type: boolean
          default: false
      required:
        - business_account_id
        - phone_number_id
        - business_account_name
        - phone_number_name
        - phone_number
      title: GetWhatsAppAccountResponse
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
    type_:AstNodeOutput:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - add_operator
              description: 'Discriminator value: add_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
                $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Condition deciding which expression should be selected.
            trueExpression:
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Expression selected if the condition is true.
            falseExpression:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
            value_schema:
              $ref: '#/components/schemas/type_:LlmLiteralJsonSchemaProperty'
              description: JSON schema describing the value that the LLM should extract.
            prompt:
              type: string
              description: >-
                The prompt to evaluate to a boolean value. Deprecated. Use a
                boolean schema instead.
          required:
            - type
            - value_schema
            - prompt
        - type: object
          properties:
            type:
              type: string
              enum:
                - lt_operator
              description: 'Discriminator value: lt_operator'
            left:
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
                $ref: '#/components/schemas/type_:AstNodeOutput'
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Left operand of the binary operator.
            right:
              $ref: '#/components/schemas/type_:AstNodeOutput'
              description: Right operand of the binary operator.
          required:
            - type
            - left
            - right
      discriminator:
        propertyName: type
      title: AstNodeOutput
    type_:WorkflowEdgeModelOutputForwardCondition:
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
      title: WorkflowEdgeModelOutputForwardCondition
    type_:WorkflowEdgeModelOutputBackwardCondition:
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
              $ref: '#/components/schemas/type_:AstNodeOutput'
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
      title: WorkflowEdgeModelOutputBackwardCondition
    type_:WorkflowEdgeModelOutput:
      type: object
      properties:
        source:
          type: string
          description: ID of the source node.
        target:
          type: string
          description: ID of the target node.
        forward_condition:
          $ref: '#/components/schemas/type_:WorkflowEdgeModelOutputForwardCondition'
          description: >-
            Condition that must be met for the edge to be traversed in the
            forward direction (source to target).
        backward_condition:
          $ref: '#/components/schemas/type_:WorkflowEdgeModelOutputBackwardCondition'
          description: >-
            Condition that must be met for the edge to be traversed in the
            backward direction (target to source).
      required:
        - source
        - target
      title: WorkflowEdgeModelOutput
    type_:PositionOutput:
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
      required:
        - x
        - 'y'
      title: PositionOutput
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
        interruption_ignore_term_languages:
          type: array
          items:
            type: string
          description: >-
            Language codes for which preset ignore-term categories have been
            activated. Stored explicitly so display is not inferred from term
            overlap.
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
    type_:TtsConversationalConfigWorkflowOverrideOutput:
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
          description: 'Deprecated: this field is a no-op and is ignored.'
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
      title: TtsConversationalConfigWorkflowOverrideOutput
    type_:FileInputConfigWorkflowOverride:
      type: object
      properties:
        enabled:
          type: boolean
          description: >-
            When enabled, users may attach images or PDFs in chat when the LLM
            supports multimodal input.
        max_files_in_memory:
          type: integer
          description: >-
            Number of most-recent files kept in memory during a conversation.
            Older files are summarized and their bytes freed.
        max_files_per_conversation:
          type: integer
          description: >-
            Total files a user can upload in one conversation. Uploads are
            billed per file. Use -1 for no limit, or a value >=
            max_files_in_memory.
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
    type_:ConversationConfigWorkflowOverrideOutput:
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
      title: ConversationConfigWorkflowOverrideOutput
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
    type_:BuiltInToolsWorkflowOverrideOutput:
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
      title: BuiltInToolsWorkflowOverrideOutput
    type_:RagConfigWorkflowOverrideOutput:
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
      title: RagConfigWorkflowOverrideOutput
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
    type_:PromptAgentApiModelWorkflowOverrideOutputBackupLlmConfig:
      oneOf:
        - $ref: '#/components/schemas/type_:BackupLlmDefault'
        - $ref: '#/components/schemas/type_:BackupLlmDisabled'
        - $ref: '#/components/schemas/type_:BackupLlmOverride'
      description: >-
        Configuration for backup LLM cascading. Can be disabled, use system
        defaults, or specify custom order.
      title: PromptAgentApiModelWorkflowOverrideOutputBackupLlmConfig
    type_:PromptAgentApiModelWorkflowOverrideOutputToolsItem:
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
      title: PromptAgentApiModelWorkflowOverrideOutputToolsItem
    type_:PromptAgentApiModelWorkflowOverrideOutput:
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
          $ref: '#/components/schemas/type_:BuiltInToolsWorkflowOverrideOutput'
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
          $ref: '#/components/schemas/type_:RagConfigWorkflowOverrideOutput'
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
            #/components/schemas/type_:PromptAgentApiModelWorkflowOverrideOutputBackupLlmConfig
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
              #/components/schemas/type_:PromptAgentApiModelWorkflowOverrideOutputToolsItem
          description: >-
            A list of tools that the agent can use over the course of the
            conversation, use tool_ids instead
      title: PromptAgentApiModelWorkflowOverrideOutput
    type_:AgentConfigApiModelWorkflowOverrideOutput:
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
          $ref: '#/components/schemas/type_:PromptAgentApiModelWorkflowOverrideOutput'
          description: The prompt for the agent
      title: AgentConfigApiModelWorkflowOverrideOutput
    type_:ConversationalConfigApiModelWorkflowOverrideOutput:
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
            #/components/schemas/type_:TtsConversationalConfigWorkflowOverrideOutput
          description: Configuration for conversational text to speech
        conversation:
          $ref: '#/components/schemas/type_:ConversationConfigWorkflowOverrideOutput'
          description: Configuration for conversational events
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:LanguagePresetOutput'
          description: Language presets for conversations
        vad:
          $ref: '#/components/schemas/type_:VadConfigWorkflowOverride'
          description: Configuration for voice activity detection
        agent:
          $ref: '#/components/schemas/type_:AgentConfigApiModelWorkflowOverrideOutput'
          description: Agent specific configuration
      title: ConversationalConfigApiModelWorkflowOverrideOutput
    type_:EntryBehavior:
      type: string
      enum:
        - generate_immediately
        - wait_for_user
        - auto
      default: auto
      title: EntryBehavior
    type_:WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem:
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
      title: WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem
    type_:WorkflowPhoneNumberNodeModelOutputTransferDestination:
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
      title: WorkflowPhoneNumberNodeModelOutputTransferDestination
    type_:WorkflowPhoneNumberNodeModelOutputPostDialDigits:
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
      title: WorkflowPhoneNumberNodeModelOutputPostDialDigits
    type_:WorkflowToolLocator:
      type: object
      properties:
        tool_id:
          type: string
      required:
        - tool_id
      title: WorkflowToolLocator
    type_:AgentWorkflowResponseModelNodesValue:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - end
              description: 'Discriminator value: end'
            position:
              $ref: '#/components/schemas/type_:PositionOutput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
            - position
            - edge_order
        - type: object
          properties:
            type:
              type: string
              enum:
                - override_agent
              description: 'Discriminator value: override_agent'
            position:
              $ref: '#/components/schemas/type_:PositionOutput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
            conversation_config:
              $ref: >-
                #/components/schemas/type_:ConversationalConfigApiModelWorkflowOverrideOutput
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
            - position
            - edge_order
            - conversation_config
            - additional_prompt
            - additional_knowledge_base
            - additional_tool_ids
            - label
            - entry_behavior
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
                  #/components/schemas/type_:WorkflowPhoneNumberNodeModelOutputCustomSipHeadersItem
              description: >-
                Custom SIP headers to include when transferring the call. Each
                header can be either a static value or a dynamic variable
                reference.
            transfer_destination:
              $ref: >-
                #/components/schemas/type_:WorkflowPhoneNumberNodeModelOutputTransferDestination
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
                #/components/schemas/type_:WorkflowPhoneNumberNodeModelOutputPostDialDigits
              description: >-
                DTMF digits to send after call connects (e.g., 'ww1234' for
                extension). Can be either a static value or a dynamic variable
                reference. Use 'w' for 0.5s pause. Only supported for Twilio
                transfers.
            position:
              $ref: '#/components/schemas/type_:PositionOutput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
            - custom_sip_headers
            - transfer_destination
            - transfer_type
            - position
            - edge_order
        - type: object
          properties:
            type:
              type: string
              enum:
                - standalone_agent
              description: 'Discriminator value: standalone_agent'
            position:
              $ref: '#/components/schemas/type_:PositionOutput'
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
            - position
            - edge_order
            - delay_ms
            - enable_transferred_agent_first_message
            - preserve_client_tts_overrides
        - type: object
          properties:
            type:
              type: string
              enum:
                - start
              description: 'Discriminator value: start'
            position:
              $ref: '#/components/schemas/type_:PositionOutput'
              description: Position of the node in the workflow.
            edge_order:
              type: array
              items:
                type: string
              description: The ids of outgoing edges in the order they should be evaluated.
          required:
            - type
            - position
            - edge_order
        - type: object
          properties:
            type:
              type: string
              enum:
                - tool
              description: 'Discriminator value: tool'
            position:
              $ref: '#/components/schemas/type_:PositionOutput'
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
            - position
            - edge_order
            - tools
      discriminator:
        propertyName: type
      title: AgentWorkflowResponseModelNodesValue
    type_:AgentWorkflowResponseModel:
      type: object
      properties:
        edges:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:WorkflowEdgeModelOutput'
        nodes:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:AgentWorkflowResponseModelNodesValue'
        prevent_subagent_loops:
          type: boolean
          default: false
          description: Whether to prevent loops in the workflow execution.
      required:
        - edges
        - nodes
        - prevent_subagent_loops
      title: AgentWorkflowResponseModel
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
    type_:ConflictSection:
      type: string
      enum:
        - conversation_config
        - platform_settings
        - procedures
        - workflow
      title: ConflictSection
    type_:FieldConflict:
      type: object
      properties:
        path:
          type: string
          description: >-
            Identifier of the conflicting field relative to its section: a
            dot-path within conversation_config/platform_settings, or a
            procedure id.
        section:
          $ref: '#/components/schemas/type_:ConflictSection'
          description: Which config section this path belongs to.
        base_value:
          description: Value at the common ancestor (merge base).
        source_value:
          description: Value on the source branch tip.
        target_value:
          description: Value on the target branch tip.
      required:
        - path
        - section
      title: FieldConflict
    type_:MergePreviewResponseModel:
      type: object
      properties:
        agent_id:
          type: string
          description: The ID of the agent
        name:
          type: string
          description: The name of the agent
        conversation_config:
          $ref: '#/components/schemas/type_:ConversationalConfig'
          description: The conversation configuration of the agent
        metadata:
          $ref: '#/components/schemas/type_:AgentMetadataResponseModel'
          description: The metadata of the agent
        platform_settings:
          $ref: '#/components/schemas/type_:AgentPlatformSettingsResponseModel'
          description: The platform settings of the agent
        phone_numbers:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:MergePreviewResponseModelPhoneNumbersItem
          description: The phone numbers of the agent
        whatsapp_accounts:
          type: array
          items:
            $ref: '#/components/schemas/type_:GetWhatsAppAccountResponse'
          description: WhatsApp accounts assigned to the agent
        workflow:
          $ref: '#/components/schemas/type_:AgentWorkflowResponseModel'
          description: The workflow of the agent
        access_info:
          $ref: '#/components/schemas/type_:ResourceAccessInfo'
          description: The access information of the agent for the user
        tags:
          type: array
          items:
            type: string
          description: Agent tags used to categorize the agent
        version_id:
          type: string
          description: The ID of the version the agent is on
        branch_id:
          type: string
          description: The ID of the branch the agent is on
        main_branch_id:
          type: string
          description: The ID of the main branch for this agent
        overridden_fields:
          type: array
          items:
            type: string
          description: >-
            Dot-paths of config fields where both branches modified the same
            field relative to their common ancestor (conflicts). Present
            regardless of which side wins the conflict.
        conflicts:
          type: array
          items:
            $ref: '#/components/schemas/type_:FieldConflict'
          description: >-
            Structured view of the same conflicts as overridden_fields, each
            carrying the value on the base (common ancestor), source branch, and
            target branch so the divergence can be presented and resolved
            field-by-field.
        source_identical_to_target:
          type: boolean
          default: false
          description: >-
            True when the merge/rebase would be a no-op, i.e. the merged result
            is identical to the source branch tip. The rebase endpoint rejects
            in this case.
      required:
        - agent_id
        - name
        - conversation_config
        - metadata
      title: MergePreviewResponseModel
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

**Response**

```json
{
  "agent_id": "agent_7101k5zvyjhmfg983brhmhkd98n6",
  "name": "My Agent",
  "conversation_config": {
    "asr": {
      "quality": "high",
      "provider": "scribe_realtime",
      "user_input_audio_format": "pcm_16000",
      "keywords": [
        "hello",
        "world"
      ]
    },
    "turn": {
      "turn_timeout": 7,
      "initial_wait_time": 1.1,
      "silence_end_call_timeout": -1,
      "turn_eagerness": "normal",
      "spelling_patience": "auto",
      "speculative_turn": false,
      "retranscribe_on_turn_timeout": false,
      "turn_model": "turn_v3",
      "interruption_ignore_terms": [
        "interruption_ignore_terms"
      ],
      "interruption_ignore_term_languages": [
        "interruption_ignore_term_languages"
      ],
      "transcribe_on_disabled_interruptions": false,
      "soft_timeout_config": {
        "timeout_seconds": -1,
        "message": "Hhmmmm...yeah."
      }
    },
    "tts": {
      "model_id": "eleven_turbo_v2",
      "voice_id": "cjVigY5qzO86Huf0OWal",
      "supported_voices": [
        {
          "label": "label",
          "voice_id": "voice_id"
        }
      ],
      "expressive_mode": true,
      "suggested_audio_tags": [
        {
          "tag": "tag"
        }
      ],
      "agent_output_audio_format": "pcm_16000",
      "optimize_streaming_latency": 3,
      "stability": 0.5,
      "speed": 1,
      "similarity_boost": 0.8,
      "text_normalisation_type": "system_prompt",
      "pronunciation_dictionary_locators": [
        {
          "pronunciation_dictionary_id": "pronunciation_dictionary_id",
          "version_id": null
        }
      ],
      "enable_phoneme_tags": true
    },
    "conversation": {
      "text_only": true,
      "max_duration_seconds": 600,
      "client_events": [
        "audio",
        "interruption"
      ],
      "monitoring_enabled": true,
      "monitoring_events": [
        "conversation_initiation_metadata"
      ],
      "source_attribution": true
    },
    "language_presets": {
      "key": {
        "overrides": {
          "asr": {
            "keywords": [
              "hello",
              "world"
            ]
          },
          "turn": {
            "soft_timeout_config": {
              "message": "Hhmmmm...yeah."
            }
          },
          "tts": {
            "model_id": "eleven_turbo_v2",
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "stability": 0.5,
            "speed": 1,
            "similarity_boost": 0.8
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "tool_ids": [
                "tool_ids"
              ],
              "knowledge_base": [
                {
                  "type": "file",
                  "name": "My Knowledge Base",
                  "id": "123",
                  "usage_mode": "auto"
                }
              ]
            }
          }
        }
      }
    },
    "agent": {
      "first_message": "Hello, how can I help you today?",
      "language": "en",
      "hinglish_mode": true,
      "disable_first_message_interruptions": false,
      "max_conversation_duration_message": "max_conversation_duration_message",
      "prompt": {
        "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
        "llm": "gemini-2.0-flash-001",
        "temperature": 0,
        "max_tokens": -1,
        "tool_ids": [
          "tool_ids"
        ],
        "built_in_tools": {
          "end_call": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "language_detection": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "transfer_to_agent": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "transfer_to_number": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "skip_turn": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "play_keypad_touch_tone": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
            "assignments": [
              {
                "dynamic_variable": "user_name",
                "value_path": "user.name",
                "source": "response",
                "sanitize": false,
                "preserve_native_type": false
              }
            ]
          },
          "voicemail_detection": {
            "name": "end_call",
            "params": {
              "system_tool_type": "end_call"
            },
            "type": "system",
            "description": "",
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
        },
        "knowledge_base": [
          {
            "type": "file",
            "name": "My Knowledge Base",
            "id": "123",
            "usage_mode": "auto"
          }
        ],
        "rag": {
          "max_vector_distance": 0.5,
          "max_retrieved_rag_chunks_count": 5
        }
      }
    }
  },
  "metadata": {
    "created_at_unix_secs": 1,
    "updated_at_unix_secs": 1
  },
  "platform_settings": {
    "evaluation": {
      "criteria": [
        {
          "id": "criterion_binary_001",
          "name": "Issue resolved",
          "conversation_goal_prompt": "Determine whether the agent fully resolved the user's issue.",
          "use_knowledge_base": false,
          "scope": "conversation",
          "scoring_mode": "binary",
          "max_score": 100
        }
      ]
    },
    "widget": {
      "variant": "tiny",
      "placement": "top-left",
      "expandable": "never",
      "avatar": {
        "type": "orb",
        "color_1": "#2792dc",
        "color_2": "#9ce6e6"
      },
      "feedback_mode": "none",
      "bg_color": "bg_color",
      "text_color": "text_color",
      "btn_color": "btn_color",
      "btn_text_color": "btn_text_color",
      "border_color": "border_color",
      "focus_color": "focus_color",
      "border_radius": 1,
      "btn_radius": 1,
      "action_text": "action_text",
      "start_call_text": "start_call_text",
      "end_call_text": "end_call_text",
      "expand_text": "expand_text",
      "listening_text": "listening_text",
      "speaking_text": "speaking_text",
      "shareable_page_text": "shareable_page_text",
      "shareable_page_show_terms": true,
      "terms_text": "terms_text",
      "terms_html": "terms_html",
      "terms_key": "terms_key",
      "show_avatar_when_collapsed": true,
      "disable_banner": true,
      "override_link": "override_link",
      "markdown_link_allowed_hosts": [
        {
          "hostname": "hostname"
        }
      ],
      "markdown_link_include_www": true,
      "markdown_link_allow_http": true,
      "mic_muting_enabled": true,
      "transcript_enabled": true,
      "text_input_enabled": true,
      "conversation_mode_toggle_enabled": true,
      "default_expanded": true,
      "always_expanded": true,
      "dismissible": true,
      "show_agent_status": true,
      "show_conversation_id": true,
      "strip_audio_tags": true,
      "syntax_highlight_theme": "light",
      "show_resize_button": true,
      "language_selector": false,
      "supports_text_only": true,
      "custom_avatar_path": "https://example.com/avatar.png",
      "language_presets": {
        "key": {}
      }
    },
    "data_collection": {
      "key": {
        "type": "string",
        "description": "My property",
        "is_system_provided": false,
        "dynamic_variable": "",
        "constant_value": ""
      }
    },
    "data_collection_scopes": {
      "key": "conversation"
    },
    "analysis_items": {
      "evaluation_criteria": [
        {
          "source": "system",
          "analysis_item_id": "__system_eval_criteria_sentiment"
        }
      ],
      "data_collection": [
        {
          "source": "system",
          "analysis_item_id": "__system_data_collection_topic"
        }
      ]
    },
    "overrides": {
      "custom_llm_extra_body": true,
      "enable_conversation_initiation_client_data_from_webhook": true,
      "enable_starting_workflow_node_id_from_client": true
    },
    "workspace_overrides": {
      "conversation_initiation_client_data_webhook": {
        "url": "https://example.com/webhook",
        "request_headers": {
          "Content-Type": "application/json"
        }
      }
    },
    "testing": {
      "attached_tests": [
        {
          "test_id": "test_123",
          "workflow_node_id": "node_abc"
        },
        {
          "test_id": "test_456"
        }
      ]
    },
    "archived": true,
    "guardrails": {
      "version": "1"
    },
    "summary_language": "summary_language",
    "auto_translate_transcript_to_app_language": true,
    "auth": {
      "enable_auth": true,
      "allowlist": [
        {
          "hostname": "https://example.com"
        }
      ],
      "require_origin_header": true,
      "shareable_token": "1234567890"
    },
    "call_limits": {
      "agent_concurrency_limit": -1,
      "daily_limit": 100000,
      "bursting_enabled": true
    },
    "privacy": {
      "record_voice": true,
      "retention_days": -1,
      "delete_transcript_and_pii": false,
      "delete_audio": false,
      "apply_to_existing_conversations": false,
      "zero_retention_mode": false
    },
    "trust_context": "unknown",
    "analysis_llm": "gpt-4o-mini",
    "safety": {
      "is_blocked_ivc": true,
      "is_blocked_non_ivc": true,
      "ignore_safety_evaluation": true
    }
  },
  "phone_numbers": [
    {
      "provider": "exotel",
      "label": "Exotel Outbound",
      "phone_number": "+919999999999",
      "phone_number_id": "phnum_X3Pbu5gP6NNKBscdCdwB",
      "assigned_agent": {
        "agent_id": "F3Pbu5gP6NNKBscdCdwB",
        "agent_name": "My Agent"
      }
    }
  ],
  "whatsapp_accounts": [
    {
      "business_account_id": "business_account_id",
      "phone_number_id": "phone_number_id",
      "business_account_name": "business_account_name",
      "phone_number_name": "phone_number_name",
      "phone_number": "phone_number",
      "assigned_agent_id": "assigned_agent_id",
      "enable_messaging": true,
      "enable_audio_message_response": true,
      "enable_typing_indicator": true,
      "assigned_agent_name": "assigned_agent_name",
      "is_token_expired": true
    }
  ],
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "type": "llm",
          "condition": "User's last message contains a question about our pricing.",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {
          "type": "unconditional",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "type": "result",
          "successful": true,
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "type": "result",
          "successful": true,
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {
          "type": "unconditional",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "type": "llm",
          "condition": "User's last message contains a question about our pricing.",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      },
      "tool_b_to_end": {
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": {
          "type": "llm",
          "condition": "User's last message contains a question about our pricing.",
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
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
          },
          "label": null
        },
        "backward_condition": {
          "type": "expression",
          "expression": {
            "type": "and_operator",
            "children": []
          },
          "label": null
        }
      }
    },
    "nodes": {
      "entry_node": {
        "type": "override_agent",
        "additional_knowledge_base": [
          {
            "type": "file",
            "name": "My Knowledge Base",
            "id": "123",
            "usage_mode": "auto"
          }
        ],
        "additional_prompt": "additional_prompt",
        "additional_tool_ids": [
          "additional_tool_ids"
        ],
        "conversation_config": {
          "asr": {
            "quality": "high",
            "provider": "scribe_realtime",
            "user_input_audio_format": "pcm_16000",
            "keywords": [
              "hello",
              "world"
            ]
          },
          "turn": {
            "turn_timeout": 7,
            "silence_end_call_timeout": -1,
            "turn_eagerness": "normal",
            "spelling_patience": "auto",
            "speculative_turn": false,
            "retranscribe_on_turn_timeout": false,
            "turn_model": "turn_v3",
            "interruption_ignore_terms": [
              "interruption_ignore_terms"
            ],
            "interruption_ignore_term_languages": [
              "interruption_ignore_term_languages"
            ],
            "transcribe_on_disabled_interruptions": false,
            "soft_timeout_config": {
              "timeout_seconds": -1,
              "message": "Hhmmmm...yeah.",
              "use_llm_generated_message": false
            }
          },
          "tts": {
            "model_id": "eleven_turbo_v2",
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "agent_output_audio_format": "pcm_16000",
            "optimize_streaming_latency": 3,
            "stability": 0.5,
            "speed": 1,
            "similarity_boost": 0.8,
            "pronunciation_dictionary_locators": [
              {
                "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                "version_id": null
              }
            ]
          },
          "conversation": {
            "max_duration_seconds": 600,
            "client_events": [
              "audio",
              "interruption"
            ]
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "dynamic_variables": {
              "dynamic_variable_placeholders": {
                "user_name": "John Doe"
              }
            },
            "disable_first_message_interruptions": false,
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "temperature": 0,
              "max_tokens": -1,
              "tool_ids": [
                "tool_ids"
              ],
              "built_in_tools": {
                "end_call": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "language_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_agent": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_number": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "skip_turn": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "play_keypad_touch_tone": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "voicemail_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
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
              },
              "knowledge_base": [
                {
                  "type": "file",
                  "name": "My Knowledge Base",
                  "id": "123",
                  "usage_mode": "auto"
                }
              ],
              "tools": [
                {
                  "type": "api_integration_webhook",
                  "api_integration_connection_id": "api_integration_connection_id",
                  "api_integration_id": "api_integration_id",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ],
                  "description": "description",
                  "dynamic_variables": {
                    "dynamic_variable_placeholders": {
                      "user_name": "John Doe"
                    }
                  },
                  "execution_mode": "immediate",
                  "interruption_mode": "allow",
                  "name": "name",
                  "pre_tool_speech": "auto",
                  "response_timeout_secs": 1,
                  "tool_call_sound_behavior": "auto",
                  "tool_error_handling_mode": "auto",
                  "tool_version": "tool_version",
                  "disable_interruptions": true,
                  "force_pre_tool_speech": true,
                  "api_schema_overrides": null,
                  "tool_call_sound": null
                }
              ]
            }
          }
        },
        "edge_order": [
          "edge_order"
        ],
        "entry_behavior": "generate_immediately",
        "label": "label",
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "failure_node": {
        "type": "override_agent",
        "additional_knowledge_base": [
          {
            "type": "file",
            "name": "My Knowledge Base",
            "id": "123",
            "usage_mode": "auto"
          }
        ],
        "additional_prompt": "additional_prompt",
        "additional_tool_ids": [
          "additional_tool_ids"
        ],
        "conversation_config": {
          "asr": {
            "quality": "high",
            "provider": "scribe_realtime",
            "user_input_audio_format": "pcm_16000",
            "keywords": [
              "hello",
              "world"
            ]
          },
          "turn": {
            "turn_timeout": 7,
            "silence_end_call_timeout": -1,
            "turn_eagerness": "normal",
            "spelling_patience": "auto",
            "speculative_turn": false,
            "retranscribe_on_turn_timeout": false,
            "turn_model": "turn_v3",
            "interruption_ignore_terms": [
              "interruption_ignore_terms"
            ],
            "interruption_ignore_term_languages": [
              "interruption_ignore_term_languages"
            ],
            "transcribe_on_disabled_interruptions": false,
            "soft_timeout_config": {
              "timeout_seconds": -1,
              "message": "Hhmmmm...yeah.",
              "use_llm_generated_message": false
            }
          },
          "tts": {
            "model_id": "eleven_turbo_v2",
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "agent_output_audio_format": "pcm_16000",
            "optimize_streaming_latency": 3,
            "stability": 0.5,
            "speed": 1,
            "similarity_boost": 0.8,
            "pronunciation_dictionary_locators": [
              {
                "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                "version_id": null
              }
            ]
          },
          "conversation": {
            "max_duration_seconds": 600,
            "client_events": [
              "audio",
              "interruption"
            ]
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "dynamic_variables": {
              "dynamic_variable_placeholders": {
                "user_name": "John Doe"
              }
            },
            "disable_first_message_interruptions": false,
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "temperature": 0,
              "max_tokens": -1,
              "tool_ids": [
                "tool_ids"
              ],
              "built_in_tools": {
                "end_call": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "language_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_agent": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_number": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "skip_turn": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "play_keypad_touch_tone": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "voicemail_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
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
              },
              "knowledge_base": [
                {
                  "type": "file",
                  "name": "My Knowledge Base",
                  "id": "123",
                  "usage_mode": "auto"
                }
              ],
              "tools": [
                {
                  "type": "api_integration_webhook",
                  "api_integration_connection_id": "api_integration_connection_id",
                  "api_integration_id": "api_integration_id",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ],
                  "description": "description",
                  "dynamic_variables": {
                    "dynamic_variable_placeholders": {
                      "user_name": "John Doe"
                    }
                  },
                  "execution_mode": "immediate",
                  "interruption_mode": "allow",
                  "name": "name",
                  "pre_tool_speech": "auto",
                  "response_timeout_secs": 1,
                  "tool_call_sound_behavior": "auto",
                  "tool_error_handling_mode": "auto",
                  "tool_version": "tool_version",
                  "disable_interruptions": true,
                  "force_pre_tool_speech": true,
                  "api_schema_overrides": null,
                  "tool_call_sound": null
                }
              ]
            }
          }
        },
        "edge_order": [
          "edge_order"
        ],
        "entry_behavior": "generate_immediately",
        "label": "label",
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "start_node": {
        "type": "start",
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "success_conversation": {
        "type": "override_agent",
        "additional_knowledge_base": [
          {
            "type": "file",
            "name": "My Knowledge Base",
            "id": "123",
            "usage_mode": "auto"
          }
        ],
        "additional_prompt": "additional_prompt",
        "additional_tool_ids": [
          "additional_tool_ids"
        ],
        "conversation_config": {
          "asr": {
            "quality": "high",
            "provider": "scribe_realtime",
            "user_input_audio_format": "pcm_16000",
            "keywords": [
              "hello",
              "world"
            ]
          },
          "turn": {
            "turn_timeout": 7,
            "silence_end_call_timeout": -1,
            "turn_eagerness": "normal",
            "spelling_patience": "auto",
            "speculative_turn": false,
            "retranscribe_on_turn_timeout": false,
            "turn_model": "turn_v3",
            "interruption_ignore_terms": [
              "interruption_ignore_terms"
            ],
            "interruption_ignore_term_languages": [
              "interruption_ignore_term_languages"
            ],
            "transcribe_on_disabled_interruptions": false,
            "soft_timeout_config": {
              "timeout_seconds": -1,
              "message": "Hhmmmm...yeah.",
              "use_llm_generated_message": false
            }
          },
          "tts": {
            "model_id": "eleven_turbo_v2",
            "voice_id": "cjVigY5qzO86Huf0OWal",
            "agent_output_audio_format": "pcm_16000",
            "optimize_streaming_latency": 3,
            "stability": 0.5,
            "speed": 1,
            "similarity_boost": 0.8,
            "pronunciation_dictionary_locators": [
              {
                "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                "version_id": null
              }
            ]
          },
          "conversation": {
            "max_duration_seconds": 600,
            "client_events": [
              "audio",
              "interruption"
            ]
          },
          "agent": {
            "first_message": "Hello, how can I help you today?",
            "language": "en",
            "dynamic_variables": {
              "dynamic_variable_placeholders": {
                "user_name": "John Doe"
              }
            },
            "disable_first_message_interruptions": false,
            "prompt": {
              "prompt": "You are a helpful assistant that can answer questions about the topic of the conversation.",
              "llm": "gemini-2.0-flash-001",
              "temperature": 0,
              "max_tokens": -1,
              "tool_ids": [
                "tool_ids"
              ],
              "built_in_tools": {
                "end_call": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "language_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_agent": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "transfer_to_number": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "skip_turn": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "play_keypad_touch_tone": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ]
                },
                "voicemail_detection": {
                  "name": "end_call",
                  "params": {
                    "system_tool_type": "end_call"
                  },
                  "type": "system",
                  "description": "",
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
              },
              "knowledge_base": [
                {
                  "type": "file",
                  "name": "My Knowledge Base",
                  "id": "123",
                  "usage_mode": "auto"
                }
              ],
              "tools": [
                {
                  "type": "api_integration_webhook",
                  "api_integration_connection_id": "api_integration_connection_id",
                  "api_integration_id": "api_integration_id",
                  "assignments": [
                    {
                      "dynamic_variable": "user_name",
                      "value_path": "user.name",
                      "source": "response",
                      "sanitize": false,
                      "preserve_native_type": false
                    }
                  ],
                  "description": "description",
                  "dynamic_variables": {
                    "dynamic_variable_placeholders": {
                      "user_name": "John Doe"
                    }
                  },
                  "execution_mode": "immediate",
                  "interruption_mode": "allow",
                  "name": "name",
                  "pre_tool_speech": "auto",
                  "response_timeout_secs": 1,
                  "tool_call_sound_behavior": "auto",
                  "tool_error_handling_mode": "auto",
                  "tool_version": "tool_version",
                  "disable_interruptions": true,
                  "force_pre_tool_speech": true,
                  "api_schema_overrides": null,
                  "tool_call_sound": null
                }
              ]
            }
          }
        },
        "edge_order": [
          "edge_order"
        ],
        "entry_behavior": "generate_immediately",
        "label": "label",
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "success_end": {
        "type": "end",
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        }
      },
      "success_phone": {
        "type": "phone_number",
        "custom_sip_headers": [
          {
            "type": "dynamic",
            "key": "key",
            "value": "value"
          }
        ],
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        },
        "transfer_destination": {
          "type": "phone",
          "phone_number": "phone_number"
        },
        "transfer_type": "blind",
        "post_dial_digits": null,
        "uui": null
      },
      "success_transfer": {
        "type": "standalone_agent",
        "delay_ms": 1,
        "edge_order": [
          "edge_order"
        ],
        "enable_transferred_agent_first_message": true,
        "position": {
          "x": 1.1,
          "y": 1.1
        },
        "preserve_client_tts_overrides": true,
        "agent_id": null,
        "node_id": null,
        "transfer_message": null
      },
      "tool_node_a": {
        "type": "tool",
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        },
        "tools": [
          {
            "tool_id": "tool_id"
          }
        ]
      },
      "tool_node_b": {
        "type": "tool",
        "edge_order": [
          "edge_order"
        ],
        "position": {
          "x": 1.1,
          "y": 1.1
        },
        "tools": [
          {
            "tool_id": "tool_id"
          }
        ]
      }
    },
    "prevent_subagent_loops": false
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "anonymous_access_level_override": "admin",
    "access_source": "creator"
  },
  "tags": [
    "tags"
  ],
  "version_id": "version_id",
  "branch_id": "branch_id",
  "main_branch_id": "main_branch_id",
  "overridden_fields": [
    "overridden_fields"
  ],
  "conflicts": [
    {
      "path": "path",
      "section": "conversation_config",
      "base_value": {
        "key": "value"
      },
      "source_value": {
        "key": "value"
      },
      "target_value": {
        "key": "value"
      }
    }
  ],
  "source_identical_to_target": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.previewRebase("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtbrch_8901k4t9z5defmb8vh3e9361y7nj");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.preview_rebase(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbrch_8901k4t9z5defmb8vh3e9361y7nj/rebase-preview")! as URL,
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
