---
title: "Get a team"
source: https://docs.langchain.com/langsmith/smith-api/teams/get-a-team
path: langsmith/smith-api/teams/get-a-team
---

/langsmith/langsmith-platform-openapi.json get /api/v1/platform/orgs/current/teams/{team_id}
Deprecated: use the corresponding /user-groups endpoint.
Gets one team in the organization.
An organization scoped team needs organization:teams:read.
A workspace scoped team needs workspaces:teams:read in its workspace.
