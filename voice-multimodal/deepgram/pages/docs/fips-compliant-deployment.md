---
title: "FIPS-Compliant Deployment"
source: https://developers.deepgram.com/docs/fips-compliant-deployment.md
path: docs/fips-compliant-deployment
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# FIPS-Compliant Deployment

Deepgram provides FIPS 140-3 self-hosted images for the API, Engine, License Proxy, and Billing containers, plus models encrypted using FIPS-approved algorithms.

## Container Images

Use the FIPS variants of the `release-260728` images (the `-fips` tag suffix):

| Component         | Image                                                            |
| ----------------- | ---------------------------------------------------------------- |
| **API**           | `quay.io/deepgram/self-hosted-api:release-260728-fips`           |
| **Engine**        | `quay.io/deepgram/self-hosted-engine:release-260728-fips`        |
| **License Proxy** | `quay.io/deepgram/self-hosted-license-proxy:release-260728-fips` |

See the [release changelog](/changelog/2026/7/28) for the equivalent component versions.

## Configuration

### Enable FIPS Mode

FIPS mode is set per service. Add the following block to the configuration file of **every** service you deploy:

```toml
[fips]
mode = "enabled"
```

Set it in each of:

* `api.toml` (API)
* `engine.toml` (Engine)
* `license-proxy.toml` (License Proxy)
* `billing.toml` (Billing — airgapped deployments only)

The FIPS images do not enable FIPS mode on their own. A service whose configuration omits this block runs OpenSSL in standard (non-FIPS) mode, even on a FIPS image. Confirm each service logs `openssl_fips_enabled=true` at startup.

### Engine Environment Variables

As with any self-hosted Engine deployment, the Engine container requires these NVIDIA environment variables:

```
NVIDIA_VISIBLE_DEVICES=all
NVIDIA_DRIVER_CAPABILITIES=compute,utility
```

These are set in your container orchestration configuration. See the reference configs for [Docker](https://github.com/deepgram/self-hosted-resources/blob/85b1eda4f4f2be3eac18848a8f2dd0d67633563d/docker/docker-compose.license-proxy.yml#L8-L12) and [Kubernetes](https://github.com/deepgram/self-hosted-resources/blob/85b1eda4f4f2be3eac18848a8f2dd0d67633563d/charts/deepgram-self-hosted/templates/engine/engine.deployment.yaml#L145-L151).

### TLS Certificate

Customers must provide their own full-chain PKI certificate for the API's HTTPS endpoint.

## Models

Your Deepgram account team provides download links for the FIPS-encrypted models compatible with these images. FIPS models use the `.dgv2` encrypted file format.

`.dgv2` and `.dg` models are not interchangeable. The FIPS Engine loads only `.dgv2` models — it will not load `.dg` models.

### Model Support

**Flux STT is not currently supported on FIPS images.** [Flux STT](/docs/flux-self-hosted) can only be run on standard (non-FIPS) images.

**Flux TTS runs on FIPS images.** [Flux TTS](/docs/deploy-flux-tts) is subject to the [MP3 and FLAC output](#mp3-and-flac-output) issue below: batch `/v2/speak` requests return MP3 unless they set `encoding`, so set it explicitly. Streaming `/v2/speak` output is unaffected.

## Caveats

### MP3 and FLAC Output

MP3 and FLAC output are not available on FIPS images. This is a known issue. A text-to-speech request that asks for either format returns `HTTP 200` with an empty body rather than an error.

`/v1/speak` and batch `/v2/speak` both return MP3 when the request does not set `encoding`, so set `encoding` explicitly on FIPS images. Streaming `/v2/speak` returns `linear16` and is unaffected.

Format support on FIPS images:

* `linear16` and `opus` are unaffected, and are the recommended formats.
* `mp3` and `flac` are unavailable.
* Verify any other format against your own deployment before relying on it.

This limitation applies to audio output only. Speech-to-text requests that submit MP3 or FLAC *input* are unaffected.

### TLS 1.3 Only

The FIPS API image enforces TLS 1.3 exclusively. It rejects TLS 1.2 connections outright and rejects non-FIPS cipher suites (such as ChaCha20). Any TLS-1.2-only client, SDK, or proxy in front of the API will fail to connect.

Ensure your entire client stack negotiates TLS 1.3 before cutover.

The `[fips]` configuration flag does not control TLS behavior. TLS 1.3 enforcement is baked into the FIPS image itself, so disabling the `[fips]` flag will not restore TLS 1.2 support.

## Airgapped (Offline) Deployment

The deployment above reaches Deepgram's hosted license server through the License Proxy, which requires outbound internet access. If you require running FIPS-compliant self-hosted Deepgram deployments in environments without public internet connectivity, contact your Deepgram account team to inquire about airgapped access, which uses the FIPS Billing image (`quay.io/deepgram/self-hosted-billing:release-260728-fips`) to run license validation offline.

---

## What's Next

* [Deploy STT Services](/docs/deploy-stt-services) - Standard deployment guide
* [Status Endpoint](/docs/self-hosted-status-endpoint) - Monitor node health and readiness
