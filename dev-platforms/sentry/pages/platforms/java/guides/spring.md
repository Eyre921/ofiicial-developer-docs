---
title: "Spring"
source: https://docs.sentry.io/platforms/java/guides/spring.md
path: platforms/java/guides/spring
---

---
title: "Spring"
description: "Learn how to use Sentry's Spring SDK."
url: https://docs.sentry.io/platforms/java/guides/spring/
---

# Sentry for Spring

There are multiple variants of Sentry available for Spring:

* For Spring 5, use `sentry-spring` ([GitHub](https://github.com/getsentry/sentry-java/tree/master/sentry-spring))
* For Spring 6, use `sentry-spring-jakarta` ([GitHub](https://github.com/getsentry/sentry-java/tree/master/sentry-spring-jakarta))
* For Spring 7, use `sentry-spring-7` ([GitHub](https://github.com/getsentry/sentry-java/tree/main/sentry-spring-7))

Sentry's integration with [Spring](https://spring.io/projects/spring-framework) supports Spring Framework 5.1.2 and above to report unhandled exceptions and optional user information. If you're on an older version, use [our legacy integration](https://docs.sentry.io/platforms/java/legacy/spring.md). The minimum version of Spring Framework supported by the Sentry WebFlux integration is, instead, 5.2.4.

* Provides a [HandlerExceptionResolver](https://docs.spring.io/spring/docs/4.3.9.RELEASE/javadoc-api/org/springframework/web/servlet/HandlerExceptionResolver.html) to send unhandled exceptions to Sentry
* Attaches HTTP request information to every `SentryEvent` recorded within the scope of the request
* Provides the ability to [record user information](https://docs.sentry.io/platforms/java/guides/spring/advanced-usage.md)

To use Sentry with **Spring Boot**, we recommend using Sentry [Spring Boot integration](https://docs.sentry.io/platforms/java/guides/spring-boot.md) as it provides richer configuration capabilities.

On this page, we get you up and running with Sentry's SDK.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/java/guides/spring.md#install)

Sentry captures data by using an SDK within your application’s runtime.

Error Monitoring\[ ]Tracing\[ ]Profiling\[ ]Logs\[x]OpenTelemetry

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

**Gradle (Spring 5)**

```groovy
implementation 'io.sentry:sentry-spring:8.61.1'
// ___PRODUCT_OPTION_START___ profiling
implementation 'io.sentry:sentry-async-profiler:8.61.1'
// ___PRODUCT_OPTION_END___ profiling
```

**Gradle (Spring 6)**

```groovy
implementation 'io.sentry:sentry-spring-jakarta:8.61.1'
// ___PRODUCT_OPTION_START___ profiling
implementation 'io.sentry:sentry-async-profiler:8.61.1'
// ___PRODUCT_OPTION_END___ profiling
```

**Gradle (Spring 7)**

```groovy
implementation 'io.sentry:sentry-spring-7:8.61.1'
// ___PRODUCT_OPTION_START___ profiling
implementation 'io.sentry:sentry-async-profiler:8.61.1'
// ___PRODUCT_OPTION_END___ profiling
```

**Maven (Spring 5)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring</artifactId>
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

**Maven (Spring 6)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring-jakarta</artifactId>
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

**Maven (Spring 7)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring-7</artifactId>
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

**SBT (Spring 5)**

```scala
libraryDependencies += "io.sentry" % "sentry-spring" % "8.61.1"
// ___PRODUCT_OPTION_START___ profiling
libraryDependencies += "io.sentry" % "sentry-async-profiler" % "8.61.1"
// ___PRODUCT_OPTION_END___ profiling
```

**SBT (Spring 6)**

```scala
libraryDependencies += "io.sentry" % "sentry-spring-jakarta" % "8.61.1"
// ___PRODUCT_OPTION_START___ profiling
libraryDependencies += "io.sentry" % "sentry-async-profiler" % "8.61.1"
// ___PRODUCT_OPTION_END___ profiling
```

**SBT (Spring 7)**

```scala
libraryDependencies += "io.sentry" % "sentry-spring-7" % "8.61.1"
// ___PRODUCT_OPTION_START___ profiling
libraryDependencies += "io.sentry" % "sentry-async-profiler" % "8.61.1"
// ___PRODUCT_OPTION_END___ profiling
```

For other dependency managers see the [central Maven repository (Spring 5)](https://search.maven.org/artifact/io.sentry/sentry-spring), [central Maven repository (Spring 6)](https://search.maven.org/artifact/io.sentry/sentry-spring-jakarta), and [central Maven repository (Spring 7)](https://search.maven.org/artifact/io.sentry/sentry-spring-7).

We recommend using our Gradle plugin as it can add integrations and provide source context for events.

If you are manually adding multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

When running your application, please add our `sentry-opentelemetry-agent` to the `java` command. In case you are using an application server to run your `.WAR` file, please add it to the `JAVA_OPTS` of your application server.

Download the latest version of the `sentry-opentelemetry-agent-8.61.1.jar` from [MavenCentral](https://search.maven.org/artifact/io.sentry/sentry-opentelemetry-agent):

```bash
curl https://repo1.maven.org/maven2/io/sentry/sentry-opentelemetry-agent/8.61.1/sentry-opentelemetry-agent-8.61.1.jar -o sentry-opentelemetry-agent-8.61.1.jar
```

Then run your application with:

```bash
SENTRY_AUTO_INIT=false JAVA_TOOL_OPTIONS="-javaagent:sentry-opentelemetry-agent-8.61.1.jar" java -jar your-application.jar
```

*Other available variations of the above snippet: Java CLI argument*

In case of an application server, adding the Agent might look more like the following:

```bash
JAVA_OPTS="${JAVA_OPTS} JAVA_TOOL_OPTIONS="-javaagent:sentry-opentelemetry-agent-8.61.1.jar"
```

*Other available variations of the above snippet: Java CLI argument*

## [Configure](https://docs.sentry.io/platforms/java/guides/spring.md#configure)

Configuration should happen as early as possible in your application's lifecycle.

The `sentry-spring`, `sentry-spring-jakarta`, and `sentry-spring-7` libraries provide an `@EnableSentry` annotation that registers all required Spring beans. `@EnableSentry` can be placed on any class annotated with [@Configuration](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/context/annotation/Configuration.html) including the main entry class in Spring Boot applications annotated with [@SpringBootApplication](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/autoconfigure/SpringBootApplication.html).

**Java (Spring 5)**

```java
import io.sentry.spring.EnableSentry;
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
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
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
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
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
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
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
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
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
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
// NOTE: Replace the test DSN below with YOUR OWN DSN to see the events from this app in your Sentry
// project/dashboard
@EnableSentry(
  dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
)
@Configuration
class SentryConfiguration
```

Configure Data Collection in `sentry.properties`. Setting any Data Collection field applies its defaults to omitted fields:

```properties
# Use Data Collection defaults but don't collect automatic user information.
data-collection.user-info=false
# Configure other data categories here.
```

The DSN can be also provided through the system property `sentry.dsn`, environment variable `SENTRY_DSN` or the `dsn` property in `sentry.properties` file. [See the configuration page](https://docs.sentry.io/platforms/java/configuration.md) for more details on external configuration.

Once this integration is configured you can *also* use Sentry’s static API, [as shown on the usage page](https://docs.sentry.io/platforms/java/guides/spring/usage.md), to record breadcrumbs, set the current user, or manually send events, for example.

By default, only unhandled exceptions are sent to Sentry. This behavior can be tuned through configuring the `exceptionResolverOrder` property. For example, setting it to `Ordered#HIGHEST_PRECEDENCE` ensures exceptions that have been handled by exception resolvers with higher order are sent to Sentry - including ones handled by `@ExceptionHandler` annotated methods.

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

The SDK can be configured using a `sentry.properties` file:

```properties
// ___PRODUCT_OPTION_START___ performance
# Enable tracing
traces-sample-rate=1.0
// ___PRODUCT_OPTION_END___ performance
// ___PRODUCT_OPTION_START___ profiling
# Enable profiling
profile-session-sample-rate=1.0
profile-lifecycle=TRACE
// ___PRODUCT_OPTION_END___ profiling
// ___PRODUCT_OPTION_START___ logs
# Enable logs
logs.enabled=true
// ___PRODUCT_OPTION_END___ logs
```

## [Verify](https://docs.sentry.io/platforms/java/guides/spring.md#verify)

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

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/java/guides/spring/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/java/guides/spring.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

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

