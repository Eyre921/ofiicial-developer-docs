---
title: "Register an end user"
source: https://openrouter.ai/docs/api/api-reference/end-users/register-an-end-user.md
path: docs/api/api-reference/end-users/register-an-end-user
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Register an end user

> Register a caller-supplied tracking ID under the authenticated organization. No login account, policy, or credentials are created. [Management key](/docs/guides/overview/auth/management-api-keys) required.



## OpenAPI

````yaml /openapi/openapi.yaml post /end-users
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
  /end-users:
    post:
      tags:
        - End Users
      summary: Register an end user
      description: >-
        Register a caller-supplied tracking ID under the authenticated
        organization. No login account, policy, or credentials are created.
        [Management key](/docs/guides/overview/auth/management-api-keys)
        required.
      operationId: createEndUser
      requestBody:
        content:
          application/json:
            example:
              user: employee_123
            schema:
              $ref: '#/components/schemas/CreateEndUserRequest'
        required: true
      responses:
        '201':
          content:
            application/json:
              example:
                data:
                  created_at: '2026-09-16T12:00:00Z'
                  is_active: true
                  updated_at: '2026-09-16T12:00:00Z'
                  user: employee_123
              schema:
                $ref: '#/components/schemas/EndUserResponse'
          description: The registered end user. No generated public identifier is returned.
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
        '409':
          content:
            application/json:
              example:
                error:
                  code: 409
                  message: This tracking ID is already registered
              schema:
                $ref: '#/components/schemas/ConflictResponse'
          description: >-
            The tracking ID is already registered in this organization, active
            or not.
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
    CreateEndUserRequest:
      additionalProperties: false
      example:
        user: employee_123
      properties:
        user:
          description: >-
            Immutable case-sensitive tracking string supplied as user on
            inference requests. URL-encode it in resource paths.
          example: employee_123
          maxLength: 256
          minLength: 1
          pattern: ^[^\p{Cc}]+$
          type: string
      required:
        - user
      type: object
    EndUserResponse:
      example:
        data:
          created_at: '2026-09-16T12:00:00Z'
          is_active: true
          updated_at: '2026-09-16T12:00:00Z'
          user: employee_123
      properties:
        data:
          $ref: '#/components/schemas/EndUser'
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
    EndUser:
      additionalProperties: false
      example:
        created_at: '2026-09-16T12:00:00Z'
        is_active: true
        updated_at: '2026-09-16T12:00:00Z'
        user: employee_123
      properties:
        created_at:
          description: Registration creation time.
          example: '2026-09-16T12:00:00Z'
          format: date-time
          type: string
        is_active:
          description: >-
            Whether this registration is active. Not an inference authorization
            decision.
          example: true
          type: boolean
        updated_at:
          description: Last registration lifecycle update time.
          example: '2026-09-16T12:00:00Z'
          format: date-time
          type: string
        user:
          description: >-
            Immutable case-sensitive tracking string supplied as user on
            inference requests. URL-encode it in resource paths.
          example: employee_123
          maxLength: 256
          minLength: 1
          pattern: ^[^\p{Cc}]+$
          type: string
      required:
        - user
        - is_active
        - created_at
        - updated_at
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
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
