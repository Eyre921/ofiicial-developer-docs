---
title: "GitHub"
source: https://docs.trychroma.com/cloud/sync/github
path: cloud/sync/github
---

Sync GitHub repositories into Chroma Cloud.

## Walkthrough

When syncing a new version of a repository, Chroma forks the existing collection using copy-on-write and only processes the diff, so re-syncs are fast and storage-efficient.

## Direct Sync

Direct Sync is the default syncing method, which uses the Chroma Cloud GitHub app. To use your own custom GitHub app, use [Platform Sync](/cloud/sync/github#platform-sync).

1. **Prerequisites**

   This walkthrough assumes that you have a GitHub account with at least one repository.

2. **New database setup**

   If you do not already have a Chroma Cloud account, you will need to create one at [trychroma.com](https://www.trychroma.com). After creating an account, you can create a database by specifying a name:

   ![Create database screen](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_create_database.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=5220f46021cae5a7e499f214281a819b)

   On the setup screen, select "Sync a GitHub repo":

   ![Onboarding screen for syncing a GitHub repo](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_new_db_onboarding.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=51d0ad54884b809feddc953e1eba024a)

   Install the Chroma GitHub App into your GitHub account or organization:

   ![GitHub app installation screen](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_new_db_github_install.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=45c99e24d08e331ef6504facf0fe159b)

   And follow the prompts to initiate sync. Choose the **repo** to sync code from, the **branch or commit hash** version of the code to index, and new **collection name** for the synced code. (The collection will be created by the syncing process, and must not exist yet.)

   ![/sync repo to Chroma Collection UI](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_install.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=539ed22801adcd5feab8b76bfd3d0d89)

3. **Existing database setup**

   Open an existing database in Chroma Cloud, and select "Sync" from the menu:

   ![/sync tab in Chroma Cloud UI](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_existing_db.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=159bbc3995b6b6bb48a22bca1102de46)

   On the Sync page, select "Create" to begin syncing code. If you have not already connected GitHub, you may be prompted to install the Chroma Cloud GitHub app again.

   ![Create path for a new Sync](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_existing_db_add.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=748b97800d89f2ce326a934cb8c7896f)

   Then, follow the prompts to initiate sync. Choose the **repo** to sync code from, the **branch or commit hash** version of the code to index, and a new **collection name** for the synced code. (The collection will be created by the syncing process, and must not exist yet.)

   ![Create flow for a new Sync](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_existing_db_sync.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=194259df8ad5dbd68022c471c5f7e39a)

4. **Viewing an Invocation**

   Each Sync create a new Invocation. When completed, select "View Collection" to see the new Chroma collection containing the synced code:

   ![Invocation screen for a Sync](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/db_invocation.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=35840ad5dc28a6046ab62608d0e802e8)

## Platform Sync

**Team & Enterprise only**

Platform Sync is only available on Chroma Cloud [Team and Enterprise plans](https://trychroma.com/pricing).

1. **Prerequisites**

   This walkthrough assumes that you have already [created a GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps) and installed it into at least one GitHub account or organization.

   The GitHub App must have read-only access to the "Contents" and "Metadata" permissions listed under "Repository permissions." These permissions ensure Chroma can index repositories authorized on the GitHub app.

   ![GitHub App contents](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/gh-contents.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=0da708687d6e0460ae38c8184f0ebf62)

   ![GitHub App metadata](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/gh-metadata.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=8b9b2ea022eca81b6057fcd8856914bf)

2. **Setup**

   If you do not already have a Chroma Cloud account, you will need to create one at [trychroma.com](https://www.trychroma.com). After creating an account, you can create a database by specifying a name:

   ![Create database screen](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_create_database.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=5220f46021cae5a7e499f214281a819b)

   Once you have a database, you should create an API key to be able to access the Sync Function's API. You can choose to make this API key scoped to all databases on your account or only the one you just created:

   ![API key issuance for Chroma Cloud](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/api_keys.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=c8a627fa7dae1dece9b959a7ce877260)

   The final setup step is to grant Chroma access to the repositories to which your GitHub App has access. You will need to retrieve the app's ID and private key from GitHub:

   ![GitHub App ID](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/github_app_id.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=5a88d883040055f04b11fe1f3a5fce50)

   ![GitHub Secret Key](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/github_secret_key.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=382e99be6cff3755d637f4360ad21e16)

   With these credentials, navigate to the "Sync" -> "New GitHub sync" -> "Register your GitHub app" to configure your GitHub App with Chroma.

   ![Platform setup](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/platform_setup.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=da80cb7ce05cf01d9ec5798ade3e319f)

   On the "Connect your custom GitHub app" screen, submit the App ID and private key from GitHub:

   ![Creating a custom github app](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/custom-github-app-screen.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=62cb9907833db5c76691ed9519aca249)

3. **Creating a source**

   To create a source, you must send an API request to the Sync Function's API:

   ```bash theme={null}
   curl -X POST https://sync.trychroma.com/api/v1/sources \
       -H "x-chroma-token: <YOUR_CHROMA_API_KEY>" \
       -H "Content-Type: application/json" \
       -d '{
           "database_name": "<YOUR_DATABASE_NAME>",
           "embedding_model": "Qwen/Qwen3-Embedding-0.6B",
           "github": {
           "repository": "chroma-core/chroma",
           "app_id": "<YOUR_GITHUB_APP_ID>"
           }
       }'
   ```

4. **Invoking the Sync Function**

   To invoke the Sync Function, you must select a source on which to create the invocation. See the previous step for details on how to create a source. Once you select the source in the UI, you can invoke the Sync Function by clicking "Create invocation":

   ![Creating a custom sync invocation](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/custom_source_invocation.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=ef35cf1e8dbaf9dda4cfb7ec0a699334)

   Alternatively, you can invoke the Sync Function by sending an API request to the Sync Function's API:

   ```bash theme={null}
   curl -X POST https://sync.trychroma.com/api/v1/sources/{source_id}/invocations \
       -H "x-chroma-token: <YOUR_CHROMA_API_KEY>" \
       -H "Content-Type: application/json" \
       -d '{
           "target_collection_name": "<YOUR_TARGET_COLLECTION_NAME>",
           "ref_identifier": {
                   // only one of these should be supplied
                   "branch": "<YOUR_BRANCH_NAME>",
                   "sha": "<YOUR_COMMIT_SHA>"
               }
       }'
   ```
