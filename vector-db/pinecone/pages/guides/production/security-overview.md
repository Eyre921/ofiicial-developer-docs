---
title: "Security overview"
source: https://docs.pinecone.io/guides/production/security-overview
path: guides/production/security-overview
---

Overview of Pinecone security features for production: API keys, SSO, service accounts, audit logs, CMEK encryption, backups, and Private Endpoints.

## Access management

### API keys

Each Pinecone [project](/guides/projects/understanding-projects) has one or more [API keys](/guides/projects/manage-api-keys). In order to make calls to the Pinecone API, a user must provide a valid API key for the relevant Pinecone project.

You can [manage API key permissions](/guides/projects/manage-api-keys) in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/keys). For the roles you can assign to an API key and the operations each role covers, see [Project roles](/guides/projects/understanding-projects#project-roles).

### Organization single sign-on (SSO)

SSO allows organizations to manage their teams' access to Pinecone through their identity management solution. Once your integration is configured, you can require that users from your domain sign in through SSO, and you can specify a default role for teammates when they sign up. SSO is available on Standard and Enterprise plans.

For more information, see [configure single sign on](/guides/production/configure-single-sign-on/okta).

### Role-based access controls (RBAC)

Pinecone uses role-based access controls (RBAC) to manage access to resources.

Service accounts, API keys, and users are all *principals*. A principal's access is determined by the *roles* assigned to it. Roles are assigned to a principal for a *resource*, either a project or an organization. The roles available to be assigned depend on the type of principal and resource.

You can manage roles in the [Pinecone console](https://app.pinecone.io) or programmatically with the Admin API. For more information, see [Manage roles and access](/guides/production/manage-rbac).

#### Service account roles

A service account can be assigned roles for the organization it belongs to, and any projects within that organization. For more information, see [Organization roles](/guides/organizations/understanding-organizations#organization-roles) and [Project roles](/guides/projects/understanding-projects#project-roles).

#### API key roles

An API key can be assigned any [project role](/guides/projects/understanding-projects#project-roles) except `ProjectOwner`, `ProjectManager`, and `ProjectMember`, and only for the project it belongs to. For more information, see [API keys](#api-keys).

#### User roles

A user can be assigned roles for each organization they belong to, and any projects within that organization. For more information, see [Organization roles](/guides/organizations/understanding-organizations#organization-roles) and [Project roles](/guides/projects/understanding-projects#project-roles).

## Compliance

<Note>
  To learn more about data privacy and compliance at Pinecone, visit the [Pinecone Trust and Security Center](https://security.pinecone.io/).
</Note>

### Audit logs

<Note>
  To enable and manage audit logs, you must be an [organization owner](/guides/organizations/understanding-organizations#organization-roles). This feature is available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

[Audit logs](/guides/production/configure-audit-logs) provide a detailed record of user and API actions that occur within Pinecone.

Events are captured every 30 minutes and each log batch will be saved into its own file as a JSON blob, keyed by the time of the log to be written. Only logs since the integration was created and enabled will be saved.

Audit log events adhere to a standard JSON schema and include the following fields:

```jsonc JSON theme={null}
{
    "id": "00000000-0000-0000-0000-000000000000",
    "organization_id": "AA1bbbbCCdd2EEEe3FF",
    "organization_name": "example-org",
    "client": {
        "userAgent": "rawUserAgent"
    },
    "actor": {
        "principal_id": "00000000-0000-0000-0000-000000000000",
        "principal_name": "example@pinecone.io",
        "principal_type": "user", // user, api_key, service_account
        "display_name": "Example Person" // Only in case of user
    },
	"event": {
        "time": "2024-10-21T20:51:53.697Z",
        "action": "create",
        "resource_type": "index",
        "resource_id": "uuid",
        "resource_name": "docs-example",
        "outcome": {
            "result": "success",
            "reason": "", // Only displays for "result": "failure"
            "error_code": "", // Only displays for "result": "failure"
        },
        "parameters": { // Varies based on event
        }
	}
}
```

The following events are captured in the audit logs:

* [Organization events](#organization-events)
* [Project events](#project-events)
* [Index events](#index-events)
* [User and API key events](#user-and-api-key-events)
* [Security and governance events](#security-and-governance-events)

#### Organization events

| Action            | Query parameters                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| Rename org        | `event.action: update`, `event.resource_type: organization`, `event.resource_id: NEW_ORG_NAME`                 |
| Delete org        | `event.action: delete`, `event.resource_type: organization`, `event.resource_id: DELETED_ORG_NAME`             |
| Create org member | `event.action: create`, `event.resource_type: user`, `event.resource_id: [ARRAY_OF_USER_EMAILS]`               |
| Update org member | `event.action: update`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, role: NEW_ROLE }` |
| Delete org member | `event.action: delete`, `event.resource_type: user`, `event.resource_id: USER_EMAIL`                           |

#### Project events

| Action                     | Query parameters                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Create project             | `event.action: create`, `event.resource_type: project`, `event.resouce_id: PROJ_NAME`                              |
| Update project             | `event.action: update`, `event.resource_type: project`, `event.resource_id: PROJECT_NAME`                          |
| Delete project             | `event.action: delete`, `event.resource_type: project`, `event.resource_id: PROJECT_NAME`                          |
| Invite project member      | `event.action: create`, `event.resource_type: user`, `event.resource_id: [ARRAY_OF_USER_EMAILS]`                   |
| Update project member role | `event.action: update`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, role: NEW_ROLE }`     |
| Delete project member      | `event.action: delete`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, project: PROJ_NAME }` |

#### Index events

| Action        | Query parameters                                                                        |
| ------------- | --------------------------------------------------------------------------------------- |
| Create index  | `event.action: create`, `event.resource_type: index`, `event.resouce_id: INDEX_NAME`    |
| Update index  | `event.action: update`, `event.resource_type: index`, `event.resource_id: INDEX_NAME`   |
| Delete index  | `event.action: delete`, `event.resource_type: index`, `event.resource_id: INDEX_NAME`   |
| Create backup | `event.action: create`, `event.resource_type: backup`, `event.resource_id: BACKUP_NAME` |
| Delete backup | `event.action: delete`, `event.resource_type: backup`, `event.resource_id: BACKUP_NAME` |

#### User and API key events

| Action         | Query parameters                                                                        |
| -------------- | --------------------------------------------------------------------------------------- |
| User login     | `event.action: login`, `event.resource_type: user`, `event.resouce_id: USERNAME`        |
| Create API key | `event.action: create`, `event.resource_type: api-key`, `event.resource_id: API_KEY_ID` |
| Delete API key | `event.action: delete`, `event.resource_type: api-key`, `event.resource_id: API_KEY_ID` |

#### Security and governance events

| Action                  | Query parameters                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| Create Private Endpoint | `event.action: create`, `event.resource_type: private-endpoints`, `event.resource_id: PRIVATE_ENDPOINT_ID` |
| Delete Private Endpoint | `event.action: delete`, `event.resource_type: private-endpoints`, `event.resource_id: PRIVATE_ENDPOINT_ID` |

## Data protection

### Customer-managed encryption keys (CMEK)

Data within a Pinecone project can be encrypted using [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek). This allows you to encrypt your data using keys that you manage in your cloud provider's key management system (KMS). Pinecone supports CMEK using Amazon Web Services (AWS) KMS.

For [Bring your own cloud (BYOC)](/guides/production/bring-your-own-cloud), you use KMS on infrastructure in your own account rather than this console CMEK integration.

### Backup and recovery

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

A backup is a static copy of your index that only consumes storage. It is a non-queryable representation of a set of records. You can [create a backup](/guides/manage-data/back-up-an-index) of an index, and you can [create a new index from a backup](/guides/manage-data/restore-an-index). This allows you to restore the index with the same or different configurations.

For more information, see [Understanding backups](/guides/manage-data/backups-overview).

### Encryption at rest

Pinecone encrypts stored data using the 256-bit Advanced Encryption Standard (AES-256) encryption algorithm.

### Encryption in transit

Pinecone uses standard protocols to encrypt user data in transit. Clients open HTTPS or gRPC connections to the Pinecone API; the Pinecone API gateway uses gRPC connections to user deployments in the cloud. These HTTPS and gRPC connections use the TLS 1.2 protocol with 256-bit Advanced Encryption Standard (AES-256) encryption.

<img alt="Diagram showing encryption protocols for user data in transit" />

Traffic is also encrypted in transit between the Pinecone backend and cloud infrastructure services, such as S3 and GCS. For more information, see [Google Cloud Platform](https://cloud.google.com/docs/security/encryption-in-transit) and [AWS security documentation](https://docs.aws.amazon.com/AmazonS3/userguide/UsingEncryption.html).

## Network security

<a />

### Private Endpoints

Use [Private Endpoints](/guides/production/configure-private-endpoints) to connect via AWS PrivateLink or Azure Private Link. This establishes private connectivity between your Pinecone serverless indexes and your cloud VPC/VNet while keeping traffic off the public internet.

<img alt="PrivateLink diagram" />

Private Endpoints are additive to other Pinecone security features: data is also [encrypted in transit](#encryption-in-transit), [encrypted at rest](#encryption-at-rest), and an [API key](#api-keys) is required to authenticate.

### Proxies

The following Pinecone SDKs support the use of proxies:

* [Python SDK](/reference/sdks/python/overview#proxy-configuration)
* [Node.js SDK](/reference/sdks/node/overview#proxy-configuration)
