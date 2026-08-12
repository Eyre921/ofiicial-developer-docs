---
title: "Share Netlify Build Plugins"
source: https://docs.netlify.com/extend/develop-and-share/share-build-plugins.md
path: extend/develop-and-share/share-build-plugins
---

---
title: "Share Build Plugins"
description: "Learn what requirements you must meet to share your build plugins by publishing them to npm."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

If you'd like to share your plugin with others, you can [publish it to npm](#publish-to-npm). All Netlify Build Plugins in the [npm Public Registry](https://npmjs.com) can be installed by any Netlify user through [file-based installation](/extend/install-and-use/build-plugins#file-based-installation).

## Publish to npm

To publish a Build Plugin to npm, follow npm's documentation for [contributing packages to the registry](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry).

Be sure to add the following properties to your plugin's `package.json` file:

- [`name`](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#name) should start with `netlify-plugin-` (such as
  `netlify-plugin-example` or `@scope/netlify-plugin-example`). It should match the plugin `name` field. It is
  recommended for the plugin repository to be named like this as well.
- [`keywords`](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#keywords) should contain the `netlify` and `netlify-plugin`
  keywords. The same applies to [GitHub topics](https://github.com/topics). This helps users find your plugin.
- [`repository`](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#repository) and
  [`bugs`](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#bugs) should be defined. Those are displayed to users when an error
  occurs inside your plugin.

