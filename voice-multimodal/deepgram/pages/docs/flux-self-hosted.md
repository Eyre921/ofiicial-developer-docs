---
title: "Using the Flux Model"
source: https://developers.deepgram.com/docs/flux-self-hosted.md
path: docs/flux-self-hosted
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Using the Flux Model

## Requirements

Please familiarize yourself with these general requirements before attempting to deploy Flux to your self-hosted Deepgram instances.

* Flux requires a newer NVIDIA GPU (Ampere generation or later). Older GPUs such as the NVIDIA T4 are not supported.
* The Flux model must be hosted on a separate instance from other Deepgram speech-to-text (STT) and text-to-speech (TTS) models.
* Your Deepgram API and Engine TOML files must explicitly enable Flux
* Flux doesn't require and is not compatible with any other models (e.g. diarizer, entity detector)
* You must use Deepgram container images from October 2025 or later (`release-251015`)
* The Flux model file must be added to your `engine` models directory

Flux is not supported on the NVIDIA T4 or similar older GPUs due to their compute capabilities. Run Flux on a newer NVIDIA GPU (Ampere generation or later) such as the NVIDIA A10, L4, L40S, A100, or H100.

Unlike the Nova family of models, Flux **cannot co-exist with other STT models on the same Engine node**. This means you must provision a dedicated server specifically for handling Flux requests. For optimal streaming performance, we also recommend provisioning a **separate API node** to route Flux requests to your Flux-configured Engine node.

## Flux GPU Resource Allocation

**Flux must run in isolation from other Deepgram models.**
Flux requires a certain amount of GPU memory per stream, and this memory is allocated on Engine startup.
By default, Flux allocates all GPU memory for Flux streams.

Do not enable Flux in the Engine configuration file unless you intend to use it.

An Engine running Flux is not designed to serve any other Deepgram traffic, including other STT models (such as Nova-3), TTS,
or supplementary models. Attempting to do so will result in resource exhaustion and request failures due to lack of GPU memory.

For example, if you enable Flux, and then submit a Nova-3 request on the same GPU, you will encounter out-of-memory errors such as:

```text
...called `Result::unwrap()` on an `Err` value: Internal torch error: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of
21.95 GiB of which 13.00 MiB is free. Process 6456 has 1006.00 MiB memory in use. Process 6583 has 20.94 GiB memory in use. Of the allocated memory
788.04 MiB is allocated by PyTorch, and 13.96 MiB is reserved by PyTorch but unallocated...
```

Provision separate infrastructure for Flux, and ensure no other Deepgram models are present on the same Engine.

## Selecting the Flux Model

Deepgram offers two Flux models for self-hosted deployments:

* **`flux-general-en`** — English-only conversational STT
* **`flux-general-multi`** — Multilingual conversational STT with code-switching support (English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch)

You must specify which model to load using the `model_name` field in your Engine configuration. If `model_name` is not set, Engine defaults to `flux-general-en`.

```toml Deepgram Engine Configuration
[flux]
enabled = true
max_streams = 0 # Placeholder; required for production. Set explicitly based on GPU type.
model_name = "flux-general-multi" # or "flux-general-en"
```

Engine can only load one Flux model at a time. If you need both English and Multilingual, provision separate Engine instances for each.

## Configuring Max Streams

Flux automatically derives a maximum number of concurrent streams based on available GPU memory. However, for optimal and predictable performance, you must explicitly configure the `max_streams` value in the `[flux]` section of your Engine configuration file (shown in [Selecting the Flux Model](#selecting-the-flux-model)).

The appropriate value depends on your GPU type and should be set according to Deepgram's benchmarking recommendations. Explicitly configuring this value ensures that concurrency limits result in consistent latency under load.

### Recommended Values by GPU Type

Contact your Deepgram account representative for the recommended `max_streams` values for the GPUs you plan to use.

### Indicators of Excessive Concurrency

If `max_streams` is set too high (or left at the auto-calculated default), you may observe the following behavior under load:

* Voice agents stop responding or experience long delays
* Calls are dropped after sustained concurrent usage
* Errors appear in the API container logs, such as:
  `audio_window_end increased by more than 3 frames`

If you encounter these behaviors, reduce the `max_streams` value and repeat load testing until throughput and latency stabilize.

### Monitoring Stream Usage

You can monitor Flux stream usage through the Engine metrics endpoint. The following metrics are available:

* `flux_max_streams`: The configured maximum number of Flux streams
* `flux_used_streams`: The current number of active Flux streams
* `flux_fraction_streams`: The fraction of max streams currently in use

See the [Metrics Guide](/docs/metrics-guide) for more information on accessing Engine metrics.

## Flux Model Files

Each Flux variant has its own model file:

* **Flux English**: `flux-general-en.*.dg`
* **Flux Multilingual**: `flux-general-multi.*.dg`

You only need the model file for the variant you intend to deploy. If both models are present, only the model specified in `model_name` will be loaded. Contact your Deepgram account representative or Deepgram Support to obtain the model file.

## Enable Flux in Deepgram Self-Hosted Deployment

Flux requires a couple of configuration changes in your self-hosted Deepgram deployment.

In your Deepgram Engine configuration, enable Flux using the `[flux]` section shown in [Selecting the Flux Model](#selecting-the-flux-model). Do not enable `[flux]` unless this server is dedicated exclusively to Flux.

In your Deepgram API configuration, make sure that the `/v2/listen` endpoint is enabled. This endpoint is new for Flux.
Earlier Deepgram Speech-to-Text (STT) models (including Nova-3 and Nova-2) are served via the `/v1/listen` endpoint.

```toml Deepgram API Configuration
[features]
listen_v2 = true
```

## Deepgram Self-Hosted Logs

The following log entries may be useful in identifying Flux behaviors.

### Ensure Flux Model is Loaded

To ensure that the Flux model is being loaded by your Deepgram self-hosted instance, you can check the `engine` container logs.

Use the appropriate tool to find your `engine` container, and obtain the logs for that container.

For example:

```
# 🐳 Docker: Find container ID or name, and get logs
docker ps
docker logs <containerIdOrName>

# ⛴️ Kubernetes: Find the Engine Pod and get logs for it
kubectl --namespace dg-self-hosted get pod
kubectl --namespace dg-self-hosted logs engine-12345
```

During the startup of the `engine` container, to indicate a successful model load, look for the log entry similar to the following.

```text
INFO impeller::charmer::output_processor: flux-subprocess/21 sttreaming.inference_process [<string>:62]: Model loaded successfully, ready to accept requests.
INFO impeller::flux::prewarm: Finished prewarming Flux model
INFO impeller: Starting instance. instance=55c02da4-e79f-4bf4-bf73-cd9dbfb21a18
```

## Potential Issues

### Flux Present but Disabled

If you have the Flux model file in your engine `models` directory, but the feature is disabled in the `engine.toml` configuration file,
you will still see this message appear in your `engine` logs, provided you're running a container image that supports Flux.

```text
INFO load_model{path=/models/flux-general-en.caf79279.dg}: impeller::model_suppliers::autoload: Inserting model key=AsrKey { name: "flux-general-en", version: "2025-12-02.74258", languages: List([Language("en"), Language("en-au"), Language("en-ca"), Language("en-gb"), Language("en-in"), Language("en-nz"), Language("en-us")]), aliases: {}, tags: [], uuid: caf79279-3e00-460b-9d2f-ce7d2764a79a, formatted: false, mode: TurnTaking, architecture: Some(Flux) }
```

### Flux Model File Missing

If you see the errors below, that indicates the Flux model file is missing from your `models` directory.
Please ask your Deepgram account representative or support team for assistance in obtaining the Flux model file.

```text maxLines=6 highlight={1,3,5}
ERROR impeller: Engine was configured to run the Flux model, but we failed to load it. err=Failure(Can't find flux-general-en model)
thread 'main-rt-5' panicked at /build/src/lib.rs:1119:17:
Error loading Flux model: failure: Can't find flux-general-en model
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Error: task 20 panicked with message "Error loading Flux model: failure: Can't find flux-general-en model"
terminate called after throwing an instance of 'c10::Error'
  what():  CUDA error: driver shutting down
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Device-side assertions were explicitly omitted for this error check; the error probably arose while initializing the DSA handlers.
Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAException.cpp:43 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0x70242061e170 in /libtorch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0xfa (0x7024205c16dc in /libtorch/lib/libc10.so)
frame #2: c10::cuda::c10_cuda_check_implementation(int, char const*, char const*, int, bool) + 0x3cc (0x70249564208c in /libtorch/lib/libc10_cuda.so)
frame #3: c10::cuda::CUDAKernelLaunchRegistry::CUDAKernelLaunchRegistry() + 0xae (0x702495640dbe in /libtorch/lib/libc10_cuda.so)
frame #4: c10::cuda::CUDAKernelLaunchRegistry::get_singleton_ref() + 0x4c (0x702495640f4c in /libtorch/lib/libc10_cuda.so)
frame #5: c10::cuda::c10_cuda_check_implementation(int, char const*, char const*, int, bool) + 0x75 (0x702495641d35 in /libtorch/lib/libc10_cuda.so)
frame #6: <unknown function> + 0x753c6 (0x7024956513c6 in /libtorch/lib/libc10_cuda.so)
frame #7: <unknown function> + 0x7591c (0x70249565191c in /libtorch/lib/libc10_cuda.so)
frame #8: c10::cuda::getStreamFromPool(bool, signed char) + 0x13 (0x702495652c43 in /libtorch/lib/libc10_cuda.so)
frame #9: <unknown function> + 0x3573dab (0x576927e72dab in /bin/impeller)
frame #10: <unknown function> + 0x1939036 (0x576926238036 in /bin/impeller)
frame #11: <unknown function> + 0x1961017 (0x576926260017 in /bin/impeller)
frame #12: <unknown function> + 0x3297caf (0x576927b96caf in /bin/impeller)
frame #13: <unknown function> + 0x8a19a (0x70249c2d519a in /usr/lib64/libc.so.6)
frame #14: clone + 0x44 (0x70249c359534 in /usr/lib64/libc.so.6)
```

### Flux Not Enabled in Engine

If the Flux model is failing to load, you may see this warning from the `engine` (aka. `impeller`) logs.
This suggests that the `Engine.toml` configuration has not had Flux enabled, but the Flux model is in your `models` directory.

```text
INFO load_model{path=/models/flux-general-en.caf79279.dg}: impeller::model_suppliers::autoload: new
WARN load_model{path=/models/flux-general-en.caf79279.dg}: impeller::model_suppliers::autoload: Failed to load model err=Manifest(TomlError { message: "unknown variant `turn-taking`, expected one of `all`, `batch`, `streaming`", raw: Some("architecture = \"flux\"\nformatted = false\ngeneration = \"alpha\"\nlanguages = [\"en\", \"en-AU\", \"en-CA\", \"en-GB\", \"en-IN\", \"en-NZ\", \"en-US\"]\nmode = \"turn-taking\"\nmultilingual = false\nname = \"flux-general-en\"\nuuid = \"caf79279-3e00-460b-9d2f-ce7d2764a79a\"\nversion = \"2025-12-02.74258\"\n"), keys: ["mode"], span: Some(141..154) })
```

### Older Deepgram Container Images

If you see the following error in your logs, you may be running an old Deepgram `engine` container image.
Please make sure that you are using an `engine` container image that was released with Flux (`release-251015`), or later.

```text
Error: TOML parse error at line 57, column 1
   |
57 | [flux]
   | ^^^^^^
missing field `socket_path`
```

### Flux model running on CPU

Under certain circumstances, you may see a log entry in the Engine logs indicating "*Running model on device cpu*." This is particularly common on Google Kubernetes Engine (GKE). In these scenarios, the GPU is not being utilized for Flux inference, which will cause performance issues such as:

* Out of Memory (OOM) errors
* High request latency, including the API pod aggressively aborting connections due to request response times getting too long

If you see this message in your Engine logs, it indicates that the process in charge of Flux inference is not able to utilize the NVIDIA GPU, likely due to an issue accessing the drivers. This may happen even if the parent Engine process reports that it's detecting the GPU correctly.

We recommend enabling the `health.gpu_required` configuration flag on your Engine containers to ensure that any GPU detection issues are fatal, instead of allowing the container to proceed in a degraded state. This configuration option is available as `engine.health.gpuRequired` in our Helm chart.

To address the root cause, ensure that a valid NVIDIA driver is installed, and use tools like `nvtop` or `nvidia-smi` to monitor GPU utilization. You can also call `ldconfig` in a `postStart` hook as demonstrated in [this GitHub thread](https://github.com/deepgram/self-hosted-resources/pull/113), which may resolve the driver issue.

## Access Flux Endpoint

The Flux model is accessed by the WebSocket protocol only, using the `ws://<ipOrHostname>/v2/listen` URL.
This URL path is exposed by the Deepgram API server container, similar to the other Deepgram APIs.

Once you've verified that Flux is installed and loaded by the Deepgram self-hosted services, please
follow the [developer documentation](/docs/flux/quickstart).
