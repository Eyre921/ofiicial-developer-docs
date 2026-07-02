---
title: "API tokens"
source: https://replicate.com/docs/topics/security/api-tokens.md
path: docs/topics/security/api-tokens
---

You use API tokens to authenticate your requests to Replicate’s HTTP API. These tokens are secrets, and should be treated like passwords. They are 40-character strings that always start with `r8_` and are required when making API requests. You can create and manage multiple API tokens to use with different applications or environments.

[](#using-api-tokens)Using API tokens
-------------------------------------

Pass API tokens in the `Authorization` header of your HTTP requests. Here’s an example using curl:

```bash
curl -s -X POST \
  -H "Authorization: Bearer $REPLICATE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"input": {"prompt": "a cat wearing a hat"}}' \
  https://api.replicate.com/v1/models/black-forest-labs/flux-schnell/predictions
```

You can also use the [Replicate client libraries](https://replicate.com/docs/reference/client-libraries) to make API requests.

[](#creating-api-tokens)Creating API tokens
-------------------------------------------

Replicate creates a default API token when you create your account, but you can create multiple API tokens for different purposes, such as separate tokens for development, staging, and production environments or different projects. To create and manage your API tokens, visit [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens).

Each token can be given a descriptive name to help you identify its purpose and usage.

[](#disabling-api-tokens)Disabling API tokens
---------------------------------------------

If you accidentally expose a token or no longer need it, you can disable it from the web interface. This is useful if you accidentally leaked your token and want to prevent unauthorized use.

To disable a token:

1.  Go to [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)
2.  Find the token you want to disable
3.  Click the disable button next to the token

Once you disable a token, any applications using that token can no longer make API requests. You’ll need to create a new token and update your applications accordingly.

[](#keeping-your-api-tokens-secure)Keeping your API tokens secure
-----------------------------------------------------------------

To keep your API tokens secure, take the following steps:

*   Use environment variables to store your tokens rather than hardcoding them in your source code
*   Use [different tokens](https://replicate.com/account/api-tokens) for different environments (development, staging, production) and applications
*   Refresh your tokens periodically as part of good security hygiene
*   Consider using dedicated secret management services for production applications

[](#automated-token-scanning)Automated token scanning
-----------------------------------------------------

Replicate automatically monitors for API tokens that may have been compromised or accidentally exposed. Our system:

*   Scans public GitHub repositories for accidentally committed API tokens
*   Detects potential token compromise through various security monitoring techniques
*   Automatically disables compromised tokens to protect your account

When we detect a potentially compromised token, we:

1.  Immediately disable the affected token(s) to prevent unauthorized use
2.  Send you an email notification explaining what happened and what steps to take
3.  Provide guidance on how to create replacement tokens and update your applications

The email notification will explain whether we found the token in a public repository or detected other signs of compromise. Any applications using the disabled token will stop working immediately, so you’ll need to:

1.  Create a new API token at [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)
2.  Update your applications to use the new token
3.  If you have other tokens that may have been exposed, consider refreshing or deleting them

This automated protection helps keep your account secure even if tokens are accidentally exposed.
