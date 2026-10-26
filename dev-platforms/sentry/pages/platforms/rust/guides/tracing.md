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

* Reporting `tracing` events to Sentry as events, breadcrumbs, or logs.
* Reporting `tracing` spans to Sentry.
* Reporting errors and panics with the correct trace correlation.

## [Install](https://docs.sentry.io/platforms/rust/guides/tracing.md#install)

Error Monitoring\[ ]Tracing\[ ]Logs

To add Sentry with the `tracing` integration to your Rust project, add the necessary dependencies to your `Cargo.toml`:

```toml
[dependencies]
tracing = "0.1.41"
tracing-subscriber = "0.3.19"
sentry = { version = "0.49.3", features = [
  "tracing"
] }
tokio = { version = "1.45.0", features = ["full"] }
```

## [Configure](https://docs.sentry.io/platforms/rust/guides/tracing.md#configure)

Initialize the Sentry SDK and register the Sentry layer to start sending `tracing` events and spans to Sentry:

Macros like `#[tokio::main]` and `#[actix_web::main]` are not supported. The Sentry client must be initialized before the async runtime is started, as shown below.

```rust
use tracing_subscriber::prelude::*;

fn main() {
    // Initialize Sentry
    let _guard = sentry::init(
        sentry::ClientOptions::new()
            .dsn("https://<key>@o<orgId>.ingest.sentry.io/<projectId>")
            .maybe_release(sentry::release_name!())
            # ___PRODUCT_OPTION_START___ performance
            // Capture all traces and spans. Set to a lower value in production
            .traces_sample_rate(1.0)
            # ___PRODUCT_OPTION_END___ performance
    );

    // Register the Sentry tracing layer
    tracing_subscriber::registry()
        .with(tracing_subscriber::fmt::layer())
        .with(sentry::integrations::tracing::layer())
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

# ___PRODUCT_OPTION_START___ performance
#[tracing::instrument] // Captures a root span (transaction) around this function execution
# ___PRODUCT_OPTION_END___ performance
async fn fail() {
    tracing::debug!("Doing work"); // Adds a breadrcumb
    # ___PRODUCT_OPTION_START___ performance
    let _span = tracing::info_span("Child span").entered(); // Captures a child span
    # ___PRODUCT_OPTION_END___ performance
    tracing::error!("Everything is on fire!");
}
```

By default, error-level events from `tracing` are captured as Sentry events, while events at or above info level are added to the current scope as breadcrumbs.

Additionally, the SDK captures [logs](https://docs.sentry.io/product/logs.md) for `tracing` events at the info level or above, unless logs were disabled when initializing the SDK.

This behavior can be customized by applying a custom `event_filter` when creating the layer. The following snippet shows the default `event_filter` that's applied when using the `sentry` crate with the `tracing` feature flag.

```rust
use sentry::integrations::tracing::EventFilter;

let sentry_layer =
    sentry::integrations::tracing::layer().event_filter(|md| match *md.level() {
        // Capture error and warn level events as both logs and events in Sentry
        tracing::Level::ERROR => EventFilter::Event | EventFilter::Log,
        // Ignore trace level events, as they're too verbose
        tracing::Level::TRACE => EventFilter::Ignore,
        // Capture everything else as both a breadcrumb and a log
        _ => EventFilter::Breadcrumb | EventFilter::Log,
    });
```

## [Verify](https://docs.sentry.io/platforms/rust/guides/tracing.md#verify)

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/rust/guides/tracing/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Select Issues, and then Errors & Outages in the sidebar, where you will find the newly created issue. Clicking on the issue's title will open a page where you can see detailed information and mark it as resolved.

If you're using tracing (the Sentry feature), you can view the recorded traces and spans by selecting Explore, and then Traces in the sidebar.

If you're using logs, you can view the recorded logs by selecting Explore, and then Logs in the sidebar.

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

