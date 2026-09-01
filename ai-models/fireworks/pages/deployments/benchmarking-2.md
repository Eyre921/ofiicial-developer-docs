---
title: "Performance benchmarking"
source: https://docs.fireworks.ai/deployments/benchmarking
path: deployments/benchmarking
---

Measure and optimize your deployment's performance with load testing

Understanding your deployment's performance under various load conditions is essential for production readiness. Fireworks provides tools and best practices for benchmarking throughput, latency, and identifying bottlenecks.

## Fireworks Benchmark Tool

Use our open-source benchmarking tool to measure and optimize your deployment's performance:

**[Fireworks Benchmark Tool](https://github.com/fw-ai/benchmark)**

This tool allows you to:

* Test throughput and latency under various load conditions
* Simulate production traffic patterns
* Identify performance bottlenecks
* Compare different deployment configurations

### Installation

```bash theme={null}
git clone https://github.com/fw-ai/benchmark.git
cd benchmark
pip install -r requirements.txt
```

### Basic usage

Run a basic benchmark test:

```bash theme={null}
python benchmark.py \
  --model "accounts/fireworks/models/llama-v3p1-8b-instruct" \
  --deployment "your-deployment-id" \
  --num-requests 1000 \
  --concurrency 10
```

### Key metrics to monitor

When benchmarking your deployment, focus on these key metrics:

* **Throughput**: Requests per second (RPS) your deployment can handle
* **Latency**: Time to first token (TTFT) and end-to-end response time
* **Token generation rate**: Tokens per second during generation
* **Error rate**: Failed requests under load

## Custom benchmarking

You can also develop custom performance testing scripts or integrate with monitoring tools to track metrics over time. Consider:

* Using production-like request patterns and payloads
* Testing with various concurrency levels
* Monitoring resource utilization (GPU, memory, network)
* Testing autoscaling behavior under load

## Best practices

1. **Warm up your deployment**: Run a few requests before benchmarking to ensure models are loaded
2. **Test realistic scenarios**: Use request patterns and payloads similar to your production workload
3. **Gradually increase load**: Start with low concurrency and gradually increase to find your deployment's limits
4. **Monitor for errors**: Track error rates and response codes to identify issues under load
5. **Compare configurations**: Test different deployment shapes, quantization levels, and hardware to optimize cost and performance

## Next steps

<CardGroup>
  <Card title="Autoscaling" href="/deployments/autoscaling" icon="arrows-up-down">
    Configure autoscaling to handle variable load
  </Card>

  <Card title="Client-side optimization" href="/deployments/client-side-performance-optimization" icon="bolt">
    Optimize your client code for maximum throughput
  </Card>
</CardGroup>
