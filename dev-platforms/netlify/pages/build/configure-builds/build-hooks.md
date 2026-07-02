---
title: "Netlify Build Hooks"
source: https://docs.netlify.com/build/configure-builds/build-hooks.md
path: build/configure-builds/build-hooks
---

---
title: "Build hooks"
description: "Set up build hooks that trigger new builds and deploys when a URL receives a request. Use build hooks with external services or send requests yourself."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Build hooks are URLs you can use to trigger new builds and deploys. You can find them in 
### NavigationPath Component:

Project configuration > Build & deploy > Continuous deployment > Build hooks
.

![](/images/configure-builds-build-hooks.png)

Select **Add build hook** to create a new build hook. The build hook name is for your reference, and will display in your list of build hooks, as well as in the default deploy message for each deploy triggered by the hook.

Select a branch to build by default. Only branches which have been deployed at least once will appear in this list.

Upon saving your build hook settings, Netlify will give you a unique URL for that build hook. To trigger this hook, you need to send a POST request to that URL.

In most cases, this POST request will be sent from a service you want to integrate with Netlify, but you can also send these requests yourself. For example, you can run a [curl](https://curl.haxx.se/) command from your terminal:

```bash
curl -X POST -d '{}' https://api.netlify.com/build_hooks/5c23354f454e1350f8543e78
```

You can also test build hook requests with tools like [Postman](https://www.postman.com/).

### Note - Note

Builds must be [active](/build/configure-builds/stop-or-activate-builds) for build hooks to trigger builds of your site.

## Parameters

Build hooks accept the following optional URL query parameters to alter the behavior of the triggered build:

- `trigger_branch`: parameter that specifies which repository branch the build will use. If the branch does not exist in your repository at the time of the build, the build will fail, with an error message in the build log.
- `trigger_title`: parameter that specifies a title to replace the default deploy message in your site deploy list.
- `clear_cache`: when set to `true`, this parameter triggers a build with a cleared cache.

Here is an example build hook URL using these parameters:

```bash
https://api.netlify.com/build_hooks/5c23354f454e1350f8543e78?trigger_branch=testing&trigger_title=triggered+by+This+Awesome+Service&clear_cache=true
```

This would trigger a deploy from an existing branch called `testing`, with a custom message: `triggered by This Awesome Service`.

![Deploy list item for a branch deploy from the 'testing' branch, with message, 'triggered by This Awesome Service'.](/images/configure-builds-custom-hook-deploy.png)

## Payload

You can send a custom payload in your build hook POST request. The contents must be passed as a string, which will be URL-encoded and made available in the triggered build as an [environment variable](/build/configure-builds/environment-variables#build-hook-metadata-and-payload). You can access it in the build by using the variable `INCOMING_HOOK_BODY`.
