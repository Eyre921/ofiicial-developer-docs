---
title: "Negroni"
source: https://docs.sentry.io/platforms/go/guides/negroni.md
path: platforms/go/guides/negroni
---

---
title: "Negroni"
description: "Negroni is an idiomatic approach to web middleware in Go. Learn how to set it up with Sentry."
url: https://docs.sentry.io/platforms/go/guides/negroni/
---

# Sentry for Negroni

For a quick reference, there is a [complete example](https://github.com/getsentry/sentry-go/tree/master/_examples/negroni) at the Go SDK source code repository.

[Go Dev-style API documentation](https://pkg.go.dev/github.com/getsentry/sentry-go/negroni) is also available.

## [Install](https://docs.sentry.io/platforms/go/guides/negroni.md#install)

```bash
go get github.com/getsentry/sentry-go
go get github.com/getsentry/sentry-go/negroni
```

## [Configure](https://docs.sentry.io/platforms/go/guides/negroni.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/go/guides/negroni.md#initialize-the-sentry-sdk)

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

### [Options](https://docs.sentry.io/platforms/go/guides/negroni.md#options)

`sentrynegroni` accepts a struct of `Options` that allows you to configure how the handler will behave.

```go
// Whether Sentry should repanic after recovery, in most cases it should be set to true,
// as negroni.Classic includes its own Recovery middleware that handles http responses.
Repanic bool
// Whether you want to block the request before moving forward with the response.
// Because Negroni's default `Recovery` handler doesn't restart the application,
// it's safe to either skip this option or set it to `false`.
WaitForDelivery bool
// Timeout for the event delivery requests.
Timeout time.Duration
```

```go
app := negroni.Classic()

app.Use(sentrynegroni.New(sentrynegroni.Options{
    // modify your own config options
    Repanic:         true,
    WaitForDelivery: false,
    Timeout:         5 * time.Second,
}))
```

## [Verify](https://docs.sentry.io/platforms/go/guides/negroni.md#verify)

```go
app := negroni.Classic()

app.Use(sentrynegroni.New(sentrynegroni.Options{
// specify options here...
}))

// Set up routes
mux := http.NewServeMux()

mux.HandleFunc("/", func(rw http.ResponseWriter, r *http.Request) {
	// capturing an error intentionally to simulate usage
	sentry.CaptureMessage("It works!")
	
	fmt.Fprintf(rw, "Hello world!")
})

app.UseHandler(mux)

// And run it
http.ListenAndServe(":3000", app)
```

## [Usage](https://docs.sentry.io/platforms/go/guides/negroni.md#usage)

`sentrynegroni` attaches an instance of `*sentry.Hub` (<https://pkg.go.dev/github.com/getsentry/sentry-go#Hub>) to the request's context, which makes it available throughout the rest of the request's lifetime. You can access it by using the `sentry.GetHubFromContext()` method on the request itself in any of your proceeding middleware and routes. And it should be used instead of the global `sentry.CaptureMessage`, `sentry.CaptureException`, or any other calls, as it keeps the separation of data between the requests.

Your middleware automatically captures transactions for incoming requests. See [Automatic Instrumentation](https://docs.sentry.io/platforms/go/guides/negroni/tracing/instrumentation/auto-instrumentation.md) for what's captured. To add custom spans within your handlers, see [Custom Instrumentation](https://docs.sentry.io/platforms/go/guides/negroni/tracing/instrumentation/custom-instrumentation.md).

**Keep in mind that `*sentry.Hub` won't be available in middleware attached before `sentrynegroni`!**

```go
app := negroni.Classic()

app.Use(sentrynegroni.New(sentrynegroni.Options{
	Repanic: true,
}))

app.Use(negroni.HandlerFunc(func(rw http.ResponseWriter, r *http.Request, next http.HandlerFunc) {
	hub := sentry.GetHubFromContext(r.Context())
	hub.Scope().SetTag("someRandomTag", "maybeYouNeedIt")
	next(rw, r)
}))

mux := http.NewServeMux()

mux.HandleFunc("/", func(rw http.ResponseWriter, r *http.Request) {
	hub := sentry.GetHubFromContext(r.Context())
	hub.WithScope(func(scope *sentry.Scope) {
		scope.SetAttributes(attribute.String("unwantedQuery", "someQueryDataMaybe"))
		hub.CaptureMessage("User provided unwanted query string, but we recovered just fine")
	})
	rw.WriteHeader(http.StatusOK)
})

mux.HandleFunc("/foo", func(rw http.ResponseWriter, r *http.Request) {
	// sentrynagroni handler will catch it just fine. Also, because we attached "someRandomTag"
	// in the middleware before, it will be sent through as well
	panic("y tho")
})

app.UseHandler(mux)

http.ListenAndServe(":3000", app)
```

### [Accessing Request in `BeforeSend` callback](https://docs.sentry.io/platforms/go/guides/negroni.md#accessing-request-in-beforesend-callback)

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

## [Using Negroni's `PanicHandlerFunc` Option](https://docs.sentry.io/platforms/go/guides/negroni.md#using-negronis-panichandlerfunc-option)

Negroni provides an option called `PanicHandlerFunc`, which lets you "plug-in" to its default `Recovery` middleware.

`sentrynegroni` exports a very barebones implementation, which utilizes it, so if you don't need anything else than just reporting panics to Sentry, you can use it instead, as it's just one line of code!

You can still use `BeforeSend` and event processors to modify data before delivering it to Sentry, using this method as well.

```go
app := negroni.New()

recovery := negroni.NewRecovery()
recovery.PanicHandlerFunc = sentrynegroni.PanicHandlerFunc

app.Use(recovery)

mux := http.NewServeMux()
mux.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
	panic("y tho")
})

app.UseHandler(mux)

http.ListenAndServe(":3000", app)
```

## [Next Steps](https://docs.sentry.io/platforms/go/guides/negroni.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Go Frameworks

- [Echo](https://docs.sentry.io/platforms/go/guides/echo.md)
- [FastHTTP](https://docs.sentry.io/platforms/go/guides/fasthttp.md)
- [Fiber](https://docs.sentry.io/platforms/go/guides/fiber.md)
- [Fiber v3](https://docs.sentry.io/platforms/go/guides/fiberv3.md)
- [Gin](https://docs.sentry.io/platforms/go/guides/gin.md)
- [gRPC](https://docs.sentry.io/platforms/go/guides/grpc.md)
- [Iris](https://docs.sentry.io/platforms/go/guides/iris.md)
- [net/http](https://docs.sentry.io/platforms/go/guides/http.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/go/guides/negroni/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/go/guides/negroni/usage.md)
- [Source Context](https://docs.sentry.io/platforms/go/guides/negroni/source-context.md)
- [Integrations](https://docs.sentry.io/platforms/go/guides/negroni/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/go/guides/negroni/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/go/guides/negroni/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/go/guides/negroni/tracing.md)
- [Logs](https://docs.sentry.io/platforms/go/guides/negroni/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/go/guides/negroni/metrics.md)
- [Crons](https://docs.sentry.io/platforms/go/guides/negroni/crons.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/go/guides/negroni/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/go/guides/negroni/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/go/guides/negroni/troubleshooting.md)

