---
title: "Create test"
source: https://elevenlabs.io/docs/api-reference/tests/create.md
path: docs/api-reference/tests/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create test

POST https://api.elevenlabs.io/v1/convai/agent-testing/create
Content-Type: application/json

Creates a new agent response test.

Reference: https://elevenlabs.io/docs/api-reference/tests/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agent-testing/create:
    post:
      operationId: create
      summary: Create Agent Response Test
      description: Creates a new agent response test.
      tags:
        - subpackage_conversationalAi/tests
      parameters:
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
                $ref: '#/components/schemas/CreateAgentTestResponseModel'
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
              $ref: '#/components/schemas/conversational_ai_tests_create_Request'
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
    TestFromConversationMetadata-Input:
      type: object
      properties:
        conversation_id:
          type: string
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
        original_agent_reply:
          type: array
          items:
            $ref: >-
              #/components/schemas/ConversationHistoryTranscriptCommonModel-Input
          default: []
      required:
        - conversation_id
        - agent_id
      title: TestFromConversationMetadata-Input
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
        - template_preview
        - genesys_bot_connector
      default: unknown
      description: Enum representing the possible sources for conversation initiation.
      title: ConversationInitiationSource
    AgentSuccessfulResponseExample:
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
    AgentFailureResponseExample:
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
    CreateResponseUnitTestRequest:
      type: object
      properties:
        from_conversation_metadata:
          oneOf:
            - $ref: '#/components/schemas/TestFromConversationMetadata-Input'
            - type: 'null'
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
              #/components/schemas/ConversationHistoryTranscriptCommonModel-Input
        conversation_initiation_source:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationSource'
            - type: 'null'
          description: >-
            Simulate the test as if the conversation originated from this
            channel.
        type:
          type: string
          enum:
            - llm
          default: llm
        success_condition:
          type: string
          default: ''
          description: >-
            A prompt that evaluates whether the agent's response is successful.
            Should return True or False.
        success_examples:
          type: array
          items:
            $ref: '#/components/schemas/AgentSuccessfulResponseExample'
          description: >-
            Non-empty list of example responses that should be considered
            successful
        failure_examples:
          type: array
          items:
            $ref: '#/components/schemas/AgentFailureResponseExample'
          description: >-
            Non-empty list of example responses that should be considered
            failures
        name:
          type: string
        parent_folder_id:
          type:
            - string
            - 'null'
          description: >-
            The ID of the parent folder. If not provided, the test will be
            created at the root level.
      required:
        - name
      title: CreateResponseUnitTestRequest
    UnitTestToolCallParameterEval:
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
          description: MatchAnythingParameterEvaluationStrategy variant
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
          description: ExactParameterEvaluationStrategy variant
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
          description: LLMParameterEvaluationStrategy variant
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
          description: RegexParameterEvaluationStrategy variant
      discriminator:
        propertyName: type
      title: UnitTestToolCallParameterEval
    UnitTestToolCallParameter:
      type: object
      properties:
        eval:
          $ref: '#/components/schemas/UnitTestToolCallParameterEval'
        path:
          type: string
      required:
        - eval
        - path
      title: UnitTestToolCallParameter
    ReferencedToolCommonModelType:
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
    ReferencedToolCommonModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the tool
        type:
          $ref: '#/components/schemas/ReferencedToolCommonModelType'
          description: The type of the tool
      required:
        - id
        - type
      description: Reference to a tool for unit test evaluation.
      title: ReferencedToolCommonModel
    UnitTestWorkflowNodeTransitionEvaluationNodeId:
      type: object
      properties:
        type:
          type: string
          enum:
            - node_id
          default: node_id
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
    UnitTestToolCallEvaluationModel-Input:
      type: object
      properties:
        parameters:
          type: array
          items:
            $ref: '#/components/schemas/UnitTestToolCallParameter'
          description: >-
            Parameters to evaluate for the agent's tool call. If empty, the tool
            call parameters are not evaluated.
        referenced_tool:
          oneOf:
            - $ref: '#/components/schemas/ReferencedToolCommonModel'
            - type: 'null'
          description: The tool to evaluate a call against.
        verify_absence:
          type: boolean
          default: false
          description: Whether to verify that the tool was NOT called.
        workflow_node_transition:
          oneOf:
            - $ref: >-
                #/components/schemas/UnitTestWorkflowNodeTransitionEvaluationNodeId
            - type: 'null'
          description: >-
            Configuration for testing workflow node transitions. When set, the
            test will verify the agent transitions to the specified workflow
            node.
      title: UnitTestToolCallEvaluationModel-Input
    CreateToolCallUnitTestRequest:
      type: object
      properties:
        from_conversation_metadata:
          oneOf:
            - $ref: '#/components/schemas/TestFromConversationMetadata-Input'
            - type: 'null'
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
              #/components/schemas/ConversationHistoryTranscriptCommonModel-Input
        conversation_initiation_source:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationSource'
            - type: 'null'
          description: >-
            Simulate the test as if the conversation originated from this
            channel.
        type:
          type: string
          enum:
            - tool
          default: tool
        tool_call_parameters:
          oneOf:
            - $ref: '#/components/schemas/UnitTestToolCallEvaluationModel-Input'
            - type: 'null'
          description: >-
            How to evaluate the agent's tool call (if any). If empty, the tool
            call is not evaluated.
        check_any_tool_matches:
          type:
            - boolean
            - 'null'
          description: >-
            If set to True this test will pass if any tool call returned by the
            LLM matches the criteria. Otherwise it will fail if more than one
            tool is returned by the agent.
        name:
          type: string
        parent_folder_id:
          type:
            - string
            - 'null'
          description: >-
            The ID of the parent folder. If not provided, the test will be
            created at the root level.
      required:
        - name
      title: CreateToolCallUnitTestRequest
    MockingStrategy:
      type: string
      enum:
        - all
        - selected
        - none
      default: none
      title: MockingStrategy
    MockNoMatchBehavior:
      type: string
      enum:
        - call_real_tool
        - raise_error
      default: raise_error
      title: MockNoMatchBehavior
    SimulationToolMockBehaviorConfig:
      type: object
      properties:
        mocking_strategy:
          $ref: '#/components/schemas/MockingStrategy'
          default: none
          description: >-
            Which tools to mock: 'all' mocks every mockable tool, 'selected'
            mocks only those in mocked_tool_names/mocked_tool_ids, 'none'
            disables mocking.
        fallback_strategy:
          $ref: '#/components/schemas/MockNoMatchBehavior'
          default: raise_error
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
    CreateSimulationTestRequest:
      type: object
      properties:
        from_conversation_metadata:
          oneOf:
            - $ref: '#/components/schemas/TestFromConversationMetadata-Input'
            - type: 'null'
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
              #/components/schemas/ConversationHistoryTranscriptCommonModel-Input
        conversation_initiation_source:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationSource'
            - type: 'null'
          description: >-
            Simulate the test as if the conversation originated from this
            channel.
        type:
          type: string
          enum:
            - simulation
          default: simulation
        success_condition:
          type:
            - string
            - 'null'
          description: >-
            Deprecated legacy single success criterion. Use success_conditions
            instead. At least one of success_condition or success_conditions is
            required.
        success_conditions:
          type: array
          items:
            type: string
          description: >-
            List of prompts that evaluate whether the simulation was successful.
            If provided, all criteria are evaluated and merged into a final
            result. Capped at the maximum number of evaluation criteria.
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
          type:
            - string
            - 'null'
          description: >-
            The environment to use when running this simulation test. If not
            provided, defaults to 'production'.
        tool_mock_config:
          $ref: '#/components/schemas/SimulationToolMockBehaviorConfig'
          description: Configuration for which tools to mock and fallback behavior.
        evaluation_model:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
          description: >-
            LLM model to use for evaluating simulation results. Defaults to
            Claude Sonnet 4.6.
        simulated_user_model:
          oneOf:
            - $ref: '#/components/schemas/LLM'
            - type: 'null'
          description: LLM model for the simulated user. Defaults to Claude Sonnet 4.6.
        name:
          type: string
        parent_folder_id:
          type:
            - string
            - 'null'
          description: >-
            The ID of the parent folder. If not provided, the test will be
            created at the root level.
      required:
        - name
      title: CreateSimulationTestRequest
    conversational_ai_tests_create_Request:
      oneOf:
        - $ref: '#/components/schemas/CreateResponseUnitTestRequest'
        - $ref: '#/components/schemas/CreateToolCallUnitTestRequest'
        - $ref: '#/components/schemas/CreateSimulationTestRequest'
      description: Create Chat Response Test Request Information
      title: conversational_ai_tests_create_Request
    CreateAgentTestResponseModel:
      type: object
      properties:
        id:
          type: string
      required:
        - id
      title: CreateAgentTestResponseModel
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
  "name": "string"
}
```

**Response**

```json
{
  "id": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.create();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.create()

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

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/create"

	payload := strings.NewReader("{\n  \"name\": \"string\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/create")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agent-testing/create")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agent-testing/create', [
  'body' => '{
  "name": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/create");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/create")! as URL,
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
