---
title: "Consumer authentication"
source: https://docs.pinecone.io/guides/marketplace/consumer-auth-overview
path: guides/marketplace/consumer-auth-overview
---

Configure consumer sign-in for a Pinecone Marketplace deployment using link access or Google sign-in to control who can use your knowledge application.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Consumer authentication controls who can use a published knowledge application. Each deployment configures its own consumer authentication independently.

## Available providers

| Provider                          | Use it for                                                                                |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| [Link access](#link-access)       | Internal pilots, demos, or applications you intend to share with anyone who has the link. |
| [Google sign-in](#google-sign-in) | Applications used by people in a Google-based organization.                               |

## How to choose

* Pick **link access** when you need the lowest-friction option and the application does not require identifying who asked what.
* Pick **Google sign-in** when you want interactions tied to a Google account.

You can change the consumer authentication provider from the deployment dashboard. Changing the provider creates a new building version; publish the version to apply the change.

## Link access

Link access is the lowest-friction consumer authentication option. Anyone who has the deployment URL can use the knowledge application without signing in. Use it for internal pilots, demos, and applications where you do not need to identify who is asking questions.

### Configure link access

1. Open the deployment dashboard.
2. Go to **Access**.
3. Set the consumer authentication provider to **Link**.
4. Save the change. Marketplace creates a new building version.
5. Publish the version. See [Publish a deployment](/guides/marketplace/publish-a-deployment).

### Share the URL

Once a deployment is published, copy its URL from the dashboard and send it to end users. End users open the URL and start using the application immediately.

### What link access does and does not do

| Does                                         | Does not do                      |
| -------------------------------------------- | -------------------------------- |
| Let anyone with the link use the application | Identify individual end users    |
| Log events for every interaction             | Tie events to a user identity    |
| Apply the deployment's scope and guardrails  | Provide row-level access control |

If you need to know who asked what, use [Google sign-in](#google-sign-in) instead.

## Google sign-in

Google sign-in requires end users to authenticate with Google before using the knowledge application. Use it when you want every interaction tied to a verified Google account.

### Configure Google sign-in

1. Open the deployment dashboard.
2. Go to **Access**.
3. Under **Access**, select the Google sign-in option.
4. Configure the allowed sign-in scope: restrict to one or more email domains, or allow any Google account.
5. Save the change. Marketplace creates a new building version.
6. Publish the version.

### Sign-in flow

When end users open the deployment URL, they are prompted to sign in with Google. Marketplace checks the email against the allowed scope. Authorized users land in the application; unauthorized users see a friendly access-denied page. Sessions persist until the end user signs out.

### Revoking access

To revoke an end user's access, update the allowed sign-in scope to exclude their email or domain, then publish the change. Existing sessions for excluded users will fail on next request.

## Sessions and identity

When end users sign in:

* Their session is scoped to the deployment.
* Their identity is recorded in the [event log](/guides/marketplace/analytics-and-event-logs) for traceability.
* Their feedback is associated with their identity.

Link access does not establish an end-user identity. Events from link-accessed applications are still logged, without the user attribution.

## Sharing the application

After publishing, copy the deployment URL from the dashboard and share it with end users. The URL is the entry point regardless of which consumer authentication provider is configured.
