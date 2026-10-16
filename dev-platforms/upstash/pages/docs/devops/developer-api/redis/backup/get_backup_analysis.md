---
title: "Get Backup Analysis"
source: https://upstash.com/docs/devops/developer-api/redis/backup/get_backup_analysis
path: docs/devops/developer-api/redis/backup/get_backup_analysis
---

/devops/developer-api/openapi.yaml get /redis/backup-analysis/{id}/{backupid}
This endpoint returns the state of a backup's analysis and, once completed, the report. Daily backups of databases on a Pro plan or with the Production Pack are analyzed automatically when they complete, except on regional and HIPAA databases and for backups over 200 GiB.
