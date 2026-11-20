---
title: "Spring"
source: https://docs.sentry.io/platforms/java/guides/spring.md
path: platforms/java/guides/spring
---

---
title: "Spring"
description: "Learn how to set up Sentry in your Spring application and capture your first events."
url: https://docs.sentry.io/platforms/java/guides/spring/
---

# Sentry for Spring

Are you using Spring Boot? Then follow our [Spring Boot quick start guide](https://docs.sentry.io/platforms/java/guides/spring-boot.md) instead.

## [Prerequisites](https://docs.sentry.io/platforms/java/guides/spring.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Spring Framework `5.1.2`+
  * [Sentry WebFlux integration](https://docs.sentry.io/platforms/java/guides/spring-boot/webflux.md) requires Spring Framework `5.2.4` or above

If you're on an older version, use [our legacy integration](https://docs.sentry.io/platforms/java/legacy/spring.md).

## [Install](https://docs.sentry.io/platforms/java/guides/spring.md#install)

Install Sentry for your Spring version:

**Gradle Plugin**

```groovy
plugins {
  id "io.sentry.jvm.gradle" version "6.27.0"
}
dependencies {
  implementation 'io.sentry:sentry-async-profiler:8.65.0'
}
```

**\[Maven Plugin] pom.xml**

```xml
<plugin>
  <groupId>io.sentry</groupId>
  <artifactId>sentry-maven-plugin</artifactId>
  <version>0.12.0</version>
  <!-- Required to allow auto-install of Sentry SDK and Integrations -->
  <extensions>true</extensions>
  <configuration>
    <!-- In case you're self hosting, provide the URL here -->
    <!-- <url>http://localhost:8000/</url> -->
    <org>___SENTRY_ORG_SLUG___</org>
    <project>___SENTRY_PROJECT_SLUG___</project>
    <!-- Do not commit your auth token with this file, you should provide it via the SENTRY_AUTH_TOKEN environment variable or similar -->
    <!-- <authToken>${env.SENTRY_AUTH_TOKEN}</authToken> -->
    <authToken>___SENTRY_AUTH_TOKEN___</authToken>
    <!-- Enable debugging to see logs in case something goes wrong when uploading the source bundle -->
    <debugSentryCli>true</debugSentryCli>
   </configuration>
   <executions>
    <execution>
      <goals>
        <!-- Generates a source bundle and uploads it to Sentry -->
        <!-- This enables source context, allowing you to see your source code as part of your stack traces in Sentry -->
        <!-- Learn more about this feature in its dedicated "Source Context" docs page -->
        <goal>uploadSourceBundle</goal>
        <!--  Validates Sentry SDK dependency versions. -->
        <!--  Mixing SDK dependency versions can result in build or run time errors. -->
        <!--  If mixed versions are detected, the build will fail. -->
        <goal>validateSdkDependencyVersions</goal>
      </goals>
    </execution>
  </executions>
</plugin>
<dependencies>
  <dependency>
      <groupId>io.sentry</groupId>
      <artifactId>sentry-async-profiler</artifactId>
      <version>8.65.0</version>
  </dependency>
</dependencies>
```

**Gradle (Spring 5)**

```groovy
implementation 'io.sentry:sentry-spring:8.65.0'
implementation 'io.sentry:sentry-async-profiler:8.65.0'
```

**Gradle (Spring 6)**

```groovy
implementation 'io.sentry:sentry-spring-jakarta:8.65.0'
implementation 'io.sentry:sentry-async-profiler:8.65.0'
```

**Gradle (Spring 7)**

```groovy
implementation 'io.sentry:sentry-spring-7:8.65.0'
implementation 'io.sentry:sentry-async-profiler:8.65.0'
```

**Maven (Spring 5)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring</artifactId>
    <version>8.65.0</version>
</dependency>
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-async-profiler</artifactId>
    <version>8.65.0</version>
</dependency>
```

**Maven (Spring 6)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring-jakarta</artifactId>
    <version>8.65.0</version>
</dependency>
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-async-profiler</artifactId>
    <version>8.65.0</version>
</dependency>
```

**Maven (Spring 7)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring-7</artifactId>
    <version>8.65.0</version>
</dependency>
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-async-profiler</artifactId>
    <version>8.65.0</version>
</dependency>
```

**SBT (Spring 5)**

```scala
libraryDependencies += "io.sentry" % "sentry-spring" % "8.65.0"
libraryDependencies += "io.sentry" % "sentry-async-profiler" % "8.65.0"
```

**SBT (Spring 6)**

```scala
libraryDependencies += "io.sentry" % "sentry-spring-jakarta" % "8.65.0"
libraryDependencies += "io.sentry" % "sentry-async-profiler" % "8.65.0"
```

**SBT (Spring 7)**

```scala
libraryDependencies += "io.sentry" % "sentry-spring-7" % "8.65.0"
libraryDependencies += "io.sentry" % "sentry-async-profiler" % "8.65.0"
```

For other dependency managers see the [central Maven repository (Spring 5)](https://search.maven.org/artifact/io.sentry/sentry-spring), [central Maven repository (Spring 6)](https://search.maven.org/artifact/io.sentry/sentry-spring-jakarta), and [central Maven repository (Spring 7)](https://search.maven.org/artifact/io.sentry/sentry-spring-7).

We recommend using our Gradle plugin as it can add integrations and provide source context for events.

If you are manually adding multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

## [Configure](https://docs.sentry.io/platforms/java/guides/spring.md#configure)

**Error Monitoring** starts once Sentry is configured. **Application Metrics** need no extra configuration, and you'll learn how to send them in step [#4](https://docs.sentry.io/platforms/java/guides/spring.md#send-application-metrics-). This guide also configures **Tracing**, **Logs**, and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

Configuration should happen as early as possible in your application's lifecycle.

The `sentry-spring`, `sentry-spring-jakarta`, and `sentry-spring-7` libraries provide an `@EnableSentry` annotation that registers all required Spring beans. Place it on any class annotated with [@Configuration](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/context/annotation/Configuration.html), including your main [@SpringBootApplication](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/autoconfigure/SpringBootApplication.html) class.

**Java (Spring 5)**

```java
import io.sentry.spring.EnableSentry;
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
)
@Configuration
class SentryConfiguration {
}
```

**Java (Spring 6)**

```java
import io.sentry.spring.jakarta.EnableSentry;
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
)
@Configuration
class SentryConfiguration {
}
```

**Java (Spring 7)**

```java
import io.sentry.spring7.EnableSentry;
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
)
@Configuration
class SentryConfiguration {
}
```

**Kotlin (Spring 5)**

```kotlin
import io.sentry.spring.EnableSentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
)
@Configuration
class SentryConfiguration
```

**Kotlin (Spring 6)**

```kotlin
import io.sentry.spring.jakarta.EnableSentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
)
@Configuration
class SentryConfiguration
```

**Kotlin (Spring 7)**

```kotlin
import io.sentry.spring7.EnableSentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
)
@Configuration
class SentryConfiguration
```

Then configure the remaining options in `sentry.properties`.

The snippet also configures:

* Data Collection: via [`data-collection`](https://docs.sentry.io/platforms/java/guides/spring/data-management/data-collected.md)
* Tracing: via [`traces-sample-rate`](https://docs.sentry.io/platforms/java/guides/spring/configuration/options.md#tracesSampleRate)
* Profiling: via [`profile-session-sample-rate`](https://docs.sentry.io/platforms/java/guides/spring/configuration/options.md#profileSessionSampleRate) and [`profile-lifecycle`](https://docs.sentry.io/platforms/java/guides/spring/configuration/options.md#profileLifecycle)
* Logs: via [`logs.enabled`](https://docs.sentry.io/platforms/java/guides/spring/logs.md)

Don't need a feature? Remove its configuration. Remove the `sentry-async-profiler` dependency to disable Profiling.

```properties
# Use Data Collection defaults but don't collect automatic user information.
data-collection.user-info=false
# Configure other data categories here.

# Enable tracing
traces-sample-rate=1.0

# Enable profiling
profile-session-sample-rate=1.0
profile-lifecycle=TRACE

# Enable logs
logs.enabled=true
```

The DSN can also come from the `sentry.dsn` system property, the `SENTRY_DSN` environment variable, or `sentry.properties`. See the [configuration page](https://docs.sentry.io/platforms/java/configuration.md) for details on external configuration.

### [Capture Handled Exceptions](https://docs.sentry.io/platforms/java/guides/spring.md#capture-handled-exceptions)

By default, only unhandled exceptions are sent to Sentry. You can tune this behavior by configuring the `exceptionResolverOrder` property. For example, setting it to `Ordered#HIGHEST_PRECEDENCE` ensures exceptions that have been handled by exception resolvers with higher order are sent to Sentry – including ones handled by `@ExceptionHandler` annotated methods.

**Java (Spring 5)**

```java
import io.sentry.spring.EnableSentry;
import org.springframework.core.Ordered;
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  exceptionResolverOrder = Ordered.LOWEST_PRECEDENCE
)
class SentryConfiguration {
}
```

**Java (Spring 6)**

```java
import io.sentry.spring.jakarta.EnableSentry;
import org.springframework.core.Ordered;
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  exceptionResolverOrder = Ordered.LOWEST_PRECEDENCE
)
class SentryConfiguration {
}
```

**Java (Spring 7)**

```java
import io.sentry.spring7.EnableSentry;
import org.springframework.core.Ordered;
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  exceptionResolverOrder = Ordered.LOWEST_PRECEDENCE
)
class SentryConfiguration {
}
```

**Kotlin (Spring 5)**

```kotlin
import io.sentry.spring.EnableSentry
import org.springframework.core.Ordered
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  exceptionResolverOrder = Ordered.LOWEST_PRECEDENCE
)
class SentryConfiguration
```

**Kotlin (Spring 6)**

```kotlin
import io.sentry.spring.jakarta.EnableSentry
import org.springframework.core.Ordered
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  exceptionResolverOrder = Ordered.LOWEST_PRECEDENCE
)
class SentryConfiguration
```

**Kotlin (Spring 7)**

```kotlin
import io.sentry.spring7.EnableSentry
import org.springframework.core.Ordered
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  exceptionResolverOrder = Ordered.LOWEST_PRECEDENCE
)
class SentryConfiguration
```

### [Add the OpenTelemetry Agent (Optional)](https://docs.sentry.io/platforms/java/guides/spring.md#add-the-opentelemetry-agent-optional)

[Sentry's OpenTelemetry](https://docs.sentry.io/platforms/java/guides/spring/opentelemetry.md) support lets Sentry use OpenTelemetry instrumentation to trace your application. Sentry's agent attaches when the JVM starts. Your configuration stays the same, but Sentry is still initialized by `@EnableSentry`, so set `SENTRY_AUTO_INIT=false` to stop the agent from initializing it as well.

Download the latest version of the `sentry-opentelemetry-agent-8.65.0.jar` from [MavenCentral](https://search.maven.org/artifact/io.sentry/sentry-opentelemetry-agent):

```bash
curl https://repo1.maven.org/maven2/io/sentry/sentry-opentelemetry-agent/8.65.0/sentry-opentelemetry-agent-8.65.0.jar -o sentry-opentelemetry-agent-8.65.0.jar
```

Then run your application with:

```bash
SENTRY_AUTO_INIT=false JAVA_TOOL_OPTIONS="-javaagent:sentry-opentelemetry-agent-8.65.0.jar" java -jar your-application.jar
```

*Other available variations of the above snippet: Java CLI argument*

If you run a `.WAR` file on an application server, add the agent to the server's `JAVA_OPTS` instead:

```bash
JAVA_OPTS="${JAVA_OPTS} JAVA_TOOL_OPTIONS="-javaagent:sentry-opentelemetry-agent-8.65.0.jar"
```

*Other available variations of the above snippet: Java CLI argument*

See the [agent setup guide](https://docs.sentry.io/platforms/java/guides/spring/opentelemetry/setup/agent.md) or [agentless setup guide](https://docs.sentry.io/platforms/java/guides/spring/opentelemetry/setup/agentless.md) for details.

## [Send Logs](https://docs.sentry.io/platforms/java/guides/spring.md#send-logs)

Use `Sentry.logger()` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/java/guides/spring/logs.md) for all available logging methods and the syntax for formatting messages.

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

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/java/guides/spring.md#send-application-metrics-)

Use `Sentry.metrics()` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later.

See [Set Up Metrics](https://docs.sentry.io/platforms/java/guides/spring/metrics.md) for all metric types and configuration options.

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

## [Verify Your Setup](https://docs.sentry.io/platforms/java/guides/spring.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/java/guides/spring.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/java/guides/spring.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

Are you having problems setting up the SDK or integration?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/java/guides/spring/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other Java Frameworks

- [java.util.logging](https://docs.sentry.io/platforms/java/guides/jul.md)
- [Log4j 2.x](https://docs.sentry.io/platforms/java/guides/log4j2.md)
- [Logback](https://docs.sentry.io/platforms/java/guides/logback.md)
- [Servlet](https://docs.sentry.io/platforms/java/guides/servlet.md)
- [Spring Boot](https://docs.sentry.io/platforms/java/guides/spring-boot.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/java/guides/spring/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/java/guides/spring/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/java/guides/spring/configuration.md)
- [Logs](https://docs.sentry.io/platforms/java/guides/spring/logs.md)
- [Integrations](https://docs.sentry.io/platforms/java/guides/spring/integrations.md)
- [Tracing](https://docs.sentry.io/platforms/java/guides/spring/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/java/guides/spring/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/java/guides/spring/data-management.md)
- [Async Methods](https://docs.sentry.io/platforms/java/guides/spring/async.md)
- [Record User Information](https://docs.sentry.io/platforms/java/guides/spring/advanced-usage.md)
- [Profiling](https://docs.sentry.io/platforms/java/guides/spring/profiling.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/java/guides/spring/security-policy-reporting.md)
- [Crons](https://docs.sentry.io/platforms/java/guides/spring/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/java/guides/spring/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/java/guides/spring/feature-flags.md)
- [Source Context](https://docs.sentry.io/platforms/java/guides/spring/source-context.md)
- [Gradle](https://docs.sentry.io/platforms/java/guides/spring/gradle.md)
- [Maven](https://docs.sentry.io/platforms/java/guides/spring/maven.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/java/guides/spring/opentelemetry.md)
- [Migration Guides](https://docs.sentry.io/platforms/java/guides/spring/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/java/guides/spring/troubleshooting.md)
- [Legacy SDK (1.7)](https://docs.sentry.io/platforms/java/guides/spring/legacy.md)

