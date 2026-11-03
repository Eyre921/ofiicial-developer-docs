---
title: "Developer tools"
source: https://developers.notion.com/guides/developer-tools/overview
path: guides/developer-tools/overview
---

Access developer tools, copy resource IDs, and monitor connection health in Notion.

Use Notion’s developer tools to copy resource IDs, access your connections and tokens, and check API requests and errors. Add the **Developer** section to your sidebar for quick access to your tools.

## Turn on developer features

1. Open **Settings** from your workspace menu.
2. Select **Developer**.
3. Turn on **Enable developer features**.

The switch shows the developer toolbar, developer menus, and resource IDs. This preference is saved on your device.

Press **⌘⇧.** on macOS or **Ctrl+Shift+.** on Windows or Linux to turn developer features on or off. The shortcut changes the same setting as the switch.

## Copy resource IDs

With developer features on, use the toolbar at the bottom of the window to copy IDs for your user, workspace, and the page or resource you're viewing. Select an item to copy its ID.

Open a page, block, or database menu and select **Developer** to find IDs for that resource. The available IDs depend on what you're viewing.

To hide only the toolbar, select its **Hide the developer bar** button. Developer menus stay available. Use **Toggle developer bar** in a Developer menu to show it again. Turning developer features off and back on also restores the toolbar.

## Add Developer to your sidebar

In the customizable sidebar, the **Developer** section is separate from the developer features switch. You can keep the section visible with developer features off, or use developer features without adding the section.

1. Select the sidebar tab where you want the section to appear.
2. Select **Customize sidebar**.
3. Select **Add section**, then **Developer**.
4. Select **Done**.

The section includes links to tools available in your workspace, such as Workers, Connections, Personal access tokens, and MCP tokens. To create API credentials, see [Personal access tokens](/guides/connections-and-tokens/personal-access-tokens).

## Move or remove the section

Open **Customize sidebar** and drag the Developer section to change its position. You can also open the section's menu and use **Move up**, **Move down**, or **Move to tab**.

To hide the section from a tab, select **Remove from sidebar** beside Developer, then **Done**. Add it again through **Add section** whenever you need it. Moving or removing the section doesn't change the developer features switch.

## Monitor connection health

Open a connection’s **Health** tab in the Developer portal to see API requests, errors, and rate limits from the last 24 hours. See [Connection health](/guides/developer-tools/connection-health) to understand the charts and warnings.
