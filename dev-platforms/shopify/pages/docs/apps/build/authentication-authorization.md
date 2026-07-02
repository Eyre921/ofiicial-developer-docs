---
title: "Authentication"
source: https://shopify.dev/docs/apps/build/authentication-authorization.md
path: docs/apps/build/authentication-authorization
---

---
title: Authentication and authorization
description: >-
  Learn about the different methods of authenticating and authorizing apps with
  Shopify’s platform.
source_url:
  html: 'https://shopify.dev/docs/apps/build/authentication-authorization'
  md: 'https://shopify.dev/docs/apps/build/authentication-authorization.md'
---

# Authentication and authorization

This guide introduces the different methods of authenticating and authorizing apps with Shopify’s platform. Make sure that you understand the differences between the types of authentication and authorization methods before you begin your development process.

You can [use Shopify CLI to generate a starter app](https://shopify.dev/docs/apps/build/scaffold-app) with boilerplate code that handles authentication and authorization. The starter app includes code for an app rendered in the Shopify admin that follows best practices:

* Authorizing your app using [session tokens](https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens) and [token exchange](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/token-exchange).

* Installing on stores using [Shopify managed installation](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation).

  You should use this starter app unless you need to scaffold a standalone app.

[Scaffold an app\
\
](https://shopify.dev/docs/apps/build/scaffold-app)

[Scaffold an app that follows all authentication and authorization best practices.](https://shopify.dev/docs/apps/build/scaffold-app)

***

## Authentication vs.​authorization

Authentication is the process of verifying the identity of the user or the app. To keep transactions on Shopify’s platform [safe and secure](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance), all apps connecting with Shopify APIs must authenticate when making API requests.

Authorization is the process of giving permissions to apps. When an app user installs a Shopify app they authorize the app, enabling the app to acquire an access token. For example, an app might be authorized to access orders and product data in a store.

***

## Types of authentication and authorization methods

The authentication and authorization methods that your app needs to use depends on the tool that you used to create your app, and the components that your app uses.

### Authentication

* Apps rendered in the Shopify admin need to authenticate their incoming requests with [session tokens](https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens).
* Standalone apps need to implement their own authentication method for incoming requests.

### Authorization

Authorization encompasses the installation of an app and the means to acquire an access token.

To avoid unnecessary redirects and page flickers during the app installation process, you should [configure your app's required access scopes using Shopify CLI](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration). This allows Shopify to [manage the installation process for you](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation).

If you aren't able to use Shopify CLI to configure your app, then your app will install as part of the [authorization code grant flow](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant). This provides a degraded user experience.

If you're building an app for your own organization and don't require user interaction, you can use the [client credentials grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant) to acquire access tokens.

The following table outlines the supported installation and token acquisition flows for various app configurations.

Whenever possible, you should create apps rendered in the Shopify admin that use Shopify managed installation and token exchange.

| Type of app | Supported installation flows | Supported token acquisition flows |
| - | - | - |
| App rendered in the Shopify admin | * [Shopify managed installation (recommended)](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation)* [Installation during authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) | * [Token exchange (recommended)](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/token-exchange)* [Authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) |
| Standalone app | * [Shopify managed installation (recommended)](https://shopify.dev/docs/apps/build/authentication-authorization/app-installation)* [Installation during authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) | * [Authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant) |
| Admin-created custom app | * Installed upon generation in the Shopify admin | * [Generate in the Shopify admin](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin) |

OAuth 2.0 is the industry-standard protocol for authorizing or giving permissions to apps. The following video illustrates how OAuth works at Shopify. Note that this video was created before [token exchange](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/token-exchange) was introduced, and might use the term "OAuth" interchangeably with "authorization code grant."

***

## Getting started

* Authenticate your app using [session tokens](https://shopify.dev/docs/apps/build/authentication-authorization/session-tokens).
* Authorize your app using a session token with [token exchange](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/token-exchange).
* Authorize your standalone app with [authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/authorization-code-grant).
* Authenticate your app created in the Shopify admin with [access tokens](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin).

***

## Tools

[Shopify CLI\
\
](https://shopify.dev/docs/apps/build/cli-for-apps)

[A command-line tool to help you build Shopify apps faster](https://shopify.dev/docs/apps/build/cli-for-apps)

[shopify\_api\
\
](https://github.com/Shopify/shopify-api-ruby)

[Shopify’s official Ruby gem for interacting with the Admin API](https://github.com/Shopify/shopify-api-ruby)

[@shopify/shopify-api\
\
](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

[Shopify’s official Node library for interacting with the Storefront and Admin APIs, handling OAuth, webhooks, and billing](https://github.com/Shopify/shopify-app-js/tree/main/packages/apps/shopify-api)

[@shopify/admin-api-client\
\
](https://github.com/Shopify/shopify-app-js/tree/main/packages/api-clients/admin-api-client)

[Shopify’s official lightweight Node library for interacting with the Admin API](https://github.com/Shopify/shopify-app-js/tree/main/packages/api-clients/admin-api-client)

***

