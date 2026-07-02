---
title: "Create a page"
source: https://developers.notion.com/reference/post-page
path: reference/post-page
---

post /v1/pages
Use this API to create a new [page](/reference/page) as a child of an existing page or [data source](/reference/data-source).

### Use cases

#### Choosing a parent

In most cases, provide a `page_id` or `data_source` under the `parent` parameter to create a page under an existing [page](/reference/page), or [data source](/reference/data-source), respectively.

There is a 3rd option, available for [public connections](/guides/get-started/overview#connection-types) and [personal access tokens](/guides/get-started/personal-access-tokens): creating a private page at the workspace level. To do this, omit the `parent` parameter, or provide `parent[workspace]=true`. This can be useful for quickly creating pages that can then be organized manually in the Notion app later, helping you get to your life's work faster.

For internal connections, a page or data source parent is currently required in the API, because there is no one specific Notion user associated with them that could be used as the "owner" of the new private page.

#### Setting up page properties

If the new page is a child of an existing page,`title` is the only valid property in the `properties` body parameter.

If the new page is a child of an existing [data source](/reference/data-source), the keys of the `properties` object body param must match the parent [data source's properties](/reference/property-object).

#### Setting up page content

This endpoint can be used to create a new page with or without content using the `children` option. To add content to a page after creating it, use the [Append block children](/reference/patch-block-children) endpoint.

**Templates**: As an alternative to building up page content manually, the `template` body parameter can be used to specify an existing data source template to be used to populate the content and properties of the new page.

When omitted, the default is `template[type]=none`, which means no template is applied. The other options for `template[type]` are:

* `default`: Apply the data source's default template.
  * This is only allowed for pages created under a data source that has a default template configured in the Notion app.
* `template_id`: Provide a specific `template_id` to use as the blueprint for your page.
  * The API bot must have access to the template page, and it must be within the same workspace.
  * Although any valid page ID can be used as the `template[template_id]`, we recommend only using pages that are configured as actual [database templates](https://www.notion.com/help/database-templates) under the same data source as the parent of your new page to make sure that page properties can get merged in correctly.

When using `default` or `template_id`, you can optionally provide `template[timezone]` — an [IANA timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) string (e.g. `America/New_York`) — to control the timezone used when resolving template variables like `@now` and `@today`. If omitted, the associated user's timezone is used for public connections and personal access tokens, or UTC for internal connections. An invalid timezone returns a `validation_error`.

When applying a template, the `children` parameter is **not** allowed. The page is returned as blank initially in the API response, and then Notion's systems apply the template asynchronously after the API request finishes. For more information, see our full guide on [creating pages from templates](/guides/data-apis/creating-pages-from-templates).

### General behavior

Returns a new [page object](/reference/page).

When creating a page with the `markdown` body parameter, you can set `allow_async: true` to receive an HTTP `202` response with an `async_task` object instead of waiting for the page creation to finish in the original request. This is useful for high-block markdown requests that may take longer than typical HTTP client timeout budgets.

If `allow_async` is omitted or `false`, this endpoint keeps its existing synchronous response behavior. `allow_async` changes response behavior only; it does not change validation, permissions, or which operation runs. See [Retrieve an async task](/reference/retrieve-async-task) and [Working with markdown content](/guides/data-apis/working-with-markdown-content#running-large-markdown-writes-asynchronously) for polling examples.

<Tip>
  **Newlines in markdown content**

  When using the `markdown` body parameter, newlines must be encoded as `\n` in the JSON string — for example, `"# Heading\n\nParagraph"`. The interactive API explorer on this page does not support multiline input, so use cURL, an SDK, or any HTTP client that sends properly encoded JSON. When using cURL, wrap the `--data` body in **single quotes** (`'...'`) so that `\n` is preserved for the JSON parser.
</Tip>

<Warning>
  **Some page `properties` are not supported via the API**

  A request body that includes `rollup`, `created_by`, `created_time`, `last_edited_by`, or `last_edited_time` values in the properties object returns an error. These Notion-generated values cannot be created or updated via the API. If the `parent` contains any of these properties, then the new page’s corresponding values are automatically created.
</Warning>

<Info>
  **Requirements**

  Your connection must have [Insert Content capabilities](/reference/capabilities#content-capabilities) on the target parent page or database in order to call this endpoint. To update your connection's capabilities, navigate to the <a href={developerConnectionsUrl}>Developer portal</a>, select your connection, open the **Configuration** tab, and scroll to the Capabilities section.

  Attempting a query without update content capabilities returns an HTTP response with a 403 status code.
</Info>

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
