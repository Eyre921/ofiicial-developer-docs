---
title: "Multi-Step Workloads"
source: https://docs.netlify.com/build/async-workloads/multi-step-workloads.md
path: build/async-workloads/multi-step-workloads
---

---
title: "Multi-step Async Workloads"
description: "Break up tasks into discrete steps that can run independently, handle failures, and retry automatically, ensuring efficient and durable execution."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

When using event-driven architectures, it's common to break up the code into discrete steps so that those steps can run, fail, and retry on their own. While there are many patterns to solve this, Async Workloads has a built-in method of doing multi-step processes that allows developers to code workflows together without having to create separate workloads.

To build these multi-step workloads, the `AsyncWorkloadEvent` provides a `step` field that includes methods for creating steps. The primary method for defining step functions is `step.run(id, callback)`.

```ts
import { asyncWorkloadFn, AsyncWorkloadEvent } from "@netlify/async-workloads";

export default asyncWorkloadFn(async ({step}: AsyncWorkloadEvent) => {

	const results = await step.run('step-id', ()=>{

		// logic for this step goes here

		// optionally, return the step data used for later parts
		// of the workload.
		return {};
	});
});
```

All available methods for steps are documented on the [`AsyncWorkloadEvent` documentation](/build/async-workloads/writing-workloads#event-step).

## Steps in practice

To understand the application of this, compare the implementation of a common workflow with a workload implemented with a step function.

The common workflow is: sign up a user, add them to an external billing system, sync that billing information with the site database, and send a welcome email.

```ts
import { asyncWorkloadFn, AsyncWorkloadConfig } from "@netlify/async-workloads";

export default asyncWorkloadFn(async (event) => {

	const { accountId } = await doSignup(event.eventData);

	const { billingSystemId } = await setupBilling(accountId);

	const user = await updateUser({billingSystemId});

	await sendEmail(user);

});

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
	events: ['account.signup'],
};
```

With this workload, `doSignup`, `setupBilling` , `updateUser` , and `sendEmail` functions	 could all run into transient issues - network outages, APIs are unavailable, etc. This could be attempted with error catching and in-code retrying, but if the issues take a very long time to resolve (that's relative - a long time could mean 30 seconds, 3 days, etc.), then the options become much more limited or expensive to keep functions running indefinitely until issues resolve. In addition to handling failures, if something breaks, the workload will retry completely regardless of any work that was already successful. Given that workloads should aim to be idempotent, this shouldn't be a major deal but it will consume resources and time for all involved systems.

This is the same workload implemented using step functions.

```ts
import { asyncWorkloadFn, AsyncWorkloadConfig, AsyncWorkloadEvent } from "@netlify/async-workloads";

export default asyncWorkloadFn(async ({eventData, step}: AsyncWorkloadEvent) => {

	const { accountId } = await step.run('signup-user', ()=>{
		return doSignup(eventData);
	});

	const { billingSystemId } = await step.run('add-to-billing', ()=>{
		return setupBilling(accountId);
	});

	const user = await step.run('sync-user-billing', ()=>{
		return updateUser({billingSystemId});
	});

	await sendEmail(user);

});

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
	events: ['account.signup'],
};
```

This implementation is very similar to the original implementation. With steps, workloads can define the full scope of work that's needed but the durable execution will automatically retry these workloads. The steps will ensure only work that has not completed yet will run until it gets to the end.

This workload function runs until it hits a step that it has not completed before or until the workload completes. After running a step function for the first time, the workload will be reinvoked. All previous steps will resolve their previous results without having to run the function again.

This means that this workload will have 4 invocations to get to completion. The first invocation will run until it hits the `signup-user` step and will run that callback. Once completed, the full workload is invoked again. This next invocation will already have the results of `signup-user`, so it will resolve that result without running the step function and will continue the workload until it hits the `add-to-billing` step. It does this same process of running and invoking itself again as it accumulates the results of all step functions.

If any steps fail, the workload will be retried but all steps that were completed before that failure will persist their respective results. So, if `sendEmail()` fails (the very last step in the workload), the workload will be retried according to the retry schedule but all of the step functions before it will not be invoked again.

## Sleeping

In addition to breaking up logic into discrete, isolated steps, Async Workloads provides the ability for workloads to "sleep" mid-execution and continue after that minimum duration has passed. This allows developers to represent full workflows, including their relationship to time within the workload.

To update the above example to have a 24-hour waiting period before sending the welcome email, add a `step.sleep(id, duration)`:

```ts
import { asyncWorkloadFn, AsyncWorkloadConfig, AsyncWorkloadEvent } from "@netlify/async-workloads";

export default asyncWorkloadFn(async ({eventData, step}) => {

	const { accountId } = await step.run('signup-user', ()=>{
		return doSignup(eventData);
	});

	const { billingSystemId } = await step.run('add-to-billing', ()=>{
		return setupBilling(accountId);
	});

	const user = await step.run('sync-user-billing', ()=>{
		return updateUser({billingSystemId});
	});

	await step.sleep('24h-delay-for-email', '1 day');

	await sendEmail(user);
});

export const asyncWorkloadConfig: AsyncWorkloadConfig = {
	events: ['account.signup'],
};
```

## Parallelized and nested steps

Steps can also be triggered in parallel. In the standard step lifecycle, the workload will restart after a step is invoked, but if two or more steps start at the same time, it will let them complete before continuing and re-invoking the workload. Running steps in parallel allows you to start the steps once and just await their results. This can be done with loops or other collections as well.

```js
import { asyncWorkloadFn } from "@netlify/async-workloads";

export default asyncWorkloadFn(async ({step}) => {

	const step1Result = step.run('step1', ()=>{
		return { foo: '1' };
	});

	const step2Result = step.run('step2', ()=>{
		return { bar: '2' };
	});

	const parallelResults = await Promise.all([step1Result, step2Result]);

	await step.run('log-results', ()=>{
		console.log(parallelResults);
		// outputs [{foo: '1'}, {bar: '2'}]
	});

});
```

Nesting steps works the same. The step lifecycle will not trigger re-invocation unless the all steps are complete.

```js
import { asyncWorkloadFn } from "@netlify/async-workloads";

export default asyncWorkloadFn(async ({step}) => {

	const step1Result = step.run('step1', ()=>{

		const step3Result = step.run('step3', ()=>{
			return { baz: '3' };
		});

		return { foo: '1', step3Result };
	});

	const step2Result = step.run('step2', ()=>{
		return { bar: '2' };
	});

	const results = await Promise.all([step1Result, step2Result]);

	await step.run('log-results', ()=>{
		console.log(results);
		// outputs [{foo: '1', step3Result: {baz: '3'}}, {bar: '2'}]
	});
});
```

## Step invocation lifecycle

It's important to understand that after each new step function that has not run yet, the complete workload is reinvoked. This will give each step a clean slate and as much time within the serverless runtime. This also means anything outside of a step function can be called multiple times for each step method. If you expect a process to run only once within a workflow, put the process inside of a step.

To examine how logic outside of steps and logic inside of steps will run when executing a multi-step workload, review the following example.

```js
import { asyncWorkloadFn} from "@netlify/async-workloads";

export default asyncWorkloadFn(async ({step}) => {

	console.log('outside logic A');

	await step.run('step1', ()=>{
		console.log('inside of step 1');
	});

	console.log('outside logic B');

	await step.run('step2', ()=>{
		console.log('inside of step 2');
	});

	await step.run('step3', ()=>{
		console.log('inside of step 3');
	});
});
```

This workload will have the following log pattern:

```plaintext
outside logic A
inside of step 1
outside logic A
outside logic B
inside of step 2
outside logic A
outside logic B
inside of step 3
outside logic A
outside logic B
```

This example demonstrates that the workload starts the function again each time but only runs the functions that it has not hit yet. It will re-invoke the workload after a new step method. Everything not inside of a step will be re-run. This is why it's important to ensure everything outside of a step is ok to run again.

The `step.sleep` method works the same.

```js
import { asyncWorkloadFn } from "@netlify/async-workloads";

export default asyncWorkloadFn(async ({step}) => {

	console.log('A');

	await step.sleep('first-wait', '1 hour');

	console.log('B');

	await step.sleep('second-wait', '2 hours');

	console.log('C');
});
```

After 3 hours, this workload will have the following log pattern:

```plaintext
A
A
B
A
B
C
```

