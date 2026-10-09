---
title: "Notion-flavored Markdown format"
source: https://developers.notion.com/guides/data-apis/notion-flavored-markdown
path: guides/data-apis/notion-flavored-markdown
---

Reference for Notion-flavored Markdown, the syntax used by markdown_version v2.

Notion-flavored Markdown is the syntax for `markdown_version: "v2"`, an opt-in preview on the markdown endpoints. See [Markdown versions](/guides/data-apis/working-with-markdown-content#markdown-versions) for where to send the parameter. The default, `v1`, uses [enhanced markdown](/guides/data-apis/enhanced-markdown).

The specification below comes from the same source as the Notion MCP server's Markdown spec. It is written for AI agents, so it is terse. You can paste it into your own agent's prompt.

```markdown theme={null}
# Notion-flavored Markdown

CommonMark + GFM tables, task lists, strikethrough; custom emoji :smile:; inline math $...$; display math uses bare $$ lines around the equation (never same-line $$...$$ or \[...\]); citations [^URL] only (no footnotes). Notion XML tags below. Never write other HTML tags (e.g. <div>, <details>, <figure>, <small>, <sup>, <sub>, <mark>); they are saved as literal text.

Rules:
- Escape literal tags in text as \<tag> or &lt;tag&gt;; never inside code or mention labels, which are already literal.
- Always fence code blocks; never indent them. One-copyable-block rule: make the opening and closing fence longer than the longest backtick run in the content. Triple-backtick content requires four-backtick outer fences; never use triple backticks both outside and inside.
- Hard line break = trailing \ replacing the space before it. Empty paragraph = <p />.

Inline tags:
- <b>, <i>, <s>, <u> (the only underline); required when styled text has leading/trailing spaces.
- <span color="..." discussion-urls="url,url">text</span>; nest to combine: <span color="orange"><u>word</u></span>.
- Use <mention url="...">Label</mention> or <mention url="..." /> for mentioning Notion entities user://..., HTTPS page URLs, collection://..., agent://.... Database mentions use type="database" to distinguish them from page mentions. Regular links use [text](url).
- <date start="YYYY-MM-DD" end="YYYY-MM-DD" start-time="HH:mm" end-time="HH:mm" time-zone="IANA_TZ" />

Block tags: always use the tag form when a block needs attributes, children, or edge whitespace — <quote> not >, <li> not -. Most accept color="gray|brown|orange|yellow|green|blue|purple|pink|red" (text) or _bg forms like "blue_bg" (background). Color a whole block or cell with its color attribute; use <span color> only for words inside text.

One container shape for <p>, <h1>-<h4>, <quote>, <toggle heading="h1|h2|h3|h4" color="...">, <li color="..."> in <ul>/<ol type="1|a|i">, <column> in <columns>, <tab icon="emoji or Notion Icon"> in <tabs>, <mail to="..." cc="..." bcc="..." from="..." subject="..." attachments="url,url">, <meeting-notes>:

<quote color="purple_bg">
Title text

- child bullet

<callout icon="💡" color="yellow_bg">
Callout body child
</callout>
</quote>

The title/label is body text right after the opening tag, never an attribute. Children follow a blank line — plain Markdown, no <p> wrappers or > prefixes. Blank lines touching the opening or closing tags become stray whitespace; never pad. <p /> = empty title.

Other blocks:
- <todo checked="true|false"> when a todo needs color; else - [ ] / - [x].
- <equation color="...">x + y = z</equation>
- <table-of-contents color="..." />
- Media (body = optional caption): ![caption](url), or <image source="..." color="...">caption</image> for attributes; other embeds use their type's tag: <pdf source="...">caption</pdf>, likewise <file>, <audio>, <video>, <bookmark>, <embed>. Each image must be its own block: never inline it with text (paragraph, list-item, etc.) or another image, and separate consecutive images with a blank line. Use <external_object_instance integration="github|figma|google_drive">Embed name</external_object_instance> to create a rich integration embed placeholder.
- <page url="..." color="...">Title</page>; represents a subpage on the current page. Warning: an update_content, replace_content, or replace_content_range update that leaves out this tag deletes the subpage when allow_deleting_content is true. Otherwise the update fails with a validation_error. Omit url only when creating a new subpage.
- <folder url="...">Title</folder>; represents an existing folder. Use the retrieve page markdown endpoint to read its immediate children, then follow nested folder URLs to continue traversing. Preserve the tag unless intentionally moving or deleting the folder; folders cannot be created from Markdown.
- <database url="..." data-source-url="..." inline="true|false" icon="emoji" wiki="true|false" color="...">Title</database>; same url/title rules. Wiki databases set wiki="true"; their pages use parent type "page" with the wiki page URL, not "dataSource".
- <synced-block url="...">...</synced-block> (omit url for new); <synced-block-reference url="..." notice="...">...</synced-block-reference>.
- <meeting-notes attendees="user://id,..." view-url="...">Title<meeting-notes-section-notes>Notes</meeting-notes-section-notes><meeting-notes-section-summary>Summary</meeting-notes-section-summary></meeting-notes>; content outside <meeting-notes-section-notes> is ignored; omit view-url and the summary section for new. An existing <meeting-notes> may also have an optional read-only <meeting-notes-section-transcript> child: a "Transcript omitted" body means the transcript was not loaded, so follow its instructions to load it; never edit its contents, and never add it to new meeting notes.
- <custom-block definition-id="UUID" url="..." />; places an instance of a custom block definition deployed in this workspace. Use a self-closing tag on its own line; the instance inherits the definition's bindings. Omit url for a new instance; readback adds its instance URL. Preserve that URL when editing, reordering, or moving an existing instance.
- Columns: <columns><column ratio="50">...</column><column ratio="50">...</column></columns>. ratio is an optional percentage of the column-list width.

Tables:
- Pipe tables (escape | in cells as \|) for plain tables; <table> only for styled ones; never mix the two.
- <table fit-page-width="true|false" header-row="true|false" header-column="true|false">, optional <colgroup><col width="180" color="..." /></colgroup>, <tr color="..."> rows, <th>/<td color="..."> cells.
- Cells are inline-only (<br /> for line breaks); copy the existing cells' formatting when adding rows (pad with blank lines if the existing cells do).
```
