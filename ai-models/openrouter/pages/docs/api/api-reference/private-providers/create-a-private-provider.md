---
title: "Create a private provider"
source: https://openrouter.ai/docs/api/api-reference/private-providers/create-a-private-provider.md
path: docs/api/api-reference/private-providers/create-a-private-provider
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a private provider

> Create a private, bring-your-own-key provider visible only to your organization. Use its slug as `provider_slug` when creating private endpoints. Requires both the private endpoints and the private providers entitlements. [Management key](/docs/guides/overview/auth/management-api-keys) required.



## OpenAPI

````yaml /openapi/openapi.yaml post /private-providers
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
  - description: External Users endpoints
    name: External Users
  - description: Files endpoints
    name: Files
  - description: Generation history endpoints
    name: Generations
  - description: Guardrails endpoints
    name: Guardrails
  - description: Images endpoints
    name: Images
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
  - description: Private Providers endpoints
    name: Private Providers
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
  /private-providers:
    post:
      tags:
        - Private Providers
      summary: Create a private provider
      description: >-
        Create a private, bring-your-own-key provider visible only to your
        organization. Use its slug as `provider_slug` when creating private
        endpoints. Requires both the private endpoints and the private providers
        entitlements. [Management
        key](/docs/guides/overview/auth/management-api-keys) required.
      operationId: createPrivateProvider
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreatePrivateProviderRequest'
        required: true
      responses:
        '201':
          content:
            application/json:
              schema:
                properties:
                  data:
                    $ref: '#/components/schemas/PrivateProvider'
                required:
                  - data
                type: object
          description: The provider was created
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
        '409':
          content:
            application/json:
              example:
                error:
                  code: 409
                  message: Resource conflict. Please try again later.
              schema:
                $ref: '#/components/schemas/ConflictResponse'
          description: Conflict - Resource conflict or concurrent modification
        '422':
          content:
            application/json:
              example:
                error:
                  code: 422
                  message: Invalid argument
              schema:
                $ref: '#/components/schemas/UnprocessableEntityResponse'
          description: Unprocessable Entity - Semantic validation failure
        '429':
          content:
            application/json:
              example:
                error:
                  code: 429
                  message: Rate limit exceeded
              schema:
                $ref: '#/components/schemas/TooManyRequestsResponse'
          description: Too Many Requests - Rate limit exceeded
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
        '502':
          content:
            application/json:
              example:
                error:
                  code: 502
                  message: Provider returned error
              schema:
                $ref: '#/components/schemas/BadGatewayResponse'
          description: Bad Gateway - Provider/upstream API failure
components:
  schemas:
    CreatePrivateProviderRequest:
      properties:
        base_url:
          description: >-
            HTTPS base URL of an OpenAI-compatible API, used by private
            endpoints under this provider that set no URL of their own. Without
            it, each endpoint must set its own. Private, internal, metadata and
            OpenRouter hosts are rejected.
          example: https://inference.example.com/v1
          minLength: 1
          type: string
        data_policy:
          $ref: '#/components/schemas/PrivateProviderDataPolicy'
        display_name:
          description: Defaults to `name`.
          example: Acme
          maxLength: 80
          minLength: 1
          type: string
        name:
          description: >-
            Provider name, shown in your activity, logs and Broadcast output.
            2-64 letters, numbers, spaces, dots, underscores or hyphens. Cannot
            be changed later. Neither the name nor its slug may match a public
            provider name or slug (case-insensitive); other customers may use
            the same name.
          example: Acme
          maxLength: 64
          minLength: 2
          pattern: ^[A-Za-z0-9][A-Za-z0-9 ._-]*$
          type: string
        slug:
          description: >-
            2-64 lowercase letters and numbers, separated by single hyphens.
            Cannot be changed later. Defaults to the name lowercased, with every
            run of other characters replaced by a hyphen (`Acme Inference`
            becomes `acme-inference`).
          example: acme
          maxLength: 64
          minLength: 2
          pattern: ^[a-z0-9]+(?:-[a-z0-9]+)*$
          type: string
      required:
        - name
      type: object
    PrivateProvider:
      example:
        base_url: https://inference.example.com/v1
        created_at: '2026-10-06T12:00:00.000Z'
        data_policy:
          prompt_retention_days: null
          retains_prompts: false
          training: false
        display_name: Acme
        name: Acme
        slug: acme
      properties:
        base_url:
          description: >-
            HTTPS base URL of an OpenAI-compatible API, used by private
            endpoints under this provider that set no URL of their own. Without
            it, each endpoint must set its own. Private, internal, metadata and
            OpenRouter hosts are rejected.
          example: https://inference.example.com/v1
          minLength: 1
          type:
            - string
            - 'null'
        created_at:
          type: string
        data_policy:
          description: Your declared data policy, or `null` when none was declared.
          properties:
            prompt_retention_days:
              description: >-
                Days prompts are retained. Must be `null` unless
                `retains_prompts` is true.
              maximum: 3650
              minimum: 1
              type:
                - integer
                - 'null'
            retains_prompts:
              description: Whether the provider retains prompts or completions.
              type: boolean
            training:
              description: Whether the provider trains on prompts.
              type: boolean
          required:
            - training
            - retains_prompts
            - prompt_retention_days
          type:
            - object
            - 'null'
        display_name:
          description: Human-readable provider name shown in the UI.
          example: Acme
          type: string
        name:
          description: Provider name, shown in your activity, logs and Broadcast output.
          example: Acme
          type: string
        slug:
          description: >-
            The slug you chose, unique within your account. Use it as
            `provider_slug` when creating private endpoints and BYOK keys, and
            in `provider.order`, `only` and `ignore`.
          example: acme
          type: string
      required:
        - name
        - slug
        - display_name
        - base_url
        - data_policy
        - created_at
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
    TooManyRequestsResponse:
      description: Too Many Requests - Rate limit exceeded
      example:
        error:
          code: 429
          message: Rate limit exceeded
      properties:
        error:
          $ref: '#/components/schemas/TooManyRequestsResponseErrorData'
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
    PrivateProviderDataPolicy:
      description: >-
        Defaults to training on and retaining prompts, the most conservative
        declaration. Your own declaration; it applies to your own traffic and
        OpenRouter does not verify it.
      example:
        prompt_retention_days: null
        retains_prompts: false
        training: false
      properties:
        prompt_retention_days:
          description: >-
            Days prompts are retained. Must be `null` unless `retains_prompts`
            is true.
          maximum: 3650
          minimum: 1
          type:
            - integer
            - 'null'
        retains_prompts:
          description: Whether the provider retains prompts or completions.
          type: boolean
        training:
          description: Whether the provider trains on prompts.
          type: boolean
      required:
        - training
        - retains_prompts
        - prompt_retention_days
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
    TooManyRequestsResponseErrorData:
      description: Error data for TooManyRequestsResponse
      example:
        code: 429
        message: Rate limit exceeded
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
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
