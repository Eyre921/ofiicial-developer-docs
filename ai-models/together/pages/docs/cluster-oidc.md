---
title: "Set up OIDC authentication"
source: https://docs.together.ai/docs/cluster-oidc
path: docs/cluster-oidc
---

Authenticate team members to a GPU cluster's Kubernetes API using your organization's identity provider.

External OpenID Connect (OIDC) lets each team member authenticate to a GPU cluster's Kubernetes API using their own identity from your organization's identity provider (IdP), such as Google, Okta, Auth0, or Microsoft Entra ID. Access is then controlled with standard Kubernetes role-based access control (RBAC).

<Tip>
  Use OIDC when you want per-user audit trails, per-user revocation, and least-privilege access via RBAC. You may not need this if you're the only operator or you never interact with the Kubernetes API directly.
</Tip>

## How it works

Kubernetes' API server can validate JSON Web Tokens (JWTs) issued by an external OIDC provider. When a user runs `kubectl`, the OIDC kubeconfig calls a local helper that handles login interactively, then attaches the resulting token to every API request.

<Accordion title="OIDC flow">
  The flow has four stages: **login**, **token**, **validate**, and **authorize**.

  <Steps>
    <Step title="Login">
      The user runs a `kubectl` command. `kubectl` sees the exec plugin in the OIDC kubeconfig and invokes `kubectl-together_login`. The plugin opens the user's default browser and redirects to the IdP's authorization endpoint with a PKCE challenge. The user signs in to the IdP with their organization credentials.
    </Step>

    <Step title="Token">
      The IdP issues a signed ID token (a JWT) and redirects back to `http://localhost:8000` or `:18000`, where the plugin is listening. The plugin caches the token under `$HOME/.kube/cache/oidc-login/` and returns it to `kubectl`.
    </Step>

    <Step title="Validate">
      `kubectl` sends the API request with the token in the `Authorization: Bearer …` header. The Kubernetes API server validates the token by fetching the IdP's public signing keys from its OIDC discovery document (`<issuer-url>/.well-known/openid-configuration`), verifying the token's signature, and checking that the `iss` and `aud` claims match the issuer URL and client ID configured on the cluster. A failure here returns `401 Unauthorized`.
    </Step>

    <Step title="Authorize">
      The API server reads the configured username claim (`email`, `preferred_username`, or `sub`) and uses it as the user identity for RBAC. It evaluates ClusterRoleBindings and RoleBindings to decide whether the request is allowed. No matching binding returns `403 Forbidden`.
    </Step>
  </Steps>

  ```mermaid theme={null}
  sequenceDiagram
      participant User as User (kubectl)
      participant Plugin as Login Plugin
      participant IdP as Your Identity Provider
      participant K8s as Kubernetes API Server

      User->>Plugin: kubectl get pods
      Plugin->>IdP: Opens browser for login
      IdP-->>Plugin: Returns signed JWT (ID token)
      Plugin-->>User: Passes token to kubectl
      User->>K8s: API request + Bearer token
      K8s->>K8s: Validates JWT signature, issuer, audience
      K8s->>K8s: Extracts username from token claims
      K8s->>K8s: Evaluates RBAC rules
      K8s-->>User: Response (or 403 if no RBAC match)
  ```
</Accordion>

## Username claim

The username claim is the field in the OIDC token that Kubernetes uses as the identity for RBAC. Supported values are `email`, `preferred_username`, or `sub`. Choose based on what your IdP reliably provides; `email` gives the simplest RBAC experience because the `--user` value is just the user's email address.

<Note>
  **The username claim affects the RBAC `--user` value.** The format Kubernetes uses for the identity depends on which claim you choose:

  * `email` produces `user@company.com`, used as-is.
  * `sub` produces `<issuer-url>#<sub-value>` (e.g., `https://accounts.google.com#105010678054620911233`).
  * `preferred_username` produces `<issuer-url>#<username>` (e.g., `https://login.microsoftonline.com/<TENANT_ID>/v2.0#user@company.com`).

  You'll need this exact value when creating RBAC bindings.
</Note>

## Prerequisites

Before you can set up OIDC authentication, make sure you have:

* An OIDC-compatible identity provider (Google, Okta, Auth0, Entra ID, etc.).
* A [GPU cluster](/docs/gpu-clusters-overview) with external OIDC enabled. OIDC must be configured at cluster creation; see [Enable external OIDC on the cluster](#enable-external-oidc-on-the-cluster) below.
* `kubectl` installed locally.
* The [admin kubeconfig](/docs/gpu-clusters-quickstart) for the cluster, to create RBAC bindings.

## Set up the cluster (admin)

The tasks in this section are run by a cluster admin using the [admin kubeconfig](/docs/gpu-clusters-quickstart). Once these are complete, share this page with your team members so they can [connect to the cluster](#connect-to-the-cluster-user).

<Steps>
  <Step title="Create an OIDC application in your identity provider">
    Create an OIDC client or application in your identity provider with the following settings.

    **Redirect URIs:**

    * `http://localhost:8000`.
    * `http://localhost:18000`.

    **Auth method:** authorization code flow with Proof Key for Code Exchange (PKCE).

    **Scopes:**

    * Always include `openid`.
    * If using `email` as the username claim, add the `email` scope.
    * If using `preferred_username` as the username claim, add the `profile` scope.
    * If using `sub` as the username claim, no additional scopes are needed.

    <Note>
      The kubeconfig generator automatically includes the correct scopes via `--oidc-extra-scope` based on your chosen username claim. You only need to ensure your IdP application allows these scopes.
    </Note>

    Record these values; you'll need them when enabling OIDC on the cluster:

    * **Issuer URL**.
    * **Client ID**.
    * **Client Secret**, only if your provider requires it (see [Set the OIDC client secret](#set-the-oidc-client-secret) below).

    <Tip>
      **Provider-specific issuer URL notes:**

      * **Auth0:** the issuer URL **must** end with a trailing slash (e.g., `https://your-tenant.auth0.com/`). Without it, OIDC discovery will fail.
      * **Okta:** use the full authorization server URL including `/oauth2/default` (e.g., `https://your-org.okta.com/oauth2/default`). The bare Okta domain will return `invalid_client`.
      * **Google:** the issuer URL is always `https://accounts.google.com`.
    </Tip>
  </Step>

  <Step title="Enable external OIDC on the cluster">
    <Warning>
      **OIDC must be configured at cluster creation time.** It cannot be added or changed after the cluster is created.
    </Warning>

    1. Go to **GPU Clusters → Create cluster**.
    2. Enable **Use custom OIDC**.
    3. Select **Configure OIDC**.
    4. Fill in:
       * **Issuer URL** from the OIDC application.
       * **Client ID** from the OIDC application.
       * **Username claim**: choose `email`, `preferred_username`, or `sub`.
    5. Wait for the UI to verify your configuration (discovery document, reachability, required claims).
    6. Create the cluster.
  </Step>

  <Step title="Grant RBAC permissions">
    <Warning>
      **Use the admin kubeconfig for this task**, not the OIDC kubeconfig. OIDC users cannot grant themselves permission. An existing cluster admin must create the RBAC bindings first.
    </Warning>

    Before any OIDC user can access the cluster, a cluster admin must create Kubernetes RBAC bindings that grant permissions to their identity.

    The `--user` value must match the exact identity Kubernetes extracts from the token. This depends on which username claim you configured.

    **If username claim is `email`:**

    ```bash theme={null}
    kubectl create clusterrolebinding my-user-admin \
      --clusterrole=cluster-admin \
      --user="user@company.com"
    ```

    **If username claim is `sub`:**

    ```bash theme={null}
    # Format: <issuer-url>#<sub-value>
    kubectl create clusterrolebinding my-user-admin \
      --clusterrole=cluster-admin \
      --user="https://accounts.google.com#105010678054620911233"
    ```

    **If username claim is `preferred_username`:**

    ```bash theme={null}
    # Format: <issuer-url>#<preferred-username-value>
    kubectl create clusterrolebinding my-user-admin \
      --clusterrole=cluster-admin \
      --user="https://login.microsoftonline.com/<TENANT_ID>/v2.0#user@company.com"
    ```
  </Step>
</Steps>

## Connect to the cluster (user)

The tasks in this section are run by each team member using their local machine.

<Steps>
  <Step title="Download the OIDC kubeconfig">
    Once the cluster status is **Ready** (visible on the cluster details page; see [GPU clusters management](/docs/gpu-clusters-management)):

    1. Open the cluster details page.
    2. Select **View OIDC kubeconfig**.
    3. Copy the kubeconfig content and save it to a file on your machine:

    ```bash theme={null}
    # Create the .kube directory if it doesn't exist.
    mkdir -p $HOME/.kube

    # Reads the kubeconfig from your clipboard. Run this immediately after copying from the dashboard.
    pbpaste > $HOME/.kube/my-cluster-oidc.yaml   # macOS
    ```

    <Tip>
      On Linux, replace `pbpaste` with `xclip -selection clipboard -o`. On any platform, you can also paste into the file using your editor of choice.
    </Tip>
  </Step>

  <Step title="Install the login helper">
    The OIDC kubeconfig uses an exec plugin to handle browser-based login and token caching. Download the binary for your platform from the [`together-kubelogin` releases](https://github.com/togethercomputer/together-kubelogin/releases/latest), verify its checksum, and move it onto your `PATH`.

    <Tabs>
      <Tab title="macOS Apple Silicon">
        ```bash theme={null}
        curl -fsSL -O https://github.com/togethercomputer/together-kubelogin/releases/latest/download/kubectl-together_login_darwin_arm64.zip
        curl -fsSL -O https://github.com/togethercomputer/together-kubelogin/releases/latest/download/kubectl-together_login_darwin_arm64.zip.sha256
        shasum -a 256 -c kubectl-together_login_darwin_arm64.zip.sha256
        unzip kubectl-together_login_darwin_arm64.zip
        sudo mv kubectl-together_login /usr/local/bin/
        rm kubectl-together_login_darwin_arm64.zip kubectl-together_login_darwin_arm64.zip.sha256
        ```
      </Tab>

      <Tab title="macOS Intel">
        ```bash theme={null}
        curl -fsSL -O https://github.com/togethercomputer/together-kubelogin/releases/latest/download/kubectl-together_login_darwin_amd64.zip
        curl -fsSL -O https://github.com/togethercomputer/together-kubelogin/releases/latest/download/kubectl-together_login_darwin_amd64.zip.sha256
        shasum -a 256 -c kubectl-together_login_darwin_amd64.zip.sha256
        unzip kubectl-together_login_darwin_amd64.zip
        sudo mv kubectl-together_login /usr/local/bin/
        rm kubectl-together_login_darwin_amd64.zip kubectl-together_login_darwin_amd64.zip.sha256
        ```
      </Tab>

      <Tab title="Linux amd64">
        ```bash theme={null}
        curl -fsSL -O https://github.com/togethercomputer/together-kubelogin/releases/latest/download/kubectl-together_login_linux_amd64.zip
        curl -fsSL -O https://github.com/togethercomputer/together-kubelogin/releases/latest/download/kubectl-together_login_linux_amd64.zip.sha256
        sha256sum -c kubectl-together_login_linux_amd64.zip.sha256
        unzip kubectl-together_login_linux_amd64.zip
        sudo mv kubectl-together_login /usr/local/bin/
        rm kubectl-together_login_linux_amd64.zip kubectl-together_login_linux_amd64.zip.sha256
        ```
      </Tab>

      <Tab title="Linux arm64">
        ```bash theme={null}
        curl -fsSL -O https://github.com/togethercomputer/together-kubelogin/releases/latest/download/kubectl-together_login_linux_arm64.zip
        curl -fsSL -O https://github.com/togethercomputer/together-kubelogin/releases/latest/download/kubectl-together_login_linux_arm64.zip.sha256
        sha256sum -c kubectl-together_login_linux_arm64.zip.sha256
        unzip kubectl-together_login_linux_arm64.zip
        sudo mv kubectl-together_login /usr/local/bin/
        rm kubectl-together_login_linux_arm64.zip kubectl-together_login_linux_arm64.zip.sha256
        ```
      </Tab>
    </Tabs>

    Verify the installation by running:

    ```bash theme={null}
    kubectl together-login --help
    ```
  </Step>

  <Step title="Set the OIDC client secret">
    The kubeconfig uses PKCE (`S256`) by default, so most providers do **not** require a client secret. However, some providers (e.g., Google) require one even for desktop or native PKCE flows. If your provider does not require a client secret, skip this task.

    If your provider requires it, set it for the current session:

    ```bash theme={null}
    export OIDC_CLIENT_SECRET="<your-client-secret>"
    ```

    <Warning>
      **Do not persist this secret in shell config files** (e.g., `.bashrc`, `.zshrc`). Set it per session, or use a secrets manager to inject it.
    </Warning>
  </Step>

  <Step title="Verify access">
    Run:

    ```bash theme={null}
    # Clear any cached tokens from previous attempts.
    rm -rf $HOME/.kube/cache/oidc-login/

    # Test access using the OIDC kubeconfig.
    kubectl --kubeconfig=$HOME/.kube/my-cluster-oidc.yaml get nodes
    ```

    **What to expect:**

    * **Browser opens** for login. Sign in with your IdP credentials.
    * **`403 Forbidden`:** authentication worked, but no RBAC binding exists for your identity. Ask your admin to complete [Grant RBAC permissions](#grant-rbac-permissions).
    * **Success:** you're authenticated and authorized. You're done.
  </Step>
</Steps>

## Revoking access

To revoke a user's access:

1. Remove their RBAC binding from the cluster:
   ```bash theme={null}
   kubectl delete clusterrolebinding my-user-admin
   ```
2. Remove the user from your IdP, or from the relevant group, to prevent new tokens from being issued.

Existing tokens will continue to work until they expire. For immediate revocation, perform both steps together.

## Token lifetime and refresh

OIDC tokens are short-lived (typically one hour, depending on your IdP configuration). When a token expires, the login plugin automatically opens a browser for re-authentication. If your IdP supports refresh tokens, re-authentication may be seamless without a login prompt.

Cached tokens are stored locally in `$HOME/.kube/cache/oidc-login/`. To force a fresh login, delete this directory.

## Troubleshooting

### `403 Forbidden`

Authentication succeeded, but there is no RBAC binding granting that identity the required permissions.

**Fix:**

* Confirm the exact value of your username claim (e.g., is it `user@company.com` or a `sub` UUID?).
* Ask a cluster admin to create a ClusterRoleBinding or RoleBinding for your user or group (see [Grant RBAC permissions](#grant-rbac-permissions)).

### `401 Unauthorized` or "provide credentials"

Token validation failed at the API server.

**Fix:**

* Verify the cluster's OIDC configuration: issuer URL must match token `iss`, client ID must match token `aud`, and the username claim must exist in the token.
* Clear cached tokens and retry:
  ```bash theme={null}
  rm -rf $HOME/.kube/cache/oidc-login/
  ```

### `client_secret is missing`

Your IdP requires a client secret that wasn't provided.

**Fix:**

```bash theme={null}
export OIDC_CLIENT_SECRET="<your-client-secret>"
```

### Browser login doesn't open

**Fix:**

* Ensure `kubectl-together_login` is installed and on your PATH.
* Run `kubectl together-login --help` to verify.

## Security best practices

* Use short-lived OIDC tokens, and rely on your IdP for user lifecycle (joiners, movers, leavers).
* Keep the admin kubeconfig restricted to break-glass scenarios. Use OIDC for day-to-day access.
* Use `email` as the username claim for the simplest RBAC setup. Other claims require issuer-prefixed `--user` values.
