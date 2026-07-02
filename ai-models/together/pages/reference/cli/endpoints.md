---
title: "Endpoints"
source: https://docs.together.ai/reference/cli/endpoints
path: reference/cli/endpoints
---

Create, update, and manage dedicated inference endpoints from your terminal.

Create and manage [dedicated endpoints](/docs/dedicated-endpoints/overview) for model inference.

## Endpoint ID

Many commands require an `ENDPOINT_ID` to identify which endpoint to operate on. The endpoint ID is a unique identifier assigned at creation time, in the format `endpoint-<uuid>`.

For example: `endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462`.

<Note>
  The endpoint ID is different from the model name (e.g., `meta-llama/Llama-3.3-70B-Instruct-Turbo`) or the display name you set with `--display-name`.
</Note>

### Find your endpoint ID

To find your endpoint ID, you can:

* Run the `tg endpoints create` command to create an endpoint. The endpoint ID is returned in the output.
* Run the `tg endpoints list` command to list all your endpoints. The endpoint ID is displayed for each endpoint.
* View the endpoint details page in the [Together AI console](https://api.together.ai/endpoints).

## Create

Create a new dedicated endpoint.

```bash Shell theme={null}
tg endpoints create \
  --model meta-llama/Llama-3.3-70B-Instruct-Turbo \
  --hardware 4x_nvidia_h100_80gb_sxm \
  --display-name "My Endpoint" \
  --wait
```

### Parameters

| Flag                           | Description                                                                                                                                            |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--model [string]`             | (**required**) The model to deploy.                                                                                                                    |
| `--hardware [string]`          | (**required**) GPU type to use for inference.<br /><br />Use `tg endpoints hardware` to discover available GPU identifiers.                            |
| `--min-replicas [number]`      | Minimum number of replicas to deploy. Default: 1.                                                                                                      |
| `--max-replicas [number]`      | Maximum number of replicas to deploy. Default: 1.                                                                                                      |
| `--display-name [string]`      | A human-readable name for the endpoint.                                                                                                                |
| `--no-auto-start`              | Create the endpoint in `STOPPED` state instead of auto-starting it.                                                                                    |
| `--no-speculative-decoding`    | Disable speculative decoding for this endpoint.                                                                                                        |
| `--inactive-timeout [number]`  | Minutes of inactivity after which the endpoint auto-stops. Set to 0 to disable.                                                                        |
| `--availability-zone [string]` | Start the endpoint in a specific availability zone (e.g. `us-central-4b`).<br /><br />Use `tg endpoints availability-zones` to discover valid options. |
| `--wait`                       | Wait for the endpoint to be ready after creation. Cannot be combined with `--json`.                                                                    |

<Note>
  `--no-prompt-cache` is accepted for backward compatibility but no longer has any effect.
</Note>

## Hardware

List all hardware options (optionally filtered by model and availability).

<CodeGroup>
  ```bash List all theme={null}
  tg endpoints hardware
  ```

  ```bash Filter for model theme={null}
  # Only returns hardware for this model
  tg endpoints hardware \
    --model meta-llama/Llama-3.3-70B-Instruct-Turbo
  ```

  ```bash Available hardware theme={null}
  # Only returns hardware for this model that is currently available
  tg endpoints hardware \
    --model meta-llama/Llama-3.3-70B-Instruct-Turbo \
    --available
  ```

  ```bash JSON theme={null}
  # Get the id of the first usable option for a given model.
  # You can pass this directly to an endpoint create call.
  tg endpoints hardware \
    --model meta-llama/Llama-3.3-70B-Instruct-Turbo \
    --available \
    --json | jq '.[0].id'

  # Prints "2x_nvidia_h100_80gb_sxm"
  ```
</CodeGroup>

### Parameters

| Flag               | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `--model [string]` | Filter hardware that is compatible with a given model. |
| `--available`      | Filter for only hardware that is currently available.  |

## Retrieve

Print details for a specific endpoint.

```bash Shell theme={null}
tg endpoints retrieve endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

## Update

Update the configuration of an existing endpoint.

```bash Shell theme={null}
tg endpoints update endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462 \
  --min-replicas 2 \
  --max-replicas 4 
```

### Parameters

At least one update flag must be supplied.

| Flag                          | Description                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------- |
| `--display-name [string]`     | New human-readable name for the endpoint.                                       |
| `--min-replicas [number]`     | New minimum number of replicas to maintain.                                     |
| `--max-replicas [number]`     | New maximum number of replicas to scale up to.                                  |
| `--inactive-timeout [number]` | Minutes of inactivity after which the endpoint auto-stops. Set to 0 to disable. |

## Start

Start a dedicated endpoint.

```bash Shell theme={null}
tg endpoints start endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Parameters

| Flag     | Description                     |
| -------- | ------------------------------- |
| `--wait` | Wait for the endpoint to start. |

## Stop

Stop a dedicated endpoint.

```bash Shell theme={null}
tg endpoints stop endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Parameters

| Flag     | Description                    |
| -------- | ------------------------------ |
| `--wait` | Wait for the endpoint to stop. |

## Delete

Delete a dedicated endpoint.

```bash Shell theme={null}
tg endpoints delete endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

## List

List your dedicated endpoints.

```bash Shell theme={null}
tg endpoints list
```

### Parameters

| Flag                                   | Description           |
| -------------------------------------- | --------------------- |
| `--usage-type [on-demand \| reserved]` | Filter by usage type. |
| `--after [string]`                     | Pagination cursor.    |

<Note>
  `--mine` and `--type` are accepted for backward compatibility but no longer have any effect. `tg endpoints list` already returns the dedicated endpoints on your account.
</Note>

## Availability zones

List the availability zones you can deploy endpoints into.

```bash Shell theme={null}
tg endpoints availability-zones
```

## Adapters

Manage [LoRA adapters](/docs/dedicated-endpoints/lora-adapter) bound to a dedicated endpoint. Once an adapter is bound, call it for inference by passing the combined `endpoint_name:adapter_model_name` identifier as the `model` parameter.

The `MODEL_ID` argument used by `add` and `remove` is the combined identifier in the form `endpoint_name:adapter_model_name`.

### List

List the adapters bound to an endpoint.

```bash Shell theme={null}
tg endpoints adapters list endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

Alias: `tg endpoints adapters ls`.

### Add

Bind an adapter to an endpoint.

```bash Shell theme={null}
tg endpoints adapters add \
  endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462 \
  my-endpoint:my-org/my-lora-adapter
```

### Remove

Remove an adapter binding from an endpoint.

```bash Shell theme={null}
tg endpoints adapters remove \
  endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462 \
  my-endpoint:my-org/my-lora-adapter
```

Aliases: `tg endpoints adapters delete`, `tg endpoints adapters rm`.
