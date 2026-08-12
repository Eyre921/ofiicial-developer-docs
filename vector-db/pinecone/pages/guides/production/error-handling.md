---
title: "Error handling"
source: https://docs.pinecone.io/guides/production/error-handling
path: guides/production/error-handling
---

Handle Pinecone API errors with retry logic, exponential backoff, and best practices for 4xx client errors, 5xx server errors, and rate limit responses.

## Understand error types

Pinecone uses [conventional HTTP response codes](/reference/api/errors) to indicate the success or failure of API requests:

* **2xx codes** indicate success
* **4xx codes** indicate client errors (issues with your request)
* **5xx codes** indicate server errors (issues with Pinecone's servers)

### Client errors (4xx)

Client errors indicate problems with your request. These errors typically require changes to your code or configuration:

* **400 - Invalid Argument**: Your request contains invalid parameters. Check your request format and parameters.
* **401 - Unauthenticated**: Your API key is missing or invalid. Verify your [API key](/guides/projects/manage-api-keys).
* **402 - Payment Required**: Your account has a payment issue or may be deactivated for non-payment. Check your billing status in the [console](https://app.pinecone.io) and see [Account deactivation for non-payment](/guides/organizations/manage-billing/non-payment-account-deactivation).
* **403 - Forbidden**: You've exceeded a [quota](/reference/api/database-limits#object-limits) or hit [deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).
* **404 - Not Found**: The requested resource doesn't exist. Verify the resource name and that it hasn't been deleted.
* **409 - Already Exists**: You're trying to create a resource that already exists.
* **429 - Too Many Requests**: You're being [rate-limited](/reference/api/database-limits#rate-limits). Implement [backoff and retry logic](#implement-retry-logic).

### Server errors (5xx)

Server errors indicate temporary issues with Pinecone's infrastructure:

* **500 - Unknown**: An internal server error occurred.
* **502 - Bad Gateway**: The API gateway received an invalid response from a backend service.
* **503 - Unavailable**: The service is currently unavailable.
* **504 - Gateway Timeout**: The API gateway did not receive a timely response from the backend server. This can occur due to slow requests or backend processing delays.

**Best practice for 5xx errors**: [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). These errors are typically transient.

## Capture errors

Each SDK provides error handling mechanisms specific to the language:

### Python SDK

The Python SDK raises exceptions that you can catch and handle:

```python theme={null}
from pinecone import Pinecone
from pinecone.exceptions import PineconeException

pc = Pinecone(api_key="YOUR_API_KEY")
index = pc.Index("your-index")

try:
    index.upsert(
        vectors=[
            {"id": "vec1", "values": [0.1, 0.2, 0.3]}
        ]
    )
except PineconeException as e:
    # Handle Pinecone-specific errors
    print(f"Pinecone error: {e}")
except Exception as e:
    # Handle other errors
    print(f"Unexpected error: {e}")
```

See the [Python SDK documentation](https://sdk.pinecone.io/python/) for more details on exception handling.

### Node.js SDK

The Node.js SDK uses standard JavaScript error handling:

```javascript theme={null}
const { Pinecone } = require('@pinecone-database/pinecone');

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

try {
  const index = pc.index('your-index');
  await index.upsert([
    { id: 'vec1', values: [0.1, 0.2, 0.3] }
  ]);
} catch (error) {
  console.error('Error upserting data:', error);
  // Handle the error appropriately
}
```

See the [Node.js SDK documentation](https://sdk.pinecone.io/typescript/) for more information.

### Other SDKs

For SDK-specific error handling patterns, see the documentation for your language:

* [Go SDK](/reference/sdks/go/overview)
* [Java SDK](/reference/sdks/java/overview)

## Implement retry logic

For transient errors (5xx codes and 429 rate limiting), implement retry logic. Start with basic retries for simple use cases, or use exponential backoff for production systems.

### Basic retry logic

For simple use cases, start with a basic retry loop with fixed delays:

```python theme={null}
import time
from pinecone.exceptions import PineconeException

def simple_retry(func, max_retries=3, delay=2):
    """
    Retry a function with a fixed delay between attempts.

    Args:
        func: Function to retry
        max_retries: Maximum number of retry attempts
        delay: Delay in seconds between retries
    """
    for attempt in range(max_retries):
        try:
            return func()
        except PineconeException as e:
            if attempt == max_retries - 1:
                raise  # Last attempt, re-raise the exception

            print(f"Attempt {attempt + 1} failed, retrying in {delay}s...")
            time.sleep(delay)

# Usage
try:
    simple_retry(lambda: index.upsert(vectors))
except Exception as e:
    print(f"Failed after {max_retries} attempts: {e}")
```

This basic approach works well for occasional transient errors, but for production systems with higher traffic, use exponential backoff instead.

### Exponential backoff

Exponential backoff progressively increases the wait time between retries to avoid overwhelming the service:

```python theme={null}
import time
import random

def exponential_backoff_retry(func, max_retries=5, base_delay=1, max_delay=60):
    """
    Retry a function with exponential backoff.

    Args:
        func: Function to retry
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay between retries
    """
    for attempt in range(max_retries):
        try:
            return func()
        except PineconeException as e:
            if attempt == max_retries - 1:
                raise  # Last attempt, re-raise the exception

            # Get status code if available
            status_code = getattr(e, 'status', None)

            # Only retry on 5xx errors or 429 (rate limiting)
            if status_code and (status_code >= 500 or status_code == 429):
                # Calculate delay with exponential backoff and jitter
                delay = min(base_delay * (2 ** attempt), max_delay)
                jitter = random.uniform(0, delay * 0.1)  # Add 10% jitter
                wait_time = delay + jitter

                print(f"Retry attempt {attempt + 1}/{max_retries} after {wait_time:.2f}s")
                time.sleep(wait_time)
            else:
                # Don't retry client errors (4xx except 429)
                raise

# Usage
try:
    exponential_backoff_retry(lambda: index.upsert(vectors))
except Exception as e:
    print(f"Failed after retries: {e}")
```

### Go SDK

The Go SDK has built-in retries with exponential backoff. Set a `RetryPolicy` on the client and it applies to both the REST (control/data/inference) and gRPC (data plane) clients. Retries cover 429 and transient 5xx / gRPC `UNAVAILABLE` errors; other 4xx errors are never retried.

```go theme={null}
package main

import (
	"os"

	"github.com/pinecone-io/go-pinecone/v6/pinecone"
)

func main() {
	pc, err := pinecone.NewClient(pinecone.NewClientParams{
		ApiKey:      os.Getenv("PINECONE_API_KEY"),
		RetryPolicy: pinecone.DefaultRetryPolicy(), // 3 retries, 500ms base, 30s cap, 2x backoff
	})
	if err != nil {
		panic(err)
	}
	_ = pc
}
```

To customize the behavior, construct a `RetryPolicy` with your own `MaxRetries`, `BaseDelay`, `MaxDelay`, and `BackoffMultiplier`. See the [Go SDK documentation](/reference/sdks/go/overview) for details.

### Key retry principles

1. **Add jitter**: Random variation in retry timing helps avoid thundering herd problems.
2. **Set max retries**: Prevent infinite retry loops.
3. **Cap delay time**: Don't wait indefinitely between retries.
4. **Don't retry client errors**: 4xx errors (except 429) won't resolve with retries.
5. **Log retry attempts**: Track retry behavior for monitoring and debugging.

## Handle rate limits (429)

When you receive a 429 error, you're being rate-limited. See [Rate limits](/reference/api/database-limits#rate-limits) for current limits.

Rate limits help protect your applications and maintain the health of the serverless infrastructure. **Most limits can be adjusted upon request**—if you need higher limits to scale, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

**Best practices**:

* Implement exponential backoff as described above.
* Proactively [monitor request metrics](/guides/production/monitoring) and reduce the request rate if you're approaching limits.
* Use [batching](/guides/index-data/upsert-data#upsert-in-batches) to reduce the number of requests.
* For high-throughput needs, see [Increase throughput](/guides/optimize/increase-throughput).

## Getting support

If you've implemented error handling and retry logic but continue to experience issues:

1. Review [How to work with Support](/troubleshooting/how-to-work-with-support) for best practices.
2. Gather the following information:
   * Index name and project name
   * Error messages and stack traces
   * Timestamp of errors
   * Request/response examples (without sensitive data)
   * Whether the issue is reproducible
3. [Contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

Ensure your [plan tier](https://www.pinecone.io/pricing/) provides the support SLA you need for production workloads.

## See also

* [API error codes](/reference/api/errors)
* [Database limits](/reference/api/database-limits)
* [Assistant limits](/reference/api/assistant/assistant-limits)
* [Monitoring](/guides/production/monitoring)
* [Production checklist](/guides/production/production-checklist)
