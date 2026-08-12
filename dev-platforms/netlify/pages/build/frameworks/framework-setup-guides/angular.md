---
title: "Angular on Netlify"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/angular.md
path: build/frameworks/framework-setup-guides/angular
---

---
title: "Angular on Netlify"
description: "Learn about Angular on our platform. Rely on our automatic framework detection and add redirects for your Angular application."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Angular is a component-based open source framework for building enterprise-grade single-page applications (SPAs) with client-side routing, server-side rendering, and prerendering. Scully, an open source static site generator, is built specifically for Angular apps.

## Key features

These features provide important benefits for Angular projects, including ones built and deployed with Netlify.

- **Robust integrated tooling.** Using declarative templates, you can extend Angular's template language for more customization. You can also get immediate Angular-specific help and feedback with popular IDEs and editors.
- **Helpfully opinionated.** As a framework, Angular predetermines certain project decisions, but this reduces the number of choices a team has to make. Using features like the [`ng generate`](https://angular.io/cli/generate) command and without relying on third-party libraries, your team can focus on building an app, not the setup.
- **Image optimization**. The [`NgOptimizedImage` directive](https://angular.io/guide/image-directive#getting-started-with-ngoptimizedimage), backed by [Netlify Image CDN](#netlify-image-cdn), makes it easier to adopt performance best practices for loading images.
- **Supported by Google.** Angular is Google's largest application and has the reliability of being backed and maintained by the company. The team also adheres to Long-Term Support (LTS) and has a [public roadmap](https://angular.io/guide/roadmap).
- **Built with TypeScript.** When building out Angular applications, you can take advantage of type safety and tooling using TypeScript. [Strict mode](https://angular.io/guide/strict-mode) can help you avoid type errors before hitting production.

In addition to the Angular-specific items above, Netlify gives you control over [branch and deploy](/deploy/deploy-overview#branches-and-deploys) settings. This allows you to set up continuous deployment according to your project needs, such as only deploying particular branches or creating Deploy Previews on `git push`.

## Netlify integration

Angular applications on Netlify can benefit from integrations such as automatic framework detection and built-in redirects functionality.

### Automatic framework detection

When you [link a repository](/manage/projects/add-new-project/#import-from-an-existing-repository) for a project, Netlify tries to detect the framework your site is using. If your site is built with Angular, Netlify provides a suggested build command: `ng build --prod`. Based on your `angular.json`, Netlify automatically configures the publish directory. If your site has server-side rendering enabled, this is automatically configured using an Edge Function. 

If you're using the CLI to run [Netlify Dev](/api-and-cli-guides/cli-guides/local-development) for a local development environment, Netlify also suggests a dev command and port: `ng serve` and `4200`. You can override suggested values or set them in a configuration file instead, but automatic framework detection may help simplify the process of setting up an Angular app on Netlify.

### Netlify Image CDN

When deploying your Angular applications to Netlify, `NgOptimizedImage` automatically uses [Netlify Image CDN](/build/image-cdn/overview) to optimize and transform images on demand without impacting build times. Netlify Image CDN also handles content negotiation to use the most efficient image format for the requesting client.

To transform a source image hosted on another domain, you must first configure allowed domains in your `netlify.toml` file:

```toml
[images]
  remote_images = ["https://my-images.com/.*", "https://animals.more-images.com/[bcr]at/.*"]
```

The `remote_images` property accepts an array of regex. If your images are in specific subdomains or directories, you can use regex to allow just those subdomains or directories.

Visit the [Angular docs](https://angular.io/guide/image-directive#getting-started-with-ngoptimizedimage) to learn more.

### Redirects

Although we recommend [prerendering your Angular app](https://www.netlify.com/blog/2021/02/08/pre-rendering-with-angular-universal/) or using Scully to produce static files, you may need to use [redirects](/manage/routing/redirects/overview) to enable Angular routing and page refresh functionality for pages with client-side rendering. You can use a `_redirects` file or a [Netlify configuration file](/build/configure-builds/file-based-configuration#redirects) to configure these.

In `_redirects`:

```
/* /index.html 200
```

Make sure you include the `_redirects` file in your `angular.json` assets array so that Angular will include a copy of the file when building your project:

```
"assets": [
  "src/_redirects"
]
```

In `netlify.toml`:

```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Caution - Redirects on SSR

Pages utilizing [Server-Side Rendering (SSR)](https://angular.dev/guide/ssr) are not subject to redirects placed in `_redirects` or `netlify.toml`.
This is because SSR uses Edge Functions, which run before redirects are evaluated.
Instead, use Angular's built-in redirects feature: [Setting up redirects](https://angular.dev/guide/routing/common-router-tasks#setting-up-redirects)

### Accessing `Request` and `Context` during Server-Side Rendering (SSR)

During server-side rendering, you can access the incoming `Request` object and the Netlify-specific `Context` object via the `netlify.request` and `netlify.context` providers:

```ts
import type { Context } from "@netlify/edge-functions"

export class FooComponent {

  constructor(
    // ...
    @Inject('netlify.request') @Optional() request?: Request,
    @Inject('netlify.context') @Optional() context?: Context,
  ) {
    console.log(`Rendering Foo for path ${request?.url} from location ${context?.geo?.city}`)
    // ...
  }
  
}
```

The `Request` and `Context` objects will not be available on the client-side or during [prerendering](https://angular.dev/guide/prerendering#prerendering-parameterized-routes). To test this in local development, run your Angular project using `netlify serve`.

## More resources

- [Video: Angular in the Jamstack](https://www.youtube.com/playlist?list=PLzlG0L9jlhEO5HFKx36Pd6LZ6aY44oseL)
- [Netlify Blog: Angular posts](https://www.netlify.com/tags/angular/)
- [Netlify redirect rules for Angular apps](https://medium.com/@seraya/netlify-redirect-rules-for-angular-6-apps-d9f27ad40449)
- [Angular documentation](https://angular.io/docs)
- [Scully documentation](https://scully.io/docs/learn/overview/)

