---
title: "Deployment Tags"
source: https://docs.fireworks.ai/deployments/deployment-tags
path: deployments/deployment-tags
---

Attach customer-defined metadata to dedicated deployments

Deployment tags are key-value metadata attached to a dedicated deployment. Use them to record information such as an environment, team, or workload.

Tag changes are atomic and do not replace other deployment metadata.

## Manage tags with firectl

Upgrade firectl before using the tag commands:

```bash theme={null}
firectl upgrade
```

These commands require firectl `1.8.3` or later.

Set one tag:

```bash theme={null}
firectl deployment tag set <DEPLOYMENT_ID> --key environment --value prod
```

Set multiple tags atomically:

```bash theme={null}
firectl deployment tag set <DEPLOYMENT_ID> \
  --tag environment=prod \
  --tag team=search
```

Use either `--key` with `--value` or one or more `--tag` flags. Do not combine the two forms in one command.

List tags:

```bash theme={null}
firectl deployment tag list <DEPLOYMENT_ID>
```

Remove one or more tags atomically:

```bash theme={null}
firectl deployment tag unset <DEPLOYMENT_ID> \
  --key environment \
  --key team
```

`set` overwrites existing values for the specified keys. `unset` ignores keys that do not exist. Each command changes all supplied keys in one request or makes no changes.

<Note>
  firectl uses logical tag keys and manages the API's `custom/` prefix for you. Do not add that prefix to firectl keys. For example, `--key environment` writes the API key `custom/environment`; `--key custom/environment` writes `custom/custom/environment`.
</Note>

## Manage tags with the REST API

The REST API exposes canonical tag keys. Customer-managed keys must begin with `custom/`.

Set one or more tags:

```bash theme={null}
curl --request POST \
  --url "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/deployments/${DEPLOYMENT_ID}:setTags" \
  --header "Authorization: Bearer ${FIREWORKS_API_KEY}" \
  --header "Content-Type: application/json" \
  --data '{
    "tags": {
      "custom/environment": "prod",
      "custom/team": "search"
    }
  }'
```

Remove one or more tags:

```bash theme={null}
curl --request POST \
  --url "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/deployments/${DEPLOYMENT_ID}:deleteTags" \
  --header "Authorization: Bearer ${FIREWORKS_API_KEY}" \
  --header "Content-Type: application/json" \
  --data '{
    "keys": [
      "custom/environment",
      "custom/team"
    ]
  }'
```

The set and delete endpoints modify only the supplied keys. Other tags and Fireworks-managed annotations remain unchanged.

### Add tags when creating a deployment

Direct API clients can include canonical keys in the deployment's `annotations` map:

```json theme={null}
{
  "annotations": {
    "custom/environment": "prod",
    "custom/team": "search"
  }
}
```

<Warning>
  Bare annotation keys such as `environment`, `team`, or `project` are not customer-writable. Deployment creation requests containing them return `403 PERMISSION_DENIED`. Prefix customer-managed keys with `custom/`, or create the deployment and use `firectl deployment tag set`.
</Warning>

To change tags after creation, use `:setTags` and `:deleteTags`. Regular account callers cannot replace the complete `annotations` map through `UpdateDeployment`.

## Read tags

For regular account users, `GetDeployment` and `ListDeployments` return only customer-owned deployment tags, with the canonical `custom/` prefix:

```json theme={null}
{
  "annotations": {
    "custom/environment": "prod",
    "custom/team": "search"
  }
}
```

firectl's `deployment tag list` command shows deployment tags and removes one leading `custom/` prefix from each displayed key.

<Warning>
  Regular account responses no longer include legacy bare annotation keys. A client that previously read `annotations["environment"]`, for example, now receives no value and no error for that key. Set the canonical `custom/environment` tag and read `annotations["custom/environment"]` instead.
</Warning>

## Validation

* A deployment can have at most 64 customer tags.
* firectl logical keys can contain 1–121 ASCII characters. API keys can contain at most 128 characters, including `custom/`.
* The `custom/` API prefix is case-sensitive.
* The firectl logical key—and the portion of a REST key after `custom/`—may contain ASCII letters, digits, `-`, `_`, `.`, and `/`. It must start and end with an ASCII letter or digit.
* Values must be non-empty valid UTF-8 with at most 128 Unicode code points.
* Values cannot have leading or trailing whitespace or contain control characters.

## Deployment list filtering

Tag filtering in `ListDeployments` and `firectl deployment list` is not currently supported.
