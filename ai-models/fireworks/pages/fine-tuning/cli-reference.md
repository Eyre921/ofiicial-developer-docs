---
title: "Training Overview"
source: https://docs.fireworks.ai/fine-tuning/cli-reference
path: fine-tuning/cli-reference
---

Launch RFT jobs using the eval-protocol CLI

The Eval Protocol CLI provides the fastest, most reproducible way to launch RFT jobs. This page covers everything you need to know about using `eval-protocol create rft`.

<Note>
  Before launching, review [Training Prerequisites & Validation](/fine-tuning/training-prerequisites) for requirements, validation checks, and common errors.
</Note>

<Tip>
  Already familiar with [firectl](/fine-tuning/cli-reference#using-firectl-cli-alternative)? Use it as an alternative to eval-protocol.
</Tip>

## Installation and setup

The following guide will help you:

* Upload your evaluator to Fireworks. If you don't have one yet, see [Concepts > Evaluators](/fine-tuning/evaluators)
* Upload your dataset to Fireworks
* Create and launch the RFT job

<Steps>
  <Step title="Install Eval Protocol CLI">
    ```bash theme={null}
    pip install eval-protocol
    ```

    Verify installation:

    ```bash theme={null}
    eval-protocol --version
    ```
  </Step>

  <Step title="Set up authentication">
    Configure your Fireworks API key:

    ```bash theme={null}
    export FIREWORKS_API_KEY="fw_your_api_key_here"
    ```

    Or create a `.env` file:

    ```bash theme={null}
    FIREWORKS_API_KEY=fw_your_api_key_here
    ```
  </Step>

  <Step title="Test your evaluator locally">
    Before training, verify your evaluator works. This command discovers and runs your `@evaluation_test` with pytest. If a Dockerfile is present, it builds an image and runs the test in Docker; otherwise it runs on your host.

    ```bash theme={null}
    cd evaluator_directory
    ep local-test
    ```

    <Note>
      If using a Dockerfile, it must use a Debian-based image (no Alpine or CentOS), be single-stage (no multi-stage builds), and only use supported instructions: `FROM`, `RUN`, `COPY`, `ADD`, `WORKDIR`, `USER`, `ENV`, `CMD`, `ENTRYPOINT`, `ARG`. Instructions like `EXPOSE` and `VOLUME` are ignored. See the [RFT quickstart guide](/fine-tuning/quickstart-svg-agent) for details.
    </Note>
  </Step>

  <Step title="Create the RFT job">
    From the directory where your evaluator and dataset (dataset.jsonl) are located,

    ```bash theme={null}
    eval-protocol create rft \
      --base-model accounts/fireworks/models/qwen3-4b \
      --output-model my-model-name 
    ```

    The CLI will:

    * Upload evaluator code (if changed)
    * Upload dataset (if changed)
    * Create the RFT job
    * Display dashboard links for monitoring

    Expected output:

    ```
    Created Reinforcement Fine-tuning Job
       name: accounts/your-account/reinforcementFineTuningJobs/abc123

    Dashboard Links:
       Evaluator: https://app.fireworks.ai/dashboard/evaluators/your-evaluator
       Dataset:   https://app.fireworks.ai/dashboard/datasets/your-dataset
       RFT Job:   https://app.fireworks.ai/dashboard/fine-tuning/reinforcement/abc123
    ```
  </Step>

  <Step title="Monitor training">
    Click the RFT Job link to watch training progress in real-time. See [Monitor Training](/fine-tuning/monitor-training) for details.
  </Step>
</Steps>

## Common CLI options

Customize your RFT job with these flags:

**Model and output**:

```bash theme={null}
--base-model accounts/fireworks/models/qwen3-4b  # Base model to fine-tune
--output-model my-custom-name                                   # Name for fine-tuned model
```

**Training parameters**:

```bash theme={null}
--epochs 2                    # Number of training epochs (default: 1)
--learning-rate 5e-5          # Learning rate (default: 1e-4)
--lora-rank 16                # LoRA rank (default: 8)
--batch-size 65536            # RFT V1 packed-token budget; remains active with --batch-size-samples
--chunk-size 200              # Prompts rolled out per GRPO training step (default: 200). -1 disables chunking.
```

**Loss method**:

```bash theme={null}
--rl-loss-method dapo           # RL loss method: grpo (default), dapo, gspo-token
--rl-kl-beta 0.001              # KL beta override (only for grpo; rejected for dapo/gspo-token)
```

**Rollout (sampling) parameters**:

```bash theme={null}
--temperature 0.8               # Sampling temperature (default: 0.7)
--n 8                           # Number of rollouts per prompt (default: 4)
--response-candidates-count 8   # Alias for --n in firectl (default: 8, minimum: 2)
--max-tokens 4096               # Max tokens per response (default: 32768)
--top-p 0.95                    # Top-p sampling (default: 1.0)
--top-k 50                      # Top-k sampling (default: 40)
--max-concurrent-rollouts 64    # Max in-flight rollouts per job (default: 96, or the value set in @evaluation_test). Throughput only; no training effect.
```

**Remote environments**:

```bash theme={null}
--remote-server-url https://your-evaluator.example.com  # For remote rollout processing
```

**Force re-upload**:

```bash theme={null}
--force                       # Re-upload evaluator even if unchanged
```

See all options:

```bash theme={null}
eval-protocol create rft --help
```

## Advanced options

<AccordionGroup>
  <Accordion title="Weights & Biases integration">
    Track training metrics in W\&B for deeper analysis:

    ```bash theme={null}
    eval-protocol create rft \
      --base-model accounts/fireworks/models/qwen3-4b \
      --wandb-project my-rft-experiments \
      --wandb-entity my-org
    ```

    Set `WANDB_API_KEY` in your environment first.
  </Accordion>

  <Accordion title="Custom checkpoint frequency">
    Save intermediate checkpoints during training:

    ```bash theme={null}
    firectl rftj create \
      --base-model accounts/fireworks/models/qwen3-4b \
      --checkpoint-frequency 500  # Save every 500 steps
      ...
    ```

    Available in `firectl` only.
  </Accordion>

  <Accordion title="Custom timeout">
    For evaluators that need more time:

    ```bash theme={null}
    firectl rftj create \
      --rollout-timeout 300  # 5 minutes per rollout
      ...
    ```

    Default is 60 seconds. Increase for complex evaluations.
  </Accordion>
</AccordionGroup>

For other tuning parameters — rollout concurrency, chunk size, loss method, and more — see [Parameter Tuning](/fine-tuning/parameter-tuning).

## Examples

**Fast experimentation** (small model, 1 epoch):

```bash theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-4b \
  --output-model quick-test
```

**High-quality training** (more rollouts, higher temperature):

```bash theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-4b \
  --output-model high-quality-model \
  --n 8 \
  --temperature 1.0
```

**Remote environment** (for multi-turn agents):

```bash theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-4b \
  --remote-server-url https://your-agent.example.com \
  --output-model remote-agent
```

**Multiple epochs with custom learning rate**:

```bash theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-4b \
  --epochs 3 \
  --learning-rate 5e-5 \
  --output-model multi-epoch-model
```

## Using `firectl` CLI (Alternative)

For users already familiar with Fireworks `firectl`, you can create RFT jobs directly:

```bash theme={null}
firectl rftj create \
  --base-model accounts/fireworks/models/qwen3-4b \
  --dataset accounts/your-account/datasets/my-dataset \
  --evaluator accounts/your-account/evaluators/my-evaluator \
  --output-model my-finetuned-model
```

**Differences from `eval-protocol`**:

* Requires fully qualified resource names (accounts/...)
* Must manually upload evaluators and datasets first
* More verbose but offers finer control
* Same underlying API as `eval-protocol`

See [firectl documentation](/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-create) for all options.

## Next steps

<CardGroup>
  <Card title="Prerequisites & Validation" icon="list-check" href="/fine-tuning/training-prerequisites">
    Review requirements, validation, and common errors
  </Card>

  <Card title="Monitor training" icon="chart-line" href="/fine-tuning/monitor-training">
    Track job progress, inspect rollouts, and debug issues
  </Card>

  <Card title="Parameter tuning" icon="sliders" href="/fine-tuning/parameter-tuning">
    Learn how to adjust parameters for better results
  </Card>
</CardGroup>
