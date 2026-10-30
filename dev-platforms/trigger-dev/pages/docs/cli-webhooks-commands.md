---
title: "CLI webhooks commands"
source: https://trigger.dev/docs/cli-webhooks-commands
path: docs/cli-webhooks-commands
---

Set or generate the signing secret of a hosted webhook endpoint from your terminal, without printing it.

**These commands store a [webhook endpoint's](/docs/webhooks/overview) signing secret without printing it, so the value stays out of your terminal history, logs and AI agent transcripts.** `endpoint` is the endpoint's declared id (the `id` passed to `webhooks.endpoint.define`) or its `wh_` id.

## Replacing an existing secret

When the endpoint already has a secret, both commands ask how long the old one keeps working, with the same choices as the dashboard: stop immediately, 1 hour, 24 hours (the default) or 7 days. In a script or an AI agent, where there's no prompt, pass `--previous-secret-ttl` instead; the command refuses to replace the secret without it, so a rotation can't cut the provider off by accident:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest webhooks set-secret stripe --env prod --from-env STRIPE_WEBHOOK_SECRET --previous-secret-ttl 24h
```

## webhooks set-secret

Stores the signing secret or public key a provider issued, such as the `whsec_` secret Stripe returns when you create a webhook endpoint. It replaces the endpoint's current secret.

Pipe the secret in from the provider's CLI or a file:

```bash npm theme={"theme":"css-variables"}
stripe webhook_endpoints create -d url="$WEBHOOK_URL" -d "enabled_events[]=checkout.session.completed" \
  | jq -r .secret \
  | npx trigger.dev@latest webhooks set-secret stripe --env prod
```

```bash pnpm theme={"theme":"css-variables"}
stripe webhook_endpoints create -d url="$WEBHOOK_URL" -d "enabled_events[]=checkout.session.completed" \
  | jq -r .secret \
  | pnpm dlx trigger.dev@latest webhooks set-secret stripe --env prod
```

```bash bun theme={"theme":"css-variables"}
stripe webhook_endpoints create -d url="$WEBHOOK_URL" -d "enabled_events[]=checkout.session.completed" \
  | jq -r .secret \
  | bunx trigger.dev@latest webhooks set-secret stripe --env prod
```

Or read it from an environment variable. Without `--from-file`, the command checks the shell environment, then the project's `.env`, `.env.development`, `.env.local` and `.env.development.local` files:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest webhooks set-secret stripe --env prod --from-env STRIPE_WEBHOOK_SECRET
```

Run it in a terminal without either option and it asks for the secret with a masked prompt.

**From env** `--from-env`

Read the secret from this environment variable.

**From file** `--from-file`

With `--from-env`, read the variable from this `.env` file only.

**Previous secret TTL** `--previous-secret-ttl`

When the endpoint already has a secret, how long the old one keeps working while the provider switches to the new one: seconds (`3600`) or a duration (`1h`, `24h`, `7d`), at most 7 days. `0` stops it straight away, for a secret that leaked.

## webhooks generate-secret

Generates a new signing secret, for providers that accept a secret you choose, such as GitHub. It replaces the endpoint's current secret.

Save it to an env file, then hand it to the provider by variable name:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest webhooks generate-secret github --env prod --to-env GITHUB_WEBHOOK_SECRET
```

The command writes `GITHUB_WEBHOOK_SECRET` to `.env.local`, creating the file if needed, and prints only where it saved the value. Or pipe it straight into the provider's CLI with `--print`, which outputs the secret and nothing else.

When the output isn't a terminal, the command refuses to print the secret unless you pass `--to-env` or `--print`, so an AI agent running it doesn't capture the value by accident.

**To env** `--to-env`

Save the secret as this variable in an env file.

**To file** `--to-file`

With `--to-env`, the file to save to. Defaults to `.env.local`.

**Print** `--print`

Print only the secret, for piping it into another command.

**Previous secret TTL** `--previous-secret-ttl`

When the endpoint already has a secret, how long the old one keeps working while the provider switches to the new one: seconds (`3600`) or a duration (`1h`, `24h`, `7d`), at most 7 days. `0` stops it straight away, for a secret that leaked.

## Options

**Environment** `--env | -e`

The environment to use: `dev`, `prod`, `staging` or `preview`. Defaults to `prod`.

**Config file** `--config | -c`

The name of the config file found at the project path. Defaults to `trigger.config.ts`

**Project ref** `--project-ref | -p`

The project ref. Required if there is no config file.

**Branch** `--branch | -b`

The branch to use. Required with `--env preview`.

### Common options

These options are available on most commands.

**Login profile** `--profile`

The login profile to use. Defaults to the current profile, which is set by your last `login` or `switch` (initially "default").

**API URL** `--api-url | -a`

Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.

**Log level** `--log-level | -l`

The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.

**Skip telemetry** `--skip-telemetry`

Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.

**Help** `--help | -h`

Shows the help information for the command.

**Version** `--version | -v`

Displays the version number of the CLI.
