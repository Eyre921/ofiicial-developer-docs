---
title: "Migrate to Notion-flavored Markdown (v2)"
source: https://developers.notion.com/guides/data-apis/migrate-to-notion-flavored-markdown
path: guides/data-apis/migrate-to-notion-flavored-markdown
---

Switch your markdown requests from enhanced markdown (v1) to Notion-flavored Markdown (v2) and update your parser for the syntax changes.

This guide is for integrations that read or write page and comment content with the markdown endpoints, especially code that parses or generates markdown. Enhanced markdown (`v1`) is deprecated. The next Notion-Version makes Notion-flavored Markdown (`v2`) the default and rejects `markdown_version: "v1"`. Watch the [changelog](/page/changelog) for the version name and date.

You can switch now on any current Notion-Version. The steps below cover the request change, the syntax changes, and how to test.

## 1. Find where you send markdown

These endpoints accept `markdown_version`:

| Endpoint | Where to send `markdown_version` |
| - | - |
| [`GET /v1/pages/:page_id/markdown`](/reference/retrieve-page-markdown) | Query parameter |
| [`PATCH /v1/pages/:page_id/markdown`](/reference/update-page-markdown) | Body parameter |
| [`POST /v1/pages`](/reference/post-page) | Body parameter, next to `markdown` |
| [`POST /v1/comments`](/reference/create-a-comment) | Body parameter, next to `markdown` |
| [`PATCH /v1/comments/:comment_id`](/reference/update-a-comment) | Body parameter, next to `markdown` |

On `POST /v1/pages` and the comment endpoints, send `markdown_version` only with `markdown`. Sending it with `children` or `rich_text` returns a `400` `validation_error`.

## 2. Add `markdown_version: "v2"`

Set the parameter on every request in the table. The version applies to the whole request, so `v2` input is parsed as `v2` and `v2` responses are rendered as `v2`.

```bash cURL theme={null}
curl 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown?markdown_version=v2' \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
  -H "Notion-Version: 2026-03-11"

curl -X PATCH 'https://api.notion.com/v1/pages/YOUR_PAGE_ID/markdown' \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2026-03-11" \
  --data '{
    "type": "insert_content",
    "insert_content": { "content": "## Next steps\n\n- [ ] Review the launch plan" },
    "markdown_version": "v2"
  }'
```

```javascript JavaScript theme={null}
import { Client } from "@notionhq/client";
const notion = new Client({ auth: process.env.NOTION_API_KEY });

const page = await notion.pages.retrieveMarkdown({
  page_id: "YOUR_PAGE_ID",
  markdown_version: "v2",
});

await notion.pages.updateMarkdown({
  page_id: "YOUR_PAGE_ID",
  type: "insert_content",
  insert_content: { content: "## Next steps\n\n- [ ] Review the launch plan" },
  markdown_version: "v2",
});
```

The JavaScript SDK supports `markdown_version` in `@notionhq/client` v5.29.0 and later.

## 3. Update your parser and generator

Compare your code against the [syntax differences](#syntax-differences) table below. The biggest changes are structural:

* Separate blocks with a blank line. In `v2`, a single newline doesn't start a new block.
* Don't indent children with tabs, except in lists. A block that has children uses its tag form, such as `<p>`, `<quote>`, or `<toggle>`, with the children after a blank line.
* Put block colors in a `color` attribute on the block's tag. `v2` saves `{color="..."}` as literal text.
* Expect `v2` output to use tags for inline formatting, such as `<b>` and `<code>`, where `v1` used `**` and backticks.

For the full `v2` syntax, see the [Notion-flavored Markdown format reference](/guides/data-apis/notion-flavored-markdown).

## 4. Handle new v2 behavior

**Parse errors return a `400`.** When `v2` input can't become the blocks it describes, the request fails with a `validation_error` whose message starts with `Markdown errors blocked parsing`. `v1` saved the same input as literal text. For example, an image inside a line of text (`Text ![chart](https://example.com/chart.png) more`) fails in `v2`. Put each image on its own line with blank lines around it.

**Updates can return `warnings`.** A `PATCH /v1/pages/:page_id/markdown` request that succeeds can include a `warnings` array. Each entry has a `code` and a `message`:

| `code` | Meaning |
| - | - |
| `deprecated_tag` | You sent a `v1` tag, such as `<details>` or `<mention-date>`. It was converted to the `v2` tag. |
| `html_tag_autofix` | You sent an HTML tag, such as `<div>`. It was removed or converted. |
| `unsupported_tag` | You sent a tag that `v2` doesn't know. It was saved as literal text. |

Log these warnings while you migrate. A `deprecated_tag` warning means your generator still writes `v1` syntax. See [Update warnings](/guides/data-apis/working-with-markdown-content#update-warnings) for the response shape.

**Meeting note transcripts use a new tag.** `v2` puts the transcript in `<meeting-notes-section-transcript>` inside `<meeting-notes>`. See [Transcripts in v2](/guides/data-apis/working-with-markdown-content#transcripts-in-v2).

## 5. Test the switch

1. Pick a page that uses the block types your integration reads or writes.
2. Retrieve it twice, once with `markdown_version=v1` and once with `markdown_version=v2`. Diff the two outputs and check each difference against the table below.
3. Run your parser on the `v2` output and confirm it finds the same blocks it found in the `v1` output.
4. On a test page, write your generator's output with `PATCH /v1/pages/:page_id/markdown`, `"type": "replace_content"`, and `"markdown_version": "v2"`. Check that the response has no `warnings`. Then retrieve the page with `markdown_version=v2` and run your parser on it. Check that it finds the blocks you meant to write. Don't compare exact text, because `v2` output can differ from valid input, such as `<b>` for `**`.

## Syntax differences

Each row shows the same content in both versions, taken from real API output. Syntax not listed here, such as plain headings, bulleted and numbered list items, `- [ ]` to-dos, links, images, dividers, fenced code, block equations, citations, and custom emoji, is the same in both versions.

### Structure

| Content | `v1` | `v2` | Notes |
| - | - | - | - |
| Between blocks | One newline | One blank line | In `v2`, lines separated by a single newline join into one block. |
| Line break inside a block | `<br>` | `<br />` | `v2` also accepts a trailing `\` at the end of the line. |
| Children of a block | Indented one tab under the parent | Inside the parent's tag, after a blank line, not indented | Nested list items are indented with spaces in `v2` output: 2 under `-`, 3 under `1.`. Tabs still work for list items. |
| Block color | `{color="blue"}` at the end of the first line | `color="blue"` on the block's tag | Applies to every block that has a color. |
| Empty block | `<empty-block/>` | `<p />` | |

### Blocks

| Block | `v1` | `v2` | Notes |
| - | - | - | - |
| Paragraph with color | `Text {color="gray_bg"}` | `<p color="gray_bg">` `Text` `</p>` | |
| Heading with color | `# Heading {color="blue"}` | `<h1 color="blue">` `Heading` `</h1>` | Same for `<h2>` to `<h4>`. |
| Toggle heading | `## Title {toggle="true"}` with tab-indented children | `<toggle heading="h2">` `Title` `Children` `</toggle>` | |
| Toggle | `<details>` `<summary>Title</summary>` `Children` `</details>` | `<toggle>` `Title` `Children` `</toggle>` | The title is the first line, then a blank line. |
| Quote | `> Text` | `> Text` | Same for a plain quote. In `v2`, separate two quotes with a blank line, or they join into one. |
| Quote with color or children | `> Text {color="purple_bg"}` with tab-indented children | `<quote color="purple_bg">` `Text` `Children` `</quote>` | |
| Callout | `<callout icon="💡" color="yellow_bg">` with tab-indented content | `<callout icon="💡" color="yellow_bg">` `Text` `Children` `</callout>` | Same tag. Content isn't indented, and a blank line follows the first line. |
| Bulleted list item with color | `- Item {color="blue"}` | `<ul>` `<li color="blue">` `Item` `</li>` `</ul>` | Use `<ol>` for numbered items. |
| To-do with color | `- [ ] Task {color="green"}` | `<todo checked="false" color="green">` `Task` `</todo>` | |
| Code language | Full name, like ` ```python ` or ` ```typescript ` | Short name, like ` ```py ` or ` ```ts ` | Plain text becomes `txt`. Some names don't change, like `javascript`, `bash`, and `mermaid`. `v2` input accepts the full names too. |
| Plain table | `<table header-row="true">` with `<tr>` and `<td>` | GFM pipe table: `\| Name \| Owner \|` `\| --- \| --- \|` `\| Spec \| Ada \|` | The `\| --- \|` row is required. |
| Styled table | `<table>` with one cell per line, like `<td>Name</td>` | `<table>` with each cell's content on its own line inside `<td>` | Used when a table has a header column, colors, or widths. |
| File, PDF, video, audio | `<file src="URL">Caption</file>` | `<file source="URL">` `Caption` `</file>` | `src` becomes `source`. Without a caption, `v2` uses a self-closing tag, like `<pdf source="URL" />`. |
| Bookmark | `<unknown url="..." alt="bookmark"/>` | `<bookmark source="URL" />` | `v1` doesn't render bookmarks. |
| Embed | `<embed src="URL"></embed>` | `<embed source="URL" />` | |
| Table of contents | `<table_of_contents/>` | `<table-of-contents />` | Underscore becomes hyphen. |
| Synced block | `<synced_block url="...">` and `<synced_block_reference url="...">` | `<synced-block url="...">` and `<synced-block-reference url="...">` | Content isn't indented in `v2`. |
| Columns and tabs | `<columns>` / `<column>` and `<tabs>` / `<tab>` with tab-indented content | Same tags, content not indented | |
| Child page | `<page url="URL">Title</page>` | `<page url="URL">` `Title` `</page>` | |
| Child database | `<database url="URL" inline="true" data-source-url="...">Title</database>` | `<database url="URL" data-source-url="..." inline="true">` `Title` `</database>` | |
| Meeting notes | `<meeting-notes readOnlyViewMeetingNoteUrl="URL">` with `<summary>`, `<notes>`, and `<transcript>` | `<meeting-notes view-url="URL">` with `<meeting-notes-section-summary>`, `<meeting-notes-section-notes>`, and `<meeting-notes-section-transcript>` | |

### Inline content

| Content | `v1` | `v2` | Notes |
| - | - | - | - |
| Bold, italic, strikethrough | `**text**`, `*text*`, `~~text~~` | `<b>text</b>`, `<i>text</i>`, `<s>text</s>` | `v2` output always uses tags. `v2` input accepts both forms. |
| Underline | `<span underline="true">text</span>` | `<u>text</u>` | |
| Inline code | `` `code` `` | `<code>code</code>` | `v2` output uses the tag. `v2` input accepts backticks. |
| Inline math | ``$`E=mc^2`$`` | `$E=mc^2$` | |
| Escaped `<` and `>` | `\<tag\>` | `\<tag>` | `v2` escapes only `<`. |
| User mention | `<mention-user url="user://ID"/>` | `<mention url="user://ID" />` | All mentions use one `<mention>` tag in `v2`. |
| Page mention | `<mention-page url="URL">Title</mention-page>` | `<mention url="URL">Title</mention>` | |
| Database mention | `<mention-database url="URL">Name</mention-database>` | `<mention url="URL" type="database">Name</mention>` | |
| Data source mention | `<mention-data-source url="collection://ID">Name</mention-data-source>` | `<mention url="collection://ID">Name</mention>` | |
| Agent mention | `<mention-agent url="agent://ID">Name</mention-agent>` | `<mention url="agent://ID">Name</mention>` | |
| Date mention | `<mention-date start="2026-11-02" startTime="09:30" timeZone="America/Los_Angeles"/>` | `<date start="2026-11-02" start-time="09:30" time-zone="America/Los_Angeles" />` | The tag is `<date>`, and attribute names use hyphens. |

## Common problems

**Content runs together into one block.** Your generator puts one newline between blocks. Add a blank line between blocks.

**A quote swallows the lines after it.** A line right after a `>` line joins the quote. Add a blank line after the quote.

**Indented text joins its parent paragraph.** Tab indentation only nests list items in `v2`. For other children, use the parent's tag form, such as `<p>` or `<toggle>`.

**`{color="..."}` shows up as text on the page.** `v2` doesn't read the `v1` color syntax and doesn't warn about it. Move the color into the block's `color` attribute.

**An update fails with `Markdown errors blocked parsing`.** The input mixes syntax that `v2` can't parse, such as an image inside a line of text. The error message says what to fix.
