---
title: "Create a project"
source: https://docs.pinecone.io/admin/projects/create-a-project
path: admin/projects/create-a-project
---

Create a new Pinecone project in your organization using the console or Admin API, including project name, tags, and customer-managed encryption keys (CMEK).

If you're an [organization owner or organization manager](/admin/organizations/understanding-organizations#organization-roles), you can create a project in your organization.

> [tab] Pinecone console
>
> 1. In the Pinecone console, go to [**your profile > Organization settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).
>
> 2. Click **+ Create project**.
>
> 3. Enter a project name in **Give your project a name**.
>
>    > [!NOTE]
>    >
>    > A project name can contain up to 512 characters. For more information, see [Object identifiers](/reference/api/database-limits/identifier-limits).
>
> 4. (Optional) Tags are key-value pairs that you can use to categorize and identify the project. To add a tag, click **+ Add tag** and enter a tag key and value.
>
> 5. (Optional, Enterprise plan) Turn on **Enforce customer managed encryption (CMEK)**. For more information, see [Configure CMEK](/guides/production/configure-cmek).
>
> 6. Click **Create project**.
>
>    To create an index from a sample movies dataset, go to **Database > Quickstart** and click **Load from dataset**.
>
> > [!NOTE]
> >
> > The number of projects per organization varies by plan. For details, see [Projects per organization](/reference/api/database-limits/object-limits). To create additional projects, [upgrade your plan](/admin/billing/upgrade-billing-plan).

> [tab] Code
>
> > [!NOTE]
> >
> > To complete this action through the Admin API, you need an [access token](/admin/organizations/manage-service-accounts#retrieve-an-access-token).
>
> ```bash curl theme={null}
> PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
>
> curl "https://api.pinecone.io/admin/projects" \
>     -H "X-Pinecone-Api-Version: 2026-07" \
> 	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
> 	-d '{
>           "name":"example-project"
>         }'
> ```
>
> ```bash CLI theme={null}
> # Target the organization for which you want to 
> # create a project.
> pc target -o "example-org"
> # Create the project and set it as the target 
> # project for the CLI.
> pc project create -n "example-project" --target
> ```
>
> The example returns a response like the following:
>
> ```json curl theme={null}
> {
>   "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
>   "name": "example-project",
>   "max_pods": 0,
>   "force_encryption_with_cmek": false,
>   "organization_id": "-NM7af6f234168c4e44a",
>   "created_at": "2025-03-16T22:46:45.030Z"
> }
> ```
>
> ```text CLI theme={null}
> [SUCCESS] Project example-cli-project created successfully.
>
> ATTRIBUTE           VALUE
> Name                example-project
> ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
> Organization ID     -NM7af6f234168c4e44a
> Created At          2025-10-27 23:27:46.370088 +0000 UTC
> Force Encryption    false
> Max Pods            5
>
> [SUCCESS] Target project set to example-cli-project
> ```

## Next steps

* [Add users to your project](/admin/projects/manage-project-members#add-members-to-a-project)
* [Create an index](/guides/index-data/create-an-index)
* [Create an assistant](/guides/assistant/create-assistant)
