---
title: "List members lookup"
source: https://docs.x.com/enterprise-api/lists/list-members/migrate/list-members-lookup-standard-to-twitter-api-v2
path: enterprise-api/lists/list-members/migrate/list-members-lookup-standard-to-twitter-api-v2
---

If you have been working with the standard v1.1 GET lists/members and GET lists/memberships. Reference for the Enterprise X API tier covering migrate.

### List members lookup: Standard v1.1 compared to X API v2

If you have been working with the standard v1.1 [GET lists/members](https://developer.x.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members) and [GET lists/memberships](https://developer.x.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and X API v2 List member endpoints.

* **Similarities**
  * Authentication methods
* **Differences**
  * Endpoint URLs
  * Rate limits
  * App and Project requirements
  * Data objects per request limits
  * Response data formats
  * Request parameters

#### Similarities

**Authentication**

Both endpoint versions support both [OAuth 1.0a User Context](/resources/fundamentals/authentication#oauth-1-0a-2) and [App only](/resources/fundamentals/authentication#oauth-2-0). Therefore, if you were previously using one of the standard v1.1 List members endpoints, you can continue using the same authentication method if you migrate to the X API v2 version.

Depending on your authentication library/package of choice, App only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App only Access Token, see [this App only guide](/resources/fundamentals/authentication#bearer-token-also-known-as-app-only).

#### Differences

**Endpoint URLs**

* Standard v1.1 endpoints:
  * GET [https://api.x.com/1.1/lists/members.json](https://api.x.com/1.1/lists/members.json)
    (Lookup members of a specified List)
  * GET [https://api.x.com/1.1/lists/memberships.json](https://api.x.com/1.1/lists/memberships.json)
    (Lookup Lists a user is a member of)
* X API v2 endpoint:
  * GET [https://api.x.com/2/lists/:id/members](https://api.x.com/2/lists/:id/members)
    (Lookup members of a specified List)

  * GET [https://api.x.com/2/users/:id/list\_memberships](https://api.x.com/2/users/:id/list_memberships)
    (Lookup Lists a user is a member of)

**Rate limits**

|                                                                                                                                                                |                                                                                                                                                                                                                                                           |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Standard v1.1**                                                                                                                                              | **X API v2**                                                                                                                                                                                                                                              |
| /1.1/lists/members.json<br /><br />900 requests per 15-minute window with OAuth 1.0a User Context<br /><br />15 requests per 15-minute window with App only    | /2/lists/:id/members<br /><br />900 requests per 15-minute window with OAuth 1.0a User Context<br /><br />900 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE<br /><br />900 requests per 15-minute window with App only        |
| /1.1/lists/memberships.json<br /><br />15 requests per 15-minute window with OAuth 1.0a User Context<br /><br />15 requests per 15-minute window with App only | /2/users/:id/list\_memberships<br /><br />15 requests per 15-minute window with OAuth 1.0a User Context<br /><br />15 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE<br /><br />15 requests per 15-minute window with App only |

**App and Project requirements**

The X API v2 endpoints require that you use credentials from a [developer App](/resources/fundamentals/developer-apps) that is associated with a [Project](/resources/fundamentals/developer-apps) when authenticating your requests. All X API v1.1 endpoints can use credentials from Apps or Apps associated with a project.

**Data objects per request limits**

The standard v1.1 /1.1/lists/members endpoint allows you to return up to 5000 users per request. The new v2 endpoints allow you to return up to 100 users per request. By default, 100 user objects will be returned, to change the number of results you will need to pass a query parameter max\_results= with a number between 1-100; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.

 Additionally, the endpoint /1.1/lists/memberships, allow you to return up to 1000 Lists per request. With the v2 replacement, the endpoint allows up to 100 Lists per request. By default 100 Lists objects are returned, use the query parameters max\_results= and pagination\_token in the same fashion as /1.1/lists/members to change the number of results.

**Response data format**

One of the biggest differences between standard v1.1 and X API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default and then have the option to use parameters to identify which additional fields or sets of fields should return in the payload.

The X API v2 version /users/:id/list\_memberships will deliver the List id and name fields by default. To request any additional fields or objects, you will need to use the [fields](/x-api/fundamentals/fields) and [expansions](/x-api/fundamentals/expansions) parameters. Any List fields that you request from this endpoint will return in the primary List object. Any expanded object and fields will return an includes object within your response. You can then match any expanded objects back to the primary List object by matching the IDs located in both the primary and the expanded object. 

Here are examples of possible List fields and expansions:

* created\_at

* follower\_count

* member\_count

* owner\_id

* description

* private

|                                |                   |
| :----------------------------- | :---------------- |
| **Endpoint**                   | **Expansion**     |
| /2/lists/:id/members           | pinned\_tweet\_id |
| /2/users/:id/list\_memberships | owner\_id         |

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](/x-api/fundamentals/data-dictionary/reference#how-to-use-fields-and-expansions). 

We have also put together a [data format migration guide](/x-api/migrate/data-format-migration) that can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you with the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields. 

In addition to the changes in how you request certain fields, X API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Post](/x-api/fundamentals/data-dictionary/reference#tweet) and [user](/x-api/fundamentals/data-dictionary/reference#user) objects.

* At the JSON root level, the standard endpoints return Post objects in a statuses array, while X API v2 returns a data array. 

* Instead of referring to Retweeted and Quoted "statuses", X API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 

* Instead of using both favorites (in Post object) and favourites (in user object), X API v2 uses the term like. 

* X is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Post and user attributes are only included if they have non-null values.

**Request parameters**

The following standard v1.1 request parameters have equivalents in X API v2:

**List members lookup**

|                     |                   |
| :------------------ | :---------------- |
| **Standard v1.1**   | **X API v2**      |
| list\_id            | id                |
| slug                | No equivalent     |
| owner\_screen\_name | No equivalent     |
| owner\_id           | No equivalent     |
| count               | max\_results      |
| cursor              | pagination\_token |
| include\_entities   | No equivalent     |
| skip\_status        | No equivalent     |

**List membership lookup**

|                   |                   |
| :---------------- | :---------------- |
| **Standard v1.1** | **X API v2**      |
| user\_id          | id                |
| screen\_name      | No equivalent     |
| count             | max\_results      |
| cursor            | pagination\_token |
