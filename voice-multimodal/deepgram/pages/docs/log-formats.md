---
title: "Log Formats"
source: https://developers.deepgram.com/docs/log-formats.md
path: docs/log-formats
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Log Formats

Deepgram self-hosted containers support four log output formats. Use the `--log-format` CLI flag to select the format that best fits your logging infrastructure.

This flag applies to all self-hosted container images: API, Engine, License Proxy, and Billing.

## Available Formats

| Format  | Flag                   | Description                                                                                                |
| ------- | ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| Full    | `--log-format=full`    | Default. Verbose output with all fields, timestamps, and span context. Best for development and debugging. |
| Compact | `--log-format=compact` | Abbreviated output. Omits redundant span context for more concise logs.                                    |
| Pretty  | `--log-format=pretty`  | Human-readable output with color highlighting. Best for local development.                                 |
| Json    | `--log-format=json`    | Structured JSON output. Best for log aggregation systems (i.e. Datadog, Splunk, ELK).                      |

## Configuration

The log format is set as a CLI flag appended to the container's `command`. It is not configured via TOML.

### Docker Compose

```yaml
services:
  api:
    image: quay.io/deepgram/self-hosted-api:release-260319
    command: -v serve /api.toml --log-format=json
    # ...

  engine:
    image: quay.io/deepgram/self-hosted-engine:release-260319
    command: -v serve /engine.toml --log-format=json
    # ...

  license-proxy:
    image: quay.io/deepgram/self-hosted-license-proxy:release-260319
    command: -v serve /license-proxy.toml --log-format=json
    # ...
```

### Kubernetes (Helm)

In a Helm values override, set the command args for each container:

```yaml
api:
  additionalArgs: ["--log-format=json"]

engine:
  additionalArgs: ["--log-format=json"]

licenseProxy:
  additionalArgs: ["--log-format=json"]

billing:
  additionalArgs: ["--log-format=json"]
```

The API container also accepts a legacy `--json` flag for JSON output. If both `--json` and `--log-format` are specified, `--log-format` takes precedence.

## Example Output

### Full (default)

```
2026-03-19T14:30:00.123456Z  INFO serve: deepgram::server: Starting API server host=0.0.0.0 port=8080
2026-03-19T14:30:00.234567Z  INFO serve: deepgram::license: License validated successfully expires=2027-09-19T00:00:00Z
2026-03-19T14:30:01.345678Z  INFO serve: deepgram::engine: Engine connection established endpoint=engine:9991
```

### Compact

```
2026-03-19T14:30:00.123456Z  INFO serve: Starting API server host=0.0.0.0 port=8080
2026-03-19T14:30:00.234567Z  INFO serve: License validated expires=2027-09-19T00:00:00Z
2026-03-19T14:30:01.345678Z  INFO serve: Engine connected endpoint=engine:9991
```

### Pretty

```
  2026-03-19T14:30:00.123456Z  INFO serve: Starting API server
    host: 0.0.0.0
    port: 8080

  2026-03-19T14:30:00.234567Z  INFO serve: License validated successfully
    expires: 2027-09-19T00:00:00Z
```

### Json

```json
{"timestamp":"2026-03-19T14:30:00.123456Z","level":"INFO","target":"deepgram::server","message":"Starting API server","host":"0.0.0.0","port":8080}
{"timestamp":"2026-03-19T14:30:00.234567Z","level":"INFO","target":"deepgram::license","message":"License validated successfully","expires":"2027-09-19T00:00:00Z"}
{"timestamp":"2026-03-19T14:30:01.345678Z","level":"INFO","target":"deepgram::engine","message":"Engine connection established","endpoint":"engine:9991"}
```

## Availability

The `--log-format` flag is available in release `260319` and later on all self-hosted container images.

---

## What's Next

* [Metrics Guide](/docs/metrics-guide) - Monitor your deployment with Prometheus metrics
* [Status Endpoint](/docs/self-hosted-status-endpoint) - Check node health and readiness
