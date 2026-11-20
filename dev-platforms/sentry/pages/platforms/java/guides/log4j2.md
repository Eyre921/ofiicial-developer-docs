---
title: "Log4j 2.x"
source: https://docs.sentry.io/platforms/java/guides/log4j2.md
path: platforms/java/guides/log4j2
---

---
title: "Log4j 2.x"
description: "Learn how to set up Sentry's Log4j 2.x integration to capture logs."
url: https://docs.sentry.io/platforms/java/guides/log4j2/
---

# Sentry for Log4j 2.x

The `sentry-log4j2` library provides [Log4j 2.x](https://logging.apache.org/log4j/2.x/) support for Sentry via an [Appender](https://logging.apache.org/log4j/2.x/log4j-core/apidocs/org/apache/logging/log4j/core/Appender.html) that sends logged exceptions to Sentry. You can find the source [on GitHub](https://github.com/getsentry/sentry-java/tree/master/sentry-log4j2).

## [Prerequisites](https://docs.sentry.io/platforms/java/guides/log4j2.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Java version `8` (also known as Java `1.8`) or above

## [Install](https://docs.sentry.io/platforms/java/guides/log4j2.md#install)

Add `sentry-log4j2` to your project (Maven Plugin and Gradle Plugin automatically add integrations for you):

**\[Maven Plugin] pom.xml**

```xml
<plugin>
  <groupId>io.sentry</groupId>
  <artifactId>sentry-maven-plugin</artifactId>
  <version>0.12.0</version>
  <!-- Required to allow auto-install of Sentry SDK and Integrations, including log4j2 -->
  <extensions>true</extensions>
  <configuration>
    <!-- your configuration -->
   </configuration>
   <executions>
    <!-- your executions -->
  </executions>
</plugin>
<dependencies>
  <!-- your dependencies -->
</dependencies>
```

**Maven**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-log4j2</artifactId>
    <version>8.65.0</version>
</dependency>
```

**Gradle Plugin**

```groovy
plugins {
  id "io.sentry.jvm.gradle" version "6.27.0"
}
```

**Gradle**

```groovy
implementation 'io.sentry:sentry-log4j2:8.65.0'
```

**SBT**

```scala
libraryDependencies += "io.sentry" % "sentry-log4j2" % "8.65.0"
```

For other dependency managers see the [central Maven repository](https://search.maven.org/artifact/io.sentry/sentry-log4j2).

We recommend using our Gradle plugin as it can add integrations and provide source context for events.

If you are manually adding multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

## [Configure](https://docs.sentry.io/platforms/java/guides/log4j2.md#configure)

Add the `Sentry` appender to your `log4j2.xml`.

Make sure to set the DSN in one place only:

* Use the snippet in the "Without DSN" code box tab if Sentry is already initialized in your application. This is the case if you call [`Sentry.init`](https://docs.sentry.io/platforms/java.md) in your code, use the [Spring](https://docs.sentry.io/platforms/java/guides/spring.md) or [Spring Boot](https://docs.sentry.io/platforms/java/guides/spring-boot.md) integration, or run the [Sentry OpenTelemetry agent](https://docs.sentry.io/platforms/java/opentelemetry/setup/agent.md).
* Use the snippet in the "With DSN" code box tab to have the appender initialize Sentry.

The example configures a `ConsoleAppender` that logs to standard out at the `INFO` level, and a `SentryAppender` that sends messages at the `ERROR` level and above to Sentry.

The `ConsoleAppender` is provided only as an example of a non-Sentry appender set to a different logging threshold, similar to what you may already have in your project.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<Configuration>

  <Appenders>
    <Console name="CONSOLE" target="SYSTEM_OUT">
      <PatternLayout
        pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"
      />
    </Console>
    <Sentry name="SENTRY" />
  </Appenders>

  <Loggers>
    <Root level="INFO">
      <AppenderRef ref="CONSOLE" />
      <AppenderRef ref="SENTRY" level="ERROR" />
    </Root>
  </Loggers>

</Configuration>
```

*Other available variations of the above snippet: With DSN*

`SentryAppender` does not support [Log4j's asynchronous loggers](https://logging.apache.org/log4j/2.x/manual/async.html). The Sentry Java SDK itself is already asynchronous and does not perform any blocking operation on the calling thread.

Sentry Logs must be enabled for the appender to send log messages as Logs. If Sentry is initialized elsewhere, make sure Logs are enabled there. If the appender initializes the SDK, the `sentry.properties` file as shown in the "Additional Options" section below enables them.

### [Additional Options If the Appender Initializes Sentry](https://docs.sentry.io/platforms/java/guides/log4j2.md#additional-options-if-the-appender-initializes-sentry)

If the appender initializes the SDK, you can also use Sentry's static API, as shown on the [usage page](https://docs.sentry.io/platforms/java/guides/log4j2/usage.md), to record breadcrumbs, set the current user, or capture events manually.

To set other options, such as data collection, add a `sentry.properties` file. The DSN is already in the appender, so it isn't needed there. See the [configuration page](https://docs.sentry.io/platforms/java/configuration.md) for where the SDK reads this file from.

```properties
# Enable logs
logs.enabled=true

# Use Data Collection defaults but don't collect automatic user information.
# https://docs.sentry.io/platforms/java/guides/log4j2/data-management/data-collected/
data-collection.user-info=false
```

### [Minimum Log Level](https://docs.sentry.io/platforms/java/guides/log4j2.md#minimum-log-level)

Two log levels are used to configure this integration, as illustrated below in the provided code samples:

1. Configure the lowest level required for a log message to become an event (`minimumEventLevel`) sent to Sentry.
2. Configure the lowest level a message has to be to become a breadcrumb (`minimumBreadcrumbLevel`)
3. Configure the lowest level a message has to be to be sent as Sentry Log (`minimumLevel`).

Setting `minimumEventLevel` or `minimumBreadcrumbLevel` in `log4j2.xml` only affects events logged by way of Log4j2. The settings will have no effect when calling `Sentry.captureMessage` or similar directly.

Breadcrumbs are kept in memory (by default the last 100 records) and are sent with events. For example, by default, if you log 100 entries with `logger.info` or `logger.warn`, no event is sent to Sentry. If you then log with `logger.error`, an event is sent to Sentry that includes those 100 `info` or `warn` messages. For this to work, `SentryAppender` needs to receive **all** log entries to decide what to keep as breadcrumb or send as event. Set the `SentryAppender` log level configuration to a value lower than what is set for the `minimumBreadcrumbLevel` and `minimumEventLevel` so that `SentryAppender` receives these log messages.

```xml
<!-- Setting minimumBreadcrumbLevel modifies the default minimum level to add breadcrumbs from INFO to DEBUG  -->
<!-- Setting minimumEventLevel the default minimum level to capture an event from ERROR to WARN  -->
<Sentry
  name="SENTRY"
  minimumBreadcrumbLevel="DEBUG"
  minimumEventLevel="WARN"
  minimumLevel="DEBUG"
/>
```

*Other available variations of the above snippet: With DSN*

## [Verify Your Setup](https://docs.sentry.io/platforms/java/guides/log4j2.md#verify-your-setup)

To verify that the integration is working, log an error through Log4j2:

```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

Logger logger = LogManager.getLogger("example");
logger.error("This is a test log message");
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/java/guides/log4j2.md#view-captured-data-in-sentry)

Now, open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application (it takes a couple of moments for the data to appear).

## [Next Steps](https://docs.sentry.io/platforms/java/guides/log4j2.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn more about [setting up logging](https://docs.sentry.io/platforms/java/guides/log4j2/logs.md)
* Learn how to [send application metrics](https://docs.sentry.io/platforms/java/metrics.md) and [traces](https://docs.sentry.io/platforms/java/tracing.md)
* Configure [profiling](https://docs.sentry.io/platforms/java/profiling.md) to capture performance data from your application

Are you having problems setting up the SDK or integration?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/java/guides/log4j2/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other Java Frameworks

- [java.util.logging](https://docs.sentry.io/platforms/java/guides/jul.md)
- [Logback](https://docs.sentry.io/platforms/java/guides/logback.md)
- [Servlet](https://docs.sentry.io/platforms/java/guides/servlet.md)
- [Spring](https://docs.sentry.io/platforms/java/guides/spring.md)
- [Spring Boot](https://docs.sentry.io/platforms/java/guides/spring-boot.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/java/guides/log4j2/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/java/guides/log4j2/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/java/guides/log4j2/configuration.md)
- [Logs](https://docs.sentry.io/platforms/java/guides/log4j2/logs.md)
- [Integrations](https://docs.sentry.io/platforms/java/guides/log4j2/integrations.md)
- [Tracing](https://docs.sentry.io/platforms/java/guides/log4j2/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/java/guides/log4j2/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/java/guides/log4j2/data-management.md)
- [Profiling](https://docs.sentry.io/platforms/java/guides/log4j2/profiling.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/java/guides/log4j2/security-policy-reporting.md)
- [Crons](https://docs.sentry.io/platforms/java/guides/log4j2/crons.md)
- [Advanced Usage](https://docs.sentry.io/platforms/java/guides/log4j2/advanced_usage.md)
- [User Feedback](https://docs.sentry.io/platforms/java/guides/log4j2/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/java/guides/log4j2/feature-flags.md)
- [Source Context](https://docs.sentry.io/platforms/java/guides/log4j2/source-context.md)
- [Gradle](https://docs.sentry.io/platforms/java/guides/log4j2/gradle.md)
- [Maven](https://docs.sentry.io/platforms/java/guides/log4j2/maven.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/java/guides/log4j2/opentelemetry.md)
- [Migration Guides](https://docs.sentry.io/platforms/java/guides/log4j2/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/java/guides/log4j2/troubleshooting.md)
- [Legacy SDK (1.7)](https://docs.sentry.io/platforms/java/guides/log4j2/legacy.md)

