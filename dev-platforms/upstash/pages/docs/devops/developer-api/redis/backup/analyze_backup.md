---
title: "Analyze Backup"
source: https://upstash.com/docs/devops/developer-api/redis/backup/analyze_backup
path: docs/devops/developer-api/redis/backup/analyze_backup
---

/devops/developer-api/openapi.yaml post /redis/backup-analysis/{id}/{backupid}
This endpoint starts the offline analysis of a completed backup. The analysis scans the backup without touching the running database and takes minutes for large backups; poll the GET endpoint until the state is completed or failed. Available for databases on a Pro plan or with the Production Pack; other databases get 404. Not available for RDB exports, backups over 200 GiB, HIPAA databases or regional databases, nor for a backup whose analysis is already pending or completed.
