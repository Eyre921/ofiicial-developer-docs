---
title: "firectl identity-provider create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/identity-provider-create
path: tools-sdks/firectl/commands/identity-provider-create
---

Creates a new identity provider.

```
firectl identity-provider create [flags]
```

### Examples

```
# Create SAML identity provider with metadata URL
firectl identity-provider create --display-name="Company SAML" \
  --saml-metadata-url="https://company.okta.com/app/xyz/sso/saml/metadata"

# Create SAML identity provider with IdP-initiated SSO
firectl identity-provider create --display-name="Company SAML" \
  --saml-metadata-url="https://company.okta.com/app/xyz/sso/saml/metadata" \
  --enable-idp-initiated-sso

# Create SAML identity provider with metadata XML file (when URL is not publicly accessible)
firectl identity-provider create --display-name="Company SAML" \
  --saml-metadata-xml-file="/path/to/metadata.xml"

# Create OIDC identity provider
firectl identity-provider create --display-name="Company OIDC" \
  --oidc-issuer="https://auth.company.com" \
  --oidc-client-id="abc123" \
  --oidc-client-secret="secret456"

# Create OIDC identity provider with multiple domains
firectl identity-provider create --display-name="Example OIDC" \
  --oidc-issuer="https://accounts.google.com" \
  --oidc-client-id="client123" \
  --oidc-client-secret="secret456" \
  --tenant-domains="example.com,example.co.uk"
```

### Flags

```
      --display-name string             The display name of the identity provider (required)
      --dry-run                         Print the request proto without running it.
      --enable-idp-initiated-sso        Enable IdP-initiated SAML SSO. When enabled, users can login from their identity provider's portal. Only supported for SAML providers.
      --enable-jit-user-provisioning    Enable Just-In-Time (JIT) user provisioning. When enabled, users are automatically created on first SSO login if they don't already exist.
      --enforce-sso                     Enforce SSO authentication and restrict account access to approved email domains only
  -h, --help                            help for create
      --jit-default-role string         Default role for JIT-provisioned users (admin, user, contributor, inference-user). Defaults to the least privileged role available for the account.
      --oidc-client-id string           The OIDC client ID for OIDC providers
      --oidc-client-secret string       The OIDC client secret for OIDC providers
      --oidc-issuer string              The OIDC issuer URL for OIDC providers
  -o, --output Output                   Set the output format to "text", "json", or "flag". (default text)
      --saml-metadata-url string        The SAML metadata URL for SAML providers
      --saml-metadata-xml-file string   Path to SAML metadata XML file. Use when your IdP metadata URL is not publicly accessible (e.g., behind a VPN).
      --tenant-domains string           Comma-separated list of allowed domains for the organization (e.g., 'example.com,example.co.uk'). If not provided, domain will be derived from account email.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
