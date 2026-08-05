---
title: "Metrics Guide"
source: https://developers.deepgram.com/docs/metrics-guide.md
path: docs/metrics-guide
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Metrics Guide

Each section also contains details on implementing image-specific liveness and readiness probes. These should be implemented when using a container orchestration tool that supports health probes. For example, the [`deepgram-self-hosted` Helm chart](https://github.com/deepgram/self-hosted-resources/tree/main/charts/deepgram-self-hosted) includes these checks by default.

## Deepgram API

For self-hosted deployments, the Deepgram API container images expose an endpoint `/v1/status`, on port 8080 by default. Querying this endpoint will yield three pieces of information:

1. If a successful response is received, the API is alive and listening to messages
2. The response body gives a backward-looking indication of `system_health`
3. The response body indicates how many requests this API instance is processing

### Liveness Probe

Use a TCP check on the open port (port 8080 by default).

### Readiness Probe

Query the status of the `/v1/status/engine`endpoint and check whether it is in a `"Connected"` state with at least one Engine container.

```bash cURL
curl --silent http://localhost:PORT/v1/status/engine | grep --quiet -e '^{\"engine_connection_status\"\:\"Connected\".*}$'
```

Make sure to replace the `PORT` placeholder with the port your container is listening on (port 8080 by default).

### Model Metadata

Make a GET request to list all models the Engine has loaded, along with their metadata. For broader information, see the [Model Metadata endpoint documentation](/guides/fundamentals/model-metadata). When pointed at a self-hosted deployment, this endpoint is helpful to confirm that models present in your models directory are being loaded by the container as expected.

```bash cURL
curl --location 'http://localhost:8080/v1/models'
```

## Deepgram Engine

The Deepgram Engine container image publishes an extensive set of system metrics. These metrics are configured on a separate endpoint and port than the main service.

### Docker/Podman

Choose a host port `HOST_PORT` where external queries can be made, and choose a container port `CONTAINER_PORT` where Engine can internally publish its metrics. These can be the same port number, since they are binding to different networks (the host network versus the container network)

<h2> Port Collision </h2>
"Port collision" can occur when you try to bind to the same port from two different services. Since we are binding to both a container port and a host port, we have to be aware of this on two different networks.

When selecting a host port, do not use the same port that is used by any other Deepgram service, or any other service running on the host machine. In the default Deepgram `docker-compose.yml` file, the API often uses port `8080`, and the License Proxy often uses ports `8443` and `8089`. A common default value for the Engine `HOST_PORT` is `9991`.

When selecting a container port, do not select port `8080`, as this is used on the container network to communicate between the Engine and the API. A common default value for the Engine `CONTAINER_PORT` is `9991`.

Within your `docker-compose.yml` file you must publish the internal container port to the external host port, as shown below. See [Published Ports](https://docs.docker.com/network/#published-ports) in the official Docker documentation for more details.

```yaml yaml
services:
  engine:
    # other definitions
    ports:
      - "HOST_PORT:CONTAINER_PORT"
```

To modify the Engine configuration, edit your `engine.toml` file to specify the container port to publish metrics to:

```toml toml
# To support metrics we need to expose an Engine endpoint
[metrics_server]
  host = "0.0.0.0"
  port = CONTAINER_PORT
```

Make sure to replace the placeholders `HOST_PORT` and `CONTAINER_PORT` in both of the above snippets.

Metrics may now be queried from the self-hosted instance on the local host at `:HOST_PORT/metrics`.

### Kubernetes

The Engine metrics endpoint is exposed by default by the `deepgram-self-hosted` Helm chart via a NodePort Service. This service's name is defined as the `.engine.namePrefix` configuration values appended by `-metrics`. By default, this service will be named `deepgram-engine-metrics`. See the `engine.metricsServer.*` [configuration values](https://github.com/deepgram/self-hosted-resources/tree/main/charts/deepgram-self-hosted#values) for more options.

When `scaling.auto.enabled` is set to `true`, the Engine metrics endpoint will be automatically scraped by Prometheus and used for auto-scaling.

### Available Metrics

Upon startup of the containers, a limited set of metrics will be available until the first request is made. After the first request, the complete set becomes available.

#### Initial Metrics

`engine_estimated_stream_capacity` increases as you open more streams until you reach GPU capacity. When it stops increasing, you have reached the GPU stream capacity.

```
# HELP engine_estimated_stream_capacity The number of streams the node believes it can serve with acceptable latency.
# TYPE engine_estimated_stream_capacity gauge
engine_estimated_stream_capacity <integer>
# HELP engine_active_requests Number of active inference requests.
# TYPE engine_active_requests gauge
engine_active_requests{kind="batch"} <integer>
engine_active_requests{kind="stream"} <integer>
engine_active_requests{kind="tts"} <integer>
# HELP engine_max_active_requests Maximum number of active inference requests. Zero means no limit.
# TYPE engine_max_active_requests gauge
engine_max_active_requests <integer>
```

#### Complete Metrics

After the first request, additional metrics become available. The following subsections organize metrics by category.

##### Request metrics

```
# HELP engine_active_requests Number of active inference requests.
# TYPE engine_active_requests gauge
engine_active_requests{kind="batch"} <integer>
engine_active_requests{kind="stream"} <integer>
engine_active_requests{kind="tts"} <integer>
# HELP engine_requests Number of inference requests.
# TYPE engine_requests counter
engine_requests_total{kind="batch",response_status="1xx"} <integer>
engine_requests_total{kind="batch",response_status="2xx"} <integer>
engine_requests_total{kind="batch",response_status="3xx"} <integer>
engine_requests_total{kind="batch",response_status="4xx"} <integer>
engine_requests_total{kind="batch",response_status="5xx"} <integer>
engine_requests_total{kind="stream",response_status="1xx"} <integer>
engine_requests_total{kind="stream",response_status="2xx"} <integer>
engine_requests_total{kind="stream",response_status="3xx"} <integer>
engine_requests_total{kind="stream",response_status="4xx"} <integer>
engine_requests_total{kind="stream",response_status="5xx"} <integer>
engine_requests_total{kind="tts",response_status="1xx"} <integer>
engine_requests_total{kind="tts",response_status="2xx"} <integer>
engine_requests_total{kind="tts",response_status="3xx"} <integer>
engine_requests_total{kind="tts",response_status="4xx"} <integer>
engine_requests_total{kind="tts",response_status="5xx"} <integer>
# HELP engine_max_active_requests Maximum number of active inference requests. Zero means no limit.
# TYPE engine_max_active_requests gauge
engine_max_active_requests <integer>
# HELP engine_estimated_stream_capacity The number of streams the node believes it can serve with acceptable latency.
# TYPE engine_estimated_stream_capacity gauge
engine_estimated_stream_capacity <integer>
```

##### Batch (pre-recorded) STT (ASR) metrics

```
# HELP engine_batch_response_time_seconds Time to process a batch request.
# TYPE engine_batch_response_time_seconds histogram
engine_batch_response_time_seconds_bucket{le="1.0"} <integer>
engine_batch_response_time_seconds_bucket{le="2.5"} <integer>
engine_batch_response_time_seconds_bucket{le="5.0"} <integer>
engine_batch_response_time_seconds_bucket{le="10.0"} <integer>
engine_batch_response_time_seconds_bucket{le="30.0"} <integer>
engine_batch_response_time_seconds_bucket{le="60.0"} <integer>
engine_batch_response_time_seconds_bucket{le="+Inf"} <integer>
engine_batch_response_time_seconds_sum <float>
engine_batch_response_time_seconds_count <integer>
# HELP engine_asr_per_batch_audio_duration_seconds Total audio duration represented by each inferencer ASR batch.
# TYPE engine_asr_per_batch_audio_duration_seconds histogram
# UNIT engine_asr_per_batch_audio_duration_seconds seconds
engine_asr_per_batch_audio_duration_seconds_bucket{le="0.1"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="0.25"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="0.5"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="1.0"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="2.0"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="5.0"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="10.0"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="20.0"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="40.0"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="60.0"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="120.0"} <integer>
engine_asr_per_batch_audio_duration_seconds_bucket{le="+Inf"} <integer>
engine_asr_per_batch_audio_duration_seconds_sum <float>
engine_asr_per_batch_audio_duration_seconds_count <integer>
# HELP engine_asr_per_batch_wall_time_seconds Wall-clock time spent inferring each inferencer ASR batch.
# TYPE engine_asr_per_batch_wall_time_seconds histogram
# UNIT engine_asr_per_batch_wall_time_seconds seconds
engine_asr_per_batch_wall_time_seconds_bucket{le="0.005"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="0.01"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="0.025"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="0.05"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="0.1"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="0.25"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="0.5"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="1.0"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="2.5"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="5.0"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="10.0"} <integer>
engine_asr_per_batch_wall_time_seconds_bucket{le="+Inf"} <integer>
engine_asr_per_batch_wall_time_seconds_sum <float>
engine_asr_per_batch_wall_time_seconds_count <integer>
# HELP engine_asr_per_batch_realtime_factor Per-batch ASR real-time factor: audio duration inferenced divided by wall-clock inference time.
# TYPE engine_asr_per_batch_realtime_factor histogram
engine_asr_per_batch_realtime_factor_bucket{le="0.01"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="0.03"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="0.1"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="0.3"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="1.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="3.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="10.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="30.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="100.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="300.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="1000.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="3000.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="10000.0"} <integer>
engine_asr_per_batch_realtime_factor_bucket{le="+Inf"} <integer>
engine_asr_per_batch_realtime_factor_sum <float>
engine_asr_per_batch_realtime_factor_count <integer>
# HELP engine_asr_per_file_audio_duration_seconds Total audio duration for each /listen batch-mode ASR request.
# TYPE engine_asr_per_file_audio_duration_seconds histogram
# UNIT engine_asr_per_file_audio_duration_seconds seconds
engine_asr_per_file_audio_duration_seconds_bucket{le="1.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="3.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="10.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="30.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="100.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="300.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="1000.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="3000.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="10000.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="30000.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="100000.0"} <integer>
engine_asr_per_file_audio_duration_seconds_bucket{le="+Inf"} <integer>
engine_asr_per_file_audio_duration_seconds_sum <float>
engine_asr_per_file_audio_duration_seconds_count <integer>
# HELP engine_asr_per_file_wall_time_seconds Wall-clock time spent processing each /listen batch-mode ASR request.
# TYPE engine_asr_per_file_wall_time_seconds histogram
# UNIT engine_asr_per_file_wall_time_seconds seconds
engine_asr_per_file_wall_time_seconds_bucket{le="0.05"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="0.1"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="0.25"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="0.5"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="1.0"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="2.5"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="5.0"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="10.0"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="30.0"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="60.0"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="120.0"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="240.0"} <integer>
engine_asr_per_file_wall_time_seconds_bucket{le="+Inf"} <integer>
engine_asr_per_file_wall_time_seconds_sum <float>
engine_asr_per_file_wall_time_seconds_count <integer>
# HELP engine_asr_per_file_realtime_factor Per-file ASR real-time factor for /listen batch mode: audio duration processed divided by wall-clock processing time.
# TYPE engine_asr_per_file_realtime_factor histogram
engine_asr_per_file_realtime_factor_bucket{le="0.01"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="0.03"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="0.1"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="0.3"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="1.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="3.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="10.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="30.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="100.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="300.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="1000.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="3000.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="10000.0"} <integer>
engine_asr_per_file_realtime_factor_bucket{le="+Inf"} <integer>
engine_asr_per_file_realtime_factor_sum <float>
engine_asr_per_file_realtime_factor_count <integer>
```

##### Streaming STT (ASR) metrics

```
# HELP engine_stream_connection_latency_seconds Latency establishing a streaming connection.
# TYPE engine_stream_connection_latency_seconds histogram
engine_stream_connection_latency_seconds_bucket{le="0.25"} <integer>
engine_stream_connection_latency_seconds_bucket{le="0.5"} <integer>
engine_stream_connection_latency_seconds_bucket{le="0.75"} <integer>
engine_stream_connection_latency_seconds_bucket{le="1.0"} <integer>
engine_stream_connection_latency_seconds_bucket{le="1.5"} <integer>
engine_stream_connection_latency_seconds_bucket{le="2.0"} <integer>
engine_stream_connection_latency_seconds_bucket{le="2.5"} <integer>
engine_stream_connection_latency_seconds_bucket{le="3.0"} <integer>
engine_stream_connection_latency_seconds_bucket{le="3.5"} <integer>
engine_stream_connection_latency_seconds_bucket{le="4.0"} <integer>
engine_stream_connection_latency_seconds_bucket{le="5.0"} <integer>
engine_stream_connection_latency_seconds_bucket{le="10.0"} <integer>
engine_stream_connection_latency_seconds_bucket{le="+Inf"} <integer>
engine_stream_connection_latency_seconds_sum <float>
engine_stream_connection_latency_seconds_count <integer>
# HELP engine_stream_latency Latency processing streaming requests.
# TYPE engine_stream_latency histogram
engine_stream_latency_bucket{le="0.1"} <integer>
engine_stream_latency_bucket{le="0.2"} <integer>
engine_stream_latency_bucket{le="0.3"} <integer>
engine_stream_latency_bucket{le="0.4"} <integer>
engine_stream_latency_bucket{le="0.5"} <integer>
engine_stream_latency_bucket{le="0.6"} <integer>
engine_stream_latency_bucket{le="0.7"} <integer>
engine_stream_latency_bucket{le="0.8"} <integer>
engine_stream_latency_bucket{le="0.9"} <integer>
engine_stream_latency_bucket{le="1.0"} <integer>
engine_stream_latency_bucket{le="1.1"} <integer>
engine_stream_latency_bucket{le="1.2"} <integer>
engine_stream_latency_bucket{le="1.3"} <integer>
engine_stream_latency_bucket{le="1.4"} <integer>
engine_stream_latency_bucket{le="1.5"} <integer>
engine_stream_latency_bucket{le="1.6"} <integer>
engine_stream_latency_bucket{le="1.7"} <integer>
engine_stream_latency_bucket{le="1.8"} <integer>
engine_stream_latency_bucket{le="1.9"} <integer>
engine_stream_latency_bucket{le="2.0"} <integer>
engine_stream_latency_bucket{le="5.0"} <integer>
engine_stream_latency_bucket{le="10.0"} <integer>
engine_stream_latency_bucket{le="+Inf"} <integer>
engine_stream_latency_sum <float>
engine_stream_latency_count <integer>
```

##### TTS metrics

The `tier` label identifies the TTS model family (for example, `aura` or `aura-2`).

```
# HELP engine_tts_first_raw_byte_latency Latency of inferring the first response byte for TTS requests.
# TYPE engine_tts_first_raw_byte_latency histogram
engine_tts_first_raw_byte_latency_bucket{le="0.05",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.1",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.2",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.3",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.4",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.5",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.6",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.7",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.8",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="0.9",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.0",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.1",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.2",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.3",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.4",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.5",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.6",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.7",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.8",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="1.9",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="2.0",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="2.5",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="3.0",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="4.0",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="5.0",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="10.0",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="30.0",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="60.0",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_bucket{le="+Inf",tier="<model>"} <integer>
engine_tts_first_raw_byte_latency_sum{tier="<model>"} <float>
engine_tts_first_raw_byte_latency_count{tier="<model>"} <integer>
# HELP engine_tts_first_transcoded_byte_latency Latency of first response byte for TTS requests.
# TYPE engine_tts_first_transcoded_byte_latency histogram
engine_tts_first_transcoded_byte_latency_bucket{le="0.05",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.1",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.2",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.3",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.4",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.5",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.6",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.7",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.8",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="0.9",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.0",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.1",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.2",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.3",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.4",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.5",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.6",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.7",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.8",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="1.9",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="2.0",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="2.5",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="3.0",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="4.0",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="5.0",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="10.0",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="30.0",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="60.0",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_bucket{le="+Inf",tier="<model>"} <integer>
engine_tts_first_transcoded_byte_latency_sum{tier="<model>"} <float>
engine_tts_first_transcoded_byte_latency_count{tier="<model>"} <integer>
# HELP engine_tts_failures_during_response Number of failures that occur during audio generation.
# TYPE engine_tts_failures_during_response counter
engine_tts_failures_during_response_total <integer>
```

##### Flux metrics

```
# HELP engine_flux_cursor_latency_seconds The cursor latency as measured inside impeller, after transcoding and rate-limiting.
# TYPE engine_flux_cursor_latency_seconds histogram
# UNIT engine_flux_cursor_latency_seconds seconds
engine_flux_cursor_latency_seconds_bucket{le="0.0"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="0.001"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="0.003"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="0.01"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="0.03"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="0.1"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="0.3"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="1.0"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="3.0"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="10.0"} <integer>
engine_flux_cursor_latency_seconds_bucket{le="+Inf"} <integer>
engine_flux_cursor_latency_seconds_sum <float>
engine_flux_cursor_latency_seconds_count <integer>
# HELP engine_flux_max_streams The max number of flux streams that can be processed on the GPU.
# TYPE engine_flux_max_streams gauge
engine_flux_max_streams <integer>
# HELP engine_flux_used_streams The number of flux streams that are being processed on the GPU.
# TYPE engine_flux_used_streams gauge
engine_flux_used_streams <integer>
# HELP engine_flux_fraction_streams The fraction of flux streams that are being processed on the GPU.
# TYPE engine_flux_fraction_streams gauge
engine_flux_fraction_streams <float>
```

#### Streaming STT latency metrics

Together, the `engine_stream_latency_bucket` metrics may be used to plot a histogram of streaming latency in Grafana, using the PromQL queries below. This set of metrics tracks the latency of each new stream. With this data, distribution and trends in streaming latency may be monitored for each deployment.

```
histogram_quantile(0.10, sum by (le) (rate(engine_stream_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.25, sum by (le) (rate(engine_stream_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.50, sum by (le) (rate(engine_stream_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.75, sum by (le) (rate(engine_stream_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.90, sum by (le) (rate(engine_stream_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.95, sum by (le) (rate(engine_stream_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.99, sum by (le) (rate(engine_stream_latency_bucket[5m]))) or vector(0)
```

#### TTS latency metrics

The `engine_tts_first_raw_byte_latency` and `engine_tts_first_transcoded_byte_latency` histograms can be used to monitor TTS performance in Grafana. The raw byte latency measures inference time before transcoding, while the transcoded byte latency includes the transcoding step.

Use these PromQL queries to plot TTS first-byte latency quantiles, filtering by model tier:

```
histogram_quantile(0.50, sum by (le) (rate(engine_tts_first_transcoded_byte_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.90, sum by (le) (rate(engine_tts_first_transcoded_byte_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.95, sum by (le) (rate(engine_tts_first_transcoded_byte_latency_bucket[5m]))) or vector(0)
histogram_quantile(0.99, sum by (le) (rate(engine_tts_first_transcoded_byte_latency_bucket[5m]))) or vector(0)
```

To filter by a specific model tier (for example, `aura-2`):

```
histogram_quantile(0.50, sum by (le) (rate(engine_tts_first_transcoded_byte_latency_bucket{tier="aura-2"}[5m]))) or vector(0)
histogram_quantile(0.95, sum by (le) (rate(engine_tts_first_transcoded_byte_latency_bucket{tier="aura-2"}[5m]))) or vector(0)
histogram_quantile(0.99, sum by (le) (rate(engine_tts_first_transcoded_byte_latency_bucket{tier="aura-2"}[5m]))) or vector(0)
```

### Liveness Probe

Use a TCP check on the open port (port 8080 by default).

### Readiness Probe

Use a TCP check on the open port (port 8080 by default).

## Deepgram License Proxy

For self-hosted deployments, the Deepgram License Proxy container images expose an endpoint `/v1/status`, on port 8080 by default. Querying this endpoint will indicate if the license proxy is able to communicate with the Deepgram license server.

### Liveness Probe

Use a TCP check on the open status port (port 8080 by default).

### Readiness Probe

Query the status of the `/v1/status`endpoint and check the connection state.

```bash cURL
curl --silent http://localhost:8080/v1/status | grep --quiet -e '^{.*\"state\"\:\"\(Connected\|TrustBased\)\".*}$'
```

Make sure to replace the `PORT` placeholder with the port your container is listening on (port 8080 by default).

## Summary

To access metrics for the API, Engine, and License Proxy containers, run the following CURL request from the same machine the containers are running on. The ports in the commands below are the default port numbers; check your configuration files to see if the port mapping was changed.

* API: `curl "http://localhost:8080/v1/status"` and `curl "http://localhost:8080/v1/status/engine"`
* Engine: `curl "http://localhost:9991/metrics"`
* License Proxy: `curl "http://localhost:8080/v1/status"`

***

What's Next

You may want to setup tooling for ingesting and monitoring system metrics, for example, with our Prometheus guide.

* [Prometheus Integration](/docs/prometheus-integration)
