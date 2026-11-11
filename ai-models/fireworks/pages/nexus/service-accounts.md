---
title: "Service Accounts"
source: https://docs.fireworks.ai/nexus/service-accounts
path: nexus/service-accounts
---

Create a Nexus service account and its API key in Nexus settings, for LLM gateways, CI, and other automated systems that should not use a person's key.

A service account is a non-human user with its own API keys. Use one for an [LLM gateway](/nexus/llm-gateways), a CI pipeline, or a backend service, so the key keeps working when people leave and audit logs show which calls were automated.

* Any member can create a service account and its keys. You don't need to be an admin.
* Service accounts cannot sign in to [nexus.fireworks.ai](https://nexus.fireworks.ai).

> [!NOTE]
>
> Service accounts are managed under **API Keys** in Nexus settings, not on the **Members** page. The [app.fireworks.ai/account/users](https://app.fireworks.ai/account/users) path in the [Platform docs](/accounts/service-accounts) does not exist in Nexus.

## Create a service account and its key

**1. Open API Keys**

Go to [Settings → API Keys](https://nexus.fireworks.ai/settings/api-keys) and click **Create API key**.

**2. Add a service account**

Under **Service Account API Keys**, click **+** to add a service account, and give it a name, such as `prod-litellm`.

**3. Create the key**

Select the new service account and create its key. Copy the `fw_...` key right away and store it in your secret manager. The API Keys page doesn't list service account keys, so you can't find or copy it there later.

To add another key later, for example to rotate one, repeat these steps and pick the existing service account in step 2.

* A service account created in the console gets the default `user` role. To give it a different role, use `firectl` as shown below.
* To see service account keys, an admin can run `firectl api-key list --all-users`.

## Set a role or script it with firectl

Use [`firectl`](/tools-sdks/firectl/firectl) to choose a role when you create the account, change a role, or list service accounts:

```bash theme={null}
firectl user create --user-id "prod-litellm" --service-account --role=inference-user
firectl user update prod-litellm --role=contributor
firectl api-key create --service-account "prod-litellm"
firectl user list --filter 'service_account=true'
```

If you leave out `--role`, the role is `user`. See [User roles](/accounts/users#user-roles) for each role's permissions.

* To match an existing service account, check its role first with `firectl user get <user-id>`.
* `firectl signin` connects to `gateway.fireworks.ai:443` over gRPC (HTTP/2). A corporate proxy that inspects TLS can break that connection, with errors such as `missing selected ALPN property` or `error reading server preface: EOF`. Ask your network team to allow HTTP/2 gRPC to that host or exempt it from TLS inspection, or use the console steps above.

## Billing and audit logs

* Service account usage counts toward your account's quotas and bill, like a member's usage.
* [Spend limits](/nexus/usage-limits) apply to service accounts the same way they apply to members. Check the limit before a gateway or pipeline depends on the key.
* Audit logs show a service account as `<user-id>@<account-id>.sa.fireworks.ai`.
