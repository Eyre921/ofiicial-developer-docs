---
title: "Eleventy Static Site Generator on Netlify"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/eleventy.md
path: build/frameworks/framework-setup-guides/eleventy
---

---
title: "Eleventy on Netlify"
description: "Learn about Eleventy on our platform and requirements for build plugins in Eleventy applications. Use edge functions to dynamically render templates."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Eleventy (11ty) is a flexible and configurable open source static site generator. Although it's written in JavaScript, it doesn't depend on a specific framework for generating or serving content.

## Key features

These features provide important benefits for Eleventy projects, including ones built and deployed with Netlify.

- **JavaScript-friendly.** Eleventy was developed as a JavaScript alternative to Jekyll. It's not dependent on a client-side JavaScript framework or library, which means it doesn't predetermine your frontend stack.
- **Flexible config.** By default, Eleventy requires no configuration, but it has flexible options for custom setup. It is intentionally decoupled from frameworks, build pipelines, and other tools in order to support your preferences.
- **Adaptable project structure.** Eleventy works with your project's existing directory structure and generates HTML based on the templates, content, and data you provide.
- **Choice of templating.** By default, Eleventy uses the template language [Liquid](https://www.11ty.dev/docs/languages/liquid/). However, it supports many [template languages](https://www.11ty.dev/docs/languages/) and allows them to be mixed and combined. This allows a project to migrate to or adopt Eleventy gradually over time.

## Netlify integration

When you [link a repository](/manage/projects/add-new-project/#import-from-an-existing-repository) for a project, Netlify tries to detect the framework your site is using. If your site is built with Eleventy, Netlify provides a suggested build command and output directory: `eleventy` and `_site`. If you're using the CLI to run [Netlify Dev](/api-and-cli-guides/cli-guides/local-development) for a local development environment, Netlify also suggests a dev command and port: `eleventy --serve` and `8080`. You can override suggested values or set them in a configuration file instead, but automatic framework detection may help simplify the process of setting up an Eleventy site on Netlify.

For manual configuration, check out the [typical build settings](/build/frameworks/overview#eleventy) for Eleventy.

### Edge Functions

Edge Functions connect the Netlify platform and workflow with an open runtime standard at the network edge. This enables you to build fast, personalized web experiences with an ecosystem of development tools.

You can browse a [full library of reference examples](https://edge-functions-examples.netlify.app/) for different ways to use Edge Functions. For more details, check out the [Edge Functions documentation](/build/edge-functions/overview).

Eleventy has [a dedicated plugin](https://www.11ty.dev/docs/plugins/edge/) to take advantage of Edge Functions on Netlify, allowing you to use dynamic template languages on the edge to dynamically render templates and modify build-time generated content. This unlocks [many new use cases](https://demo-eleventy-edge.netlify.app/) in a performance-focused way with zero client-side JavaScript: forms, cookies, user personalization, A/B testing, and more.

### Requirement for Build Plugins

To use a Netlify build plugin with your Eleventy site, you must update your site's `.gitignore` file. Without this change, installed Netlify build plugins and all current versions of Eleventy will both attempt to use `.netlify/plugins/node_modules/`, resulting in build errors. As a workaround, we recommend you change `node_modules` to `**/node_modules/**` in the `.gitignore` file.

## More resources

- [Typical Eleventy build settings](/build/frameworks/overview#eleventy)
- [Netlify Blog: Eleventy posts](https://www.netlify.com/blog/tags/Eleventy/)
- [Learn Jamstack video course](https://www.netlify.com/blog/2020/03/12/learn-jamstack-with-a-free-3.5-hour-video-of-demos-and-examples/#main) with corresponding [Eleventy example site](https://github.com/philhawksworth/fcc-3-build-with-ssg)
- [Eleventy documentation](https://www.11ty.dev/docs/)

