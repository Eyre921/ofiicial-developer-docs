---
title: "Plans and Accounts"
source: https://docs.fireworks.ai/nexus/plans
path: nexus/plans
---

Compare the Nexus Pro, Team, and Enterprise plans, and see how a Nexus account at nexus.fireworks.ai relates to your Fireworks platform account.

Nexus has its own accounts and plans at [nexus.fireworks.ai](https://nexus.fireworks.ai). Choose a plan when you sign up, and change it later from **Plans** in the app.

## Compare plans

<table>
  <thead>
    <tr>
      <th />

      <th>Pro</th>
      <th>Team</th>
      <th>Enterprise</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Best for**</td>
      <td>One person</td>
      <td>A team that shares billing</td>
      <td>Companies that need admin controls</td>
    </tr>

    <tr>
      <td>**Price**</td>
      <td>\$8 per month</td>
      <td>\$10 per seat per month</td>
      <td>Usage-based. [Contact sales](https://fireworks.ai/contact)</td>
    </tr>

    <tr>
      <td>**Seats**</td>
      <td>1</td>
      <td>Up to 200. Admins buy seats and invite members</td>
      <td>Unlimited</td>
    </tr>

    <tr>
      <td>**Usage**</td>
      <td>Included usage, reset on a rolling window and monthly</td>
      <td>More included usage per seat than Pro</td>
      <td>Pay for what you use</td>
    </tr>

    <tr>
      <td>**Models**</td>
      <td>[Nexus Auto](/nexus/auto) and your own Claude and ChatGPT models</td>
      <td>Same as Pro</td>
      <td>Same as Team, plus [open models](/nexus/open-models) on Fireworks serverless</td>
    </tr>

    <tr>
      <td>**Data**</td>
      <td>[Zero Data Retention](/nexus/data-security) across all plans</td>
    </tr>

    <tr>
      <td>**Admin controls**</td>
      <td>[Model Providers](/nexus/provider-keys)</td>
      <td>Members, seats, and Model Providers</td>
      <td>[Enterprise Controls](/nexus/enterprise-controls), including Spend Limits, SSO, and SCIM</td>
    </tr>
  </tbody>
</table>

Current prices are on the [Plans page](https://nexus.fireworks.ai/plans).

* Every plan works with the same [harnesses](/nexus/harnesses) and the [Nexus CLI](/nexus/cli).
* On Pro and Team, Nexus Auto runs Anthropic and OpenAI models on your own account. Sign in to the harness with your Claude or ChatGPT subscription, save your keys with `nexus auto`, or connect a [Provider Key](/nexus/provider-keys).
* Pro and Team don't include general access to open models. Your model picker shows Nexus Auto (`auto`) next to your own Claude or ChatGPT models, and Nexus Auto still routes your requests to open models.
* Enterprise includes general access to the open models on Fireworks serverless, so you can choose one directly, such as `glm-latest`.
* Included usage counts turns that run on Fireworks. Anthropic and OpenAI turns bill to your own provider account.
* When a Pro or Team seat reaches its included usage, Fireworks turns pause until the window resets. For more usage, upgrade to Team or Enterprise.
* To move from Pro to Team, open **Plans**, choose **Team**, and confirm the change by email.

## Nexus and platform accounts are separate

Nexus and the Fireworks platform use separate accounts, sign-ins, and billing.

| | Nexus | Fireworks platform |
| - | - | - |
| **Web app** | [nexus.fireworks.ai](https://nexus.fireworks.ai) | [app.fireworks.ai](https://app.fireworks.ai) |
| **Use it for** | Connecting AI tools with Nexus CLI or Nexus Desktop | Serverless and dedicated inference, fine-tuning, and the Fireworks API |
| **API keys** | Created by `nexus login`, or under **Settings** in the Nexus app | Created in the platform console |

* You can have both accounts under the same email.
* Each site keeps its own sign-in, so you can be signed in to both at once.
* A platform API key does not carry a Nexus plan, and a Nexus key does not work for platform features such as deployments or fine-tuning.

If you use Nexus features on a platform account, [contact us](https://fireworks.ai/contact) for help moving to a Nexus account.
