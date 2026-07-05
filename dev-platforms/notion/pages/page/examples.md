---
title: "Examples"
source: https://developers.notion.com/page/examples
path: page/examples
---

## Introductory

<CardGroup>
  <Card title="Create a Notion block" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/basic/1-add-block.ts" icon="github">
    In this introductory codebase, start by learning the basics of Notion's Public API: creating a new block.
  </Card>

  <Card title="Create a linked Notion block" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/basic/2-add-linked-block.ts" icon="github">
    Build on the previous example by creating a block in Notion and adding a link to it.
  </Card>

  <Card title="Create a styled/linked Notion block" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/basic/3-add-styled-block.ts" icon="github">
    Extend the previous example further by styling a block of text that links to an external website.
  </Card>

  <Card title="Get text from any type of block" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/parse-text-from-any-block-type" icon="github">
    This connection shows how to get a list of blocks from a Notion page and parse the text from any type of block.
  </Card>
</CardGroup>

## Intermediate

<CardGroup>
  <Card title="Create a Notion database" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/1-create-a-database.ts" icon="github">
    Create your first Notion database with a defined set of properties.
  </Card>

  <Card title="Add new pages to a database" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/2-add-page-to-database.ts" icon="github">
    Build on the previous example by creating a database and adding new pages to it.
  </Card>

  <Card title="Query pages in a database" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/3-query-database.ts" icon="github">
    Learn how to filter your database rows (pages) after creating them from scratch.
  </Card>

  <Card title="Filter and sort database pages" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/4-sort-database.ts" icon="github">
    Filter and sorts pages after adding them to a new database.
  </Card>

  <Card title="Upload files to a page" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/5-upload-file.ts" icon="github">
    Create, send, and attach a file upload to a page's contents and as a comment attachment.
  </Card>

  <Card title="Build a full-stack Notion connection" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/web-form-with-express" icon="github">
    Learn how to build a Notion connection with an interactive front-end using Express.js and the Notion SDK for JavaScript.
  </Card>
</CardGroup>

## Advanced

<CardGroup>
  <Card title="Sync Spotify Playlists with Notion" href="/guides/tutorials/spotify" icon="book">
    This connection populates a Notion database with track metadata from a Spotify playlist.
  </Card>

  <Card title="Integrate Mailchimp Campaigns with Notion" href="/guides/tutorials/integrate-mailchimp-campaigns-with-notion-databases" icon="book">
    This connection populates a Notion database with Mailchimp campaign information, including subscriber contact information.
  </Card>

  <Card title="Log Strava Activity in Notion" href="/guides/tutorials/log-strava-activity-in-notion" icon="book">
    This connection syncs a Strava athlete's activity metadata within a Notion database.
  </Card>

  <Card title="Add rows (pages) to an existing database" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/generate-random-data" icon="github">
    This connection finds the first database that your bot has access to, and creates correctly-typed random rows of data.
  </Card>

  <Card title="Sync Notion with GitHub issues" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/notion-github-sync" icon="github">
    This Notion connection syncs GitHub Issues for a specific repo to a Notion database. This example shows a one-way sync — changes in GitHub cause an update in Notion.
  </Card>

  <Card title="Send an email from a Notion trigger" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/database-email-update" icon="github">
    This Notion connection sends an email whenever the *Status* property of a page in a database is updated. This sample shows how to use Notion to cause an external action. In this case, the connection sends emails using SendGrid's API.
  </Card>

  <Card title="Sync Notion with GitHub PRs" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/notion-task-github-pr-sync" icon="github">
    This Notion connection updates Notion tasks when a linked Github PR is closed/merged. This connection requires the Notion task link be mentioned in the PR description.
  </Card>
</CardGroup>
