---
title: "java.util.logging"
source: https://docs.sentry.io/platforms/java/guides/jul.md
path: platforms/java/guides/jul
---

---
title: "java.util.logging"
url: https://docs.sentry.io/platforms/java/guides/jul/
---

# Sentry for java.util.logging

The `sentry-jul` library provides a [java.util.logging Handler](http://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html) that sends logged exceptions to Sentry.

##### Sentry Logs

Enable the Sentry Logs feature to unlock Sentry's full logging power. With Sentry Logs, you can search, filter, and analyze logs from across your entire application in one place.

Once this integration is configured you can *also* use Sentry’s static API, [as shown on the usage page](https://docs.sentry.io/platforms/java/guides/jul/usage.md), in order to do things like record breadcrumbs, set the current user, or manually send events. The source can be found [on GitHub](https://github.com/getsentry/sentry-java/tree/master/sentry-jul).

On this page, we get you up and running with Sentry's SDK.

##### Using a framework?

Check out the other SDKs we support in the left-hand dropdown.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/java/guides/jul.md#install)

Sentry captures data by using an SDK within your application’s runtime.

Error Monitoring\[ ]Tracing\[ ]Profiling\[x]Logs\[x]OpenTelemetry

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-jul</artifactId>
    <version>8.61.1</version>
</dependency>
// ___PRODUCT_OPTION_START___ profiling
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-async-profiler</artifactId>
    <version>8.61.1</version>
</dependency>
// ___PRODUCT_OPTION_END___ profiling
```

*Other available variations of the above snippet: Gradle, SBT*

For other dependency managers, see the [central Maven repository](https://search.maven.org/artifact/io.sentry/sentry-jul).

If you are using multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

When running your application, please add our `sentry-opentelemetry-agent` to the `java` command.

Download the latest version of the `sentry-opentelemetry-agent-8.61.1.jar` from [MavenCentral](https://search.maven.org/artifact/io.sentry/sentry-opentelemetry-agent):

```bash
curl https://repo1.maven.org/maven2/io/sentry/sentry-opentelemetry-agent/8.61.1/sentry-opentelemetry-agent-8.61.1.jar -o sentry-opentelemetry-agent-8.61.1.jar
```

Then run your application with:

```bash
SENTRY_PROPERTIES_FILE=sentry.properties JAVA_TOOL_OPTIONS="-javaagent:sentry-opentelemetry-agent-8.61.1.jar" java -jar your-application.jar
```

*Other available variations of the above snippet: Java CLI argument*

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

### [DSN Configuration](https://docs.sentry.io/platforms/java/guides/jul.md#dsn-configuration)

Sentry reads the DSN from the system property `sentry.dsn`, environment variable `SENTRY_DSN` or the `dsn` property in `sentry.properties` file. [See the configuration page](https://docs.sentry.io/platforms/java/configuration.md) for more details on external configuration.

```properties
dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>
# Use Data Collection defaults but don't collect automatic user information.
# https://docs.sentry.io/platforms/java/guides/jul/data-management/data-collected/
data-collection.user-info=false
# Configure other data categories here.
<!-- ___PRODUCT_OPTION_START___ logs -->
# Enable logs
logs.enabled=true
<!-- ___PRODUCT_OPTION_END___ logs  -->
```

### [Minimum Log Level](https://docs.sentry.io/platforms/java/guides/jul.md#minimum-log-level)

Two log levels are used to configure this integration:

1. Configure the lowest level required for a log message to become an event (`minimumEventLevel`) sent to Sentry.
2. Configure the lowest level a message has to be to become a breadcrumb (`minimumBreadcrumbLevel`).

3) Configure the lowest level a message has to be to be sent as Sentry Log (`minimumLevel`).

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

The SDK can be configured using a `sentry.properties` file:

```properties
dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>
# Use Data Collection defaults but don't collect automatic user information.
# https://docs.sentry.io/platforms/java/data-management/data-collected/
data-collection.user-info=false
# Configure other data categories here.
# ___PRODUCT_OPTION_START___ performance
traces-sample-rate=1.0
# ___PRODUCT_OPTION_END___ performance
// ___PRODUCT_OPTION_START___ logs
logs.enabled=true
// ___PRODUCT_OPTION_END___ logs
// ___PRODUCT_OPTION_START___ profiling

# Enable profiling
profile-session-sample-rate=1.0
profile-lifecycle=TRACE
// ___PRODUCT_OPTION_END___ profiling
```

Learn more about setting up logging in our [Logs documentation](https://docs.sentry.io/platforms/java/guides/jul/logs.md).

## [Verify](https://docs.sentry.io/platforms/java/guides/jul.md#verify)

This snippet includes an intentional error, so you can test that everything is working as soon as you set it up.

```java
import io.sentry.Sentry;

try {
  throw new Exception("This is a test.");
} catch (Exception e) {
  Sentry.captureException(e);
}
```

*Other available variations of the above snippet: Kotlin*

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/java/guides/jul/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/java/guides/jul.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

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

