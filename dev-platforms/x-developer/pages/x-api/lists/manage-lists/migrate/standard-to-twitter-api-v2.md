---
title: "v1 to v2"
source: https://docs.x.com/x-api/lists/manage-lists/migrate/standard-to-twitter-api-v2
path: x-api/lists/manage-lists/migrate/standard-to-twitter-api-v2
---

If you have been working with the standard v1.1 POST lists/create, POST lists/destroy, and POST. Reference for the X API v2 standard tier covering migrate.

### Manage Lists: Standard v1.1 compared to X API v2

If you have been working with the standard v1.1 [POST lists/create](https://developer.x.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create), [POST lists/destroy](https://developer.x.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy), and [POST lists/update](https://developer.x.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-update) endpoints, the goal of this guide is to help you understand the similarities and differences between the standard v1.1 and X API v2 manage List endpoints.

* **Similarities**
  * Authentication
* **Differences**
  * Endpoint URLs
  * App and Project requirements
  * HTTP methods
  * Rate limits
  * Request parameters

#### Similarities

**Authentication**

Both endpoint versions support [OAuth 1.0a User Context](https://developer.x.com/content/developer-twitter/resources/fundamentals/authentication). Therefore, if you were previously using one of the standard v1.1 manage Lists endpoints, you can continue using the same authentication method if you migrate to the X API v2 version.

#### Differences

**Endpoint URLs**

* Standard v1.1 endpoints:
  * POST [https://api.x.com/1.1/lists/create.json](https://api.x.com/1.1/lists/create.json)
    (Creates a List)
  * POST [https://api.x.com/1.1/lists/destroy.json](https://api.x.com/1.1/lists/destroy.json)
    (Deletes a List)
  * POST [https://api.x.com/1.1/lists/update.json](https://api.x.com/1.1/lists/update.json)
    (Updates a List)
* X API v2 endpoint:
  * POST [https://api.x.com/2/lists](https://api.x.com/2/lists)
    (Creates a List)

  * DELETE [https://api.x.com/2/lists/:id](https://api.x.com/2/lists/:id)
    (Deletes a List)

  * PUT [https://api.x.com/2/lists/:id](https://api.x.com/2/lists/:id)
    (Updates a List)

**Rate limits**

\| **Standard v1**
