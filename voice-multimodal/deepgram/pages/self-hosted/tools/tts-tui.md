---
title: "Validate Deepgram Self-Hosted TTS"
source: https://developers.deepgram.com/self-hosted/tools/tts-tui.md
path: self-hosted/tools/tts-tui
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Validate Deepgram Self-Hosted TTS

`tts-tui` is an open-source terminal application written in Rust for testing and validating Deepgram text-to-speech on self-hosted deployments. It supports Deepgram-compatible HTTP endpoints and Amazon SageMaker, with interactive voice selection, multi-format audio output, and local audio caching.

## Features

* **Validate self-hosted TTS** — confirm that Aura-2 models produce correct audio on your own infrastructure before going to production.
* **Test output formats** — switch between MP3, Linear16 (WAV), FLAC, and other encodings with configurable sample rates.
* **Multi-language support** — synthesize speech in any Deepgram-supported language and save utterances for comparison.
* **Audio caching** — repeated playback is served from disk instantly, so you can iterate without redundant API calls.
* **Dual provider support** — test both Deepgram-compatible HTTP endpoints and Amazon SageMaker `InvokeEndpoint` deployments from the same tool.

## Prerequisites

* [Rust Toolchain](https://rustup.rs) (only required when building from source)
* Deepgram self-hosted TTS deployment

## Installation

### Run Pre-compiled Binary

1. Download the latest release from [GitHub Releases](https://github.com/deepgram-devs/deepgram-demos-rust/releases/latest).
2. Extract the ZIP file.
3. Run the `tts-tui` binary.

### Build from Source

```bash
git clone https://github.com/deepgram-devs/deepgram-demos-rust.git
cd deepgram-demos-rust/tts-tui
cargo install --path .
```

Once installed, the `tts-tui` binary is available from anywhere on your system.

## Configure for self-hosted

Use the `--endpoint` flag to point `tts-tui` at your Deepgram-compatible HTTP endpoint:

```bash
tts-tui --provider deepgram --endpoint https://your-selfhosted-deepgram.example.com/v1/speak
```

If the endpoint requires an API key, supply it through the `DEEPGRAM_API_KEY` environment variable or press `k` inside the running application.

## Configure for Amazon SageMaker

Use self-hosted Deepgram TTS on Amazon SageMaker through the AWS SageMaker Runtime `InvokeEndpoint` API:

```bash
tts-tui \
  --provider sagemaker \
  --sagemaker-endpoint-name your-sagemaker-endpoint \
  --aws-region us-east-2
```

The same settings can be supplied with environment variables:

```bash
export TTS_TUI_PROVIDER=sagemaker
export SAGEMAKER_ENDPOINT_NAME=your-sagemaker-endpoint
export AWS_REGION=us-east-2
tts-tui
```

## Learn more

* [GitHub repository](https://github.com/deepgram-devs/deepgram-demos-rust/tree/main/tts-tui)
* [Latest release](https://github.com/deepgram-devs/deepgram-demos-rust/releases/latest)
