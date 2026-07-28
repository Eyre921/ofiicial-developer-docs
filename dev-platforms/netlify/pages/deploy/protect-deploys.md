---
title: "Protect deploys"
source: https://docs.netlify.com/deploy/protect-deploys.md
path: deploy/protect-deploys
---

---
title: "Protect deploys"
description: "Learn how to secure your deploys with project visibility, password protection, visitor access controls, and other security measures."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Control who can access your deploys on Netlify with project visibility, password protection, visitor access controls, Netlify team-based restrictions, blocking web traffic, and more.

## Project visibility

> **Pricing Information:** This feature is available on [Credit-based Free, Personal, and Pro](https://www.netlify.com/pricing/?category=personal) plans only. On a Free and Personal plan, private projects can only be seen by the Team Owner. On [Pro](https://www.netlify.com/pricing/?category=pro) plans, you can add unlimited team members to your project or team to view a project.

You can control who can access your project's deploys by making the project **private**, so that only logged-in members of your Netlify team can view it.

If your team has private by default enabled, new projects start private, unless you change the visibility setting. This includes [previews](/deploy/deploy-overview/#types-of-previews), which stay private unless you change the preview visibility setting. You can set visibility defaults at the team level or adjust them per project, with separate settings for production deploys and previews.

On Pro plans, you can invite unlimited team members to view a private project's deploys.

Learn more in our [project visibility docs](/manage/security/secure-access-to-sites/project-visibility).

## Password protection

You can control who can access your project's deploys by requiring a password. Learn more at our [Password Protection docs](/manage/security/secure-access-to-sites/password-protection).

## Web traffic rules

You can control who can access your project's deploys by setting up Firewall Traffic Rules. 

Set a rule to limit access based on a web visitor's: 
- IP address
- Country
- Subregion

Learn more at our [Firewall Traffic Rules docs](/manage/security/secure-access-to-sites/traffic-rules).

## Rate limiting

You can control who can access your project's deploys by setting up rate limiting. Learn more at our [Rate Limiting docs](/manage/security/secure-access-to-sites/rate-limiting).            
