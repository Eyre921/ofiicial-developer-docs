---
title: "About GraphQL"
source: https://shopify.dev/docs/apps/build/graphql.md
path: docs/apps/build/graphql
---

---
title: About GraphQL
description: >-
  Get an introduction into GraphQL, its benefits over REST, and how you can use
  GraphQL at Shopify.
source_url:
  html: 'https://shopify.dev/docs/apps/build/graphql'
  md: 'https://shopify.dev/docs/apps/build/graphql.md'
---

# About GraphQL

**Note:**

The REST Admin API is a legacy API as of October 1, 2024. All apps and integrations should be built with the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql). For details and migration steps, visit our [migration guide](https://shopify.dev/docs/apps/build/graphql/migrate).

GraphQL has become Shopify's technology of choice for building APIs. If you're used to working with REST APIs, then GraphQL might seem confusing at first. When you begin using GraphQL, you need to change how you think about retrieving and working with data. The following guides introduce you to GraphQL concepts and help you begin experimenting with GraphQL.

***

## What is Graph​QL?

GraphQL is a query language and a runtime system. Clients form requests by using the GraphQL query language, and the GraphQL server executes the request and returns the data in a response. The following are GraphQL request types:

* [**Queries**](https://shopify.dev/docs/apps/build/graphql/basics/queries): Requests to retrieve data, similar to a `GET` request in REST
* [**Mutations**](https://shopify.dev/docs/apps/build/graphql/basics/mutations): Requests to create and modify data, similar to a `PUT`, `POST`, or `DELETE` request in REST

Unlike REST APIs, which have different endpoints for each resource, a GraphQL API has a single endpoint for all available data. Clients specify the data they need, for both read and write operations, and the server responds with only that data.

GraphQL request structures resemble JSON. However, GraphQL requests don't use quotes for field names and don't have colons separating field names and values. Responses are in JSON format.

The following is a simple GraphQL query and the JSON response:

## POST /admin/api/{api\_version}/graphql.json

## GraphQL query

```graphql
query {
  product(id: "gid://shopify/Product/10079785100") {
    title
    handle
    createdAt
  }
}
```

## JSON response

```json
{
  "data": {
    "product": {
      "title": "The T-Shirt",
      "handle": "the-t-shirt",
      "createdAt": "2024-01-27T19:24:10Z"
    }
  }
}
```

In the JSON response, the structure within the top-level data object mirrors the structure of the corresponding GraphQL request.

### Additional types

In addition to queries and mutations, the GraphQL type system includes the following types:

| Type | Description |
| - | - |
| Scalar | Primitive data types such as strings, Booleans, and integers. Can also represent unstructured data like a JSON blob. These are the basic building blocks of the GraphQL schema.GraphQL has the following built-in scalar types:- **Int**: A signed 32-bit integer
- **Float**: A signed double-precision floating-point value
- **String**: A UTF-8 character sequence
- **Boolean**: A `true` or `false` Boolean value
- **ID**: A unique identifier, which is often used either to refetch an object or as the key for a cache. The value isn't intended to be human-readable. |
| Enum | A scalar that's restricted to a set of allowed values.Enums enable you to validate that arguments of this type are one of the allowed values, and communicate through the type system that a field will always be one of a finite set of values. |
| Object | A fundamental unit that represents a structured set of data. Object types are collections of readable fields, where each field represents a type in the GraphQL type system and defines the kind of data that you can fetch.Object types are the most common units in a GraphQL schema, and they enable data to be modeled in a structural and relational way. |
| Input object | Similar to an object type, but used as input arguments in queries and mutations.Input objects enable you to pass complex, structured data to mutations.The key difference between input object and object types is that input objects are for inputs, or arguments to queries and mutations, and objects are for outputs, or data that you can fetch. |
| Interface | An abstract type that defines a specific set of fields that any object implementing the interface must contain.This mechanism ensures that different object types implementing the same interface share common fields, and promotes consistency across the objects. |
| Union | A type that can return one of several specific object types that are defined in the schema.Unlike interfaces, unions don't enforce common fields between these object types. The object type that's returned in a specific case is determined at runtime. This is useful when a field could return different object types, and these types don't necessarily share any fields.Refer to an example of the [`discount` union.](https://shopify.dev/docs/api/admin-graphql/latest/queries/discountNode#examples-Retrieve_a_discount_by_its_ID) |
| List | An array of another GraphQL type, for example an array of scalars or objects. |

***

## Benefits of Graph​QL over REST

Shopify's REST and GraphQL APIs have some similarities. For example, they're versioned, require authentication and explicit access scopes, and enforce rate limits. However, there are several benefits to using GraphQL over REST, summarized in the following table:

| GraphQL | REST |
| - | - |
| **Work with multiple resources in a single query or mutation**Use GraphQL features like connections, variables, fragments, and aliases for efficient queries and fetch data from multiple types in one request. | **Work with one resource at a time**REST APIs are designed to return a single resource type per endpoint. Fetching associated data often requires multiple calls or chained requests. |
| **Request only the data that you need**Reduce payload size, improve performance, and reduce over-fetching by requesting the exact data that you need. | **Limited resource filtering**Filter top-level resource properties using the `fields` parameter. However, filtering isn't available for properties of child resources. |
| **Strongly typed and part of a schema**GraphQL is strongly typed, which provides for safer data handling through validation and autocompletion.Everything that's available through a GraphQL API is included in its schema. | **Weakly typed and lacking machine-readable data**REST data is weakly typed and has fewer validation guardrails. This can lead to errors or unpredictable results due to incorrect data formatting. |
| **Shopify knows what data an app is using**Shopify knows which fields each app is using, which makes it easier for us to evolve our APIs over time and focus on resources that the community uses.We can easily mark a part of our schema as deprecated, which is reflected in documentation. | **Shopify doesn't know what data an app is using**When an app requests a REST endpoint, Shopify has no way of knowing if it's actually using every piece of data that's returned. It's similar to doing a `SELECT *` to a SQL database.When Shopify needs to make breaking changes, such as removing an attribute from a response, we can't know which developers the change directly affects. This means that we need to notify all developers who use an endpoint, which creates noise for those who aren't affected. |
| **Documentation is a first-class citizen**The documentation for a GraphQL API lives side-by-side with the code that constitutes it. Using GraphQL's introspection feature, you can query the schema to explore its contents and documentation. | **Documentation is secondary**Most REST APIs lack embedded metadata. Apps are dependent on external documentation that can become out of sync with the API. |

### Example

In GraphQL, you can get information about related objects with a single request to a single endpoint, and scope your request down to only the fields that you need.

For example, in the case of an order, you might want to know the total price, the customer's name, metafields, and the title of other variants belonging to the product in the order.

Using REST, you need to make a request to the following endpoints and filter out unnecessary data:

* `/orders/{order_id}.json`
* `/products/{product_id}/variants.json`
* `/customers/{customer_id}/metafields.json`

Using GraphQL, you can make a single request using connections to get the desired data:

## Example

## Endpoint

```text
POST https://{shop}.myshopify.com/admin/api/{api_version}/graphql.json
```

## GraphQL query

```graphql
query {
  order(id:"gid://shopify/Order/5369369690390") {
    id
    totalPriceSet{
      shopMoney {
        amount
      }
    }
    customer {
      displayName
      metafields (first:10) {
        edges {
          node {
            key
            value
          }
        }
      }
    }
    lineItems (first:10) {
      edges {
        node {
          variant {
            product {
              variants(first:10) {
                edges {
                  node {
                    title
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

## JSON response

```json
{
  "data": {
    "order": {
      "id": "gid://shopify/Order/5369369690390",
      "totalPriceSet": {
        "shopMoney": {
          "amount": "2099.85"
        }
      },
      "customer": {
        "displayName": "Ayumu Hirano",
        "metafields": {
          "edges": [
            {
              "node": {
                "key": "birth_date",
                "value": "1990-02-22"
              }
            }
          ]
        }
      },
      "lineItems": {
        "edges": [
          {
            "node": {
              "variant": {
                "product": {
                  "variants": {
                    "edges": [
                      {
                        "node": {
                          "title": "Ice"
                        }
                      },
                      {
                        "node": {
                          "title": "Dawn"
                        }
                      }
                    ]
                  }
                }
              }
            }
          }
        ]
      }
    }
  }
}
```

***

## Graph​QL concepts

Refer to the following guides to learn the fundamentals of GraphQL:

[Queries\
\
](https://shopify.dev/docs/apps/build/graphql/basics/queries)

[Retrieve data from Shopify using queries.](https://shopify.dev/docs/apps/build/graphql/basics/queries)

[Mutations\
\
](https://shopify.dev/docs/apps/build/graphql/basics/mutations)

[Create and modify Shopify data using mutations.](https://shopify.dev/docs/apps/build/graphql/basics/mutations)

[Variables\
\
](https://shopify.dev/docs/apps/build/graphql/basics/variables)

[Write reusable requests using variables.](https://shopify.dev/docs/apps/build/graphql/basics/variables)

[Advanced concepts\
\
](https://shopify.dev/docs/api/usage/graphql-basics/advanced)

[Supercharge your requests using inline fragments, and learn how to build requests that contain multiple queries.](https://shopify.dev/docs/api/usage/graphql-basics/advanced)

[Optimized requests\
\
](https://shopify.dev/docs/apps/build/graphql/migrate/learn-how#optimizing-your-requests)

[Review some tips for refining requests to optimize performance and lower query costs.](https://shopify.dev/docs/apps/build/graphql/migrate/learn-how#optimizing-your-requests)

### Additional guides

Refer to the following guides to learn more about how GraphQL APIs work at Shopify:

[Pagination\
\
](https://shopify.dev/docs/api/usage/pagination-graphql)

[Retrieve consecutive pages of resources using cursor-based pagination.](https://shopify.dev/docs/api/usage/pagination-graphql)

[Global IDs\
\
](https://shopify.dev/docs/api/usage/gids)

[Learn about the identifiers that Shopify uses for objects in GraphQL.](https://shopify.dev/docs/api/usage/gids)

[Bulk operations\
\
](https://shopify.dev/docs/api/usage/bulk-operations)

[Read and write high volumes of data and avoid throttling using asynchronous operations.](https://shopify.dev/docs/api/usage/bulk-operations)

[Rate limits\
\
](https://shopify.dev/docs/api/usage/limits#rate-limits)

[Learn about the rate limits for each API.](https://shopify.dev/docs/api/usage/limits#rate-limits)

[Error handling\
\
](https://shopify.dev/docs/apps/build/graphql/migrate/learn-how#understanding-error-handling)

[Learn about detecting and recovering from errors in GraphQL.](https://shopify.dev/docs/apps/build/graphql/migrate/learn-how#understanding-error-handling)

***

## Tools and resources

Explore the following developer tools and resources to learn more about Shopify GraphQL APIs. For a complete list of APIs, and for information about the libraries that you can use to interact with them, explore our [API documentation](https://shopify.dev/docs/api).

[.dev Assistant\
\
](https://shopify.dev/docs/apps/build/graphql?assistant=1)

[Generate GraphQL operations, convert REST requests to GraphQL operations, and get interactive help with Shopify's AI-powered assistant.\
\
Trained on Shopify data for high accuracy.](https://shopify.dev/docs/apps/build/graphql?assistant=1)

[GraphQL Admin API reference\
\
](https://shopify.dev/docs/api/admin-graphql)

[Consult the complete reference to Shopify’s GraphQL Admin API.](https://shopify.dev/docs/api/admin-graphql)

[Shopify Admin API GraphiQL explorer\
\
](https://shopify.dev/docs/api/usage/api-exploration/admin-graphiql-explorer)

[Browse Shopify’s GraphQL Admin API schema and documentation.](https://shopify.dev/docs/api/usage/api-exploration/admin-graphiql-explorer)

[GraphQL Storefront API reference\
\
](https://shopify.dev/docs/api/storefront)

[Consult the complete reference to Shopify’s GraphQL Storefront API.](https://shopify.dev/docs/api/storefront)

[Shopify Storefront API GraphiQL explorer\
\
](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/api-exploration/graphiql-storefront-api)

[Browse Shopify’s Storefront API schema and documentation.](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/api-exploration/graphiql-storefront-api)

[Shopify GraphiQL app\
\
](https://shopify-graphiql-app.shopifycloud.com/)

[Explore your store's data, and test queries and mutations, using the GraphQL Admin and Storefront APIs.](https://shopify-graphiql-app.shopifycloud.com/)

***

