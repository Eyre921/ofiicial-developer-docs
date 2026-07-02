---
title: "Certificate Status"
source: https://developers.deepgram.com/docs/certificates-endpoint.md
path: docs/certificates-endpoint
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Certificate Status

The certificates endpoint returns certificate lifecycle information for your Deepgram self-hosted deployment. Use it to track certificate creation, end-of-support, and end-of-life dates.

This endpoint is available on all self-hosted container images:

| Image         | Endpoint           | Default Port                                        |
| ------------- | ------------------ | --------------------------------------------------- |
| API           | `/v1/certificates` | 8080                                                |
| Engine        | `/v1/certificates` | 9991 (metrics port)                                 |
| License Proxy | `/v1/certificates` | 8089                                                |
| Billing       | `/v1/certificates` | 8080 (requires `certificates_port` in billing.toml) |

## Response Format

```json
{
  "beginning_of_support": "2025-11-13 15:25:28.0 +00:00:00",
  "end_of_support": "2027-05-15 03:25:28.0 +00:00:00",
  "end_of_life": "2028-11-12 15:25:58.0 +00:00:00",
  "instance_id": "235c0e16-c791-45b8-bf41-757ca11ac2b9"
}
```

| Field                  | Description                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `beginning_of_support` | UTC timestamp when the certificate was created.                                                                            |
| `end_of_support`       | 18 months after `beginning_of_support`. After this date, Deepgram no longer provides support for this certificate version. |
| `end_of_life`          | 36 months after `beginning_of_support`. The certificate expires on this date.                                              |
| `instance_id`          | Unique identifier for this deployment instance.                                                                            |

## Making a Request

```shell cURL (API)
curl http://localhost:8080/v1/certificates
```

```shell cURL (Engine)
curl http://localhost:9991/v1/certificates
```

```python Python
import requests

response = requests.get("http://localhost:8080/v1/certificates")
cert = response.json()
print(f"Certificate created: {cert['beginning_of_support']}")
print(f"End of support: {cert['end_of_support']}")
print(f"End of life: {cert['end_of_life']}")
print(f"Instance ID: {cert['instance_id']}")
```

```javascript JavaScript
const response = await fetch('http://localhost:8080/v1/certificates');
const cert = await response.json();
console.log(`Certificate created: ${cert.beginning_of_support}`);
console.log(`End of support: ${cert.end_of_support}`);
console.log(`End of life: ${cert.end_of_life}`);
console.log(`Instance ID: ${cert.instance_id}`);
```

## Certificate Lifecycle

Deepgram self-hosted certificates follow a fixed lifecycle:

1. **Active** (0–18 months after creation) — Full support. Software updates and security patches are available.
2. **End of Support** (18–36 months after creation) — The deployment continues to function, but Deepgram no longer provides support or updates for this certificate version. Plan your renewal.
3. **End of Life** (36 months after creation) — The certificate expires. The deployment will no longer validate against the Deepgram license server.

## Startup Log Message

All self-hosted containers log certificate information on startup. You can inspect this without querying an endpoint:

```
INFO impeller: Certificates information. beginning_of_support=2025-11-13 15:26:33.0 +00:00:00 end_of_support=2027-05-15 3:26:33.0 +00:00:00 end_of_life=2028-11-12 15:27:03.0 +00:00:00 instance_id=c32fb5ff-538c-4b93-b854-8c038a22c302
```

This message appears in the logs for API, Engine, License Proxy, and Billing containers. If a certificate has expired, the container will log an error and refuse to start.

## Monitoring Certificate Expiry

Check the `eol` field periodically to ensure your deployment renews before certificate expiration. A recommended approach:

```python Python
from datetime import datetime, timezone
import requests

response = requests.get("http://localhost:8080/v1/certificates")
cert = response.json()

eol = datetime.fromisoformat(cert["end_of_life"])
days_remaining = (eol - datetime.now(timezone.utc)).days

if days_remaining < 90:
    print(f"WARNING: Certificate expires in {days_remaining} days")
elif days_remaining < 180:
    print(f"Certificate expires in {days_remaining} days — plan renewal")
else:
    print(f"Certificate valid for {days_remaining} more days")
```

## Billing Container Configuration

The Billing container requires `certificates_port` in `billing.toml` to serve the certificates endpoint. Without this setting, the certificates server binds to an ephemeral port and is not reachable.

```toml
[server]
  host = "0.0.0.0"
  port = 8443
  base_url = "/"
  certificates_port = 8080
```

Expose this port in your Docker Compose or Kubernetes configuration to query `/v1/certificates` on the Billing container.

## Availability

The `/v1/certificates` endpoint is available in release `260319` and later on all self-hosted container images.

***

## What's Next

* [Status Endpoint](/docs/self-hosted-status-endpoint) - Monitor node health and readiness
* [System Maintenance](/docs/maintaining) - Keeping your deployment healthy
