---
title: "Frequently Asked Questions"
source: https://docs.perplexity.ai/docs/resources/faq
path: docs/resources/faq
---

Answers to common questions about the Perplexity API, covering models, output and capabilities, search behavior, billing and limits, errors, data privacy, and support.

## Models

<AccordionGroup>
  <Accordion title="Does the API Currently Support Web Browsing?">
    Yes, the [Sonar Models](/docs/sonar/models) leverage information from Perplexity's search index and the public internet.
  </Accordion>

  <Accordion title="What Are the Context Windows for Each Model?">
    Context window size varies by model. For Sonar models, see the [Sonar models reference](/docs/sonar/models); for the third-party models available through the Agent API, see the [Agent API models page](/docs/agent-api/models) and the linked provider documentation.

    Note that the **context window**—the maximum number of tokens a model can process in a single request—is different from **search context size**, which controls how much web information is retrieved. See the [pricing glossary](/docs/getting-started/pricing) for the distinction.
  </Accordion>

  <Accordion title="Do You Support Fine-Tuning?">
    Currently, we do not support fine-tuning.
  </Accordion>

  <Accordion title="How Are Models Versioned and Deprecated?">
    When a model is retired, we announce it in the [changelog](/docs/resources/changelog) along with a recommended replacement. To avoid disruption, pin an explicit model ID in your requests rather than relying on a default, and watch the changelog for deprecation notices. The current list of available models is always on the [Sonar models](/docs/sonar/models) and [Agent API models](/docs/agent-api/models) pages.
  </Accordion>

  <Accordion title="Do You Expose CoTs If I Use Your Reasoning APIs or Deep Research API?">
    We expose the CoTs for Sonar Reasoning Pro. We don't currently expose the CoTs for Deep Research.
  </Accordion>
</AccordionGroup>

## Output & Capabilities

<AccordionGroup>
  <Accordion title="Can I Get Structured (JSON) Output?">
    Yes. Use the `response_format` parameter to constrain a response to a JSON schema. See [Structured Outputs](/docs/sonar/features#structured-outputs) for Sonar and [Structured Outputs](/docs/agent-api/output-control#structured-outputs) for the Agent API. For reasoning models, see the note below about `<think>` tokens preceding the JSON.
  </Accordion>

  <Accordion title="Why Isn't the `response_format` Parameter Working for Reasoning Models?">
    The `sonar-reasoning-pro` model is designed to output a `<think>` section containing reasoning tokens, immediately followed by a valid JSON object. As a result, the `response_format` parameter does not remove these reasoning tokens from the output.

    We recommend using a custom parser to extract the valid JSON portion. An example implementation can be found [here](https://github.com/ppl-ai/api-discussion/blob/main/utils/extract_json_reasoning_models.py).
  </Accordion>

  <Accordion title="Does the API Support Streaming Responses?">
    Yes. Pass `stream: true` to receive the response incrementally as it is generated, instead of waiting for the full result. See [Streaming Responses](/docs/sonar/features#streaming-responses) for Sonar and [Streaming Responses](/docs/agent-api/output-control#streaming-responses) for the Agent API. The [official SDKs](/docs/sdk/overview) expose streaming directly.
  </Accordion>

  <Accordion title="Does the API Support Tool or Function Calling?">
    Yes. The Agent API provides built-in tools, including [web search](/docs/agent-api/tools/web-search), [fetch URL content](/docs/agent-api/tools/fetch-url-content), [people search](/docs/agent-api/tools/people-search), [finance search](/docs/agent-api/tools/finance-search), and a [code sandbox](/docs/agent-api/tools/sandbox). The model decides when to call them while answering your request.
  </Accordion>

  <Accordion title="To What Extent Is the API OpenAI Compatible?">
    The Perplexity API is designed to be broadly compatible with OpenAI's chat completions endpoint. It adopts a similar structure—including fields such as `id`, `model`, and `usage`—and supports analogous parameters like `model`, `messages`, and `stream`.

    **Key Differences from the standard OpenAI response include:**

    * **Response Object Structure:**
      * OpenAI responses typically have an `object` value of `"chat.completion"` and a `created` timestamp, whereas our response uses `object: "response"` and a `created_at` field.
      * Instead of a `choices` array, our response content is provided under an `output` array that contains detailed message objects.

    * **Message Details:**
      * Each message in our output includes a `type` (usually `"message"`), a unique `id`, and a `status`.
      * The actual text is nested within a `content` array that contains objects with `type`, `text`, and an `annotations` array for additional context.

    * **Additional Fields:**
      * Our API response provides extra meta-information (such as `status`, `error`, `instructions`, and `max_output_tokens`) that are not present in standard OpenAI responses.
      * The `usage` field also differs, offering detailed breakdowns of input and output tokens (including fields like `input_tokens_details` and `output_tokens_details`).

    These differences are intended to provide enhanced functionality and additional context while maintaining broad compatibility with OpenAI's API design.
  </Accordion>

  <Accordion title="Are the Reasoning Tokens in Deep Research Same as CoTs in the Answer?">
    Reasoning tokens in Deep Research are a bit different than the CoTs in the answer—these tokens are used to reason through the research material before generating the final output via the CoTs.
  </Accordion>
</AccordionGroup>

## Search & Results

<AccordionGroup>
  <Accordion title="Why Are the Results from the API Different from the UI?">
    1. The API uses the same search system as the UI with differences in configuration—so their outputs may differ.
    2. The underlying AI model might differ between the API and the UI for a given query.
  </Accordion>

  <Accordion title="Is the Internet Data Access Provided by the API Identical to That of Perplexity's Web Interface?">
    Yes, the API offers exactly the same internet data access as Perplexity's web platform.
  </Accordion>

  <Accordion title="Does the API Use Content Filtering or SafeSearch?">
    Yes, for the API, content filtering in the form of SafeSearch is turned on by default. This helps filter out potentially offensive and inappropriate content, including pornography, from search results. SafeSearch is an automated filter that works across search results to provide a safer experience. You can learn more about SafeSearch on the [official Wikipedia page](https://en.wikipedia.org/wiki/SafeSearch).
  </Accordion>
</AccordionGroup>

## Account, Billing & Limits

<AccordionGroup>
  <Accordion title="How Does API Pricing Work?">
    Pricing is usage-based and varies by API. Sonar charges per token plus a per-request fee that depends on search context size; the Search API charges per request; the Agent API charges per token at direct provider rates with no markup, plus a per-invocation fee for tools; and Embeddings charge per token. See the full breakdown on the [Pricing page](/docs/getting-started/pricing).
  </Accordion>

  <Accordion title="How Do I Add Credits or Set Up Billing?">
    Purchase API credits in the [API Platform console](https://console.perplexity.ai) under the billing section. Enable **auto top-up** to add credits automatically when your balance runs low and avoid interrupted service. You can also buy credits through the [AWS Marketplace](/docs/resources/aws-marketplace) for consolidated billing, or [contact our sales team](https://perplexity.typeform.com/to/nXeehCGo) for enterprise procurement. Your [usage tier](/docs/admin/rate-limits-usage-tiers) advances automatically as your cumulative purchases grow.
  </Accordion>

  <Accordion title="How Can I Upgrade to the Next Usage Tier?">
    The only way for an account to be upgraded to the next usage tier is through all-time credit purchase.

    Here are the spending criteria associated with each tier:

    | Tier   | Credit Purchase (all time) |
    | ------ | -------------------------- |
    | Tier 0 | -                          |
    | Tier 1 | \$50                       |
    | Tier 2 | \$250                      |
    | Tier 3 | \$500                      |
    | Tier 4 | \$1000                     |
    | Tier 5 | \$5000                     |
  </Accordion>

  <Accordion title="What Are the Limitations to the Number of API Calls?">
    You can find our [rate limits here](/docs/admin/rate-limits-usage-tiers).
  </Accordion>

  <Accordion title="How Can I Track My Spend/Usage per API Key?">
    We offer a way to track your billing per API key. You can do this by navigating to the following location:

    **Settings > View Dashboard > Invoice history > Invoices**

    Then click on any invoice and each item from the total bill will have a code at the end of it (e.g., pro (743S)). Those 4 characters are the last 4 of your API key.
  </Accordion>
</AccordionGroup>

## Errors & Troubleshooting

<AccordionGroup>
  <Accordion title="How Should I Respond to 401: Authorization Errors?">
    401 error codes indicate that the provided API key is invalid, deleted, or belongs to an account which ran out of credits. You likely need to purchase more credits in the [API Platform console](https://console.perplexity.ai). You can avoid this issue by configuring auto-top-up.
  </Accordion>

  <Accordion title="How Should I Handle 429: Too Many Requests Errors?">
    A 429 means you've exceeded your rate limit. Rate limits scale with your [usage tier](/docs/admin/rate-limits-usage-tiers) and use a leaky-bucket algorithm that allows short bursts up to your limit. Retry with exponential backoff and jitter, use burst capacity for batch jobs, and upgrade your tier—or [request a custom limit](https://perplexity.typeform.com/to/yctmfyVT)—for sustained higher throughput. See [Error Handling](/docs/sdk/error-handling) for retry examples in both SDKs.
  </Accordion>

  <Accordion title="What Should I Do About 5xx or Connection and Timeout Errors?">
    5xx responses indicate a transient server-side issue, and connection or timeout errors usually point to a network problem. Retry these with exponential backoff, set sensible client timeouts, and log the `X-Request-ID` response header to include when you contact support. The [Error Handling guide](/docs/sdk/error-handling) covers the SDK exception types and recovery patterns.
  </Accordion>

  <Accordion title="Where Can I Check API Status and Incidents?">
    Current API availability and incident history are on the [System Status page](/docs/resources/status). If you're seeing errors that aren't explained there, reach out through the support channels below.
  </Accordion>
</AccordionGroup>

## Data, Privacy & Security

<AccordionGroup>
  <Accordion title="Will User Data Submitted Through the API Be Used for Model Training or Other Purposes?">
    We collect the following types of information:

    **API Usage Data:** We collect billable usage metadata such as the number of requests and tokens. You can view your own usage in the [API Platform console](https://console.perplexity.ai).

    **User Account Information:** When you create an account with us, we collect your name, email address, and other relevant contact information.

    We do not retain any query data sent through the API and do not train on any of your data.
  </Accordion>

  <Accordion title="Where Are Perplexity's Language Models Hosted?">
    Our compute is hosted via Amazon Web Services in North America. By default, the API has zero day retention of user prompt data, which is never used for AI training.
  </Accordion>

  <Accordion title="What Security and Compliance Certifications Does the API Have?">
    Perplexity maintains a **SOC 2 Type II** report, a **2025 HIPAA gap assessment**, and a **CAIQlite** cloud security assessment. These reports, along with data-processing and other compliance documentation (for example, for DPA or GDPR requests), are available through the [Perplexity Trust Center](https://trust.perplexity.ai/). See [Privacy & Security](/docs/resources/privacy-security) for an overview, or [contact us](mailto:api@perplexity.ai) for documents not published there.
  </Accordion>
</AccordionGroup>

## Support & Reliability

<AccordionGroup>
  <Accordion title="How Do I File a Bug Report and What Happens Afterward?">
    To file a bug report, please head to our [Developer Community](https://community.perplexity.ai/) and create a new post in the "Bug Reports" category.

    We truly appreciate your patience, and we'll get back to you as soon as possible. Due to the current volume of reports, it may take a little time for us to respond—but rest assured, we're on it.
  </Accordion>

  <Accordion title="How Do I Request a New Feature?">
    A Feature Request is a suggestion to improve or add new functionality to the Perplexity Sonar API, such as:

    * Requesting support for a new model or capability (e.g., image processing, fine-tuning options)
    * Asking for new API parameters (e.g., additional filters, search options)
    * Suggesting performance improvements (e.g., faster response times, better citation handling)
    * Enhancing existing API features (e.g., improving streaming reliability, adding new output formats)

    If your request aligns with these, please submit a feature request here: [Github Feature requests](https://github.com/ppl-ai/api-discussion/issues)
  </Accordion>

  <Accordion title="What's the Best Way to Stay Up to Date with API Updates?">
    We email users about new developments and also post in the [changelog](/docs/resources/changelog).
  </Accordion>

  <Accordion title="Does Perplexity Provide Service Quality Assurances Such as Service Uptime, Frequency of Failures, and Target Recovery Time in the Event of a Failure?">
    We do not guarantee this at the moment.
  </Accordion>

  <Accordion title="I Have Another Question or an Issue">
    Please reach out to [api@perplexity.ai](mailto:api@perplexity.ai) or [support@perplexity.ai](mailto:support@perplexity.ai) for other API inquiries. You can also post on our [discussion forum](https://github.com/ppl-ai/api-discussion/discussions) and we will get back to you.
  </Accordion>
</AccordionGroup>
