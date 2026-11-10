---
title: "firectl identity-provider update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/identity-provider-update
path: tools-sdks/firectl/commands/identity-provider-update
---

Updates an identity provider.

```
firectl identity-provider update [flags]
```

Only the flags you pass are changed. For example, passing only `--oidc-client-secret` replaces the client secret and keeps the stored OIDC issuer and client ID. Requires the `admin` role.

### Examples

```
# Rename an identity provider
firectl identity-provider update my-provider --display-name="Updated Company SSO"

# Rotate an OIDC client secret (other OIDC settings are kept)
firectl identity-provider update my-provider --oidc-client-secret="<new-client-secret>"

# Change the SAML metadata URL
firectl identity-provider update accounts/my-account/identityProviders/my-provider \
  --saml-metadata-url="https://company.okta.com/app/xyz/sso/saml/metadata"
```

### Flags

```
      --display-name string             The display name of the identity provider
      --dry-run                         Print the request proto without running it.
      --enable-idp-initiated-sso        Enable IdP-initiated SAML SSO. When enabled, users can login from their identity provider's portal. Only supported for SAML providers.
      --enable-jit-user-provisioning    Enable Just-In-Time (JIT) user provisioning
      --enforce-sso                     Enforce SSO authentication and restrict account access to approved email domains only
  -h, --help                            help for update
      --jit-default-role string         Default role for JIT-provisioned users (admin, user, contributor, inference-user). Defaults to inference-user.
      --oidc-client-id string           The OIDC client ID for OIDC providers
      --oidc-client-secret string       The OIDC client secret for OIDC providers
      --oidc-issuer string              The OIDC issuer URL for OIDC providers
  -o, --output Output                   Set the output format to "text", "json", or "flag". (default text)
      --saml-metadata-url string        The SAML metadata URL for SAML providers
      --saml-metadata-xml-file string   Path to SAML metadata XML file. Use when your IdP metadata URL is not publicly accessible (e.g., behind a VPN).
      --tenant-domains string           Comma-separated list of allowed domains for the organization (e.g., 'example.com,example.co.uk')
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
