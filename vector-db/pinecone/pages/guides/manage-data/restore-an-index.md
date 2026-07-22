---
title: "Restore an index"
source: https://docs.pinecone.io/guides/manage-data/restore-an-index
path: guides/manage-data/restore-an-index
---

Restore serverless indexes from backup snapshots.

## Create a serverless index from a backup

When restoring a serverless index from backup, you can change the index name, tags, and deletion protection setting. All other properties of the restored index will remain identical to the source index, including cloud and region by default, dimension and similarity metric, and associated embedding model when restoring an index with [integrated embedding](/guides/index-data/indexing-overview#integrated-embedding). To restore a backup into a different region than the source index, see [Restore to a different region](#restore-to-a-different-region).

To [create a serverless index from a backup](/reference/api/latest/control-plane/create_index_from_backup), provide the ID of the backup, the name of the new index, and, optionally, changes to the index tags and deletion protection settings:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index_from_backup(
      backup_id="a65ff585-d987-4da5-a622-72e19a6ed5f4",
      name="restored-index",
      tags={
          "tag0": "val0", 
          "tag1": "val1"
      },
      deletion_protection="enabled"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const response = await pc.createIndexFromBackup({
    backupId: 'a65ff585-d987-4da5-a622-72e19a6ed5f4',
    name: 'restored-index',
    tags: {
      tag0: 'val0',
      tag1: 'val1'
    },
    deletionProtection: 'enabled'
  });

  console.log(response);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateIndexFromBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String backupID = "a65ff585-d987-4da5-a622-72e19a6ed5f4";
          String indexName = "restored-index";

          CreateIndexFromBackupResponse backupResponse = pc.createIndexFromBackup(backupID, indexName);
          System.out.println(backupResponse);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"
  	"time"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	indexName := "restored-index"
  	restoredIndexTags := pinecone.IndexTags{"restored_on": time.Now().Format("2006-01-02 15:04")}
  	createIndexFromBackupResp, err := pc.CreateIndexFromBackup(ctx, &pinecone.CreateIndexFromBackupParams{
  		BackupId: "e12269b0-a29b-4af0-9729-c7771dec03e3",
  		Name:     indexName,
  		Tags:     &restoredIndexTags,
  	})

  	fmt.Printf(prettifyStruct(createIndexFromBackupResp))
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="a65ff585-d987-4da5-a622-72e19a6ed5f4"

  curl "https://api.pinecone.io/backups/$BACKUP_ID/create-index" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -H 'Content-Type: application/json' \
    -d '{
          "name": "restored-index",
          "tags": {
            "tag0": "val0",
            "tag1": "val1"
          },
          "deletion_protection": "enabled"
        }'
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  {'deletion_protection': 'enabled',
   'dimension': 1024,
   'embed': {'dimension': 1024,
             'field_map': {'text': 'chunk_text'},
             'metric': 'cosine',
             'model': 'multilingual-e5-large',
             'read_parameters': {'input_type': 'query', 'truncate': 'END'},
             'vector_type': 'dense',
             'write_parameters': {'input_type': 'passage', 'truncate': 'END'}},
   'host': 'example-dense-index-python3-govk0nt.svc.aped-4627-b74a.pinecone.io',
   'metric': 'cosine',
   'name': 'example-dense-index-python3',
   'spec': {'serverless': {'cloud': 'aws', 'region': 'us-east-1'}},
   'status': {'ready': True, 'state': 'Ready'},
   'tags': {'tag0': 'val0', 'tag1': 'val1'},
   'vector_type': 'dense'}
  ```

  ```javascript JavaScript theme={null}
  {
    restoreJobId: 'e9ba8ff8-7948-4cfa-ba43-34227f6d30d4',
    indexId: '025117b3-e683-423c-b2d1-6d30fbe5027f'
  }
  ```

  ```java Java theme={null}
  class CreateIndexFromBackupResponse {
      restoreJobId: e9ba8ff8-7948-4cfa-ba43-34227f6d30d4
      indexId: 025117b3-e683-423c-b2d1-6d30fbe5027f
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "index_id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
    "restore_job_id": "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4"
  }
  ```

  ```json curl theme={null}
  {
      "restore_job_id":"e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
      "index_id":"025117b3-e683-423c-b2d1-6d30fbe5027f"
  }
  ```
</CodeGroup>

<Tip>
  You can create a serverless index from a backup using the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
</Tip>

## Restore to a different region

The [create index from backup](/reference/api/latest/control-plane/create_index_from_backup) endpoint always creates the new index in the same cloud and region as the backup. To restore a backup into a different region, use the `unstable` version of the [create index](/reference/api/latest/control-plane/create_index) endpoint instead. Specify the backup as `source_backup_id` within `spec.serverless` and set the target `region` there.

The following rules apply:

* The target region must be on the same cloud provider as the backup. Restoring to a different cloud provider is not supported.
* The backup must be in the current Pinecone project, and the new index is created in the same project.
* The `dimension`, `metric`, and `vector_type` must match the source index.
* Restoring to a different region is not supported for BYOC indexes.

<Warning>
  Restoring to a different region is in [public preview](/release-notes/feature-availability). It is available through the `unstable` API version and the REST API only.
</Warning>

For example, the following request restores a backup of a dense index hosted in the AWS `us-east-1` region into a new index in the AWS `us-west-2` region:

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: unstable" \
  -d '{
    "name": "restored-index",
    "vector_type": "dense",
    "dimension": 1536,
    "metric": "cosine",
    "spec": {
      "serverless": {
        "cloud": "aws",
        "region": "us-west-2",
        "source_backup_id": "a65ff585-d987-4da5-a622-72e19a6ed5f4"
      }
    }
  }'
```

Because the backup data is copied between regions, restoring to a different region can take longer than restoring within the same region. If restoring to a different region is not yet available for the backup's region, the request fails with a `412 Precondition Failed` error.

## List restore jobs

You can [list all restore jobs](/reference/api/latest/control-plane/list_restore_jobs) as follows.

<Note>
  Up to 100 restore jobs are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of restore jobs are returned instead. Whenever there are additional restore jobs to return, the response also includes a `pagination_token` that you can use to get the next batch of jobs. When the response does not include a `pagination_token`, there are no more restore jobs to return.
</Note>

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  restore_jobs = pc.list_restore_jobs()

  print(restore_jobs)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const restoreJobs = await pc.listRestoreJobs();

  console.log(restoreJobs);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateIndexFromBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API-KEY").build();

          // List all restore jobs with default pagination limit
          RestoreJobList restoreJobList = pc.listRestoreJobs(null, null);

          // List all restore jobs with pagination limit of 5
          RestoreJobList restoreJobListWithLimit = pc.listRestoreJobs(5);

          // List all restore jobs with pagination limit and token
          RestoreJobList restoreJobListPaginated = pc.listRestoreJobs(5, "eyJza2lwX3Bhc3QiOiIxMDEwMy0=");

          System.out.println(restoreJobList);
          System.out.println(restoreJobListWithLimit);
          System.out.println(restoreJobListPaginated);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	limit := 2
  	restoreJobs, err := pc.ListRestoreJobs(ctx, &pinecone.ListRestoreJobsParams{
  		Limit: &limit,
  	})
  	if err != nil {
  		log.Fatalf("Failed to list restore jobs: %v", err)
  	}

  	fmt.Printf(prettifyStruct(restoreJobs))
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/restore-jobs" \
  	-H "X-Pinecone-Api-Version: 2025-10" \
  	-H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  [{
      "restore_job_id": "06b08366-a0a9-404d-96c2-e791c71743e5",
      "backup_id": "95707edb-e482-49cf-b5a5-312219a51a97",
      "target_index_name": "restored-index",
      "target_index_id": "027aff93-de40-4f48-a573-6dbcd654f961",
      "status": "Completed",
      "created_at": "2025-05-15T13:59:51.439479+00:00",
      "completed_at": "2025-05-15T14:00:09.222998+00:00",
      "percent_complete": 100.0
  }, {
      "restore_job_id": "4902f735-b876-4e53-a05c-bc01d99251cb",
      "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
      "target_index_name": "restored-index2",
      "target_index_id": "027aff93-de40-4f48-a573-6dbcd654f961",
      "status": "Completed",
      "created_at": "2025-05-15T21:06:19.906074+00:00",
      "completed_at": "2025-05-15T21:06:39.360509+00:00",
      "percent_complete": 100.0
  }]
  ```

  ```javascript JavaScript theme={null}
  {
    data: [
      {
        restoreJobId: '69acc1d0-9105-4fcb-b1db-ebf97b285c5e',
        backupId: '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
        targetIndexName: 'restored-index2',
        targetIndexId: 'e6c0387f-33db-4227-9e91-32181106e56b',
        status: 'Completed',
        createdAt: 2025-05-14T17:25:59.378Z,
        completedAt: 2025-05-14T17:26:23.997Z,
        percentComplete: 100
      },
      {
        restoreJobId: '9857add2-99d4-4399-870e-aa7f15d8d326',
        backupId: '94a63aeb-efae-4f7a-b059-75d32c27ca57',
        targetIndexName: 'restored-index',
        targetIndexId: '0d8aed24-adf8-4b77-8e10-fd674309dc85',
        status: 'Completed',
        createdAt: 2025-04-25T18:14:05.227Z,
        completedAt: 2025-04-25T18:14:11.074Z,
        percentComplete: 100
      }
    ],
    pagination: undefined
  }
  ```

  ```java Java theme={null}
  class RestoreJobList {
      data: [class RestoreJobModel {
          restoreJobId: cf597d76-4484-4b6c-b07c-2bfcac3388aa
          backupId: 0d75b99f-be61-4a93-905e-77201286c02e
          targetIndexName: restored-index
          targetIndexId: 8a810881-1505-46c0-b906-947c048b15f5
          status: Completed
          createdAt: 2025-05-16T20:09:18.700631Z
          completedAt: 2025-05-16T20:11:30.673296Z
          percentComplete: 100.0
          additionalProperties: null
      }, class RestoreJobModel {
          restoreJobId: 4902f735-b876-4e53-a05c-bc01d99251cb
          backupId: 8c85e612-ed1c-4f97-9f8c-8194e07bcf71
          targetIndexName: restored-index2
          targetIndexId: 710cb6e6-bfb4-4bf5-a425-9754e5bbc832
          status: Completed
          createdAt: 2025-05-15T21:06:19.906074Z
          completedAt: 2025-05-15T21:06:39.360509Z
          percentComplete: 100.0
          additionalProperties: null
      }]
      pagination: class PaginationResponse {
          next: eyJsaW1pdCI6Miwib2Zmc2V0IjoyfQ==
          additionalProperties: null
      }
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "data": [
      {
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "completed_at": "2025-05-16T20:11:30.673296Z",
        "created_at": "2025-05-16T20:09:18.700631Z",
        "percent_complete": 100,
        "restore_job_id": "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
        "status": "Completed",
        "target_index_id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
        "target_index_name": "restored-index"
      },
      {
        "backup_id": "95707edb-e482-49cf-b5a5-312219a51a97",
        "completed_at": "2025-05-15T21:04:34.2463Z",
        "created_at": "2025-05-15T21:04:15.949067Z",
        "percent_complete": 100,
        "restore_job_id": "eee4f8b8-cd3e-45fe-9ed5-93c28e237f24",
        "status": "Completed",
        "target_index_id": "5a0d555f-7ccd-422a-a3a6-78f7b73350c0",
        "target_index_name": "restored-index2"
      }
    ],
    "pagination": {
      "next": "eyJsaW1pdCI6MTAsIm9mZnNldCI6MTB9"
    }
  }
  ```

  ```json curl theme={null}
  {
    "data": [
      {
        "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
        "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
        "target_index_name": "restored-index",
        "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
        "status": "Completed",
        "created_at": "2025-04-25T18:14:05.227526Z",
        "completed_at": "2025-04-25T18:14:11.074618Z",
        "percent_complete": 100
      },
      {
        "restore_job_id": "69acc1d0-9105-4fcb-b1db-ebf97b285c5e",
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "target_index_name": "restored-index2",
        "target_index_id": "e6c0387f-33db-4227-9e91-32181106e56b",
        "status": "Completed",
        "created_at": "2025-05-14T17:25:59.378989Z",
        "completed_at": "2025-05-14T17:26:23.997284Z",
        "percent_complete": 100
      }
    ],
    "pagination": null
  }
  ```
</CodeGroup>

## View restore job details

You can [view the details of a specific restore job](/reference/api/latest/control-plane/describe_restore_job), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  restore_job = pc.describe_restore_job(job_id="9857add2-99d4-4399-870e-aa7f15d8d326")

  print(restore_job)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const restoreJob = await pc.describeRestoreJob('9857add2-99d4-4399-870e-aa7f15d8d326');

  console.log(restoreJob);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateIndexFromBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API-KEY").build();

          RestoreJobModel restoreJob = pc.describeRestoreJob("9857add2-99d4-4399-870e-aa7f15d8d326");

          System.out.println(restoreJob);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	restoreJob, err := pc.DescribeRestoreJob(ctx, "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4")
  	if err != nil {
  		log.Fatalf("Failed to describe restore job: %v", err)
  	}

  	fmt.Printf(prettifyStruct(restoreJob))
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  JOB_ID="9857add2-99d4-4399-870e-aa7f15d8d326"

  curl "https://api.pinecone.io/restore-jobs/$JOB_ID" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json'
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  {'backup_id': '94a63aeb-efae-4f7a-b059-75d32c27ca57',
   'completed_at': datetime.datetime(2025, 4, 25, 18, 14, 11, 74618, tzinfo=tzutc()),
   'created_at': datetime.datetime(2025, 4, 25, 18, 14, 5, 227526, tzinfo=tzutc()),
   'percent_complete': 100.0,
   'restore_job_id': '9857add2-99d4-4399-870e-aa7f15d8d326',
   'status': 'Completed',
   'target_index_id': '0d8aed24-adf8-4b77-8e10-fd674309dc85',
   'target_index_name': 'restored-index'}
  ```

  ```javascript JavaScript theme={null}
  {
    restoreJobId: '9857add2-99d4-4399-870e-aa7f15d8d326',
    backupId: '94a63aeb-efae-4f7a-b059-75d32c27ca57',
    targetIndexName: 'restored-index',
    targetIndexId: '0d8aed24-adf8-4b77-8e10-fd674309dc85',
    status: 'Completed',
    createdAt: 2025-04-25T18:14:05.227Z,
    completedAt: 2025-04-25T18:14:11.074Z,
    percentComplete: 100
  }
  ```

  ```java Java theme={null}
  class RestoreJobModel {
      restoreJobId: cf597d76-4484-4b6c-b07c-2bfcac3388aa
      backupId: 0d75b99f-be61-4a93-905e-77201286c02e
      targetIndexName: restored-index
      targetIndexId: 0d8aed24-adf8-4b77-8e10-fd674309dc85
      status: Completed
      createdAt: 2025-05-16T20:09:18.700631Z
      completedAt: 2025-05-16T20:11:30.673296Z
      percentComplete: 100.0
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "completed_at": "2025-05-16T20:11:30.673296Z",
    "created_at": "2025-05-16T20:09:18.700631Z",
    "percent_complete": 100,
    "restore_job_id": "e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
    "status": "Completed",
    "target_index_id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
    "target_index_name": "restored-index"
  }
  ```

  ```json curl theme={null}
  {
    "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
    "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
    "target_index_name": "restored-index",
    "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
    "status": "Completed",
    "created_at": "2025-04-25T18:14:05.227526Z",
    "completed_at": "2025-04-25T18:14:11.074618Z",
    "percent_complete": 100
  }
  ```
</CodeGroup>
