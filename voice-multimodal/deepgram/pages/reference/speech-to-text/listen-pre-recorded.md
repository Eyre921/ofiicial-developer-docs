---
title: "Pre-Recorded Audio"
source: https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded.md
path: reference/speech-to-text/listen-pre-recorded
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Pre-Recorded Audio

POST https://api.deepgram.com/v1/listen
Content-Type: application/json

Transcribe audio and video using Deepgram's speech-to-text REST API

Reference: https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Deepgram API Specification
  version: 1.0.0
paths:
  /v1/listen:
    post:
      operationId: transcribe
      summary: Transcribe and analyze pre-recorded audio and video
      description: Transcribe audio and video using Deepgram's speech-to-text REST API
      tags:
        - subpackage_listen.subpackage_listen/v1.subpackage_listen/v1/media
      parameters:
        - name: callback
          in: query
          description: URL to which we'll make the callback request
          required: false
          schema:
            type: string
        - name: callback_method
          in: query
          description: HTTP method by which the callback request will be made
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersCallbackMethod'
            default: POST
        - name: extra
          in: query
          description: >-
            Arbitrary key-value pairs that are attached to the API response for
            usage in downstream processing
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersExtra'
        - name: sentiment
          in: query
          description: Recognizes the sentiment throughout a transcript or text
          required: false
          schema:
            type: boolean
            default: false
        - name: summarize
          in: query
          description: >-
            Summarize content. For Listen API, supports string version option.
            For Read API, accepts boolean only.
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersSummarize'
        - name: tag
          in: query
          description: >-
            Label your requests for the purpose of identification during usage
            reporting
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersTag'
        - name: topics
          in: query
          description: Detect topics throughout a transcript or text
          required: false
          schema:
            type: boolean
            default: false
        - name: custom_topic
          in: query
          description: >-
            Custom topics you want the model to detect within your input audio
            or text if present Submit up to `100`.
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersCustomTopic'
        - name: custom_topic_mode
          in: query
          description: >-
            Sets how the model will interpret strings submitted to the
            `custom_topic` param. When `strict`, the model will only return
            topics submitted using the `custom_topic` param. When `extended`,
            the model will return its own detected topics in addition to those
            submitted using the `custom_topic` param
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersCustomTopicMode'
            default: extended
        - name: intents
          in: query
          description: Recognizes speaker intent throughout a transcript or text
          required: false
          schema:
            type: boolean
            default: false
        - name: custom_intent
          in: query
          description: >-
            Custom intents you want the model to detect within your input audio
            if present
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersCustomIntent'
        - name: custom_intent_mode
          in: query
          description: >-
            Sets how the model will interpret intents submitted to the
            `custom_intent` param. When `strict`, the model will only return
            intents submitted using the `custom_intent` param. When `extended`,
            the model will return its own detected intents in the
            `custom_intent` param.
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersCustomIntentMode'
            default: extended
        - name: detect_entities
          in: query
          description: Identifies and extracts key entities from content in submitted audio
          required: false
          schema:
            type: boolean
            default: false
        - name: detect_language
          in: query
          description: Identifies the dominant language spoken in submitted audio
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersDetectLanguage'
        - name: diarize
          in: query
          description: >-
            Deprecated: use `diarize_model` instead. Recognize speaker changes.
            Each word in the transcript will be assigned a speaker number
            starting at 0.
          required: false
          schema:
            type: boolean
            default: false
        - name: diarize_model
          in: query
          description: >-
            Select and enable a specific diarization model version. Specifying
            this parameter enables diarization and selects the model — you do
            not need to also set the deprecated `diarize=true` parameter. For
            batch, supported values are `latest` (currently v2), `v1`, and `v2`.
            For streaming, supported values are `latest` (currently v1) and
            `v1`; `v2` returns a validation error on streaming requests.
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersDiarizeModel'
        - name: dictation
          in: query
          description: Dictation mode for controlling formatting with dictated speech
          required: false
          schema:
            type: boolean
            default: false
        - name: encoding
          in: query
          description: Specify the expected encoding of your submitted audio
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersEncoding'
        - name: filler_words
          in: query
          description: >-
            Filler Words can help transcribe interruptions in your audio, like
            "uh" and "um"
          required: false
          schema:
            type: boolean
            default: false
        - name: keyterm
          in: query
          description: >-
            Key term prompting can boost or suppress specialized terminology and
            brands. Only compatible with Nova-3
          required: false
          schema:
            type: array
            items:
              type: string
        - name: keywords
          in: query
          description: Keywords can boost or suppress specialized terminology and brands
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersKeywords'
        - name: language
          in: query
          description: >-
            The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that
            hints at the primary spoken language. Depending on the Model and API
            endpoint you choose only certain languages are available
          required: false
          schema:
            type: string
            default: en
        - name: measurements
          in: query
          description: >-
            Spoken measurements will be converted to their corresponding
            abbreviations
          required: false
          schema:
            type: boolean
            default: false
        - name: model
          in: query
          description: AI model used to process submitted audio
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersModel'
            default: base-general
        - name: multichannel
          in: query
          description: Transcribe each audio channel independently
          required: false
          schema:
            type: boolean
            default: false
        - name: numerals
          in: query
          description: Numerals converts numbers from written format to numerical format
          required: false
          schema:
            type: boolean
            default: false
        - name: paragraphs
          in: query
          description: Splits audio into paragraphs to improve transcript readability
          required: false
          schema:
            type: boolean
            default: false
        - name: profanity_filter
          in: query
          description: >-
            Profanity Filter looks for recognized profanity and converts it to
            the nearest recognized non-profane word or removes it from the
            transcript completely
          required: false
          schema:
            type: boolean
            default: false
        - name: punctuate
          in: query
          description: Add punctuation and capitalization to the transcript
          required: false
          schema:
            type: boolean
            default: false
        - name: redact
          in: query
          description: Redaction removes sensitive information from your transcripts
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersRedact'
            default: false
        - name: replace
          in: query
          description: Search for terms or phrases in submitted audio and replaces them
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersReplace'
        - name: search
          in: query
          description: Search for terms or phrases in submitted audio
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersSearch'
        - name: smart_format
          in: query
          description: >-
            Apply formatting to transcript output. When set to true, additional
            formatting will be applied to transcripts to improve readability
          required: false
          schema:
            type: boolean
            default: false
        - name: utterances
          in: query
          description: Segments speech into meaningful semantic units
          required: false
          schema:
            type: boolean
            default: false
        - name: utt_split
          in: query
          description: >-
            Seconds to wait before detecting a pause between words in submitted
            audio
          required: false
          schema:
            type: number
            format: double
            default: 0.8
        - name: version
          in: query
          description: Version of an AI model to use
          required: false
          schema:
            $ref: '#/components/schemas/V1ListenPostParametersVersion'
            default: latest
        - name: mip_opt_out
          in: query
          description: >-
            Opts out requests from the Deepgram Model Improvement Program. Refer
            to our Docs for pricing impacts before setting this to true.
            https://dpgr.am/deepgram-mip
          required: false
          schema:
            type: boolean
            default: false
        - name: Authorization
          in: header
          description: |
            Use `Authorization: Token <API_KEY>`
            Example: `Authorization: Token 12345abcdef`
          required: true
          schema:
            type: string
      responses:
        '200':
          description: >-
            Returns either transcription results, or a request_id when using a
            callback.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/listen_v1_media_transcribe_Response_200'
        '400':
          description: Invalid Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListenV1Response'
      requestBody:
        description: Transcribe an audio or video file
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ListenV1RequestUrl'
servers:
  - url: https://api.deepgram.com
    description: Base
components:
  schemas:
    V1ListenPostParametersCallbackMethod:
      type: string
      enum:
        - POST
        - PUT
      default: POST
      title: V1ListenPostParametersCallbackMethod
    V1ListenPostParametersExtra:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ListenPostParametersExtra
    V1ListenPostParametersSummarize0:
      type: string
      enum:
        - v2
      title: V1ListenPostParametersSummarize0
    V1ListenPostParametersSummarize:
      oneOf:
        - $ref: '#/components/schemas/V1ListenPostParametersSummarize0'
        - type: boolean
          default: false
      title: V1ListenPostParametersSummarize
    V1ListenPostParametersTag:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ListenPostParametersTag
    V1ListenPostParametersCustomTopic:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ListenPostParametersCustomTopic
    V1ListenPostParametersCustomTopicMode:
      type: string
      enum:
        - extended
        - strict
      default: extended
      title: V1ListenPostParametersCustomTopicMode
    V1ListenPostParametersCustomIntent:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ListenPostParametersCustomIntent
    V1ListenPostParametersCustomIntentMode:
      type: string
      enum:
        - extended
        - strict
      default: extended
      title: V1ListenPostParametersCustomIntentMode
    V1ListenPostParametersDetectLanguage:
      oneOf:
        - type: boolean
          default: false
        - type: array
          items:
            type: string
      title: V1ListenPostParametersDetectLanguage
    V1ListenPostParametersDiarizeModel:
      type: string
      enum:
        - latest
        - v1
        - v2
      title: V1ListenPostParametersDiarizeModel
    V1ListenPostParametersEncoding:
      type: string
      enum:
        - linear16
        - flac
        - mulaw
        - amr-nb
        - amr-wb
        - opus
        - speex
        - g729
      title: V1ListenPostParametersEncoding
    V1ListenPostParametersKeywords:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ListenPostParametersKeywords
    V1ListenPostParametersModel0:
      type: string
      enum:
        - nova-3
        - nova-3-general
        - nova-3-medical
        - nova-2
        - nova-2-general
        - nova-2-meeting
        - nova-2-finance
        - nova-2-conversationalai
        - nova-2-voicemail
        - nova-2-video
        - nova-2-medical
        - nova-2-drivethru
        - nova-2-automotive
        - nova
        - nova-general
        - nova-phonecall
        - nova-medical
        - enhanced
        - enhanced-general
        - enhanced-meeting
        - enhanced-phonecall
        - enhanced-finance
        - base
        - meeting
        - phonecall
        - finance
        - conversationalai
        - voicemail
        - video
      description: Our public models available to all accounts
      title: V1ListenPostParametersModel0
    V1ListenPostParametersModel:
      oneOf:
        - $ref: '#/components/schemas/V1ListenPostParametersModel0'
        - type: string
      title: V1ListenPostParametersModel
    V1ListenPostParametersRedactSchemaOneOf1Items:
      type: string
      enum:
        - pci
        - pii
        - numbers
      title: V1ListenPostParametersRedactSchemaOneOf1Items
    V1ListenPostParametersRedact1:
      type: array
      items:
        $ref: '#/components/schemas/V1ListenPostParametersRedactSchemaOneOf1Items'
      title: V1ListenPostParametersRedact1
    V1ListenPostParametersRedact:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/V1ListenPostParametersRedact1'
      title: V1ListenPostParametersRedact
    V1ListenPostParametersReplace:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ListenPostParametersReplace
    V1ListenPostParametersSearch:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: V1ListenPostParametersSearch
    V1ListenPostParametersVersion0:
      type: string
      enum:
        - latest
      description: Use the latest version of a model
      title: V1ListenPostParametersVersion0
    V1ListenPostParametersVersion:
      oneOf:
        - $ref: '#/components/schemas/V1ListenPostParametersVersion0'
        - type: string
      title: V1ListenPostParametersVersion
    ListenV1RequestUrl:
      type: object
      properties:
        url:
          type: string
          format: uri
      required:
        - url
      description: Audio file URL to transcribe
      title: ListenV1RequestUrl
    ListenV1ResponseMetadataModelInfo:
      type: object
      properties: {}
      title: ListenV1ResponseMetadataModelInfo
    ListenV1ResponseMetadataSummaryInfo:
      type: object
      properties:
        model_uuid:
          type: string
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      title: ListenV1ResponseMetadataSummaryInfo
    ListenV1ResponseMetadataSentimentInfo:
      type: object
      properties:
        model_uuid:
          type: string
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      title: ListenV1ResponseMetadataSentimentInfo
    ListenV1ResponseMetadataTopicsInfo:
      type: object
      properties:
        model_uuid:
          type: string
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      title: ListenV1ResponseMetadataTopicsInfo
    ListenV1ResponseMetadataIntentsInfo:
      type: object
      properties:
        model_uuid:
          type: string
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      title: ListenV1ResponseMetadataIntentsInfo
    ListenV1ResponseMetadata:
      type: object
      properties:
        transaction_key:
          type: string
          default: deprecated
        request_id:
          type: string
          format: uuid
        sha256:
          type: string
        created:
          type: string
          format: date-time
        duration:
          type: number
          format: double
        channels:
          type: integer
        models:
          type: array
          items:
            type: string
        model_info:
          $ref: '#/components/schemas/ListenV1ResponseMetadataModelInfo'
        summary_info:
          $ref: '#/components/schemas/ListenV1ResponseMetadataSummaryInfo'
        sentiment_info:
          $ref: '#/components/schemas/ListenV1ResponseMetadataSentimentInfo'
        topics_info:
          $ref: '#/components/schemas/ListenV1ResponseMetadataTopicsInfo'
        intents_info:
          $ref: '#/components/schemas/ListenV1ResponseMetadataIntentsInfo'
        tags:
          type: array
          items:
            type: string
      required:
        - request_id
        - sha256
        - created
        - duration
        - channels
        - models
        - model_info
      title: ListenV1ResponseMetadata
    ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems:
      type: object
      properties:
        confidence:
          type: number
          format: double
        start:
          type: number
          format: double
        end:
          type: number
          format: double
        snippet:
          type: string
      title: ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems
    ListenV1ResponseResultsChannelsItemsSearchItems:
      type: object
      properties:
        query:
          type: string
        hits:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems
      title: ListenV1ResponseResultsChannelsItemsSearchItems
    ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems:
      type: object
      properties:
        word:
          type: string
        start:
          type: number
          format: double
        end:
          type: number
          format: double
        confidence:
          type: number
          format: double
      title: ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems:
      type: object
      properties:
        text:
          type: string
        start:
          type: number
          format: double
        end:
          type: number
          format: double
      title: >-
        ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems:
      type: object
      properties:
        sentences:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems
        speaker:
          type: integer
        num_words:
          type: integer
        start:
          type: number
          format: double
        end:
          type: number
          format: double
      title: >-
        ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs:
      type: object
      properties:
        transcript:
          type: string
        paragraphs:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems
      title: ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs
    ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems:
      type: object
      properties:
        label:
          type: string
        value:
          type: string
        raw_value:
          type: string
        confidence:
          type: number
          format: double
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
      title: ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems
    ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems:
      type: object
      properties:
        summary:
          type: string
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
      title: ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems
    ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems:
      type: object
      properties:
        text:
          type: string
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
        topics:
          type: array
          items:
            type: string
      title: ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems
    ListenV1ResponseResultsChannelsItemsAlternativesItems:
      type: object
      properties:
        transcript:
          type: string
        confidence:
          type: number
          format: double
        words:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems
        paragraphs:
          $ref: >-
            #/components/schemas/ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs
        entities:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems
        summaries:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems
        topics:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems
      title: ListenV1ResponseResultsChannelsItemsAlternativesItems
    ListenV1ResponseResultsChannelsItems:
      type: object
      properties:
        search:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsSearchItems
        alternatives:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsChannelsItemsAlternativesItems
        detected_language:
          type: string
      title: ListenV1ResponseResultsChannelsItems
    ListenV1ResponseResultsChannels:
      type: array
      items:
        $ref: '#/components/schemas/ListenV1ResponseResultsChannelsItems'
      title: ListenV1ResponseResultsChannels
    ListenV1ResponseResultsUtterancesItemsWordsItems:
      type: object
      properties:
        word:
          type: string
        start:
          type: number
          format: double
        end:
          type: number
          format: double
        confidence:
          type: number
          format: double
        speaker:
          type: integer
        speaker_confidence:
          type: number
          format: double
        punctuated_word:
          type: string
      title: ListenV1ResponseResultsUtterancesItemsWordsItems
    ListenV1ResponseResultsUtterancesItems:
      type: object
      properties:
        start:
          type: number
          format: double
        end:
          type: number
          format: double
        confidence:
          type: number
          format: double
        channel:
          type: integer
        transcript:
          type: string
        words:
          type: array
          items:
            $ref: >-
              #/components/schemas/ListenV1ResponseResultsUtterancesItemsWordsItems
        speaker:
          type: integer
        id:
          type: string
          format: uuid
      title: ListenV1ResponseResultsUtterancesItems
    ListenV1ResponseResultsUtterances:
      type: array
      items:
        $ref: '#/components/schemas/ListenV1ResponseResultsUtterancesItems'
      title: ListenV1ResponseResultsUtterances
    ListenV1ResponseResultsSummary:
      type: object
      properties:
        result:
          type: string
        short:
          type: string
      title: ListenV1ResponseResultsSummary
    SharedTopicsResultsTopicsSegmentsItemsTopicsItems:
      type: object
      properties:
        topic:
          type: string
        confidence_score:
          type: number
          format: double
      title: SharedTopicsResultsTopicsSegmentsItemsTopicsItems
    SharedTopicsResultsTopicsSegmentsItems:
      type: object
      properties:
        text:
          type: string
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
        topics:
          type: array
          items:
            $ref: >-
              #/components/schemas/SharedTopicsResultsTopicsSegmentsItemsTopicsItems
      title: SharedTopicsResultsTopicsSegmentsItems
    SharedTopicsResultsTopics:
      type: object
      properties:
        segments:
          type: array
          items:
            $ref: '#/components/schemas/SharedTopicsResultsTopicsSegmentsItems'
      title: SharedTopicsResultsTopics
    SharedTopicsResults:
      type: object
      properties:
        topics:
          $ref: '#/components/schemas/SharedTopicsResultsTopics'
      title: SharedTopicsResults
    SharedTopics:
      type: object
      properties:
        results:
          $ref: '#/components/schemas/SharedTopicsResults'
      description: Output whenever `topics=true` is used
      title: SharedTopics
    SharedIntentsResultsIntentsSegmentsItemsIntentsItems:
      type: object
      properties:
        intent:
          type: string
        confidence_score:
          type: number
          format: double
      title: SharedIntentsResultsIntentsSegmentsItemsIntentsItems
    SharedIntentsResultsIntentsSegmentsItems:
      type: object
      properties:
        text:
          type: string
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
        intents:
          type: array
          items:
            $ref: >-
              #/components/schemas/SharedIntentsResultsIntentsSegmentsItemsIntentsItems
      title: SharedIntentsResultsIntentsSegmentsItems
    SharedIntentsResultsIntents:
      type: object
      properties:
        segments:
          type: array
          items:
            $ref: '#/components/schemas/SharedIntentsResultsIntentsSegmentsItems'
      title: SharedIntentsResultsIntents
    SharedIntentsResults:
      type: object
      properties:
        intents:
          $ref: '#/components/schemas/SharedIntentsResultsIntents'
      title: SharedIntentsResults
    SharedIntents:
      type: object
      properties:
        results:
          $ref: '#/components/schemas/SharedIntentsResults'
      description: Output whenever `intents=true` is used
      title: SharedIntents
    SharedSentimentsSegmentsItems:
      type: object
      properties:
        text:
          type: string
        start_word:
          type: number
          format: double
        end_word:
          type: number
          format: double
        sentiment:
          type: string
        sentiment_score:
          type: number
          format: double
      title: SharedSentimentsSegmentsItems
    SharedSentimentsAverage:
      type: object
      properties:
        sentiment:
          type: string
        sentiment_score:
          type: number
          format: double
      title: SharedSentimentsAverage
    SharedSentiments:
      type: object
      properties:
        segments:
          type: array
          items:
            $ref: '#/components/schemas/SharedSentimentsSegmentsItems'
        average:
          $ref: '#/components/schemas/SharedSentimentsAverage'
      description: Output whenever `sentiment=true` is used
      title: SharedSentiments
    ListenV1ResponseResults:
      type: object
      properties:
        channels:
          $ref: '#/components/schemas/ListenV1ResponseResultsChannels'
        utterances:
          $ref: '#/components/schemas/ListenV1ResponseResultsUtterances'
        summary:
          $ref: '#/components/schemas/ListenV1ResponseResultsSummary'
        topics:
          $ref: '#/components/schemas/SharedTopics'
        intents:
          $ref: '#/components/schemas/SharedIntents'
        sentiments:
          $ref: '#/components/schemas/SharedSentiments'
      required:
        - channels
      title: ListenV1ResponseResults
    ListenV1Response:
      type: object
      properties:
        metadata:
          $ref: '#/components/schemas/ListenV1ResponseMetadata'
        results:
          $ref: '#/components/schemas/ListenV1ResponseResults'
      required:
        - metadata
        - results
      description: The standard transcription response
      title: ListenV1Response
    ListenV1AcceptedResponse:
      type: object
      properties:
        request_id:
          type: string
          format: uuid
          description: Unique identifier for tracking the asynchronous request
      required:
        - request_id
      description: Accepted response for asynchronous transcription requests
      title: ListenV1AcceptedResponse
    listen_v1_media_transcribe_Response_200:
      oneOf:
        - $ref: '#/components/schemas/ListenV1Response'
        - $ref: '#/components/schemas/ListenV1AcceptedResponse'
      title: listen_v1_media_transcribe_Response_200
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: |
        Use `Authorization: Token <API_KEY>`
        Example: `Authorization: Token 12345abcdef`
    JwtAuth:
      type: http
      scheme: bearer
      description: |
        Use `Authorization: Bearer <JWT>`
        Example: `Authorization: Bearer eyJhbGciOiJ...`

```

## Examples



**Request**

```json
{
  "url": "https://dpgr.am/spacewalk.wav"
}
```

**Response**

```json
{
  "metadata": {
    "transaction_key": "deprecated",
    "request_id": "a847f427-4ad5-4d67-9b95-db801e58251c",
    "sha256": "154e291ecfa8be6ab8343560bcc109008fa7853eb5372533e8efdefc9b504c33",
    "created": "2024-05-12T18:57:13.426Z",
    "duration": 25.933313,
    "channels": 1,
    "models": [
      "30089e05-99d1-4376-b32e-c263170674af"
    ],
    "model_info": {
      "30089e05-99d1-4376-b32e-c263170674af": {
        "name": "2-general-nova",
        "version": "2024-01-09.29447",
        "arch": "nova-2"
      }
    },
    "summary_info": {
      "model_uuid": "67875a7f-c9c4-48a0-aa55-5bdb8a91c34a",
      "input_tokens": 95,
      "output_tokens": 63
    },
    "sentiment_info": {
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "input_tokens": 105,
      "output_tokens": 105
    },
    "topics_info": {
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "input_tokens": 105,
      "output_tokens": 7
    },
    "intents_info": {
      "model_uuid": "80ab3179-d113-4254-bd6b-4a2f96498695",
      "input_tokens": 105,
      "output_tokens": 4
    },
    "tags": [
      "test"
    ]
  },
  "results": {
    "channels": [
      {
        "search": [
          {
            "query": "spacewalk",
            "hits": [
              {
                "confidence": 0.98,
                "start": 5.2,
                "end": 5.8,
                "snippet": "the first all-female spacewalk"
              }
            ]
          }
        ],
        "alternatives": [
          {
            "transcript": "This historic spacewalk marks a significant milestone for women in space exploration.",
            "confidence": 0.95,
            "words": [
              {
                "word": "This",
                "start": 0,
                "end": 0.3,
                "confidence": 0.98
              },
              {
                "word": "historic",
                "start": 0.3,
                "end": 0.7,
                "confidence": 0.97
              },
              {
                "word": "spacewalk",
                "start": 5.2,
                "end": 5.8,
                "confidence": 0.99
              }
            ],
            "paragraphs": {
              "transcript": "This historic spacewalk marks a significant milestone for women in space exploration.",
              "paragraphs": [
                {
                  "sentences": [
                    {
                      "text": "This historic spacewalk marks a significant milestone for women in space exploration.",
                      "start": 0,
                      "end": 6
                    }
                  ],
                  "speaker": 1,
                  "num_words": 12,
                  "start": 0,
                  "end": 6
                }
              ]
            },
            "entities": [
              {
                "label": "Event",
                "value": "spacewalk",
                "raw_value": "spacewalk",
                "confidence": 0.95,
                "start_word": 2,
                "end_word": 3
              }
            ],
            "summaries": [
              {
                "summary": "The transcript highlights the importance of the first all-female spacewalk.",
                "start_word": 0,
                "end_word": 12
              }
            ],
            "topics": [
              {
                "text": "This historic spacewalk marks a significant milestone for women in space exploration.",
                "start_word": 0,
                "end_word": 12,
                "topics": [
                  "Space Exploration"
                ]
              }
            ]
          }
        ],
        "detected_language": "en"
      }
    ],
    "utterances": [
      {
        "start": 0,
        "end": 6,
        "confidence": 0.95,
        "channel": 1,
        "transcript": "This historic spacewalk marks a significant milestone for women in space exploration.",
        "words": [
          {
            "word": "This",
            "start": 0,
            "end": 0.3,
            "confidence": 0.98,
            "speaker": 1,
            "speaker_confidence": 0.99,
            "punctuated_word": "This"
          },
          {
            "word": "historic",
            "start": 0.3,
            "end": 0.7,
            "confidence": 0.97,
            "speaker": 1,
            "speaker_confidence": 0.99,
            "punctuated_word": "historic"
          },
          {
            "word": "spacewalk",
            "start": 5.2,
            "end": 5.8,
            "confidence": 0.99,
            "speaker": 1,
            "speaker_confidence": 0.99,
            "punctuated_word": "spacewalk."
          }
        ],
        "speaker": 1,
        "id": "utt-001"
      }
    ],
    "summary": {
      "result": "success",
      "short": "Speaker 1 highlights the historic significance of the first all-female spacewalk as a milestone for women in space exploration."
    },
    "topics": {
      "results": {
        "topics": {
          "segments": [
            {
              "text": "And, um, I think if it signifies anything, it is, uh, to honor the the women who came before us who, um, were skilled and qualified, um, and didn't get the the same opportunities that we have today.",
              "start_word": 32,
              "end_word": 69,
              "topics": [
                {
                  "topic": "Spacewalk",
                  "confidence_score": 0.91581345
                }
              ]
            }
          ]
        }
      }
    },
    "intents": {
      "results": {
        "intents": {
          "segments": [
            {
              "text": "If you found this valuable, you can subscribe to the show on spotify or your favorite podcast app.",
              "start_word": 354,
              "end_word": 414,
              "intents": [
                {
                  "intent": "Encourage podcasting",
                  "confidence_score": 0.0038975573
                }
              ]
            }
          ]
        }
      }
    },
    "sentiments": {
      "segments": [
        {
          "text": "Yeah. As as much as, um, it's worth celebrating, uh, the first, uh, spacewalk, um, with an all-female team, I think many of us are looking forward to it just being normal. And, um, I think if it_signf",
          "start_word": 0,
          "end_word": 69,
          "sentiment": "positive",
          "sentiment_score": 0.5810546875
        }
      ],
      "average": {
        "sentiment": "positive",
        "sentiment_score": 0.5810185185185185
      }
    }
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/listen"

payload = { "url": "https://dpgr.am/spacewalk.wav" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/listen';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"url":"https://dpgr.am/spacewalk.wav"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.deepgram.com/v1/listen"

	payload := strings.NewReader("{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Token <apiKey>")
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

url = URI("https://api.deepgram.com/v1/listen")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/listen")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/listen', [
  'body' => '{
  "url": "https://dpgr.am/spacewalk.wav"
}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/listen");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["url": "https://dpgr.am/spacewalk.wav"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/listen")! as URL,
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
