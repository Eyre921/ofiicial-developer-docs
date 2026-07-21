---
title: "Run conversation evaluation"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/analysis/run-evaluation.md
path: docs/eleven-agents/api-reference/conversations/analysis/run-evaluation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Run conversation evaluation

POST https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/analysis/evaluations/run
Content-Type: application/json

Rerun a specific evaluation for a conversation.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/analysis/run-evaluation

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
                $ref: '#/components/schemas/type_:GetConversationResponseModel'
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
                evaluation_id:
                  type: string
                  description: ID of the single evaluation criterion to rerun.
                scope:
                  $ref: '#/components/schemas/type_:AnalysisScope'
              required:
                - evaluation_id
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
    type_:AnalysisScope:
      type: string
      enum:
        - conversation
        - agent
      default: conversation
      title: AnalysisScope
    type_:GetConversationResponseModelStatus:
      type: string
      enum:
        - initiated
        - in-progress
        - processing
        - done
        - failed
      title: GetConversationResponseModelStatus
    type_:ConversationDeletionSettings:
      type: object
      properties:
        deletion_time_unix_secs:
          type: integer
        deleted_logs_at_time_unix_secs:
          type: integer
        deleted_audio_at_time_unix_secs:
          type: integer
        deleted_transcript_at_time_unix_secs:
          type: integer
        delete_transcript_and_pii:
          type: boolean
          default: false
        delete_audio:
          type: boolean
          default: false
      title: ConversationDeletionSettings
    type_:ConversationFeedbackType:
      type: string
      enum:
        - thumbs
        - rating
      title: ConversationFeedbackType
    type_:UserFeedbackScore:
      type: string
      enum:
        - like
        - dislike
      title: UserFeedbackScore
    type_:ConversationHistoryFeedbackCommonModel:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:ConversationFeedbackType'
        overall_score:
          $ref: '#/components/schemas/type_:UserFeedbackScore'
        likes:
          type: integer
          default: 0
        dislikes:
          type: integer
          default: 0
        rating:
          type: integer
        comment:
          type: string
      title: ConversationHistoryFeedbackCommonModel
    type_:AuthorizationMethod:
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
    type_:LlmCategoryUsage:
      type: object
      properties:
        irreversible_generation:
          $ref: '#/components/schemas/type_:LlmUsageOutput'
        initiated_generation:
          $ref: '#/components/schemas/type_:LlmUsageOutput'
      title: LlmCategoryUsage
    type_:PlatformCategoryUsage:
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
    type_:PlatformUsage:
      type: object
      properties:
        category_usage:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:PlatformCategoryUsage'
      description: >-
        Per-category breakdown of ``platform_charge`` (the analogue of
        ``llm_usage``).
      title: PlatformUsage
    type_:ConversationVoiceUsageModel:
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
    type_:ConversationTtsUsageModel:
      type: object
      properties:
        primary_tts_model:
          type: string
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
            $ref: '#/components/schemas/type_:ConversationVoiceUsageModel'
      description: Aggregated TTS usage for a conversation (analytics-only, not billing).
      title: ConversationTtsUsageModel
    type_:ConversationAsrUsageModel:
      type: object
      properties:
        asr_model:
          type: string
        total_transcription_calls:
          type: integer
          default: 0
        total_audio_input_seconds:
          type: number
          format: double
          default: 0
      description: Aggregated ASR usage for a conversation (analytics-only, not billing).
      title: ConversationAsrUsageModel
    type_:ConversationChargingCommonModel:
      type: object
      properties:
        dev_discount:
          type: boolean
          default: false
        is_burst:
          type: boolean
          default: false
        tier:
          type: string
        llm_usage:
          $ref: '#/components/schemas/type_:LlmCategoryUsage'
        llm_price:
          type: number
          format: double
        llm_charge:
          type: integer
        call_charge:
          type: integer
        platform_charge:
          type: integer
        platform_usage:
          $ref: '#/components/schemas/type_:PlatformUsage'
        platform_price:
          type: number
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
          $ref: '#/components/schemas/type_:ConversationTtsUsageModel'
        asr_usage:
          $ref: '#/components/schemas/type_:ConversationAsrUsageModel'
      title: ConversationChargingCommonModel
    type_:TelephonyDirection:
      type: string
      enum:
        - inbound
        - outbound
      default: inbound
      title: TelephonyDirection
    type_:ConversationHistoryMetadataCommonModelPhoneCall:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - exotel
              description: 'Discriminator value: exotel'
            direction:
              $ref: '#/components/schemas/type_:TelephonyDirection'
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
        - type: object
          properties:
            type:
              type: string
              enum:
                - sip_trunking
              description: 'Discriminator value: sip_trunking'
            direction:
              $ref: '#/components/schemas/type_:TelephonyDirection'
            phone_number_id:
              type: string
            agent_number:
              type: string
            external_number:
              type: string
            call_id:
              type: string
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
        - type: object
          properties:
            type:
              type: string
              enum:
                - twilio
              description: 'Discriminator value: twilio'
            direction:
              $ref: '#/components/schemas/type_:TelephonyDirection'
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
      discriminator:
        propertyName: type
      title: ConversationHistoryMetadataCommonModelPhoneCall
    type_:ConversationHistoryBatchCallModel:
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
    type_:ConversationHistoryErrorCommonModel:
      type: object
      properties:
        code:
          type: integer
        reason:
          type: string
      required:
        - code
      title: ConversationHistoryErrorCommonModel
    type_:ConversationHistoryRagUsageCommonModel:
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
    type_:FeatureStatusCommonModel:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
        used:
          type: boolean
          default: false
      title: FeatureStatusCommonModel
    type_:WorkflowFeaturesUsageCommonModel:
      type: object
      properties:
        enabled:
          type: boolean
          default: false
        tool_node:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        standalone_agent_node:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        phone_number_node:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        end_node:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
      title: WorkflowFeaturesUsageCommonModel
    type_:TestsFeatureUsageCommonModel:
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
    type_:FeaturesUsageCommonModel:
      type: object
      properties:
        language_detection:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        transfer_to_agent:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        transfer_to_number:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        multivoice:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        dtmf_tones:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        external_mcp_servers:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        pii_zrm_workspace:
          type: boolean
          default: false
        pii_zrm_agent:
          type: boolean
          default: false
        tool_dynamic_variable_updates:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        is_livekit:
          type: boolean
          default: false
        voicemail_detection:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        dtmf_input:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        workflow:
          $ref: '#/components/schemas/type_:WorkflowFeaturesUsageCommonModel'
        agent_testing:
          $ref: '#/components/schemas/type_:TestsFeatureUsageCommonModel'
        versioning:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
        file_input:
          $ref: '#/components/schemas/type_:FeatureStatusCommonModel'
      title: FeaturesUsageCommonModel
    type_:ConversationHistoryElevenAssistantCommonModel:
      type: object
      properties:
        is_eleven_assistant:
          type: boolean
          default: false
      title: ConversationHistoryElevenAssistantCommonModel
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
        - salesforce_integration
        - template_preview
        - genesys_bot_connector
        - subagent_tool
      default: unknown
      description: Enum representing the possible sources for conversation initiation.
      title: ConversationInitiationSource
    type_:AsyncConversationMetadataDeliveryStatus:
      type: string
      enum:
        - pending
        - success
        - failed
      title: AsyncConversationMetadataDeliveryStatus
    type_:AsyncConversationMetadata:
      type: object
      properties:
        delivery_status:
          $ref: '#/components/schemas/type_:AsyncConversationMetadataDeliveryStatus'
        delivery_timestamp:
          type: integer
        delivery_error:
          type: string
        external_system:
          type: string
        external_id:
          type: string
        external_link:
          type: string
        retry_count:
          type: integer
          default: 0
        last_retry_timestamp:
          type: integer
        last_processed_external_message_id:
          type: string
      required:
        - delivery_status
        - delivery_timestamp
        - external_system
        - external_id
      description: Metadata for async conversation delivery (Zendesk, Slack, etc.).
      title: AsyncConversationMetadata
    type_:WhatsAppConversationInfoDirection:
      type: string
      enum:
        - inbound
        - outbound
        - unknown
      default: unknown
      title: WhatsAppConversationInfoDirection
    type_:WhatsAppConversationInfo:
      type: object
      properties:
        direction:
          $ref: '#/components/schemas/type_:WhatsAppConversationInfoDirection'
          default: unknown
        whatsapp_phone_number_id:
          type: string
        whatsapp_user_id:
          type: string
        awaiting_first_user_message:
          type: boolean
      required:
        - whatsapp_user_id
      title: WhatsAppConversationInfo
    type_:SmsConversationInfoDirection:
      type: string
      enum:
        - inbound
        - outbound
      title: SmsConversationInfoDirection
    type_:SmsConversationInfo:
      type: object
      properties:
        direction:
          $ref: '#/components/schemas/type_:SmsConversationInfoDirection'
        phone_number_id:
          type: string
        sms_user_phone_number:
          type: string
        agent_phone_number:
          type: string
      required:
        - direction
        - sms_user_phone_number
      title: SmsConversationInfo
    type_:AgentDefinitionSource:
      type: string
      enum:
        - cli
        - ui
        - api
        - template
        - unknown
      default: unknown
      title: AgentDefinitionSource
    type_:ConversationVoiceRewardModel:
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
    type_:ConversationHistoryMetadataCommonModel:
      type: object
      properties:
        start_time_unix_secs:
          type: integer
        accepted_time_unix_secs:
          type: integer
        call_duration_secs:
          type: integer
        cost:
          type: integer
        deletion_settings:
          $ref: '#/components/schemas/type_:ConversationDeletionSettings'
        feedback:
          $ref: '#/components/schemas/type_:ConversationHistoryFeedbackCommonModel'
        authorization_method:
          $ref: '#/components/schemas/type_:AuthorizationMethod'
        charging:
          $ref: '#/components/schemas/type_:ConversationChargingCommonModel'
        phone_call:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryMetadataCommonModelPhoneCall
        batch_call:
          $ref: '#/components/schemas/type_:ConversationHistoryBatchCallModel'
        termination_reason:
          type: string
          default: ''
        error:
          $ref: '#/components/schemas/type_:ConversationHistoryErrorCommonModel'
        warnings:
          type: array
          items:
            type: string
        main_language:
          type: string
        rag_usage:
          $ref: '#/components/schemas/type_:ConversationHistoryRagUsageCommonModel'
        text_only:
          type: boolean
          default: false
        features_usage:
          $ref: '#/components/schemas/type_:FeaturesUsageCommonModel'
        eleven_assistant:
          $ref: >-
            #/components/schemas/type_:ConversationHistoryElevenAssistantCommonModel
        initiator_id:
          type: string
        conversation_initiation_source:
          $ref: '#/components/schemas/type_:ConversationInitiationSource'
        conversation_initiation_source_version:
          type: string
        timezone:
          type: string
        async_metadata:
          $ref: '#/components/schemas/type_:AsyncConversationMetadata'
        whatsapp:
          $ref: '#/components/schemas/type_:WhatsAppConversationInfo'
        sms:
          $ref: '#/components/schemas/type_:SmsConversationInfo'
        agent_created_from:
          $ref: '#/components/schemas/type_:AgentDefinitionSource'
        agent_last_updated_from:
          $ref: '#/components/schemas/type_:AgentDefinitionSource'
        voice_rewards:
          type: array
          items:
            $ref: '#/components/schemas/type_:ConversationVoiceRewardModel'
        cost_fiat:
          type: number
          format: double
          description: >-
            Total fiat cost of the conversation in USD, i.e. the sum of the LLM
            price and the non-LLM platform price (the fiat analogue of
            ``cost``). ``None`` when neither is set (e.g. conversations that
            predate fiat cost tracking).
      required:
        - start_time_unix_secs
        - call_duration_secs
      title: ConversationHistoryMetadataCommonModel
    type_:EvaluationSuccessResult:
      type: string
      enum:
        - success
        - failure
        - unknown
      title: EvaluationSuccessResult
    type_:CriteriaScoringMode:
      type: string
      enum:
        - binary
        - numeric_uniform
      default: binary
      title: CriteriaScoringMode
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
    type_:VisitedAgentRef:
      type: object
      properties:
        agent_id:
          type: string
        branch_id:
          type: string
      required:
        - agent_id
      description: >-
        An agent (and optional branch) that participated in the call, in
        first-seen transcript order.
      title: VisitedAgentRef
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
    type_:ConversationInitiationSourceInfo:
      type: object
      properties:
        source:
          $ref: '#/components/schemas/type_:ConversationInitiationSource'
          description: Source of the conversation initiation
        version:
          type: string
          description: The SDK version number
      description: Information about the source of conversation initiation
      title: ConversationInitiationSourceInfo
    type_:ConversationInitiationClientDataRequestOutput:
      type: object
      properties:
        conversation_config_override:
          $ref: '#/components/schemas/type_:ConversationConfigClientOverrideOutput'
        custom_llm_extra_body:
          type: object
          additionalProperties:
            description: Any type
        user_id:
          type: string
          description: >-
            ID of the end user participating in this conversation (for agent
            owner's user identification)
        source_info:
          $ref: '#/components/schemas/type_:ConversationInitiationSourceInfo'
        branch_id:
          type: string
          description: ID of the agent branch to use for this conversation
        environment:
          type: string
          description: Environment to use for resolving environment variables
        starting_workflow_node_id:
          type: string
          description: >-
            If set, start the workflow at this node id instead of the default
            entry
        dynamic_variables:
          type: object
          additionalProperties:
            description: Any type
      title: ConversationInitiationClientDataRequestOutput
    type_:ConversationHistoryTranscriptResponseModelRole:
      type: string
      enum:
        - user
        - agent
      title: ConversationHistoryTranscriptResponseModelRole
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
                - run_subagent_error
              description: 'Discriminator value: run_subagent_error'
            status:
              type: string
              enum:
                - error
            error:
              type: string
          required:
            - result_type
            - error
        - type: object
          properties:
            result_type:
              type: string
              enum:
                - run_subagent_success
              description: 'Discriminator value: run_subagent_success'
            status:
              type: string
              enum:
                - success
            query:
              type: string
            agent_response:
              type: string
          required:
            - result_type
            - query
            - agent_response
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
    type_:EmbeddingModelEnum:
      type: string
      enum:
        - e5_mistral_7b_instruct
        - multilingual_e5_large_instruct
      default: e5_mistral_7b_instruct
      title: EmbeddingModelEnum
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
    type_:GetConversationResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        agent_name:
          type: string
        conversation_product:
          type: string
          default: agent
        status:
          $ref: '#/components/schemas/type_:GetConversationResponseModelStatus'
        user_id:
          type: string
        branch_id:
          type: string
        version_id:
          type: string
          description: The ID of the agent version used for this conversation
        metadata:
          $ref: '#/components/schemas/type_:ConversationHistoryMetadataCommonModel'
        analysis:
          $ref: '#/components/schemas/type_:ConversationHistoryAnalysisCommonModel'
        visited_agents:
          type: array
          items:
            $ref: '#/components/schemas/type_:VisitedAgentRef'
        conversation_initiation_client_data:
          $ref: >-
            #/components/schemas/type_:ConversationInitiationClientDataRequestOutput
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
            $ref: >-
              #/components/schemas/type_:ConversationHistoryTranscriptResponseModel
        tag_ids:
          type: array
          items:
            type: string
          description: Conversation tag ids assigned to this conversation.
        otlp_traces:
          type: object
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
  "evaluation_id": "evaluation_id"
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
    "accepted_time_unix_secs": 1,
    "cost": 1,
    "deletion_settings": {
      "deletion_time_unix_secs": 1,
      "deleted_logs_at_time_unix_secs": 1,
      "deleted_audio_at_time_unix_secs": 1,
      "deleted_transcript_at_time_unix_secs": 1,
      "delete_transcript_and_pii": true,
      "delete_audio": true
    },
    "feedback": {
      "type": "thumbs",
      "overall_score": "like",
      "likes": 1,
      "dislikes": 1,
      "rating": 1,
      "comment": "comment"
    },
    "authorization_method": "invalid",
    "charging": {
      "dev_discount": true,
      "is_burst": true,
      "tier": "tier",
      "llm_price": 1.1,
      "llm_charge": 1,
      "call_charge": 1,
      "platform_charge": 1,
      "platform_price": 1.1,
      "free_minutes_consumed": 1.1,
      "free_llm_dollars_consumed": 1.1
    },
    "phone_call": {
      "type": "exotel",
      "agent_number": "agent_number",
      "call_sid": "call_sid",
      "direction": "inbound",
      "external_number": "external_number",
      "phone_number_id": "phone_number_id",
      "stream_sid": "stream_sid"
    },
    "batch_call": {
      "batch_call_id": "batch_call_id",
      "batch_call_recipient_id": "batch_call_recipient_id"
    },
    "termination_reason": "termination_reason",
    "error": {
      "code": 1,
      "reason": "reason"
    },
    "warnings": [
      "warnings"
    ],
    "main_language": "main_language",
    "rag_usage": {
      "usage_count": 1,
      "embedding_model": "embedding_model"
    },
    "text_only": true,
    "features_usage": {
      "pii_zrm_workspace": true,
      "pii_zrm_agent": true,
      "is_livekit": true
    },
    "eleven_assistant": {
      "is_eleven_assistant": true
    },
    "initiator_id": "initiator_id",
    "conversation_initiation_source": "unknown",
    "conversation_initiation_source_version": "conversation_initiation_source_version",
    "timezone": "timezone",
    "async_metadata": {
      "delivery_status": "pending",
      "delivery_timestamp": 1,
      "external_system": "external_system",
      "external_id": "external_id",
      "delivery_error": "delivery_error",
      "external_link": "external_link",
      "retry_count": 1,
      "last_retry_timestamp": 1,
      "last_processed_external_message_id": "last_processed_external_message_id"
    },
    "whatsapp": {
      "whatsapp_user_id": "whatsapp_user_id",
      "direction": "inbound",
      "whatsapp_phone_number_id": "whatsapp_phone_number_id",
      "awaiting_first_user_message": true
    },
    "sms": {
      "direction": "inbound",
      "sms_user_phone_number": "sms_user_phone_number",
      "phone_number_id": "phone_number_id",
      "agent_phone_number": "agent_phone_number"
    },
    "agent_created_from": "cli",
    "agent_last_updated_from": "cli",
    "voice_rewards": [
      {
        "voice_id": "voice_id",
        "reward_usd_cents": 1.1
      }
    ],
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
      "agent_metadata": {
        "agent_id": "agent_id"
      },
      "message": "Hello, how are you?",
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
  "agent_name": "My agent",
  "conversation_product": "conversation_product",
  "user_id": "user_id",
  "branch_id": "branch_id",
  "version_id": "agtvrsn_5xM3yVvZQKV0EfqQpLr2",
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
  },
  "visited_agents": [
    {
      "agent_id": "agent_id",
      "branch_id": "branch_id"
    }
  ],
  "conversation_initiation_client_data": {
    "conversation_config_override": {
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
    },
    "custom_llm_extra_body": {
      "key": "value"
    },
    "user_id": "user_id",
    "source_info": {
      "source": "unknown",
      "version": "version"
    },
    "branch_id": "branch_id",
    "environment": "environment",
    "starting_workflow_node_id": "starting_workflow_node_id",
    "dynamic_variables": {
      "key": "value"
    }
  },
  "environment": "production",
  "tag_ids": [
    "tag_ids"
  ],
  "otlp_traces": {
    "key": "value"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.analysis.runEvaluation("conversation_id", {
        evaluationId: "evaluation_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.analysis.run_evaluation(
    conversation_id="conversation_id",
    evaluation_id="evaluation_id",
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

	payload := strings.NewReader("{\n  \"evaluation_id\": \"evaluation_id\"\n}")

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
request.body = "{\n  \"evaluation_id\": \"evaluation_id\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run")
  .header("Content-Type", "application/json")
  .body("{\n  \"evaluation_id\": \"evaluation_id\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/analysis/evaluations/run', [
  'body' => '{
  "evaluation_id": "evaluation_id"
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
request.AddParameter("application/json", "{\n  \"evaluation_id\": \"evaluation_id\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["evaluation_id": "evaluation_id"] as [String : Any]

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
