---
title: "Metafields"
source: https://shopify.dev/docs/apps/build/custom-data.md
path: docs/apps/build/custom-data
---

---
title: About metafields
description: Use metafields to extend Shopify's data models.
source_url:
  html: 'https://shopify.dev/docs/apps/build/metafields'
  md: 'https://shopify.dev/docs/apps/build/metafields.md'
---

# About metafields

Shopify includes built-in data models like products, customers, and orders. Metafields extend these models by letting you add custom data to any [Shopify resource](https://shopify.dev/docs/api/admin-graphql/latest/enums/MetafieldOwnerType).

You can use metafields to add warranty information to products, track customer lifetime value, store fulfillment notes on orders, link related products, trigger Shopify Flow automations, or power backend processes. This flexibility lets you extend Shopify's data model for specialized features and business logic.

**Info:**

Metafields add individual custom fields to specific Shopify resources.

* Need to create standalone objects with multiple related fields? Use [metaobjects](https://shopify.dev/docs/apps/build/metaobjects) instead.
* For a deep dive on how to structure your data using both tools, see [Data modeling with metafields and metaobjects](https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).



Want to skip ahead? Choose a path based on what you're building:

* **Building an app**: Use [app-owned metafields](#app-owned-metafields) with TOML configuration.
* **Extending existing store data**: Use [merchant-owned metafields](#merchant-owned-metafields) with GraphQL.

***

## What are metafields?

Metafields are key-value pairs with the following components:

* **Identifier**: A combination of namespace and key (for example, `custom.warranty_info`). Namespaces are logical containers that not only provide organization and prevent naming conflicts, they establish [ownership](#metafield-ownership).
* **Value**: The data being stored.
* **Type**: Defines the kind of value (such as text, number, date, or reference) and how the value is interpreted. [See available types](https://shopify.dev/docs/apps/build/metafields/list-of-data-types).

### Metafield definitions

Before creating a metafield, you will create a metafield definition. Metafield definitions establish data schemas that enable type validation, Shopify admin integration, query filtering, access control, and performance optimization.

**Note:**

Shopify provides pre-built "standard" definitions for common use cases like ISBN numbers, product ingredients, and care instructions. Using standard definitions helps ensure interoperability across the Shopify ecosystem and saves you from defining schemas for well-known data types. Explore [standard metafield definitions](https://shopify.dev/docs/apps/build/metafields/list-of-standard-definitions).

### Metafield ownership

Ownership determines access and control. When creating metafields, you choose between two ownership models:

| **Ownership Type** | **Purpose** | **Namespace** |
| - | - | - |
| App-owned | App-managed data for internal logic, configuration, and workflows | Use reserved namespace `$app` (GraphQL) or `app` (TOML) |
| Merchant-owned | Merchant-managed data shared across all apps | Use any non-reserved namespace, such as `custom` |

**Additional ownership types:**

* **Shopify-reserved**: Metafields with Shopify-controlled namespaces and structures, including those typically prefixed with reserved namespace `shopify--` and [standard definitions](https://shopify.dev/docs/apps/build/metafields/list-of-standard-definitions). Shopify controls the structure, but the metafields are typically [merchant-owned](#merchant-owned-metafields).
* **App-data**: A special type of app-owned metafield tied to your app installation (not to products, customers, or orders) and completely hidden from the Shopify admin. See [App-data metafields](#app-data-metafields) for details.

***

## App-owned metafields

App-owned metafields are custom data entries controlled by your app. Your app manages both the structure and values, which are view only in the Shopify admin (by default).

App-ownership is defined using the `app` reserved namespace.

**Info:**

App-owned data is viewable by default in the Shopify admin. If you need to store data that is not visible, consider [App-data metafields](#app-data-metafields).

### Example

You want to track internal SKU codes for products. Because your app manages inventory tracking, you create an app-owned metafield.

#### Step 1: Create the metafield definition

Create the metafield definition using your app's `shopify.app.toml` file. The following creates the definition with app-owned namespace `app` and key `internal_sku`:

## File

shopify.app.toml

```toml
[product.metafields.app.internal_sku]
name = "Internal SKU"
description = "Internal inventory tracking code"
type = "single_line_text_field"
```

Deploy it with your app:

## Terminal

```bash
shopify app deploy
```

#### Step 2: Create the metafield

After you create the metafield definition, add the metafield (value) using the GraphQL Admin API. Use the same namespace, key, and type from the definition:

## GraphQL

POST https://{shop}.myshopify.com/api/{api\_version}/graphql.json

```graphql
mutation AddInternalSKU {
  productUpdate(
    input: {
      id: "gid://shopify/Product/123456789"
      metafields: [
        {
          namespace: "$app"
          key: "internal_sku"
          value: "INV-2024-COTTON-001"
          type: "single_line_text_field"
        }
      ]
    }
  ) {
    product {
      id
      metafield(namespace: "$app", key: "internal_sku") {
        id
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

**Note:**

Get a product ID by querying `products(first: 1)` in GraphiQL, or find it in the Shopify admin URL when viewing a product: `/admin/products/123456789`.

***

## Merchant-owned metafields

Merchant-owned metafields are custom data entries that merchants and all installed apps can modify. Both the structure and values are editable, making them ideal for shared data across multiple apps.

Create merchant-owned metafields using any [non-reserved namespace](#metafield-ownership) (such as `custom`, `specs`, or `inventory`).

**Info:**

Merchant-owned definitions can't be created in `shopify.app.toml`.

### Example

You want to add warranty information to products. Because this type of field should be managed in the Shopify admin, you use a merchant-owned metafield.

#### Step 1: Create the metafield definition

First, create the metafield definition using the GraphQL Admin API. The following example doesn't use namespace `$app`, so the definition will be merchant-owned:

## GraphQL

POST https://{shop}.myshopify.com/api/{api\_version}/graphql.json

```graphql
mutation {
  metafieldDefinitionCreate(definition: {
    name: "Warranty Information",
    namespace: "custom",
    key: "warranty_info",
    description: "Product warranty details and coverage information",
    type: "multi_line_text_field",
    ownerType: PRODUCT,
    access: {
      storefront: PUBLIC_READ,
    },
  }) {
    createdDefinition {
      name
      namespace
      key
      type
      access
    }
  }
}
```

#### Step 2: Create the metafield

After you create the metafield definition, add the metafield (value). Use the same namespace, key, and type from the definition:

## GraphQL

POST https://{shop}.myshopify.com/api/{api\_version}/graphql.json

```graphql
mutation AddWarrantyInfo {
  productUpdate(
    input: {
      id: "gid://shopify/Product/123456789"
      metafields: [
        {
          namespace: "custom"
          key: "warranty_info"
          value: "2-year manufacturer warranty. Covers defects in materials and workmanship."
          type: "multi_line_text_field"
        }
      ]
    }
  ) {
    product {
      id
      metafield(namespace: "custom", key: "warranty_info") {
        id
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

***

## App-data metafields

App-data metafields are tied to a specific app installation and are completely hidden from the Shopify admin. They're stored on the `AppInstallation` resource and can only be accessed by the owning app via GraphQL or through the [`app` object in Liquid](https://shopify.dev/docs/api/liquid/objects/app). They can't be created using `shopify.app.toml`.

Unlike [app-owned metafields](#app-owned-metafields) on shared resources, the `$app` reserved namespace isn't required because the `AppInstallation` owner provides isolation — only your app can access its own installation's metafields.

**Caution:**

Generally, private app data should be stored in an app-specific, secure database. App-data metafields can be used for per-installation configuration values, but sensitive credentials should be stored in environment variables or a dedicated secret management system.

### Example

You want to store a feature tier configuration for each app installation. Because this data should be completely hidden from merchants and specific to each installation, you use app-data metafields.

#### Step 1: Retrieve the app installation ID

Get the app installation ID using the [`currentAppInstallation`](https://shopify.dev/docs/api/admin-graphql/latest/queries/currentAppInstallation) query:

## POST https://{shop}.myshopify.com/api/{api\_version}/graphql.json

## GraphQL query

```graphql
query {
  currentAppInstallation {
    id
  }
}
```

## Response

```json
{
  "data": {
    "currentAppInstallation": {
      "id": "gid://shopify/AppInstallation/123456"
    }
  }
}
```

#### Step 2: Create the app-data metafield

Create the app-data metafield using the [`metafieldsSet`](https://shopify.dev/docs/api/admin-graphql/current/mutations/metafieldsSet) mutation:

## POST https://{shop}.myshopify.com/api/{api\_version}/graphql.json

## GraphQL mutation

```graphql
mutation CreateAppDataMetafield($metafieldsSetInput: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafieldsSetInput) {
    metafields {
      id
      namespace
      key
    }
    userErrors {
      field
      message
    }
  }
}
```

## Variables

```json
{
  "metafieldsSetInput": [
    {
      "namespace": "app_config",
      "key": "feature_tier",
      "type": "single_line_text_field",
      "value": "premium",
      "ownerId": "gid://shopify/AppInstallation/123456"
    }
  ]
}
```

***

## Permissions

Configure who can read and write your metafields using the `access` settings on your definition.

### Shopify admin permissions

`admin` controls permissions for both the Shopify admin and the GraphQL Admin API.

**For app-owned metafields:**

##### TOML

```toml
# Merchants can view but not edit (default)
access.admin = "merchant_read"

# Merchants can view and edit
access.admin = "merchant_read_write"
```

##### GraphQL

```graphql
access: {
  admin: MERCHANT_READ  # view only (default)
}

access: {
  admin: MERCHANT_READ_WRITE  # view and edit
}
```

**For merchant-owned metafields:**

* Always full access - readable and writable by merchants and all apps with appropriate scopes. No configuration needed.

### Storefront permissions

`storefront` controls permissions for the Storefront API (used by headless and custom storefronts). This setting doesn't affect Liquid templates - metafields are always accessible in Liquid regardless of this setting.

**Available settings:**

##### TOML

```toml
# Hidden from Storefront API (default)
access.storefront = "none"

# Accessible in Storefront API
access.storefront = "public_read"
```

##### GraphQL

```graphql
access: {
  storefront: NONE  # hidden (default)
}

access: {
  storefront: PUBLIC_READ  # accessible
}
```

**Note:**

Metafield access depends on its owning resource.

### Customer accounts permissions

`customer_accounts` controls permissions for the Customer Accounts API.

**Available settings:**

##### TOML

```toml
# Hidden from Customer Accounts API (default)
access.customer_account = "none"

# Readable in Customer Accounts API
access.customer_account = "read"

# Readable and writable in Customer Accounts API
access.customer_account = "read_write"
```

##### GraphQL

```graphql
access: {
  customerAccount: NONE  # hidden (default)
}

access: {
  customerAccount: READ  # readable
}

access: {
  customerAccount: READ_WRITE  # readable and writable
}
```

**Note:**

Customer Account API access levels can only be adjusted via GraphQL Admin API mutation for app-owned metafields (namespace `app--`). For merchant-owned metafields, Customer Account API access can only be configured through the Shopify admin.

***

## Next steps

* Learn how to [model your data structure](https://shopify.dev/docs/apps/build/metaobjects/data-modeling-with-metafields-and-metaobjects).
* Learn how to [work with metafield definitions](https://shopify.dev/docs/apps/build/metafields/definitions).
* Learn how to [work with metafield values](https://shopify.dev/docs/apps/build/metafields/manage-metafields).
* Learn how to use metafields to [query resources](https://shopify.dev/docs/apps/build/metafields/query-using-metafields).
* Learn how to [enable filtering and other advanced features](https://shopify.dev/docs/apps/build/metafields/use-metafield-capabilities).

***

