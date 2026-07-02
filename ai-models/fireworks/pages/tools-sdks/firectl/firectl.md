---
title: "Getting started"
source: https://docs.fireworks.ai/tools-sdks/firectl/firectl
path: tools-sdks/firectl/firectl
---

Learn to create, deploy, and manage resources using Firectl

Firectl can be installed several ways based on your choice and platform.

<CodeGroup>
  ```bash homebrew theme={null}
  brew tap fw-ai/firectl
  brew install firectl

  # If you encounter a failed SHA256 check, try first running
  brew update
  ```

  ```bash macOS (Apple Silicon) theme={null}
  curl https://storage.googleapis.com/fireworks-public/firectl/stable/darwin-arm64.gz -o firectl.gz
  gzip -d firectl.gz && chmod a+x firectl
  sudo mv firectl /usr/local/bin/firectl
  sudo chown root: /usr/local/bin/firectl
  ```

  ```bash macOS (x86_64) theme={null}
  curl https://storage.googleapis.com/fireworks-public/firectl/stable/darwin-amd64.gz -o firectl.gz
  gzip -d firectl.gz && chmod a+x firectl
  sudo mv firectl /usr/local/bin/firectl
  sudo chown root: /usr/local/bin/firectl
  ```

  ```bash Linux  (x86_64) theme={null}
  wget -O firectl.gz https://storage.googleapis.com/fireworks-public/firectl/stable/linux-amd64.gz
  gunzip firectl.gz
  sudo install -o root -g root -m 0755 firectl /usr/local/bin/firectl
  ```

  ```Text Windows (64 bit) theme={null}
  wget -L https://storage.googleapis.com/fireworks-public/firectl/stable/firectl.exe
  ```
</CodeGroup>

### Sign into Fireworks account

To sign into your Fireworks account:

```bash theme={null}
firectl signin
```

If you have set up [Custom SSO](/accounts/sso) then also pass your account ID:

```bash theme={null}
firectl signin <ACCOUNT_ID>
```

### Check you have signed in

To show which account you have signed into:

```bash theme={null}
firectl whoami
```

### Check your installed version

```bash theme={null}
firectl version
```

### Upgrade to the latest version

```bash theme={null}
sudo firectl upgrade
```
