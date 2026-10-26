---
title: "Gin"
source: https://docs.sentry.io/platforms/go/guides/gin.md
path: platforms/go/guides/gin
---

---
title: "Gin"
description: "Gin is a high-performance HTTP web framework written in Golang. Learn how to set it up with Sentry."
url: https://docs.sentry.io/platforms/go/guides/gin/
---

# Sentry for Gin

For a quick reference, there is a [complete example](https://github.com/getsentry/sentry-go/tree/master/_examples/gin) at the Go SDK source code repository.

[Go Dev-style API documentation](https://pkg.go.dev/github.com/getsentry/sentry-go/gin) is also available.

## [Install](https://docs.sentry.io/platforms/go/guides/gin.md#install)

```bash
go get github.com/getsentry/sentry-go
go get github.com/getsentry/sentry-go/gin
```

## [Configure](https://docs.sentry.io/platforms/go/guides/gin.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/go/guides/gin.md#initialize-the-sentry-sdk)

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

### [Options](https://docs.sentry.io/platforms/go/guides/gin.md#options)

`sentrygin` accepts a struct of `Options` that allows you to configure how the handler will behave.

```go
// Whether Sentry should repanic after recovery, in most cases it should be set to true,
// as gin.Default includes its own Recovery middleware that handles http responses.
Repanic bool
// Whether you want to block the request before moving forward with the response.
// Because Gin's default `Recovery` handler doesn't restart the application,
// it's safe to either skip this option or set it to `false`.
WaitForDelivery bool
// Timeout for the event delivery requests.
Timeout time.Duration
```

```go
app := gin.Default()
app.Use(sentrygin.New(sentrygin.Options{
    // you can modify these options
    Repanic:         true,
    WaitForDelivery: false,
    Timeout:         5 * time.Second,
}))
```

## [Verify](https://docs.sentry.io/platforms/go/guides/gin.md#verify)

```go
app := gin.Default()

// you can attach the handler as one of your middleware
app.Use(sentrygin.New(sentrygin.Options{
// specify options here...
}))

// Set up routes
app.GET("/", func(ctx *gin.Context) {
	// capturing an error intentionally to simulate usage
	sentry.CaptureMessage("It works!")
	
	ctx.String(http.StatusOK, "Hello world!")
})

// And run it
app.Run(":3000")
```

## [Usage](https://docs.sentry.io/platforms/go/guides/gin.md#usage)

`sentrygin` attaches an instance of `*sentry.Hub` (<https://pkg.go.dev/github.com/getsentry/sentry-go#Hub>) to the `*gin.Context`, which makes it available throughout the rest of the request's lifetime. You can access it by using the `sentrygin.GetHubFromContext()` method on the context itself in any of your proceeding middleware and routes. And it should be used instead of the global `sentry.CaptureMessage`, `sentry.CaptureException`, or any other calls, as it keeps the separation of data between the requests.

Your middleware automatically captures transactions for incoming requests. See [Automatic Instrumentation](https://docs.sentry.io/platforms/go/guides/gin/tracing/instrumentation/auto-instrumentation.md) for what's captured. To add custom spans within your handlers, see [Custom Instrumentation](https://docs.sentry.io/platforms/go/guides/gin/tracing/instrumentation/custom-instrumentation.md).

**Keep in mind that `*sentry.Hub` won't be available in middleware attached before `sentrygin`!**

```go
app := gin.Default()

app.Use(sentrygin.New(sentrygin.Options{
	Repanic: true,
}))

app.Use(func(ctx *gin.Context) {
	if hub := sentrygin.GetHubFromContext(ctx); hub != nil {
		hub.Scope().SetTag("someRandomTag", "maybeYouNeedIt")
	}
	ctx.Next()
})

app.GET("/", func(ctx *gin.Context) {
	if hub := sentrygin.GetHubFromContext(ctx); hub != nil {
		hub.WithScope(func(scope *sentry.Scope) {
			scope.SetAttributes(attribute.String("unwantedQuery", "someQueryDataMaybe"))
			hub.CaptureMessage("User provided unwanted query string, but we recovered just fine")
		})
	}
	ctx.Status(http.StatusOK)
})

app.GET("/foo", func(ctx *gin.Context) {
	// sentrygin handler will catch it just fine. Also, because we attached "someRandomTag"
	// in the middleware before, it will be sent through as well
	panic("y tho")
})

app.Run(":3000")
```

### [Accessing Request in `BeforeSend` callback](https://docs.sentry.io/platforms/go/guides/gin.md#accessing-request-in-beforesend-callback)

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

## [Next Steps](https://docs.sentry.io/platforms/go/guides/gin.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Go Frameworks

- [Echo](https://docs.sentry.io/platforms/go/guides/echo.md)
- [FastHTTP](https://docs.sentry.io/platforms/go/guides/fasthttp.md)
- [Fiber](https://docs.sentry.io/platforms/go/guides/fiber.md)
- [Fiber v3](https://docs.sentry.io/platforms/go/guides/fiberv3.md)
- [gRPC](https://docs.sentry.io/platforms/go/guides/grpc.md)
- [Iris](https://docs.sentry.io/platforms/go/guides/iris.md)
- [Negroni](https://docs.sentry.io/platforms/go/guides/negroni.md)
- [net/http](https://docs.sentry.io/platforms/go/guides/http.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/go/guides/gin/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/go/guides/gin/usage.md)
- [Source Context](https://docs.sentry.io/platforms/go/guides/gin/source-context.md)
- [Integrations](https://docs.sentry.io/platforms/go/guides/gin/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/go/guides/gin/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/go/guides/gin/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/go/guides/gin/tracing.md)
- [Logs](https://docs.sentry.io/platforms/go/guides/gin/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/go/guides/gin/metrics.md)
- [Crons](https://docs.sentry.io/platforms/go/guides/gin/crons.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/go/guides/gin/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/go/guides/gin/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/go/guides/gin/troubleshooting.md)

