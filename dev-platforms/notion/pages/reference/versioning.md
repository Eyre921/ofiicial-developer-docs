---
title: "Versioning"
source: https://developers.notion.com/reference/versioning
path: reference/versioning
---

Learn about API change management and how to set the appropriate version in your connection.

The Notion API is versioned. Our API versions are named for the date the version is released. For example, our latest version is .

Set the version by including a `Notion-Version` header. Setting this header is **required**.

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.notion.com/v1/users/01da9b00-e400-4959-91ce-af55307647e5 \
    -H "Authorization: Bearer secret_t1CdN9S8yicG5eWLUOfhcWaOscVnFXns"
    -H "Notion-Version: 2026-03-11"
  ```

  ```javascript JavaScript theme={null}
  // If you're using the JavaScript SDK, the appropriate
  // Notion-Version header will be set for you.
  const { Client } = require('@notionhq/client');

  // To override the default version, pass the `notionVersion` argument
  // when initializing the `Client`. For example:
  //
  // const notion = new Client({
  //   auth: process.env.NOTION_ACCESS_TOKEN,
  //   notionVersion: "2026-03-11"
  // });
  const notion = new Client({ auth: process.env.NOTION_ACCESS_TOKEN });
  ```
</CodeGroup>

A new API version is released when we introduce a **backwards-incompatible** change to the API. For example, changing a property type's name.

<CodeGroup>
  ```json JSON theme={null}
  // Prior to version 2021-05-13, the rich text property is called "text"
  "properties": {
  	"Description": {
  		"type": "text",
  		"text": [/* ... */]
  	}
  }

  // In version 2021-05-13, the rich text property is now called "rich_text"
  "properties": {
  	"Description": {
  		"type": "rich_text",
  		"rich_text": [/* ... */]
  	}
  }
  ```
</CodeGroup>

In the above example, if you do not upgrade to the new version, you will continue to set text properties using `text` when creating or updating a page. Once you upgrade to the new version, you will need to use `rich_text` to set that same text property.

Similarly, the page response will be returned with the property type `text` on the old version, while on the new version, the response will say `rich_text`.

<Warning>
  **Required Header**

  The `Notion-Version` header must be included in all REST API requests. This ensures the Notion API response is consistent with what your code expects.

  The most recent `Notion-Version` is .
</Warning>

<Note>
  **Versioning is only for backwards incompatible changes**

  For new features and additions to the API, such as adding a new API endpoint, or including a new object in an existing API endpoint's response, there won't be a new version. You'll be able to take advantage of any new functionality on the version of the API you're currently using.
</Note>

### What we consider backwards compatible

The following types of changes are made without a new API version. Your integration should be resilient to them:

* **Additive changes** — new endpoints, new optional request parameters, new fields in response objects.
* **Opaque identifier format changes** — pagination cursors, request IDs, and other values not documented as stable identifiers may change in length, format, or structure at any time. Cursors may embed metadata such as session keys or timestamps. **Do not parse, validate, or store cursors beyond passing them back as `start_cursor`.** Only record identifiers (page IDs, database IDs, user IDs, block IDs, etc.) are guaranteed to be stable UUIDs.
* **Error message text improvements** — human-readable `message` strings in error responses may be reworded for clarity. Programmatic error `code` values (e.g. `validation_error`, `object_not_found`) are stable and will not change without a version bump.
* **Rate limit adjustments** — rate limits may change. Always respect `Retry-After` headers.
* **Performance and ordering improvements** — result ordering for endpoints that don't guarantee a specific sort order may change. Pagination behavior may change to improve reliability.

<Tip>
  **Treat all cursors as opaque**

  The `next_cursor` value returned by paginated endpoints may contain session metadata beyond a simple identifier. Always pass it back verbatim as `start_cursor` — do not parse, modify, or validate its format.
</Tip>

**Note:** You may notice that Notion API URLs contain a `v1`. This is not related to the versioning described above. We don't intend to change these URLs.

## Frequently asked questions

<AccordionGroup>
  <Accordion title="How do releases of the JavaScript SDK work?">
    Releases of the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) are published to NPM as [`@notionhq/client`](https://www.npmjs.com/package/@notionhq/client)
    and use a separate [semantic versioning](https://semver.org/) scheme.
    View the [GitHub release notes](https://github.com/makenotion/notion-sdk-js/releases) for the latest version and changes over time. Some SDK changes are also
    featured in the [API changelog](/page/changelog).

    When upgrading to a new "minor" or "patch" version of the SDK, you generally won't need to make any code changes to your connection. These updates contain backwards-compatible
    improvements and fixes.

    However, new "major" versions of the SDK are not backwards-compatible, and you may need to make updates to your connection.

    <Note>Some major releases drop support for older Notion API versions and update the default version used to make requests when no `notionVersion` is provided to
    the SDK `Client` constructor.<br /><br />For example, `v5.0.0` and above dropped support for `2022-06-28` and earlier. Starting with `v5.12.0`, the SDK also supports `2026-03-11`.
    <br /><br />See the upgrade guides for [2026-03-11](/guides/get-started/upgrade-guide-2026-03-11) and [2025-09-03](/guides/get-started/upgrade-guide-2025-09-03).
    See the [compatibility table](https://github.com/makenotion/notion-sdk-js?tab=readme-ov-file#requirements-and-compatibility) in the README to see which versions
    of the SDK are compatible with which versions of the API.</Note>
  </Accordion>

  <Accordion title="Will staying on an older API version work indefinitely?">
    We don't currently have any plans to stop supporting older API versions. If this changes in the future, we'll communicate this with all affected
    users and provide a time window and migration guidance. However, we recommend upgrading to the latest version
    to take advantage of the latest features and improvements.
  </Accordion>
</AccordionGroup>
