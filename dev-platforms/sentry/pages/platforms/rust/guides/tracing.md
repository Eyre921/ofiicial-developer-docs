---
title: "tokio-rs/tracing"
source: https://docs.sentry.io/platforms/rust/guides/tracing.md
path: platforms/rust/guides/tracing
---

---
title: "tokio-rs/tracing"
description: "Learn about monitoring your Rust application with Sentry's tokio-rs/tracing integration."
url: https://docs.sentry.io/platforms/rust/guides/tracing/
---

# Sentry for tokio-rs/tracing

The Sentry SDK offers an integration for tokio's [tracing](https://github.com/tokio-rs/tracing) ecosystem that supports:

* Reporting `tracing` spans to Sentry as transactions and spans.
* Reporting `tracing` events to Sentry as logs.
* Reporting errors and panics with the correct trace correlation.

## [Install](https://docs.sentry.io/platforms/rust/guides/tracing.md#install)

To add Sentry with the `tracing` integration to your Rust project, add the necessary dependencies to your `Cargo.toml`:

```toml
[dependencies]
tracing = "0.1.41"
tracing-subscriber = "0.3.19"
sentry = { version = "0.49.5", features = [
  "tracing"
] }
tokio = { version = "1.45.0", features = ["full"] }
```

## [Configure](https://docs.sentry.io/platforms/rust/guides/tracing.md#configure)

Initialize the Sentry SDK and register the Sentry layers to start sending `tracing` spans and logs to Sentry:

Macros like `#[tokio::main]` and `#[actix_web::main]` are not supported. The Sentry client must be initialized before the async runtime is started, as shown below.

```rust
use sentry::integrations::tracing::{LogLayer, SpanLayer};
use tracing_subscriber::filter::LevelFilter;
use tracing_subscriber::prelude::*;

fn main() {
    // Initialize Sentry
    let _guard = sentry::init(
        sentry::ClientOptions::new()
            .dsn("https://<key>@o<orgId>.ingest.sentry.io/<projectId>")
            .maybe_release(sentry::release_name!())
            // Capture all traces and spans. Set to a lower value in production
            .traces_sample_rate(1.0)
    );

    // Register the Sentry tracing layers
    tracing_subscriber::registry()
        .with(tracing_subscriber::fmt::layer())
        // Capture INFO, WARN, and ERROR spans as Sentry transactions and spans
        .with(SpanLayer::new().with_filter(LevelFilter::INFO))
        // Capture INFO, WARN, and ERROR events as Sentry logs
        .with(LogLayer::new().with_filter(LevelFilter::INFO))
        .init();

    tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .build()?
        .block_on(async {
            // Futures should to be bound to a Hub
            // Learn more at https://docs.rs/sentry-core/latest/sentry_core/#parallelism-concurrency-and-async
            fail().bind_hub(sentry::Hub::current()).await;
        });
}

#[tracing::instrument] // Captures a root span (transaction) around this function execution
async fn fail() {
    tracing::info!("Doing work"); // Captured as a log
    let _span = tracing::info_span("Child span").entered(); // Captures a child span
    tracing::error!("Everything is on fire!"); // Captured as a log, linked to the child span
}
```

The integration provides two layers, and we recommend installing both:

* [`SpanLayer`](https://docs.rs/sentry-tracing/latest/sentry_tracing/struct.SpanLayer.html): Captures `tracing` spans as Sentry transactions and spans.
* [`LogLayer`](https://docs.rs/sentry-tracing/latest/sentry_tracing/struct.LogLayer.html): Captures `tracing` events as Sentry logs. Requires the `logs` feature, which is enabled by default.

The layers don't filter by level on their own, and without a filter they capture every level, including `DEBUG` and `TRACE`. We recommend giving each layer a `tracing_subscriber` filter, as shown above. `LevelFilter::INFO` is a sensible starting point for most applications.

The SDK also provides [`ErrorLayer`](https://docs.rs/sentry-tracing/latest/sentry_tracing/struct.ErrorLayer.html) and [`BreadcrumbLayer`](https://docs.rs/sentry-tracing/latest/sentry_tracing/struct.BreadcrumbLayer.html), which capture `tracing` events as Sentry errors and breadcrumbs. They're mainly there to support legacy setups, so most applications should stick with the span and log layers.

`sentry::integrations::tracing::layer()` and `SentryLayer` are deprecated as of version `0.49.4`. When migrating, replace the legacy layer instead of adding the new layers alongside it: combining `SpanLayer` with the legacy layer can panic. See the [migration guide](https://docs.rs/sentry-tracing/~0.49/sentry_tracing/struct.SentryLayer.html) for details.

## [Verify](https://docs.sentry.io/platforms/rust/guides/tracing.md#verify)

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/rust/guides/tracing/usage.md).

To view the recorded traces and spans, log into [sentry.io](https://sentry.io), select your project, and then select Explore > Traces in the sidebar.

To view the recorded logs, select Explore > Logs in the sidebar.

## [Next Steps](https://docs.sentry.io/platforms/rust/guides/tracing.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Rust Frameworks

- [Actix Web](https://docs.sentry.io/platforms/rust/guides/actix-web.md)
- [axum](https://docs.sentry.io/platforms/rust/guides/axum.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/rust/guides/tracing/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/rust/guides/tracing/usage.md)
- [Native Crash Reporting](https://docs.sentry.io/platforms/rust/guides/tracing/native-crash-reporting.md)
- [Enriching Events](https://docs.sentry.io/platforms/rust/guides/tracing/enriching-events.md)
- [Source Context](https://docs.sentry.io/platforms/rust/guides/tracing/source-context.md)
- [Data Management](https://docs.sentry.io/platforms/rust/guides/tracing/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/rust/guides/tracing/tracing.md)
- [Logs](https://docs.sentry.io/platforms/rust/guides/tracing/logs.md)
- [Metrics](https://docs.sentry.io/platforms/rust/guides/tracing/metrics.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/rust/guides/tracing/security-policy-reporting.md)
- [Troubleshooting](https://docs.sentry.io/platforms/rust/guides/tracing/troubleshooting.md)

