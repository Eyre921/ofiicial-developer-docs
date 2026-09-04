---
title: "Unfurl attribute (Link Previews)"
source: https://developers.notion.com/reference/unfurl-attribute-object
path: reference/unfurl-attribute-object
---

A Link Preview is rendered from an array of unfurl attribute objects.

A [Link Preview](/guides/link-previews/introduction) is a real-time excerpt of authenticated content that unfurls in Notion when an authenticated user shares an enabled link. The display of a Link Preview can include structured content and rich media from the source service.

Custom Link Preview connections are no longer available for new developers to create. Existing supported Link Preview integrations continue to work for Notion users.

Link Previews can be displayed in their full format, or they can be shown as a "Mention".

Let's first look at an example of a full-format Link Preview:

<Frame>
  <img />
</Frame>

Here is the same link again but now as a Mention — a miniature version of a Link Preview that uses the same data.

<Frame>
  <img />
</Frame>

A Link Preview or Mention displays data that is sent to Notion as an array of unfurl attribute objects. There are a number of optional attributes. However, **every array must contain a `title` attribute and a `dev` attribute.**

Using the same Link Preview and Mention we saw above, let's look at the array of unfurl attribute objects that would render these previews. The following payload represents the example Link Preview and Mention above:

<CodeGroup>
  ```json JSON expandable theme={null}
  [
    {
      "id": "title",
      "name": "Title",
      "type": "inline",
      "inline": {
        "title": {
          "value": "Feature Request: Link Previews",
          "section": "title"
        }
      }
    },
    {
      "id": "dev",
      "name": "Developer Name",
      "type": "inline",
      "inline": {
        "plain_text": {
          "value": "Acme Inc",
          "section": "secondary"
        }
      }
    },
    {
      "id": "state",
      "name": "State",
      "type": "relation",
      "relation": {
        "uri": "acme:item_state/open",
        "mention": {
          "section": "primary"
        }
      }
    },
    {
      "id": "itemId",
      "name": "Item Id",
      "type": "inline",
      "inline": {
        "plain_text": {
          "value": "#23487",
          "section": "identifier"
        }
      }
    },
    {
      "id": "itemIcon",
      "name": "Item Icon",
      "type": "inline",
      "inline": {
        "color": {
          "value": {
            "r": 247,
            "g": 247,
            "b": 42
          },
          "section": "entity"
        }
      }
    },
    {
      "id": "description",
      "name": "Description",
      "type": "inline",
      "inline": {
        "plain_text": {
          "value": "Would love to be able to preview some Acme resources in Notion!\n Maybe an open item?",
          "section": "body"
        }
      }
    },
    {
      "id": "updated_at",
      "name": "Updated At",
      "type": "inline",
      "inline": {
        "datetime": {
          "value": "2022-01-11T19:53:18.829Z",
          "section": "secondary"
        }
      }
    },
    {
      "id": "label",
      "name": "Label",
      "type": "inline",
      "inline": {
        "enum": {
          "value": "🔨 Ready to Build",
          "color": {
            "r": 100,
            "g": 100,
            "b": 100
          },
          "section": "primary"
        }
      }
    },
    {
      "id": "media",
      "name": "Embed",
      "embed": {
        "src_url": "https://c.tenor.com/XgaU95K_XiwAAAAC/kermit-typing.gif",
        "image": {
          "section": "embed"
        }
      }
    }
  ]
  ```
</CodeGroup>

Each unfurl attribute object in this array maps to a different customizable section of a Link Preview. (To learn more about each section, jump to [The `section` value](/reference/unfurl-attribute-object#the-section-value).

<Frame>
  <img />
</Frame>

First, let's let at the properties in each individual unfurl attribute object.

## The unfurl attribute object

<CodeGroup>
  ```json Example unfurl attribute object theme={null}
  {
      "id": "title",
      "name": "Title",
      "type": "inline",
      "inline": {
        "title": {
          "value": "Feature Request: Link Previews",
          "section": "title"
        }
      }
    }
  ```
</CodeGroup>

Each unfurl attribute object contains the following values:

| Field                 | Type                  | Description                                                                                                                                                    | Example value                                                                    |
| :-------------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| `id`                  | `string`              | A unique identifier for the attribute. If more than one attribute with the same `id` is provided, then the latter attribute overrides the value of the first.  | `"title"`                                                                        |
| `name`                | `string`              | A human readable name describing the attribute.                                                                                                                | `"Title"`                                                                        |
| `type`                | `inline` \|\| `embed` | The type of attribute. Most attributes are `inline`. Use `embed` for rich media sub-types like `image`, `video`, or `audio`.                                   | `"inline"`                                                                       |
| `inline` \|\| `embed` | `object`              | An object whose key is a sub-type. The child sub-type object includes the `value` to display and the `section` of the Link Preview where the data is rendered. | `{ "title": { "value": "Feature Request: Link Previews", "section": "title" } }` |

### Inline sub-type objects

The key of inline sub-type objects represents the kind of sub-type. The values of the key are the `value` to display and the `section` of the Link Preview where the value is rendered.

| Sub-type     | Description                                                                                                                             | Example value                                                                                                             |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| `color`      | A color with r, b, g values.                                                                                                            | `{ "value": { "r": 247, "g": 247, "b": 42 }, "section": "entity" }`                                                       |
| `date`       | A date.                                                                                                                                 | `{ "value": "2022-01-11", "section": "secondary" }`                                                                       |
| `datetime`   | A datetime.                                                                                                                             | `{ "value": "2022-01-11T19:53:18.829Z", "section": "secondary" }`                                                         |
| `enum`       | A string value and optional color object.                                                                                               | `{ "value": "🔨 Ready to Build", "color": { "r": 100, "g": 100, "b": 100 }, "section": "primary" }`                       |
| `plain_text` | Any plain text content.                                                                                                                 | `{ "value": "Would love to be able to preview some Acme resources in Notion!\n Maybe an open item?", "section": "body" }` |
| `title`\*    | The title of the Link Preview. \*An unfurl attribute object of this type must be included in every payload that renders a Link Preview. | `{ "value": "Feature Request: Link Previews", "section": "title" }`                                                       |

#### The `dev` attribute

Every array of attribute objects that is sent to Notion to render a Link Preview must also include a `dev` attribute. The attribute indicates the service or company associated with the Link Preview. It takes the following format:

<CodeGroup>
  ```json Example dev attribute theme={null}
  {
      "id": "dev",
      "name": "Developer Name",
      "type": "inline",
      "inline": {
        "plain_text": {
          "value": "Acme Inc",
          "section": "secondary"
       }
     }
   }
  ```
</CodeGroup>

### Embed sub-type child objects

The `embed` sub-type object adds rich content like JPGs, GIFs, or iFrames to a Link Preview.

<Frame>
  <img />
</Frame>

All embed sub-type objects contain: a `src_url` field that is a link to the embed, and an object whose key is the sub-type of the embed and whose value is an object indicating the `section` of the Link Preview where the value is rendered.

| Sub-type | Description                                           | Example value                                                                                     |
| -------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `audio`  | Audio from a source URL.                              | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4", "audio": { "section": "embed" } }`  |
| `html`   | HTML from a source URL that is rendered in an iFrame. | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.html", "html": { "section": "embed" } }`  |
| `image`  | Image from a source URL.                              | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.png", "image": { "section": "avatar" } }` |
| `video`  | Video from a source URL.                              | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4", "video": { "section": "embed" } }`  |

<Note>
  There’s no need to ask a user to log in to the source service in an iFrame embed. If they’re using a Link Preview, then they’ve already authenticated.
</Note>

### The `section` value

The `section` value of an unfurl attribute object defines where an attribute is rendered in the Link Preview or Mention.

<Frame>
  <img />
</Frame>

<br />

<Frame>
  <img />
</Frame>

A `section` is specified in the sub-type object for the attribute. Refer to the table below for details about each `section` and its valid parent sub-types.

| Section    | Description                                                                                    | Valid parent sub-types                   |
| :--------- | :--------------------------------------------------------------------------------------------- | :--------------------------------------- |
| avatar     | The picture found on the bottom left of a Link Preview.                                        | `image`, `plain_text`                    |
| background | A background color for the Link Preview.                                                       | `color`                                  |
| body       | The main string content of a Link Preview.                                                     | `plain_text`                             |
| embed      | The large space where the content of an `embed` attribute type is displayed in a Link Preview. | `audio`, `html`, `image`, `pdf`, `video` |
| entity     | The small picture found in the subheading of a Link Preview and in a Mention.                  | `color`, `image`                         |
| identifier | The subheading found on the bottom of a Link Preview and on the left side of a Mention.        | `image`, `plain_text`                    |
| primary    | The first subheading section.                                                                  | `enum`, `date`, `datetime`, `plain_text` |
| secondary  | The second subheading section.                                                                 | `date`, `datetime`, `plain_text`         |
| title\*    | The main heading in a Link Preview or Mention. \*Required.                                     | `title`                                  |
