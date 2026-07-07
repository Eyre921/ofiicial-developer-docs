---
title: "Update Speech Engine"
source: https://elevenlabs.io/docs/api-reference/speech-engine/update.md
path: docs/api-reference/speech-engine/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update Speech Engine

PATCH https://api.elevenlabs.io/v1/speech-engine/{speech_engine_id}
Content-Type: application/json

Update a Speech Engine resource (partial update)

Reference: https://elevenlabs.io/docs/api-reference/speech-engine/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/speech-engine/{speech_engine_id}:
    patch:
      operationId: update
      summary: Update Speech Engine
      description: Update a Speech Engine resource (partial update)
      tags:
        - speechEngine
      parameters:
        - name: speech_engine_id
          in: path
          description: The speech engine ID (accepts seng_ or agent_ prefix)
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
                $ref: '#/components/schemas/SpeechEngineResponse'
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
              $ref: '#/components/schemas/UpdateSpeechEngineRequest'
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
    SpeechEngineConfigRequestHeaders:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ConvAISecretLocator'
        - $ref: '#/components/schemas/ConvAIDynamicVariable'
      title: SpeechEngineConfigRequestHeaders
    SpeechEngineConfig:
      type: object
      properties:
        ws_url:
          type: string
          description: The WebSocket URL for the transcript server
        request_headers:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/SpeechEngineConfigRequestHeaders'
          description: Headers to include in the WebSocket connection request
      required:
        - ws_url
      title: SpeechEngineConfig
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
    ASRConversationalConfig:
      type: object
      properties:
        quality:
          $ref: '#/components/schemas/ASRQuality'
          default: high
          description: The quality of the transcription
        provider:
          $ref: '#/components/schemas/ASRProvider'
          default: scribe_realtime
          description: The provider of the transcription service
        user_input_audio_format:
          $ref: '#/components/schemas/ASRInputFormat'
          default: pcm_16000
          description: The format of the audio to be transcribed
        keywords:
          type: array
          items:
            type: string
          description: Keywords to boost prediction probability for
      title: ASRConversationalConfig
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
    TTSConversationalConfig-Input:
      type: object
      properties:
        model_id:
          $ref: '#/components/schemas/TTSConversationalModel'
          default: eleven_flash_v2
          description: The model to use for TTS
        voice_id:
          type: string
          default: cjVigY5qzO86Huf0OWal
          description: The voice ID to use for TTS
        supported_voices:
          type: array
          items:
            $ref: '#/components/schemas/SupportedVoice'
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
            $ref: '#/components/schemas/SuggestedAudioTag'
          description: >-
            Suggested audio tags to boost expressive speech (for eleven_v3 and
            eleven_v3_conversational models). The agent can still use other tags
            not listed here.
        agent_output_audio_format:
          $ref: '#/components/schemas/TTSOutputFormat'
          default: pcm_16000
          description: The audio format to use for TTS
        optimize_streaming_latency:
          $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
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
          $ref: '#/components/schemas/TextNormalisationType'
          default: system_prompt
          description: >-
            Method for converting numbers to words before converting text to
            speech. If set to SYSTEM_PROMPT, the system prompt will be updated
            to include normalization instructions. If set to ELEVENLABS, the
            text will be normalized after generation, incurring slight
            additional latency.
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PydanticPronunciationDictionaryVersionLocator'
          description: The pronunciation dictionary locators
        enable_phoneme_tags:
          type: boolean
          default: false
          description: >-
            Opt-in to SSML phoneme tag handling for V3 models. When enabled,
            phoneme tags (inline and from pronunciation dictionaries) are parsed
            into inline IPA before being sent to the model.
      title: TTSConversationalConfig-Input
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
    BaseTurnConfig:
      type: object
      properties:
        turn_timeout:
          type: number
          format: double
          default: 7
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
          type: number
          format: double
          default: -1
          description: >-
            Maximum wait time since the user last spoke before terminating the
            call
        turn_eagerness:
          $ref: '#/components/schemas/TurnEagerness'
          default: normal
          description: >-
            Controls how eager the agent is to respond. Low = less eager (waits
            longer), Standard = default eagerness, High = more eager (responds
            sooner)
        spelling_patience:
          $ref: '#/components/schemas/SpellingPatience'
          default: auto
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
          $ref: '#/components/schemas/TurnModel'
          default: turn_v3
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
      title: BaseTurnConfig
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
    FileInputConfig:
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
    BackgroundSoundConfig:
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
    ConversationConfig-Input:
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
            $ref: '#/components/schemas/ClientEvent'
          description: The events that will be sent to the client
        file_input:
          $ref: '#/components/schemas/FileInputConfig'
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
            $ref: '#/components/schemas/ClientEvent'
          description: The events that will be sent to monitoring connections.
        background_sound:
          $ref: '#/components/schemas/BackgroundSoundConfig'
          description: Configuration for background sound during conversations.
        source_attribution:
          type: boolean
          default: false
          description: >-
            When enabled and knowledge base content is present, the LLM is
            instructed to report which sources it used.
      title: ConversationConfig-Input
    ConfigEntityType:
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
    ConversationHistoryRedactionConfig:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
          description: Whether conversation history redaction is enabled
        entities:
          type: array
          items:
            $ref: '#/components/schemas/ConfigEntityType'
          description: >-
            The entities to redact from the conversation transcript, audio and
            analysis. Use top-level types like 'name', 'email_address', or dot
            notation for specific subtypes like 'name.full_name'.
      title: ConversationHistoryRedactionConfig
    PrivacyConfig-Input:
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
          $ref: '#/components/schemas/ConversationHistoryRedactionConfig'
          description: Config for PII redaction in the conversation history
      title: PrivacyConfig-Input
    AgentCallLimits:
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
    SpeechEngineConversationInitiationClientDataConfig:
      type: object
      properties:
        first_message:
          type: boolean
          default: false
          description: Whether the first message can be overridden by the client
      title: SpeechEngineConversationInitiationClientDataConfig
    UpdateSpeechEngineRequest:
      type: object
      properties:
        name:
          type:
            - string
            - 'null'
        speech_engine:
          oneOf:
            - $ref: '#/components/schemas/SpeechEngineConfig'
            - type: 'null'
        asr:
          oneOf:
            - $ref: '#/components/schemas/ASRConversationalConfig'
            - type: 'null'
        tts:
          oneOf:
            - $ref: '#/components/schemas/TTSConversationalConfig-Input'
            - type: 'null'
        turn:
          oneOf:
            - $ref: '#/components/schemas/BaseTurnConfig'
            - type: 'null'
        conversation:
          oneOf:
            - $ref: '#/components/schemas/ConversationConfig-Input'
            - type: 'null'
        privacy:
          oneOf:
            - $ref: '#/components/schemas/PrivacyConfig-Input'
            - type: 'null'
        call_limits:
          oneOf:
            - $ref: '#/components/schemas/AgentCallLimits'
            - type: 'null'
        language:
          type:
            - string
            - 'null'
        tags:
          type:
            - array
            - 'null'
          items:
            type: string
        overrides:
          oneOf:
            - $ref: >-
                #/components/schemas/SpeechEngineConversationInitiationClientDataConfig
            - type: 'null'
      title: UpdateSpeechEngineRequest
    TTSConversationalConfig-Output:
      type: object
      properties:
        model_id:
          $ref: '#/components/schemas/TTSConversationalModel'
          default: eleven_flash_v2
          description: The model to use for TTS
        voice_id:
          type: string
          default: cjVigY5qzO86Huf0OWal
          description: The voice ID to use for TTS
        supported_voices:
          type: array
          items:
            $ref: '#/components/schemas/SupportedVoice'
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
            $ref: '#/components/schemas/SuggestedAudioTag'
          description: >-
            Suggested audio tags to boost expressive speech (for eleven_v3 and
            eleven_v3_conversational models). The agent can still use other tags
            not listed here.
        agent_output_audio_format:
          $ref: '#/components/schemas/TTSOutputFormat'
          default: pcm_16000
          description: The audio format to use for TTS
        optimize_streaming_latency:
          $ref: '#/components/schemas/TTSOptimizeStreamingLatency'
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
          $ref: '#/components/schemas/TextNormalisationType'
          default: system_prompt
          description: >-
            Method for converting numbers to words before converting text to
            speech. If set to SYSTEM_PROMPT, the system prompt will be updated
            to include normalization instructions. If set to ELEVENLABS, the
            text will be normalized after generation, incurring slight
            additional latency.
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PydanticPronunciationDictionaryVersionLocator'
          description: The pronunciation dictionary locators
        enable_phoneme_tags:
          type: boolean
          default: false
          description: >-
            Opt-in to SSML phoneme tag handling for V3 models. When enabled,
            phoneme tags (inline and from pronunciation dictionaries) are parsed
            into inline IPA before being sent to the model.
      title: TTSConversationalConfig-Output
    ConversationConfig-Output:
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
            $ref: '#/components/schemas/ClientEvent'
          description: The events that will be sent to the client
        file_input:
          $ref: '#/components/schemas/FileInputConfig'
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
            $ref: '#/components/schemas/ClientEvent'
          description: The events that will be sent to monitoring connections.
        background_sound:
          $ref: '#/components/schemas/BackgroundSoundConfig'
          description: Configuration for background sound during conversations.
        source_attribution:
          type: boolean
          default: false
          description: >-
            When enabled and knowledge base content is present, the LLM is
            instructed to report which sources it used.
      title: ConversationConfig-Output
    PrivacyConfig-Output:
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
          $ref: '#/components/schemas/ConversationHistoryRedactionConfig'
          description: Config for PII redaction in the conversation history
      title: PrivacyConfig-Output
    AgentDefinitionSource:
      type: string
      enum:
        - cli
        - ui
        - api
        - template
        - unknown
      default: unknown
      title: AgentDefinitionSource
    AgentMetadataDBModel:
      type: object
      properties:
        created_at_unix_secs:
          type: integer
        updated_at_unix_secs:
          type: integer
        created_from:
          $ref: '#/components/schemas/AgentDefinitionSource'
          default: unknown
        last_updated_from:
          $ref: '#/components/schemas/AgentDefinitionSource'
          default: unknown
      required:
        - created_at_unix_secs
        - updated_at_unix_secs
      title: AgentMetadataDBModel
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
    SpeechEngineResponse:
      type: object
      properties:
        speech_engine_id:
          type: string
          description: The speech engine resource ID
        name:
          type: string
          description: Human-readable name for the speech engine
        speech_engine:
          $ref: '#/components/schemas/SpeechEngineConfig'
          description: WebSocket connection settings for the upstream transcript server
        asr:
          $ref: '#/components/schemas/ASRConversationalConfig'
          description: Automatic speech recognition configuration
        tts:
          $ref: '#/components/schemas/TTSConversationalConfig-Output'
          description: Text-to-speech output configuration
        turn:
          $ref: '#/components/schemas/BaseTurnConfig'
          description: Turn detection configuration
        conversation:
          $ref: '#/components/schemas/ConversationConfig-Output'
          description: >-
            Conversation-level settings including client events and duration
            limits
        privacy:
          $ref: '#/components/schemas/PrivacyConfig-Output'
          description: Privacy settings controlling recording, retention, and PII handling
        call_limits:
          $ref: '#/components/schemas/AgentCallLimits'
          description: Concurrency and daily conversation limits for this speech engine
        language:
          type: string
          description: ISO language code used by the speech engine (e.g. 'en')
        tags:
          type: array
          items:
            type: string
          description: Arbitrary tags for categorization and filtering
        overrides:
          $ref: >-
            #/components/schemas/SpeechEngineConversationInitiationClientDataConfig
          description: Override settings the client may set during conversation initiation
        metadata:
          $ref: '#/components/schemas/AgentMetadataDBModel'
          description: Creation and update timestamps with source information
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
          description: The access information of the speech engine for the user
      required:
        - speech_engine_id
        - name
        - speech_engine
        - asr
        - tts
        - turn
        - conversation
        - privacy
        - call_limits
        - language
        - tags
        - overrides
        - metadata
      title: SpeechEngineResponse
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
{}
```

**Response**

```json
{
  "speech_engine_id": "seng_3701k3ttaq12ewp8b7qv5rfyszkz",
  "name": "My Speech Engine",
  "speech_engine": {
    "ws_url": "wss://example.com/transcript",
    "request_headers": {}
  },
  "asr": {
    "quality": "high",
    "provider": "elevenlabs",
    "user_input_audio_format": "pcm_16000",
    "keywords": []
  },
  "tts": {
    "model_id": "eleven_flash_v2",
    "voice_id": "cjVigY5qzO86Huf0OWal",
    "agent_output_audio_format": "pcm_16000",
    "optimize_streaming_latency": 3,
    "stability": 0.5,
    "speed": 1,
    "similarity_boost": 0.8
  },
  "turn": {
    "turn_timeout": 7,
    "silence_end_call_timeout": -1,
    "turn_eagerness": "normal",
    "mode": "turn"
  },
  "conversation": {
    "max_duration_seconds": 600,
    "client_events": [
      "audio",
      "interruption",
      "agent_response",
      "user_transcript"
    ]
  },
  "privacy": {
    "record_voice": true,
    "retention_days": -1,
    "delete_transcript_and_pii": false,
    "delete_audio": false,
    "apply_to_existing_conversations": false,
    "zero_retention_mode": false
  },
  "call_limits": {
    "agent_concurrency_limit": -1,
    "daily_limit": 100000,
    "bursting_enabled": true
  },
  "language": "en",
  "tags": [
    "production",
    "v1"
  ],
  "overrides": {
    "first_message": false
  },
  "metadata": {
    "created_at_unix_secs": 1714000000,
    "updated_at_unix_secs": 1714000000,
    "created_from": "api",
    "last_updated_from": "api"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.speechEngine.update("speech_engine_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.speech_engine.update(
    speech_engine_id="speech_engine_id",
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

	url := "https://api.elevenlabs.io/v1/speech-engine/speech_engine_id"

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

url = URI("https://api.elevenlabs.io/v1/speech-engine/speech_engine_id")

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

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/speech-engine/speech_engine_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/speech-engine/speech_engine_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/speech-engine/speech_engine_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-engine/speech_engine_id")! as URL,
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
