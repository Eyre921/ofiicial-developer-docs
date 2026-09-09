---
title: "Client-side performance optimization"
source: https://docs.fireworks.ai/deployments/client-side-performance-optimization
path: deployments/client-side-performance-optimization
---

Optimize your client code for maximum performance with dedicated deployments

When using a dedicated deployment, it is important to optimize the client-side HTTP connection pooling for maximum performance. We recommend using our [Python SDK](/tools-sdks/python-sdk) as it has good defaults for connection pooling and utilizes [httpx](https://www.python-httpx.org/) for optimal performance with Python's `asyncio` library. It also includes retry logic for handling `429` errors that Fireworks returns when the server is overloaded.

## General optimization recommendations

Based on our benchmarks, we recommend the following:

1. Use a client library optimized for high concurrency, such as [httpx](https://www.python-httpx.org/) in Python or [http.Agent](https://nodejs.org/api/http.html#class-httpagent) in Node.js.
2. Use the `AsyncFireworks` client for high-concurrency workloads.
3. Increase concurrency until performance stops improving or you observe too many `429` errors.

## Code example: Optimal concurrent requests (Python)

Install the [Fireworks Python SDK](/tools-sdks/python-sdk):

<Note>
  The SDK is currently in alpha. Use the `--pre` flag when installing to get the latest version.
</Note>

<CodeGroup>
  ```bash pip theme={null}
  pip install --pre fireworks-ai
  ```

  ```bash poetry theme={null}
  poetry add --pre fireworks-ai
  ```

  ```bash uv theme={null}
  uv add --pre fireworks-ai
  ```
</CodeGroup>

Here's how to implement optimal concurrent requests using `asyncio` and the `AsyncFireworks` client:

```python main.py theme={null}
import asyncio
import time
import statistics
from fireworks import AsyncFireworks


async def make_concurrent_requests(
    messages: list[str],
    model: str,
    max_workers: int = 1000,
):
    """Make concurrent requests with optimized connection pooling"""

    client = AsyncFireworks(
        max_retries=5,
    )

    # Semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(max_workers)
    latencies = []

    async def single_request(message: str):
        """Make a single request with semaphore control"""
        async with semaphore:
            start_time = time.perf_counter()
            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": message}],
                max_tokens=100,
            )
            latency = time.perf_counter() - start_time
            latencies.append(latency)
            return response.choices[0].message.content

    # Create all request tasks
    tasks = [single_request(message) for message in messages]

    # Execute all requests concurrently
    results = await asyncio.gather(*tasks)
    return results, latencies


# Usage example
async def main():
    messages = ["Hello!"] * 1000  # 1000 requests

    model = "accounts/fireworks/models/qwen3-0p6b"

    start_time = time.perf_counter()
    results, latencies = await make_concurrent_requests(
        messages=messages,
        model=model,
    )
    total_time = time.perf_counter() - start_time

    # Calculate performance metrics
    num_requests = len(results)
    requests_per_second = num_requests / total_time

    # Latency statistics (in milliseconds)
    latencies_ms = [lat * 1000 for lat in latencies]
    avg_latency = statistics.mean(latencies_ms)
    min_latency = min(latencies_ms)
    max_latency = max(latencies_ms)
    p50_latency = statistics.median(latencies_ms)
    p95_latency = statistics.quantiles(latencies_ms, n=20)[18]  # 95th percentile
    p99_latency = statistics.quantiles(latencies_ms, n=100)[98]  # 99th percentile

    print("\n" + "=" * 50)
    print("Performance Results")
    print("=" * 50)
    print(f"Total requests:      {num_requests}")
    print(f"Total time:          {total_time:.2f} seconds")
    print(f"Throughput:          {requests_per_second:.2f} requests/second")
    print("\nLatency Statistics (ms):")
    print(f"  Min:               {min_latency:.2f}")
    print(f"  Max:               {max_latency:.2f}")
    print(f"  Avg:               {avg_latency:.2f}")
    print(f"  P50 (median):      {p50_latency:.2f}")
    print(f"  P95:               {p95_latency:.2f}")
    print(f"  P99:               {p99_latency:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
```

This implementation:

* Uses `AsyncFireworks` for non-blocking async requests with optimized connection pooling
* Uses `asyncio.Semaphore` to control concurrency to avoid overwhelming the server
