---
title: "Service Accounts"
source: https://docs.fireworks.ai/accounts/service-accounts
path: accounts/service-accounts
---

How to manage and use service accounts in Fireworks

Service accounts in Fireworks allow applications, scripts, and automated systems to authenticate and perform actions securely—without relying on human credentials. They are ideal for CI/CD pipelines, backend services, and automated workflows. Service Accounts let you avoid shared credentials and easily distinguish between what automated systems did vs humans in audit logs.

Service accounts can take actions using an API key, like creating deployments, running models or creating datasets (see [API reference](https://fireworks.ai/docs/api-reference/introduction)). Service accounts cannot login through the web interface or use OIDC tokens.

To manage service accounts via the Fireworks web UI visit [app.fireworks.ai/account/users](https://app.fireworks.ai/account/users).

## Creating a Service Account

Using our firectl you can create service accounts

```bash theme={null}
firectl user create --user-id "my-service-account" --service-account
```

## Creating an API Key for a Service Account

Using firectl you can create an API key on behalf of a service account:

```bash theme={null}
firectl api-key create --service-account "my-service-account"
```

## Roles

You can assign a role when creating a service account using the `--role` flag:

```bash theme={null}
firectl user create --user-id "my-service-account" --service-account --role=contributor
```

If not specified, the default service account role is `user`.

To change the role of an existing service account, use the update command:

```bash theme={null}
firectl user update my-service-account --role=inference-user
```

See [Managing users](/accounts/users) for available roles.

## Listing Service Accounts

To list all service accounts in your account:

```bash theme={null}
firectl user list --filter 'service_account=true'
```

## Billing

* Service accounts count toward the same account quotas and limits assigned to the account
* Usage is tracked by the account, not individual user vs service account

## Auditing

In audit logs users are referenced by their email id's. Service accounts are referenced by `my-service-account@my-account.sa.fireworks.ai`.
