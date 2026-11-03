---
title: "Create a team"
source: https://docs.langchain.com/langsmith/smith-api/teams/create-a-team
path: langsmith/smith-api/teams/create-a-team
---

/langsmith/langsmith-platform-openapi.json post /api/v1/platform/orgs/current/teams
Creates an organization-wide team. Needs organization:teams:manage. Workspace scoped
teams are not created here: granting an organization-wide team access to a
workspace creates its workspace scoped team there, so workspace_id and
parent_team_id return 400.
