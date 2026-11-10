---
title: "API requests"
source: https://developers.notion.com/cli/guides/api-requests
path: cli/guides/api-requests
---

Make Notion API requests from the terminal.

Use `ntn api` to call the Notion API from your terminal. It adds the `Authorization` and `Notion-Version` headers. [Log in with the CLI](/cli/get-started/authentication) or set `NOTION_API_TOKEN` to the token you want to use.

## Make a request

Set `PAGE_ID` to the ID of a page you can read. Pass its API path to `ntn api`. The leading slash is optional.

```bash theme={null}
ntn api v1/pages/$PAGE_ID
ntn api /v1/pages/$PAGE_ID
```

Without request body input, `ntn api` sends a `GET` request.

To create a child page, set `PARENT_PAGE_ID` to the ID of a page you can add content to. Pass the parent and title as body fields.

```bash theme={null}
ntn api v1/pages \
  "parent[page_id]=$PARENT_PAGE_ID" \
  'properties[title][title][0][text][content]=CLI-created page'
```

When body fields are present, `ntn api` sends a `POST` request unless you override the method.

Use `-X` to choose the method. This request restores a page from the trash.

```bash theme={null}
ntn api "v1/pages/$PAGE_ID" -X PATCH in_trash:=false
```

## Build request data inline

Inline inputs after the path can set body fields, query parameters, and request headers.

| Form | Meaning | Example |
| :- | :- | :- |
| `path=value` | Body field with a string value | `parent[page_id]=abc123` |
| `path:=json` | Body field parsed as JSON | `in_trash:=false` |
| `name==value` | Query parameter | `page_size==100` |
| `Header:Value` | Request header | `Accept:application/json` |

Use `=` when the value should be a string:

```bash theme={null}
ntn api v1/search query=roadmap
```

Use `:=` to send a number. This page must have a number property named `Priority`.

```bash theme={null}
ntn api "v1/pages/$PAGE_ID" -X PATCH \
  'properties[Priority][number]:=2'
```

Typed values can be booleans, numbers, strings, arrays, objects, or `null`:

```bash theme={null}
ntn api v1/search \
  filter:='{"property":"object","value":"page"}' \
  page_size:=10
```

## Choose body syntax

For nested objects, use brackets or dots. Quote the whole argument when it contains brackets or spaces so your shell passes it as one field.

```bash theme={null}
ntn api v1/pages \
  "parent[page_id]=$PARENT_PAGE_ID" \
  'properties.title.title[0].text.content=Meeting notes'
```

Use explicit array indexes when order matters:

```bash theme={null}
ntn api "v1/blocks/$PAGE_ID/children" -X PATCH \
  'children[0][type]=paragraph' \
  'children[0][paragraph][rich_text][0][text][content]=First paragraph' \
  'children[1][type]=heading_2' \
  'children[1][heading_2][rich_text][0][text][content]=Next section'
```

Use `[]` to append repeated values in input order:

```bash theme={null}
ntn api v1/comments \
  "parent[page_id]=$PAGE_ID" \
  'rich_text[][text][content]=First comment line' \
  'rich_text[][text][content]=Second comment line'
```

For a rich text property named `Build version`, put the name in brackets.

```bash theme={null}
ntn api "v1/pages/$PAGE_ID" -X PATCH \
  'properties[Build version][rich_text][0][text][content]=2026.05.11'
```

> [!NOTE]
>
> Inline request syntax is inspired by [HTTPie](https://github.com/httpie/cli)
> and implemented in [httpcliparser](https://github.com/jclem/httpcliparser).

## Send JSON from a file or stdin

Use inline inputs for small bodies. Use stdin or `--data` when the body is easier to write as JSON.

Send a JSON file:

```bash theme={null}
ntn api v1/pages < create-page.json
```

Pipe generated JSON:

```bash theme={null}
jq -n --arg page_id "$PARENT_PAGE_ID" '{
  parent: { page_id: $page_id },
  properties: {
    title: {
      title: [{ text: { content: "Generated page" } }]
    }
  }
}' | ntn api v1/pages
```

Pass a JSON string directly:

```bash theme={null}
ntn api v1/search --data '{"query":"roadmap","page_size":10}'
```

Only use one body source per request: stdin JSON, `--data`, or inline body fields. You can still combine headers and query parameters with any one body source.

## Add query parameters and headers

Use `==` for query parameters. This request lists up to 10 users.

```bash theme={null}
ntn api v1/users page_size==10
```

Use `Header:Value` for request headers:

```bash theme={null}
ntn api v1/users \
  Accept:application/json \
  X-Trace-Id:cli-test-123
```

Repeated query parameters and headers are preserved in the order you pass them.

> [!NOTE]
>
> `ntn api` already sets `Authorization` and `Notion-Version`. You usually do
> not need to pass those headers manually.

## Override the API version

By default, `ntn api` fetches the latest supported `Notion-Version`.

Use `--notion-version` for one request:

```bash theme={null}
ntn api v1/users/me --notion-version 2026-03-11
```

Use `NOTION_API_VERSION` for a shell session or script:

```bash theme={null}
export NOTION_API_VERSION=2026-03-11
ntn api v1/users/me
```

## Inspect endpoints before calling them

List the public API surface:

```bash theme={null}
ntn api ls
```

Print it as JSON for scripts:

```bash theme={null}
ntn api ls --json
```

Show the live endpoint help for a path:

```bash theme={null}
ntn api v1/comments --help
```

Print the reduced OpenAPI fragment for an endpoint:

```bash theme={null}
ntn api v1/comments --spec -X POST
```

Print the official markdown reference page for an endpoint:

```bash theme={null}
ntn api v1/comments --docs -X POST
```

If a path supports multiple methods, pass `-X` so `ntn api` knows which operation to inspect.

## Debug a request

Run with `--verbose` to print request and response metadata to stderr:

```bash theme={null}
ntn --verbose api v1/pages/$PAGE_ID
```

Verbose output includes the final method, URL, request headers, JSON request body, response status, response headers, and response body. The `Authorization` request header is redacted by default.

> [!WARNING]
>
> `--unsafe-verbose` is a hidden debugging flag that disables `Authorization`
> header redaction in verbose logs. It is dangerous because it can display
> your bearer token in command output. Only use it in a controlled local
> environment, and never paste its output into shared logs, tickets, or chat.

## Troubleshooting

| Problem | What to check |
| :- | :- |
| The request used `POST` unexpectedly | Body input, `--data`, or stdin JSON makes `POST` the default. Use `-X` to override it. |
| An inline value has the wrong type | Use `:=` for JSON values like `true`, `10`, `null`, arrays, and objects. Use `=` only for strings. |
| A nested body path is hard to read | Prefer bracket notation, especially for property names with spaces or punctuation. |
| `--spec` or `--docs` says the method is ambiguous | Add `-X GET`, `-X POST`, `-X PATCH`, or the method you want to inspect. |
| The body source conflicts | Use only one of stdin JSON, `--data`, or inline body fields. |
| You need to inspect a failing request | Add `--verbose` and check the final method, URL, status, and `x-request-id`. |

## Next steps

> [card] [File uploads](/cli/guides/file-uploads)
>
> Upload local files or import external files into Notion.

> [card] [API reference](/reference/intro)
>
> Browse Notion API endpoints and schemas.
