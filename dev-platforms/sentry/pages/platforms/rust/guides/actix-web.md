---
title: "Actix Web"
source: https://docs.sentry.io/platforms/rust/guides/actix-web.md
path: platforms/rust/guides/actix-web
---

---
title: "Actix Web"
description: "Learn about monitoring your Actix Web application with Sentry."
url: https://docs.sentry.io/platforms/rust/guides/actix-web/
---

# Sentry for Actix Web

The Sentry SDK offers a middleware for the [Actix Web](https://actix.rs/) framework that supports:

* Capturing server errors returned by Actix Web services.
* Starting a [transaction](https://docs.sentry.io/concepts/key-terms/tracing.md) for each request-response cycle.

## [Install](https://docs.sentry.io/platforms/rust/guides/actix-web.md#install)

To add Sentry with the Actix Web integration to your Rust project, add a new dependency to your `Cargo.toml`:

```toml
[dependencies]
actix-web = "4.11.0"
sentry = { version = "0.49.5", features = ["actix"] }
```

## [Configure](https://docs.sentry.io/platforms/rust/guides/actix-web.md#configure)

Initialize and configure the Sentry client. This will enable a set of default integrations, such as panic reporting. Then, initialize Actix Web with the Sentry middleware. The Sentry middleware provides correct request and trace association for any captured errors or panics, so it should be the first to process the request, that means it should be the last in your chain of `wrap` calls.

Macros like `#[tokio::main]` and `#[actix_web::main]` are not supported. The Sentry client must be initialized before the async runtime is started, as shown below.

```rust
use std::io;

use actix_web::{get, App, Error, HttpRequest, HttpServer};

#[get("/")]
async fn failing(_req: HttpRequest) -> Result<String, Error> {
    Err(io::Error::new(io::ErrorKind::Other, "An error happens here").into())
}

fn main() -> io::Result<()> {
    let _guard = sentry::init(
        sentry::ClientOptions::new()
            .dsn("https://<key>@o<orgId>.ingest.sentry.io/<projectId>")
            .maybe_release(sentry::release_name!())
            // Capture all traces and spans. Set to a lower value in production
            .traces_sample_rate(1.0)
            // Capture user IPs and potentially sensitive headers when using HTTP server integrations
            // see https://docs.sentry.io/platforms/rust/data-management/data-collected for more info
            .send_default_pii(true)
            // Capture all HTTP request bodies, regardless of size
            .max_request_body_size(sentry::MaxRequestBodySize::Always),
    );

    actix_web::rt::System::new().block_on(async {
        HttpServer::new(|| {
            App::new()
                .wrap(
                    sentry::integrations::actix::Sentry::builder()
                        .capture_server_errors(true) // Capture server errors
                        .start_transaction(true) // Start a transaction (Sentry root span) for each request
                        .finish(),
                )
                .service(failing)
        })
        .bind("127.0.0.1:3001")?
        .run()
        .await
    })?;

    Ok(())
}
```

## [Verify](https://docs.sentry.io/platforms/rust/guides/actix-web.md#verify)

The snippet above sets up a service that always fails, so you can test that everything is working as soon as you set it up.

Send a request to the application. The response error will be captured by Sentry.

```bash
curl http://localhost:3001/
```

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/rust/guides/actix-web/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/rust/guides/actix-web.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Rust Frameworks

- [axum](https://docs.sentry.io/platforms/rust/guides/axum.md)
- [tokio-rs/tracing](https://docs.sentry.io/platforms/rust/guides/tracing.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/rust/guides/actix-web/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/rust/guides/actix-web/usage.md)
- [Native Crash Reporting](https://docs.sentry.io/platforms/rust/guides/actix-web/native-crash-reporting.md)
- [Enriching Events](https://docs.sentry.io/platforms/rust/guides/actix-web/enriching-events.md)
- [Source Context](https://docs.sentry.io/platforms/rust/guides/actix-web/source-context.md)
- [Data Management](https://docs.sentry.io/platforms/rust/guides/actix-web/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/rust/guides/actix-web/tracing.md)
- [Logs](https://docs.sentry.io/platforms/rust/guides/actix-web/logs.md)
- [Metrics](https://docs.sentry.io/platforms/rust/guides/actix-web/metrics.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/rust/guides/actix-web/security-policy-reporting.md)
- [Troubleshooting](https://docs.sentry.io/platforms/rust/guides/actix-web/troubleshooting.md)

