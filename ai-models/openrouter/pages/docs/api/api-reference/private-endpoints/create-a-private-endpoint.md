---
title: "Create a private endpoint"
source: https://openrouter.ai/docs/api/api-reference/private-endpoints/create-a-private-endpoint.md
path: docs/api/api-reference/private-endpoints/create-a-private-endpoint
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a private endpoint

> Create a private endpoint as a draft. Drafts are not routable: validate one with `POST /private-endpoints/{id}/validate`, then activate it with `POST /private-endpoints/{id}/activate`. Pass `activate` to do all three in one call; if validation fails the draft is kept and returned with the failed checks. Send an `Idempotency-Key` header to make retries safe: a repeated key with the same request returns the endpoint the first request created; reusing it with different fields returns 422 `idempotency_key_reused`. [Management key](/docs/guides/overview/auth/management-api-keys) required.



## OpenAPI

````yaml /openapi/openapi.yaml post /private-endpoints
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
  - description: End Users endpoints
    name: End Users
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
  /private-endpoints:
    post:
      tags:
        - Private Endpoints
      summary: Create a private endpoint
      description: >-
        Create a private endpoint as a draft. Drafts are not routable: validate
        one with `POST /private-endpoints/{id}/validate`, then activate it with
        `POST /private-endpoints/{id}/activate`. Pass `activate` to do all three
        in one call; if validation fails the draft is kept and returned with the
        failed checks. Send an `Idempotency-Key` header to make retries safe: a
        repeated key with the same request returns the endpoint the first
        request created; reusing it with different fields returns 422
        `idempotency_key_reused`. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      operationId: createPrivateEndpoint
      parameters:
        - description: >-
            Retry-safe create: a repeated create with the same key from the same
            organization returns the endpoint the first request created instead
            of creating another. The endpoint is returned as it is now. Reusing
            a key with a different request body (model, provider, base URL,
            upstream model ID, declared ZDR or region, or pricing) is rejected
            with 422 `idempotency_key_reused`. `activate` is not compared, and
            later edits to the endpoint do not affect the comparison.
          in: header
          name: idempotency-key
          required: false
          schema:
            description: >-
              Retry-safe create: a repeated create with the same key from the
              same organization returns the endpoint the first request created
              instead of creating another. The endpoint is returned as it is
              now. Reusing a key with a different request body (model, provider,
              base URL, upstream model ID, declared ZDR or region, or pricing)
              is rejected with 422 `idempotency_key_reused`. `activate` is not
              compared, and later edits to the endpoint do not affect the
              comparison.
            example: wayfair-gpt-4o-eastus-2026-09
            maxLength: 255
            minLength: 1
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreatePrivateEndpointRequest'
        required: true
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ManagedPrivateEndpointResponse'
          description: 'The created endpoint: a draft, or active when `activate` was passed'
        '400':
          content:
            application/json:
              example:
                error:
                  code: 400
                  message: Invalid request parameters
              schema:
                $ref: '#/components/schemas/BadRequestResponse'
          description: Bad Request - Invalid request parameters or malformed input
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
              schema:
                anyOf:
                  - $ref: >-
                      #/components/schemas/CreatePrivateEndpointValidationFailedResponse
                  - $ref: '#/components/schemas/NotFoundResponse'
          description: >-
            The model, provider, or validation workspace was not found. When
            `activate` was passed and the draft was created, `data` carries it
            and any validation checks.
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
        '409':
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: >-
                      #/components/schemas/CreatePrivateEndpointValidationFailedResponse
                  - $ref: '#/components/schemas/ConflictResponse'
          description: >-
            The request conflicts with the endpoint state, such as a stale
            validation. When `activate` was passed and the draft was created,
            `data` carries it and any validation checks.
        '422':
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: >-
                      #/components/schemas/CreatePrivateEndpointValidationFailedResponse
                  - $ref: '#/components/schemas/UnprocessableEntityResponse'
          description: >-
            The request was invalid, or validation failed. When `activate` was
            passed and the draft was created, `data` carries it and any
            validation checks.
        '500':
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: >-
                      #/components/schemas/CreatePrivateEndpointValidationFailedResponse
                  - $ref: '#/components/schemas/InternalServerResponse'
          description: >-
            Internal server error. When `activate` was passed and the draft was
            created, `data` carries it and any validation checks.
        '502':
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: >-
                      #/components/schemas/CreatePrivateEndpointValidationFailedResponse
                  - $ref: '#/components/schemas/BadGatewayResponse'
          description: >-
            An upstream dependency failed. When `activate` was passed and the
            draft was created, `data` carries it and any validation checks.
components:
  schemas:
    CreatePrivateEndpointRequest:
      properties:
        activate:
          $ref: '#/components/schemas/PrivateEndpointActivation'
        base_url:
          description: >-
            HTTPS base URL of your deployment. Required unless the provider
            derives its URL from the BYOK credential (Azure, Amazon Bedrock,
            Google Vertex).
          example: https://contoso.openai.azure.com
          minLength: 1
          type: string
        declared_region:
          description: Attest where this deployment processes data.
          enum:
            - global
            - europe
            - us
            - null
          example: us
          type:
            - string
            - 'null'
        declared_zdr:
          description: Attest that this deployment retains no prompt or completion data.
          type:
            - boolean
            - 'null'
        model_permaslug:
          description: Permanent slug of the model this endpoint serves.
          example: openai/gpt-4o-2024-08-06
          minLength: 1
          type: string
        pricing:
          $ref: '#/components/schemas/PrivateEndpointPricing'
        provider_slug:
          description: Slug of the upstream provider.
          example: azure
          minLength: 1
          type: string
        upstream_model_id:
          description: Model or deployment identifier sent to the upstream provider.
          example: gpt-4o-prod
          minLength: 1
          type: string
      required:
        - model_permaslug
        - provider_slug
        - upstream_model_id
      type: object
    ManagedPrivateEndpointResponse:
      properties:
        data:
          $ref: '#/components/schemas/ManagedPrivateEndpoint'
      required:
        - data
      type: object
    BadRequestResponse:
      description: Bad Request - Invalid request parameters or malformed input
      example:
        error:
          code: 400
          message: Invalid request parameters
      properties:
        error:
          $ref: '#/components/schemas/BadRequestResponseErrorData'
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
    CreatePrivateEndpointValidationFailedResponse:
      properties:
        data:
          properties:
            endpoint:
              $ref: '#/components/schemas/ManagedPrivateEndpoint'
            validation:
              $ref: '#/components/schemas/PrivateEndpointValidationNullable'
          required:
            - endpoint
            - validation
          type: object
        error:
          properties:
            code:
              type: integer
            message:
              type: string
          required:
            - code
            - message
          type: object
      required:
        - error
        - data
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
    ConflictResponse:
      description: Conflict - Resource conflict or concurrent modification
      example:
        error:
          code: 409
          message: Resource conflict. Please try again later.
      properties:
        error:
          $ref: '#/components/schemas/ConflictResponseErrorData'
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
    UnprocessableEntityResponse:
      description: Unprocessable Entity - Semantic validation failure
      example:
        error:
          code: 422
          message: Invalid argument
      properties:
        error:
          $ref: '#/components/schemas/UnprocessableEntityResponseErrorData'
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
    BadGatewayResponse:
      description: Bad Gateway - Provider/upstream API failure
      example:
        error:
          code: 502
          message: Provider returned error
      properties:
        error:
          $ref: '#/components/schemas/BadGatewayResponseErrorData'
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
    PrivateEndpointActivation:
      description: >-
        Validate and activate in the same call. On a failed validation the draft
        is kept and returned with a 422, so fix it and call `/validate` and
        `/activate` instead of creating it again.
      example:
        workspace_id: 550e8400-e29b-41d4-a716-446655440000
      properties:
        workspace_id:
          description: >-
            Workspace whose BYOK credential is used for the live validation
            call. The workspace must belong to your account.
          example: 550e8400-e29b-41d4-a716-446655440000
          format: uuid
          type: string
      required:
        - workspace_id
      type: object
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
    ManagedPrivateEndpoint:
      allOf:
        - $ref: '#/components/schemas/PrivateEndpointSummary'
        - properties:
            declared_region:
              $ref: '#/components/schemas/PrivateEndpointDeclaredRegion'
            declared_zdr:
              description: >-
                Whether you attest this deployment retains no prompt or
                completion data. `null` means undeclared.
              example: true
              type:
                - boolean
                - 'null'
          required:
            - declared_zdr
            - declared_region
          type: object
    BadRequestResponseErrorData:
      description: Error data for BadRequestResponse
      example:
        code: 400
        message: Invalid request parameters
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
    PrivateEndpointValidationNullable:
      properties:
        checks:
          items:
            $ref: '#/components/schemas/PrivateEndpointCheck'
          type: array
        passed:
          description: Whether every check passed.
          example: true
          type: boolean
      required:
        - passed
        - checks
      type:
        - object
        - 'null'
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
    ConflictResponseErrorData:
      description: Error data for ConflictResponse
      example:
        code: 409
        message: Resource conflict. Please try again later.
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
    UnprocessableEntityResponseErrorData:
      description: Error data for UnprocessableEntityResponse
      example:
        code: 422
        message: Invalid argument
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
    BadGatewayResponseErrorData:
      description: Error data for BadGatewayResponse
      example:
        code: 502
        message: Provider returned error
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
    PrivateEndpointSummary:
      properties:
        created_at:
          description: ISO timestamp of when the endpoint was created.
          example: '2026-09-24T10:30:00Z'
          type: string
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
        provider_name:
          description: Display name of the upstream provider.
          example: Azure
          type: string
        status:
          $ref: '#/components/schemas/PrivateEndpointStatus'
      required:
        - id
        - status
        - model_permaslug
        - model_slug
        - model_name
        - provider_name
        - created_at
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
    PrivateEndpointCheck:
      example:
        name: auth_ok
        passed: true
      properties:
        actual_model:
          description: >-
            Model the upstream reported serving, when it differs from the
            request.
          type:
            - string
            - 'null'
        name:
          description: Check name.
          example: auth_ok
          type: string
        passed:
          type: boolean
        reason:
          $ref: '#/components/schemas/PrivateEndpointCheckReason'
        upstream_message:
          description: Error message returned by your deployment when the call failed.
          type:
            - string
            - 'null'
        upstream_status:
          description: HTTP status returned by your deployment when the call failed.
          maximum: 599
          minimum: 400
          type: integer
      required:
        - name
        - passed
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
    PrivateEndpointCheckReason:
      description: Why the check failed.
      enum:
        - database_error
        - endpoint_limit_reached
        - invalid_base_url
        - model_not_found
        - provider_not_found
        - endpoint_not_found
        - workspace_not_found
        - no_byok_key
        - key_decryption_failed
        - upstream_error
        - invalid_response
        - invalid_stream
        - missing_usage
        - model_mismatch
        - not_validated
        - validation_stale
      example: no_byok_key
      type: string
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
