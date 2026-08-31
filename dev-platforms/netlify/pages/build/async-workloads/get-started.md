---
title: "Async Workloads: Get Started"
source: https://docs.netlify.com/build/async-workloads/get-started.md
path: build/async-workloads/get-started
---

---
title: "Get started with Async Workloads"
description: "Create Async Workload functions in TypeScript and JavaScript. Leverage the AsyncWorkloadClient library to send events to run workloads."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

This page will help you get started with the Async Workloads extension. It describes how to enable the extension, write basic workloads, and send events to them.

## Key concepts

The Async Workloads extension turns Netlify serverless functions into durable, event-driven workloads. When you define workloads, you create serverless functions. Given this, the capabilities and limitations for serverless functions also apply to workloads. Any exceptions will be explicitly noted.

Learn more about [serverless functions](/build/functions/overview).

An Async Workload function is similar to a [background function](/build/functions/background-functions) but is durable, event-driven, and offers more enhanced capabilities. The function runs asynchronously, so it will not return a [`Response` object](https://developer.mozilla.org/en-US/docs/Web/API/Response). Instead, the client can invoke the function by sending a matching event and the workload function can run its logic and persist any state it needs.

## Setup

To get started, install the **Async Workloads** extension for your team. After you install the extension, all sites on your team will be able to build Async Workloads functions.

For teams on the Starter plan, you need to configure the extension with an Async Workloads API key. In the Netlify UI, navigate to 
### NavigationPath Component:

Project configuration > Build & Deploy > Async Workloads
 for the site you want to configure. Select **Create a new API key** to input and save the new API key. For customers on all other plans, this step is optional as an API key is automatically generated for you at the team level upon installing the extension.

Add the `@netlify/async-workloads` module to your project. This will provide the functionality and types for those using TypeScript.

### Tabs Component:

<TabItem label="npm">
```bash title="npm"
npm install @netlify/async-workloads
```
</TabItem>

<TabItem label="pnpm">
```bash title="pnpm"
pnpm add @netlify/async-workloads
```
</TabItem>

<TabItem label="yarn">
```bash title="yarn"
yarn add @netlify/async-workloads
```
</TabItem>

## Write an Async Workload function

Start by adding a serverless function to your project by creating the file in [your functions directory](/build/functions/configuration#directory).

A function file must be written using the [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) syntax and have a [default export](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) with a `asyncWorkloadFn` wrapped handler.

### Tabs Component:

<TabItem label="TypeScript">

```ts title="TypeScript"

export default asyncWorkloadFn((event: AsyncWorkloadEvent) => {

	console.log('Hello, Async Workloads!');

});

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
	events: ['say-hello']
};
```
</TabItem>

<TabItem label="JavaScript">

```js title="JavaScript"

export default asyncWorkloadFn((event) => {

	console.log('Hello, Async Workloads!');

});

export const asyncWorkloadConfig = {
	events: ['say-hello']
};
```
</TabItem>

This workload will be called when the `"say-hello"` event is sent by a client. Once sent, this workload will run and log the message.

## Send your first event

Async Workloads provides a client library called `AsyncWorkloadsClient` that can be used to send events.

The basic flow is to instantiate the client and then send the message.

```ts
const client = new AsyncWorkloadsClient();
// optionally send data
await client.send('EVENT_NAME', {data: {}});
```

Typically, Async Workload functions are triggered by other serverless endpoints that respond to user actions on a website. When this occurs, the client is instantiated and used within that serverless endpoint after other checks are performed or data is aggregated.

The following example is a serverless function that can be called at the `/say-hey` route on the site. When the function is called, it will send the event to the Async Workloads system. At that point, the workload function defined above will run.

### Tabs Component:

<TabItem label="TypeScript">

```ts title="TypeScript"

export default async (req: Request) => {

	// do some work... authenticate the user, pull data, etc.

	const client = new AsyncWorkloadsClient();
	await client.send('say-hello');

  return new Response('', { status: 200 });
};

export const config: Config = {
	path: '/say-hey'
}
```
</TabItem>

<TabItem label="JavaScript">

```js title="JavaScript"

export default async (req) => {

	// do some work... authenticate the user, pull data, etc.

	const client = new AsyncWorkloadsClient();
	await client.send('say-hello');

  return new Response('', { status: 200 });
};

export const config = {
	path: '/say-hey'
}
```
</TabItem>


