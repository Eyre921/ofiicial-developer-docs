---
title: "Servlet"
source: https://docs.sentry.io/platforms/java/guides/servlet.md
path: platforms/java/guides/servlet
---

---
title: "Servlet"
description: "Learn how to set up Sentry in your Servlet-based Java application and capture your first events."
url: https://docs.sentry.io/platforms/java/guides/servlet/
---

# Sentry for Servlet

Sentry's Java SDK enables capturing sessions for Release health as well as reporting messages and errors.

Sentry for Java is a collection of modules provided by Sentry. At its core, Sentry for Java provides a raw client for sending events to Sentry. To begin, we **highly recommend** you use one of the logging libraries or framework integrations.

The Sentry Java SDK can be used with Kotlin, Scala, and other JVM languages. Code examples are typically provided in both Java and Kotlin.

## [Prerequisites](https://docs.sentry.io/platforms/java/guides/servlet.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Java version `8` (also known as Java `1.8`) or above

## [Install](https://docs.sentry.io/platforms/java/guides/servlet.md#install)

Install the Sentry SDK for your Java logging framework or application:

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-servlet</artifactId>
    <version>8.65.0</version>
</dependency>
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-async-profiler</artifactId>
    <version>8.65.0</version>
</dependency>
```

*Other available variations of the above snippet: Gradle, SBT*

For other dependency managers, see the [central Maven repository](https://search.maven.org/artifact/io.sentry/sentry-servlet).

`sentry-servlet` module comes with a `ServletContainerInitializer` that registers a `ServletRequestListener` which enhances each Sentry event triggered within the scope of HTTP request with a request information like HTTP method, query string, url and HTTP headers.

If you are using multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

### [Jakarta support](https://docs.sentry.io/platforms/java/guides/servlet.md#jakarta-support)

We also provide a module called `sentry-servlet-jakarta` if you want to use `jakarta.servlet-api` instead of `javax.servlet-api`.

## [Configure](https://docs.sentry.io/platforms/java/guides/servlet.md#configure)

**Error Monitoring** starts once Sentry is configured. **Application Metrics** need no extra configuration, and you'll learn how to send them in step [#4](https://docs.sentry.io/platforms/java/guides/servlet.md#send-application-metrics-). This guide also configures **Tracing**, **Logs**, and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

Don't need a feature? Remove its configuration from the SDK initialization. To disable Profiling, also remove the `sentry-async-profiler` dependency. Profiling is not supported on Windows.

### [With OpenTelemetry](https://docs.sentry.io/platforms/java/guides/servlet.md#with-opentelemetry)

Sentry's OpenTelemetry agent attaches when the JVM starts and is configured through a `sentry.properties` file.

Download the latest version of the `sentry-opentelemetry-agent-8.65.0.jar` from [MavenCentral](https://search.maven.org/artifact/io.sentry/sentry-opentelemetry-agent):

```bash
curl https://repo1.maven.org/maven2/io/sentry/sentry-opentelemetry-agent/8.65.0/sentry-opentelemetry-agent-8.65.0.jar -o sentry-opentelemetry-agent-8.65.0.jar
```

The SDK can be configured using a `sentry.properties` file.

The snippet also turns on:

* Tracing: via [`traces-sample-rate`](https://docs.sentry.io/platforms/java/guides/servlet/configuration/options.md#tracesSampleRate)
* Profiling: via [`profile-session-sample-rate`](https://docs.sentry.io/platforms/java/guides/servlet/configuration/options.md#profileSessionSampleRate) and [`profile-lifecycle`](https://docs.sentry.io/platforms/java/guides/servlet/configuration/options.md#profileLifecycle)
* Data Collection: via [`data-collection`](https://docs.sentry.io/platforms/java/guides/servlet/data-management/data-collected.md)
* Logs: via [`logs.enabled`](https://docs.sentry.io/platforms/java/guides/servlet/logs.md)

```properties
dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>
# Use Data Collection defaults but don't collect automatic user information.
data-collection.user-info=false
# Configure other data categories here.

# Enable tracing
traces-sample-rate=1.0

# Enable logs
logs.enabled=true

# Enable profiling
profile-session-sample-rate=1.0
profile-lifecycle=TRACE
```

Then run your application with:

```bash
SENTRY_PROPERTIES_FILE=sentry.properties JAVA_TOOL_OPTIONS="-javaagent:sentry-opentelemetry-agent-8.65.0.jar" java -jar your-application.jar
```

*Other available variations of the above snippet: Java CLI argument*

See the [agent setup guide](https://docs.sentry.io/platforms/java/opentelemetry/setup/agent.md) or [agentless setup guide](https://docs.sentry.io/platforms/java/opentelemetry/setup/agentless.md) for details.

### [Without OpenTelemetry](https://docs.sentry.io/platforms/java/guides/servlet.md#without-opentelemetry)

Configuration should happen as early as possible in your application's lifecycle. The following example configures a `SentryInitializer` servlet container initializer that initializes Sentry on application startup.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/java/guides/servlet/configuration/options.md#tracesSampleRate)
* Profiling: via [`profileSessionSampleRate`](https://docs.sentry.io/platforms/java/guides/servlet/configuration/options.md#profileSessionSampleRate) and [`profileLifecycle`](https://docs.sentry.io/platforms/java/guides/servlet/configuration/options.md#profileLifecycle)
* Data Collection: via [`dataCollection`](https://docs.sentry.io/platforms/java/guides/servlet/data-management/data-collected.md)
* Logs: via [`logs.enabled`](https://docs.sentry.io/platforms/java/guides/servlet/logs.md)

```java
package sentry.sample;

import io.sentry.ProfileLifecycle;
import io.sentry.Sentry;
import javax.servlet.ServletContainerInitializer;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;

public final class SentryInitializer implements ServletContainerInitializer {

  @Override
  public void onStartup(Set<Class<?>> c, ServletContext ctx) throws ServletException {
    Sentry.init(options -> {
      options.setDsn("https://<key>@o<orgId>.ingest.sentry.io/<projectId>");

      // Use Data Collection defaults but don't collect automatic user information.
      options.getDataCollection().forceDataCollection();
      options.getDataCollection().setUserInfo(false);
      // Configure other data categories here.

      // Set traces_sample_rate to 1.0 to capture 100%
      // of transactions for tracing.
      // We recommend adjusting this value in production.
      options.setTracesSampleRate(1.0);

      // Enable profiling
      options.setProfileSessionSampleRate(1.0);
      options.setProfileLifecycle(ProfileLifecycle.TRACE);

      // Enable logs
      options.getLogs().setEnabled(true);
    });
  }
}
```

*Other available variations of the above snippet: kotlin*

Learn more about setting up logging in our [Logs documentation](https://docs.sentry.io/platforms/java/logs.md).

Create a file in `src/main/resources/META-INF/services` named `javax.servlet.ServletContainerInitializer`, with a full name of your custom `SentryInitializer` class as a content:

```properties
sentry.sample.SentryInitializer
```

## [Send Logs](https://docs.sentry.io/platforms/java/guides/servlet.md#send-logs)

Use `Sentry.logger()` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/java/guides/servlet/logs.md) for all available logging methods and the syntax for formatting messages.

```java
import io.sentry.Sentry;
import io.sentry.SentryAttribute;
import io.sentry.SentryAttributes;
import io.sentry.SentryLogLevel;
import io.sentry.logger.SentryLogParameters;


Sentry.logger().info("A simple log message");
Sentry.logger().error("A %s log message", "formatted");

// attach custom attributes with Sentry.logger().log()
Sentry.logger().log(
    SentryLogLevel.FATAL,
    SentryLogParameters.create(
        SentryAttributes.of(
            SentryAttribute.stringAttribute("my.string-attribute", "some-value"),
            SentryAttribute.named("my.attribute", new Point(1, 2))
        )
    ),
    "log message %s",
    "param1"
);
```

*Other available variations of the above snippet: kotlin*

We also provide integrations for:

* [Logback](https://docs.sentry.io/platforms/java/guides/logback/logs.md)
* [Log4j2](https://docs.sentry.io/platforms/java/guides/log4j2/logs.md)
* [java.util.logging](https://docs.sentry.io/platforms/java/guides/jul/logs.md)

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/java/guides/servlet.md#send-application-metrics-)

Use `Sentry.metrics()` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later.

See [Set Up Metrics](https://docs.sentry.io/platforms/java/guides/servlet/metrics.md) for all metric types and configuration options.

```java
import io.sentry.Sentry;
import io.sentry.SentryAttribute;
import io.sentry.SentryAttributes;
import io.sentry.metrics.MetricsUnit;
import io.sentry.metrics.SentryMetricsParameters;

Sentry.metrics().count("button_click", 1.0);
Sentry.metrics().gauge("queue_depth", 42.0);

// pass additional attributes via SentryMetricsParameters
Sentry.metrics().distribution(
  "response_time",
  1.0,
  MetricsUnit.Duration.MILLISECOND,
  SentryMetricsParameters.create(
    SentryAttributes.of(
      SentryAttribute.stringAttribute("browser", "Firefox")
    )
  )
);
```

*Other available variations of the above snippet: kotlin*

## [Verify Your Setup](https://docs.sentry.io/platforms/java/guides/servlet.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add this intentional error to your application:

```java
import io.sentry.Sentry;

try {
  throw new Exception("This is a test.");
} catch (Exception e) {
  Sentry.captureException(e);
}
```

*Other available variations of the above snippet: Kotlin*

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/java/guides/servlet.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/java/guides/servlet.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

Are you having problems setting up the SDK or integration?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/java/guides/servlet/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other Java Frameworks

- [java.util.logging](https://docs.sentry.io/platforms/java/guides/jul.md)
- [Log4j 2.x](https://docs.sentry.io/platforms/java/guides/log4j2.md)
- [Logback](https://docs.sentry.io/platforms/java/guides/logback.md)
- [Spring](https://docs.sentry.io/platforms/java/guides/spring.md)
- [Spring Boot](https://docs.sentry.io/platforms/java/guides/spring-boot.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/java/guides/servlet/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/java/guides/servlet/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/java/guides/servlet/configuration.md)
- [Logs](https://docs.sentry.io/platforms/java/guides/servlet/logs.md)
- [Integrations](https://docs.sentry.io/platforms/java/guides/servlet/integrations.md)
- [Tracing](https://docs.sentry.io/platforms/java/guides/servlet/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/java/guides/servlet/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/java/guides/servlet/data-management.md)
- [Profiling](https://docs.sentry.io/platforms/java/guides/servlet/profiling.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/java/guides/servlet/security-policy-reporting.md)
- [Crons](https://docs.sentry.io/platforms/java/guides/servlet/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/java/guides/servlet/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/java/guides/servlet/feature-flags.md)
- [Source Context](https://docs.sentry.io/platforms/java/guides/servlet/source-context.md)
- [Gradle](https://docs.sentry.io/platforms/java/guides/servlet/gradle.md)
- [Maven](https://docs.sentry.io/platforms/java/guides/servlet/maven.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/java/guides/servlet/opentelemetry.md)
- [Migration Guides](https://docs.sentry.io/platforms/java/guides/servlet/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/java/guides/servlet/troubleshooting.md)
- [Legacy SDK (1.7)](https://docs.sentry.io/platforms/java/guides/servlet/legacy.md)

