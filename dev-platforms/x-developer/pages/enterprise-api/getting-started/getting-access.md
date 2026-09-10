---
title: "Getting enterprise access"
source: https://docs.x.com/enterprise-api/getting-started/getting-access
path: enterprise-api/getting-started/getting-access
---

Apply for X Enterprise API access, work with your dedicated account team during onboarding, and get credentials configured for your data volume.

Enterprise access requires an application and onboarding process. Your dedicated account team will help you get set up with credentials and configure your access.

<Button href="/forms/enterprise-api-interest">Apply for Enterprise access</Button>

***

## Step 1: Apply for enterprise access

<Steps>
  <Step title="Submit an application">
    [Fill out the Enterprise interest form](/forms/enterprise-api-interest) with details about your organization and use case.
  </Step>

  <Step title="Discuss your needs">
    Our sales team will reach out to understand your data volume, endpoint requirements, and support needs.
  </Step>

  <Step title="Get a custom package">
    Receive a tailored plan with pricing, rate limits, and access levels designed for your use case.
  </Step>
</Steps>

***

## Step 2: Get onboarded

Once your Enterprise plan is in place, your dedicated account manager will help you set up:

<Steps>
  <Step title="Create your developer app">
    Set up your app in the [Developer Console](https://console.x.com) with Enterprise-level access.
  </Step>

  <Step title="Configure your access">
    Your account manager will help configure rate limits, endpoint access, and any custom settings.
  </Step>

  <Step title="Generate credentials">
    Generate your API keys and tokens for authentication.
  </Step>
</Steps>

***

## Step 3: Save your credentials

You'll receive several credentials depending on your authentication needs:

| Credential                | Purpose                                                                  |
| :------------------------ | :----------------------------------------------------------------------- |
| **API Key & Secret**      | Identify your app. Used to generate tokens and sign OAuth 1.0a requests. |
| **Bearer Token**          | App-only authentication for reading public data.                         |
| **Access Token & Secret** | Make requests on behalf of your own account (OAuth 1.0a).                |
| **Client ID & Secret**    | OAuth 2.0 authentication for user-context requests.                      |

<Warning>
  **Save immediately.** X only displays credentials once. Store them in a password manager or secure vault. If you lose them, regenerate them (which invalidates the old ones).
</Warning>

***

## Which credentials do you need?

<Tabs>
  <Tab title="Reading public data">
    Use the **Bearer Token** for simple, read-only access to public data.

    ```bash theme={null}
    curl "https://api.x.com/2/users/by/username/xdevelopers" \
      -H "Authorization: Bearer $BEARER_TOKEN"
    ```

    Best for: Searching posts, looking up users, reading trends.
  </Tab>

  <Tab title="Acting as a user">
    Use **OAuth 2.0** (recommended) or **OAuth 1.0a** to act on behalf of users.

    OAuth 2.0 offers fine-grained scopes—request only the permissions you need.

    Best for: Posting, liking, following, accessing DMs.

    [OAuth 2.0 guide →](/resources/fundamentals/authentication/oauth-2-0/overview)
  </Tab>

  <Tab title="Acting as yourself">
    Use your **Access Token & Secret** to make requests as your own account.

    These tokens represent the account that owns the app.

    Best for: Testing, personal bots, your own automation.
  </Tab>
</Tabs>

***

## Credential security best practices

<CardGroup>
  <Card title="Use environment variables" icon="terminal">
    Never hardcode credentials in your source code.
  </Card>

  <Card title="Don't commit to git" icon="code-branch">
    Add credential files to `.gitignore`.
  </Card>

  <Card title="Rotate regularly" icon="arrows-rotate">
    Regenerate credentials periodically as a security measure.
  </Card>

  <Card title="Use minimal scopes" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-shield-check.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=768533bde161ac68862de87449f011c3">
    Only request the OAuth permissions your app needs.
  </Card>
</CardGroup>

***

## Next steps

<CardGroup>
  <Card title="Make your first request" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/getting-started/make-your-first-request">
    Call the API with your new credentials.
  </Card>

  <Card title="Learn about authentication" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-key.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=de93497af2dde62afd3a06e896d330f5" href="/resources/fundamentals/authentication/overview">
    Understand OAuth 1.0a and OAuth 2.0.
  </Card>
</CardGroup>
