---
title: "Managing users"
source: https://docs.fireworks.ai/accounts/users
path: accounts/users
---

Add, delete, and manage roles for users in your Fireworks account

See the concepts [page](/getting-started/concepts#account) for definitions of accounts and users.

## User roles

Each user in an account is assigned a role that determines their level of access:

| Role               | Description                                                                                                             |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **Admin**          | Full administrative control over resources, users, and access. Can manage all account settings and add or remove users. |
| **User** (default) | Can manage all resources, including those owned by others, but cannot manage users or access settings.                  |
| **Contributor**    | Can run inference on any resource and create and manage their own resources. Cannot modify resources owned by others.   |
| **Inference User** | Can view all resources and run inference, but cannot create or modify resources.                                        |

<Note>
  The `contributor` and `inference-user` roles are newer roles that provide more granular access control. Contact Fireworks support if you need these roles enabled for your account.
</Note>

#### Resource management

| Permission                                                             | Inference User | Contributor | User | Admin |
| :--------------------------------------------------------------------- | :------------: | :---------: | :--: | :---: |
| Execute inference on any deployment                                    |        ✅       |      ✅      |   ✅  |   ✅   |
| View all resources (deployments, models, fine tuning jobs, datasets)   |        ✅       |      ✅      |   ✅  |   ✅   |
| Create new resources (deployments, models, fine tuning jobs, datasets) |        ❌       |      ✅      |   ✅  |   ✅   |
| Manage their own resources (edit/delete)                               |        ❌       |      ✅      |   ✅  |   ✅   |
| Manage resources owned by others (edit/delete)                         |        ❌       |      ❌      |   ✅  |   ✅   |

#### API key & account management

| Permission                                       | Inference User | Contributor | User | Admin |
| :----------------------------------------------- | :------------: | :---------: | :--: | :---: |
| Manage self-owned API keys (create/delete)       |        ✅       |      ✅      |   ✅  |   ✅   |
| View all users and service accounts              |        ✅       |      ✅      |   ✅  |   ✅   |
| Create service account API keys                  |        ❌       |      ❌      |   ❌  |   ✅   |
| Delete other users and service accounts API keys |        ❌       |      ❌      |   ❌  |   ✅   |
| Add/modify/delete users and their access         |        ❌       |      ❌      |   ❌  |   ✅   |

## Adding users

To add a new user to your Fireworks account, run the following command. If the email for the new user is already associated with a Fireworks account, they will have the option to freely switch between your account and their existing account(s). You can also add users in the Fireworks web UI at [https://app.fireworks.ai/account/users](https://app.fireworks.ai/account/users).

```bash theme={null}
firectl user create --email="alice@example.com"
```

To create another admin user, pass the `--role=admin` flag:

```bash theme={null}
firectl user create --email="alice@example.com" --role=admin
```

## Updating a user's role

To update a user's role, run

```bash theme={null}
firectl user update <USER_ID> --role=<ROLE>
```

Where `<ROLE>` is one of: `admin`, `user`, `contributor`, or `inference-user`.

## Deleting users

You can remove a user from your account by running:

```bash theme={null}
firectl user delete <USER_ID>
```
