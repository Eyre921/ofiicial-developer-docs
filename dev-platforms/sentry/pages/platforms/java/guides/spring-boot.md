---
title: "Spring Boot"
source: https://docs.sentry.io/platforms/java/guides/spring-boot.md
path: platforms/java/guides/spring-boot
---

---
title: "Spring Boot"
description: "Learn how to use Sentry's Spring Boot SDK."
url: https://docs.sentry.io/platforms/java/guides/spring-boot/
---

# Sentry for Spring Boot

There are multiple variants of Sentry available for Spring Boot. If you're using our Gradle plugin it will pick the right dependency for you. If you're manually adding the dependency:

* For Spring Boot 2, use `sentry-spring-boot-starter` ([GitHub](https://github.com/getsentry/sentry-java/tree/main/sentry-spring-boot-starter))
* For Spring Boot 3, use `sentry-spring-boot-starter-jakarta` ([GitHub](https://github.com/getsentry/sentry-java/tree/main/sentry-spring-boot-starter-jakarta))
* For Spring Boot 4, use `sentry-spring-boot-4` ([GitHub](https://github.com/getsentry/sentry-java/tree/main/sentry-spring-boot-4))

Sentry's integration with [Spring Boot](https://spring.io/projects/spring-boot) supports Spring Boot 2.1.0 and above to report unhandled exceptions as well as release and registration of beans. If you're on an older version, use [our legacy integration](https://docs.sentry.io/platforms/java/legacy/spring.md). The minimum version of Spring Boot supported by the Sentry WebFlux integration is, instead, 2.2.5.RELEASE.

The `sentry-spring-boot-starter`, `sentry-spring-boot-starter-jakarta`, and `sentry-spring-boot-4` libraries enhance [Sentry Spring](https://docs.sentry.io/platforms/java/guides/spring.md) to:

* manage a fine-grained configuration using `application.properties` or `application.yaml`
* automatically include the release when [Spring Boot Git integration is configured](https://docs.spring.io/spring-boot/how-to/build.html#howto.build.generate-git-info)
* automatically register `BeforeSendCallback`, `BeforeBreadcrumbCallback`, `EventProcessor`, `Integration` beans

On this page, we get you up and running with Sentry's SDK.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/java/guides/spring-boot.md#install)

Sentry captures data by using an SDK within your application’s runtime.

Error Monitoring\[ ]Tracing\[ ]Profiling\[ ]Logs\[x]OpenTelemetry

**Gradle Plugin**

```groovy
plugins {
  id "io.sentry.jvm.gradle" version "6.25.0"
}
// ___PRODUCT_OPTION_START___ profiling
dependencies {
  implementation 'io.sentry:sentry-async-profiler:8.62.0'
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
      <version>8.62.0</version>
  </dependency>
</dependencies>
// ___PRODUCT_OPTION_END___ profiling
```

**Gradle (Spring Boot 2)**

```groovy
implementation 'io.sentry:sentry-spring-boot-starter:8.62.0'
// ___PRODUCT_OPTION_START___ profiling
implementation 'io.sentry:sentry-async-profiler:8.62.0'
// ___PRODUCT_OPTION_END___ profiling
```

**Gradle (Spring Boot 3)**

```groovy
implementation 'io.sentry:sentry-spring-boot-starter-jakarta:8.62.0'
// ___PRODUCT_OPTION_START___ profiling
implementation 'io.sentry:sentry-async-profiler:8.62.0'
// ___PRODUCT_OPTION_END___ profiling
```

**Gradle (Spring Boot 4)**

```groovy
implementation 'io.sentry:sentry-spring-boot-4:8.62.0'
// ___PRODUCT_OPTION_START___ profiling
implementation 'io.sentry:sentry-async-profiler:8.62.0'
// ___PRODUCT_OPTION_END___ profiling
```

**Maven (Spring Boot 2)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring-boot-starter</artifactId>
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

**Maven (Spring Boot 3)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring-boot-starter-jakarta</artifactId>
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

**Maven (Spring Boot 4)**

```xml
<dependency>
    <groupId>io.sentry</groupId>
    <artifactId>sentry-spring-boot-4</artifactId>
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

We recommend using our Gradle plugin as it can add integrations and provide source context for events.

If you are manually adding multiple Sentry dependencies, you can add a [bill of materials](https://docs.sentry.io/platforms/java/configuration/bill-of-materials.md) to avoid specifying the version of each dependency.

When running your application, please add our `sentry-opentelemetry-agent` to the `java` command.

Download the latest version of the `sentry-opentelemetry-agent-8.62.0.jar` from [MavenCentral](https://search.maven.org/artifact/io.sentry/sentry-opentelemetry-agent):

```bash
curl https://repo1.maven.org/maven2/io/sentry/sentry-opentelemetry-agent/8.62.0/sentry-opentelemetry-agent-8.62.0.jar -o sentry-opentelemetry-agent-8.62.0.jar
```

Then run your application with:

```bash
SENTRY_AUTO_INIT=false JAVA_TOOL_OPTIONS="-javaagent:sentry-opentelemetry-agent-8.62.0.jar" java -jar your-application.jar
```

*Other available variations of the above snippet: Java CLI argument*

## [Configure](https://docs.sentry.io/platforms/java/guides/spring-boot.md#configure)

Sentry's Spring Boot integration auto-configures `sentry.in-app-packages` property with the package where `@SpringBootApplication` or `@SpringBootConfiguration` annotated class is located.

Provide a `sentry.dsn` property using either `application.properties` or `application.yml`:

```properties
sentry.dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>

# Use Data Collection defaults but don't collect automatic user information.
# https://docs.sentry.io/platforms/java/guides/spring-boot/data-management/data-collected/
sentry.data-collection.user-info=false
# Configure other data categories here.
# ___PRODUCT_OPTION_START___ performance

# Set traces_sample_rate to 1.0 to capture 100%
# of transactions for tracing.
# We recommend adjusting this value in production.
sentry.traces-sample-rate=1.0
# ___PRODUCT_OPTION_END___ performance
// ___PRODUCT_OPTION_START___ profiling

# Enable profiling
sentry.profile-session-sample-rate=1.0
sentry.profile-lifecycle=TRACE
// ___PRODUCT_OPTION_END___ profiling
// ___PRODUCT_OPTION_START___ logs

# Enable logs
sentry.logs.enabled=true
// ___PRODUCT_OPTION_END___ logs
```

*Other available variations of the above snippet: yaml*

By default, only unhandled exceptions are sent to Sentry. This behavior can be tuned through configuring the `sentry.exception-resolver-order` property. For example, setting it to `-2147483647` (the value of `org.springframework.core.Ordered#HIGHEST_PRECEDENCE`) ensures exceptions that have been handled by exception resolvers with higher order are sent to Sentry - including ones handled by `@ExceptionHandler` annotated methods.

```properties
sentry.exception-resolver-order=-2147483647
```

*Other available variations of the above snippet: yaml*

We recommend using Sentry's Spring Boot integration with one of the [logging framework integrations](https://docs.sentry.io/platforms/java/guides/spring-boot/logging-frameworks.md) as they work together seamlessly. To use Sentry **without** Spring Boot, we recommend using the [Sentry Spring integration](https://docs.sentry.io/platforms/java/guides/spring.md).

Once this integration is configured you can *also* use Sentry’s static API, [as shown on the usage page](https://docs.sentry.io/platforms/java/guides/spring-boot/usage.md), to record breadcrumbs, set the current user, or manually send events, for example.

## [Verify](https://docs.sentry.io/platforms/java/guides/spring-boot.md#verify)

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

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/java/guides/spring-boot/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/java/guides/spring-boot.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other Java Frameworks

- [java.util.logging](https://docs.sentry.io/platforms/java/guides/jul.md)
- [Log4j 2.x](https://docs.sentry.io/platforms/java/guides/log4j2.md)
- [Logback](https://docs.sentry.io/platforms/java/guides/logback.md)
- [Servlet](https://docs.sentry.io/platforms/java/guides/servlet.md)
- [Spring](https://docs.sentry.io/platforms/java/guides/spring.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/java/guides/spring-boot/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/java/guides/spring-boot/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/java/guides/spring-boot/configuration.md)
- [Logs](https://docs.sentry.io/platforms/java/guides/spring-boot/logs.md)
- [Integrations](https://docs.sentry.io/platforms/java/guides/spring-boot/integrations.md)
- [Tracing](https://docs.sentry.io/platforms/java/guides/spring-boot/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/java/guides/spring-boot/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/java/guides/spring-boot/data-management.md)
- [Async Methods](https://docs.sentry.io/platforms/java/guides/spring-boot/async.md)
- [Record User Information](https://docs.sentry.io/platforms/java/guides/spring-boot/record-user.md)
- [Profiling](https://docs.sentry.io/platforms/java/guides/spring-boot/profiling.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/java/guides/spring-boot/security-policy-reporting.md)
- [Crons](https://docs.sentry.io/platforms/java/guides/spring-boot/crons.md)
- [Advanced Usage](https://docs.sentry.io/platforms/java/guides/spring-boot/advanced-usage.md)
- [User Feedback](https://docs.sentry.io/platforms/java/guides/spring-boot/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/java/guides/spring-boot/feature-flags.md)
- [Source Context](https://docs.sentry.io/platforms/java/guides/spring-boot/source-context.md)
- [Gradle](https://docs.sentry.io/platforms/java/guides/spring-boot/gradle.md)
- [Maven](https://docs.sentry.io/platforms/java/guides/spring-boot/maven.md)
- [WebFlux Integration](https://docs.sentry.io/platforms/java/guides/spring-boot/webflux.md)
- [Logging Framework Integrations](https://docs.sentry.io/platforms/java/guides/spring-boot/logging-frameworks.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/java/guides/spring-boot/opentelemetry.md)
- [Migration Guides](https://docs.sentry.io/platforms/java/guides/spring-boot/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/java/guides/spring-boot/troubleshooting.md)
- [Legacy SDK (1.7)](https://docs.sentry.io/platforms/java/guides/spring-boot/legacy.md)

