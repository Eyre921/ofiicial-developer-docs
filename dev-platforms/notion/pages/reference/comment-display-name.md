---
title: "Comment display name"
source: https://developers.notion.com/reference/comment-display-name
path: reference/comment-display-name
---

The Comment Display Name object represents the author name that shows up for a comment. This overrides the default author name when specified.

## Request format (input)

### Object properties

| Parameter | Type            | Description                                                                                                        | Example value                        |
| :-------- | :-------------- | :----------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| `type`    | `string` (enum) | Possible type values are:`"connection"`, `"user"`, or `"custom"`                                                   | `"user"`                             |
| `custom`  | `object`        | If the type is `"custom"`, include a custom object specifying the custom name`"custom": { "name": <Custom Name> }` | `"custom": { "name": "Notion Bot" }` |

* `"connection"`: name of the [connection](/guides/get-started/overview)
* `"user"`: name of the user who authenticated the connection or token (for [public connections](/guides/get-started/overview#connection-types) and [personal access tokens](/guides/get-started/personal-access-tokens))
* `"custom"`: any custom name

Example of a Create Comment request with custom display name:

<CodeGroup>
  ```json API request theme={null}
  {
    "parent": {
      "page_id": "d0a1ffaf-a4d8-4acf-a1ed-abae6e110418"
    },
    "rich_text": [
      {
        "text": {
          "content": "Thanks for checking us out!"
        }
      }
    ],
    "display_name": {
      "type": "custom",
      "custom": {
        "name": "Notion Bot"
      }
    }
  }
  ```
</CodeGroup>

## Response format (output)

### Object properties

The response of Comment APIs like [Create comment](/reference/create-a-comment) contains `attachments` with the following fields:

| Field           | Type            | Description                                                      | Example value  |
| :-------------- | :-------------- | :--------------------------------------------------------------- | :------------- |
| `type`          | `string` (enum) | Possible type values are:`"connection"`, `"user"`, or `"custom"` | `"custom"`     |
| `resolved_name` | `string`        | The custom display name shown in a comment                       | `"Notion Bot"` |

<CodeGroup>
  ```json API Response theme={null}
  {
    ...existing parameters omitted,
    "display_name": {
      "type": "custom",
      "resolved_name": "Notion Bot"
    }
  }
  ```
</CodeGroup>
