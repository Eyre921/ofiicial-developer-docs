---
title: "Get a private endpoint"
source: https://openrouter.ai/docs/api/api-reference/private-endpoints/get-a-private-endpoint.md
path: docs/api/api-reference/private-endpoints/get-a-private-endpoint
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a private endpoint

> Get one private endpoint with its upstream configuration and current pricing. [Management key](/docs/guides/overview/auth/management-api-keys) required.



## OpenAPI

````yaml /openapi/openapi.yaml get /private-endpoints/{id}
openapi: 3.1.0
info:
  contact:
    email: support@openrouter.ai
    name: OpenRouter Support
    url: https://openrouter.ai/docs
  description: OpenAI-compatible API with additional OpenRouter features
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
  title: OpenRouter API
  version: 1.0.0
servers:
  - description: Production server
    url: https://openrouter.ai/api/v1
    x-speakeasy-server-id: production
security:
  - apiKey: []
tags:
  - description: API key management endpoints
    name: API Keys
  - description: Analytics and usage endpoints
    name: Analytics
  - description: Anthropic Messages endpoints
    name: Anthropic Messages
  - description: BYOK endpoints
    name: BYOK
  - description: >-
      Submit, list, poll, and delete asynchronous batches of inference requests.
      See https://openrouter.ai/docs/batch-quickstart.
    name: Batch
  - description: Benchmarks endpoints
    name: Benchmarks
  - description: Chat completion endpoints
    name: Chat
  - description: Task classification market-share endpoints
    name: Classifications
  - description: Containers endpoints
    name: Containers
  - description: Credit management endpoints
    name: Credits
  - description: >-
      Public OpenRouter usage datasets. Data returned by these endpoints is
      licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/):
      reuse and republish it, including commercially, with attribution to
      OpenRouter.
    name: Datasets
  - description: Text embedding endpoints
    name: Embeddings
  - description: Endpoint information
    name: Endpoints
  - description: Files endpoints
    name: Files
  - description: Generation history endpoints
    name: Generations
  - description: Guardrails endpoints
    name: Guardrails
  - description: Images endpoints
    name: Images
  - description: >-
      Create, inspect, update, provision, suspend and delete OpenRouter interns
      through an API key, and talk to them: the chat route streams
      OpenAI-compatible completions from one intern, pausing as an
      `openrouter.provide_input` tool call when the intern needs your permission
      or an answer. Available to interns programme members; other callers
      receive 404. See https://openrouter.ai/docs/guides/ori/intern-chat.
    name: Interns
  - description: Model information endpoints
    name: Models
  - description: OAuth authentication endpoints
    name: OAuth
  - description: Observability endpoints
    name: Observability
  - description: Organization endpoints
    name: Organization
  - description: Presets endpoints
    name: Presets
  - description: Private Endpoints endpoints
    name: Private Endpoints
  - description: Provider information endpoints
    name: Providers
  - description: Rerank endpoints
    name: Rerank
  - description: OpenAI-compatible Responses API endpoints
    name: Responses
  - description: >-
      Management endpoints for SCIM group-to-workspace mappings, authenticated
      with a management key. These are not the SCIM 2.0 connector endpoints for
      your identity provider. In your identity provider, enter the SCIM endpoint
      URL shown when you enable provisioning under Settings > Members > SCIM
      Mappings. See
      https://openrouter.ai/docs/guides/features/scim-mappings#set-up-provisioning.
    name: SCIM
  - description: Speech-to-text endpoints
    name: STT
    x-displayName: Transcriptions
  - description: >-
      System One endpoints for models such as Jev, compatible with the TypeSafe
      SDKs. See https://openrouter.ai/docs/guides/community/typesafe-sdk.
    name: SystemOne
    x-displayName: System One
  - description: Text-to-speech endpoints
    name: TTS
    x-displayName: Speech
  - description: >-
      The catalog of server tools OpenRouter runs on behalf of a model: accepted
      `tools[].type` spellings per API format, engines and pricing, and which
      endpoints run each tool natively. See
      https://openrouter.ai/docs/guides/features/server-tools.
    name: Tools
  - description: >-
      Store host-bound secrets for a workspace or for one intern. Scope is
      selected by the API key. Responses return metadata only, never secret
      values. See https://openrouter.ai/docs/guides/ori/vault.
    name: Vault
  - description: Video Generation endpoints
    name: Video Generation
  - description: Workspaces endpoints
    name: Workspaces
  - description: Alpha feature endpoints for Decisions requests
    name: alpha.decisions
externalDocs:
  description: OpenRouter Documentation
  url: https://openrouter.ai/docs
paths:
  /private-endpoints/{id}:
    get:
      tags:
        - Private Endpoints
      summary: Get a private endpoint
      description: >-
        Get one private endpoint with its upstream configuration and current
        pricing. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      operationId: getPrivateEndpoint
      parameters:
        - description: Stable identifier of the private endpoint.
          in: path
          name: id
          required: true
          schema:
            description: Stable identifier of the private endpoint.
            example: 5b1c4c4e-7d0a-4a8e-9f3a-2d6c1b0e8a11
            format: uuid
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateEndpointResponse'
          description: The private endpoint
        '401':
          content:
            application/json:
              example:
                error:
                  code: 401
                  message: Missing Authentication header
              schema:
                $ref: '#/components/schemas/UnauthorizedResponse'
          description: Unauthorized - Authentication required or invalid credentials
        '403':
          content:
            application/json:
              example:
                error:
                  code: 403
                  message: Only management keys can perform this operation
              schema:
                $ref: '#/components/schemas/ForbiddenResponse'
          description: Forbidden - Authentication successful but insufficient permissions
        '404':
          content:
            application/json:
              example:
                error:
                  code: 404
                  message: Resource not found
              schema:
                $ref: '#/components/schemas/NotFoundResponse'
          description: Not Found - Resource does not exist
        '408':
          content:
            application/json:
              example:
                error:
                  code: 408
                  message: Operation timed out. Please try again later.
              schema:
                $ref: '#/components/schemas/RequestTimeoutResponse'
          description: Request Timeout - Operation exceeded time limit
        '500':
          content:
            application/json:
              example:
                error:
                  code: 500
                  message: Internal Server Error
              schema:
                $ref: '#/components/schemas/InternalServerResponse'
          description: Internal Server Error - Unexpected server error
components:
  schemas:
    PrivateEndpointResponse:
      properties:
        data:
          $ref: '#/components/schemas/PrivateEndpoint'
      required:
        - data
      type: object
    UnauthorizedResponse:
      description: Unauthorized - Authentication required or invalid credentials
      example:
        error:
          code: 401
          message: Missing Authentication header
      properties:
        error:
          $ref: '#/components/schemas/UnauthorizedResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    ForbiddenResponse:
      description: Forbidden - Authentication successful but insufficient permissions
      example:
        error:
          code: 403
          message: Only management keys can perform this operation
      properties:
        error:
          $ref: '#/components/schemas/ForbiddenResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    NotFoundResponse:
      description: Not Found - Resource does not exist
      example:
        error:
          code: 404
          message: Resource not found
      properties:
        error:
          $ref: '#/components/schemas/NotFoundResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    RequestTimeoutResponse:
      description: Request Timeout - Operation exceeded time limit
      example:
        error:
          code: 408
          message: Operation timed out. Please try again later.
      properties:
        error:
          $ref: '#/components/schemas/RequestTimeoutResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    InternalServerResponse:
      description: Internal Server Error - Unexpected server error
      example:
        error:
          code: 500
          message: Internal Server Error
      properties:
        error:
          $ref: '#/components/schemas/InternalServerResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    PrivateEndpoint:
      example:
        base_url: https://contoso.openai.azure.com
        declared_region: us
        declared_zdr: true
        id: 5b1c4c4e-7d0a-4a8e-9f3a-2d6c1b0e8a11
        model_name: 'OpenAI: GPT-4o'
        model_permaslug: openai/gpt-4o-2024-08-06
        model_slug: openai/gpt-4o
        pricing:
          completion: '0.00001'
          prompt: '0.0000025'
        provider_name: Azure
        provider_slug: azure
        status: active
        upstream_model_id: gpt-4o-prod
      properties:
        base_url:
          description: >-
            HTTPS base URL of your deployment, or `null` for providers whose URL
            is derived from the BYOK credential (Azure, Amazon Bedrock, Google
            Vertex).
          example: https://contoso.openai.azure.com
          type:
            - string
            - 'null'
        declared_region:
          $ref: '#/components/schemas/PrivateEndpointDeclaredRegion'
        declared_zdr:
          description: >-
            Whether you attest this deployment retains no prompt or completion
            data. `null` means undeclared.
          example: true
          type:
            - boolean
            - 'null'
        id:
          description: Stable identifier of the private endpoint.
          example: 5b1c4c4e-7d0a-4a8e-9f3a-2d6c1b0e8a11
          format: uuid
          type: string
        model_name:
          description: >-
            Display name of the model, or `null` when the model is no longer
            listed.
          example: 'OpenAI: GPT-4o'
          type:
            - string
            - 'null'
        model_permaslug:
          description: Permanent slug of the model this endpoint serves.
          example: openai/gpt-4o-2024-08-06
          type: string
        model_slug:
          description: Public model slug, or `null` when the model is no longer listed.
          example: openai/gpt-4o
          type:
            - string
            - 'null'
        pricing:
          $ref: '#/components/schemas/PrivateEndpointPricing'
        provider_name:
          description: Display name of the upstream provider.
          example: Azure
          type: string
        provider_slug:
          description: >-
            Slug of the upstream provider, or `null` when the provider is no
            longer listed.
          example: azure
          type:
            - string
            - 'null'
        status:
          $ref: '#/components/schemas/PrivateEndpointStatus'
        upstream_model_id:
          description: Model or deployment identifier sent to the upstream provider.
          example: gpt-4o-prod
          type: string
      required:
        - id
        - status
        - model_permaslug
        - model_slug
        - model_name
        - provider_name
        - provider_slug
        - base_url
        - upstream_model_id
        - declared_zdr
        - declared_region
        - pricing
      type: object
    UnauthorizedResponseErrorData:
      description: Error data for UnauthorizedResponse
      example:
        code: 401
        message: Missing Authentication header
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    ForbiddenResponseErrorData:
      description: Error data for ForbiddenResponse
      example:
        code: 403
        message: Only management keys can perform this operation
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    NotFoundResponseErrorData:
      description: Error data for NotFoundResponse
      example:
        code: 404
        message: Resource not found
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    RequestTimeoutResponseErrorData:
      description: Error data for RequestTimeoutResponse
      example:
        code: 408
        message: Operation timed out. Please try again later.
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    InternalServerResponseErrorData:
      description: Error data for InternalServerResponse
      example:
        code: 500
        message: Internal Server Error
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    PrivateEndpointDeclaredRegion:
      description: >-
        Where you attest this deployment processes data. `global` means not
        regional; `null` means undeclared.
      enum:
        - global
        - europe
        - us
        - null
      example: us
      type:
        - string
        - 'null'
    PrivateEndpointPricing:
      description: >-
        Negotiated per-token rates reported for requests routed to this
        endpoint.
      example:
        completion: '0.00001'
        prompt: '0.0000025'
      properties:
        completion:
          description: USD per completion token, as a decimal string.
          example: '0.00001'
          pattern: ^\d+(\.\d+)?$
          type: string
        prompt:
          description: USD per prompt token, as a decimal string.
          example: '0.0000025'
          pattern: ^\d+(\.\d+)?$
          type: string
      required:
        - prompt
        - completion
      type: object
    PrivateEndpointStatus:
      description: >-
        Lifecycle state. `draft` endpoints are not routable until validated and
        activated; `disabled` endpoints are activated but temporarily not
        routable.
      enum:
        - draft
        - active
        - disabled
      example: active
      type: string
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
