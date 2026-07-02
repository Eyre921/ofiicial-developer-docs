---
title: "Manage API keys"
source: https://docs.pinecone.io/guides/assistant/admin/manage-api-keys
path: guides/assistant/admin/manage-api-keys
---

Create and manage API keys with custom permissions.

Each Pinecone [project](/guides/projects/understanding-projects) has one or more API keys. In order to [make calls to the Pinecone API](/guides/get-started/quickstart), you must provide a valid API key for the relevant Pinecone project.

This page shows you how to [create](#create-an-api-key), [view](#view-api-keys), [change permissions for](#change-api-key-permissions), and [delete](#delete-an-api-key) API keys.

<Warning>
  If you use custom API key permissions, ensure that you [target your index by host](/guides/manage-data/target-an-index#target-by-index-host-recommended) when performing data operations such as `upsert` and `query`.
</Warning>

## Create an API key

You can create a new API key for your project, as follows:

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).

    2. Select your project.

    3. Go to **API keys**.

    4. Click **Create API key**.

    5. Enter an **API key name**.

    6. Select the **Permissions** to grant to the API key. For a description of the permission roles, see [API key permissions](/guides/production/security-overview#api-keys).

       <Note>
         Users on the Starter and Builder plans can set the permissions to **All** only. To customize the permissions further, [upgrade to the Standard or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
       </Note>

    7. Click **Create key**.

    8. Copy and save the generated API key in a secure place for future use.

       <Warning>
         You will not be able to see the API key again after you close the dialog.
       </Warning>

    9. Click **Close**.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API.
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_PROJECT_ID="YOUR_PROJECT_ID"
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl -X POST "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
           -H "X-Pinecone-Api-Version: 2025-10" \
           -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
           -d '{
                 "name": "example-api-key",
                 "roles": ["ProjectEditor"]
               }'
      ```

      ```bash CLI theme={null}
      # Target the project for which you want to create an API key.
      pc target -o "example-org" -p "example-project"
      # Create the API key
      pc api-key create -n "example-api-key" --roles ProjectEditor
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "key": {
          "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
          "name": "example-api-key",
          "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
          "roles": [
            "ProjectEditor"
          ],
          "created_at": "2025-10-20T23:40:27.069075Z"
        },
        "value": "..."
      }
      ```

      ```text CLI theme={null}
      ATTRIBUTE     VALUE
      Name          example-api-key
      ID            62b0dbfe-3489-4b79-b850-34d911527c88
      Value         ...
      Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
      Roles         ProjectEditor
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## View project API keys

You can [view the API keys](/reference/api/latest/admin/list_api_keys) for your project:

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select your project.
    3. Go to the **API keys** tab.

    You will see a list of all API keys for the project, including their names, IDs, and permissions.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API.
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl -X GET "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
           -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
           -H "X-Pinecone-Api-Version: 2025-10"
      ```

      ```bash CLI theme={null}
      PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

      pc api-key list -i $PINECONE_PROJECT_ID
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "data": [
          {
            "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
            "name": "example-api-key",
            "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
            "roles": [
              "ProjectEditor"
            ],
            "created_at": "2025-10-20T23:39:43.665754Z"
          },
          {
            "id": "0d0d3678-81b4-4e0d-a4f0-70ba488acfb7",
            "name": "example-api-key-2",
            "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
            "roles": [
              "ProjectEditor"
            ],
            "created_at": "2025-10-20T23:43:13.176422Z"
          }
        ]
      }
      ```

      ```text CLI theme={null}
      Organization: example-organization (ID: -NM7af6f234168c4e44a)
      Project: example-project (ID: 32c8235a-5220-4a80-a9f1-69c24109e6f2)

      API Keys

      NAME                 ID                                      PROJECT ID                              ROLES
      example-api-key      62b0dbfe-3489-4b79-b850-34d911527c88    32c8235a-5220-4a80-a9f1-69c24109e6f2    ProjectEditor
      example-api-key-2    0d0d3678-81b4-4e0d-a4f0-70ba488acfb7    32c8235a-5220-4a80-a9f1-69c24109e6f2    ProjectEditor
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## View API key details

You can [view the details of an API key](/reference/api/latest/admin/fetch_api_key):

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select your project.
    3. Go to the **API keys** tab.
    4. In the row of the API key you want to change, in the **Actions** column, click **ellipsis (...) menu > Settings**.

    You will see the API key's name, ID, and permissions.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API.
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl -X GET "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
           -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
           -H "accept: application/json" \
           -H "X-Pinecone-Api-Version: 2025-10"
      ```

      ```bash CLI theme={null}
      PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

      pc api-key describe -i $PINECONE_API_KEY_ID
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
        "name": "example-api-key",
        "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "roles": [
          "ProjectEditor"
        ],
        "created_at": "2025-10-22T19:27:21.202955Z"
      }
      ```

      ```text CLI theme={null}
      ATTRIBUTE     VALUE
      Name          example-api-key
      ID            62b0dbfe-3489-4b79-b850-34d911527c88
      Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
      Roles         ProjectEditor
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Update an API key

<Note>
  Users on the Starter and Builder plans cannot change API key permissions once they are set. Instead, [create a new API key](#create-an-api-key) or [upgrade to the Standard or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
</Note>

If you are a [project owner](/guides/projects/understanding-projects#project-roles), you can update the name and roles of an API key:

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).

    2. Select your project.

    3. Go to the **API keys** tab.

    4. In the row of the API key you want to change, in the **Actions** column, click **ellipsis (...) menu > Settings**.

    5. Change the name and/or permissions for the API key as needed.

       For information about the different API key permissions, refer to [Understanding security - API keys](/guides/production/security-overview#api-keys).

    6. Click **Update**.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API.
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl -X PATCH "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
           -H "X-Pinecone-Api-Version: 2025-10" \
           -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
           -d '{
                 "name": "new-api-key-name",
                 "roles": ["ProjectEditor"]
               }'
      ```

      ```bash CLI theme={null}
      PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

      # Target the organization that contains the API key.
      pc target -o "example-org"
      # Update the API key name.
      pc api-key update -i $PINECONE_API_KEY_ID -n "new-api-key-name"
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
        "name": "new-api-key-name",
        "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "roles": [
          "ProjectEditor"
        ],
        "created_at": "2025-10-22T19:27:21.202955Z"
      }
      ```

      ```text CLI theme={null}
      ATTRIBUTE     VALUE
      Name          new-api-key-name
      ID            62b0dbfe-3489-4b79-b850-34d911527c88
      Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
      Roles         ProjectEditor
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Delete an API key

If you are a [project owner](/guides/projects/understanding-projects#project-roles), you can delete your API key:

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select your project.
    3. Go to the **API keys** tab.
    4. In the row of the API key you want to change, in the **Actions** column, click **ellipsis (...) menu > Delete**.
    5. Enter the **API key name**.
    6. Click **Confirm deletion**.

       <Warning>
         Deleting an API key is irreversible and will immediately disable any applications using the API key.
       </Warning>
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API.
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl -X DELETE "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
           -H "X-Pinecone-Api-Version: 2025-10" \
           -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
      ```

      ```bash CLI theme={null}
      PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

      # Delete the API key. Use --skip-confirmation to skip
      # the confirmation prompt.
      pc api-key delete -i $PINECONE_API_KEY_ID
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```text curl theme={null}
      No response payload
      ```

      ```text CLI theme={null}
      [WARN] This operation will delete API key example-api-key from project example-project.
      [WARN] Any integrations that authenticate with this API key will immediately stop working.
      [WARN] This action cannot be undone.
      Do you want to continue? (y/N): y
      [INFO] You chose to continue delete.
      [SUCCESS] API key example-api-key deleted
      ```
    </CodeGroup>
  </Tab>
</Tabs>
