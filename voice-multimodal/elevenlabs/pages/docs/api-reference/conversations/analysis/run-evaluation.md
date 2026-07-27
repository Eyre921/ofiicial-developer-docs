---
title: "Run conversation evaluation"
source: https://elevenlabs.io/docs/api-reference/conversations/analysis/run-evaluation.md
path: docs/api-reference/conversations/analysis/run-evaluation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Run conversation evaluation

POST https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/analysis/evaluations/run
Content-Type: application/json

Rerun a specific evaluation for a conversation.

Reference: https://elevenlabs.io/docs/api-reference/conversations/analysis/run-evaluation

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/conversations/{conversation_id}/analysis/evaluations/run:
    post:
      operationId: runEvaluation
      summary: Run Conversation Evaluation
      description: Rerun a specific evaluation for a conversation.
      tags:
        - analysis
      parameters:
        - name: conversation_id
          in: path
          description: ID of the conversation
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
                $ref: '#/components/schemas/GetConversationResponseModel'
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
              $ref: '#/components/schemas/RunConversationEvaluationsRequest'
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
    AnalysisScope:
      type: string
      enum:
        - conversation
        - agent
      default: conversation
      title: AnalysisScope
    RunConversationEvaluationsRequest:
      type: object
      properties:
        evaluation_id:
          type: string
          description: ID of the single evaluation criterion to rerun.
        scope:
          $ref: '#/components/schemas/AnalysisScope'
          default: conversation
      required:
        - evaluation_id
      title: RunConversationEvaluationsRequest
    GetConversationResponseModelStatus:
      type: string
      enum:
        - initiated
        - in-progress
        - processing
        - done
        - failed
      title: GetConversationResponseModelStatus
    ConversationDeletionSettings:
      type: object
      properties:
        deletion_time_unix_secs:
          type:
            - integer
            - 'null'
        deleted_logs_at_time_unix_secs:
          type:
            - integer
            - 'null'
        deleted_audio_at_time_unix_secs:
          type:
            - integer
            - 'null'
        deleted_transcript_at_time_unix_secs:
          type:
            - integer
            - 'null'
        delete_transcript_and_pii:
          type: boolean
          default: false
        delete_audio:
          type: boolean
          default: false
      title: ConversationDeletionSettings
    ConversationFeedbackType:
      type: string
      enum:
        - thumbs
        - rating
      title: ConversationFeedbackType
    UserFeedbackScore:
      type: string
      enum:
        - like
        - dislike
      title: UserFeedbackScore
    ConversationHistoryFeedbackCommonModel:
      type: object
      properties:
        type:
          oneOf:
            - $ref: '#/components/schemas/ConversationFeedbackType'
            - type: 'null'
        overall_score:
          oneOf:
            - $ref: '#/components/schemas/UserFeedbackScore'
            - type: 'null'
        likes:
          type: integer
          default: 0
        dislikes:
          type: integer
          default: 0
        rating:
          type:
            - integer
            - 'null'
        comment:
          type:
            - string
            - 'null'
      title: ConversationHistoryFeedbackCommonModel
    AuthorizationMethod:
      type: string
      enum:
        - invalid
        - public
        - authorization_header
        - signed_url
        - shareable_link
        - livekit_token
        - livekit_token_website
        - genesys_api_key
        - whatsapp
        - sms
      default: public
      title: AuthorizationMethod
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
    LLMUsage-Output:
      type: object
      properties:
        model_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/LLMInputOutputTokensUsage'
      title: LLMUsage-Output
    LLMCategoryUsage:
      type: object
      properties:
        irreversible_generation:
          $ref: '#/components/schemas/LLMUsage-Output'
        initiated_generation:
          $ref: '#/components/schemas/LLMUsage-Output'
      title: LLMCategoryUsage
    PlatformCategoryUsage:
      type: object
      properties:
        credits:
          type: integer
          default: 0
        price:
          type: number
          format: double
          default: 0
        quantity:
          type: number
          format: double
          default: 0
      description: Accumulated charge for a single :class:`PlatformCategory`.
      title: PlatformCategoryUsage
    PlatformUsage:
      type: object
      properties:
        category_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/PlatformCategoryUsage'
      description: >-
        Per-category breakdown of ``platform_charge`` (the analogue of
        ``llm_usage``).
      title: PlatformUsage
    ConversationVoiceUsageModel:
      type: object
      properties:
        voice_id:
          type: string
        audio_output_seconds:
          type: number
          format: double
          default: 0
      required:
        - voice_id
      title: ConversationVoiceUsageModel
    ConversationTTSUsageModel:
      type: object
      properties:
        primary_tts_model:
          type:
            - string
            - 'null'
        total_audio_output_seconds:
          type: number
          format: double
          default: 0
        total_characters:
          type: integer
          default: 0
        per_voice_usage:
          type: array
          items:
            $ref: '#/components/schemas/ConversationVoiceUsageModel'
      description: Aggregated TTS usage for a conversation (analytics-only, not billing).
      title: ConversationTTSUsageModel
    ConversationASRUsageModel:
      type: object
      properties:
        asr_model:
          type:
            - string
            - 'null'
        total_transcription_calls:
          type: integer
          default: 0
        total_audio_input_seconds:
          type: number
          format: double
          default: 0
      description: Aggregated ASR usage for a conversation (analytics-only, not billing).
      title: ConversationASRUsageModel
    ConversationChargingCommonModel:
      type: object
      properties:
        dev_discount:
          type: boolean
          default: false
        is_burst:
          type: boolean
          default: false
        tier:
          type:
            - string
            - 'null'
        llm_usage:
          $ref: '#/components/schemas/LLMCategoryUsage'
        llm_price:
          type:
            - number
            - 'null'
          format: double
        llm_charge:
          type:
            - integer
            - 'null'
        call_charge:
          type:
            - integer
            - 'null'
        platform_charge:
          type:
            - integer
            - 'null'
        platform_usage:
          $ref: '#/components/schemas/PlatformUsage'
        platform_price:
          type:
            - number
            - 'null'
          format: double
        free_minutes_consumed:
          type: number
          format: double
          default: 0
        free_llm_dollars_consumed:
          type: number
          format: double
          default: 0
        tts_usage:
          oneOf:
            - $ref: '#/components/schemas/ConversationTTSUsageModel'
            - type: 'null'
        asr_usage:
          oneOf:
            - $ref: '#/components/schemas/ConversationASRUsageModel'
            - type: 'null'
      title: ConversationChargingCommonModel
    TelephonyDirection:
      type: string
      enum:
        - inbound
        - outbound
      default: inbound
      title: TelephonyDirection
    ConversationHistoryMetadataCommonModelPhoneCall:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - exotel
              description: 'Discriminator value: exotel'
            direction:
              $ref: '#/components/schemas/TelephonyDirection'
            phone_number_id:
              type: string
            agent_number:
              type: string
            external_number:
              type: string
            stream_sid:
              type: string
            call_sid:
              type: string
          required:
            - type
            - direction
            - phone_number_id
            - agent_number
            - external_number
            - stream_sid
            - call_sid
          description: ConversationHistoryExotelPhoneCallModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - sip_trunking
            direction:
              $ref: '#/components/schemas/TelephonyDirection'
            phone_number_id:
              type: string
            agent_number:
              type: string
            external_number:
              type: string
            call_id:
              type:
                - string
                - 'null'
            call_sid:
              type: string
            sip_header_dynamic_variables:
              type: object
              additionalProperties:
                type: string
          required:
            - type
            - direction
            - phone_number_id
            - agent_number
            - external_number
            - call_sid
          description: ConversationHistorySIPTrunkingPhoneCallModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - twilio
            direction:
              $ref: '#/components/schemas/TelephonyDirection'
            phone_number_id:
              type: string
            agent_number:
              type: string
            external_number:
              type: string
            stream_sid:
              type: string
            call_sid:
              type: string
          required:
            - type
            - direction
            - phone_number_id
            - agent_number
            - external_number
            - stream_sid
            - call_sid
          description: ConversationHistoryTwilioPhoneCallModel variant
      discriminator:
        propertyName: type
      title: ConversationHistoryMetadataCommonModelPhoneCall
    ConversationHistoryBatchCallModel:
      type: object
      properties:
        batch_call_id:
          type: string
        batch_call_recipient_id:
          type: string
      required:
        - batch_call_id
        - batch_call_recipient_id
      title: ConversationHistoryBatchCallModel
    ConversationHistoryErrorCommonModel:
      type: object
      properties:
        code:
          type: integer
        reason:
          type:
            - string
            - 'null'
      required:
        - code
      title: ConversationHistoryErrorCommonModel
    ConversationHistoryRagUsageCommonModel:
      type: object
      properties:
        usage_count:
          type: integer
        embedding_model:
          type: string
      required:
        - usage_count
        - embedding_model
      title: ConversationHistoryRagUsageCommonModel
    FeatureStatusCommonModel:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
        used:
          type: boolean
          default: false
      title: FeatureStatusCommonModel
    WorkflowFeaturesUsageCommonModel:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
        tool_node:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        standalone_agent_node:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        phone_number_node:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        end_node:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
      title: WorkflowFeaturesUsageCommonModel
    TestsFeatureUsageCommonModel:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
        tests_ran_after_last_modification:
          type: boolean
          default: false
        tests_ran_in_last_7_days:
          type: boolean
          default: false
      title: TestsFeatureUsageCommonModel
    FeaturesUsageCommonModel:
      type: object
      properties:
        language_detection:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        transfer_to_agent:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        transfer_to_number:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        multivoice:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        dtmf_tones:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        external_mcp_servers:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        pii_zrm_workspace:
          type: boolean
          default: false
        pii_zrm_agent:
          type: boolean
          default: false
        tool_dynamic_variable_updates:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        is_livekit:
          type: boolean
          default: false
        voicemail_detection:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        dtmf_input:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        workflow:
          $ref: '#/components/schemas/WorkflowFeaturesUsageCommonModel'
        agent_testing:
          $ref: '#/components/schemas/TestsFeatureUsageCommonModel'
        versioning:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
        file_input:
          $ref: '#/components/schemas/FeatureStatusCommonModel'
      title: FeaturesUsageCommonModel
    ConversationHistoryElevenAssistantCommonModel:
      type: object
      properties:
        is_eleven_assistant:
          type: boolean
          default: false
      title: ConversationHistoryElevenAssistantCommonModel
    ConversationInitiationSource:
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
        - salesforce_integration
        - template_preview
        - genesys_bot_connector
        - subagent_tool
      default: unknown
      description: Enum representing the possible sources for conversation initiation.
      title: ConversationInitiationSource
    AsyncConversationMetadataDeliveryStatus:
      type: string
      enum:
        - pending
        - success
        - failed
      title: AsyncConversationMetadataDeliveryStatus
    AsyncConversationMetadata:
      type: object
      properties:
        delivery_status:
          $ref: '#/components/schemas/AsyncConversationMetadataDeliveryStatus'
        delivery_timestamp:
          type: integer
        delivery_error:
          type:
            - string
            - 'null'
        external_system:
          type: string
        external_id:
          type: string
        external_link:
          type:
            - string
            - 'null'
        retry_count:
          type: integer
          default: 0
        last_retry_timestamp:
          type:
            - integer
            - 'null'
        last_processed_external_message_id:
          type:
            - string
            - 'null'
      required:
        - delivery_status
        - delivery_timestamp
        - external_system
        - external_id
      description: Metadata for async conversation delivery (Zendesk, Slack, etc.).
      title: AsyncConversationMetadata
    WhatsAppConversationInfoDirection:
      type: string
      enum:
        - inbound
        - outbound
        - unknown
      default: unknown
      title: WhatsAppConversationInfoDirection
    WhatsAppConversationInfo:
      type: object
      properties:
        direction:
          $ref: '#/components/schemas/WhatsAppConversationInfoDirection'
          default: unknown
        whatsapp_phone_number_id:
          type:
            - string
            - 'null'
        whatsapp_user_id:
          type: string
        awaiting_first_user_message:
          type:
            - boolean
            - 'null'
      required:
        - whatsapp_user_id
      title: WhatsAppConversationInfo
    SmsConversationInfoDirection:
      type: string
      enum:
        - inbound
        - outbound
      title: SmsConversationInfoDirection
    SMSConversationInfo:
      type: object
      properties:
        direction:
          $ref: '#/components/schemas/SmsConversationInfoDirection'
        phone_number_id:
          type:
            - string
            - 'null'
        sms_user_phone_number:
          type: string
        agent_phone_number:
          type:
            - string
            - 'null'
      required:
        - direction
        - sms_user_phone_number
      title: SMSConversationInfo
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
    ConversationVoiceRewardModel:
      type: object
      properties:
        voice_id:
          type: string
        reward_usd_cents:
          type: number
          format: double
      required:
        - voice_id
        - reward_usd_cents
      title: ConversationVoiceRewardModel
    ConversationHistoryMetadataCommonModel:
      type: object
      properties:
        start_time_unix_secs:
          type: integer
        accepted_time_unix_secs:
          type:
            - integer
            - 'null'
        call_duration_secs:
          type: integer
        cost:
          type:
            - integer
            - 'null'
        deletion_settings:
          $ref: '#/components/schemas/ConversationDeletionSettings'
        feedback:
          $ref: '#/components/schemas/ConversationHistoryFeedbackCommonModel'
        authorization_method:
          $ref: '#/components/schemas/AuthorizationMethod'
          default: public
        charging:
          $ref: '#/components/schemas/ConversationChargingCommonModel'
        phone_call:
          oneOf:
            - $ref: >-
                #/components/schemas/ConversationHistoryMetadataCommonModelPhoneCall
            - type: 'null'
        batch_call:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryBatchCallModel'
            - type: 'null'
        termination_reason:
          type: string
          default: ''
        error:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryErrorCommonModel'
            - type: 'null'
        warnings:
          type: array
          items:
            type: string
        main_language:
          type:
            - string
            - 'null'
        rag_usage:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryRagUsageCommonModel'
            - type: 'null'
        text_only:
          type: boolean
          default: false
        features_usage:
          $ref: '#/components/schemas/FeaturesUsageCommonModel'
        eleven_assistant:
          $ref: '#/components/schemas/ConversationHistoryElevenAssistantCommonModel'
        initiator_id:
          type:
            - string
            - 'null'
        conversation_initiation_source:
          $ref: '#/components/schemas/ConversationInitiationSource'
          default: unknown
        conversation_initiation_source_version:
          type:
            - string
            - 'null'
        timezone:
          type:
            - string
            - 'null'
        async_metadata:
          oneOf:
            - $ref: '#/components/schemas/AsyncConversationMetadata'
            - type: 'null'
        whatsapp:
          oneOf:
            - $ref: '#/components/schemas/WhatsAppConversationInfo'
            - type: 'null'
        sms:
          oneOf:
            - $ref: '#/components/schemas/SMSConversationInfo'
            - type: 'null'
        agent_created_from:
          $ref: '#/components/schemas/AgentDefinitionSource'
          default: unknown
        agent_last_updated_from:
          $ref: '#/components/schemas/AgentDefinitionSource'
          default: unknown
        voice_rewards:
          type: array
          items:
            $ref: '#/components/schemas/ConversationVoiceRewardModel'
        cost_fiat:
          type:
            - number
            - 'null'
          format: double
          description: >-
            Total fiat cost of the conversation in USD, i.e. the sum of the LLM
            price and the non-LLM platform price (the fiat analogue of
            ``cost``). ``None`` when neither is set (e.g. conversations that
            predate fiat cost tracking).
      required:
        - start_time_unix_secs
        - call_duration_secs
        - cost_fiat
      title: ConversationHistoryMetadataCommonModel
    EvaluationSuccessResult:
      type: string
      enum:
        - success
        - failure
        - unknown
      title: EvaluationSuccessResult
    CriteriaScoringMode:
      type: string
      enum:
        - binary
        - numeric_uniform
      default: binary
      title: CriteriaScoringMode
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
    VisitedAgentRef:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
      required:
        - agent_id
      description: >-
        An agent (and optional branch) that participated in the call, in
        first-seen transcript order.
      title: VisitedAgentRef
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
    PromptAgentAPIModelOverride-Output:
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
      title: PromptAgentAPIModelOverride-Output
    AgentConfigOverride-Output:
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
            - $ref: '#/components/schemas/PromptAgentAPIModelOverride-Output'
            - type: 'null'
          description: The prompt for the agent
      title: AgentConfigOverride-Output
    ConversationConfigClientOverride-Output:
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
            - $ref: '#/components/schemas/AgentConfigOverride-Output'
            - type: 'null'
          description: Agent specific configuration
      title: ConversationConfigClientOverride-Output
    ConversationInitiationSourceInfo:
      type: object
      properties:
        source:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationSource'
            - type: 'null'
          description: Source of the conversation initiation
        version:
          type:
            - string
            - 'null'
          description: The SDK version number
      description: Information about the source of conversation initiation
      title: ConversationInitiationSourceInfo
    ConversationInitiationClientDataRequest-Output:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/ConversationConfigClientOverride-Output'
        custom_llm_extra_body:
          type: object
          additionalProperties:
            description: Any type
        user_id:
          type:
            - string
            - 'null'
          description: >-
            ID of the end user participating in this conversation (for agent
            owner's user identification)
        source_info:
          $ref: '#/components/schemas/ConversationInitiationSourceInfo'
        branch_id:
          type:
            - string
            - 'null'
          description: ID of the agent branch to use for this conversation
        environment:
          type:
            - string
            - 'null'
          description: Environment to use for resolving environment variables
        starting_workflow_node_id:
          type:
            - string
            - 'null'
          description: >-
            If set, start the workflow at this node id instead of the default
            entry
        dynamic_variables:
          type: object
          additionalProperties:
            description: Any type
      title: ConversationInitiationClientDataRequest-Output
    ConversationHistoryTranscriptResponseModelRole:
      type: string
      enum:
        - user
        - agent
      title: ConversationHistoryTranscriptResponseModelRole
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
    KnowledgeBaseRagChunkModel:
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
    TransferToAgentToolResultSuccessModelOutputBranchInfo:
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
      title: TransferToAgentToolResultSuccessModelOutputBranchInfo
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
            chunks:
              type: array
              items:
                $ref: '#/components/schemas/KnowledgeBaseRagChunkModel'
              description: >-
                Retrieved chunks; populated only in the
                rag-result-in-tool-result mode
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
                - run_subagent_error
              default: run_subagent_error
            status:
              type: string
              enum:
                - error
              default: error
            error:
              type: string
          required:
            - result_type
            - error
          description: RunSubagentToolResultErrorModel variant
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - run_subagent_success
              default: run_subagent_success
            status:
              type: string
              enum:
                - success
              default: success
            query:
              type: string
            agent_response:
              type: string
          required:
            - result_type
            - query
            - agent_response
          description: RunSubagentToolResultSuccessModel variant
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
                    #/components/schemas/TransferToAgentToolResultSuccessModelOutputBranchInfo
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
    EmbeddingModelEnum:
      type: string
      enum:
        - e5_mistral_7b_instruct
        - multilingual_e5_large_instruct
      default: e5_mistral_7b_instruct
      title: EmbeddingModelEnum
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
        ignored_as_backchannel:
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
    GetConversationResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        agent_name:
          type:
            - string
            - 'null'
        conversation_product:
          type: string
          default: agent
        status:
          $ref: '#/components/schemas/GetConversationResponseModelStatus'
        user_id:
          type:
            - string
            - 'null'
        branch_id:
          type:
            - string
            - 'null'
        version_id:
          type:
            - string
            - 'null'
          description: The ID of the agent version used for this conversation
        metadata:
          $ref: '#/components/schemas/ConversationHistoryMetadataCommonModel'
        analysis:
          oneOf:
            - $ref: '#/components/schemas/ConversationHistoryAnalysisCommonModel'
            - type: 'null'
        visited_agents:
          type: array
          items:
            $ref: '#/components/schemas/VisitedAgentRef'
        conversation_initiation_client_data:
          $ref: '#/components/schemas/ConversationInitiationClientDataRequest-Output'
        environment:
          type: string
          default: production
        conversation_id:
          type: string
        has_audio:
          type: boolean
        has_user_audio:
          type: boolean
        has_response_audio:
          type: boolean
        has_auxiliary_audio:
          type: boolean
        transcript:
          type: array
          items:
            $ref: '#/components/schemas/ConversationHistoryTranscriptResponseModel'
        tag_ids:
          type: array
          items:
            type: string
          description: Conversation tag ids assigned to this conversation.
        otlp_traces:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
          description: >-
            OpenTelemetry trace payload when the request uses
            format=opentelemetry; otherwise omitted.
      required:
        - agent_id
        - status
        - metadata
        - conversation_id
        - has_audio
        - has_user_audio
        - has_response_audio
        - has_auxiliary_audio
        - transcript
      title: GetConversationResponseModel
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
  "evaluation_id": "string"
}
```

**Response**

```json
{
  "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
  "status": "processing",
  "metadata": {
    "start_time_unix_secs": 1714423232,
    "call_duration_secs": 10,
    "cost_fiat": 1.1
  },
  "conversation_id": "conv_7401k5m9x2p8ec3rqv6dtnhb0fzw",
  "has_audio": true,
  "has_user_audio": true,
  "has_response_audio": true,
  "has_auxiliary_audio": true,
  "transcript": [
    {
      "role": "user",
      "time_in_call_secs": 10,
      "message": "Hello, how are you?"
    }
  ],
  "agent_name": "My agent",
  "version_id": "agtvrsn_5xM3yVvZQKV0EfqQpLr2",
  "environment": "production",
  "tag_ids": []
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.analysis.runEvaluation("conversation_id", {
        evaluationId: "string",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.analysis.run_evaluation(
    conversation_id="conversation_id",
    evaluation_id="string",
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

	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run"

	payload := strings.NewReader("{\n  \"evaluation_id\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"evaluation_id\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run")
  .header("Content-Type", "application/json")
  .body("{\n  \"evaluation_id\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run', [
  'body' => '{
  "evaluation_id": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"evaluation_id\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["evaluation_id": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run")! as URL,
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
