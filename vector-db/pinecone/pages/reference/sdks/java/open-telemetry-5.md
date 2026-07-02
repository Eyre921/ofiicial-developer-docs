---
title: "OpenTelemetry support"
source: https://docs.pinecone.io/reference/sdks/java/open-telemetry
path: reference/sdks/java/open-telemetry
---

Monitor Pinecone Java SDK operations with OpenTelemetry metrics, including latency breakdowns and error tracking.

The Pinecone Java SDK provides built-in support for capturing per-operation response metadata, making it straightforward to monitor your Pinecone usage with [OpenTelemetry](https://opentelemetry.io/) or any other observability system.

With this feature, you can track client-side latency, server processing time, network overhead, error rates, and more for every data plane operation your application makes.

## How it all fits together

The SDK's observability support is designed to be flexible. You don't need to adopt the entire observability stack at once -- start simple and add layers as your needs grow.

Here are the components involved and how they relate to each other:

* **Pinecone Java SDK**: Exposes a `ResponseMetadataListener` callback, a plain Java interface with no external dependencies. At its simplest, you can log the metadata to the console. No additional tools required.
* **[OpenTelemetry](https://opentelemetry.io/) (OTel)**: An open standard and SDK for producing structured telemetry data (metrics, traces, logs). If you want standardized metrics that follow [semantic conventions](https://opentelemetry.io/docs/specs/semconv/database/database-spans/), you add the OTel SDK and wire it to the listener. This is optional.
* **OTel Collector**: A vendor-neutral service that receives telemetry from your app and forwards it to a storage backend. Optional -- many setups export directly from the app to a backend.
* **Prometheus**: A time-series database that stores metrics, making them queryable over time. One popular storage option.
* **Grafana**: A visualization and dashboarding tool that queries Prometheus (or other backends) and displays charts and alerts. One popular visualization option.

A common setup chains these together:

```
Your App (OTel SDK) → OTel Collector → Prometheus (storage) → Grafana (visualization)
```

<Note>
  This is just one example pipeline. You can substitute Datadog, New Relic, or any OTel-compatible backend. You can also skip OTel entirely and use [Micrometer](#example-micrometerprometheus), custom logging, or any approach that suits your stack.
</Note>

## Response metadata listener

The Java SDK captures response metadata through a `ResponseMetadataListener` -- a functional interface you provide when building the Pinecone client. The listener is called after each data plane operation completes (whether it succeeds or fails), and receives a `ResponseMetadata` object containing timing, status, and context information.

The SDK itself has no OpenTelemetry dependency. You bring your own observability library and decide what to do with the metadata.

### Supported operations

The following data plane operations are instrumented, for both synchronous (`Index`) and asynchronous (`AsyncIndex`) usage:

| Operation | Description                |
| --------- | -------------------------- |
| `upsert`  | Insert or update vectors   |
| `query`   | Search for similar vectors |
| `fetch`   | Retrieve vectors by ID     |
| `update`  | Update vector metadata     |
| `delete`  | Delete vectors             |

### Available metadata

Each `ResponseMetadata` object provides the following fields:

| Method                   | Description                                        | OTel attribute            |
| ------------------------ | -------------------------------------------------- | ------------------------- |
| `getOperationName()`     | Operation type (e.g., `upsert`, `query`)           | `db.operation.name`       |
| `getIndexName()`         | Pinecone index name                                | `pinecone.index_name`     |
| `getNamespace()`         | Namespace (empty string if default)                | `db.namespace`            |
| `getServerAddress()`     | Pinecone server host                               | `server.address`          |
| `getClientDurationMs()`  | Total round-trip time in ms (always available)     | --                        |
| `getServerDurationMs()`  | Server processing time in ms (may be `null`)       | --                        |
| `getNetworkOverheadMs()` | Client minus server duration in ms (may be `null`) | --                        |
| `getStatus()`            | `"success"` or `"error"`                           | `status`                  |
| `getGrpcStatusCode()`    | Raw gRPC status code (e.g., `OK`, `UNAVAILABLE`)   | `db.response.status_code` |
| `getErrorType()`         | Error category, or `null` if successful            | `error.type`              |

Possible `errorType` values: `validation`, `connection`, `server`, `rate_limit`, `timeout`, `auth`, `not_found`, `unknown`.

### Recommended metrics

If you're recording OTel metrics, the SDK example project uses these metric names, which follow [OTel semantic conventions for database clients](https://opentelemetry.io/docs/specs/semconv/database/database-spans/):

| Metric                                | Type      | Unit | Description                     |
| ------------------------------------- | --------- | ---- | ------------------------------- |
| `db.client.operation.duration`        | Histogram | ms   | Client-measured round-trip time |
| `pinecone.server.processing.duration` | Histogram | ms   | Server processing time          |
| `db.client.operation.count`           | Counter   | --   | Total number of operations      |

## Quick start: Simple logging

The simplest way to use the listener is to log the metadata directly. This requires no additional dependencies beyond the Pinecone SDK:

```java theme={null}
import io.pinecone.clients.Pinecone;

Pinecone client = new Pinecone.Builder("PINECONE_API_KEY")
    .withResponseMetadataListener(metadata -> {
        System.out.printf("Operation: %s | Client: %dms | Server: %sms | Network: %sms | Status: %s%n",
            metadata.getOperationName(),
            metadata.getClientDurationMs(),
            metadata.getServerDurationMs(),
            metadata.getNetworkOverheadMs(),
            metadata.getStatus());
    })
    .build();
```

Once configured, every data plane operation automatically triggers the listener:

```java theme={null}
Index index = client.getIndexConnection("my-index");
index.upsert("id-1", Arrays.asList(0.1f, 0.2f, 0.3f));
// Output: Operation: upsert | Client: 47ms | Server: 40ms | Network: 7ms | Status: success
```

## Quick start: OpenTelemetry integration

To record structured metrics with OpenTelemetry, add the OTel SDK dependencies and wire a metrics recorder to the listener.

### 1. Add dependencies

Add the following to your `pom.xml`:

```xml theme={null}
<dependencies>
    <!-- Pinecone SDK -->
    <dependency>
        <groupId>io.pinecone</groupId>
        <artifactId>pinecone-client</artifactId>
        <version>LATEST</version>
    </dependency>

    <!-- OpenTelemetry SDK -->
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-sdk</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-sdk-metrics</artifactId>
    </dependency>

    <!-- OTLP exporter (sends metrics to an OTel Collector or compatible backend) -->
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-exporter-otlp</artifactId>
    </dependency>
</dependencies>

<!-- Use the OTel BOM to manage versions -->
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-bom</artifactId>
            <version>1.35.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 2. Create a metrics recorder

The SDK's [example project](https://github.com/pinecone-io/pinecone-java-client/tree/main/examples/java-otel-metrics) includes a reusable `PineconeMetricsRecorder` class you can copy into your project. It implements `ResponseMetadataListener` and records all three recommended metrics with proper OTel attributes:

```java theme={null}
import io.opentelemetry.api.common.AttributeKey;
import io.opentelemetry.api.common.Attributes;
import io.opentelemetry.api.common.AttributesBuilder;
import io.opentelemetry.api.metrics.LongCounter;
import io.opentelemetry.api.metrics.LongHistogram;
import io.opentelemetry.api.metrics.Meter;
import io.pinecone.configs.ResponseMetadata;
import io.pinecone.configs.ResponseMetadataListener;

public class PineconeMetricsRecorder implements ResponseMetadataListener {

    private static final AttributeKey<String> DB_SYSTEM = AttributeKey.stringKey("db.system");
    private static final AttributeKey<String> DB_OPERATION_NAME = AttributeKey.stringKey("db.operation.name");
    private static final AttributeKey<String> DB_NAMESPACE = AttributeKey.stringKey("db.namespace");
    private static final AttributeKey<String> PINECONE_INDEX_NAME = AttributeKey.stringKey("pinecone.index_name");
    private static final AttributeKey<String> SERVER_ADDRESS = AttributeKey.stringKey("server.address");
    private static final AttributeKey<String> STATUS = AttributeKey.stringKey("status");
    private static final AttributeKey<String> ERROR_TYPE = AttributeKey.stringKey("error.type");

    private final LongHistogram clientDurationHistogram;
    private final LongHistogram serverDurationHistogram;
    private final LongCounter operationCounter;

    public PineconeMetricsRecorder(Meter meter) {
        this.clientDurationHistogram = meter.histogramBuilder("db.client.operation.duration")
                .setDescription("Duration of Pinecone operations from client perspective")
                .setUnit("ms")
                .ofLongs()
                .build();

        this.serverDurationHistogram = meter.histogramBuilder("pinecone.server.processing.duration")
                .setDescription("Server processing time from x-pinecone-response-duration-ms header")
                .setUnit("ms")
                .ofLongs()
                .build();

        this.operationCounter = meter.counterBuilder("db.client.operation.count")
                .setDescription("Total number of Pinecone operations")
                .setUnit("{operation}")
                .build();
    }

    @Override
    public void onResponse(ResponseMetadata metadata) {
        AttributesBuilder attributesBuilder = Attributes.builder()
                .put(DB_SYSTEM, "pinecone")
                .put(DB_OPERATION_NAME, metadata.getOperationName())
                .put(PINECONE_INDEX_NAME, metadata.getIndexName())
                .put(SERVER_ADDRESS, metadata.getServerAddress())
                .put(STATUS, metadata.getStatus());

        String namespace = metadata.getNamespace();
        if (namespace != null && !namespace.isEmpty()) {
            attributesBuilder.put(DB_NAMESPACE, namespace);
        }

        if (!metadata.isSuccess() && metadata.getErrorType() != null) {
            attributesBuilder.put(ERROR_TYPE, metadata.getErrorType());
        }

        Attributes attributes = attributesBuilder.build();

        clientDurationHistogram.record(metadata.getClientDurationMs(), attributes);

        Long serverDuration = metadata.getServerDurationMs();
        if (serverDuration != null) {
            serverDurationHistogram.record(serverDuration, attributes);
        }

        operationCounter.add(1, attributes);
    }
}
```

### 3. Wire it into the Pinecone client

Initialize the OTel SDK, create the recorder, and pass it to the Pinecone client builder:

```java theme={null}
import io.opentelemetry.api.metrics.Meter;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.metrics.SdkMeterProvider;
import io.opentelemetry.sdk.metrics.export.PeriodicMetricReader;
import io.opentelemetry.exporter.otlp.metrics.OtlpGrpcMetricExporter;
import io.pinecone.clients.Pinecone;

// Set up OTel with OTLP exporter
OtlpGrpcMetricExporter exporter = OtlpGrpcMetricExporter.builder()
    .setEndpoint("http://localhost:4317")
    .build();

SdkMeterProvider meterProvider = SdkMeterProvider.builder()
    .registerMetricReader(PeriodicMetricReader.builder(exporter).build())
    .build();

OpenTelemetrySdk openTelemetry = OpenTelemetrySdk.builder()
    .setMeterProvider(meterProvider)
    .build();

// Create the metrics recorder
Meter meter = openTelemetry.getMeter("pinecone.client");
PineconeMetricsRecorder recorder = new PineconeMetricsRecorder(meter);

// Build the Pinecone client with the recorder
Pinecone client = new Pinecone.Builder("PINECONE_API_KEY")
    .withResponseMetadataListener(recorder)
    .build();

// Use the client normally -- metrics are recorded automatically
Index index = client.getIndexConnection("my-index");
index.upsert("id-1", Arrays.asList(0.1f, 0.2f, 0.3f));
index.query(3, Arrays.asList(0.1f, 0.2f, 0.3f));
```

<Tip>
  For a complete runnable example with Docker Compose, Prometheus, and Grafana, see the [java-otel-metrics example project](https://github.com/pinecone-io/pinecone-java-client/tree/main/examples/java-otel-metrics) in the SDK repository.
</Tip>

## Example: Micrometer/Prometheus

If your application uses [Micrometer](https://micrometer.io/) (common in Spring Boot), you can wire the listener to Micrometer instead of the OTel SDK:

```java theme={null}
import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.Timer;
import io.pinecone.clients.Pinecone;
import java.util.concurrent.TimeUnit;

Pinecone client = new Pinecone.Builder("PINECONE_API_KEY")
    .withResponseMetadataListener(metadata -> {
        Timer.builder("pinecone.client.duration")
            .tag("operation", metadata.getOperationName())
            .tag("index", metadata.getIndexName())
            .tag("status", metadata.getStatus())
            .register(meterRegistry)
            .record(metadata.getClientDurationMs(), TimeUnit.MILLISECONDS);
    })
    .build();
```

## Visualizing metrics

Once your metrics are flowing to a backend, you can build dashboards to monitor your Pinecone operations. If you're using Prometheus and Grafana, here are some useful queries:

**P50 and P95 client latency:**

```promql theme={null}
histogram_quantile(0.5, sum(rate(db_client_operation_duration_milliseconds_bucket[5m])) by (le))
histogram_quantile(0.95, sum(rate(db_client_operation_duration_milliseconds_bucket[5m])) by (le))
```

**P95 latency by operation type:**

```promql theme={null}
histogram_quantile(0.95, sum(rate(db_client_operation_duration_milliseconds_bucket[5m])) by (le, db_operation_name))
```

**Operation count by type:**

```promql theme={null}
sum by (db_operation_name) (db_client_operation_count_total)
```

## Understanding the latency breakdown

The `ResponseMetadata` object provides three timing values that help you pinpoint the source of latency issues:

| Component        | Method                   | What it measures                                                                                                                             |
| ---------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Client duration  | `getClientDurationMs()`  | Total round-trip time from request start to response completion. Always available.                                                           |
| Server duration  | `getServerDurationMs()`  | Time the Pinecone backend spent processing the request. Extracted from the `x-pinecone-response-duration-ms` response header. May be `null`. |
| Network overhead | `getNetworkOverheadMs()` | The difference: client duration minus server duration. Includes network latency, serialization, and deserialization. May be `null`.          |

Use these values to diagnose performance issues:

* **High server duration**: The bottleneck is on the Pinecone backend. Consider optimizing your query (e.g., reducing `topK`, using metadata filters), or check the [Pinecone status page](https://status.pinecone.io/).
* **High network overhead**: The bottleneck is in the network path between your application and Pinecone. Consider deploying your application closer to your index's cloud region, or check for network issues.

## Limitations

* **Data plane operations only.** Control plane operations (e.g., creating or deleting indexes) are not currently instrumented.
* **Bulk import operations** are not yet instrumented.
* **Server duration may be unavailable.** The `getServerDurationMs()` method returns `null` if the `x-pinecone-response-duration-ms` header is not present in the response.
* **Synchronous callback.** The listener is called synchronously after the gRPC response is received. Keep implementations lightweight and non-blocking to avoid adding latency to your operations. For heavy processing, queue the metadata for async handling.
* **Exceptions are swallowed.** Exceptions thrown by the listener are logged but do not affect the operation result.

## Best practices

* **Keep listeners lightweight.** Record metrics or enqueue work -- don't do I/O or heavy computation in the callback.
* **Follow OTel semantic conventions.** Use the attribute names shown in the [recommended metrics](#recommended-metrics) table for interoperability with standard dashboards and tooling.
* **Monitor both client and server duration.** Tracking both lets you separate Pinecone backend performance from network conditions.
* **Set alerts on error rates.** Use the `status` and `error.type` attributes to build alerts for elevated error rates across operations.
