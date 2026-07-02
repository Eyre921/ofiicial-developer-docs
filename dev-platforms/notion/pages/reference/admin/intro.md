---
title: "Introduction"
source: https://developers.notion.com/reference/admin/intro
path: reference/admin/intro
---

Learn the conventions, authentication, and pagination patterns used for Notion's Admin API.

The Admin API can be used to manage Notion resources associated with your organization. Use the navigation on the left to find details for endpoints used in the API.

<Info>
  The Admin API is only available to organizations and workspaces that are actively on the [enterprise plan](https://www.notion.com/enterprise).
</Info>

## Creating & managing tokens

Every request is authenticated with an organization bot token tied to your Notion organization. Organization owners can manage these tokens in the [organization console](https://www.notion.com/help/organization-level-controls), where they can create, edit, or revoke any active tokens.

## Conventions

The base URL to send all API requests is `https://api.notion.com/admin`. HTTPS is required for all API requests.

The Notion API follows RESTful conventions when possible, with most operations performed via `GET`, `POST`, `PATCH`, and `DELETE` requests on page and database resources. Request and response bodies are encoded as JSON.

## Code samples

Samples requests and responses are shown for each endpoint. Requests are shown using [cURL](https://curl.se/). These samples make it easy to copy, paste, and modify as you build your connection.

## Pagination

Endpoints that return lists of objects support cursor-based pagination requests. By default, Notion returns ten items per API call. If the number of items in a response from a support endpoint exceeds the default, then you can use pagination to request a specific set of the results and/or to limit the number of returned items.
