---
title: "Validate a Deepgram SageMaker Endpoint"
source: https://developers.deepgram.com/docs/test-amazon-sagemaker-endpoint.md
path: docs/test-amazon-sagemaker-endpoint
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Validate a Deepgram SageMaker Endpoint

Once your SageMaker endpoint reaches `InService`, run a client script against it to confirm that inference works end to end. Deepgram publishes a ready-made set of test clients in the [dg-sagemaker](https://github.com/deepgram-devs/dg-sagemaker) repository. Each client wraps the SageMaker bidirectional streaming or batch (HTTP) invocation API with the payload shape that the target Deepgram model expects, so you can focus on verifying the endpoint rather than writing transport code.

The repository is organized by product and by language. Pick the script that matches the model you deployed (Flux, Nova-3, or Aura) and the language you want to work in (Python, Node.js, or Java). The scripts are load-testing clients first and functional smoke tests second — running any of them with a single connection is the fastest way to prove that your endpoint accepts traffic and returns results.

The scripts evolve independently. Flags, defaults, and input formats differ between products and between languages. Always read the `README.md` inside the subdirectory you intend to run before invoking a script.

## High-level process

#### Install the required tooling

Install the language runtime and package manager for the script you plan to run. See [Required tooling](#required-tooling).

#### Configure AWS credentials and region

Configure AWS credentials locally and ensure your shell targets the region where the SageMaker endpoint is deployed. See [AWS credentials and region](#aws-credentials-and-region).

#### Clone the dg-sagemaker repository

```bash
git clone https://github.com/deepgram-devs/dg-sagemaker.git
cd dg-sagemaker
```

#### Choose the script that matches your product

Identify the subdirectory for your Deepgram product and language. See [Pick the right script](#pick-the-right-script).

#### Run the script against your endpoint

Invoke the script with your endpoint name, AWS region, and any product-specific inputs (for example, a WAV file for speech-to-text or a text file for text-to-speech).

## Prerequisites

* A Deepgram SageMaker endpoint in `InService` status. See [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker).
* AWS IAM permissions to invoke the endpoint and, optionally, to list endpoints in the target region:
  * `sagemaker:InvokeEndpoint`
  * `sagemaker:InvokeEndpointWithResponseStream`
  * `sagemaker:InvokeEndpointWithBidirectionalStream`
  * `sagemaker:ListEndpoints` and `sagemaker:DescribeEndpoint` (used by `list-endpoints` helpers)
* `git` available on your local machine.

## Pick the right script

Each Deepgram product has a dedicated script because the SageMaker payload shape and the protocol on top of it differ per model. Run the script that matches the model you deployed.

| Product                   | Language | Path in dg-sagemaker                          | Script                                                          |
| ------------------------- | -------- | --------------------------------------------- | --------------------------------------------------------------- |
| Flux (conversational STT) | Python   | `python-flux/`                                | `flux_stress.py file \| microphone \| list-endpoints`           |
| Nova-3 (streaming STT)    | Python   | `python-stt/`                                 | `stt_microphone_stress.py`, `stt_wav_stress.py stream \| batch` |
| Nova-3 (streaming STT)    | Node.js  | `js-stt/`                                     | `stress-stt.ts` (configured via `stt.file.ts`)                  |
| Nova-3 (streaming STT)    | Java     | `java/stt/aws-sdk/`, `java/stt/deepgram-sdk/` | Gradle projects; see each project's README                      |
| Aura (text-to-speech)     | Python   | `python-tts/`                                 | `tts_stress.py`                                                 |

Invocation flags, defaults, and required inputs vary per script. Consult the `README.md` in each subdirectory for the full command reference. For example, the Flux client uses the `/v2/listen` endpoint and a turn-based protocol, while the Nova-3 client uses `/v1/listen` with channel-based alternatives.

## Required tooling

Install only the tools you need for the script you plan to run.

#### Python

* Python 3.12+ (Python 3.14+ for `python-stt`)
* [uv](https://docs.astral.sh/uv/) package manager
* PortAudio for microphone or audio playback (required for `python-tts` and for microphone modes of `python-stt`/`python-flux`):
  * macOS: `brew install portaudio`
  * Linux: `sudo apt-get install portaudio19-dev`

Install dependencies inside the script's subdirectory:

```bash
cd python-stt   # or python-flux, python-tts
uv sync
```

#### Node.js

* Node.js (current LTS)
* `npx` (bundled with Node.js)

Dependencies are resolved on first invocation via `npx tsx`.

#### Java

* JDK 17 or later
* Gradle (the projects ship with the Gradle wrapper, `./gradlew`)

Each Java project is a standalone Gradle build under `java/stt/aws-sdk/` or `java/stt/deepgram-sdk/`. Refer to the per-project README for build and run commands.

## AWS credentials and region

The scripts use the standard AWS credential chain — environment variables, shared credentials file, or an attached IAM role. Configure credentials with whichever mechanism you prefer:

```bash
aws configure
```

Or export them for the current shell:

```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...   # if using temporary credentials
```

Verify the identity the scripts will use:

```bash
aws sts get-caller-identity
```

Most scripts accept a `--region` flag and default to `us-east-1` (or `us-east-2` for `python-tts`). **Make sure the region you pass matches the region where your SageMaker endpoint was deployed** — an endpoint name is only resolvable within the region it was created in.

If you are not sure which endpoints exist in a region, use the Flux client's helper subcommand to list them:

```bash
cd python-flux
uv run flux_stress.py list-endpoints --region us-east-1
```

## Run the script

Once tooling and credentials are in place, invoke the script for your product. The example below shows the simplest single-connection invocation for the Flux Python client. The Nova-3 and Aura clients follow a similar pattern but with different flags, defaults, and input formats — refer to the [dg-sagemaker](https://github.com/deepgram-devs/dg-sagemaker) repository and each subdirectory's `README.md` for the full command reference.

```bash
cd python-flux

# Stream a WAV file at real-time pace
uv run flux_stress.py file your-endpoint-name \
  --file audio.wav \
  --region us-east-1

# Or stream live microphone audio
uv run flux_stress.py microphone your-endpoint-name --region us-east-1
```

For best compatibility, use a 16-bit PCM WAV file. Convert other formats with:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 -sample_fmt s16 audio.wav
```

## Verify the result

A successful test produces:

* **Speech-to-text (Flux, Nova-3):** transcript payloads streamed back to the client. Final transcripts and interim results (or Flux `TurnInfo` events) are logged to the console.
* **Text-to-speech (Aura):** audible speech playback from the selected connection and a steady stream of synthesized audio chunks logged to the console.

If the script hangs, errors on connection, or fails to authenticate, see [Troubleshooting](#troubleshooting).

## Troubleshooting

* **`ResourceNotFound` or endpoint lookup failures** — confirm the endpoint name and that your shell is targeting the correct region. Run `aws sagemaker describe-endpoint --endpoint-name your-endpoint-name --region your-region` to verify.
* **`AccessDeniedException`** — confirm your IAM identity has `sagemaker:InvokeEndpoint` (and the bidirectional/streaming variants) for the endpoint's ARN.
* **Endpoint not yet in service** — wait until the endpoint status is `InService`. Deployment typically takes several minutes.
* **Audio format errors** — try changing the input audio format to 16-bit PCM WAV, instead of other compressed formats. Use the `ffmpeg` command as shown above.
* **Server-side errors** — check the Amazon CloudWatch Logs for the SageMaker endpoint to diagnose container-level issues.
