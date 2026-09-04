---
title: "Connection capabilities"
source: https://developers.notion.com/reference/capabilities
path: reference/capabilities
---

Learn about the capabilities that control what a connection can do and see in a Notion workspace.

All connections and [personal access tokens](/guides/get-started/personal-access-tokens) have associated capabilities which enforce what they can do and see in a Notion workspace.
These capabilities when put together enforce which API endpoints a connection or token can call, and what content and user related information they are able to see.
To set your connection's capabilities see the [Authorization](/guides/get-started/authorization) guide or navigate to the <a href={developerConnectionsUrl}>Developer portal</a>. For PATs, choose capabilities when you create the token.

<Frame>
  <img />
</Frame>

<Note>
  **If a connection is added to a page, then the connection can access the page’s children**

  When a connection receives access to a Notion page or database, it can read and write to both that resource and its children.
</Note>

## Content capabilities

Content capabilities affect how a connection can interact with [database objects](/reference/database), [page objects](/reference/page), and [block objects](/reference/block) via the API. Additionally, these capabilities affect what information is exposed to a connection in API responses. To verify which capabilities are needed for an endpoint's desired behavior, please use the API references.

* **Read content**: This capability gives a connection access to read existing content in a Notion workspace. For example, a connection with only this capability is able to call [Retrieve a database](/reference/retrieve-a-database) , but not [Update database](/reference/update-a-database).

* **Update content**: This capability gives a connection permission to update existing content in a Notion workspace. For example, a connection with only this capability is able to call the [Update page](/reference/patch-page) endpoint, but is not able to create new pages.

* **Insert content**: This capability gives a connection permission to create new content in a Notion workspace. This capability does not give the connection access to read full objects. For example a connection with only this capability is able to [Create a page](/reference/post-page) but is not able to update existing pages.

*It is possible for a connection to have any combination of these content capabilities.*

## Comment capabilities

Comment capabilities dictate how a connection can interact with the [comments](/reference/comment-object) on a page or block.

* **Read comments**: This capability gives the connection permission to [read comments](/reference/list-comments) from a Notion page or block.

* **Insert comments**: This capability gives the connection permission to [insert comments](/reference/create-a-comment) in a page or in an existing discussion.

## User capabilities

A connection can request different levels of user capabilities, which affect how [user objects](/reference/user) are returned from the Notion API:

* **No user information**: Selecting this option prevents a connection from requesting any information about users. User objects will not include any information about the user, including name, profile image, or their email address.
* **User information without email addresses**: Selecting this option ensures that User objects will include all information about a user, including name and profile image, but omit the email address.
* **User information with email addresses**: Selecting this option ensures that User objects will include all information about the user, including name, profile image, and their email address.

## Capability behaviors and best practices

For public connections, users will need to re-authenticate with a connection if the capabilities are changed in the time since the user last authenticated with the connection.

To learn more about setting your connection's capabilities refer to the [Authorization](/guides/get-started/authorization) guide.

In general, you want to request minimum capabilities that your connection needs in order to function. The fewer capabilities you request, the more likely a workspace admin will be able to install your connection.

For example:

* If your connection is solely bringing data into Notion (creating new pages, or adding blocks), your connection only needs **Insert content** capabilities.
* If your connection is reading data to export it out of Notion, your connection will only need **Read content** capabilities.
* If your connection is simply updating a property on a page or an existing block, your connection will only need **Update content** capabilities.
