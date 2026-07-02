---
title: "Connect to Turso using Java"
source: https://docs.turso.tech/connect/java
path: connect/java
---

<Steps>
  <Step title="Install">
    Currently, we have not published to the maven central. Instead, you can locally build the jar and deploy it to maven local to use it.

    Build jar and publish to maven local:

    ```bash theme={null}
    cd bindings/java

    # Please select the appropriate target platform, currently supports `macos_x86`, `macos_arm64`, `windows` and `linux_x86`
    make macos_x86

    # deploy to maven local
    make publish_local
    ```

    Now you can use the dependency as follows:

    ```gradle theme={null}
    dependencies {
        implementation("tech.turso:turso:0.0.1-SNAPSHOT")
    }
    ```
  </Step>
</Steps>
