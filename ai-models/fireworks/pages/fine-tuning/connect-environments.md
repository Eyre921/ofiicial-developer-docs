---
title: "Remote Environment Setup"
source: https://docs.fireworks.ai/fine-tuning/connect-environments
path: fine-tuning/connect-environments
---

Implement the /init endpoint to run evaluations in your infrastructure

If you already have an agent running in your product, or need to run rollouts on your own infrastructure, you can integrate it with RFT using the `RemoteRolloutProcessor`. This delegates rollout execution to an HTTP service you control.

Remote agent are ideal for:

* Multi-turn agentic workflows with tool use
* Access to private databases, APIs, or internal services
* Integration with existing agent codebases
* Complex simulations that require your infrastructure

<Tip>
  New to RFT? Start with [local agent](/fine-tuning/quickstart-math) instead. They're simpler and cover most use cases. Only use remote agent environments when you need access to private infrastructure or have an existing agent to integrate.
</Tip>

## How remote rollouts work

<Frame>
  <img alt="Remote rollout processor flow diagram showing the interaction between Eval Protocol, your remote server, and Fireworks Tracing" />
</Frame>

<Steps>
  <Step title="Fireworks triggers rollout">
    During training, Fireworks calls your service's `POST /init` endpoint with the dataset row and correlation metadata.
  </Step>

  <Step title="Your service processes the rollout">
    Your agent executes the task (e.g., multi-turn conversation, tool calls, simulation steps), logging progress via Fireworks tracing.
  </Step>

  <Step title="Status reporting">
    Your service sends structured logs tagged with rollout metadata to Fireworks so the system can track completion.
  </Step>

  <Step title="Evaluation">
    Once Fireworks detects completion, it pulls the full trace and evaluates it using your scoring logic.
  </Step>
</Steps>

<Note>
  Everything except implementing your remote server is handled automatically by Eval Protocol. You only need to implement the `/init` endpoint and add Fireworks tracing.
</Note>

## Implementing the /init endpoint

Your remote service must implement a single `/init` endpoint that accepts rollout requests.

### Request schema

<ParamField type="object">
  Model configuration including model name and inference parameters like temperature, max\_tokens, etc.
</ParamField>

<ParamField type="array">
  Array of conversation messages to send to the model
</ParamField>

<ParamField type="array">
  Array of available tools for the model (for function calling)
</ParamField>

<ParamField type="string">
  Base URL for making LLM calls through Fireworks tracing (includes correlation metadata)
</ParamField>

<ParamField type="object">
  Rollout execution metadata for correlation (rollout\_id, run\_id, row\_id, etc.)
</ParamField>

<ParamField type="string">
  Fireworks API key to use for model calls
</ParamField>

### Example request

```json theme={null}
{
  "completion_params": {
    "model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
    "temperature": 0.7,
    "max_tokens": 2048
  },
  "messages": [
    { "role": "user", "content": "What is the weather in San Francisco?" }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the weather for a city",
        "parameters": {
          "type": "object",
          "properties": {
            "city": { "type": "string" }
          }
        }
      }
    }
  ],
  "model_base_url": "https://tracing.fireworks.ai/rollout_id/brave-night-42/invocation_id/wise-ocean-15/experiment_id/calm-forest-28/run_id/quick-river-07/row_id/bright-star-91",
  "metadata": {
    "invocation_id": "wise-ocean-15",
    "experiment_id": "calm-forest-28",
    "rollout_id": "brave-night-42",
    "run_id": "quick-river-07",
    "row_id": "bright-star-91"
  },
  "api_key": "fw_your_api_key"
}
```

## Metadata correlation

The `metadata` object contains correlation IDs that you must include when logging to Fireworks tracing. This allows Eval Protocol to match logs and traces back to specific evaluation rows.

Required metadata fields:

* `invocation_id` - Identifies the evaluation invocation
* `experiment_id` - Groups related experiments
* `rollout_id` - Unique ID for this specific rollout (most important)
* `run_id` - Identifies the evaluation run
* `row_id` - Links to the dataset row

<Note>
  `RemoteRolloutProcessor` automatically generates these IDs and sends them to your server. You don't need to create them yourself—just pass them through to your logging.
</Note>

## Fireworks tracing integration

Your remote server must use Fireworks tracing to report rollout status. Eval Protocol polls these logs to detect when rollouts complete.

### Basic setup

```python theme={null}
import logging
from eval_protocol import Status, InitRequest, FireworksTracingHttpHandler, RolloutIdFilter

# Configure Fireworks tracing handler globally
fireworks_handler = FireworksTracingHttpHandler()
logging.getLogger().addHandler(fireworks_handler)

@app.post("/init")
def init(request: InitRequest):
    # Create rollout-specific logger with filter
    rollout_logger = logging.getLogger(f"eval_server.{request.metadata.rollout_id}")
    rollout_logger.addFilter(RolloutIdFilter(request.metadata.rollout_id))

    try:
        # Execute your agent logic here
        result = execute_agent(request)

        # Log successful completion with structured status
        rollout_logger.info(
            f"Rollout {request.metadata.rollout_id} completed",
            extra={"status": Status.rollout_finished()}
        )

        return {"status": "success"}

    except Exception as e:
        # Log errors with structured status
        rollout_logger.error(
            f"Rollout {request.metadata.rollout_id} failed: {e}",
            extra={"status": Status.rollout_error(str(e))}
        )
        raise
```

### Key components

1. **FireworksTracingHttpHandler**: Sends logs to Fireworks tracing service
2. **RolloutIdFilter**: Tags logs with the rollout ID for correlation
3. **Status objects**: Structured status reporting that Eval Protocol can parse
   * `Status.rollout_finished()` - Signals successful completion
   * `Status.rollout_error(message)` - Signals failure with error details

### Alternative: Environment variable approach

For simpler setups, you can use the `EP_ROLLOUT_ID` environment variable instead of manual filters.

<Tabs>
  <Tab title="Single rollout per instance">
    If your server processes one rollout at a time (e.g., serverless functions, container per request):

    ```python theme={null}
    import os
    import logging
    from eval_protocol import Status, InitRequest, FireworksTracingHttpHandler

    # Set rollout ID in environment
    os.environ["EP_ROLLOUT_ID"] = request.metadata.rollout_id

    # Configure handler (automatically picks up EP_ROLLOUT_ID)
    fireworks_handler = FireworksTracingHttpHandler()
    logging.getLogger().addHandler(fireworks_handler)

    logger = logging.getLogger(__name__)

    @app.post("/init")
    def init(request: InitRequest):
        # Logs are automatically tagged with rollout_id
        logger.info("Processing rollout...")
        # ... execute agent logic ...
    ```
  </Tab>

  <Tab title="Separate processes">
    If your `/init` handler spawns separate Python processes for each rollout:

    ```python theme={null}
    import os
    import logging
    import multiprocessing
    from eval_protocol import FireworksTracingHttpHandler, InitRequest

    def execute_rollout_step_sync(request):
        # Set EP_ROLLOUT_ID in the child process
        os.environ["EP_ROLLOUT_ID"] = request.metadata.rollout_id
        logging.getLogger().addHandler(FireworksTracingHttpHandler())

        # Execute your rollout logic here
        # Logs are automatically tagged

    @app.post("/init")
    async def init(request: InitRequest):
        # Do NOT set EP_ROLLOUT_ID in parent process
        p = multiprocessing.Process(
            target=execute_rollout_step_sync,
            args=(request,)
        )
        p.start()
        return {"status": "started"}
    ```
  </Tab>
</Tabs>

### How Eval Protocol uses tracing

1. **Your server logs completion**: Uses `Status.rollout_finished()` or `Status.rollout_error()`
2. **Eval Protocol polls**: Searches Fireworks logs by `rollout_id` tag until completion signal found
3. **Status extraction**: Reads structured status fields (`code`, `message`, `details`) to determine outcome
4. **Trace retrieval**: Fetches full trace of model calls and tool use for evaluation

## Complete example

Here's a minimal but complete remote server implementation:

```python theme={null}
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from eval_protocol import InitRequest, FireworksTracingHttpHandler, RolloutIdFilter, Status
import logging

app = FastAPI()

# Setup Fireworks tracing
fireworks_handler = FireworksTracingHttpHandler()
logging.getLogger().addHandler(fireworks_handler)

@app.post("/init")
async def init(request: InitRequest):
    # Create rollout-specific logger
    rollout_logger = logging.getLogger(f"eval_server.{request.metadata.rollout_id}")
    rollout_logger.addFilter(RolloutIdFilter(request.metadata.rollout_id))

    rollout_logger.info(f"Starting rollout {request.metadata.rollout_id}")

    try:
        # Your agent logic here
        # 1. Make model calls using request.model_base_url
        # 2. Call tools, interact with environment
        # 3. Collect results

        result = run_your_agent(
            messages=request.messages,
            tools=request.tools,
            model_config=request.completion_params,
            api_key=request.api_key
        )

        # Signal completion
        rollout_logger.info(
            f"Rollout {request.metadata.rollout_id} completed successfully",
            extra={"status": Status.rollout_finished()}
        )

        return {"status": "success", "result": result}

    except Exception as e:
        # Signal error
        rollout_logger.error(
            f"Rollout {request.metadata.rollout_id} failed: {str(e)}",
            extra={"status": Status.rollout_error(str(e))}
        )
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )

def run_your_agent(messages, tools, model_config, api_key):
    # Implement your agent logic here
    # Make model calls, use tools, etc.
    pass
```

## Testing locally

Before deploying, test your remote server locally:

<Steps>
  <Step title="Start your server">
    ```bash theme={null}
    uvicorn main:app --reload --port 8080
    ```
  </Step>

  <Step title="Configure RemoteRolloutProcessor">
    In your evaluator test, point to your local server:

    ```python theme={null}
    from eval_protocol.pytest import RemoteRolloutProcessor

    rollout_processor = RemoteRolloutProcessor(
        remote_base_url="http://localhost:8080"
    )
    ```
  </Step>

  <Step title="Run test evaluation">
    ```bash theme={null}
    pytest my-evaluator-name.py -vs
    ```

    This sends test rollouts to your local server and verifies the integration works.
  </Step>
</Steps>

## Deploying your service

Once tested locally, deploy to production:

<AccordionGroup>
  <Accordion title="Deployment checklist">
    * ✅ Service is publicly accessible (or accessible via VPN/private network)
    * ✅ HTTPS endpoint with valid SSL certificate (recommended)
    * ✅ Authentication/authorization configured
    * ✅ Monitoring and logging set up
    * ✅ Auto-scaling configured for concurrent rollouts
    * ✅ Error handling and retry logic implemented
    * ✅ Service availability SLA meets training requirements
  </Accordion>

  <Accordion title="Platform-specific guides">
    **Vercel/Serverless**:

    * One rollout per function invocation
    * Use environment variable approach
    * Configure timeout for long-running evaluations

    **AWS ECS/Kubernetes**:

    * Handle concurrent requests with proper worker configuration
    * Use RolloutIdFilter approach
    * Set up load balancing

    **On-premise**:

    * Ensure network connectivity from Fireworks
    * Configure firewall rules
    * Set up VPN if needed for security
  </Accordion>
</AccordionGroup>

## Connecting to RFT

Once your remote server is deployed, create an RFT job that uses it:

```bash theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --remote-server-url https://your-evaluator.example.com \
  --dataset my-dataset
```

The RFT job will send all rollouts to your remote server for evaluation during training.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Rollouts timing out">
    **Symptoms**: Rollouts show as timed out or never complete

    **Solutions**:

    * Check that your service is logging `Status.rollout_finished()` correctly
    * Verify Fireworks tracing handler is configured
    * Ensure rollout\_id is included in log tags
    * Check for exceptions being swallowed without logging
  </Accordion>

  <Accordion title="Correlation errors">
    **Symptoms**: Eval Protocol can't match logs to rollouts

    **Solutions**:

    * Verify you're using the exact `rollout_id` from request metadata
    * Check that RolloutIdFilter or EP\_ROLLOUT\_ID is set correctly
    * Ensure logs are being sent to Fireworks (check tracing dashboard)
  </Accordion>

  <Accordion title="Performance issues">
    **Symptoms**: Training is slow, high rollout latency

    **Solutions**:

    * Scale your service to handle concurrent requests
    * Optimize your agent logic (caching, async operations)
    * Add more workers or instances
    * Profile your code to find bottlenecks
  </Accordion>

  <Accordion title="Authentication failures">
    **Symptoms**: Model calls fail, API errors

    **Solutions**:

    * Verify API key is passed correctly from request
    * Check that your service has network access to Fireworks
    * Ensure model\_base\_url is used for traced calls
  </Accordion>
</AccordionGroup>

## Example implementations

Learn by example:

<CardGroup>
  <Card title="SVG Agent (TypeScript)" icon="image" href="/fine-tuning/quickstart-svg-agent">
    Complete walkthrough using a Vercel TypeScript server for SVG generation
  </Card>

  <Card title="Hello World Example" icon="code" href="https://github.com/eval-protocol/remote-rollout-processor-hello-world">
    Minimal Python implementation showing the basics
  </Card>
</CardGroup>

## Next steps

<CardGroup>
  <Card title="Launch training" icon="rocket" href="/fine-tuning/cli-reference">
    Launch your RFT job using the CLI
  </Card>

  <Card title="Monitor training" icon="chart-line" href="/fine-tuning/monitor-training">
    Track rollout progress and debug issues
  </Card>

  <Card title="Eval Protocol docs" icon="book" href="https://evalprotocol.io/tutorial/remote-rollout-processor">
    Full Remote Rollout Processor tutorial
  </Card>

  <Card title="Evaluator best practices" icon="lightbulb" href="/fine-tuning/evaluators">
    Design effective reward functions
  </Card>
</CardGroup>
