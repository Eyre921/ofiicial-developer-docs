---
title: "Fiber"
source: https://docs.sentry.io/platforms/go/guides/fiber.md
path: platforms/go/guides/fiber
---

---
title: "Fiber"
description: "Learn how to add Sentry instrumentation to programs using the Fiber package."
url: https://docs.sentry.io/platforms/go/guides/fiber/
---

# Sentry for Fiber

For a quick reference, there is a [complete example](https://github.com/getsentry/sentry-go/tree/master/_examples/fiber) at the Go SDK source code repository.

[Go Dev-style API documentation](https://godoc.org/github.com/getsentry/sentry-go/fiber) is also available.

## [Install](https://docs.sentry.io/platforms/go/guides/fiber.md#install)

```bash
go get github.com/getsentry/sentry-go
go get github.com/getsentry/sentry-go/fiber
```

## [Configure](https://docs.sentry.io/platforms/go/guides/fiber.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/go/guides/fiber.md#initialize-the-sentry-sdk)

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

### [Options](https://docs.sentry.io/platforms/go/guides/fiber.md#options)

`sentryfiber` accepts a struct of `Options` that allows you to configure how the handler will behave.

```go
// Repanic configures whether Sentry should repanic after recovery, in most cases it should be set to true,
// as fiber includes its own Recover middleware that handles http responses.
Repanic bool
// WaitForDelivery configures whether you want to block the request before moving forward with the response.
// Because Fiber's `Recover` handler doesn't restart the application,
// it's safe to either skip this option or set it to `false`.
WaitForDelivery bool
// Timeout for the event delivery requests.
Timeout time.Duration
```

```go
sentryHandler := sentryfiber.New(sentryfiber.Options{
    // you can modify these options
    Repanic:         true,
    WaitForDelivery: false,
    Timeout:         5 * time.Second,
})

app := fiber.New()
app.Use(sentryHandler)
```

## [Verify](https://docs.sentry.io/platforms/go/guides/fiber.md#verify)

```go
app := fiber.New()

app.Use(sentryfiber.New(sentryfiber.Options{
// specify options here...
}))

app.All("/", func(ctx *fiber.Ctx) error {
	// capturing an error intentionally to simulate usage
	sentry.CaptureMessage("It works!")
	
	return ctx.SendStatus(fiber.StatusOK)
})

if err := app.Listen(":3000"); err != nil {
	panic(err)
}
```

## [Usage](https://docs.sentry.io/platforms/go/guides/fiber.md#usage)

`sentryfiber` attaches an instance of `*sentry.Hub` (<https://godoc.org/github.com/getsentry/sentry-go#Hub>) to the request's context, which makes it available throughout the rest of the request's lifetime. You can access it by using the `sentryfiber.GetHubFromContext()` method on the context itself in any of your proceeding middleware and routes. This method should be used instead of the global `sentry.CaptureMessage`, `sentry.CaptureException`, or any other calls, as it maintains the separation of data between the requests.

Your middleware automatically captures transactions for incoming requests. See [Automatic Instrumentation](https://docs.sentry.io/platforms/go/guides/fiber/tracing/instrumentation/auto-instrumentation.md) for what's captured. To add custom spans within your handlers, see [Custom Instrumentation](https://docs.sentry.io/platforms/go/guides/fiber/tracing/instrumentation/custom-instrumentation.md).

**Keep in mind that `*sentry.Hub` won't be available in middleware attached before `sentryfiber`!**

```go
func enhanceSentryEvent := func(ctx *fiber.Ctx) error {
	if hub := sentryfiber.GetHubFromContext(ctx); hub != nil {
		hub.Scope().SetTag("someRandomTag", "maybeYouNeedIt")
	}
	return ctx.Next()
}

// Later in the code
sentryHandler := sentryfiber.New(sentryfiber.Options{
	Repanic:         true,
	WaitForDelivery: true,
})

defaultHandler := func(ctx *fiber.Ctx) error {
	if hub := sentryfiber.GetHubFromContext(ctx); hub != nil {
		hub.WithScope(func(scope *sentry.Scope) {
			scope.SetAttributes(attribute.String("unwantedQuery", "someQueryDataMaybe"))
			hub.CaptureMessage("User provided unwanted query string, but we recovered just fine")
		})
	}
	return ctx.SendStatus(fiber.StatusOK)
}

fooHandler := enhanceSentryEvent(func(ctx *fiber.Ctx) {
	panic("y tho")
})

app.All("/foo", fooHandler)
app.All("/", defaultHandler)

if err := app.Listen(":3000"); err != nil {
	panic(err)
}

fmt.Println("Listening and serving HTTP on :3000")
```

### [Accessing Context in `BeforeSend` callback](https://docs.sentry.io/platforms/go/guides/fiber.md#accessing-context-in-beforesend-callback)

```go
sentry.Init(sentry.ClientOptions{
	Dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
	BeforeSend: func(event *sentry.Event, hint *sentry.EventHint) *sentry.Event {
		if hint.Context != nil {
			if ctx, ok := hint.Context.Value(sentry.RequestContextKey).(*fiber.Ctx); ok {
				// You have access to the original Context if it panicked
				fmt.Println(utils.CopyString(ctx.Hostname()))
			}
		}
		return event
	},
})
```

## [Next Steps](https://docs.sentry.io/platforms/go/guides/fiber.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Go Frameworks

- [Echo](https://docs.sentry.io/platforms/go/guides/echo.md)
- [FastHTTP](https://docs.sentry.io/platforms/go/guides/fasthttp.md)
- [Fiber v3](https://docs.sentry.io/platforms/go/guides/fiberv3.md)
- [Gin](https://docs.sentry.io/platforms/go/guides/gin.md)
- [gRPC](https://docs.sentry.io/platforms/go/guides/grpc.md)
- [Iris](https://docs.sentry.io/platforms/go/guides/iris.md)
- [Negroni](https://docs.sentry.io/platforms/go/guides/negroni.md)
- [net/http](https://docs.sentry.io/platforms/go/guides/http.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/go/guides/fiber/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/go/guides/fiber/usage.md)
- [Source Context](https://docs.sentry.io/platforms/go/guides/fiber/source-context.md)
- [Integrations](https://docs.sentry.io/platforms/go/guides/fiber/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/go/guides/fiber/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/go/guides/fiber/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/go/guides/fiber/tracing.md)
- [Logs](https://docs.sentry.io/platforms/go/guides/fiber/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/go/guides/fiber/metrics.md)
- [Crons](https://docs.sentry.io/platforms/go/guides/fiber/crons.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/go/guides/fiber/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/go/guides/fiber/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/go/guides/fiber/troubleshooting.md)

