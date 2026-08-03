---
title: "List model configurations"
source: https://docs.together.ai/reference/dmi/configs-list
path: reference/dmi/configs-list
---

openapi.yaml GET /projects/{projectId}/configs
Lists production-ready configuration revisions compatible with a reference model. Specify the model with `referenceModel` or the deprecated `referenceModelId`; if both are supplied, they must identify the same model. Results include public configurations and configurations owned by the specified project.
