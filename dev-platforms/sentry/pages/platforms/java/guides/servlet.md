---
title: "Servlet"
source: https://docs.sentry.io/platforms/java/guides/servlet.md
path: platforms/java/guides/servlet
---

---
title: "Servlet"
url: https://docs.sentry.io/platforms/java/guides/servlet/
---

# Sentry for Servlet

Sentry's Java SDK enables capturing sessions for Release health as well as reporting messages and errors.

Sentry for Java is a collection of modules provided by Sentry; it supports Java 1.8 and above. At its core, Sentry for Java provides a raw client for sending events to Sentry. To begin, we **highly recommend** you use one of the logging libraries or framework integrations.

The Sentry Java SDK can be used with Kotlin, Scala, and other JVM languages. Code examples are typically provided in both Java and Kotlin.

On this page, we get you up and running with Sentry's SDK.

##### Using a framework?

Check out the other SDKs we support in the left-hand dropdown.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/java/guides/servlet.md#install)

Sentry captures data by using an SDK within your application’s runtime.

Error Monitoring\[ ]Tracing\[ ]Profiling\[ ]Logs\[x]OpenTelemetry

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-servlet</artifactId>
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

For other dependency managers, see the [central Maven repository](https://search.maven.org/artifact/io.sentry/sentry-servlet).

`sentry-servlet` module comes with a `ServletContainerInitializer` that registers a `ServletRequestListener` which enhances each Sentry event triggered within the scope of HTTP request with a request information like HTTP method, query string, url and HTTP headers.

If you are using multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

### [Jakarta support](https://docs.sentry.io/platforms/java/guides/servlet.md#jakarta-support)

We also provide a module called `sentry-servlet-jakarta` if you want to use `jakarta.servlet-api` instead of `javax.servlet-api`.

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

## [Configure](https://docs.sentry.io/platforms/java/guides/servlet.md#configure)

Configuration should happen as early as possible in your application's lifecycle.

The following example configures a `SentryInitializer` servlet container initializer that initializes Sentry on application startup.

```java
package sentry.sample;

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
      // https://docs.sentry.io/platforms/java/guides/servlet/data-management/data-collected/
      options.getDataCollection().forceDataCollection();
      options.getDataCollection().setUserInfo(false);
      // Configure other data categories here.
      // ___PRODUCT_OPTION_START___ performance

      // Set traces_sample_rate to 1.0 to capture 100%
      // of transactions for tracing.
      // We recommend adjusting this value in production.
      options.setTracesSampleRate(1.0);
      // ___PRODUCT_OPTION_END___ performance
      // ___PRODUCT_OPTION_START___ profiling

      // Enable profiling
      options.setProfileSessionSampleRate(1.0);
      options.setProfileLifecycle(ProfileLifecycle.TRACE);
      // ___PRODUCT_OPTION_END___ profiling
      // ___PRODUCT_OPTION_START___ logs

      // Enable logs to be sent to Sentry
      options.getLogs().setEnabled(true);
      // ___PRODUCT_OPTION_END___ logs
    });
  }
}
```

*Other available variations of the above snippet: kotlin*

Learn more about setting up logging in our [Logs documentation](https://docs.sentry.io/platforms/java/guides/servlet/logs.md).

Create a file in `src/main/resources/META-INF/services` named `javax.servlet.ServletContainerInitializer`, with a full name of your custom `SentryInitializer` class as a content:

```properties
sentry.sample.SentryInitializer
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

Learn more about setting up logging in our [Logs documentation](https://docs.sentry.io/platforms/java/guides/servlet/logs.md).

## [Verify](https://docs.sentry.io/platforms/java/guides/servlet.md#verify)

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

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/java/guides/servlet/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/java/guides/servlet.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

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

