---
title: "Version"
source: https://developers.deepgram.com/docs/version.md
path: docs/version
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Version

`version` *string* Default: `latest`

&#x20;Pre-recorded

&#x20;Streaming:Nova

Deepgram’s Version feature allows you to specify the version of the model you want to use to process your submitted audio.

## Enable Feature

To enable Version, when you call Deepgram’s API, add a `version` parameter in the query string and set it to the version of the model you want to use to process your submitted audio.

`version=MODEL_VERSION`

## Use the Latest Version

To use the latest version of your selected model, send `latest` in the `version` parameter:

`version=latest`

## Use an Earlier Version of a Standard Model

To use an earlier version of a selected Deepgram standard model, send the version number in the `version` parameter:

`version=VERSION_NUMBER`

**Example:** `version=2021-03-17.0`

You can locate version numbers of Deepgram standard models in [our changelog](https://deepgram.com/changelog/). Select **Speech Model** to filter the updates.

## Use a Specific Version of a Custom Trained Model

To use a specific version of a custom model associated with your account, send the custom model's `version_id` in the `version` parameter:

`version=VERSION_ID`

**Example:** `version=12345678-1234-1234-1234-1234567890ab`

## Get Early Access to an Updated Standard Model

When we release updated versions of Deepgram standard models, you may be able to try them out and provide feedback. To do so, send the version name of the selected model in the `version` parameter:

`version=VERSION_NAME`

**Example:** `version=beta`

To learn about updated model availability and get relevant version names, [contact Support](/support).

## When to use Versions

* If you want to make sure you are using the latest version of a Deepgram model.
* If you want to use an earlier version of a Deepgram model.
* If you want to use a specific version of a custom Deepgram model.
