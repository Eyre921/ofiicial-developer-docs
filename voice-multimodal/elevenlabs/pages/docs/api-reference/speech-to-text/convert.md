---
title: "Create transcript"
source: https://elevenlabs.io/docs/api-reference/speech-to-text/convert.md
path: docs/api-reference/speech-to-text/convert
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create transcript

POST https://api.elevenlabs.io/v1/speech-to-text
Content-Type: multipart/form-data

Transcribe an audio or video file. If webhook is set to true, the request will be processed asynchronously and results sent to configured webhooks. When use_multi_channel is true and the provided audio has multiple channels, a 'transcripts' object with separate transcripts for each channel is returned; set multichannel_output_style='combined' to instead receive a single transcript with all channels merged and sorted by time. Otherwise, returns a single transcript. The optional webhook_metadata parameter allows you to attach custom data that will be included in webhook responses for request correlation and tracking.

Reference: https://elevenlabs.io/docs/api-reference/speech-to-text/convert

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/speech-to-text:
    post:
      operationId: convert
      summary: Create transcript
      description: >-
        Transcribe an audio or video file. If webhook is set to true, the
        request will be processed asynchronously and results sent to configured
        webhooks. When use_multi_channel is true and the provided audio has
        multiple channels, a 'transcripts' object with separate transcripts for
        each channel is returned; set multichannel_output_style='combined' to
        instead receive a single transcript with all channels merged and sorted
        by time. Otherwise, returns a single transcript. The optional
        webhook_metadata parameter allows you to attach custom data that will be
        included in webhook responses for request correlation and tracking.
      tags:
        - speechToText
      parameters:
        - name: enable_logging
          in: query
          description: >-
            When enable_logging is set to false zero retention mode will be used
            for the request. This will mean log and transcript storage features
            are unavailable for this request. Zero retention mode may only be
            used by enterprise customers.
          required: false
          schema:
            type: boolean
            default: true
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Synchronous transcription result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/speech_to_text_convert_Response_200'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                model_id:
                  $ref: >-
                    #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaModelId
                  description: The ID of the model to use for transcription.
                file:
                  type: string
                  format: binary
                  description: >-
                    The file to transcribe (100ms minimum audio length). All
                    major audio and video formats are supported. Exactly one of
                    the file or cloud_storage_url parameters must be provided.
                    The file size must be less than 5.0GB.
                language_code:
                  type:
                    - string
                    - 'null'
                  description: >-
                    An ISO-639-1 or ISO-639-3 language_code corresponding to the
                    language of the audio file. Can sometimes improve
                    transcription performance if known beforehand. Defaults to
                    null, in this case the language is predicted automatically.
                tag_audio_events:
                  type: boolean
                  default: true
                  description: >-
                    Whether to tag audio events like (laughter), (footsteps),
                    etc. in the transcription.
                num_speakers:
                  type:
                    - integer
                    - 'null'
                  description: >-
                    The maximum amount of speakers talking in the uploaded file.
                    Can help with predicting who speaks when. The maximum amount
                    of speakers that can be predicted is 32. Defaults to null,
                    in this case the amount of speakers is set to the maximum
                    value the model supports.
                timestamps_granularity:
                  $ref: >-
                    #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaTimestampsGranularity
                  default: word
                  description: >-
                    The granularity of the timestamps in the transcription.
                    'word' provides word-level timestamps and 'character'
                    provides character-level timestamps per word.
                diarize:
                  type: boolean
                  default: false
                  description: >-
                    Whether to annotate which speaker is currently talking in
                    the uploaded file.
                diarization_threshold:
                  type:
                    - number
                    - 'null'
                  format: double
                  description: >-
                    Diarization threshold to apply during speaker diarization. A
                    higher value means there will be a lower chance of one
                    speaker being diarized as two different speakers but also a
                    higher chance of two different speakers being diarized as
                    one speaker (less total speakers predicted). A low value
                    means there will be a higher chance of one speaker being
                    diarized as two different speakers but also a lower chance
                    of two different speakers being diarized as one speaker
                    (more total speakers predicted). Can only be set when
                    diarize=True and num_speakers=None. Defaults to None, in
                    which case we will choose a threshold based on the model_id
                    (0.22 usually).
                additional_formats:
                  $ref: '#/components/schemas/AdditionalFormats'
                  description: A list of additional formats to export the transcript to.
                file_format:
                  $ref: >-
                    #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaFileFormat
                  default: other
                  description: >-
                    The format of input audio. Options are 'pcm_s16le_16' or
                    'other' For `pcm_s16le_16`, the input audio must be 16-bit
                    PCM at a 16kHz sample rate, single channel (mono), and
                    little-endian byte order. Latency will be lower than with
                    passing an encoded waveform.
                cloud_storage_url:
                  type:
                    - string
                    - 'null'
                  description: >-
                    [Deprecated] This parameter is deprecated and will be
                    removed in the future. Use 'source_url' instead.The HTTPS
                    URL of the file to transcribe. Exactly one of the file or
                    cloud_storage_url parameters must be provided. The file must
                    be accessible via HTTPS and the file size must be less than
                    2GB. Any valid HTTPS URL is accepted, including URLs from
                    cloud storage providers (AWS S3, Google Cloud Storage,
                    Cloudflare R2, etc.), CDNs, or any other HTTPS source. URLs
                    can be pre-signed or include authentication tokens in query
                    parameters.
                source_url:
                  type:
                    - string
                    - 'null'
                  description: >-
                    The URL of an audio or video file to transcribe. Supports
                    hosted video or audio files, YouTube video URLs, TikTok
                    video URLs, and other video hosting services.
                webhook:
                  type: boolean
                  default: false
                  description: >-
                    Whether to send the transcription result to configured
                    speech-to-text webhooks.  If set the request will return
                    early without the transcription, which will be delivered
                    later via webhook.
                webhook_id:
                  type:
                    - string
                    - 'null'
                  description: >-
                    Optional specific webhook ID to send the transcription
                    result to. Only valid when webhook is set to true. If not
                    provided, transcription will be sent to all configured
                    speech-to-text webhooks.
                temperature:
                  type:
                    - number
                    - 'null'
                  format: double
                  description: >-
                    Controls the randomness of the transcription output. Accepts
                    values between 0.0 and 2.0, where higher values result in
                    more diverse and less deterministic results. If omitted, we
                    will use a temperature based on the model you selected which
                    is usually 0.
                seed:
                  type:
                    - integer
                    - 'null'
                  description: >-
                    If specified, our system will make a best effort to sample
                    deterministically, such that repeated requests with the same
                    seed and parameters should return the same result.
                    Determinism is not guaranteed. Must be an integer between 0
                    and 2147483647.
                use_multi_channel:
                  type: boolean
                  default: false
                  description: >-
                    Whether the audio file contains multiple channels where each
                    channel contains a single speaker. When enabled, each
                    channel is transcribed independently. By default a separate
                    transcript is returned per channel; set
                    multichannel_output_style='combined' to instead receive a
                    single transcript with all channels merged and sorted by
                    time. Each word in the response includes a 'channel_index'
                    field indicating which channel it was spoken on. A maximum
                    of 5 channels is supported. Each channel is billed
                    independently at the full audio duration, so cost scales
                    linearly with the number of channels.
                multichannel_output_style:
                  $ref: >-
                    #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaMultichannelOutputStyle
                  default: separate
                  description: >-
                    Controls the response shape when use_multi_channel is
                    enabled. 'separate' (default) returns one transcript per
                    channel under 'transcripts'. 'combined' merges all channels
                    into a single transcript whose words are sorted by start
                    time, each carrying a 'channel_index' - matching the
                    single-channel response shape. 'combined' requires
                    timestamps (timestamps_granularity must not be 'none') and
                    does not support entity detection or redaction.
                webhook_metadata:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaWebhookMetadata
                    - type: 'null'
                  description: >-
                    Optional metadata to be included in the webhook response.
                    This should be a JSON string representing an object with a
                    maximum depth of 2 levels and maximum size of 16KB. Useful
                    for tracking internal IDs, job references, or other
                    contextual information.
                entity_detection:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaEntityDetection
                    - type: 'null'
                  description: >-
                    Detect entities in the transcript. Can be 'all' to detect
                    all entities, a single entity type or category string, or a
                    list of entity types/categories. Categories include 'pii',
                    'phi', 'pci', 'other', 'offensive_language'. When enabled,
                    detected entities will be returned in the 'entities' field
                    with their text, type, and character positions. Usage of
                    this parameter will incur an additional 30% surcharge on the
                    base transcription cost.
                no_verbatim:
                  type: boolean
                  default: false
                  description: >-
                    If true, the transcription will not have any filler words,
                    false starts and non-speech sounds. Only supported with
                    scribe_v2 model.
                use_speaker_library:
                  type: boolean
                  default: false
                  description: >-
                    Whether to use the speaker library for identifying known
                    speakers during diarization. When enabled and diarize is
                    true, detected speakers will be matched against registered
                    speakers in the workspace's speaker library.
                detect_speaker_roles:
                  type: boolean
                  default: false
                  description: >-
                    Whether to detect speaker roles (agent vs customer).
                    Requires diarize=true. Cannot be used with
                    use_multi_channel=true. When enabled, speaker_id values will
                    be 'agent' and 'customer' instead of 'speaker_0',
                    'speaker_1', etc. Usage incurs an additional 10% surcharge
                    on base transcription cost.
                entity_redaction:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaEntityRedaction
                    - type: 'null'
                  description: >-
                    Redact entities from the transcript text. Accepts the same
                    format as entity_detection: 'all', a category ('pii',
                    'phi'), or specific entity types. Must be a subset of
                    entity_detection. When redaction is enabled, the entities
                    field will not be returned. Usage of this parameter will
                    incur an additional 30% surcharge on the base transcription
                    cost.
                entity_redaction_mode:
                  type: string
                  default: enumerated_entity_type
                  description: >-
                    How to format redacted entities. 'redacted' replaces with
                    {REDACTED}, 'entity_type' replaces with {ENTITY_TYPE},
                    'enumerated_entity_type' replaces with {ENTITY_TYPE_N} where
                    N enumerates each occurrence. Only used when
                    entity_redaction is set.
                keyterms:
                  type: array
                  items:
                    type: string
                  default: []
                  description: >-
                    A list of keyterms to bias the transcription
                    towards.           The keyterms are words or phrases you
                    want the model to recognise more accurately.           The
                    number of keyterms cannot exceed 1000.           The length
                    of each keyterm must be less than 50 characters.          
                    Keyterms can contain at most 5 words (after
                    normalisation).           For example ["hello", "world",
                    "technical term"].           The following characters are
                    not supported: `<`, `>`, `{`, `}`, `[`, `]`, `\`.          
                    Usage of this parameter will incur an additional 20%
                    surcharge on the base transcription cost.           When
                    more than 100 keyterms are provided, a minimum billable
                    duration of 20 seconds applies per request.
              required:
                - model_id
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
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaModelId:
      type: string
      enum:
        - scribe_v2
        - scribe_v1
      description: The ID of the model to use for transcription.
      title: V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaModelId
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaTimestampsGranularity:
      type: string
      enum:
        - none
        - word
        - character
      default: word
      description: >-
        The granularity of the timestamps in the transcription. 'word' provides
        word-level timestamps and 'character' provides character-level
        timestamps per word.
      title: >-
        V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaTimestampsGranularity
    ExportOptions:
      oneOf:
        - type: object
          properties:
            format:
              type: string
              enum:
                - docx
              description: 'Discriminator value: docx'
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_duration_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_chars:
              type:
                - integer
                - 'null'
          required:
            - format
          description: DocxExportOptions variant
        - type: object
          properties:
            format:
              type: string
              enum:
                - html
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_duration_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_chars:
              type:
                - integer
                - 'null'
          required:
            - format
          description: HtmlExportOptions variant
        - type: object
          properties:
            format:
              type: string
              enum:
                - pdf
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_duration_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_chars:
              type:
                - integer
                - 'null'
          required:
            - format
          description: PdfExportOptions variant
        - type: object
          properties:
            format:
              type: string
              enum:
                - segmented_json
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_duration_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_chars:
              type:
                - integer
                - 'null'
          required:
            - format
          description: SegmentedJsonExportOptions variant
        - type: object
          properties:
            format:
              type: string
              enum:
                - srt
            max_characters_per_line:
              type:
                - integer
                - 'null'
              default: 42
            include_speakers:
              type: boolean
              default: false
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type:
                - number
                - 'null'
              format: double
              default: 0.8
            max_segment_duration_s:
              type:
                - number
                - 'null'
              format: double
              default: 4
            max_segment_chars:
              type:
                - integer
                - 'null'
              default: 84
          required:
            - format
          description: SrtExportOptions variant
        - type: object
          properties:
            format:
              type: string
              enum:
                - txt
            max_characters_per_line:
              type:
                - integer
                - 'null'
              default: 100
            include_speakers:
              type: boolean
              default: true
            include_timestamps:
              type: boolean
              default: true
            segment_on_silence_longer_than_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_duration_s:
              type:
                - number
                - 'null'
              format: double
            max_segment_chars:
              type:
                - integer
                - 'null'
          required:
            - format
          description: TxtExportOptions variant
      discriminator:
        propertyName: format
      title: ExportOptions
    AdditionalFormats:
      type: array
      items:
        $ref: '#/components/schemas/ExportOptions'
      title: AdditionalFormats
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaFileFormat:
      type: string
      enum:
        - pcm_s16le_16
        - other
      default: other
      description: >-
        The format of input audio. Options are 'pcm_s16le_16' or 'other' For
        `pcm_s16le_16`, the input audio must be 16-bit PCM at a 16kHz sample
        rate, single channel (mono), and little-endian byte order. Latency will
        be lower than with passing an encoded waveform.
      title: V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaFileFormat
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaMultichannelOutputStyle:
      type: string
      enum:
        - separate
        - combined
      default: separate
      description: >-
        Controls the response shape when use_multi_channel is enabled.
        'separate' (default) returns one transcript per channel under
        'transcripts'. 'combined' merges all channels into a single transcript
        whose words are sorted by start time, each carrying a 'channel_index' -
        matching the single-channel response shape. 'combined' requires
        timestamps (timestamps_granularity must not be 'none') and does not
        support entity detection or redaction.
      title: >-
        V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaMultichannelOutputStyle
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaWebhookMetadata:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      description: >-
        Optional metadata to be included in the webhook response. This should be
        a JSON string representing an object with a maximum depth of 2 levels
        and maximum size of 16KB. Useful for tracking internal IDs, job
        references, or other contextual information.
      title: >-
        V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaWebhookMetadata
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaEntityDetection:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      description: >-
        Detect entities in the transcript. Can be 'all' to detect all entities,
        a single entity type or category string, or a list of entity
        types/categories. Categories include 'pii', 'phi', 'pci', 'other',
        'offensive_language'. When enabled, detected entities will be returned
        in the 'entities' field with their text, type, and character positions.
        Usage of this parameter will incur an additional 30% surcharge on the
        base transcription cost.
      title: >-
        V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaEntityDetection
    V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaEntityRedaction:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      description: >-
        Redact entities from the transcript text. Accepts the same format as
        entity_detection: 'all', a category ('pii', 'phi'), or specific entity
        types. Must be a subset of entity_detection. When redaction is enabled,
        the entities field will not be returned. Usage of this parameter will
        incur an additional 30% surcharge on the base transcription cost.
      title: >-
        V1SpeechToTextPostRequestBodyContentMultipartFormDataSchemaEntityRedaction
    SpeechToTextWordResponseModelType:
      type: string
      enum:
        - word
        - spacing
        - audio_event
      description: >-
        The type of the word or sound. 'audio_event' is used for non-word sounds
        like laughter or footsteps.
      title: SpeechToTextWordResponseModelType
    SpeechToTextCharacterResponseModel:
      type: object
      properties:
        text:
          type: string
          description: The character that was transcribed.
        start:
          type:
            - number
            - 'null'
          format: double
          description: The start time of the character in seconds.
        end:
          type:
            - number
            - 'null'
          format: double
          description: The end time of the character in seconds.
      required:
        - text
      title: SpeechToTextCharacterResponseModel
    SpeechToTextWordResponseModel:
      type: object
      properties:
        text:
          type: string
          description: The word or sound that was transcribed.
        start:
          type:
            - number
            - 'null'
          format: double
          description: The start time of the word or sound in seconds.
        end:
          type:
            - number
            - 'null'
          format: double
          description: The end time of the word or sound in seconds.
        type:
          $ref: '#/components/schemas/SpeechToTextWordResponseModelType'
          description: >-
            The type of the word or sound. 'audio_event' is used for non-word
            sounds like laughter or footsteps.
        speaker_id:
          type:
            - string
            - 'null'
          description: Unique identifier for the speaker of this word.
        logprob:
          type: number
          format: double
          description: >-
            The log of the probability with which this word was predicted.
            Logprobs are in range [-infinity, 0], higher logprobs indicate a
            higher confidence the model has in its predictions.
        characters:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SpeechToTextCharacterResponseModel'
          description: The characters that make up the word and their timing information.
        channel_index:
          type:
            - integer
            - 'null'
          description: >-
            The channel this word was spoken on (for multichannel audio). Null
            for single-channel transcriptions.
      required:
        - text
        - type
        - logprob
      description: Word-level detail of the transcription with timing information.
      title: SpeechToTextWordResponseModel
    AdditionalFormatResponseModel:
      type: object
      properties:
        requested_format:
          type: string
          description: The requested format.
        file_extension:
          type: string
          description: The file extension of the additional format.
        content_type:
          type: string
          description: The content type of the additional format.
        is_base64_encoded:
          type: boolean
          description: Whether the content is base64 encoded.
        content:
          type: string
          description: The content of the additional format.
      required:
        - requested_format
        - file_extension
        - content_type
        - is_base64_encoded
        - content
      title: AdditionalFormatResponseModel
    DetectedEntity:
      type: object
      properties:
        text:
          type: string
          description: The text that was identified as an entity.
        entity_type:
          type: string
          description: >-
            The type of entity detected (e.g., 'credit_card', 'email_address',
            'person_name').
        start_char:
          type: integer
          description: Start character position in the transcript text.
        end_char:
          type: integer
          description: End character position in the transcript text.
      required:
        - text
        - entity_type
        - start_char
        - end_char
      title: DetectedEntity
    SpeechToTextChunkResponseModel:
      type: object
      properties:
        language_code:
          type: string
          description: The detected language code (e.g. 'eng' for English).
        language_probability:
          type: number
          format: double
          description: The confidence score of the language detection (0 to 1).
        text:
          type: string
          description: The raw text of the transcription.
        words:
          type: array
          items:
            $ref: '#/components/schemas/SpeechToTextWordResponseModel'
          description: List of words with their timing information.
        channel_index:
          type:
            - integer
            - 'null'
          description: >-
            The channel index this transcript belongs to (for multichannel
            audio).
        additional_formats:
          type:
            - array
            - 'null'
          items:
            oneOf:
              - $ref: '#/components/schemas/AdditionalFormatResponseModel'
              - type: 'null'
          description: Requested additional formats of the transcript.
        transcription_id:
          type:
            - string
            - 'null'
          description: The transcription ID of the response.
        entities:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/DetectedEntity'
          description: >-
            List of detected entities with their text, type, and character
            positions in the transcript.
        audio_duration_secs:
          type:
            - number
            - 'null'
          format: double
          description: The duration of the audio that was transcribed in seconds.
      required:
        - language_code
        - language_probability
        - text
        - words
      description: Chunk-level detail of the transcription with timing information.
      title: SpeechToTextChunkResponseModel
    MultichannelSpeechToTextResponseModel:
      type: object
      properties:
        transcripts:
          type: array
          items:
            $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
          description: >-
            List of transcripts, one for each audio channel. Each transcript
            contains the text and word-level details for its respective channel.
        transcription_id:
          type:
            - string
            - 'null'
          description: The transcription ID of the response.
        audio_duration_secs:
          type:
            - number
            - 'null'
          format: double
          description: >-
            The duration of the audio that was transcribed across all channels
            in seconds.
      required:
        - transcripts
      description: Response model for multichannel speech-to-text transcription.
      title: MultichannelSpeechToTextResponseModel
    SpeechToTextWebhookResponseModel:
      type: object
      properties:
        message:
          type: string
          description: The message of the webhook response.
        request_id:
          type: string
          description: The request ID of the webhook response.
        transcription_id:
          type:
            - string
            - 'null'
          description: The transcription ID of the webhook response.
      required:
        - message
        - request_id
      title: SpeechToTextWebhookResponseModel
    speech_to_text_convert_Response_200:
      oneOf:
        - $ref: '#/components/schemas/SpeechToTextChunkResponseModel'
        - $ref: '#/components/schemas/MultichannelSpeechToTextResponseModel'
        - $ref: '#/components/schemas/SpeechToTextWebhookResponseModel'
      title: speech_to_text_convert_Response_200
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

### Single channel response



**Request**

```json
{
  "file": "<file: <file1>>",
  "model_id": "scribe_v2"
}
```

**Response**

```json
{
  "language_code": "en",
  "language_probability": 0.98,
  "text": "Hello world!",
  "words": [
    {
      "end": 0.5,
      "logprob": -0.124,
      "speaker_id": "speaker_1",
      "start": 0,
      "text": "Hello",
      "type": "word"
    }
  ]
}
```

**SDK Code**

```typescript Single channel response
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.speechToText.convert({});
}
main();

```

```python Single channel response
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.speech_to_text.convert(
    file="example_file",
)

```

```go Single channel response
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-to-text"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Single channel response
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/speech-to-text")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java Single channel response
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-to-text")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php Single channel response
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-to-text', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'model_id',
        'contents' => 'scribe_v2'
    ]
  ]
]);

echo $response->getBody();
```

```csharp Single channel response
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Single channel response
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "additional_formats",
    "value": 
  ],
  [
    "name": "cloud_storage_url",
    "value": 
  ],
  [
    "name": "detect_speaker_roles",
    "value": 
  ],
  [
    "name": "diarization_threshold",
    "value": 
  ],
  [
    "name": "diarize",
    "value": 
  ],
  [
    "name": "entity_detection",
    "value": 
  ],
  [
    "name": "entity_redaction",
    "value": 
  ],
  [
    "name": "entity_redaction_mode",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "file_format",
    "value": 
  ],
  [
    "name": "keyterms",
    "value": 
  ],
  [
    "name": "language_code",
    "value": 
  ],
  [
    "name": "model_id",
    "value": "scribe_v2"
  ],
  [
    "name": "multichannel_output_style",
    "value": 
  ],
  [
    "name": "no_verbatim",
    "value": 
  ],
  [
    "name": "num_speakers",
    "value": 
  ],
  [
    "name": "seed",
    "value": 
  ],
  [
    "name": "source_url",
    "value": 
  ],
  [
    "name": "tag_audio_events",
    "value": 
  ],
  [
    "name": "temperature",
    "value": 
  ],
  [
    "name": "timestamps_granularity",
    "value": 
  ],
  [
    "name": "use_multi_channel",
    "value": 
  ],
  [
    "name": "use_speaker_library",
    "value": 
  ],
  [
    "name": "webhook",
    "value": 
  ],
  [
    "name": "webhook_id",
    "value": 
  ],
  [
    "name": "webhook_metadata",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text")! as URL,
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

### Multichannel response



**Request**

```json
{
  "file": "<file: <file1>>",
  "model_id": "scribe_v2"
}
```

**Response**

```json
{
  "transcripts": [
    {
      "language_code": "en",
      "language_probability": 0.98,
      "text": "Hello from channel one.",
      "words": [
        {
          "channel_index": 0,
          "end": 0.5,
          "logprob": -0.124,
          "speaker_id": "speaker_0",
          "start": 0,
          "text": "Hello",
          "type": "word"
        }
      ]
    },
    {
      "language_code": "en",
      "language_probability": 0.97,
      "text": "Greetings from channel two.",
      "words": [
        {
          "channel_index": 1,
          "end": 0.7,
          "logprob": -0.156,
          "speaker_id": "speaker_1",
          "start": 0.1,
          "text": "Greetings",
          "type": "word"
        }
      ]
    }
  ]
}
```

**SDK Code**

```typescript Multichannel response
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.speechToText.convert({});
}
main();

```

```python Multichannel response
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.speech_to_text.convert(
    file="example_file",
)

```

```go Multichannel response
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-to-text"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Multichannel response
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/speech-to-text")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java Multichannel response
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-to-text")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php Multichannel response
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-to-text', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'model_id',
        'contents' => 'scribe_v2'
    ]
  ]
]);

echo $response->getBody();
```

```csharp Multichannel response
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Multichannel response
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "additional_formats",
    "value": 
  ],
  [
    "name": "cloud_storage_url",
    "value": 
  ],
  [
    "name": "detect_speaker_roles",
    "value": 
  ],
  [
    "name": "diarization_threshold",
    "value": 
  ],
  [
    "name": "diarize",
    "value": 
  ],
  [
    "name": "entity_detection",
    "value": 
  ],
  [
    "name": "entity_redaction",
    "value": 
  ],
  [
    "name": "entity_redaction_mode",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "file_format",
    "value": 
  ],
  [
    "name": "keyterms",
    "value": 
  ],
  [
    "name": "language_code",
    "value": 
  ],
  [
    "name": "model_id",
    "value": "scribe_v2"
  ],
  [
    "name": "multichannel_output_style",
    "value": 
  ],
  [
    "name": "no_verbatim",
    "value": 
  ],
  [
    "name": "num_speakers",
    "value": 
  ],
  [
    "name": "seed",
    "value": 
  ],
  [
    "name": "source_url",
    "value": 
  ],
  [
    "name": "tag_audio_events",
    "value": 
  ],
  [
    "name": "temperature",
    "value": 
  ],
  [
    "name": "timestamps_granularity",
    "value": 
  ],
  [
    "name": "use_multi_channel",
    "value": 
  ],
  [
    "name": "use_speaker_library",
    "value": 
  ],
  [
    "name": "webhook",
    "value": 
  ],
  [
    "name": "webhook_id",
    "value": 
  ],
  [
    "name": "webhook_metadata",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text")! as URL,
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

### speech_to_text_convert_example



**Request**

```json
{
  "file": "<file: <file1>>",
  "model_id": "scribe_v2"
}
```

**Response**

```json
{
  "message": "Request accepted. Transcription result will be sent to the webhook.",
  "request_id": "abc123"
}
```

**SDK Code**

```typescript speech_to_text_convert_example
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.speechToText.convert({});
}
main();

```

```python speech_to_text_convert_example
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.speech_to_text.convert(
    file="example_file",
)

```

```go speech_to_text_convert_example
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-to-text"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby speech_to_text_convert_example
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/speech-to-text")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java speech_to_text_convert_example
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/speech-to-text")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php speech_to_text_convert_example
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/speech-to-text', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'model_id',
        'contents' => 'scribe_v2'
    ]
  ]
]);

echo $response->getBody();
```

```csharp speech_to_text_convert_example
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/speech-to-text");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"additional_formats\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"cloud_storage_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"detect_speaker_roles\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarization_threshold\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"diarize\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_detection\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"entity_redaction_mode\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_format\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"keyterms\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"multichannel_output_style\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"no_verbatim\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"num_speakers\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"seed\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"timestamps_granularity\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_multi_channel\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"use_speaker_library\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"webhook_metadata\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift speech_to_text_convert_example
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "additional_formats",
    "value": 
  ],
  [
    "name": "cloud_storage_url",
    "value": 
  ],
  [
    "name": "detect_speaker_roles",
    "value": 
  ],
  [
    "name": "diarization_threshold",
    "value": 
  ],
  [
    "name": "diarize",
    "value": 
  ],
  [
    "name": "entity_detection",
    "value": 
  ],
  [
    "name": "entity_redaction",
    "value": 
  ],
  [
    "name": "entity_redaction_mode",
    "value": 
  ],
  [
    "name": "file",
    "fileName": "<file1>"
  ],
  [
    "name": "file_format",
    "value": 
  ],
  [
    "name": "keyterms",
    "value": 
  ],
  [
    "name": "language_code",
    "value": 
  ],
  [
    "name": "model_id",
    "value": "scribe_v2"
  ],
  [
    "name": "multichannel_output_style",
    "value": 
  ],
  [
    "name": "no_verbatim",
    "value": 
  ],
  [
    "name": "num_speakers",
    "value": 
  ],
  [
    "name": "seed",
    "value": 
  ],
  [
    "name": "source_url",
    "value": 
  ],
  [
    "name": "tag_audio_events",
    "value": 
  ],
  [
    "name": "temperature",
    "value": 
  ],
  [
    "name": "timestamps_granularity",
    "value": 
  ],
  [
    "name": "use_multi_channel",
    "value": 
  ],
  [
    "name": "use_speaker_library",
    "value": 
  ],
  [
    "name": "webhook",
    "value": 
  ],
  [
    "name": "webhook_id",
    "value": 
  ],
  [
    "name": "webhook_metadata",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-to-text")! as URL,
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
