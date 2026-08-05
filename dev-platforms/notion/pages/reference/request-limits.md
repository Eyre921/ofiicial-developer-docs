---
title: "Request limits"
source: https://developers.notion.com/reference/request-limits
path: reference/request-limits
---

To ensure a consistent developer experience for all API users, the Notion API is rate limited and basic size limits apply to request parameters.

## Rate limits

The Notion API enforces two rate limits:

* **Per connection** — an average of three requests per second, with some bursts beyond the average allowed.
* **Per workspace** — shared across all of the workspace's connections and scaled to the workspace's plan.

Requests that exceed either limit return a `"rate_limited"` error code and an HTTP 429 response, with `additional_data.rate_limit_reason` indicating which limit was exceeded (for example, `public_api_request_rate_limit` or `public_api_space_request_rate_limit`).

Connections should handle HTTP 429 and 529 responses and respect the `Retry-After` response header. The header value is an integer number of seconds. A 529 response carries the `"service_overload"` code and means Notion is temporarily overloaded; retry it the same way as a 429.

### Retry rate-limited requests

Put outgoing requests through a queue so a burst from one job does not consume the connection's full request budget. When Notion returns 429 or 529:

1. Read `Retry-After` and pause new requests for at least that many seconds.
2. Retry the failed request after the pause.
3. If another 429 or 529 arrives, increase the delay with exponential backoff and jitter.
4. Set a retry limit. Log or surface the final error when the limit is reached.

Do not retry every error. Retry 429 and 529 responses. Retry 500, 502, 503, and 504 responses only when the request is idempotent, such as GET or DELETE, unless your application has its own idempotency protection. Fix the request before retrying most 400 responses. Treat 401 and 403 responses as authentication or authorization failures.

The JavaScript SDK retries 429 responses for every method. It also retries 500 and 503 responses for GET and DELETE requests. It respects `Retry-After`, uses exponential backoff with jitter, and limits retries. If you call the REST API directly, use the same safeguards and add explicit handling for 529 responses. These examples show the same policy in several common HTTP clients:

<CodeGroup>
  ```js JavaScript theme={null}
  async function notionRequest(url, options = {}, attempt = 0) {
    const response = await fetch(url, options)
    const method = (options.method ?? "GET").toUpperCase()
    const isIdempotent = method === "GET" || method === "DELETE"
    const retryable =
      response.status === 429 ||
      response.status === 529 ||
      (isIdempotent && [500, 502, 503, 504].includes(response.status))

    if (!retryable || attempt >= 5) {
      return response
    }

    const retryAfter = response.headers.get("retry-after")
    const retryAfterSeconds = Number(retryAfter)
    const exponentialDelaySeconds = Math.min(2 ** attempt, 30)
    const baseDelaySeconds = retryAfter !== null && Number.isFinite(retryAfterSeconds)
      ? retryAfterSeconds
      : exponentialDelaySeconds
    const jitterMs = Math.random() * 250

    await new Promise(resolve =>
      setTimeout(resolve, baseDelaySeconds * 1000 + jitterMs),
    )

    return notionRequest(url, options, attempt + 1)
  }
  ```

  ```python Python theme={null}
  import random
  import time

  import requests


  def notion_request(method, url, *, max_attempts=6, **kwargs):
      method = method.upper()
      is_idempotent = method in {"GET", "DELETE"}

      for attempt in range(max_attempts):
          response = requests.request(method, url, **kwargs)
          retryable = (
              response.status_code in {429, 529}
              or (
                  is_idempotent
                  and response.status_code in {500, 502, 503, 504}
              )
          )

          if not retryable or attempt == max_attempts - 1:
              return response

          retry_after = response.headers.get("Retry-After")
          delay = float(retry_after) if retry_after else min(2 ** attempt, 30)
          time.sleep(delay + random.uniform(0, 0.25))
  ```

  ```go Go theme={null}
  func notionRequest(client *http.Client, request *http.Request) (*http.Response, error) {
  	const maxAttempts = 6
  	isIdempotent := request.Method == http.MethodGet || request.Method == http.MethodDelete

  	for attempt := 0; attempt < maxAttempts; attempt++ {
  		attemptRequest := request.Clone(request.Context())
  		if attempt > 0 && request.Body != nil {
  			if request.GetBody == nil {
  				return nil, errors.New("request body cannot be replayed")
  			}
  			body, err := request.GetBody()
  			if err != nil {
  				return nil, err
  			}
  			attemptRequest.Body = body
  		}

  		response, err := client.Do(attemptRequest)
  		if err != nil {
  			return nil, err
  		}

  		retryableServerError := response.StatusCode == 500 ||
  			response.StatusCode == 502 || response.StatusCode == 503 ||
  			response.StatusCode == 504
  		retryable := response.StatusCode == 429 || response.StatusCode == 529 ||
  			(isIdempotent && retryableServerError)
  		if !retryable || attempt == maxAttempts-1 {
  			return response, nil
  		}

  		response.Body.Close()
  		delay := time.Duration(1<<attempt) * time.Second
  		if delay > 30*time.Second {
  			delay = 30 * time.Second
  		}
  		if seconds, err := strconv.Atoi(response.Header.Get("Retry-After")); err == nil && seconds >= 0 {
  			delay = time.Duration(seconds) * time.Second
  		}
  		time.Sleep(delay + time.Duration(rand.Intn(250))*time.Millisecond)
  	}

  	panic("unreachable")
  }
  ```

  ```java Java theme={null}
  HttpResponse<String> notionRequest(
      HttpClient client,
      HttpRequest request
  ) throws IOException, InterruptedException {
      int maxAttempts = 6;
      boolean isIdempotent = Set.of("GET", "DELETE").contains(request.method());

      for (int attempt = 0; attempt < maxAttempts; attempt++) {
          HttpResponse<String> response = client.send(
              request,
              HttpResponse.BodyHandlers.ofString()
          );
          int status = response.statusCode();
          boolean retryable = status == 429 || status == 529 ||
              (isIdempotent && Set.of(500, 502, 503, 504).contains(status));

          if (!retryable || attempt == maxAttempts - 1) {
              return response;
          }

          long retryAfter = response.headers().firstValue("Retry-After")
              .map(Long::parseLong)
              .orElse(Math.min(1L << attempt, 30));
          long jitterMillis = ThreadLocalRandom.current().nextLong(250);
          Thread.sleep(retryAfter * 1000 + jitterMillis);
      }

      throw new IllegalStateException("unreachable");
  }
  ```
</CodeGroup>

The same rules apply in other languages: centralize retries in the HTTP client, respect `Retry-After`, add jitter, and cap the fallback delay and attempt count. Avoid independent retry loops in each worker; they can create a second traffic spike when the delay expires.

<Warning>
  **Rate limits may change**

  In the future, Notion plans to adjust rate limits to balance for demand and reliability.
</Warning>

## Size limits

Notion limits the size of certain parameters, and the depth of children in requests. A requests that exceeds any of these limits will return `"validation_error"` error code (HTTP response status 400) and contain more specific details in the `"message"` property.

Connections should avoid sending requests beyond these limits proactively. It may be helpful to use test data in your own test suite which intentionally contains large parameters to verify that the errors are handled appropriately. For example, if the connection reads a URL from an external system to put into a Notion page property, the connection should have a plan to deal with URLs that are beyond the length limit of 2000 characters. The connection might choose to log the error, or send an alert to the user who set up the connection via an email, or some other action.

Note that in addition to the property limits below, payloads have a maximum size of 1000 block elements and 500KB overall.

### Limits for property values

| Property value type                                                                                   | Inner property        | Size limit        |
| :---------------------------------------------------------------------------------------------------- | :-------------------- | :---------------- |
| [Rich text object](/reference/rich-text)                                                              | `text.content`        | 2000 characters   |
| [Rich text object](/reference/rich-text)                                                              | `text.link.url`       | 2000 characters   |
| [Rich text object](/reference/rich-text)                                                              | `equation.expression` | 1000 characters   |
| Any array of all [block](/reference/block) types, including [rich text objects](/reference/rich-text) |                       | 100 elements      |
| Any URL                                                                                               |                       | 2000 characters   |
| Any email                                                                                             |                       | 200 characters    |
| Any phone number                                                                                      |                       | 200 characters    |
| Any multi-select                                                                                      |                       | 100 options       |
| Any relation                                                                                          |                       | 100 related pages |
| Any people                                                                                            |                       | 100 users         |

<Note>
  **Request size limits**

  These cap the size of a single request, not how much a property can hold. A relation property can contain far more than 100 related pages — the limit only governs how many you add or set in one request. Responses have separate limits; use [Retrieve a page property item](/reference/retrieve-a-page-property) to paginate through large values.
</Note>
