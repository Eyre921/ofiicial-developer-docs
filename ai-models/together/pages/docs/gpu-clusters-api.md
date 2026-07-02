---
title: "API & integrations"
source: https://docs.together.ai/docs/gpu-clusters-api
path: docs/gpu-clusters-api
---

Manage clusters programmatically with the Together CLI, REST API, and SkyPilot

## Overview

All cluster management operations are available through multiple interfaces for programmatic control and automation:

* **Together CLI:** Command-line tool for cluster operations.
* **REST API:** Full HTTP API for custom integrations. See the [GPU Clusters API reference](/reference/clusters-create).
* **SkyPilot:** Orchestrate AI workloads across clusters.

## Together CLI

The Together CLI provides a command-line interface for managing clusters, storage, and scaling. It's included with the Together Python SDK.

### Installation

```bash theme={null}
# Install
uv tool install "together[cli]"

# List commands
tg --help
```

### Authentication

The CLI authenticates with the `TOGETHER_API_KEY` environment variable. You can find your API token in your [account settings](https://api.together.ai/settings/projects/~first/api-keys):

```bash theme={null}
export TOGETHER_API_KEY=<your_key>
```

### Common commands

**Create a cluster:**

```bash theme={null}
tg beta clusters create \
  --name my-cluster \
  --num-gpus 8 \
  --gpu-type H100_SXM \
  --region us-central-8 \
  --billing-type ON_DEMAND \
  --cluster-type KUBERNETES
```

**Specify billing type (reserved vs on-demand):**

```bash theme={null}
# Reserved capacity
tg beta clusters create \
  --name my-cluster \
  --num-gpus 8 \
  --gpu-type H100_SXM \
  --region us-central-8 \
  --billing-type RESERVED \
  --duration-days 30 \
  --cluster-type KUBERNETES

# On-demand capacity
tg beta clusters create \
  --name my-cluster \
  --num-gpus 8 \
  --gpu-type H100_SXM \
  --region us-central-8 \
  --billing-type ON_DEMAND \
  --cluster-type KUBERNETES
```

**Delete a cluster:**

```bash theme={null}
tg beta clusters delete [CLUSTER_ID]
```

**List clusters:**

```bash theme={null}
tg beta clusters list
```

**Scale a cluster:**

```bash theme={null}
tg beta clusters update [CLUSTER_ID] --num-gpus 16
```

**Download cluster credentials (kubeconfig):**

```bash theme={null}
tg beta clusters get-credentials [CLUSTER_ID] --set-default-context
```

<Note>
  Run `tg beta clusters create` with no flags to launch an interactive prompt that walks through the required fields. See the [clusters CLI reference](/reference/cli/clusters) for the full command and flag list.
</Note>

## SkyPilot Integration

Orchestrate AI workloads on GPU Clusters using SkyPilot for simplified cluster management and job scheduling.

### Installation

```bash theme={null}
uv pip install skypilot[kubernetes]
```

### Setup

1. **Launch a Kubernetes cluster** via Together Cloud

2. **Configure kubeconfig:**

Download the cluster credentials with the Together CLI. This merges the cluster context into your local `~/.kube/config`:

```bash theme={null}
tg beta clusters get-credentials [CLUSTER_ID] --set-default-context
```

3. **Verify SkyPilot access:**

```bash theme={null}
sky check k8s
```

Expected output:

```
Checking credentials to enable infra for SkyPilot.
  Kubernetes: enabled [compute]
    Allowed contexts:
    └── t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin: enabled.

🎉 Enabled infra 🎉
  Kubernetes [compute]
```

4. **Check available GPUs:**

```bash theme={null}
sky show-gpus --infra k8s
```

### Example: Launch a Workload

Create a SkyPilot task file (`task.yaml`):

```yaml theme={null}
resources:
  accelerators: H100:8
  cloud: kubernetes

setup: |
  pip install torch transformers

run: |
  python train.py
```

Launch the task:

```bash theme={null}
sky launch -c my-job task.yaml
```

### Example: Fine-tune GPT OSS

Download the [gpt-oss-20b.yaml](https://github.com/skypilot-org/skypilot/tree/master/llm/gpt-oss-finetuning#lora-finetuning) configuration.

Launch fine-tuning:

```bash theme={null}
sky launch -c gpt-together gpt-oss-20b.yaml
```

### Benefits

* **Simplified orchestration** – Abstract away Kubernetes complexity.
* **Multi-cloud support** – Same workflow across different clouds.
* **Cost optimization** – Auto-select cheapest available resources.
* **Job management** – Easy monitoring and cancellation.

## Automation Patterns

### CI/CD Integration

**GitHub Actions example:**

```yaml theme={null}
name: Train Model

on: push

jobs:
  train:
    runs-on: ubuntu-latest
    env:
      TOGETHER_API_KEY: ${{ secrets.TOGETHER_API_KEY }}
    steps:
      - uses: actions/checkout@v3

      - name: Install the Together CLI
        run: uv tool install "together[cli]"

      - name: Create GPU Cluster
        run: |
          tg beta clusters create \
            --name training-${{ github.sha }} \
            --num-gpus 8 \
            --billing-type ON_DEMAND \
            --gpu-type H100_SXM \
            --region us-central-8 \
            --cluster-type KUBERNETES \
            --non-interactive

      - name: Run Training
        run: |
          # Submit training job to cluster
          kubectl apply -f training-job.yaml

      - name: Cleanup
        if: always()
        run: |
          tg beta clusters delete [CLUSTER_ID]
```

### Scheduled Jobs

**Cron-based cluster creation:**

```bash theme={null}
# Create cluster daily at 6 AM for batch processing
0 6 * * * tg beta clusters create \
  --name daily-batch \
  --num-gpus 16 \
  --billing-type ON_DEMAND \
  --gpu-type H100_SXM \
  --region us-central-8 \
  --cluster-type KUBERNETES \
  --non-interactive
```

### Auto-scaling Scripts

Scale a cluster up or down based on demand with the Together CLI:

```bash theme={null}
# Scale based on job queue length
if [ "$JOB_QUEUE_LENGTH" -gt 100 ]; then
  tg beta clusters update [CLUSTER_ID] --num-gpus 16
else
  tg beta clusters update [CLUSTER_ID] --num-gpus 8
fi
```

## Best Practices

### API usage

* **Use environment variables** for API keys (never hardcode).
* **Implement retry logic** for transient failures.
* **Check cluster status** before submitting jobs.
* **Clean up resources** after completion.

### CLI usage

* **Set `TOGETHER_API_KEY`** in your environment so commands authenticate automatically.
* **Use cluster IDs** for cluster references (more reliable than names).
* **Pass `--non-interactive`** (or `--json`) to skip prompts in scripts and CI.
* **Script common operations** for team consistency.

## Troubleshooting

### Authentication issues

* Verify your API key is set: `echo $TOGETHER_API_KEY`
* Confirm the key is valid in your [account settings](https://api.together.ai/settings/projects/~first/api-keys)

### API rate limits

* Implement exponential backoff
* Batch operations when possible
* Contact support for higher limits

## What's Next?

* [Review API reference documentation](/reference/clusters-create)
* [Explore the clusters CLI reference](/reference/cli/clusters)
* [Learn about cluster management](/docs/gpu-clusters-management)
* [Understand billing](/docs/gpu-clusters-billing)
