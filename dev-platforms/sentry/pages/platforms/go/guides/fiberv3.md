---
title: "Fiber v3"
source: https://docs.sentry.io/platforms/go/guides/fiberv3.md
path: platforms/go/guides/fiberv3
---

---
title: "Fiber v3"
description: "Learn how to add Sentry instrumentation to programs using Fiber v3."
url: https://docs.sentry.io/platforms/go/guides/fiberv3/
---

# Sentry for Fiber v3

For a quick reference, see the [Fiber v3 example](https://github.com/getsentry/sentry-go/tree/master/_examples/fiber) in the Go SDK source code repository.

[Go Dev-style API documentation](https://pkg.go.dev/github.com/getsentry/sentry-go/fiberv3) is also available.

Fiber v3 uses the `github.com/getsentry/sentry-go/fiberv3` package. For Fiber v2, use the [`sentry-go/fiber` package](https://docs.sentry.io/platforms/go/guides/fiber.md).

## [Install](https://docs.sentry.io/platforms/go/guides/fiberv3.md#install)

```bash
go get github.com/getsentry/sentry-go
go get github.com/getsentry/sentry-go/fiberv3
```

## [Configure](https://docs.sentry.io/platforms/go/guides/fiberv3.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/go/guides/fiberv3.md#initialize-the-sentry-sdk)

Error Monitoring\[ ]Tracing

```go
err := sentry.Init(sentry.ClientOptions{
    Dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    // Enable printing of SDK debug messages.
    // Useful when getting started or trying to figure something out.
    Debug: true,
    // Adds request headers and IP for users,
    // visit: https://docs.sentry.io/platforms/go/data-management/data-collected/ for more info
    SendDefaultPII: true,
    // ___PRODUCT_OPTION_START___ performance
    EnableTracing: true,
    // Set TracesSampleRate to 1.0 to capture 100%
    // of transactions for tracing.
    TracesSampleRate: 1.0,
    // ___PRODUCT_OPTION_END___ performance
})
if err != nil {
    log.Fatalf("sentry.Init: %s", err)
}
// Flush buffered events before the program terminates.
// Set the timeout to the maximum duration the program can afford to wait.
defer sentry.Flush(2 * time.Second)
```

### [Options](https://docs.sentry.io/platforms/go/guides/fiberv3.md#options)

`sentryfiberv3` accepts a struct of `Options` that allows you to configure how the handler behaves.

```go
// Repanic configures whether Sentry should repanic after recovery. Fiber v3
// doesn't include its own Recovery handler, so set this according to how your
// application handles panics.
Repanic bool
// WaitForDelivery configures whether to block the request before continuing.
// Enable it when the application may exit before the event is delivered.
WaitForDelivery bool
// Timeout for the event delivery requests.
Timeout time.Duration
```

```go
sentryHandler := sentryfiberv3.New(sentryfiberv3.Options{
    // you can modify these options
    Repanic:         true,
    WaitForDelivery: true,
    Timeout:         5 * time.Second,
})

app := fiber.New()
app.Use(sentryHandler)
```

## [Verify](https://docs.sentry.io/platforms/go/guides/fiberv3.md#verify)

```go
app := fiber.New()

app.Use(sentryfiberv3.New(sentryfiberv3.Options{
// specify options here...
}))

app.All("/", func(ctx fiber.Ctx) error {
    // capturing an error intentionally to simulate usage
    sentry.CaptureMessage("It works!")

    return ctx.SendStatus(fiber.StatusOK)
})

if err := app.Listen(":3000"); err != nil {
    panic(err)
}
```

## [Usage](https://docs.sentry.io/platforms/go/guides/fiberv3.md#usage)

`sentryfiberv3` attaches an instance of `*sentry.Hub` to `fiber.Ctx`, which makes it available throughout the rest of the request's lifetime. You can access it with `sentryfiberv3.GetHubFromContext()` in subsequent middleware and routes. Use this hub instead of the global capture functions to keep data separated between requests.

Your middleware automatically captures transactions for incoming requests. See [Automatic Instrumentation](https://docs.sentry.io/platforms/go/guides/fiberv3/tracing/instrumentation/auto-instrumentation.md) for what's captured. To add custom spans within your handlers, see [Custom Instrumentation](https://docs.sentry.io/platforms/go/guides/fiberv3/tracing/instrumentation/custom-instrumentation.md).

**Keep in mind that `*sentry.Hub` won't be available in middleware attached before `sentryfiberv3`!**

```go
func enhanceSentryEvent(ctx fiber.Ctx) error {
    if hub := sentryfiberv3.GetHubFromContext(ctx); hub != nil {
        hub.Scope().SetTag("someRandomTag", "maybeYouNeedIt")
    }
    return ctx.Next()
}

sentryHandler := sentryfiberv3.New(sentryfiberv3.Options{
    Repanic:         true,
    WaitForDelivery: true,
})

defaultHandler := func(ctx fiber.Ctx) error {
    if hub := sentryfiberv3.GetHubFromContext(ctx); hub != nil {
        hub.WithScope(func(scope *sentry.Scope) {
            scope.SetAttributes(attribute.String("unwantedQuery", "someQueryDataMaybe"))
            hub.CaptureMessage("User provided unwanted query string, but we recovered just fine")
        })
    }
    return ctx.SendStatus(fiber.StatusOK)
}

fooHandler := func(ctx fiber.Ctx) error {
    enhanceSentryEvent(ctx)
    panic("y tho")
}

app.Use(sentryHandler)
app.All("/foo", fooHandler)
app.All("/", defaultHandler)

if err := app.Listen(":3000"); err != nil {
    panic(err)
}
```

### [Accessing Context in `BeforeSend` Callback](https://docs.sentry.io/platforms/go/guides/fiberv3.md#accessing-context-in-beforesend-callback)

Fiber v3 passes a `fiber.Ctx` value in the request context rather than the `*fiber.Ctx` used by Fiber v2:

```go
sentry.Init(sentry.ClientOptions{
    Dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    BeforeSend: func(event *sentry.Event, hint *sentry.EventHint) *sentry.Event {
        if hint.Context != nil {
            if ctx, ok := hint.Context.Value(sentry.RequestContextKey).(fiber.Ctx); ok {
                fmt.Println(ctx.Hostname())
            }
        }
        return event
    },
})
```

## [Next Steps](https://docs.sentry.io/platforms/go/guides/fiberv3.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Go Frameworks

- [Echo](https://docs.sentry.io/platforms/go/guides/echo.md)
- [FastHTTP](https://docs.sentry.io/platforms/go/guides/fasthttp.md)
- [Fiber](https://docs.sentry.io/platforms/go/guides/fiber.md)
- [Gin](https://docs.sentry.io/platforms/go/guides/gin.md)
- [gRPC](https://docs.sentry.io/platforms/go/guides/grpc.md)
- [Iris](https://docs.sentry.io/platforms/go/guides/iris.md)
- [Negroni](https://docs.sentry.io/platforms/go/guides/negroni.md)
- [net/http](https://docs.sentry.io/platforms/go/guides/http.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/go/guides/fiberv3/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/go/guides/fiberv3/usage.md)
- [Source Context](https://docs.sentry.io/platforms/go/guides/fiberv3/source-context.md)
- [Integrations](https://docs.sentry.io/platforms/go/guides/fiberv3/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/go/guides/fiberv3/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/go/guides/fiberv3/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/go/guides/fiberv3/tracing.md)
- [Logs](https://docs.sentry.io/platforms/go/guides/fiberv3/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/go/guides/fiberv3/metrics.md)
- [Crons](https://docs.sentry.io/platforms/go/guides/fiberv3/crons.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/go/guides/fiberv3/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/go/guides/fiberv3/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/go/guides/fiberv3/troubleshooting.md)

