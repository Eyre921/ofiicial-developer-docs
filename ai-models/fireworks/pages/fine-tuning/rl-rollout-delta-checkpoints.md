---
title: "Incremental Snapshots (ARC2)"
source: https://docs.fireworks.ai/fine-tuning/rl-rollout-delta-checkpoints
path: fine-tuning/rl-rollout-delta-checkpoints
---

Build ARC2 incremental checkpoints and signal delta hot-loads for BYOT RL rollout integrations.

<Warning>
  **Early Access Feature.** This page is part of the same private-preview
  external-bucket hot-load workflow for RL rollouts. Contact Fireworks to enable
  this path on your account before using non-`FW_HOSTED` storage.
</Warning>

<Note>
  Start with the linear workflow in [RL Rollouts with Your Own
  Trainer](/fine-tuning/rl-rollout-integration) if you have not completed a first
  full snapshot and rollout yet.
</Note>

Use **incremental snapshots** between full snapshots to reduce upload size and weight-update time. Each incremental snapshot is a compressed delta against a **previous snapshot identity** already loaded on the deployment.

Fireworks supports the public **ARC2** format (`compression_format: "arc_v2"`) with **Adler32** checksums (`checksum_format: "alder32"`).

## Snapshot cadence

| When                 | Snapshot type   | Notes                                                                 |
| -------------------- | --------------- | --------------------------------------------------------------------- |
| First training step  | **Full**        | HuggingFace layout under a new `identity`                             |
| Every 20th–30th step | **Full**        | Resets the chain; faster recovery if a delta is corrupt               |
| All other steps      | **Incremental** | `previous_snapshot_identity` must match the snapshot currently served |

If an incremental hot-load fails or the chain is wedged, publish a new **full** snapshot and see [Ledger & debugging](/fine-tuning/rl-rollout-debugging).

## Why incremental?

* **Smaller uploads** — Typical compression ratios exceed 20× versus re-uploading full weights.
* **Faster loads** — Less data over the network; merge applies on replicas that already hold the previous snapshot.
* **Chain dependency** — Each incremental snapshot must reference the correct `previous_snapshot_identity` (the last successfully loaded snapshot).

## Create ARC2 deltas

You need a **pair of consecutive full checkpoints** on disk (or tensors in memory) and produce **diff safetensors** for the new step.

### Compression library

Use the Fireworks delta compression utilities. A reference implementation is available in this [GitHub gist](https://gist.github.com/ericwuatfirworks/b17ed8086cfe1b42caac556c3d364958) (`delta_compress_files_to_file`, `arc_v2`, `alder32`).

**Per-file example** (previous full snapshot `version_001`, new full snapshot `version_002_full`, upload diff as `version_002`):

```python theme={null}
from delta import delta_compress_files_to_file  # from the gist / your vendored copy

delta_compress_files_to_file(
    src="version_001/model-00000.safetensors",
    dst="version_002_full/model-00000.safetensors",
    diff_file="version_002/model-00000.safetensors",
    compression_format="arc_v2",
)
```

Repeat for each safetensors shard (same filenames as the base layout). Copy non-weight files (for example `config.json`, tokenizer) from the new full tree into `version_002/` as needed.

<Note>
  If the previous checkpoint is already in trainer CPU memory, the gist also exposes
  tensor-level helpers (`delta_compress_dicts`, etc.) so you can avoid writing full
  intermediates to disk.
</Note>

Upload only the **incremental directory** for the new `identity` (for example `s3://.../version_002/`). Do not re-upload the entire full checkpoint every step.

## Upload workflow

1. Build diffs with `arc_v2` for each `.safetensors` file.
2. Upload all files under the new `identity` prefix (same bucket parent as [snapshot layout](/fine-tuning/rl-rollout-integration#snapshot-layout)).
3. [Signal incremental ready](#signal-incremental-snapshot-ready) via `POST /hot_load`.
4. Poll `GET /hot_load` until all replicas are ready (same criteria as the [integration guide](/fine-tuning/rl-rollout-integration#poll-load-status)).

## Signal incremental snapshot ready

After all files are uploaded, signal the deployment to load the incremental snapshot:

```bash theme={null}
curl -X POST https://api.fireworks.ai/hot_load/v1/models/hot_load \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
  -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
  -H "Content-Type: application/json" \
  -d '{
    "identity": "version_002",
    "incremental_snapshot_metadata": {
      "previous_snapshot_identity": "version_001",
      "compression_format": "arc_v2",
      "checksum_format": "alder32"
    },
    "reset_prompt_cache": "all"
  }'
```

<ParamField type="string">
  The `identity` of the snapshot already loaded on the deployment (must exist in the ledger).
</ParamField>

<ParamField type="string">
  Use `"arc_v2"` for BYOT integrations.
</ParamField>

<ParamField type="string">
  Use `"alder32"`.
</ParamField>

<ParamField type="string">
  `all` (default), `none`, or `new_session`. See [KV cache behavior for RL rollouts](/guides/rollout-inference#kv-cache-behavior-for-rl-rollouts) for active stream, session ID, and reset-option semantics.
</ParamField>

Poll until every replica has `readiness: true` and `current_snapshot_identity == "version_002"`.

## Reference

* Every snapshot needs a new `identity` (single directory name, no `/`).
* Point `previous_snapshot_identity` at the snapshot the deployment is serving before this load.
* Upload incremental **diff** safetensors under the new `identity`; keep periodic **full** snapshots for recovery.

## Related pages

<CardGroup>
  <Card title="Quickstart (BYOT)" icon="rotate" href="/fine-tuning/rl-rollout-integration">
    Prerequisites, deployment setup, first full snapshot, and rollouts.
  </Card>

  <Card title="Ledger & debugging" icon="bug" href="/fine-tuning/rl-rollout-debugging">
    Inspect snapshot history and recover from a broken chain.
  </Card>

  <Card title="Inference for RL rollouts" icon="bolt" href="/guides/rollout-inference">
    Session affinity, policy version, and MoE Router Replay.
  </Card>
</CardGroup>
