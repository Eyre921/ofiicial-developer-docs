---
title: "Log4j 2.x"
source: https://docs.sentry.io/platforms/java/guides/log4j2.md
path: platforms/java/guides/log4j2
---

---
title: "Log4j 2.x"
url: https://docs.sentry.io/platforms/java/guides/log4j2/
---

# Sentry for Log4j 2.x

The `sentry-log4j2` library provides [Log4j 2.x](https://logging.apache.org/log4j/2.x/) support for Sentry via an [Appender](https://logging.apache.org/log4j/2.x/log4j-core/apidocs/org/apache/logging/log4j/core/Appender.html) that sends logged exceptions to Sentry.

##### Sentry Logs

Enable the Sentry Logs feature to unlock Sentry's full logging power. With Sentry Logs, you can search, filter, and analyze logs from across your entire application in one place.

Once the integration is configured you can *also* use Sentry’s static API, [as shown on the usage page](https://docs.sentry.io/platforms/java/guides/log4j2/usage.md), in order to do things like record breadcrumbs, set the current user, or manually send events. The source can be found [on GitHub](https://github.com/getsentry/sentry-java/tree/master/sentry-log4j2).

On this page, we get you up and running with Sentry's SDK.

##### Using a framework?

Check out the other SDKs we support in the left-hand dropdown.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/java/guides/log4j2.md#install)

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
      <version>8.62.0</version>
  </dependency>
</dependencies>
// ___PRODUCT_OPTION_END___ profiling
```

**Maven**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-log4j2</artifactId>
    <version>8.62.0</version>
</dependency>
// ___PRODUCT_OPTION_START___ profiling
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-async-profiler</artifactId>
    <version>8.62.0</version>
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
  implementation 'io.sentry:sentry-async-profiler:8.62.0'
}
// ___PRODUCT_OPTION_END___ profiling
```

**Gradle**

```groovy
implementation 'io.sentry:sentry-log4j2:8.62.0'
// ___PRODUCT_OPTION_START___ profiling
implementation 'io.sentry:sentry-async-profiler:8.62.0'
// ___PRODUCT_OPTION_END___ profiling
```

**SBT**

```scala
libraryDependencies += "io.sentry" % "sentry-log4j2" % "8.62.0"
// ___PRODUCT_OPTION_START___ profiling
libraryDependencies += "io.sentry" % "sentry-async-profiler" % "8.62.0"
// ___PRODUCT_OPTION_END___ profiling
```

For other dependency managers see the [central Maven repository](https://search.maven.org/artifact/io.sentry/sentry-log4j2).

We recommend using our Gradle plugin as it can add integrations and provide source context for events.

If you are manually adding multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

When running your application, please add our `sentry-opentelemetry-agent` to the `java` command.

Download the latest version of the `sentry-opentelemetry-agent-8.62.0.jar` from [MavenCentral](https://search.maven.org/artifact/io.sentry/sentry-opentelemetry-agent):

```bash
curl https://repo1.maven.org/maven2/io/sentry/sentry-opentelemetry-agent/8.62.0/sentry-opentelemetry-agent-8.62.0.jar -o sentry-opentelemetry-agent-8.62.0.jar
```

Then run your application with:

```bash
SENTRY_PROPERTIES_FILE=sentry.properties JAVA_TOOL_OPTIONS="-javaagent:sentry-opentelemetry-agent-8.62.0.jar" java -jar your-application.jar
```

*Other available variations of the above snippet: Java CLI argument*

## [Configure](https://docs.sentry.io/platforms/java/guides/log4j2.md#configure)

Configuration should happen as early as possible in your application's lifecycle.

The following example using the `log4j2.xml` format to configure a `ConsoleAppender` that logs to standard out at the `INFO` level, and a `SentryAppender` that logs to the Sentry server at the `ERROR` level.

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
    <Sentry name="SENTRY" dsn="https://<key>@o<orgId>.ingest.sentry.io/<projectId>" />
  </Appenders>

  <Loggers>
    <Root level="INFO">
      <AppenderRef ref="CONSOLE" />
      <AppenderRef ref="SENTRY" level="ERROR" />
    </Root>
  </Loggers>

</Configuration>
```

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

`SentryAppender` does not support [Log4j's asynchronous loggers](https://logging.apache.org/log4j/2.x/manual/async.html). The Sentry Java SDK itself is already asynchronous and does not perform any blocking operation on the calling thread.

### [DSN Configuration](https://docs.sentry.io/platforms/java/guides/log4j2.md#dsn-configuration)

Note that **you need to configure your DSN** (client key) only if you wish to initialize the SDK through the Log4j 2 integration. If you're planning to use `Sentry.init` to provide configuration, such as by using the `beforeSend` callback, you **should not** provide the DSN in both `Sentry.init` and the appender configuration; just leave it out of the appender configuration in this case.

```xml
<Sentry name="SENTRY" dsn="https://<key>@o<orgId>.ingest.sentry.io/<projectId>" />
```

If the DSN is not present in the `log4j2.xml` configuration, Sentry will attempt to read it from the system property `sentry.dsn`, environment variable `SENTRY_DSN` or the `dsn` property in `sentry.properties` file. [See the configuration page](https://docs.sentry.io/platforms/java/configuration.md) for more details on external configuration.

```properties
# Use Data Collection defaults but don't collect automatic user information.
# https://docs.sentry.io/platforms/java/guides/log4j2/data-management/data-collected/
data-collection.user-info=false
# Configure other data categories here.
// ___PRODUCT_OPTION_START___ logs
logs.enabled=true
// ___PRODUCT_OPTION_END___ logs
```

### [Minimum Log Level](https://docs.sentry.io/platforms/java/guides/log4j2.md#minimum-log-level)

Two log levels are used to configure this integration, as illustrated below in the provided code samples:

1. Configure the lowest level required for a log message to become an event (`minimumEventLevel`) sent to Sentry.
2. Configure the lowest level a message has to be to become a breadcrumb (`minimumBreadcrumbLevel`)

3) Configure the lowest level a message has to be to be sent as Sentry Log (`minimumLevel`).

Setting `minimumEventLevel` or `minimumBreadcrumbLevel` in `log4j2.xml` only affects events logged by way of Log4j2. The settings will have no effect when calling `Sentry.captureMessage` or similar directly.

Breadcrumbs are kept in memory (by default the last 100 records) and are sent with events. For example, by default, if you log 100 entries with `logger.info` or `logger.warn`, no event is sent to Sentry. If you then log with `logger.error`, an event is sent to Sentry that includes those 100 `info` or `warn` messages. For this to work, `SentryAppender` needs to receive **all** log entries to decide what to keep as breadcrumb or send as event. Set the `SentryAppender` log level configuration to a value lower than what is set for the `minimumBreadcrumbLevel` and `minimumEventLevel` so that `SentryAppender` receives these log messages.

```xml
<!-- Setting minimumBreadcrumbLevel modifies the default minimum level to add breadcrumbs from INFO to DEBUG  -->
<!-- Setting minimumEventLevel the default minimum level to capture an event from ERROR to WARN  -->
<Sentry name="SENTRY"
        dsn="https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
        minimumBreadcrumbLevel="DEBUG"
        minimumEventLevel="WARN"
        <!-- ___PRODUCT_OPTION_START___ logs  -->
        minimumLevel="DEBUG"
        <!-- ___PRODUCT_OPTION_END___ logs  -->
        />
```

```xml
<!-- Setting minimumBreadcrumbLevel modifies the default minimum level to add breadcrumbs from INFO to DEBUG  -->
<!-- Setting minimumEventLevel the default minimum level to capture an event from ERROR to WARN  -->
<Sentry name="SENTRY"
        minimumBreadcrumbLevel="DEBUG"
        minimumEventLevel="WARN"
        <!-- ___PRODUCT_OPTION_START___ logs -->
        minimumLevel="DEBUG"
        <!-- ___PRODUCT_OPTION_END___ logs  -->
        />
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

Learn more about setting up logging in our [Logs documentation](https://docs.sentry.io/platforms/java/guides/log4j2/logs.md).

## [Verify](https://docs.sentry.io/platforms/java/guides/log4j2.md#verify)

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

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/java/guides/log4j2/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/java/guides/log4j2.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

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

