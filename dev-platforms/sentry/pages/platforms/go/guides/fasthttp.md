---
title: "FastHTTP"
source: https://docs.sentry.io/platforms/go/guides/fasthttp.md
path: platforms/go/guides/fasthttp
---

---
title: "FastHTTP"
description: "Learn how to add Sentry instrumentation to programs using the FastHTTP package."
url: https://docs.sentry.io/platforms/go/guides/fasthttp/
---

# Sentry for FastHTTP

For a quick reference, there is a [complete example](https://github.com/getsentry/sentry-go/tree/master/_examples/fasthttp) available directly at the Go SDK source code repository.

[Go Dev-style API documentation](https://pkg.go.dev/github.com/getsentry/sentry-go/fasthttp) is also available.

## [Install](https://docs.sentry.io/platforms/go/guides/fasthttp.md#install)

```bash
go get github.com/getsentry/sentry-go
go get github.com/getsentry/sentry-go/fasthttp
```

## [Configure](https://docs.sentry.io/platforms/go/guides/fasthttp.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/go/guides/fasthttp.md#initialize-the-sentry-sdk)

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

### [Options](https://docs.sentry.io/platforms/go/guides/fasthttp.md#options)

`sentryfasthttp` accepts a struct of `Options` that allows you to configure how the handler will behave.

```go
// Repanic configures whether Sentry should repanic after recovery, in most cases, it defaults to false,
// as fasthttp doesn't include its own Recovery handler.
Repanic bool
// WaitForDelivery configures whether you want to block the request before moving forward with the response.
// Because fasthttp doesn't include its own `Recovery` handler, it will restart the application,
// and the event won't be delivered otherwise.
WaitForDelivery bool
// Timeout for the event delivery requests.
Timeout time.Duration
```

```go
// Create an instance of sentryfasthttp
sentryHandler := sentryfasthttp.New(sentryfasthttp.Options{
    Repanic:         false,
    WaitForDelivery: true,
    Timeout:         5 * time.Second,
})
```

## [Verify](https://docs.sentry.io/platforms/go/guides/fasthttp.md#verify)

```go
// Create an instance of sentryfasthttp
sentryHandler := sentryfasthttp.New(sentryfasthttp.Options{
// specify options here...
})

// After creating the instance, you can attach the handler as one of your middleware
fastHTTPHandler := sentryHandler.Handle(func(ctx *fasthttp.RequestCtx) {
	// capturing an error intentionally to simulate usage
	sentry.CaptureMessage("It works!")
	
	ctx.SetStatusCode(fasthttp.StatusOK)
})

fmt.Println("Listening and serving HTTP on :3000")

// And run it
if err := fasthttp.ListenAndServe(":3000", fastHTTPHandler); err != nil {
	panic(err)
}
```

## [Usage](https://docs.sentry.io/platforms/go/guides/fasthttp.md#usage)

`sentryfasthttp` attaches an instance of `*sentry.Hub` (<https://pkg.go.dev/github.com/getsentry/sentry-go#Hub>) to the request's context, which makes it available throughout the rest of the request's lifetime. You can access it by using the `sentryfasthttp.GetHubFromContext()` method on the context itself in any of your proceeding middleware and routes. And it should be used instead of the global `sentry.CaptureMessage`, `sentry.CaptureException`, or any other calls, as it keeps the separation of data between the requests.

Your middleware automatically captures transactions for incoming requests. See [Automatic Instrumentation](https://docs.sentry.io/platforms/go/guides/fasthttp/tracing/instrumentation/auto-instrumentation.md) for what's captured. To add custom spans within your handlers, see [Custom Instrumentation](https://docs.sentry.io/platforms/go/guides/fasthttp/tracing/instrumentation/custom-instrumentation.md).

**Keep in mind that `*sentry.Hub` won't be available in middleware attached before `sentryfasthttp`!**

```go
func enhanceSentryEvent(handler fasthttp.RequestHandler) fasthttp.RequestHandler {
	return func(ctx *fasthttp.RequestCtx) {
		if hub := sentryfasthttp.GetHubFromContext(ctx); hub != nil {
			hub.Scope().SetTag("someRandomTag", "maybeYouNeedIt")
		}
		handler(ctx)
	}
}

// Later in the code
sentryHandler := sentryfasthttp.New(sentryfasthttp.Options{
	Repanic: true,
	WaitForDelivery: true,
})

defaultHandler := func(ctx *fasthttp.RequestCtx) {
	if hub := sentryfasthttp.GetHubFromContext(ctx); hub != nil {
		hub.WithScope(func(scope *sentry.Scope) {
			scope.SetAttributes(attribute.String("unwantedQuery", "someQueryDataMaybe"))
			hub.CaptureMessage("User provided unwanted query string, but we recovered just fine")
		})
	}
	ctx.SetStatusCode(fasthttp.StatusOK)
}

fooHandler := enhanceSentryEvent(func(ctx *fasthttp.RequestCtx) {
	panic("y tho")
})

fastHTTPHandler := func(ctx *fasthttp.RequestCtx) {
	switch string(ctx.Path()) {
	case "/foo":
		fooHandler(ctx)
	default:
		defaultHandler(ctx)
	}
}

fmt.Println("Listening and serving HTTP on :3000")

if err := fasthttp.ListenAndServe(":3000", sentryHandler.Handle(fastHTTPHandler)); err != nil {
	panic(err)
}
```

### [Accessing Context in `BeforeSend` callback](https://docs.sentry.io/platforms/go/guides/fasthttp.md#accessing-context-in-beforesend-callback)

```go
sentry.Init(sentry.ClientOptions{
	Dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
	BeforeSend: func(event *sentry.Event, hint *sentry.EventHint) *sentry.Event {
		if hint.Context != nil {
			if ctx, ok := hint.Context.Value(sentry.RequestContextKey).(*fasthttp.RequestCtx); ok {
				// You have access to the original Context if it panicked
				fmt.Println(string(ctx.Request.Host()))
			}
		}
		return event
	},
})
```

## [Next Steps](https://docs.sentry.io/platforms/go/guides/fasthttp.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Go Frameworks

- [Echo](https://docs.sentry.io/platforms/go/guides/echo.md)
- [Fiber](https://docs.sentry.io/platforms/go/guides/fiber.md)
- [Fiber v3](https://docs.sentry.io/platforms/go/guides/fiberv3.md)
- [Gin](https://docs.sentry.io/platforms/go/guides/gin.md)
- [gRPC](https://docs.sentry.io/platforms/go/guides/grpc.md)
- [Iris](https://docs.sentry.io/platforms/go/guides/iris.md)
- [Negroni](https://docs.sentry.io/platforms/go/guides/negroni.md)
- [net/http](https://docs.sentry.io/platforms/go/guides/http.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/go/guides/fasthttp/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/go/guides/fasthttp/usage.md)
- [Source Context](https://docs.sentry.io/platforms/go/guides/fasthttp/source-context.md)
- [Integrations](https://docs.sentry.io/platforms/go/guides/fasthttp/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/go/guides/fasthttp/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/go/guides/fasthttp/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/go/guides/fasthttp/tracing.md)
- [Logs](https://docs.sentry.io/platforms/go/guides/fasthttp/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/go/guides/fasthttp/metrics.md)
- [Crons](https://docs.sentry.io/platforms/go/guides/fasthttp/crons.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/go/guides/fasthttp/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/go/guides/fasthttp/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/go/guides/fasthttp/troubleshooting.md)

