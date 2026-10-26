---
title: "gRPC"
source: https://docs.sentry.io/platforms/go/guides/grpc.md
path: platforms/go/guides/grpc
---

---
title: "gRPC"
description: "Learn how to add Sentry to a Go gRPC server or client using interceptors."
url: https://docs.sentry.io/platforms/go/guides/grpc/
---

# Sentry for gRPC

For a quick reference, there is a [complete example](https://github.com/getsentry/sentry-go/tree/master/_examples/grpc) at the Go SDK source code repository.

[Go Dev-style API documentation](https://pkg.go.dev/github.com/getsentry/sentry-go/grpc) is also available.

## [Install](https://docs.sentry.io/platforms/go/guides/grpc.md#install)

```bash
go get github.com/getsentry/sentry-go
go get github.com/getsentry/sentry-go/grpc
```

## [Configure](https://docs.sentry.io/platforms/go/guides/grpc.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/go/guides/grpc.md#initialize-the-sentry-sdk)

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

### [Server Options](https://docs.sentry.io/platforms/go/guides/grpc.md#server-options)

`sentrygrpc` accepts a struct of `ServerOptions` that allows you to configure how the server interceptors behave.

```go
// Whether Sentry should repanic after recovery. In most cases it should be set to true,
// so that your own recovery middleware or gRPC's default handling can respond to the client.
Repanic bool
// Whether to wait for Sentry to deliver the event before returning.
// Useful when Repanic is true and the process may exit or restart after the panic.
WaitForDelivery bool
// Timeout for the event delivery requests.
Timeout time.Duration
```

## [Server-Side Usage](https://docs.sentry.io/platforms/go/guides/grpc.md#server-side-usage)

Attach the unary and stream interceptors when creating your gRPC server:

```go
import (
	"fmt"
	"net"

	"google.golang.org/grpc"

	"github.com/getsentry/sentry-go"
	sentrygrpc "github.com/getsentry/sentry-go/grpc"
)

func main() {
	if err := sentry.Init(sentry.ClientOptions{
		Dsn:              "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
		TracesSampleRate: 1.0,
	}); err != nil {
		fmt.Printf("Sentry initialization failed: %v\n", err)
	}
	defer sentry.Flush(2 * time.Second)

	server := grpc.NewServer(
		grpc.UnaryInterceptor(sentrygrpc.UnaryServerInterceptor(sentrygrpc.ServerOptions{
			Repanic: true,
		})),
		grpc.StreamInterceptor(sentrygrpc.StreamServerInterceptor(sentrygrpc.ServerOptions{
			Repanic: true,
		})),
	)

	listener, err := net.Listen("tcp", ":50051")
	if err != nil {
		sentry.CaptureException(err)
		return
	}

	if err := server.Serve(listener); err != nil {
		sentry.CaptureException(err)
	}
}
```

The server interceptors automatically:

* Create a transaction for each unary or streaming RPC call.
* Recover from panics in handlers and report them to Sentry.
* Continue distributed traces from upstream clients via `sentry-trace` and `baggage` metadata.
* Attach an isolated `*sentry.Hub` to the handler's context.

## [Client-Side Usage](https://docs.sentry.io/platforms/go/guides/grpc.md#client-side-usage)

Attach the unary and stream interceptors when creating your gRPC client:

```go
import (
	"context"
	"fmt"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	"github.com/getsentry/sentry-go"
	sentrygrpc "github.com/getsentry/sentry-go/grpc"
)

func main() {
	if err := sentry.Init(sentry.ClientOptions{
		Dsn:              "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
		TracesSampleRate: 1.0,
	}); err != nil {
		fmt.Printf("Sentry initialization failed: %v\n", err)
	}
	defer sentry.Flush(2 * time.Second)

	conn, err := grpc.NewClient(
		"localhost:50051",
		grpc.WithTransportCredentials(insecure.NewCredentials()),
		grpc.WithUnaryInterceptor(sentrygrpc.UnaryClientInterceptor()),
		grpc.WithStreamInterceptor(sentrygrpc.StreamClientInterceptor()),
	)
	if err != nil {
		sentry.CaptureException(err)
		return
	}
	defer conn.Close()
}
```

The client interceptors automatically:

* Create a child span for each outgoing RPC call.
* Inject `sentry-trace` and `baggage` headers into gRPC metadata for distributed tracing.
* Set the span status based on the returned gRPC status code.

## [Usage](https://docs.sentry.io/platforms/go/guides/grpc.md#usage)

Both interceptors make a `*sentry.Hub` available on the request context, which you can retrieve using `sentry.GetHubFromContext()` in your handlers. Use this hub-bound API instead of the global `sentry.CaptureMessage` or `sentry.CaptureException` calls to keep data separated between concurrent requests.

```go
func (s *server) YourMethod(ctx context.Context, req *pb.YourRequest) (*pb.YourResponse, error) {
	if hub := sentry.GetHubFromContext(ctx); hub != nil {
		hub.WithScope(func(scope *sentry.Scope) {
			scope.SetTag("request_id", req.GetId())
			hub.CaptureMessage("Handling request")
		})
	}
	return &pb.YourResponse{}, nil
}
```

## [Next Steps](https://docs.sentry.io/platforms/go/guides/grpc.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Go Frameworks

- [Echo](https://docs.sentry.io/platforms/go/guides/echo.md)
- [FastHTTP](https://docs.sentry.io/platforms/go/guides/fasthttp.md)
- [Fiber](https://docs.sentry.io/platforms/go/guides/fiber.md)
- [Fiber v3](https://docs.sentry.io/platforms/go/guides/fiberv3.md)
- [Gin](https://docs.sentry.io/platforms/go/guides/gin.md)
- [Iris](https://docs.sentry.io/platforms/go/guides/iris.md)
- [Negroni](https://docs.sentry.io/platforms/go/guides/negroni.md)
- [net/http](https://docs.sentry.io/platforms/go/guides/http.md)

## Topics

- [Extended Configuration](https://docs.sentry.io/platforms/go/guides/grpc/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/go/guides/grpc/usage.md)
- [Source Context](https://docs.sentry.io/platforms/go/guides/grpc/source-context.md)
- [Integrations](https://docs.sentry.io/platforms/go/guides/grpc/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/go/guides/grpc/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/go/guides/grpc/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/go/guides/grpc/tracing.md)
- [Logs](https://docs.sentry.io/platforms/go/guides/grpc/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/go/guides/grpc/metrics.md)
- [Crons](https://docs.sentry.io/platforms/go/guides/grpc/crons.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/go/guides/grpc/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/go/guides/grpc/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/go/guides/grpc/troubleshooting.md)

