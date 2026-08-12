---
title: "Netlify Secrets Controller"
source: https://docs.netlify.com/build/environment-variables/secrets-controller.md
path: build/environment-variables/secrets-controller
---

---
title: "Enhanced security with Secrets Controller"
description: "With environment variable secrets, you restrict the access to sensitive data and automatically enable layers of extra protection. Learn how environment variable secrets improve your site's security posture."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

With Secrets Controller, your team can protect and manage environment variable values that require additional layers of security. Flag which environment variables are secrets, and Netlify will apply stricter requirements to them. While Netlify handles all environment variables securely, including encrypted storage, Secrets Controller protects environment variable secrets with an opinionated policy and additional security features.

This page outlines the environment variable [secrets policy](#environment-variable-secrets-policy), how to [manage](#manage-secret-values) environment variable secrets on Netlify, and how [secret scanning](#secret-scanning-overview) proactively finds embedded secrets before they're exposed.

## Environment variable secrets policy

Not all environment variables are created equal. Environment variable secrets are sensitive values that would have a detrimental impact on your organization or end users if they were accessed by the wrong party. When you flag environment variables as secret, Netlify's opinionated policy enforces how these values are accessed and which scopes and features you can use with them.

This policy's design removes options that could allow your team to inadvertently expose secrets and drives your team to be explicit about where secret values should be accessible.

Environment variable secrets have the following policy applied to them:

- Secret values are write-only. After setting a value using the UI, CLI, or API, you will no longer have access to a human-readable version of the value.
- Secret values must be set to explicit [deploy contexts](/build/environment-variables/overview#value-per-deploy-context) and [scopes](/build/environment-variables/overview#scopes) to avoid unexpected exposure.
- After an environment variable is flagged as a secret, you cannot remove the flag to reveal the secret's value.
- Environment variable secrets cannot have the `post processing` [scope](/build/environment-variables/overview#scopes) to avoid inadvertently exposing the value through features like [snippet injection](/build/post-processing/snippet-injection/).
- Only code running on Netlify's systems can read the original, unmasked values. Your code running on edge functions, serverless functions, build process, etc. will have the original unmasked values of the environment variables. Code running **outside** of Netlify's hosted systems will have masked versions of the environment variable values.
- A value set in the environment variable's `dev` [deploy context](/build/environment-variables/overview#value-per-deploy-context) will **not** have this policy applied to it. As such, only the value for the `dev` deploy context will be unmasked from the UI, CLI, and API. This will allow developers to continue developing with non-secret values that are explicitly for development.

None of these policy enforcements can be changed or customized using any form of configuration.

### Note - Values are masked except in dev context

Our UI, CLI, and API won't return unmasked values of environment variable secrets for any [deploy context](/build/environment-variables/overview#value-per-deploy-context) besides `dev`. Using the CLI to do a production build with `netlify build` won't include the raw, unmasked values. Per the policy, only code running on our systems have access to the unmasked value.

## Manage secret values

Environment variables that are marked as secret use the same underlying systems for configuring and managing values as other environment variables do. As such, you can use the same flows for [creating](/build/environment-variables/get-started/#create-environment-variables) and [modifying](/build/environment-variables/get-started/#modify-and-delete-environment-variables) environment variables. During those flows you can flag variables as secret if the values contain secrets.

### Configure environment variable secrets

Environment variables are configured through Netlify's UI, CLI, or API. For each method, you can specify values as secrets:

- In the Netlify UI, create and modify variables under 
### NavigationPath Component:

Project configuration > Environment variables
 or under 
### NavigationPath Component:

Team settings > Environment variables
. For new or existing variables, select `Contains secret values` to flag that an environment variable contains a secret.

  ![](/images/environment-variables-contains-secret-values.png)

  - If importing from an `.env` file in the Netlify UI, import all variables first, then select 
### NavigationPath Component:

Options > Edit
 and select `Contains secret values` to flag specific environment variables as secrets.

- With the Netlify CLI, use `env:set` with the `--secret` flag to create or modify a site environment variable to be an environment variable secret. Review our [Get Started with Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli#manage-environment-variables) guide to learn more.
- With the Netlify API, use [`createEnvVars`](https://open-api.netlify.com/#tag/environmentVariables/operation/createEnvVars) and [`updateEnvVar`](https://open-api.netlify.com/#tag/environmentVariables/operation/updateEnvVar) to create or modify a site environment variable with the `is_secret` field set to `true`. Review our [Get Started with Netlify API](/api-and-cli-guides/api-guides/get-started-with-api#environment-variables) guide to learn more.

Environment variable secret values can be created and modified, but they're not human-readable from the UI, CLI, or API after they're flagged as secret. To avoid allowing access to secret values, once you flag an environment variable as a secret, this flag cannot be removed.

### Use secret values

Environment variable secrets are environment variables that have restricted access. Per the secrets policy, only code running on Netlify will receive the raw, unmasked values. Within your code, you [use environment variable secrets](/build/environment-variables/get-started/#use-environment-variables) the same way as you use traditional environment variables.

Only values that are configured for the `dev` [deploy context](/build/configure-builds/file-based-configuration#deploy-contexts) are human readable from the UI, CLI, and API. This allows developers to use development context environment variables locally. All other contexts have restricted access based on our [environment variables secrets policy](#environment-variable-secrets-policy).

## Secret scanning overview

When you explicitly mark which environment variables have secret values, Netlify proactively protects your team with secret scanning. This process scans your repository code and build output files for the existence of secret values. If the scanning process finds secret values, it fails the build and adds the location of the secret values to the deploy log. secret scanning happens before publish and deploy steps to ensure secret values aren't exposed publicly or stored in files that are downloadable by members of your Netlify team.

You can monitor the status of secret scanning across your project's deploys in two places:
- On your project's overview page, where you'll find alerts if any secrets have been exposed in recent deploys
- In your deploys list, where each deploy will indicate if secrets were detected during the build process

It's easy to inadvertently add code that injects secrets into server and client code. When this happens, it can go undetected a long time after the initial leak. Secrets exposure can cost your company a lot of time, money, and customer trust. secret scanning is an essential security layer to protect your teams and end users.

### Tip - Do I need Netlify secret scanning if I'm scanning secrets on my repo?

We recommend using all security tools available to keep your team and users safe. While repository-specific secret scanning is a helpful tool for scanning secrets that your repository is aware of, there are secret values on Netlify that your code repo is unlikely to discover. For example, database passwords or server secret keys provided at runtime are unlikely to be in your code repository's list of secrets.

### Secret scanning process

secret scanning searches all files that are in your site's build, including code pulled from the repo and files generated during the build.

To reduce the chances of false positives, secret scanning only searches for environment variable secret values that have more than four characters and are not booleans.

In the common build steps that inject data into files or bundles, you don't always use the plaintext version of those values. Given this, Netlify's secret scanning will search for different permutations of values in the following formats:
- plaintext
- base64-encoded
- URI-encoded

In addition to the different encodings, any values that appear to be a multi-line string will also have their full value searched as a single line string and in multi-line form.

For example, with an environment variable secret such as `SECRET_ALPHABET="abc\ndef\nghi"` the scanner will find four matches in the following file.

```plaintext
abc\ndef\nghi <- plaintext

YWJjCmRlZgpnaGk= <- base64 encoded

abc%0Adef%0Aghi <- uri encoded

 abc
def
ghi <- the multi line value
```

### Configure secret scanning

When using environment variable secrets, secret scanning is enabled automatically. Netlify will begin scanning on the next build after an environment variable is marked as secret. You may configure how the scanning works by setting any of the following environment variables at the site or team level.

Set these environment variables to some or all deploy contexts to customize secret scanning for your site or team needs:

- **`SECRETS_SCAN_ENABLED`:** default is `true`. Set to `false` to entirely disable all secret scanning protections for the site/team, including both smart detection and scanning for environment variables marked as secrets. **Note:** Disabling this means you lose all protection for secrets defined in your environment variables.
- **`SECRETS_SCAN_OMIT_KEYS`:** default is _empty_. Set to a comma separated list of key names that should **not** be scanned for within this site or team.
- **`SECRETS_SCAN_OMIT_PATHS`:** default is _empty_. Set to a comma separated list of file paths (relative to the repository root) that should **not** be scanned within this site or team. Values can be substrings of paths or use a glob pattern format.

When you set the values at the team level, you may use site-specific environment variable values to override the team level settings. Review the environment variable [overrides](/build/environment-variables/overview#overrides) section to understand how to apply these settings to meet your team's needs.

## Secret scanning with smart detection

> **Pricing Information:** This feature is available on [Personal](https://www.netlify.com/pricing/?category=personal), [Pro](https://www.netlify.com/pricing/?category=developer), and [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

Smart detection automatically scans for potential secrets in your repository code and build output.

Unlike Netlify's standard secret scanning, smart detection doesn't require any manual configuration or environment variables.

When Netlify detects a potential secret, the following will happen:
- The build will automatically fail to prevent a secret exposure
- The deploy log will identify the location of the exposed secret for you to review

### Resolve a secret detection

If smart detection flags a secret value, we recommend you remove the value from your project based on the location shared in your deploy log and then redeploy your project.

To find the location of the exposed secret, check your deploy log at **Site dashboard > Deploys**.

After removing the secret value you should no longer see it detected in subsequent deploys.

### Manage false positives

If smart detection flags a string that is not a secret, you can add this string to a safelist to prevent smart detection from flagging the string as a secret value for your project again.

To add a false positive to a safelist:

1. For your project, go to **Project configuration > Environment variables** and choose **Add a variable** and then **Add a single variable**.

2. Give this variable the key name `SECRETS_SCAN_SMART_DETECTION_OMIT_VALUES`.

3. Add the strings you want to add to the safelist as the value of this variable, separated by commas for each false positive and then select **Create variable**.

4. To re-deploy your project, go to **Deploys** and choose **Trigger deploy > Deploy project**.

### Note

You can also manage environment variables through the Netlify CLI or API for automated workflows.

### Turn off smart detection

### Caution

Consider adding false positives to a safelist instead of turning off smart detection, to make sure your project continues to benefit from the enhanced protections.

To turn off smart detection:

1. For your project, go to **Project configuration > Environment variables**.

2. Under **Environment variables**, expand `SECRETS_SCAN_SMART_DETECTION_ENABLED` and use the **Options** menu to select **Edit**. Set the environment variable to `false` across all available scopes and confirm your changes.

**Note:** Setting `SECRETS_SCAN_SMART_DETECTION_ENABLED=false` only disables smart detection. Normal secret scanning will still run for environment variables you've explicitly marked as secrets. This allows you to continue protecting secrets defined in your environment variables while opting out of automatic smart detection. If you want to disable all secret scanning completely, set `SECRETS_SCAN_ENABLED=false` instead (though this means you lose protection for all secrets, including those defined in environment variables). 

## Enhancing the sensitive variable policy

Netlify provides all customers who are using public repositories the ability to keep sensitive variables private and away from untrusted deploys through the [sensitive variable policy](/build/environment-variables/get-started/#sensitive-variable-policy). This feature provides you with the ability to protect sensitive variables on sites that use **public** repositories. To provide the sensitive variable policy capabilities, Netlify attempts to detect sensitive values based on heuristics such as the key name and the shape of the value.

Secrets Controller is designed to offer advanced security around explicitly flagged secrets.

When using Secrets Controller with a public repository, the sensitive variable policy applies to these environment variables:
- any variables that Netlify automatically detects as sensitive, even if they are not specifically flagged with `Contains secret values`
- any variables explicitly flagged as sensitive by selecting `Contains secret values`

With the sensitive variable policy, you can choose how to manage access to sensitive values for deploys from your public repo. Explicitly marked secret values are included in this policy.

