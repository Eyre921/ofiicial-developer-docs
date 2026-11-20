---
title: "Logback"
source: https://docs.sentry.io/platforms/java/guides/logback.md
path: platforms/java/guides/logback
---

---
title: "Logback"
description: "Learn how to set up Sentry's Logback integration to capture logs."
url: https://docs.sentry.io/platforms/java/guides/logback/
---

# Sentry for Logback

The `sentry-logback` library provides [Logback](https://logback.qos.ch/) support for Sentry using an [Appender](https://logback.qos.ch/manual/appenders.html) that sends logged exceptions to Sentry. You can find the source [on GitHub](https://github.com/getsentry/sentry-java/tree/master/sentry-logback).

## [Prerequisites](https://docs.sentry.io/platforms/java/guides/logback.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Java version `8` (also known as Java `1.8`) or above

## [Install](https://docs.sentry.io/platforms/java/guides/logback.md#install)

Add `sentry-logback` to your project (Maven Plugin and Gradle Plugin automatically add integrations for you):

**\[Maven Plugin] pom.xml**

```xml
<plugin>
  <groupId>io.sentry</groupId>
  <artifactId>sentry-maven-plugin</artifactId>
  <version>0.12.0</version>
  <!-- Required to allow auto-install of Sentry SDK and Integrations -->
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
    <artifactId>sentry-logback</artifactId>
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
implementation 'io.sentry:sentry-logback:8.65.0'
```

**SBT**

```scala
libraryDependencies += "io.sentry" % "sentry-logback" % "8.65.0"
```

For other dependency managers, see the [central Maven repository](https://search.maven.org/artifact/io.sentry/sentry-logback).

We recommend using our Gradle plugin as it can add integrations and provide source context for events.

If you are manually adding multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

## [Configure](https://docs.sentry.io/platforms/java/guides/logback.md#configure)

Configuration should happen as early as possible in your application's lifecycle.

The following example configures a `ConsoleAppender` that logs to standard out at the `INFO` level, and a `SentryAppender` that logs to the Sentry server at the `ERROR` level.

The `ConsoleAppender` is provided only as an example of a non-Sentry appender set to a different logging threshold, similar to what you may already have in your project.

```xml
<configuration>
    <!-- Configure the Console appender -->
    <appender name="Console" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern
      >%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- Configure the Sentry appender, overriding the logging threshold to the WARN level -->
    <appender name="Sentry" class="io.sentry.logback.SentryAppender">
        <options>
            <logs>
                <enabled>true</enabled>
            </logs>
        </options>
    </appender>

    <!-- Enable the Console and Sentry appenders, Console is provided as an example
 of a non-Sentry logger that is set to a different logging threshold -->
    <root level="INFO">
        <appender-ref ref="Console" />
        <appender-ref ref="Sentry" />
    </root>
</configuration>
```

Sentry Logs must be enabled for the appender to send log messages as Logs. If Sentry is initialized elsewhere, make sure Logs are enabled there. If the appender initializes the SDK, the `sentry.properties` file as shown in the section below enables them.

### [Set the DSN If Nothing Else Initializes Sentry](https://docs.sentry.io/platforms/java/guides/logback.md#set-the-dsn-if-nothing-else-initializes-sentry)

You can skip this section if your application already initializes Sentry through [`Sentry.init`](https://docs.sentry.io/platforms/java.md), the [Spring](https://docs.sentry.io/platforms/java/guides/spring.md) or [Spring Boot](https://docs.sentry.io/platforms/java/guides/spring-boot.md) integration, or the [Sentry OpenTelemetry agent](https://docs.sentry.io/platforms/java/opentelemetry/setup/agent.md).

If you haven't initialized Sentry elsewhere, the handler initializes the SDK for you. Configure it with a `sentry.properties` file:

```properties
dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>

# Enable logs
logs.enabled=true

# Use Data Collection defaults but don't collect automatic user information.
# https://docs.sentry.io/platforms/java/guides/logback/data-management/data-collected/
data-collection.user-info=false
```

You can also provide the DSN through the `sentry.dsn` system property or the `SENTRY_DSN` environment variable. [See the configuration page](https://docs.sentry.io/platforms/java/configuration.md) for more details on external configuration.

### [Minimum Log Level](https://docs.sentry.io/platforms/java/guides/logback.md#minimum-log-level)

Two log levels are used to configure this integration:

1. Configure the lowest level required for a log message to become an event (`minimumEventLevel`) sent to Sentry.
2. Configure the lowest level a message has to be to become a breadcrumb (`minimumBreadcrumbLevel`).
3. Configure the lowest level a message has to be to be sent as Sentry Log (`minimumLevel`).

Setting `minimumEventLevel` or `minimumBreadcrumbLevel` in `logback.xml` only affects events logged by way of Logback. The settings will have no effect when calling `Sentry.captureMessage` or similar directly.

Breadcrumbs are kept in memory (by default the last 100 records) and are sent with events. For example, by default, if you log 100 entries with `logger.info` or `logger.warn`, no event is sent to Sentry. If you then log with `logger.error`, an event is sent to Sentry which includes those 100 `info` or `warn` messages. For this to work, `SentryAppender` needs to receive **all** log entries to decide what to keep as breadcrumb or sent as event. Set the `SentryAppender` log level configuration to a value lower than what is set for the `minimumBreadcrumbLevel` and `minimumEventLevel` so that `SentryAppender` receives these log messages.

```xml
<appender name="Sentry" class="io.sentry.logback.SentryAppender">
    <!-- Optionally change minimum Event level. Default for Events is ERROR -->
    <minimumEventLevel>WARN</minimumEventLevel>
    <!-- Optionally change minimum Breadcrumbs level. Default for Breadcrumbs is INFO -->
    <minimumBreadcrumbLevel>DEBUG</minimumBreadcrumbLevel>
    <!-- Optionally change minimum Log level. Default for Logs is INFO -->
    <minimumLevel>DEBUG</minimumLevel>
</appender>
```

### [Encoded Messages](https://docs.sentry.io/platforms/java/guides/logback.md#encoded-messages)

A Logback encoder can mask or remove sensitive values before Sentry receives a log entry. When you configure an encoder on `SentryAppender`, Sentry sends the encoded message and omits the original message template and parameters by default.

Set `includeUnencodedMessage` to `true` when you also need the original template and parameters:

```xml
<appender name="Sentry" class="io.sentry.logback.SentryAppender">
    <encoder>
        <pattern
    >%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
    </encoder>
    <includeUnencodedMessage>true</includeUnencodedMessage>
</appender>
```

Original templates and parameters can contain sensitive data. Prefer this scoped appender option to `sendDefaultPii`; the legacy `sendDefaultPii=true` behavior remains supported for compatibility.

## [Verify Your Setup](https://docs.sentry.io/platforms/java/guides/logback.md#verify-your-setup)

To verify that the integration is working, log an error through Logback:

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

Logger logger = LoggerFactory.getLogger("example");
logger.error("This is a test.", new Exception("This is a test."));
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/java/guides/logback.md#view-captured-data-in-sentry)

Now, open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application (it takes a couple of moments for the data to appear).

## [Next Steps](https://docs.sentry.io/platforms/java/guides/logback.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn more about [setting up logging](https://docs.sentry.io/platforms/java/guides/logback/logs.md)
* Learn how to [send application metrics](https://docs.sentry.io/platforms/java/metrics.md) and [traces](https://docs.sentry.io/platforms/java/tracing.md)
* Configure [profiling](https://docs.sentry.io/platforms/java/profiling.md) to capture performance data from your application

Are you having problems setting up the SDK or integration?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/java/guides/logback/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other Java Frameworks

- [java.util.logging](https://docs.sentry.io/platforms/java/guides/jul.md)
- [Log4j 2.x](https://docs.sentry.io/platforms/java/guides/log4j2.md)
- [Servlet](https://docs.sentry.io/platforms/java/guides/servlet.md)
- [Spring](https://docs.sentry.io/platforms/java/guides/spring.md)
- [Spring Boot](https://docs.sentry.io/platforms/java/guides/spring-boot.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/java/guides/logback/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/java/guides/logback/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/java/guides/logback/configuration.md)
- [Logs](https://docs.sentry.io/platforms/java/guides/logback/logs.md)
- [Integrations](https://docs.sentry.io/platforms/java/guides/logback/integrations.md)
- [Tracing](https://docs.sentry.io/platforms/java/guides/logback/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/java/guides/logback/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/java/guides/logback/data-management.md)
- [Profiling](https://docs.sentry.io/platforms/java/guides/logback/profiling.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/java/guides/logback/security-policy-reporting.md)
- [Crons](https://docs.sentry.io/platforms/java/guides/logback/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/java/guides/logback/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/java/guides/logback/feature-flags.md)
- [Source Context](https://docs.sentry.io/platforms/java/guides/logback/source-context.md)
- [Gradle](https://docs.sentry.io/platforms/java/guides/logback/gradle.md)
- [Maven](https://docs.sentry.io/platforms/java/guides/logback/maven.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/java/guides/logback/opentelemetry.md)
- [Migration Guides](https://docs.sentry.io/platforms/java/guides/logback/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/java/guides/logback/troubleshooting.md)
- [Legacy SDK (1.7)](https://docs.sentry.io/platforms/java/guides/logback/legacy.md)

