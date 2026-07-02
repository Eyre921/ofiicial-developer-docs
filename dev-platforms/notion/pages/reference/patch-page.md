---
title: "Update page"
source: https://developers.notion.com/reference/patch-page
path: reference/patch-page
---

patch /v1/pages/{page_id}
Use this API to modify attributes of a Notion page, such as its properties, icon, or cover.

### Use cases

#### Updating properties

To change the `properties` of a page in a data source, use the `properties` body parameter. This parameter can only be used if the page's parent is a [data source](/reference/data-source), aside from updating the `title` of a page outside of a data source.

The page’s `properties` schema must match the parent [data source's properties](/reference/property-object).

#### Setting the icon, cover, or "in trash" status

This endpoint can be used to update any page `icon` or `cover`, and can be used to [trash](/reference/trash-page) or restore any page.

#### Locking and unlocking a page

Use the `is_locked` boolean parameter to lock or unlock the page from being further edited in the Notion app UI. Note that this setting doesn't affect the ability to update the page using the API.

#### Applying a page template

Use the `template` body parameter object to apply a [template](/guides/data-apis/creating-pages-from-templates) to an existing page. This can either be the parent data source's default template (`type=default`), or a specific template (`type=template_id`).

You can optionally provide `template[timezone]` — an [IANA timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) string (e.g. `America/New_York`) — to control the timezone used when resolving template variables like `@now` and `@today`. If omitted, the associated user's timezone is used for public connections and personal access tokens, or UTC for internal connections.

After the API request finishes, Notion's systems merge the content and properties from your chosen template into the current page.

For more information, visit our related guide: [Creating pages from templates](/guides/data-apis/creating-pages-from-templates).

#### Erasing content from a page

Use the `erase_content` flag to delete all block children of the current page. **Use caution** with this parameter, since this is a destructive action that **cannot** be reversed using the API.

The main use case is for applying a `template` in scenarios where it makes sense to clear all of the existing page content and replace it with the template page's content, instead of appending the template content to what's already on the page.

#### Adding content to a page

To add content, use the [append block children](/reference/patch-block-children) API instead. The `page_id` can be passed as the `block_id` when adding block children to the page.

### General behavior

Returns the updated [page object](/reference/page).

<Info>
  **Requirements**

  Your connection must have [update content capabilities](/reference/capabilities#content-capabilities) on the target page in order to call this endpoint. To update your connection's capabilities, navigate to the <a href={developerConnectionsUrl}>Developer portal</a>, select your connection, open the **Configuration** tab, and scroll to the Capabilities section.

  Attempting a query without update content capabilities returns an HTTP response with a 403 status code.
</Info>

<Warning>
  **Limitations**

  * Updating [rollup property values](/reference/page-property-values#rollup) is not supported.
  * A page’s `parent` cannot be changed.
</Warning>

### Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
