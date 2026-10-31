---
title: "Search"
source: https://docs.sentry.io/concepts/search.md
path: concepts/search
---

---
title: "Search"
description: "Learn more about how to search in Sentry, including the correct query syntax, searchable properties, and custom tags."
url: https://docs.sentry.io/concepts/search/
---

# Search | Sentry Docs

Search is available on several features throughout [sentry.io](https://sentry.io), such as **Issues**, **Errors**, **Traces**, and **Dashboards**.

## [Query Syntax](https://docs.sentry.io/concepts/search.md#query-syntax)

You'll only need to use query syntax if you're using a Sentry [API](https://docs.sentry.io/api.md). You'll get pre-populated suggestions once you start typing in your search terms when using the search bar anywhere in [Sentry.io](https://sentry.sentry.io/).

Search queries are constructed using a `key:value` pattern, with an optional raw search at the end. Each `key:value` pair is a `token` and the optional raw search is itself a single `token`. The `key:value` pair `tokens` are treated as issue or event properties. The optional raw search is treated as a single `token` and searches event titles/messages.

For example:

```bash
is:resolved user.username:"Jane Doe" server:web-8 example error
```

In the example above, there are three keys (`is:`, `user.username:`, `server:`), but four tokens:

* `is:resolved`
* `user.username:"Jane Doe"`
* `server:web-8`
* `example error`

The tokens `is:resolved` and `user.username:"Jane Doe"` are standard search tokens because both use reserved keywords. See [Issue Properties](https://docs.sentry.io/concepts/search/searchable-properties.md#issue-properties) and [Event Properties](https://docs.sentry.io/concepts/search/searchable-properties.md#event-properties) for appropriate keyword usage. The token `server:web-8` is pointing to a custom tag sent by the Sentry SDK. See [Custom Tags](https://docs.sentry.io/concepts/search/searchable-properties.md#custom-tags) for more information on how to set tags.

The token `example error` is utilizing the optional raw search and is passed as part of the issue search query (which uses a CONTAINS match similar to SQL). When using the optional raw search, you can provide *one* string, and the query uses that entire string.

Search terms should auto-complete, and when they don't, that means your term is incompatible with the dataset. If you complete the term and tap the Return/Enter key, an error message is displayed.

### [Comparison Operators](https://docs.sentry.io/concepts/search.md#comparison-operators)

Sentry search supports the use of comparison operators:

* greater than (**`>`**)
* less than (**`<`**)
* greater than or equal to (**`>=`**)
* less than or equal to (**`<=`**)

Typically, when you search using properties that are numbers or durations, you should use comparison operators rather than just a colon (`:`) to find exact matches, since an exact match isn't likely to exist.

Here are some examples of valid comparison operator searches:

* `event.timestamp:>2023-09-28T00:00:00-07:00`
* `count_dead_clicks:<=10`
* `span.duration:>5s`

### [Using `OR` and `AND`](https://docs.sentry.io/concepts/search.md#using-or-and-and)

`OR` and `AND` search conditions are only available for [Explore](https://docs.sentry.io/concepts/key-terms/enrich-data.md#explore), [Sentry Dashboards](https://docs.sentry.io/product/dashboards/sentry-dashboards.md), and [Monitors](https://docs.sentry.io/product/monitors-and-alerts/monitors.md).

Use `OR` and `AND` between tokens, and use parentheses `()` to group conditions. `AND` can also be used between non-aggregates and aggregates. However, `OR` cannot.

* Non-aggregates filter data based on specific tags or attributes. For example, `user.username:jane` is a non-aggregate field.

* Aggregates filter data on numerical scales. For example, `count()` is an aggregate function and `count():>100` is an aggregate filter.

Some examples of using the `OR` condition:

```bash
# a valid `OR` query
browser:Chrome OR browser:Opera

# an invalid `OR` query
user.username:janedoe OR count():>100
```

Also, the queries prioritize `AND` before `OR`. For example, "x `AND` y `OR` z" is the same as "(x `AND` y) `OR` z". Parentheses can be used to change the grouping. For example, "x `AND` (y `OR` z)".

### [Multiple Values on the Same Key](https://docs.sentry.io/concepts/search.md#multiple-values-on-the-same-key)

You can search multiple values for the same key by putting the values in a list. For example, "x:\[value1, value2]" will find the same results as "x:value1 `OR` x:value2". When you do this, the search returns issues/events that match any search term.

An example of searching on the same key with a list of values:

```bash
release:[12.0, 13.0]
```

Currently, you can't use this type of search on the keyword `is` and you can't use wildcards with this type of search.

### [Explicit Tag Syntax](https://docs.sentry.io/concepts/search.md#explicit-tag-syntax)

We recommend you never use reserved keywords (such as `project_id`) as tags. But if you do, you must use the following syntax to search for it:

```bash
tags[project_id]:tag_value
```

### [Advanced](https://docs.sentry.io/concepts/search.md#advanced)

Sentry also offers the following advanced search options:

#### [Exclusion](https://docs.sentry.io/concepts/search.md#exclusion)

By default, search terms use the `AND` operator; that is, they return the intersection of issues/events that match all search terms.

To change this, you can use the negation operator `!` to *exclude* a search parameter.

```bash
is:unresolved !user.email:example@customer.com
```

In the example above, the search query returns all Issues that are unresolved *and* have not affected the user with the email address `example@customer.com`.

#### [Wildcard Character](https://docs.sentry.io/concepts/search.md#wildcard-character)

Search supports the wildcard character `*` as a placeholder for specific characters and strings.

```bash
browser:"Safari 11*"
```

In the example above, the search query will match on `browser` values like `"Safari 11.0.2"`, `"Safari 11.0.3"`, etc.

You may also combine the wildcard character `*` with other operators like so:

```bash
!message:"*Timeout"
```

In the above example, the search query returns results which do not have message values like `ConnectionTimeout`, `ReadTimeout`, etc.

#### [Regular Expressions (logs only)](https://docs.sentry.io/concepts/search.md#regular-expressions-logs-only)

A regular expression (regex) is a pattern that describes a sequence of characters you want to find in text. They're useful when a plain value or a wildcard isn't precise enough, like finding every log message that starts with `Timeout after` followed by any number of milliseconds.

You can match a string attribute in [logs](https://docs.sentry.io/product/logs.md) against a regular expression.

In the search bar, add a filter for the attribute, open its operator dropdown, and choose **matches regex**, or **does not match regex** to exclude matching values.

In query syntax, wrap the pattern in double slashes: `key://pattern//`.

Without any special symbols, a pattern matches anywhere in the value. This matches both `Timeout after 30ms` and `Request Timeout`:

```bash
message://Timeout//
```

Patterns support [RE2 syntax](https://github.com/google/re2/wiki/Syntax) to define more specific matchers.

You can use either or both of `^` to match the start of the field's value, and/or `$` to match the end of the log. This matches only messages that start with "Timeout":

```bash
message://^Timeout//
```

`\d` is a character class, meaning it matches any one character from a set. `\d` matches any digit. This matches `Timeout after 1s` and `Timeout after 234ms`, but not `Timeout after a while`:

```bash
message://^Timeout after \d//
```

To exclude matching values, use the negation operator `!`. This excludes timeouts whose amounts start with `\w`, or word characters:

```bash
!message://^Timeout after \w//
```

Keep the following in mind when you write patterns:

* Regular expressions only work on string attributes in logs.
* Patterns use [RE2 syntax](https://github.com/google/re2/wiki/Syntax), which doesn't support lookarounds or backreferences.
* Patterns are case sensitive. Start a pattern with `(?i)` to ignore case.
* Patterns can be up to 64 characters long. An escape sequence like `\d` counts as one character.
* Spaces and parentheses inside a pattern don't need quotes.
* A pattern ends at the first `//` followed by a space, a `)`, or the end of the query. To match `//`, escape it as `\/\/`.
* There's no list form like `key:[value1, value2]`. Use `|` inside the pattern instead.
* To search for a literal value that starts with `//`, wrap it in quotes, like `url:"//cdn.example.com/"`.

## [Page Filters](https://docs.sentry.io/concepts/search.md#page-filters)

Page filters allow you to narrow down the results shown on a page by selecting specific projects, environments, and date ranges. After you've set your filters, they'll persist as you navigate across pages in Sentry.

### [Dashboard Page Filters](https://docs.sentry.io/concepts/search.md#dashboard-page-filters)

Dashboard page filters allow you to narrow down the widget results to certain projects, environments, date ranges, and releases. You can also add custom filters to your dashboard by pressing the *plus* button. Each filter begins with selecting a dataset, and then adding a filter condition.

### [Sentry Dashboards Page Filters](https://docs.sentry.io/concepts/search.md#sentry-dashboards-page-filters)

If you want to see data for all your projects, click "Clear" in the project selector to clear any project filters. Or search for specific data key value pairs by typing them in the search bar.

## [Learn more](https://docs.sentry.io/concepts/search.md#learn-more)

* #### [Searchable Properties](https://docs.sentry.io/concepts/search/searchable-properties.md)

  Learn more about searchable properties.

* #### [Saved Searches](https://docs.sentry.io/concepts/search/saved-searches.md)

  Learn more about default, recommended, and saved searches.

## Pages in this section

- [Searchable Properties](https://docs.sentry.io/concepts/search/searchable-properties.md)
- [Saved Searches](https://docs.sentry.io/concepts/search/saved-searches.md)

