---
title: "Models"
source: https://docs.together.ai/reference/cli/models-beta
path: reference/cli/models-beta
---

Register, upload, and inspect models and adapters for dedicated model inference from your terminal.

Register, upload, and inspect the models and adapters you deploy for [dedicated model inference](/docs/dedicated-endpoints/overview) deployments with the 2.0 API.

Bringing your own weights is a two-step flow:

1. [`create`](#create) registers a model record (metadata only), then
2. [`upload`](#upload) or [`remote-uploads create`](#remote-uploads-create) adds the weight files.

See [Custom models](/docs/dedicated-endpoints/custom-models) for the end-to-end workflow.

<Note>
  These commands target the 2.0 API. For the 1.0 model commands, see [`models`](/reference/cli/models). Commands run within a Together [project](/docs/projects).
</Note>

## Create

Register a new model record. This creates metadata only. It does not upload any files. Upload the weights afterward with [`upload`](#upload) or [`remote-uploads create`](#remote-uploads-create).

```bash Shell theme={null}
tg beta models create my-custom-glm \
  --base-model zai-org/GLM-5.2
```

Alias: `tg beta models -c`.

### Parameters

| Flag                        | Description                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NAME`                      | (**required**) The inference-addressable name for the model.                                                                                                                                        |
| `--type [model \| adapter]` | Whether the record holds full weights (`model`) or a LoRA adapter (`adapter`). Set once at create time. File operations derive the type from the record. Default: `model`.                          |
| `--base-model [string]`     | (**required**) The supported base model this model derives from. Accepts a base model ID (`ml_...`) or a deploy model name (for example `zai-org/GLM-5.2`). Run `tg beta models public` to find it. |

## Upload

Upload weight files from your local machine to an existing model or adapter record.

```bash Shell theme={null}
tg beta models upload ml_abc123 ./my-model-weights
```

### Parameters

| Flag         | Description                                                         |
| ------------ | ------------------------------------------------------------------- |
| `MODEL-ID`   | (**required**) The existing model or adapter ID to upload files to. |
| `LOCAL-PATH` | (**required**) The local file or directory to upload.               |

## List

List the models in the current project.

```bash Shell theme={null}
tg beta models list
```

Alias: `tg beta models ls`.

### Parameters

| Flag               | Description                         |
| ------------------ | ----------------------------------- |
| `--limit [number]` | Maximum number of models to return. |
| `--after [string]` | Pagination cursor to start from.    |

## Retrieve

Get a single model by ID.

```bash Shell theme={null}
tg beta models retrieve ml_abc123
```

Alias: `tg beta models get`.

## Update

Update a model record. Only the fields you pass are changed.

```bash Shell theme={null}
tg beta models update ml_abc123 \
  --name my-renamed-model \
  --description "Fine-tuned GLM for support triage"
```

### Parameters

| Flag                     | Description                            |
| ------------------------ | -------------------------------------- |
| `ID`                     | (**required**) The model ID to update. |
| `--name [string]`        | New inference-addressable name.        |
| `--description [string]` | New description.                       |

## Delete

Delete a model record. This removes the metadata. It does not delete uploaded files.

```bash Shell theme={null}
tg beta models delete ml_abc123
```

Alias: `tg beta models -d`.

## Configs

List the deployable configs for a model. Pass a config ID to `tg beta endpoints deploy --config` to deploy that specific configuration.

```bash Shell theme={null}
tg beta models configs ml_abc123
```

### Parameters

| Flag               | Description                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| `MODEL`            | (**required**) The model to list configs for. Accepts a model ID (`ml_...`), a resource path, or a model name. |
| `--limit [number]` | Maximum number of configs to return.                                                                           |
| `--after [string]` | Pagination cursor to start from.                                                                               |

## List files

List the files in a model or adapter.

```bash Shell theme={null}
tg beta models ls-files ml_abc123
```

### Parameters

| Flag                  | Description                             |
| --------------------- | --------------------------------------- |
| `ID`                  | (**required**) The model or adapter ID. |
| `--revision [string]` | Revision ID to filter files for.        |

## List revisions

List the revisions of a model.

```bash Shell theme={null}
tg beta models ls-revisions ml_abc123
```

### Parameters

| Flag | Description                  |
| ---- | ---------------------------- |
| `ID` | (**required**) The model ID. |

## Download

Download the weight files of a model or adapter to a local directory.

```bash Shell theme={null}
tg beta models download ml_abc123 ./local-dir
```

### Parameters

| Flag                  | Description                                                                  |
| --------------------- | ---------------------------------------------------------------------------- |
| `MODEL-ID`            | (**required**) The model or adapter ID (a `project/name` path or object ID). |
| `LOCAL-PATH`          | (**required**) The local directory to write files into.                      |
| `--revision [string]` | Pin the download to a specific revision. Defaults to the latest.             |
| `--files [string]`    | Restrict to specific file paths. Repeatable, and commas are allowed.         |
| `--format [hf]`       | Output layout. Use `hf` for a Hugging Face snapshot layout.                  |

## List public models

List the publicly visible models across all projects. Use this to find a base model ID or name for [`create`](#create) or a model name for [`tg beta endpoints deploy`](/reference/cli/endpoints-beta#deploy).

```bash Shell theme={null}
tg beta models public \
  --product dedicated \
  --modality text
```

Add `--json` to see each model's full record, including its `id` (which subsequent operations require) and its `deploymentProfiles` array. A model can expose more than one profile, each pairing a certified config with a hardware and parallelism choice, so read the `id`, `config`, `gpuType`, and `gpuCount` of the profile you want before deploying. See [Choose a hardware config](/docs/dedicated-endpoints/configs).

### Parameters

| Flag                                                 | Description                         |
| ---------------------------------------------------- | ----------------------------------- |
| `SEARCH`                                             | Search by ID, name, or description. |
| `--limit [number]`                                   | Maximum number of models to return. |
| `--after [string]`                                   | Pagination cursor to start from.    |
| `--modality [text \| image \| audio \| video]`       | Filter by input modality.           |
| `--product [serverless \| dedicated \| fine-tuning]` | Filter by product surface.          |

## List org models

List the internal-visibility models in your organization.

```bash Shell theme={null}
tg beta models org
```

### Parameters

| Flag               | Description                         |
| ------------------ | ----------------------------------- |
| `--limit [number]` | Maximum number of models to return. |
| `--after [string]` | Pagination cursor to start from.    |

## Remote uploads

Import model weights server-side from a Hugging Face repo or a presigned S3/GCS URL, without downloading them locally first. Create a remote upload job against an existing model record, then poll it until it succeeds.

### Remote uploads create

Start a remote upload job.

```bash Shell theme={null}
tg beta models remote-uploads create ml_abc123 \
  --from https://huggingface.co/zai-org/GLM-5.2
```

For gated or private Hugging Face repos, pass a source credential with `--token`. For S3 or GCS, pass a presigned archive URL as `--from` (no token needed).

#### Parameters

| Flag               | Description                                                                           |
| ------------------ | ------------------------------------------------------------------------------------- |
| `MODEL-ID`         | (**required**) The existing model or adapter ID to upload files to.                   |
| `--from [string]`  | (**required**) The remote source URL (a Hugging Face repo or a presigned S3/GCS URL). |
| `--token [string]` | Source credential for gated or private Hugging Face repos.                            |

### Remote uploads retrieve

Get a remote upload job by ID. Poll this until `status` is `REMOTE_UPLOAD_STATUS_SUCCEEDED`.

```bash Shell theme={null}
tg beta models remote-uploads retrieve job_abc123
```

#### Parameters

| Flag | Description                              |
| ---- | ---------------------------------------- |
| `ID` | (**required**) The remote upload job ID. |

### Remote uploads list

List remote upload jobs.

```bash Shell theme={null}
tg beta models remote-uploads list
```

#### Parameters

| Flag               | Description                       |
| ------------------ | --------------------------------- |
| `--limit [number]` | Maximum number of jobs to return. |
| `--after [string]` | Pagination cursor to start from.  |

## Global options

Every command also accepts the [global parameters](/reference/cli/getting-started#global-parameters), including `--json` for machine-readable output and `--project` to override the target project.

## Resource IDs

| Prefix | Resource                                                 |
| ------ | -------------------------------------------------------- |
| `ml_`  | Model or adapter record.                                 |
| `cr_`  | Config revision (a deployable configuration of a model). |
| `job_` | Remote upload job.                                       |
