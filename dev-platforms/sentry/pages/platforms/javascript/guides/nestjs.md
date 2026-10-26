---
title: "Nest.js"
source: https://docs.sentry.io/platforms/javascript/guides/nestjs.md
path: platforms/javascript/guides/nestjs
---

---
title: "Nest.js"
description: "Learn how to set up Sentry in your Nest.js app and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/nestjs/
---

# Sentry for Nest.js

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Node version `20.19.0` or above. Node.js 22 needs `22.12` or higher, while Node.js 23 needs `23.2` or higher (`>=20.19.0 <22.0.0 || >=22.12.0 <23.0.0 || >=23.2.0`).

## [Install](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
npm install @sentry/nestjs --save
```

*Other available variations of the above snippet: yarn, pnpm*

```bash
npm install @sentry/nestjs @sentry/profiling-node --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#5](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#send-logs) and [#6](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#send-application-metrics-). This guide also enables **Tracing** and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#initialize-the-sentry-sdk)

To import and initialize Sentry, create a file named `instrument.ts` in the root directory of your project and add the code snippet shown below.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/nestjs/configuration/options.md#tracesSampleRate)
* Profiling: via [`profileSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/nestjs/configuration/options.md#profileSessionSampleRate), [`profileLifecycle`](https://docs.sentry.io/platforms/javascript/guides/nestjs/configuration/options.md#profileLifecycle), and the profiling integration

Don't need a feature? Remove its integration and options from the snippet.

```typescript
import * as Sentry from "@sentry/nestjs";
import { nodeProfilingIntegration } from "@sentry/profiling-node";

// Ensure to call this before requiring any other modules!
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  integrations: [
    // enables Profiling
    nodeProfilingIntegration(),
  ],
  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
  // Enables Profiling for every session.
  profileSessionSampleRate: 1.0,
  profileLifecycle: "trace",
});
```

### [Apply Instrumentation to Your App](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#apply-instrumentation-to-your-app)

Make sure to import the `instrument.ts` file before any other modules:

```typescript
// Import this first!
import "./instrument";

// Now import other modules
import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}

bootstrap();
```

Afterward, add the `SentryModule` as a root module to your main module:

```typescript
import { Module } from "@nestjs/common";
import { SentryModule } from "@sentry/nestjs/setup";
import { AppController } from "./app.controller";
import { AppService } from "./app.service";

@Module({
  imports: [
    SentryModule.forRoot(),
    // ...other modules
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/nestjs/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/nestjs/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

## [Capture Nest.js Errors](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#capture-nestjs-errors)

By default, Sentry only captures unhandled exceptions that aren't caught by an error filter. Additionally, `HttpException`s (including [derivatives](https://docs.nestjs.com/exception-filters#built-in-http-exceptions)) aren't captured by default because they mostly act as control flow vehicles.

To make sure Sentry captures all your app's errors, configure error handling based on how your application manages exceptions:

### [Using a Custom Global Filter](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#using-a-custom-global-filter)

If you have a global catch-all exception filter, add a `@SentryExceptionCaptured()` decorator to the filter's `catch()` method:

```typescript
import { Catch, ExceptionFilter } from "@nestjs/common";
import { SentryExceptionCaptured } from "@sentry/nestjs";

@Catch()
export class YourCatchAllExceptionFilter implements ExceptionFilter {
  @SentryExceptionCaptured()
  catch(exception, host): void {
    // your implementation here
  }
}
```

### [Not Using a Custom Global Filter](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#not-using-a-custom-global-filter)

If you don't have a global catch-all exception filter, add the `SentryGlobalFilter` to the providers of your main module, **before** any other exception filters:

```typescript
import { Module } from "@nestjs/common";
import { APP_FILTER } from "@nestjs/core";
import { SentryGlobalFilter } from "@sentry/nestjs/setup";

@Module({
  providers: [
    {
      provide: APP_FILTER,
      useClass: SentryGlobalFilter,
    },
    // ..other providers
  ],
})
export class AppModule {}
```

### [Using Error Filters for Specific Exception Types](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#using-error-filters-for-specific-exception-types)

If you have error filters for specific types of exceptions (for example, `@Catch(HttpException)`) and you want to report these errors to Sentry, you need to capture them in the `catch()` handler using `Sentry.captureException()`:

```typescript
import { ArgumentsHost, BadRequestException, Catch } from "@nestjs/common";
import { BaseExceptionFilter } from "@nestjs/core";
import { ExampleException } from "./example.exception";
import * as Sentry from "@sentry/nestjs";

@Catch(ExampleException)
export class ExampleExceptionFilter extends BaseExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    Sentry.captureException(exception);
    return super.catch(new BadRequestException(exception.message), host);
  }
}
```

Are you using WebSockets?

`SentryGlobalFilter` handles WebSocket exceptions, but NestJS doesn't apply filters registered via `APP_FILTER` to WebSocket gateways. To make sure errors thrown in a gateway are captured, add the `@UseFilters()` decorator directly to the gateway class, even if `SentryGlobalFilter` is already registered as a global provider.

```typescript
import { UseFilters } from "@nestjs/common";
import { WebSocketGateway } from "@nestjs/websockets";
import { SentryGlobalFilter } from "@sentry/nestjs/setup";

@UseFilters(new SentryGlobalFilter())
@WebSocketGateway()
export class YourGateway {
  // ...your event handlers
}
```

Are you using Microservices?

If you're using `@nestjs/microservices` make sure to handle errors in RPC contexts correctly by providing your own `RpcExceptionFilter` (see [Nest.js Microservices documentation](https://docs.nestjs.com/microservices/exception-filters)). `SentryGlobalFilter` in a [hybrid application](https://docs.nestjs.com/faq/hybrid-application) doesn't extend `BaseRpcExceptionFilter` since this depends on `@nestjs/microservices`.

Use `Sentry.captureException(exception)` in your custom filter in case you want to send these errors to Sentry, as shown in the example on the right.

```typescript
import { Catch, RpcExceptionFilter, ArgumentsHost } from "@nestjs/common";
import { Observable, throwError } from "rxjs";
import { RpcException } from "@nestjs/microservices";
import * as Sentry from "@sentry/nestjs";

@Catch(RpcException)
export class ExceptionFilter implements RpcExceptionFilter<RpcException> {
  catch(exception: RpcException, host: ArgumentsHost): Observable<any> {
    Sentry.captureException(exception); // optional
    return throwError(() => exception.getError());
  }
}
```

## [Isolate Async Context for Background Jobs](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#isolate-async-context-for-background-jobs)

Sentry automatically isolates background jobs using `@Cron()`, `@Interval()`, `@Timeout()`, `@OnEvent()`, and BullMQ `@Processor()` handlers. For other background tasks, wrap your handlers with `Sentry.withIsolationScope()` to prevent breadcrumbs and tags from leaking into unrelated events. See [Isolate Background Job Scopes](https://docs.sentry.io/platforms/javascript/guides/nestjs/features/async-context.md) for details and code examples.

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/nestjs/logs.md) for all available logging methods and the syntax for formatting messages.

```javascript
Sentry.logger.info("User example action completed");

Sentry.logger.warn("Slow operation detected", {
  operation: "data_fetch",
  duration: 3500,
});

Sentry.logger.error("Validation failed", {
  form_field: "email",
  reason: "Invalid email",
});
```

If you're already logging with another library, use an integration to capture those logs as Sentry Logs automatically:

* [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/nestjs/logs.md#console-integration) for `console` calls
* [Consola](https://docs.sentry.io/platforms/javascript/guides/nestjs/logs.md#console-integration)
* [Pino](https://docs.sentry.io/platforms/javascript/guides/nestjs/configuration/integrations/pino.md)

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/nestjs/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

On Node.js, [`nodeRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nestjs/configuration/integrations/noderuntimemetrics.md) also collects runtime health metrics automatically.

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add an intentional error to a NestJS route handler and make a request to it:

```typescript
throw new Error("Sentry Test Error");
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page, select a transaction, and then a profile ID to view its flame graph. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/nestjs.md#next-steps)

At this point, you should have integrated Sentry into your Nest.js application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/nestjs/agent-tracing.md) to monitor your AI systems
* Extend Sentry to your frontend using one of our [frontend SDKs](https://docs.sentry.io/.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nestjs/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
- [Azure Functions](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md)
- [Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md)
- [Capacitor](https://docs.sentry.io/platforms/javascript/guides/capacitor.md)
- [Cloud Functions for Firebase](https://docs.sentry.io/platforms/javascript/guides/firebase.md)
- [Cloudflare](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md)
- [Cordova](https://docs.sentry.io/platforms/javascript/guides/cordova.md)
- [Deno](https://docs.sentry.io/platforms/javascript/guides/deno.md)
- [Effect](https://docs.sentry.io/platforms/javascript/guides/effect.md)
- [Electron](https://docs.sentry.io/platforms/javascript/guides/electron.md)
- [Elysia](https://docs.sentry.io/platforms/javascript/guides/elysia.md)
- [Ember](https://docs.sentry.io/platforms/javascript/guides/ember.md)
- [Eve](https://docs.sentry.io/platforms/javascript/guides/eve.md)
- [Express](https://docs.sentry.io/platforms/javascript/guides/express.md)
- [Fastify](https://docs.sentry.io/platforms/javascript/guides/fastify.md)
- [Flue](https://docs.sentry.io/platforms/javascript/guides/flue.md)
- [Gatsby](https://docs.sentry.io/platforms/javascript/guides/gatsby.md)
- [Google Cloud Functions](https://docs.sentry.io/platforms/javascript/guides/gcp-functions.md)
- [Hapi](https://docs.sentry.io/platforms/javascript/guides/hapi.md)
- [Hono](https://docs.sentry.io/platforms/javascript/guides/hono.md)
- [Koa](https://docs.sentry.io/platforms/javascript/guides/koa.md)
- [Mastra](https://docs.sentry.io/platforms/javascript/guides/mastra.md)
- [Next.js](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)
- [Nitro](https://docs.sentry.io/platforms/javascript/guides/nitro.md)
- [Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md)
- [Nuxt](https://docs.sentry.io/platforms/javascript/guides/nuxt.md)
- [Pi Durable](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md)
- [React](https://docs.sentry.io/platforms/javascript/guides/react.md)
- [React Router Framework](https://docs.sentry.io/platforms/javascript/guides/react-router.md)
- [Remix](https://docs.sentry.io/platforms/javascript/guides/remix.md)
- [Solid](https://docs.sentry.io/platforms/javascript/guides/solid.md)
- [SolidStart](https://docs.sentry.io/platforms/javascript/guides/solidstart.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [TanStack Start React](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/nestjs/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/nestjs/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/nestjs/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/nestjs/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/nestjs/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/nestjs/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/nestjs/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/nestjs/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/nestjs/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/nestjs/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/nestjs/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/nestjs/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/nestjs/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/nestjs/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/nestjs/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/nestjs/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/nestjs/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/nestjs/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nestjs/troubleshooting.md)
- [NestJS Features](https://docs.sentry.io/platforms/javascript/guides/nestjs/features.md)

