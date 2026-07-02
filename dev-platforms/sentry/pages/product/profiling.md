---
title: "Profiling"
source: https://docs.sentry.io/product/profiling.md
path: product/profiling
---

---
title: "Profiling"
description: "Profiling offers a deeper level of visibility on top of traditional tracing, removing the need for custom instrumentation and enabling precise code-level visibility into your application in a production environment."
url: https://docs.sentry.io/product/profiling/
---

# Profiling

Sentry’s Profiling products provide precise, code-level visibility into application execution in a production environment.

## [When Should You Use Profiling?](https://docs.sentry.io/product/profiling.md#when-should-you-use-profiling)

Profiling helps you understand where time is being spent in your application at a **function level**. While [tracing](https://docs.sentry.io/concepts/key-terms/tracing.md) can help you capture information about the higher level operations (HTTP requests, database queries, UI rendering, etc.) that consume time in your application, profiling helps you debug performance by visualizing the call stacks on every thread, throughout the execution of your application.

This is especially helpful in situations where you are missing explicit instrumentation (spans and logs) that might help you narrow in on where an issue is occurring. Profiling requires *no additional instrumentation* and will automatically capture information on the functions and lines of code that take the most time as your application runs.

Profiling helps you quickly identify performance bottlenecks, enabling you to build in [performance as a feature](https://blog.codinghorror.com/performance-is-a-feature/) from day one.

## [Profiling Products](https://docs.sentry.io/product/profiling.md#profiling-products)

**The currently supported platforms are:**

* [Android (Java and Kotlin only)](https://docs.sentry.io/platforms/android/profiling.md)
* [iOS and macOS (Swift and Objective-C only)](https://docs.sentry.io/platforms/apple/profiling.md)
* [Python](https://docs.sentry.io/platforms/python/profiling.md)
* [Node.js](https://docs.sentry.io/platforms/javascript/guides/node/profiling.md)
* [PHP (including Laravel and Symfony)](https://docs.sentry.io/platforms/php/profiling.md)
* [Browser JavaScript \[beta\]](https://docs.sentry.io/platforms/javascript/profiling.md)
* [Ruby \[beta\]](https://docs.sentry.io/platforms/ruby/profiling.md)
* [React Native \[beta\]](https://docs.sentry.io/platforms/react-native/profiling.md)
* [Flutter \[experimental, iOS and macOS only\]](https://docs.sentry.io/platforms/dart/guides/flutter/profiling.md)
* [.NET \[experimental\]](https://docs.sentry.io/platforms/dotnet/profiling.md)
* [JVM (Java and other JVM based languages)](https://docs.sentry.io/platforms/java/profiling.md)

Sentry supports profiling for both backend and frontend use cases with two products:

* **Continuous Profiling** enables *continuously* profiling backend services to find code paths that are causing excessive resource usage and high infrastructure cost.
* **UI Profiling** enables profiling critical user flows (or entire user sessions) in browser and [mobile](https://docs.sentry.io/product/profiling/mobile-app-profiling.md) apps to find code paths that are causing janky scrolling and animations, high interaction latency, and slow load times that contribute to a poor user experience.

## [Profiling Page](https://docs.sentry.io/product/profiling.md#profiling-page)

On the [**Profiling**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page, you’ll find high level metrics on the slowest functions in the selected project(s), as well as any functions that have regressed or improved in performance within the selected time range.

On the **Slowest Functions** widget, you can click on the ellipses button (...) on each function to see a list of example profiles containing that function. On the **Most Regressed/Improved Functions** widget, you can click on the function duration before & after the change to see before & after example profiles containing that function.

Below the function metrics, you’ll find two tabs: **Transactions** and **Aggregate Flamegraph**.

If [tracing](https://docs.sentry.io/concepts/key-terms/tracing.md) is enabled, **Transactions** shows a list of all of the transactions instrumented in the selected projects, allowing you to break down profiling data by endpoints, routes, user flows, etc. It gives you a more focused view of application performance within a *specific* part of the application.

The **Aggregate Flamegraph** tab does *not* require tracing to be enabled, and will show you a high level view of all of the most frequent code paths within the selected projects. This gives you a more general view of where time is being spent overall in a service or application.

### [Transactions Tab](https://docs.sentry.io/product/profiling.md#transactions-tab)

The transactions list will not be populated if tracing is not enabled for at least one of the selected projects.

The **Transactions** tab, by default, shows a list of all transactions in the selected projects sorted by the frequency (count) of the transaction. The list can also be sorted by duration (p50/75/90/95), project, timestamp, etc. by clicking on the column headers in the table. The transactions list can also be filtered by specifying a query using the search bar. For example, you can search for transactions from specific users or transactions that are tagged with a custom attribute.

Click the name of a transaction to navigate to the **Transaction Summary** page, which contains aggregated performance data that is scoped to that transaction. By default, the **Profiles** tab is selected, which contains an [aggregate flame graph](https://docs.sentry.io/product/profiling/flame-charts-graphs.md) showing the most frequent code paths that were profiled within that transaction. This flame graph behaves the same as the flame graph in the **Aggregate Flamegraph** tab described below.

### [Aggregate Flamegraph Tab](https://docs.sentry.io/product/profiling.md#aggregate-flamegraph-tab)

The **Aggregate Flamegraph** tab shows a [flame graph](https://docs.sentry.io/product/profiling/flame-charts-graphs.md) with aggregated information on the frequency of code paths within the selected projects.

The wider frames represent more **frequent** code paths, which are likely more relevant optimization opportunities. You can click on a frame to select it, which will populate the sidebar on the right with links to example profiles containing the selected function.

## [Zooming Into Traces Using Profiling](https://docs.sentry.io/product/profiling.md#zooming-into-traces-using-profiling)

If you are already looking at a trace and have insufficient information to debug the root cause of the problem, profiling data can help fill in the gaps. If there is profiling data associated with the trace, there are two ways to get to it from the [**Trace View**](https://docs.sentry.io/concepts/key-terms/tracing/trace-view.md).

One way is to select a span and scroll down to the **Profile** section of the span details:

The **Most Frequent Stacks in this Span** widget shows a paginated list of call stacks in descending order of frequency that indicates where in the code most of the time in the selected span is spent. Click the **>** button to page through the other stacks, or click the **Profile** button to view the entire profile in the flame graph viewer.

The other way is to click the **Profiles** tab in the Trace View, which will show a list a profile events across *all* spans contained within the trace:

## [Getting Started](https://docs.sentry.io/product/profiling.md#getting-started)

Read the [Getting Started guide](https://docs.sentry.io/product/profiling/getting-started.md) to start using Continuous Profiling and UI Profiling.

* #### [Set Up](https://docs.sentry.io/product/profiling/getting-started.md)

  Get started with Profiling, which allows you to see code-level profiling information for your Sentry apps.

* #### [Profiling Performance Overhead](https://docs.sentry.io/product/profiling/performance-overhead.md)

  Learn more about how enabling Profiling impacts the performance of your application.

* #### [Mobile App Profiling](https://docs.sentry.io/product/profiling/mobile-app-profiling.md)

  Get started with Mobile App Profiling, which allows you to see code-level profiling information for your mobile apps.

* #### [Profile Details](https://docs.sentry.io/product/profiling/profile-details.md)

  Learn how to explore your profile data using the Profile Details page.

* #### [Flame Graphs and Aggregated Flame Graphs](https://docs.sentry.io/product/profiling/flame-charts-graphs.md)

  Learn more about how to interpret flame graphs and aggregated flame graphs.

* #### [Differential Flame Graphs](https://docs.sentry.io/product/profiling/differential-flamegraphs.md)

  Learn how to use and interpret differential flame graphs.

* #### [Transaction vs. Continuous & UI Profiling](https://docs.sentry.io/product/profiling/transaction-vs-continuous-profiling.md)

  Learn about the differences between transaction-based Profiling and the new Continuous & UI Profiling products.

* #### [Continuous & UI Profiling Migration Guide](https://docs.sentry.io/product/profiling/continuous-ui-profiling-migration-guide.md)

  Learn how to migrate from the older transaction-based Profiling API to the new Continuous and UI Profiling APIs.

## Pages in this section

- [Set Up](https://docs.sentry.io/product/profiling/getting-started.md)
- [Profiling Performance Overhead](https://docs.sentry.io/product/profiling/performance-overhead.md)
- [Mobile App Profiling](https://docs.sentry.io/product/profiling/mobile-app-profiling.md)
- [Profile Details](https://docs.sentry.io/product/profiling/profile-details.md)
- [Flame Graphs and Aggregated Flame Graphs](https://docs.sentry.io/product/profiling/flame-charts-graphs.md)
- [Differential Flame Graphs](https://docs.sentry.io/product/profiling/differential-flamegraphs.md)
- [Transaction vs. Continuous & UI Profiling](https://docs.sentry.io/product/profiling/transaction-vs-continuous-profiling.md)
- [Continuous & UI Profiling Migration Guide](https://docs.sentry.io/product/profiling/continuous-ui-profiling-migration-guide.md)

