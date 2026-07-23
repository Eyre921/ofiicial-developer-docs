---
title: "Run an A/B test"
source: https://docs.together.ai/docs/dedicated-endpoints/ab-tests
path: docs/dedicated-endpoints/ab-tests
---

Compare a candidate deployment against a baseline on live traffic.

Use A/B tests to split live traffic between a baseline deployment (the **control**) and one or more candidates (the **variants**) under a single endpoint, so you can compare them on real requests.

<Frame>
  <img alt="Per-request cohort assignment. Requests flow through the endpoint router, which assigns each one to a cohort: about 95 percent go to the control and about 5 percent to the variant." />
</Frame>

An A/B test doesn't shift the endpoint fully onto the new deployment. It maintains a fixed split, allowing you to measure how a new deployment performs before you promote it.

## How it works

A/B tests compare two or more deployments on live traffic.

While the A/B test is active, it subdivides the control's share of traffic among the control and its variants. Requests that would route to the control are re-sampled across the test members by the percentages you set; the rest of the endpoint's [traffic split](/docs/dedicated-endpoints/route-traffic) is unaffected.

<Warning>
  Test variants must be excluded from the endpoint's traffic split (weight `0` or unset); only the control belongs in the split. A variant that has a non-zero traffic-split weight causes the test to fail to start.
</Warning>

An A/B test needs exactly one control and at least one variant, up to 19 variants (20 members total). Each member, including the control, is assigned a percentage of the control's traffic, and the percentages must sum to 100. Because the test only subdivides traffic destined for the control, a control with `weight: 0` (or one that's absent from the traffic split) means the test receives no traffic at all.

<Frame>
  <img alt="An A/B experiment cohort split. The endpoint router splits requests destined for the control between the control (95 percent, in the base traffic split) and the variant (5 percent, not in the base traffic split)." />
</Frame>

Deleting an A/B test ends the variant/control split immediately, returning all traffic to the control.

## Requirements

You need a `READY` control deployment that is [receiving traffic](/docs/dedicated-endpoints/route-traffic), plus a model to test as the variant. The CLI's `ab` command creates the variant deployment for you. See [Create a deployment](/docs/dedicated-endpoints/manage#create-a-deployment) if you don't have a control yet.

The examples below use these example IDs, which you should replace with your own:

* Endpoint: `ep_abc123`.
* Control deployment: `dep_control123`.
* Variant model: `ml_CbJNwQC2ZqCU2iFT3mrCh`.
* Second variant model: `ml_Zk7pR2mQ9sT4vU6yB1nD3`.

## Create an A/B test

<Tabs>
  <Tab title="CLI">
    <Steps>
      <Step title="Route traffic to the control">
        Attach the control (and only the control) to the endpoint's traffic split. Pass the control's deployment ID—the CLI resolves its parent endpoint and preserves the other deployments' weights. For a single deployment, any non-zero weight routes all traffic to it:

        ```bash CLI theme={null}
        tg beta endpoints update dep_control123 --traffic-weight 1
        ```
      </Step>

      <Step title="Start the test">
        The CLI's `ab` command creates the variant deployment for the model you pass and starts the experiment, assigning `--percent` to the variant and the remainder to the control. Start the variant small, for example 5% (the CLI assigns the remaining 95% to the control). Percents must be integers in `[1, 100]`.

        ```bash CLI theme={null}
        tg beta endpoints ab ml_CbJNwQC2ZqCU2iFT3mrCh \
          --control dep_control123 \
          --percent 5 \
          --name sampling-tweak-v1
        ```

        Note the experiment ID (`abx_...`) and the variant's deployment ID (`dep_...`) from the response. You use the experiment ID to adjust or delete the test, and the variant's deployment ID to ramp or promote it.
      </Step>

      <Step title="Send requests">
        [Send requests](/docs/dedicated-endpoints/requests) to the endpoint, using the endpoint string as the `model` field.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Console">
    The console doesn't create the variant deployment for you, so first add it to the endpoint at traffic weight `0` (see [Create a deployment](/docs/dedicated-endpoints/manage#create-a-deployment)). The endpoint then has a control in the traffic split and at least one variant at weight `0`.

    <Steps>
      <Step title="Open the A/B test form">
        On the endpoint, select the **Traffic Tests** tab, then **New A/B test**. The console blocks the form until the endpoint has at least two deployments with one at traffic weight `0`.
      </Step>

      <Step title="Name the test">
        Enter a **Name** and an optional **Description**.
      </Step>

      <Step title="Set the control and variants">
        Confirm the **Control** deployment and select each **Variant** deployment, then set each member's traffic percentage. The percentages divide the control's share of traffic and must sum to 100.
      </Step>

      <Step title="Start the test">
        Select **Start A/B test**.
      </Step>
    </Steps>

    <Frame>
      <img alt="The Start an A/B test dialog in the Together AI console, with a name field, a traffic-split bar, and Control and Variants sections that each pair a deployment with a traffic percentage." />
    </Frame>

    The test appears in the **A/B tests** table on the Traffic Tests tab, where you can edit or stop it.

    <Frame>
      <img alt="The Traffic Tests tab in the Together AI console showing an A/B test row with its name, variant count, traffic split, and creation time." />
    </Frame>
  </Tab>
</Tabs>

## Ramp the variant

To change an existing member's share, update the experiment's members from the SDK or API. The CLI's `ab` command can start an experiment and add variants to it, but it can't change a member's percentage, so ramping is an SDK or API operation. Updating `members` replaces the whole set and re-validates the shape, so resend every member each time. In the console, open the test's actions menu on the **Traffic Tests** tab and select **Edit A/B test** to change member percentages.

<Frame>
  <img alt="Ramping the variant. In week 1 the split is 95 percent control and 5 percent variant. A single update to the member set is atomic and ETag-guarded. In week 2 the split is 80 percent control and 20 percent variant." />
</Frame>

To move to a 90% control / 10% variant split:

```python Python theme={null}
from together import Together

client = Together()
project_id = client.whoami().project_id

client.beta.endpoints.ab_experiments.update(
    "abx_abc123",
    endpoint_id="ep_abc123",
    project_id=project_id,
    members=[
        {
            "deployment_id": "dep_control123",
            "role": "AB_EXPERIMENT_MEMBER_ROLE_CONTROL",
            "percent": 90,
        },
        {
            "deployment_id": "dep_variant456",
            "role": "AB_EXPERIMENT_MEMBER_ROLE_VARIANT",
            "percent": 10,
        },
    ],
)
```

## Add more variants

You can compare more than one candidate at once. Run `ab` again with the same control and a different variant model. The CLI creates the new variant deployment, finds the existing experiment for that control, and adds the deployment to it as another variant.

<Frame>
  <img alt="A multi-way A/B experiment with one control and several variants. The control takes 70 percent and three variants take 10 percent each. An experiment can have up to 20 members, with exactly one control, and the percentages must sum to 100." />
</Frame>

Each `ab` call carves the new variant's percentage out of the control's share and leaves the existing variants untouched. Continuing from the 90% / 10% split above, adding a second variant at 10% gives 80% control / 10% / 10%:

```bash CLI theme={null}
tg beta endpoints ab ml_Zk7pR2mQ9sT4vU6yB1nD3 \
  --control dep_control123 \
  --percent 10
```

An experiment allows up to 20 members with exactly one control, and the control's share can't drop below 1%.

## Promote a variant

When you've picked a winner, promote it by [updating the endpoint's traffic split](/docs/dedicated-endpoints/route-traffic) so the winning deployment serves all traffic. Set the winner's weight to a non-zero value and set the other deployments to `0` (or delete them):

```bash CLI theme={null}
tg beta endpoints update dep_control123 --traffic-weight 0
tg beta endpoints update dep_variant456 --traffic-weight 1
```

Then [delete the test](#delete-the-test) to end the managed control/variant split.

## Delete the test

Deleting an A/B test ends the variant/control split immediately. All traffic returns to the endpoint's regular traffic split, either the control, or the variant you [promoted](#promote-a-variant).

The CLI's smart-delete `rm` accepts the experiment ID:

```bash CLI theme={null}
tg beta endpoints rm abx_abc123
```

In the console, open the test's actions menu on the **Traffic Tests** tab and select **Stop A/B test**.

To clean up the member deployments, follow the teardown order in [Manage deployments](/docs/dedicated-endpoints/manage#delete-resources) for each deployment.

## Next steps

<CardGroup>
  <Card title="Create a deployment" icon="layers-intersect" href="/docs/dedicated-endpoints/manage#create-a-deployment">
    Create control and variant deployments for an A/B test.
  </Card>

  <Card title="Split traffic" icon="arrows-split" href="/docs/dedicated-endpoints/split-traffic">
    Promote a winning variant by updating the endpoint's traffic split.
  </Card>

  <Card title="Observability" icon="chart-line" href="/docs/dedicated-endpoints/monitoring">
    Compare control and variant deployments with per-deployment metrics.
  </Card>

  <Card title="Route traffic" icon="route" href="/docs/dedicated-endpoints/route-traffic">
    Understand how traffic is routed across deployments under an endpoint.
  </Card>
</CardGroup>
