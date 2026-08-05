---
title: "Architecture"
source: https://docs.together.ai/docs/together-deployments
path: docs/together-deployments
---

Architecture, deployment lifecycle, and core concepts for dedicated container inference.

Dedicated Containers provide a flexible way to run your own Dockerized workloads on managed GPU infrastructure. You supply the container image, and Together manages everything else, handling compute provisioning, autoscaling, networking, and observability for you.

The platform is designed for teams that need full control over their runtime environment while avoiding the operational complexity of managing GPU clusters directly.

<Tip>
  **Looking for full example templates?** <br />
  See the end-to-end deployment examples: [Image Generation with Flux2](/docs/dedicated_containers_image) and [Video Generation with Wan 2.1](/docs/dedicated_containers_video).
</Tip>

With Together Deployments, you can:

* Deploy custom inference, data processing jobs, or long-running workers
* Scale workloads automatically based on demand, including down to zero
* Run queue-based or asynchronous jobs with built-in request handling
* Securely manage secrets, environment variables, and configuration
* Scale from a single replica to thousands of GPUs as traffic grows

## Platform components

<Frame>
  <img alt="Dedicated Containers Architecture" />
</Frame>

Dedicated Containers include three core components:

### Jig – deployment CLI

A lightweight CLI for building, pushing, and deploying containers. Jig handles:

* Dockerfile generation from `pyproject.toml`
* Image building and pushing to Together's registry
* Deployment creation and updates
* Secrets and volume management
* Log streaming and status monitoring

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig deploy
  ```
</CodeGroup>

[See the Jig CLI docs →](/docs/deployments-jig)

### Sprocket – worker SDK

A Python SDK for building inference workers that integrate with Together's job queue:

* Implement `setup()` and `predict(args) -> dict`
* Automatic file download and upload handling
* Progress reporting for long-running jobs
* Health checks and metrics endpoints
* Graceful shutdown support

<CodeGroup>
  ```python Python theme={null}
  import sprocket


  class MyModel(sprocket.Sprocket):
      def setup(self):
          self.model = load_model()

      def predict(self, args: dict) -> dict:
          result = self.model(args["input"])
          return {"output": result}


  if __name__ == "__main__":
      sprocket.run(MyModel(), "my-org/my-model")
  ```
</CodeGroup>

[See the Sprocket SDK docs →](/docs/deployments-sprocket)

### Container registry

A Together-hosted Docker registry at `registry.together.ai` for storing your container images. Images are private to your organization and referenced by digest for reproducible deployments.

## Available hardware

Choose from high-performance NVIDIA GPU configurations:

| GPU Type            | `gpu_type` value | Memory | Use Case                                        |
| ------------------- | ---------------- | ------ | ----------------------------------------------- |
| **NVIDIA H100 SXM** | `h100-80gb`      | 80GB   | Large models, high throughput                   |
| **NVIDIA B200**     | `b200-192gb`     | 192GB  | Next-generation hardware for the largest models |
| **CPU-only**        | `none`           | N/A    | Lightweight preprocessing or embedding models   |

For models requiring multiple GPUs, configure `gpu_count` in your deployment and use `torchrun` for distributed inference.

## When to use dedicated containers

Dedicated Containers are appropriate when:

* **You have a custom model or inference stack** – Custom architectures, fine-tuned models, or proprietary inference code
* **You've modified open-source engines** – Customized vLLM, SGLang, or other serving frameworks
* **You're running media generation** – Audio, image, or video models with variable execution times
* **You need async or batch processing** – Long-running jobs that don't fit the request-response pattern
* **You want full control** – Specific library versions, custom preprocessing, or non-standard runtimes

## How it works

1. **Package your model as a Docker container**

   Create a container with your runtime, dependencies, and inference code. Use Sprocket for queue integration or bring your own HTTP server.

2. **Configure your deployment**

   Define GPU type, replica limits, autoscaling behavior, and environment variables in `pyproject.toml`.

3. **Deploy to Together**

   Run `tg beta jig deploy` to build, push, and create your deployment. Together provisions GPUs and starts your containers.

4. **Submit jobs**

   Use the Queue API to submit jobs. Workers pull jobs from the queue, execute inference, and report results.

5. **Monitor and scale**

   View logs, metrics, and job status. The autoscaler adjusts replica count based on queue depth.

<Tip>
  **Ready to deploy?** Follow the [Quickstart guide](/docs/containers-quickstart) for a step-by-step walkthrough, or explore the [Jig CLI](/docs/deployments-jig), [Sprocket SDK](/docs/deployments-sprocket), and [Queue API](/docs/deployments-queue) docs.
</Tip>

# Monitoring and observability

### Metrics

Each Sprocket worker exposes a `/metrics` endpoint with Prometheus-compatible metrics:

```
requests_inflight 1.0
```

The autoscaler uses this metric combined with queue depth to make scaling decisions.

### Logging

Access deployment logs via:

<CodeGroup>
  ```shell CLI theme={null}
  tg beta jig logs
  tg beta jig logs --follow
  ```

  ```shell cURL theme={null}
  curl https://api.together.ai/v1/deployments/my-model/logs \
    -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

**Structured Logging in Your Application**

Use Python's logging module for structured output:

<CodeGroup>
  ```python Python theme={null}
  import logging
  import sprocket

  logging.basicConfig(
      level=logging.INFO,
      format="{levelname} {module}:{lineno}: {message}",
      style="{",
  )
  logger = logging.getLogger(__name__)


  class MyModel(sprocket.Sprocket):
      def setup(self):
          logger.info("Loading model...")
          self.model = load_model()
          logger.info("Model loaded successfully")

      def predict(self, args):
          logger.info(
              f"Processing job with prompt: {args.get('prompt', '')[:50]}..."
          )
          # ...
  ```
</CodeGroup>

### Health checks

The platform monitors your deployment's `/health` endpoint. Ensure it:

* Returns 200 when ready to accept jobs
* Returns 503 during startup or when unhealthy
* Responds within a reasonable timeout

# Autoscaling

### Configuration

Enable autoscaling in your `pyproject.toml`:

<CodeGroup>
  ```toml pyproject.toml theme={null}
  [tool.jig.deploy]
  min_replicas = 1
  max_replicas = 20

  [tool.jig.deploy.autoscaling]
  metric = "QueueBacklogPerWorker"
  target = 1.05
  ```
</CodeGroup>

### Metrics

**QueueBacklogPerWorker**

Scales based on queue depth relative to worker count.

* `target = 1.0`: Exact match (queue\_depth = workers)
* `target = 1.05`: 5% overprovisioning (recommended)
* `target = 0.9`: Aggressive scaling (more workers than needed)

**Formula:** `desired_replicas = queue_depth / target`

**CustomMetric**

Scales based on any Prometheus metric your application exposes. Your worker must export the metric on its `/metrics` endpoint.

```toml pyproject.toml theme={null}
[tool.jig.deploy.autoscaling]
metric = "CustomMetric"
custom_metric_name = "vllm:num_requests_running"
target = 80
```

* `custom_metric_name` is required and must match `^[a-zA-Z_:][a-zA-Z0-9_:]*$`.
* `target` defaults to `500` if not specified.

### Scaling behavior

1. **Scale Up:** When the metric exceeds the target, new replicas are added
2. **Scale Down:** When the metric drops below the target, replicas are removed (respecting `min_replicas`)
3. **Graceful Shutdown:** Workers complete the current job before terminating

# Troubleshooting

### Common issues

**Container fails to start**

**Symptoms:** Deployment status shows "failed" or "error"

**Check:**

1. View logs: `tg beta jig logs`
2. Verify health endpoint works locally
3. Check for missing environment variables
4. Ensure sufficient memory allocated

**Jobs stuck in pending**

**Symptoms:** Jobs submitted but never processed

**Check:**

1. Deployment status: `tg beta jig status`
2. Queue status: `tg beta jig queue-status`
3. Worker logs for errors: `tg beta jig logs --follow`
4. Verify `--queue` flag in startup command

**Out of memory errors**

**Symptoms:** Container killed, OOM in logs

**Solutions:**

1. Increase `memory` in deployment config
2. Use `device_map="auto"` for large models
3. Enable gradient checkpointing if training
4. Reduce batch size

**Slow model loading**

**Symptoms:** Long startup time, health check timeouts

**Solutions:**

1. Use volumes for model weights (faster than downloading)
2. Pre-download models in Dockerfile
3. Increase health check timeout

**GPU not detected**

**Symptoms:** `torch.cuda.is_available()` returns False

**Check:**

1. Verify `gpu_count >= 1` in config
2. Check CUDA compatibility with base image
3. Ensure PyTorch is installed with CUDA support

### Debug mode

Enable debug logging:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_DEBUG=1
  tg beta jig deploy
  ```

  ```python Python theme={null}
  import logging

  logging.getLogger().setLevel(logging.DEBUG)
  ```
</CodeGroup>

### Getting help

* View deployment status: `tg beta jig status`
* Check queue: `tg beta jig queue-status`
* Stream logs: `tg beta jig logs --follow`
* Contact support with your deployment name and request IDs

# FAQs

**General**

**Q: What's the difference between Sprocket and a regular HTTP server?**

A: Sprocket integrates with Together's managed job queue, providing automatic job distribution, status reporting, file handling, and graceful shutdown. Use Sprocket for batch/async workloads. Use a regular HTTP server for low-latency request-response APIs.

**Q: Can I use my own Dockerfile?**

A: Yes. Set `dockerfile = "Dockerfile"` in your config and jig will use your custom Dockerfile instead of generating one.

**Q: How do I handle large model weights?**

A: Use volumes (`tg beta jig volumes create`) to upload weights once, then mount them at runtime. This is faster than including weights in the container image.

**Scaling**

**Q: How does autoscaling work?**

A: The autoscaler monitors queue depth and worker utilization. When queue backlog grows, it adds replicas. When workers are idle, it removes them (down to `min_replicas`).

**Q: What's the maximum number of replicas?**

A: Set `max_replicas` in your config. The actual limit depends on your Together organization's quota.

**Q: How long does scaling take?**

A: New replicas typically start within 1-2 minutes, depending on image size and model loading time.

**Jobs**

**Q: How long can a job run?**

A: Default timeout is 5 minutes (`TERMINATION_GRACE_PERIOD_SECONDS`, default 300s). For longer jobs, increase this value in your deployment configuration.

**Q: What happens if a job fails?**

A: The job status is set to "failed" with error details. The worker remains healthy and continues processing other jobs.

**Q: Can I retry failed jobs?**

A: Resubmit the job with the same payload. Automatic retry is not currently supported.

**Billing**

**Q: How am I billed?**

A: You're billed for GPU-hours while replicas are running. Scale to zero (`min_replicas = 0`) when not in use to minimize costs.

**Q: Are there costs for the queue?**

A: Queue usage is included. You're only billed for compute (running replicas).
