---
title: "Netlify User Settings"
source: https://docs.netlify.com/manage/accounts-and-billing/user-settings.md
path: manage/accounts-and-billing/user-settings
---

---
title: "User settings"
description: "Access user settings to manage items such as your avatar, Git provider connection, UI theme, keyboard shortcuts, 2FA, and connections with other services."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

You can access your Netlify user settings by selecting your avatar (labeled "User" for screen readers) in the Netlify UI, then selecting [**User settings**](https://app.netlify.com/user/settings).

## Personal profile

Your profile includes your avatar, name, email, password, default team, connected Git providers, and appearance preference for the Netlify UI.

### Password requirements 

Netlify requires that the password you use to log in is at least 10 characters.

### Add a user avatar

If you signed up for Netlify using GitHub, GitLab, or Bitbucket, then your Netlify user avatar will default to your Git provider avatar. Users can upload a custom avatar to display by going to [**User settings**](https://app.netlify.com/user/settings). Select 
### NavigationPath Component:

User settings > General > Personal information > Edit settings
, then select **Upload image**. After uploading your image, select **Save**.

#### Avatar image guidelines

- Maximum file size: 1 MB

- Supported file formats: PNG, GIF, JPEG (.jpeg and .jpg), WebP

- Resolution: There are no resolution or aspect ratio restrictions. Images will be resized and cropped as needed to fit the display area. Images will maintain their aspect ratios when being resized. Cropping may be horizontal or vertical but never both.

### Remove a user avatar

You can remove either the avatar set by your Git provider or a custom user avatar you previously uploaded by going to [**User settings**](https://app.netlify.com/user/settings). Select 
### NavigationPath Component:

User settings > General > Personal information > Edit settings
, then select **Remove image**. Then, select **Save**. Your avatar will fall back to a [Gravatar](https://gravatar.com/) using your user email.

### Connect your Git provider accounts

You can connect your Netlify user to one or more Git providers to make logging in and collaborating with your team easier. You can add, edit, and disconnect your Git provider accounts from 
### NavigationPath Component:

User settings > General > Profile > Connected accounts
.

If you signed up for Netlify using GitHub, GitLab, or Bitbucket, then your Netlify user will already be linked to that Git provider.

You can connect your Netlify user to multiple Git providers. However, for log in purposes, you can't connect two different Netlify users to the same Git provider account. 

You also can't connect one Netlify user to more than one account from the same Git provider, unless you're [matching a non-team member](/deploy/deploy-overview#match-to-an-existing-team-member) with a team member's Netlify account.

Member lists at the site and team level include connected accounts for each member.

### Choose a Netlify UI theme

You can choose a Netlify UI theme by going to 
### NavigationPath Component:

User settings > General > Profile > Appearance
.
You can select a theme or have it be set by your operating system preferences.

### Manage keyboard shortcuts

Custom keyboard shortcuts can help you get around Netlify faster. You can define keyboard shortcuts in the [Command Palette](/command-palette).

Shortcuts are made up of one or more modifier keys, such as <kbd>shift</kbd> or <kbd>command</kbd> + any other key.

## Enable two-factor authentication (2FA)

Secure how you access teams and organizations with two-factor authentication (2FA). From your Netlify user settings, you can set up 2FA with an authentication app. If your Netlify team has a Pro plan or higher, your Organization or Team Owner may encourage or require you to set up 2FA for your Netlify user ID through your personal user settings.

Once you enable 2FA for your Netlify user ID, you're required to enter a temporary authentication code from your authentication app to access teams or organizations connected to that user ID and email. As a fallback, you can use a backup recovery code.

Example authentication apps include:
- [1Password](https://1password.com/)
- [Authy](https://authy.com/)
- [Duo](https://duo.com/product/multi-factor-authentication-mfa/duo-mobile-app)
- [Google Authenticator](https://support.google.com/accounts/answer/1066447)

To enable 2FA for your Netlify user ID:

1. Choose and install an authentication app on your phone. Your company or organization may ask you to use a certain authentication app.

2. To enable 2FA for your Netlify user ID, go to 
### NavigationPath Component:

User settings > Security > Two-factor authentication

3. Select **Enable two-factor authentication**, and you'll be presented with a QR code to scan into your chosen authentication app. Alternatively, you can enter the alphanumeric code listed under **Manual entry** directly into your authentication app. In both cases, the app will then present a 6-digit authentication code to enter into the Netlify UI.

    ![](/images/accounts-and-billing-2fa-steps.png)

4. Enter the code and select **Next: Recovery codes**. 

5. Copy or print your recovery codes so you can still access your account even if you don't have your authentication app or phone. Your recovery codes are only presented once, so be sure to copy or print them and keep them somewhere safe before completing your setup. Note that you can only use a specific recovery code once.

### Caution - Keep them secret! Keep them safe!

Recovery codes help prevent you from being locked out of your account if you lose your phone or otherwise can't access your authentication app. Store them somewhere secure where you know you can find them again.

6. After saving your recovery codes, select **Finished! I saved my recovery codes.**

If you need to disable two-factor authentication for your user ID, go to  
### NavigationPath Component:

User settings > Security > Two-factor authentication
. Select **Disable two-factor authentication**. You will need to enter a valid authentication or recovery code to complete the task.

## Connect with other applications

Under the **Applications** section of your user settings are controls for three methods of connecting your Netlify user with other applications and services:

* **OAuth applications** - If you build or use an application that accesses the Netlify API as an OAuth app, you can add it here. When you register an application, Netlify will provide a client ID and secret you can use in your application settings.
* **Personal access tokens (PATs)** - You can generate these for manual authentication in shell scripts or commands that use the [Netlify CLI](/api-and-cli-guides/cli-guides/get-started-with-cli#obtain-a-token-in-the-netlify-ui) or [API](/api-and-cli-guides/api-guides/get-started-with-api#authentication). For each token you generate, you can set an expiration date to help keep your information secure. Go to 
### NavigationPath Component:

Applications > Personal access tokens
 to get started.
* **Authorized applications** - When you use your Netlify user account to log in with another application, such as Netlify CLI, Netlify Support Forums, or Zapier, the application is added to this list. You can revoke authorization by selecting 
### NavigationPath Component:

Options > Revoke access
 for the application.

### Tip - Grant access to a team where only SSO is allowed

If your team requires you to log in with [single sign-on (SSO)](/manage/security/secure-netlify-access/configure-team-saml-sso), API calls to your team using your access tokens will be denied access by default. This applies to both personal access tokens and tokens from authorized applications. You can choose to grant access to the team when generating a new personal access token or authorizing an application. You must be logged in to the team with SSO to grant access to it. Each token can be granted access to only one SSO team. To grant access to multiple teams, use multiple tokens.


