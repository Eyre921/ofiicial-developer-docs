---
title: "Echo"
source: https://docs.sentry.io/platforms/go/guides/echo.md
path: platforms/go/guides/echo
---

---
title: "Echo"
description: "Echo is a high-performance web framework for building robust and scalable applications in Go. Learn how to set it up with Sentry. Requires Echo v5."
url: https://docs.sentry.io/platforms/go/guides/echo/
---

# Sentry for Echo

For a quick reference, there is a [complete example](https://github.com/getsentry/sentry-go/tree/master/_examples/echo) at the Go SDK source code repository.

[Go Dev-style API documentation](https://pkg.go.dev/github.com/getsentry/sentry-go/echo) is also available.

## [Install](https://docs.sentry.io/platforms/go/guides/echo.md#install)

```bash
go get github.com/getsentry/sentry-go
go get github.com/getsentry/sentry-go/echo
```

## [Configure](https://docs.sentry.io/platforms/go/guides/echo.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/go/guides/echo.md#initialize-the-sentry-sdk)

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

### [Options](https://docs.sentry.io/platforms/go/guides/echo.md#options)

`sentryecho` accepts a struct of `Options` that allows you to configure how the handler will behave.

```go
// Repanic configures whether Sentry should repanic after recovery, in most cases it should be set to true,
// as echo includes its own Recover middleware that handles http responses.
Repanic bool
// WaitForDelivery configures whether you want to block the request before moving forward with the response.
// Because Echo's `Recover` handler doesn't restart the application,
// it's safe to either skip this option or set it to `false`.
WaitForDelivery bool
// Timeout for the event delivery requests.
Timeout time.Duration
```

```go
app := echo.New()
app.Use(sentryecho.New(sentryecho.Options{
    // you can modify these options
    Repanic:         true,
    WaitForDelivery: false,
    Timeout:         5 * time.Second,
}))
```

## [Verify](https://docs.sentry.io/platforms/go/guides/echo.md#verify)

```go
app := echo.New()
app.Use(middleware.Logger())
app.Use(middleware.Recover())

// Attach the sentryecho handler as one of your middlewares
app.Use(sentryecho.New(sentryecho.Options{
// specify options here...
}))

// Set up routes
app.GET("/", func(ctx *echo.Context) error {
    // capturing an error intentionally to simulate usage
    sentry.CaptureMessage("It works!")

	return ctx.String(http.StatusOK, "Hello, World!")
})

app.Logger.Fatal(app.Start(":3000"))
```

## [Usage](https://docs.sentry.io/platforms/go/guides/echo.md#usage)

`sentryecho` attaches an instance of `*sentry.Hub` (<https://pkg.go.dev/github.com/getsentry/sentry-go#Hub>) to the `*echo.Context`, which makes it available throughout the rest of the request's lifetime. You can access it by using the `sentryecho.GetHubFromContext()` method on the context itself in any of your proceeding middleware and routes. And it should be used instead of the global `sentry.CaptureMessage`, `sentry.CaptureException` or any other calls, as it keeps the separation of data between the requests.

Your middleware automatically captures transactions for incoming requests. See [Automatic Instrumentation](https://docs.sentry.io/platforms/go/guides/echo/tracing/instrumentation/auto-instrumentation.md) for what's captured. To add custom spans within your handlers, see [Custom Instrumentation](https://docs.sentry.io/platforms/go/guides/echo/tracing/instrumentation/custom-instrumentation.md).

**Keep in mind that `*sentry.Hub` won't be available in middleware attached before `sentryecho`!**

```go
app := echo.New()

app.Use(middleware.Logger())
app.Use(middleware.Recover())

app.Use(sentryecho.New(sentryecho.Options{
	Repanic: true,
}))

app.Use(func(next echo.HandlerFunc) echo.HandlerFunc {
	return func(ctx *echo.Context) error {
		if hub := sentryecho.GetHubFromContext(ctx); hub != nil {
			hub.Scope().SetTag("someRandomTag", "maybeYouNeedIt")
		}
		return next(ctx)
	}
})

app.GET("/", func(ctx *echo.Context) error {
	if hub := sentryecho.GetHubFromContext(ctx); hub != nil {
		hub.WithScope(func(scope *sentry.Scope) {
			scope.SetAttributes(attribute.String("unwantedQuery", "someQueryDataMaybe"))
			hub.CaptureMessage("User provided unwanted query string, but we recovered just fine")
		})
	}
	return ctx.String(http.StatusOK, "Hello, World!")
})

app.GET("/foo", func(ctx *echo.Context) error {
	// sentryecho handler will catch it just fine. Also, because we attached "someRandomTag"
	// in the middleware before, it will be sent through as well
	panic("y tho")
})

app.Logger.Fatal(app.Start(":3000"))
```

### [Accessing Request in `BeforeSend` callback](https://docs.sentry.io/platforms/go/guides/echo.md#accessing-request-in-beforesend-callback)

```go
sentry.Init(sentry.ClientOptions{
	Dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
	BeforeSend: func(event *sentry.Event, hint *sentry.EventHint) *sentry.Event {
		if hint.Context != nil {
			if req, ok := hint.Context.Value(sentry.RequestContextKey).(*http.Request); ok {
				// You have access to the original Request here
			}
		}

		return event
	},
})
```

## [Next Steps](https://docs.sentry.io/platforms/go/guides/echo.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Go Frameworks

- [FastHTTP](https://docs.sentry.io/platforms/go/guides/fasthttp.md)
- [Fiber](https://docs.sentry.io/platforms/go/guides/fiber.md)
- [Fiber v3](https://docs.sentry.io/platforms/go/guides/fiberv3.md)
- [Gin](https://docs.sentry.io/platforms/go/guides/gin.md)
- [gRPC](https://docs.sentry.io/platforms/go/guides/grpc.md)
- [Iris](https://docs.sentry.io/platforms/go/guides/iris.md)
- [Negroni](https://docs.sentry.io/platforms/go/guides/negroni.md)
- [net/http](https://docs.sentry.io/platforms/go/guides/http.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/go/guides/echo/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/go/guides/echo/usage.md)
- [Source Context](https://docs.sentry.io/platforms/go/guides/echo/source-context.md)
- [Integrations](https://docs.sentry.io/platforms/go/guides/echo/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/go/guides/echo/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/go/guides/echo/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/go/guides/echo/tracing.md)
- [Logs](https://docs.sentry.io/platforms/go/guides/echo/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/go/guides/echo/metrics.md)
- [Crons](https://docs.sentry.io/platforms/go/guides/echo/crons.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/go/guides/echo/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/go/guides/echo/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/go/guides/echo/troubleshooting.md)

