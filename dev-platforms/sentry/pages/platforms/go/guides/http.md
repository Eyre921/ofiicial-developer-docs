---
title: "net/http"
source: https://docs.sentry.io/platforms/go/guides/http.md
path: platforms/go/guides/http
---

---
title: "net/http"
description: "The net/http package provides HTTP client and server implementations. Learn how to add Sentry to programs using this package."
url: https://docs.sentry.io/platforms/go/guides/http/
---

# Sentry for net/http

For a quick reference, there is a [complete example](https://github.com/getsentry/sentry-go/tree/master/_examples/http) at the Go SDK source code repository.

[Go Dev-style API documentation](https://pkg.go.dev/github.com/getsentry/sentry-go/http) is also available.

## [Install](https://docs.sentry.io/platforms/go/guides/http.md#install)

```bash
go get github.com/getsentry/sentry-go
go get github.com/getsentry/sentry-go/http
```

## [Configure](https://docs.sentry.io/platforms/go/guides/http.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/go/guides/http.md#initialize-the-sentry-sdk)

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

### [Options](https://docs.sentry.io/platforms/go/guides/http.md#options)

`sentryhttp` accepts a struct of `Options` that allows you to configure how the handler will behave.

```go
// Whether Sentry should repanic after recovery, in most cases it should be set to true,
// and you should gracefully handle http responses.
Repanic bool
// Whether you want to block the request before moving forward with the response.
// Useful, when you want to restart the process after it panics.
WaitForDelivery bool
// Timeout for the event delivery requests.
Timeout time.Duration
```

```go
// Create an instance of sentryhttp
sentryHandler := sentryhttp.New(sentryhttp.Options{
    Repanic:         true,
    WaitForDelivery: false,
    Timeout:         5 * time.Second,
})
```

## [Verify](https://docs.sentry.io/platforms/go/guides/http.md#verify)

```go
type handler struct{}

func (h *handler) ServeHTTP(rw http.ResponseWriter, r *http.Request) {
	// capturing an error intentionally to simulate usage
	sentry.CaptureMessage("It works!")
	
	rw.WriteHeader(http.StatusOK)
}

// Create an instance of sentryhttp
sentryHandler := sentryhttp.New(sentryhttp.Options{
// specify options here...
})

// Once it's done, you can set up routes and attach the handler as one of your middleware
http.Handle("/", sentryHandler.Handle(&handler{}))

fmt.Println("Listening and serving HTTP on :3000")

// And run it
if err := http.ListenAndServe(":3000", nil); err != nil {
	panic(err)
}
```

## [Usage](https://docs.sentry.io/platforms/go/guides/http.md#usage)

`sentryhttp` attaches an instance of `*sentry.Hub` (<https://pkg.go.dev/github.com/getsentry/sentry-go#Hub>) to the request's context, which makes it available throughout the rest of the request's lifetime. You can access it by using the `sentry.GetHubFromContext()` method on the request itself in any of your proceeding middleware and routes. And it should be used instead of the global `sentry.CaptureMessage`, `sentry.CaptureException`, or any other calls, as it keeps the separation of data between the requests.

Your middleware automatically captures transactions for incoming requests. See [Automatic Instrumentation](https://docs.sentry.io/platforms/go/guides/http/tracing/instrumentation/auto-instrumentation.md) for what's captured. To add custom spans within your handlers, see [Custom Instrumentation](https://docs.sentry.io/platforms/go/guides/http/tracing/instrumentation/custom-instrumentation.md).

**Keep in mind that `*sentry.Hub` won't be available in middleware attached before `sentryhttp`!**

```go
type handler struct{}

func (h *handler) ServeHTTP(rw http.ResponseWriter, r *http.Request) {
	if hub := sentry.GetHubFromContext(r.Context()); hub != nil {
		hub.WithScope(func(scope *sentry.Scope) {
			scope.SetAttributes(attribute.String("unwantedQuery", "someQueryDataMaybe"))
			hub.CaptureMessage("User provided unwanted query string, but we recovered just fine")
		})
	}
	rw.WriteHeader(http.StatusOK)
}

func enhanceSentryEvent(handler http.HandlerFunc) http.HandlerFunc {
	return func(rw http.ResponseWriter, r *http.Request) {
		if hub := sentry.GetHubFromContext(r.Context()); hub != nil {
			hub.Scope().SetTag("someRandomTag", "maybeYouNeedIt")
		}
		handler(rw, r)
	}
}

// Later in the code

sentryHandler := sentryhttp.New(sentryhttp.Options{
	Repanic: true,
})

http.Handle("/", sentryHandler.Handle(&handler{}))
http.HandleFunc("/foo", sentryHandler.HandleFunc(
	enhanceSentryEvent(func(rw http.ResponseWriter, r *http.Request) {
		panic("y tho")
	}),
))

fmt.Println("Listening and serving HTTP on :3000")

if err := http.ListenAndServe(":3000", nil); err != nil {
	panic(err)
}
```

### [Accessing Request in `BeforeSend` callback](https://docs.sentry.io/platforms/go/guides/http.md#accessing-request-in-beforesend-callback)

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

## [Next Steps](https://docs.sentry.io/platforms/go/guides/http.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Go Frameworks

- [Echo](https://docs.sentry.io/platforms/go/guides/echo.md)
- [FastHTTP](https://docs.sentry.io/platforms/go/guides/fasthttp.md)
- [Fiber](https://docs.sentry.io/platforms/go/guides/fiber.md)
- [Fiber v3](https://docs.sentry.io/platforms/go/guides/fiberv3.md)
- [Gin](https://docs.sentry.io/platforms/go/guides/gin.md)
- [gRPC](https://docs.sentry.io/platforms/go/guides/grpc.md)
- [Iris](https://docs.sentry.io/platforms/go/guides/iris.md)
- [Negroni](https://docs.sentry.io/platforms/go/guides/negroni.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/go/guides/http/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/go/guides/http/usage.md)
- [Source Context](https://docs.sentry.io/platforms/go/guides/http/source-context.md)
- [Integrations](https://docs.sentry.io/platforms/go/guides/http/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/go/guides/http/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/go/guides/http/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/go/guides/http/tracing.md)
- [Logs](https://docs.sentry.io/platforms/go/guides/http/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/go/guides/http/metrics.md)
- [Crons](https://docs.sentry.io/platforms/go/guides/http/crons.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/go/guides/http/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/go/guides/http/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/go/guides/http/troubleshooting.md)

