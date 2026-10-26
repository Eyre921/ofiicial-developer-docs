---
title: "Logback"
source: https://docs.sentry.io/platforms/java/guides/logback.md
path: platforms/java/guides/logback
---

---
title: "Logback"
url: https://docs.sentry.io/platforms/java/guides/logback/
---

# Sentry for Logback

The `sentry-logback` library provides [Logback](https://logback.qos.ch/) support for Sentry using an [Appender](https://logback.qos.ch/apidocs/ch/qos/logback/core/Appender.html) that sends logged exceptions to Sentry.

##### Sentry Logs

Enable the Sentry Logs feature to unlock Sentry's full logging power. With Sentry Logs, you can search, filter, and analyze logs from across your entire application in one place.

Once this integration is configured you can *also* use Sentry’s static API, [as shown on the usage page](https://docs.sentry.io/platforms/java/guides/logback/usage.md), in order to do things like record breadcrumbs, set the current user, or manually send events. The source can be found [on GitHub](https://github.com/getsentry/sentry-java/tree/master/sentry-logback).

On this page, we get you up and running with Sentry's SDK.

##### Using a framework?

Check out the other SDKs we support in the left-hand dropdown.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/java/guides/logback.md#install)

Sentry captures data by using an SDK within your application’s runtime.

Error Monitoring\[ ]Tracing\[ ]Profiling\[x]Logs\[x]OpenTelemetry

**\[Maven Plugin] pom.xml**

```xml
<plugin>
  <groupId>io.sentry</groupId>
  <artifactId>sentry-maven-plugin</artifactId>
  <version>0.11.0</version>
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
// ___PRODUCT_OPTION_START___ profiling
<dependencies>
  <dependency>
      <groupId>io.sentry</groupId>
      <artifactId>sentry-async-profiler</artifactId>
      <version>8.61.1</version>
  </dependency>
</dependencies>
// ___PRODUCT_OPTION_END___ profiling
```

**Maven**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-logback</artifactId>
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

**Gradle Plugin**

```groovy
plugins {
  id "io.sentry.jvm.gradle" version "6.24.0"
}
// ___PRODUCT_OPTION_START___ profiling
dependencies {
  implementation 'io.sentry:sentry-async-profiler:8.61.1'
}
// ___PRODUCT_OPTION_END___ profiling
```

**Gradle**

```groovy
implementation 'io.sentry:sentry-logback:8.61.1'
// ___PRODUCT_OPTION_START___ profiling
implementation 'io.sentry:sentry-async-profiler:8.61.1'
// ___PRODUCT_OPTION_END___ profiling
```

**SBT**

```scala
libraryDependencies += "io.sentry" % "sentry-logback" % "8.61.1"
// ___PRODUCT_OPTION_START___ profiling
libraryDependencies += "io.sentry" % "sentry-async-profiler" % "8.61.1"
// ___PRODUCT_OPTION_END___ profiling
```

For other dependency managers, see the [central Maven repository](https://search.maven.org/artifact/io.sentry/sentry-logback).

We recommend using our Gradle plugin as it can add integrations and provide source context for events.

If you are manually adding multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

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
            // ___PRODUCT_OPTION_START___ logs
            <logs>
                <enabled>true</enabled>
            </logs>
            // ___PRODUCT_OPTION_END___ logs
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
    <appender name="Sentry" class="io.sentry.logback.SentryAppender" />

    <!-- Enable the Console and Sentry appenders, Console is provided as an example
 of a non-Sentry logger that is set to a different logging threshold -->
    <root level="INFO">
        <appender-ref ref="Console" />
        <appender-ref ref="Sentry" />
    </root>
</configuration>
```

### [SDK Configuration](https://docs.sentry.io/platforms/java/guides/logback.md#sdk-configuration)

Configure the SDK using a `sentry.properties` file:

```properties
dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>
# Use Data Collection defaults but don't collect automatic user information.
# https://docs.sentry.io/platforms/java/guides/logback/data-management/data-collected/
data-collection.user-info=false
# Configure other data categories here.
```

You can also provide the DSN through the `sentry.dsn` system property or the `SENTRY_DSN` environment variable. [See the configuration page](https://docs.sentry.io/platforms/java/configuration.md) for more details on external configuration.

### [Minimum Log Level](https://docs.sentry.io/platforms/java/guides/logback.md#minimum-log-level)

Two log levels are used to configure this integration:

1. Configure the lowest level required for a log message to become an event (`minimumEventLevel`) sent to Sentry.
2. Configure the lowest level a message has to be to become a breadcrumb (`minimumBreadcrumbLevel`).

3) Configure the lowest level a message has to be to be sent as Sentry Log (`minimumLevel`).

Setting `minimumEventLevel` or `minimumBreadcrumbLevel` in `logback.xml` only affects events logged by way of Logback. The settings will have no effect when calling `Sentry.captureMessage` or similar directly.

Breadcrumbs are kept in memory (by default the last 100 records) and are sent with events. For example, by default, if you log 100 entries with `logger.info` or `logger.warn`, no event is sent to Sentry. If you then log with `logger.error`, an event is sent to Sentry which includes those 100 `info` or `warn` messages. For this to work, `SentryAppender` needs to receive **all** log entries to decide what to keep as breadcrumb or sent as event. Set the `SentryAppender` log level configuration to a value lower than what is set for the `minimumBreadcrumbLevel` and `minimumEventLevel` so that `SentryAppender` receives these log messages.

```xml
<appender name="Sentry" class="io.sentry.logback.SentryAppender">
    <!-- Optionally change minimum Event level. Default for Events is ERROR -->
    <minimumEventLevel>WARN</minimumEventLevel>
    <!-- Optionally change minimum Breadcrumbs level. Default for Breadcrumbs is INFO -->
    <minimumBreadcrumbLevel>DEBUG</minimumBreadcrumbLevel>
    // ___PRODUCT_OPTION_START___ logs
    <!-- Optionally change minimum Log level. Default for Logs is INFO -->
    <minimumLevel>DEBUG</minimumLevel>
    // ___PRODUCT_OPTION_END___ logs
</appender>
```

```xml
<appender name="Sentry" class="io.sentry.logback.SentryAppender">
    <!-- Optionally change minimum Event level. Default for Events is ERROR -->
    <minimumEventLevel>WARN</minimumEventLevel>
    <!-- Optionally change minimum Breadcrumbs level. Default for Breadcrumbs is INFO -->
    <minimumBreadcrumbLevel>DEBUG</minimumBreadcrumbLevel>
    // ___PRODUCT_OPTION_START___ logs
    <!-- Optionally change minimum Log level. Default for Logs is INFO -->
    <minimumLevel>DEBUG</minimumLevel>
    // ___PRODUCT_OPTION_END___ logs
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

Learn more about setting up logging in our [Logs documentation](https://docs.sentry.io/platforms/java/guides/logback/logs.md).

## [Verify](https://docs.sentry.io/platforms/java/guides/logback.md#verify)

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

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/java/guides/logback/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/java/guides/logback.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

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

