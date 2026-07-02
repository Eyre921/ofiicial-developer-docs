---
title: "Code sandbox"
source: https://docs.together.ai/docs/together-code-sandbox
path: docs/together-code-sandbox
---

Level-up generative code tooling with fast, secure code sandboxes at scale

Together Code Sandbox offers a fully configurable development environment with fast start-up times, robust snapshotting, and a suite of mature dev tools.

Together Code Sandbox can spin up a sandbox by cloning a template in under 3 seconds. Inside this VM, you can run any code, install any dependencies and even run servers.

Under the hood, the SDK uses the microVM infrastructure of CodeSandbox to spin up sandboxes. It supports:

* Memory snapshot/restore (checkpointing) at any point in time
* Resume/clone VMs from a snapshot in 3 seconds
* VM FS persistence (with git version control)
* Environment customization using Docker & Docker Compose (Dev Containers)

## Accessing Together Code Sandbox

Code Sandbox is a Together product that is currently available on our [custom plans](https://www.together.ai/contact-sales).\
A self-serve option is possible by creating an account with [CodeSandbox](https://codesandbox.io/pricing).

> 📌 About CodeSandbox.io
>
> [CodeSandbox](https://codesandbox.io/blog/joining-together-ai-introducing-codesandbox-sdk) is a Together company that is in the process of migrating all relevant products to the Together platform. In the coming months, all Code Sandbox features will be fully migrated into your Together account.
>
> Note that Together Code Sandbox is referred to as the SDK within the CodeSandbox.io

## Getting Started

To get started, install the SDK:

```text Text theme={null}
npm install @codesandbox/sdk
```

Then, create an API token by going to [https://codesandbox.io/t/api](https://codesandbox.io/t/api), and clicking on the "Create API Token" button. You can then use this token to authenticate with the SDK:

```typescript TypeScript theme={null}
import { CodeSandbox } from "@codesandbox/sdk";
 
const sdk = new CodeSandbox(process.env.CSB_API_KEY!);
 
const sandbox = await sdk.sandboxes.create();
 
const session = await sandbox.connect();
 
const output = await session.commands.run("echo 'Hello World'");
 
console.log(output) // Hello World
```

<br />

## Sandbox life-cycle

By default a Sandbox will be created from a template. A template is a memory/fs snapshot of a Sandbox, meaning it will be a direct continuation of the template. If the template was running a dev server, that dev server is running when the Sandbox is created.

When you create, resume or restart a Sandbox you can access its `bootupType`. This value indicates how the Sandbox was started.

**FORK**: The Sandbox was created from a template. This happens when you call `create` successfully.\
**RUNNING**: The Sandbox was already running. This happens when you call `resume` and the Sandbox was already running.\
**RESUME**: The Sandbox was resumed from hibernation. This happens when you call `resume` and the Sandbox was hibernated.\
**CLEAN**: The Sandbox was created or resumed from scratch. This happens when you call `create` or `resume` and the Sandbox was not running and was missing a snapshot. This can happen if the Sandbox was shut down, restarted, the snapshot was expired (old snapshot) or if something went wrong.

## Managing CLEAN bootups

Whenever we boot a sandbox from scratch, we'll:

1. Start the Firecracker VM
2. Create a default user (called pitcher-host)
3. (optional) Build the Docker image specified in the .devcontainer/devcontainer.json file
4. Start the Docker container
5. Mount the /project/sandbox directory as a volume inside the Docker container

You will be able to connect to the Sandbox during this process and track its progress.

```javascript JavaScript theme={null}
const sandbox = await sdk.sandboxes.create()
 
const setupSteps = sandbox.setup.getSteps()
 
for (const step of setupSteps) {
  console.log(`Step: ${step.name}`);
  console.log(`Command: ${step.command}`);
  console.log(`Status: ${step.status}`);
 
  const output = await step.open()
 
  output.onOutput((output) => {
    console.log(output)
  })
 
  await step.waitUntilComplete()
}
```

<br />

## Using templates

Code Sandbox has default templates that you can use to create sandboxes. These templates are available in the Template Library and by default we use the "Universal" template. To create your own template you will need to use our CLI.

## Creating the template

Create a new folder in your project and add the files you want to have available inside your Sandbox. For example set up a Vite project:

```text Text theme={null}
npx create-vite@latest my-template
```

Now we need to configure the template with tasks so that it will install dependencies and start the dev server. Create a my-template/.codesandbox/tasks.json file with the following content:

```json JSON theme={null}
{  
    "setupTasks": [  
        "npm install"  
    ],  
    "tasks": {  
        "dev-server": {  
            "name": "Dev Server",  
            "command": "npm run dev",  
            "runAtStart": true  
        }  
    }  
}
```

The `setupTasks` will run after the Sandbox has started, before any other tasks.

Now we are ready to deploy the template to our clusters, run:

```text Text theme={null}
$ CSB_API_KEY=your-api-key npx @codesandbox/sdk build ./my-template --ports 5173
```

<br />

<Tip>
  ### Note

  The template will by default be built with Micro VM Tier unless you pass --vmTier to the build command.
</Tip>

This will start the process of creating Sandboxes for each of our clusters, write files, restart, wait for port 5173 to be available and then hibernate. This generates the snapshot that allows you to quickly create Sandboxes already running a dev server from the template.

When all clusters are updated successfully you will get a "Template Tag" back which you can use when you create your sandboxes.

```javascript JavaScript theme={null}
const sandbox = await sdk.sandboxes.create({  
    source: 'template',  
    id: 'some-template-tag'  
})
```

<br />

## Connecting Sandboxes in the browser

In addition to running your Sandbox in the server, you can also connect it to the browser. This requires some collaboration with the server.

```javascript JavaScript theme={null}
app.post('/api/sandboxes', async (req, res) => {
  const sandbox = await sdk.sandboxes.create();
  const session = await sandbox.createBrowserSession({
    // Create isolated sessions by using a unique reference to the user
    id: req.session.username,
  });
 
  res.json(session)
})
 
app.get('/api/sandboxes/:sandboxId', async (req, res) => {
  const sandbox = await sdk.sandboxes.resume(req.params.sandboxId);
  const session = await sandbox.createBrowserSession({
    // Resume any existing session by using the same user reference
    id: req.session.username,
  });
 
  res.json(session)
})
```

Then in the browser:

```javascript JavaScript theme={null}
import { connectToSandbox } from '@codesandbox/sdk/browser';
 
const sandbox = await connectToSandbox({
  // The session object you either passed on page load or fetched from the server
  session: initialSessionFromServer,
  // When reconnecting to the sandbox, fetch the session from the server
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`)
});
 
await sandbox.fs.writeTextFile('test.txt', 'Hello World');
```

The browser session automatically manages the connection and will reconnect if the connection is lost. This is controlled by an option called `onFocusChange` and by default it will reconnect when the page is visible.

```javascript JavaScript theme={null}
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
  onFocusChange: (notify) => {
    const onVisibilityChange = () => {
      notify(document.visibilityState === 'visible');
    }
 
    document.addEventListener('visibilitychange', onVisibilityChange);
 
    return () => {
      document.removeEventListener('visibilitychange', onVisibilityChange);
    }
  }
});
```

If you tell the browser session when it is in focus it will automatically reconnect when hibernated. Unless you explicitly disconnect the session.

While the `connectToSandbox` promise is resolving you can also listen to initialization events to show a loading state:

```javascript JavaScript theme={null}
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
  onInitCb: (event) => {}
});
```

## Disconnecting the Sandbox

Disconnecting the session will end the session and automatically hibernate the sandbox after a timeout. You can also hibernate the sandbox explicitly from the server.

```javascript JavaScript theme={null}
import { connectToSandbox } from '@codesandbox/sdk/browser'
 
const sandbox = await connectToSandbox({
  session: initialSessionFromServer,
  getSession: (id) => fetchJson(`/api/sandboxes/${id}`),
})
 
// Disconnect returns a promise that resolves when the session is disconnected
sandbox.disconnect();
 
// Optionally hibernate the sandbox explicitly by creating an endpoint on your server
fetch('/api/sandboxes/' + sandbox.id + '/hibernate', {
  method: 'POST'
})
 
// You can reconnect explicitly from the browser by
sandbox.reconnect()
```

<br />

## Pricing

The self-serve option for running Code Sandbox is priced according to the CodeSandbox SDK plans, which follow two main pricing components:

VM credits: Credits serve as the unit of measurement for VM runtime. One credit equates to a specific amount of resources used per hour, depending on the specs of the VM you are using. VM credits follow a pay-as-you-go approach and are priced at \$0.01486 per credit. Learn more about credits here.

VM concurrency: This defines the maximum number of VMs you can run simultaneously with the SDK. As explored below, each CodeSandbox plan has a different VM concurrency limit.

<Tip>
  ### Note

  We use minutes as the smallest unit of measurement for VM credits. E.g.: if a VM runs for 3 minutes and 25 seconds, we bill the equivalent of 4 minutes of VM runtime.
</Tip>

<br />

## VM credit prices by VM size

Below is a summary of how many VM credits are used per hour of runtime in each of our available VM sizes. Note that, by default, we recommend using the Nano VM size, as it should provide enough resources for most simple workflows (Pico is mostly suitable for very simple code execution jobs).

| VM size | Credits / hour | Cost / hour | CPU      | RAM    |
| :------ | :------------- | :---------- | :------- | :----- |
| Pico    | 5 credits      | \$0.0743    | 2 cores  | 1 GB   |
| Nano    | 10 credits     | \$0.1486    | 2 cores  | 4 GB   |
| Micro   | 20 credits     | \$0.2972    | 4 cores  | 8 GB   |
| Small   | 40 credits     | \$0.5944    | 8 cores  | 16 GB  |
| Medium  | 80 credits     | \$1.1888    | 16 cores | 32 GB  |
| Large   | 160 credits    | \$2.3776    | 32 cores | 64 GB  |
| XLarge  | 320 credits    | \$4.7552    | 64 cores | 128 GB |

<br />

### Concurrent VMs

To pick the most suitable plan for your use case, consider how many concurrent VMs you require and pick the corresponding plan:

* Build (free) plan: 10 concurrent VMs
* Scale plan: 250 concurrent VMs
* Enterprise plan: custom concurrent VMs

In case you expect a high volume of VM runtime, our Enterprise plan also provides special discounts on VM credits.

<Tip>
  ### For enterprise

  Please [contact Sales](https://www.together.ai/contact-sales)
</Tip>

### Estimating your bill

To estimate your bill, you must consider:

* The base price of your CodeSandbox plan.
* The number of included VM credits on that plan.
* How many VM credits you expect to require.

As an example, let's say you are planning to run 80 concurrent VMs on average, each running 3 hours per day, every day, on the Nano VM size. Here's the breakdown:

* You will need a Scale plan (which allows up to 100 concurrent VMs).
* You will use a total of 72,000 VM credits per month (80 VMs x 3 hours/day x 30 days x 10 credits/hour).
* Your Scale plan includes 1100 free VM credits each month, so you will purchase 70,900 VM credits (72,000 - 1100).

Based on this, your expected bill for that month is:

* Base price of Scale plan: \$170
* Total price of VM credits: $1053.57 (70,900 VM credits * $0.01486/credit)
* Total bill: \$1223.57

<br />

## Further reading

Learn more about Sandbox configurations and features on the [CodeSandbox SDK documentation page](https://codesandbox.io/docs/sdk/manage-sandboxes)
