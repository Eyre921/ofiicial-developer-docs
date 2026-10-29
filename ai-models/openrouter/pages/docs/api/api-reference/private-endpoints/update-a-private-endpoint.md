---
title: "Update a private endpoint"
source: https://openrouter.ai/docs/api/api-reference/private-endpoints/update-a-private-endpoint.md
path: docs/api/api-reference/private-endpoints/update-a-private-endpoint
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a private endpoint

> Change any of the endpoint fields you own in one call; only the fields present change, and the response is the whole endpoint. `pricing` and `declared_parameters` replace their stored value, `settings` changes only the fields it names (`null` clears a limit or restores the provider default); routing picks these up for subsequent requests on drafts and active endpoints alike. `upstream_model_id`, `base_url`, `declared_zdr` and `declared_region` re-point a draft: an omitted `upstream_model_id` or `base_url` keeps the stored one, omitted data-policy declarations are kept while the upstream is unchanged and cleared when it changes, and any upstream change clears earlier validation. Naming an upstream field on an active endpoint returns 409 `already_active` and writes nothing; delete and re-create instead. Every group is checked before anything is written: 400 `parameters_invalid` when `tool_choice` is declared without `tools` tested or declared, 400 `settings_invalid` when `max_prompt_tokens` exceeds the context length, both completion APIs are off, or `excluded_parameters` names a tested parameter, 422 `pricing_invalid` for rates the provider strategy cannot represent. [Management key](/docs/guides/overview/auth/management-api-keys) required.



## OpenAPI

````yaml /openapi/openapi.yaml patch /private-endpoints/{id}
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
  /private-endpoints/{id}:
    patch:
      tags:
        - Private Endpoints
      summary: Update a private endpoint
      description: >-
        Change any of the endpoint fields you own in one call; only the fields
        present change, and the response is the whole endpoint. `pricing` and
        `declared_parameters` replace their stored value, `settings` changes
        only the fields it names (`null` clears a limit or restores the provider
        default); routing picks these up for subsequent requests on drafts and
        active endpoints alike. `upstream_model_id`, `base_url`, `declared_zdr`
        and `declared_region` re-point a draft: an omitted `upstream_model_id`
        or `base_url` keeps the stored one, omitted data-policy declarations are
        kept while the upstream is unchanged and cleared when it changes, and
        any upstream change clears earlier validation. Naming an upstream field
        on an active endpoint returns 409 `already_active` and writes nothing;
        delete and re-create instead. Every group is checked before anything is
        written: 400 `parameters_invalid` when `tool_choice` is declared without
        `tools` tested or declared, 400 `settings_invalid` when
        `max_prompt_tokens` exceeds the context length, both completion APIs are
        off, or `excluded_parameters` names a tested parameter, 422
        `pricing_invalid` for rates the provider strategy cannot represent.
        [Management key](/docs/guides/overview/auth/management-api-keys)
        required.
      operationId: updatePrivateEndpoint
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdatePrivateEndpointRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateEndpointResponse'
          description: The updated endpoint
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
    UpdatePrivateEndpointRequest:
      description: >-
        Only the fields present change. `base_url`, `upstream_model_id`,
        `declared_zdr` and `declared_region` are accepted on a draft only;
        `pricing` and `declared_parameters` replace their value; `settings` is
        itself a partial update where `null` clears a limit or restores the
        provider default.
      example:
        declared_parameters:
          - seed
        settings:
          context_length: 128000
      properties:
        base_url:
          description: >-
            HTTPS base URL of your deployment. Required unless the provider
            derives its URL from the BYOK credential (Azure, Amazon Bedrock,
            Google Vertex).
          example: https://contoso.openai.azure.com
          minLength: 1
          type: string
        declared_parameters:
          description: >-
            Parameters the upstream supports beyond the tested ones. Replaces
            the earlier declaration; tested parameters stay. Order and repeated
            names are ignored, but the list holds at most as many entries as
            there are declarable parameters, repeats included. `tool_choice`
            requires `tools` to be tested or declared.
          example:
            - temperature
            - seed
          items:
            $ref: '#/components/schemas/PrivateEndpointDeclaredParameter'
          maxItems: 25
          type: array
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
        pricing:
          allOf:
            - $ref: '#/components/schemas/PrivateEndpointPricing'
            - description: >-
                Replaces the whole pricing object: omitting `cache_read` or
                `cache_write` reverts that rate to the pricing strategy default.
        settings:
          allOf:
            - $ref: '#/components/schemas/UpdatePrivateEndpointSettingsRequest'
            - description: >-
                Only the fields present change; an omitted field keeps its
                stored value and `null` clears a limit or reverts a flag to the
                provider default.
        upstream_model_id:
          description: Model or deployment identifier sent to the upstream provider.
          example: gpt-4o-prod
          minLength: 1
          type: string
      type: object
    PrivateEndpointResponse:
      properties:
        data:
          $ref: '#/components/schemas/PrivateEndpoint'
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
    PrivateEndpointDeclaredParameter:
      description: A chat request parameter the endpoint accepts.
      enum:
        - temperature
        - top_p
        - top_k
        - min_p
        - top_a
        - frequency_penalty
        - presence_penalty
        - repetition_penalty
        - max_tokens
        - max_completion_tokens
        - logit_bias
        - logprobs
        - top_logprobs
        - prediction
        - seed
        - response_format
        - structured_outputs
        - stop
        - tools
        - tool_choice
        - parallel_tool_calls
        - reasoning
        - reasoning_effort
        - web_search_options
        - verbosity
      example: seed
      type: string
    PrivateEndpointPricing:
      description: >-
        Negotiated per-token rates reported for requests routed to this
        endpoint.
      example:
        cache_read: '0.00000025'
        cache_write: '0.000003125'
        completion: '0.00001'
        prompt: '0.0000025'
      properties:
        cache_read:
          description: >-
            USD per cache-read prompt token, as a decimal string. When omitted,
            inherited from the public endpoint of the same model and provider:
            scaled by its cache-read to prompt ratio, or left at the pricing
            strategy default when it publishes no cache-read rate. Required when
            there is no such endpoint and the provider bills cache reads.
          example: '0.00000025'
          pattern: ^\d+(\.\d+)?$
          type: string
        cache_write:
          description: >-
            USD per cache-write prompt token, as a decimal string. When omitted,
            inherited from the public endpoint of the same model and provider:
            scaled by its cache-write to prompt ratio, or left at the pricing
            strategy default when it publishes no cache-write rate. Required
            when there is no such endpoint and the provider bills cache writes.
          example: '0.000003125'
          pattern: ^\d+(\.\d+)?$
          type: string
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
    UpdatePrivateEndpointSettingsRequest:
      description: >-
        Capabilities and limits to set over the ones copied from the public
        endpoint for this model and provider (or from the model). Omitted fields
        keep the copied values.
      example:
        context_length: 128000
        reasoning:
          supported: true
      properties:
        completions:
          properties:
            chat:
              description: Serves `/chat/completions`; `null` uses the provider default.
              type:
                - boolean
                - 'null'
            text:
              description: Serves `/completions`; `null` uses the provider default.
              type:
                - boolean
                - 'null'
          type: object
        context_length:
          description: >-
            Longest prompt plus completion, in tokens, or `null` to keep the
            model default.
          example: 128000
          minimum: 1
          type:
            - integer
            - 'null'
        excluded_parameters:
          description: >-
            Request parameters the upstream rejects even though the model
            supports them; requests using one do not route here. Cannot name a
            tested parameter.
          example:
            - logit_bias
          items:
            enum:
              - temperature
              - top_p
              - top_k
              - min_p
              - top_a
              - frequency_penalty
              - presence_penalty
              - repetition_penalty
              - max_tokens
              - max_completion_tokens
              - logit_bias
              - logprobs
              - top_logprobs
              - prediction
              - seed
              - response_format
              - structured_outputs
              - stop
              - tools
              - tool_choice
              - parallel_tool_calls
              - include_reasoning
              - reasoning
              - reasoning_effort
              - web_search_options
              - verbosity
            type: string
          type: array
        inputs:
          properties:
            audio:
              description: Accepts audio input. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
            base64_files:
              description: Accepts base64 file data. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
            base64_images:
              description: Accepts base64 image data. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
            file_urls:
              description: Accepts file URLs. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
            image_urls:
              description: Accepts image URLs. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
          type: object
        max_completion_tokens:
          description: >-
            Longest completion the upstream returns, in tokens, or `null` to
            keep the model default.
          example: 16384
          minimum: 1
          type:
            - integer
            - 'null'
        max_prompt_tokens:
          description: >-
            Longest prompt, in tokens, or `null` for no cap below the context
            length. Cannot exceed `context_length`, or the model context length
            while `context_length` is `null`.
          example: null
          minimum: 1
          type:
            - integer
            - 'null'
        quantization:
          $ref: '#/components/schemas/PrivateEndpointQuantization'
        reasoning:
          properties:
            return_mechanism:
              $ref: '#/components/schemas/PrivateEndpointReasoningReturnMechanism'
            supported:
              description: Whether requests with `reasoning` route to this endpoint.
              example: true
              type: boolean
          type: object
        tool_choice:
          properties:
            auto:
              description: 'Accepts `tool_choice: "auto"`.'
              type: boolean
            function:
              description: Accepts a named function in `tool_choice`.
              type: boolean
            none:
              description: 'Accepts `tool_choice: "none"`.'
              type: boolean
            required:
              description: 'Accepts `tool_choice: "required"`.'
              type: boolean
          type: object
      type: object
    PrivateEndpoint:
      example:
        base_url: https://contoso.openai.azure.com
        declared_parameters:
          - temperature
          - seed
        declared_region: us
        declared_zdr: true
        id: 5b1c4c4e-7d0a-4a8e-9f3a-2d6c1b0e8a11
        max_completion_tokens: 131072
        model_name: 'OpenAI: GPT-4o'
        model_permaslug: openai/gpt-4o-2024-08-06
        model_slug: openai/gpt-4o
        pricing:
          cache_read: '0.00000025'
          cache_write: '0.000003125'
          completion: '0.00001'
          prompt: '0.0000025'
        provider_name: Azure
        provider_slug: azure
        settings:
          completions:
            chat: true
            text: false
          context_length: 128000
          excluded_parameters:
            - logit_bias
          inputs:
            audio: false
            base64_files: null
            base64_images: true
            file_urls: null
            image_urls: true
          max_completion_tokens: 16384
          max_prompt_tokens: null
          quantization: bf16
          reasoning:
            return_mechanism: reasoning
            supported: true
          tool_choice:
            auto: true
            function: false
            none: true
            required: true
        status: active
        tested_parameters:
          - tools
          - tool_choice
          - response_format
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
        declared_parameters:
          description: >-
            Parameters you declared the upstream supports. Requests that use a
            parameter only route to this endpoint when it is tested or declared.
          example:
            - temperature
            - seed
          items:
            type: string
          type: array
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
        max_completion_tokens:
          description: >-
            Most completion tokens a request routed to this endpoint can
            produce, or `null` when the endpoint sets no cap beyond the model
            context length.
          example: 131072
          type:
            - integer
            - 'null'
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
        settings:
          $ref: '#/components/schemas/PrivateEndpointSettings'
        status:
          $ref: '#/components/schemas/PrivateEndpointStatus'
        tested_parameters:
          description: >-
            Parameters a validation run proved the upstream honors (`tools`,
            `tool_choice`, `response_format`, `structured_outputs`, `stop`).
            Read-only; cleared when the upstream configuration changes.
          example:
            - tools
            - tool_choice
            - response_format
          items:
            type: string
          type: array
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
        - tested_parameters
        - declared_parameters
        - settings
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
    PrivateEndpointQuantization:
      description: Weight precision the deployment runs at; `unknown` when not stated.
      enum:
        - int4
        - int8
        - fp4
        - mxfp4
        - nvfp4
        - fp6
        - fp8
        - mxfp8
        - fp16
        - bf16
        - fp32
        - unknown
      example: bf16
      type: string
    PrivateEndpointReasoningReturnMechanism:
      description: >-
        Where the upstream puts reasoning tokens in its response: `reasoning`
        and `reasoning-content` are response fields, `content-string` is inline
        in the message, `none` returns no reasoning. `null` uses the provider
        default.
      enum:
        - content-string
        - reasoning-content
        - reasoning
        - none
        - null
      example: reasoning
      type:
        - string
        - 'null'
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
    PrivateEndpointSettings:
      description: >-
        Capabilities and limits routing uses for this endpoint. A new endpoint
        copies them from the public endpoint for the same model and provider, or
        from the model, and the owner can change them. Rate limits are not part
        of this object: a private endpoint is billed to its own upstream key, so
        request limits stay with the provider.
      example:
        completions:
          chat: true
          text: false
        context_length: 128000
        excluded_parameters:
          - logit_bias
        inputs:
          audio: false
          base64_files: null
          base64_images: true
          file_urls: null
          image_urls: true
        max_completion_tokens: 16384
        max_prompt_tokens: null
        quantization: bf16
        reasoning:
          return_mechanism: reasoning
          supported: true
        tool_choice:
          auto: true
          function: false
          none: true
          required: true
      properties:
        completions:
          properties:
            chat:
              description: Serves `/chat/completions`; `null` uses the provider default.
              type:
                - boolean
                - 'null'
            text:
              description: Serves `/completions`; `null` uses the provider default.
              type:
                - boolean
                - 'null'
          required:
            - chat
            - text
          type: object
        context_length:
          description: >-
            Longest prompt plus completion, in tokens, or `null` to keep the
            model default.
          example: 128000
          minimum: 1
          type:
            - integer
            - 'null'
        excluded_parameters:
          description: >-
            Request parameters the upstream rejects even though the model
            supports them; requests using one do not route here. Cannot name a
            tested parameter.
          example:
            - logit_bias
          items:
            enum:
              - temperature
              - top_p
              - top_k
              - min_p
              - top_a
              - frequency_penalty
              - presence_penalty
              - repetition_penalty
              - max_tokens
              - max_completion_tokens
              - logit_bias
              - logprobs
              - top_logprobs
              - prediction
              - seed
              - response_format
              - structured_outputs
              - stop
              - tools
              - tool_choice
              - parallel_tool_calls
              - include_reasoning
              - reasoning
              - reasoning_effort
              - web_search_options
              - verbosity
            type: string
          type: array
        inputs:
          properties:
            audio:
              description: Accepts audio input. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
            base64_files:
              description: Accepts base64 file data. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
            base64_images:
              description: Accepts base64 image data. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
            file_urls:
              description: Accepts file URLs. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
            image_urls:
              description: Accepts image URLs. `null` keeps the provider default.
              type:
                - boolean
                - 'null'
          required:
            - image_urls
            - base64_images
            - file_urls
            - base64_files
            - audio
          type: object
        max_completion_tokens:
          description: >-
            Longest completion the upstream returns, in tokens, or `null` to
            keep the model default.
          example: 16384
          minimum: 1
          type:
            - integer
            - 'null'
        max_prompt_tokens:
          description: >-
            Longest prompt, in tokens, or `null` for no cap below the context
            length. Cannot exceed `context_length`, or the model context length
            while `context_length` is `null`.
          example: null
          minimum: 1
          type:
            - integer
            - 'null'
        quantization:
          $ref: '#/components/schemas/PrivateEndpointQuantization'
        reasoning:
          properties:
            return_mechanism:
              $ref: '#/components/schemas/PrivateEndpointReasoningReturnMechanism'
            supported:
              description: Whether requests with `reasoning` route to this endpoint.
              example: true
              type: boolean
          required:
            - supported
            - return_mechanism
          type: object
        tool_choice:
          properties:
            auto:
              description: 'Accepts `tool_choice: "auto"`.'
              type: boolean
            function:
              description: Accepts a named function in `tool_choice`.
              type: boolean
            none:
              description: 'Accepts `tool_choice: "none"`.'
              type: boolean
            required:
              description: 'Accepts `tool_choice: "required"`.'
              type: boolean
          required:
            - none
            - auto
            - required
            - function
          type: object
      required:
        - context_length
        - max_prompt_tokens
        - max_completion_tokens
        - quantization
        - reasoning
        - inputs
        - tool_choice
        - excluded_parameters
        - completions
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
