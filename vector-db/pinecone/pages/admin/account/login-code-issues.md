---
title: "Login code issues"
source: https://docs.pinecone.io/admin/account/login-code-issues
path: admin/account/login-code-issues
---

Fix a rejected Pinecone login code, which can expire after 10 hours or be invalidated by a shared inbox, a newer code request, or an offset system clock.

If Pinecone doesn't accept the login code you received by email, check the following causes.

## The code has expired

A code is valid for 10 hours. After that, Pinecone no longer accepts it.

## The code has already been used

If you're using a shared email account or distribution list, check with your teammates to see if anyone else has used your code.

## A subsequent request was made

If you're using a shared account, someone else may have requested a code after you did, which invalidates the first code.

## Your computer's system clock time is offset

User authentication with a verification code relies on your device's system clock to verify the time. If your computer's clock is more than 10 minutes off from your time zone, the login will fail. If you see the following error message, set your system clock to the correct time and time zone before trying again.

```
Please check your computer's system clock time. See https://docs.pinecone.io/troubleshooting/login-code-issues for more information.
```

## Your anti-spam filter followed the links in the email to check their validity

If one of the links submitted the code as part of the URL, check with your anti-spam system admin or vendor to see if this might be the cause.
