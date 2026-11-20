---
title: "java.util.logging"
source: https://docs.sentry.io/platforms/java/guides/jul.md
path: platforms/java/guides/jul
---

---
title: "java.util.logging"
description: "Learn how to set up Sentry's JUL integration to capture logs."
url: https://docs.sentry.io/platforms/java/guides/jul/
---

# Sentry for java.util.logging

The `sentry-jul` library provides a [java.util.logging Handler](http://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html) that sends logged exceptions to Sentry. You can find the source [on GitHub](https://github.com/getsentry/sentry-java/tree/master/sentry-jul).

## [Prerequisites](https://docs.sentry.io/platforms/java/guides/jul.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Java version `8` (also known as Java `1.8`) or above

## [Install](https://docs.sentry.io/platforms/java/guides/jul.md#install)

Add the `sentry-jul` dependency to your project:

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-jul</artifactId>
    <version>8.65.0</version>
</dependency>
```

*Other available variations of the above snippet: Gradle, SBT*

For other dependency managers, see the [central Maven repository](https://search.maven.org/artifact/io.sentry/sentry-jul).

If you are using multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

## [Configure](https://docs.sentry.io/platforms/java/guides/jul.md#configure)

Configuration should happen as early as possible in your application's lifecycle.

The following example configures a `ConsoleHandler` that logs to standard out at the `INFO` level and a `SentryHandler` that logs to the Sentry server at the `WARN` level. The `ConsoleHandler` is only provided as an example of a non-Sentry appender that is set to a different logging threshold, like one you may already have in your project.

The `ConsoleHandler` is provided only as an example of a non-Sentry appender set to a different logging threshold, similar to what you may already have in your project.

Example configuration using the `logging.properties` format:

```properties
# Enable the Console and Sentry handlers
handlers=java.util.logging.ConsoleHandler,io.sentry.jul.SentryHandler

# Set the default log level to INFO
.level=INFO

# Override the Sentry handler log level to WARNING
io.sentry.jul.SentryHandler.level=WARNING
```

When starting your application, add the `java.util.logging.config.file` to the system properties, with the full path to the `logging.properties` as its value:

```bash
java -Djava.util.logging.config.file=/path/to/app.properties MyClass
```

Sentry Logs must be enabled for the appender to send log messages as Logs. If Sentry is initialized elsewhere, make sure Logs are enabled there. If the appender initializes the SDK, the `sentry.properties` file as shown in the section below enables them.

### [Set the DSN If Nothing Else Initializes Sentry](https://docs.sentry.io/platforms/java/guides/jul.md#set-the-dsn-if-nothing-else-initializes-sentry)

You can skip this section if your application already initializes Sentry through [`Sentry.init`](https://docs.sentry.io/platforms/java.md), the [Spring](https://docs.sentry.io/platforms/java/guides/spring.md) or [Spring Boot](https://docs.sentry.io/platforms/java/guides/spring-boot.md) integration, or the [Sentry OpenTelemetry agent](https://docs.sentry.io/platforms/java/opentelemetry/setup/agent.md).

If you haven't initialized Sentry elsewhere, the handler initializes the SDK for you. It reads the DSN from the system property `sentry.dsn`, the environment variable `SENTRY_DSN`, or the `dsn` property in a `sentry.properties` file. See the [configuration page](https://docs.sentry.io/platforms/java/configuration.md) for details on external configuration.

```properties
dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>

# Enable logs
logs.enabled=true

# Use Data Collection defaults but don't collect automatic user information.
# https://docs.sentry.io/platforms/java/guides/jul/data-management/data-collected/
data-collection.user-info=false
```

### [Minimum Log Level](https://docs.sentry.io/platforms/java/guides/jul.md#minimum-log-level)

Two log levels are used to configure this integration:

1. Configure the lowest level required for a log message to become an event (`minimumEventLevel`) sent to Sentry.
2. Configure the lowest level a message has to be to become a breadcrumb (`minimumBreadcrumbLevel`).
3. Configure the lowest level a message has to be to be sent as Sentry Log (`minimumLevel`).

Setting `minimumEventLevel` or `minimumBreadcrumbLevel` in `logging.properties` only affects events logged by way of JUL. The settings will have no effect when calling `Sentry.captureMessage` or similar directly.

Breadcrumbs are kept in memory (by default the last 100 records) and are sent with events. For example, by default, if you log 100 entries with `logger.config` or `logger.warn`, no event is sent to Sentry. If you then log with `logger.error`, an event is sent to Sentry which includes those 100 `config` or `warning` messages. For this to work, `SentryHandler` needs to receive **all** log entries to decide what to keep as breadcrumb or send as event. Set the `SentryHandler` log level configuration to a value lower than what is set for the `minimumBreadcrumbLevel` and `minimumEventLevel` so that `SentryHandler` receives these log messages.

```properties
io.sentry.jul.SentryHandler.minimumEventLevel=INFO
io.sentry.jul.SentryHandler.minimumBreadcrumbLevel=CONFIG
io.sentry.jul.SentryHandler.level=CONFIG
...
```

### [String Formatting Style](https://docs.sentry.io/platforms/java/guides/jul.md#string-formatting-style)

By default, [MessageFormat#format](https://docs.oracle.com/javase/8/docs/api/java/text/MessageFormat.html#format-java.lang.Object:A-java.lang.StringBuffer-java.text.FieldPosition-) method is used to render parameterized log messages. It can be changed to use [String#format](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#format-java.lang.String-java.lang.Object...-) by setting `printfStyle` property to `true`:

```properties
io.sentry.jul.SentryHandler.printfStyle=true
```

## [Verify Your Setup](https://docs.sentry.io/platforms/java/guides/jul.md#verify-your-setup)

To verify that the integration is working, log an error through JUL:

```java
import java.util.logging.Level;
import java.util.logging.Logger;

Logger logger = Logger.getLogger("example");
logger.log(Level.SEVERE, "This is a test.", new Exception("This is a test."));
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/java/guides/jul.md#view-captured-data-in-sentry)

Now, open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application (it takes a couple of moments for the data to appear).

## [Next Steps](https://docs.sentry.io/platforms/java/guides/jul.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn more about [setting up logging](https://docs.sentry.io/platforms/java/guides/jul/logs.md)
* Learn how to [send application metrics](https://docs.sentry.io/platforms/java/metrics.md) and [traces](https://docs.sentry.io/platforms/java/tracing.md)
* Configure [profiling](https://docs.sentry.io/platforms/java/profiling.md) to capture performance data from your application

Are you having problems setting up the SDK or integration?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/java/guides/jul/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other Java Frameworks

- [Log4j 2.x](https://docs.sentry.io/platforms/java/guides/log4j2.md)
- [Logback](https://docs.sentry.io/platforms/java/guides/logback.md)
- [Servlet](https://docs.sentry.io/platforms/java/guides/servlet.md)
- [Spring](https://docs.sentry.io/platforms/java/guides/spring.md)
- [Spring Boot](https://docs.sentry.io/platforms/java/guides/spring-boot.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/java/guides/jul/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/java/guides/jul/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/java/guides/jul/configuration.md)
- [Logs](https://docs.sentry.io/platforms/java/guides/jul/logs.md)
- [Integrations](https://docs.sentry.io/platforms/java/guides/jul/integrations.md)
- [Tracing](https://docs.sentry.io/platforms/java/guides/jul/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/java/guides/jul/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/java/guides/jul/data-management.md)
- [Profiling](https://docs.sentry.io/platforms/java/guides/jul/profiling.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/java/guides/jul/security-policy-reporting.md)
- [Crons](https://docs.sentry.io/platforms/java/guides/jul/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/java/guides/jul/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/java/guides/jul/feature-flags.md)
- [Source Context](https://docs.sentry.io/platforms/java/guides/jul/source-context.md)
- [Gradle](https://docs.sentry.io/platforms/java/guides/jul/gradle.md)
- [Maven](https://docs.sentry.io/platforms/java/guides/jul/maven.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/java/guides/jul/opentelemetry.md)
- [Migration Guides](https://docs.sentry.io/platforms/java/guides/jul/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/java/guides/jul/troubleshooting.md)
- [Legacy SDK (1.7)](https://docs.sentry.io/platforms/java/guides/jul/legacy.md)

