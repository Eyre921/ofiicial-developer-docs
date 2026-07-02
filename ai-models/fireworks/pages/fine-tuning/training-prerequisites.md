---
title: "Training Prerequisites & Validation"
source: https://docs.fireworks.ai/fine-tuning/training-prerequisites
path: fine-tuning/training-prerequisites
---

Requirements, validation checks, and common issues when launching RFT jobs

Before launching an RFT job using the [CLI](/fine-tuning/cli-reference) or [Web UI](/fine-tuning/web-ui-guide), ensure you meet these prerequisites and understand the validation process.

## Prerequisites

Before launching an RFT job, ensure you have the following set up. Our quickstart guides will walk you through this.

<AccordionGroup>
  <Accordion title="Dataset prepared and uploaded">
    Your dataset must be in JSONL format with prompts (system and user messages). Each line represents one training example.

    Upload via CLI:

    ```bash theme={null}
    eval-protocol create dataset my-dataset --file dataset.jsonl
    ```

    Or via the [Fireworks dashboard](https://app.fireworks.ai/dashboard/datasets).
  </Accordion>

  <Accordion title="Evaluator created">
    Your reward function must be tested and uploaded. For local evaluators, upload via pytest:

    ```bash theme={null}
    cd evaluator_directory
    pytest my-evaluator-name.py -vs
    ```

    The test automatically registers your evaluator with Fireworks. For remote environment testing, deploy your HTTP service first.
  </Accordion>

  <Accordion title="Fireworks API key configured">
    Set your API key as an environment variable:

    ```bash theme={null}
    export FIREWORKS_API_KEY="fw_your_api_key_here"
    ```

    Or store it in a `.env` file in your project directory.
  </Accordion>

  <Accordion title="Base model selected">
    Choose a base model that supports fine-tuning. Popular options:

    * `accounts/fireworks/models/llama-v3p1-8b-instruct` - Good balance of quality and speed
    * `accounts/fireworks/models/qwen3-0p6b` - Fast training for experimentation
    * `accounts/fireworks/models/llama-v3p1-70b-instruct` - Best quality, slower training

    Check available models at [fireworks.ai/models](https://fireworks.ai/models).
  </Accordion>
</AccordionGroup>

## Job validation

Before starting training, Fireworks validates your configuration:

<AccordionGroup>
  <Accordion title="Dataset format validation">
    * ✅ Valid JSONL format
    * ✅ Each line has `messages` array
    * ✅ Messages have `role` and `content` fields
    * ✅ File size within limits
    * ❌ Missing fields → error with specific line numbers
    * ❌ Invalid JSON → syntax error details
  </Accordion>

  <Accordion title="Evaluator validation">
    * ✅ Evaluator code syntax is valid
    * ✅ Required dependencies are available
    * ✅ Entry point function exists
    * ✅ Test runs completed successfully
    * ❌ Import errors → missing dependencies
    * ❌ Syntax errors → code issues
  </Accordion>

  <Accordion title="Resource availability">
    * ✅ Sufficient GPU quota
    * ✅ Base model supports fine-tuning
    * ✅ Account has RFT permissions
    * ❌ Insufficient quota → request increase
    * ❌ Invalid model → choose different base model
  </Accordion>

  <Accordion title="Parameter validation">
    * ✅ Parameters within valid ranges
    * ✅ Compatible parameter combinations
    * ❌ Invalid ranges → error with allowed values
    * ❌ Conflicting options → resolution guidance
  </Accordion>
</AccordionGroup>

If validation fails, you'll receive specific error messages with instructions to fix the issues.

## Common errors and fixes

<AccordionGroup>
  <Accordion title="Invalid dataset format">
    **Error**: `Dataset validation failed: invalid JSON on line 42`

    **Fix**:

    1. Open your JSONL file
    2. Check line 42 for JSON syntax errors
    3. Common issues: missing quotes, trailing commas, unescaped characters
    4. Validate JSON at jsonlint.com

    **Error**: `Missing required field 'messages'`

    **Fix**: Each dataset row must have a `messages` array:

    ```json theme={null}
    {"messages": [{"role": "user", "content": "..."}]}
    ```
  </Accordion>

  <Accordion title="Evaluator not found">
    **Error**: `Evaluator 'my-evaluator' not found in account`

    **Fix**:

    1. Upload your evaluator first:
       ```bash theme={null}
       cd evaluator_directory
       pytest my-evaluator-name.py -vs
       ```
    2. Or specify evaluator ID if using UI:
       * Check [Evaluators dashboard](https://app.fireworks.ai/dashboard/evaluators)
       * Copy exact evaluator ID
  </Accordion>

  <Accordion title="Insufficient quota">
    **Error**: `Insufficient GPU quota for this job`

    **Fix**:

    1. Check your current quota at [Account Settings](https://app.fireworks.ai/account/settings)
    2. Request a quota increase through the dashboard
    3. Or choose a smaller base model to reduce GPU requirements
  </Accordion>

  <Accordion title="Parameter out of range">
    **Error**: `Learning rate 1e-2 outside valid range [1e-5, 5e-4]`

    **Fix**: Adjust the parameter to be within the allowed range:

    ```bash theme={null}
    --learning-rate 1e-4  # Use default value
    ```

    See [CLI Reference](tools-sdks/firectl/commands/reinforcement-fine-tuning-job-create) for all available parameters.
  </Accordion>

  <Accordion title="Evaluator build timeout">
    **Error**: `Evaluator build timed out after 10 minutes`

    **Fix**:

    1. Check build logs in [Evaluators dashboard](https://app.fireworks.ai/dashboard/evaluators)
    2. Common issues:
       * Large dependencies taking too long to install
       * Network issues downloading packages
       * Syntax errors in requirements.txt
    3. Wait for build to complete, then retry launching your job
    4. Consider splitting large dependencies or using lighter alternatives
  </Accordion>
</AccordionGroup>

## What happens after launching

Once your job is created, here's what happens:

<Steps>
  <Step title="Job queued">
    Your job enters the queue and waits for available GPU resources. Queue time depends on current demand.

    **Status**: `PENDING`
  </Step>

  <Step title="Dataset validation">
    Fireworks validates your dataset to ensure it meets format requirements and quality standards. This typically takes 1-2 minutes.

    **Status**: `VALIDATING`
  </Step>

  <Step title="Training starts">
    The system begins generating rollouts, evaluating them, and updating model weights. You'll see:

    * Rollout generation and evaluation
    * Reward curves updating in real-time
    * Training loss decreasing

    **Status**: `RUNNING`
  </Step>

  <Step title="Monitor progress">
    Track training via the dashboard. See [Monitor Training](/fine-tuning/monitor-training) for details on interpreting metrics and debugging issues.

    **Status**: `RUNNING` → `COMPLETED`
  </Step>

  <Step title="Job completes">
    When training finishes, your fine-tuned model is ready for deployment.

    **Status**: `COMPLETED`

    Next: [Deploy your model](/fine-tuning/deploying-loras) for inference.
  </Step>
</Steps>

## Next steps

<CardGroup>
  <Card title="Launch with CLI" icon="terminal" href="/fine-tuning/cli-reference">
    Use eval-protocol CLI for fast, scriptable launches
  </Card>

  <Card title="Launch with Web UI" icon="browser" href="/fine-tuning/web-ui-guide">
    Use the dashboard for visual, guided job creation
  </Card>

  <Card title="Monitor training" icon="chart-line" href="/fine-tuning/monitor-training">
    Track job progress, inspect rollouts, and debug issues
  </Card>
</CardGroup>
