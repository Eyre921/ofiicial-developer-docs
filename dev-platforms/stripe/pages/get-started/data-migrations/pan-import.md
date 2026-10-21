---
title: "the migration process"
source: https://docs.stripe.com/get-started/data-migrations/pan-import.md
path: get-started/data-migrations/pan-import
---

# Import payment data to Stripe

Securely migrate your customers and their saved payment details from your previous processor to Stripe.

We work with your team and your current payment provider, where needed, to move your customer and payment data securely. During the migration, you can start accepting and charging new customers on Stripe while continuing to charge existing customers through your current processor.

Choose the appropriate migration process.

| Your situation | What to do |
| --- | --- |
| You’re moving payment data from *another processor* (or a custom solution) *to Stripe* | Follow the [steps below](https://docs.stripe.com/get-started/data-migrations/pan-import.md#process-overview) and the Stripe Data Migrations team will execute the import for you. |
| You need to move data *between two Stripe accounts* | Use our [self-serve copy](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve.md) tool, which you can initiate from your Stripe Dashboard. |
| You need to migrate *subscriptions* | Migrate subscriptions using the [Billing migration toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit.md) or [the API](https://docs.stripe.com/billing/subscriptions/import-subscriptions.md).

Cancel your previous subscriptions as soon as your Stripe subscriptions become active or you’ll bill your customers twice. |

## Import process overview 

This guide explains how to migrate to Stripe from another payment processor or a custom payment solution.

| Step | Task | What happens | Owner |
| --- | --- | --- | --- |
| 1 | [Prepare for the migration](https://docs.stripe.com/get-started/data-migrations/pan-import.md#prepare-migration) | Set up your Stripe account according to your business requirements and begin accepting new payments when ready. | You |
| 2 | [Request the migration](https://docs.stripe.com/get-started/data-migrations/pan-import.md#request-migration) | Request a data export from your previous processor and submit an [import request](https://support.stripe.com/contact/email?topic=migrations) to Stripe. | You |
| 3 | [Transfer the data](https://docs.stripe.com/get-started/data-migrations/pan-import.md#transfer-data) | Stripe shares SFTP credentials with your previous processor using a PGP key or mobile number. Your previous processor encrypts your data with the Stripe PGP key and uploads it to that server. | Stripe and your previous processor |
| 4 | [Import execution](https://docs.stripe.com/get-started/data-migrations/pan-import.md#import-execution) | Stripe reviews the uploaded data and sends you a validation summary. You validate and approve the migration. Stripe imports the data and returns a mapping file. | Stripe and you |
| 5 | [Post import](https://docs.stripe.com/get-started/data-migrations/pan-import.md#post-import) | Update your integration with the mapping file, switch payments to Stripe for existing customers, then monitor payment performance. | You |

> [Bacs imports](https://docs.stripe.com/get-started/data-migrations/payment-method-imports.md?payment-methods=bacs) involve an additional step of getting sponsor bank approval. After you submit a Bacs import request, our team guides you through the requirements. End-to-end Bacs migrations typically take 4–6 weeks, while other requests complete within 10 business days after we receive all requirements.

## Prepare for the migration

### Set up your Stripe account 

You need a Stripe account to initiate the migration process. Follow these instructions to [set up your account](https://docs.stripe.com/get-started/account/set-up.md), and contact [Stripe support](https://support.stripe.com/topics/migration) if you need assistance. Learn more about [testing your integration here](https://docs.stripe.com/testing.md).

> Stripe offers optimization features, including card account updater (CAU), network tokens, and Adaptive Acceptance, that can improve authorization rates on migrated cards. See [Authorization Boost](https://stripe.com/authorization-boost) for details.

### Decide how to map customers 

Imported payment methods must be attached to a [Customer](https://docs.stripe.com/api/customers/object.md) object. You have two options:

- **Create new `Customer` objects**: This is the default process. We recommend it if none of your existing customers already exist in Stripe.
- **Map to existing customers**: To avoid duplicate objects, provide a CSV [mapping file](https://docs.stripe.com/get-started/data-migrations/map-payment-data.md) of your previous processor’s customer IDs to your Stripe [customer IDs](https://docs.stripe.com/api/customers/object.md#customer_object-id). We attach the payment methods to these customers during the migration.

By default, Stripe imports all customers and payment methods in the data file. If you only want to import a subset, provide a CSV containing only the customer IDs or [payment method](https://docs.stripe.com/api/payment_methods/object.md) IDs you want to include when you submit the [migrations intake form](https://support.stripe.com/contact/email?topic=migrations).

## Request the migration

### Request a data export from your previous processor 

Processors differ in how they handle export requests—some charge a fee, and some require specific forms. Start by contacting your current processor’s support team. You can send them this [sample message](https://support.stripe.com/questions/request-data-from-a-current-processor-for-a-data-import-to-stripe).

> Processors can take anywhere from a few days to several months to produce a final export, so build this into your migration timeline. After Stripe receives valid data, imports typically complete within 10 business days (larger datasets can take longer). Stripe reviews the data, identifies any problems, and works with you and your previous processor to resolve them. You review and approve a summary of the import before it’s finalized.

### Request a data import from Stripe 

After you request the data from your previous processor, submit a migration request to Stripe using our [intake form](https://support.stripe.com/contact/email?topic=migrations). For ownership verification purposes, you must be logged in to your Stripe account to access the form.

After you submit the form, you receive a confirmation that we received it. Our team follows up by email within 3 business days to answer any questions and provide next steps for your migration. We don’t offer phone or chat support for data migration requests.

> Never send sensitive credit card details or customer information directly to Stripe. If you have this data, let us know in your migration request form so we can help you securely transfer your data.

## Transfer the data

### SFTP credentials 

Stripe creates a dedicated SFTP server for each migration request. To securely deliver the SFTP credentials, Stripe requires one of the following:

1. **Your previous processor’s public PGP key**: Stripe encrypts the SFTP credentials with this key and sends them directly to your processor.
2. **A mobile phone number, including the country code**: Stripe texts you the SFTP password and emails you the username in the migration thread.

If Stripe doesn’t already have this information on file for your processor, we outline the required steps after you submit your request.

### Data encryption 

For security purposes, all data uploaded to Stripe’s SFTP server must be encrypted with the Stripe public PGP key. If you’re unfamiliar with PGP, see [GPG](https://gnupg.org/) and start by [importing a public key](https://www.gnupg.org/gph/en/manual.html#AEN84).

### PGP migration key

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBF0dLOEBEADMhdKpL6HmgV3rGuW/Qj9by6I/bdCOX9HrGf6MNXr00rtOKSQ5
KpM6pacMxXeaUKXgKGiU6gFWq3r6NXLRcKCmTGlnyuS2gI1Pv6R3uo+tjzeuRhiR
dKFiGDZOcreZ7b2x6q4DmpAIdf4mnVwHvLT2IeZBIDb/VlZnyIBBtUiTohmL6rVp
waAsjutd9tmnAQg/Mu/Y4C2QArr2Bqy9XlD1osyqBBOaWLKM/opoh4gpxSH90f5C
ymAZykMMk8EnPQ6F8lro6BFkOSw1wu47fBijf7pq1a15JyoA66UkPmCXiuV0XrJc
k6stzjh1zPBrhdtcQ6TaDsyxoPCzLJ4I38SSGtXdJ+jfn8WTt1Qbl4JSI1UfrbSL
nnoaAnKjy4H5q3MI7o3b87IKYe4zzFn0vPU4xOaT7AJNPu0x/BBk0bGFGw37i8+5
6FXmb+wWloT1aCA5GzpvmYGrQNK2aI2vCTlOg0IJJJzLCXpar4RzB5mSFoxaRlC/
VW5o2TndrWmQKW0yiAlTefh1Kk88h8E0bCVcklaTTaXkNk5OJJiVvf2XjbIPcKoq
mQ7N0ExfEiDQhgmABbG3KmWjHjvciaMsxVKYE1nBOhyPXaT3BRuKbOcyhWX8SF07
B31Awq/WKhMH/S6LZOqg9ui7UyohS1XkLiFhlPOStkK4Hn77guVidsTARQARAQAB
tDdTdHJpcGUgSW1wb3J0IEtleSAoUENJKSA8c3VwcG9ydC1taWdyYXRpb25zQHN0
cmlwZS5jb20+iQJUBBMBCAA+AhsDBQsJCAcCBhUKCQgLAgQWAgMBAh4BAheAFiEE
rr98SDjETS/cmaP5nHi3Ygwema0FAmp67gIFCQ+vBCEACgkQnHi3Ygwema00nQ//
W0JxDx3b+5cbBRnDs2fjzF944neXjqBeB9STbAoFfpeuUBuwU4mp1PS/GBdEXxT3
FTtoA7umQhYdAlale/ALquRMNzcAl4cOB4UaIUSGbRI0c2gy5wcKjnSSr4vlYpsc
0iKb3yfVkqHBUVvrBSOHJF2t82TnUmUwAvS9coqc1V6Lggm9kRCcbYN/QDY4/o9k
Hflpo91S3Z/BHR78WYtCQ0CPtlBkBSM6ZLcyjTtWmR4X6D+6z6sxz74abm0o/Wfc
9tISYpj3wQICyudtX7eCQlpP16nTbEXlfhFQL0cuU0gMa+Q8kHfqG9gxXtZXiXef
Z1w+iJa3abrG3WIbYlpox1kWKVqNZuNRbJjPAFQ+4gO6Qn/jT0wDPttcUxROGECL
ZsJ0GQo/rgfV1dRcHJchxSF5BryISfkX/znmzq49RtwkWBBi/2IIBecHLkNjEC9l
BYLMERrlHZcFkXU0D/7iL91YCtusInkC2bfM3+KyqidgX2Am03Ijtvkt2gnETCXj
0cnOa/EklzAFqRoB+V1saH72WMqXaR5FRPn3SSQraYSuxW+jb9ct7ESynQfp8mRj
T3V5qO8nFBdiqb7uDFj6ghuPzzOHywnpScgMFkUSszZYoKY9TJYhDUAWV82Pu3cv
NQXXfbdN/8fPuJqzWr+Y/JYsnErkOhHY9rpWIFfwlf+JAlQEEwEIAD4CGwMFCwkI
BwIGFQoJCAsCBBYCAwECHgECF4AWIQSuv3xIOMRNL9yZo/mceLdiDB6ZrQUCXbtk
kwUJAu9TYwAKCRCceLdiDB6ZrRvyD/9QHjvBRlFsA6XDr98/ik0xlx3vkVU6fx2c
xWu2C+yGEQwe1QZzctKfWALuANLEUKuoVWM/waqyfazAMzKHY+X7P4f8kilu14iF
hlCux+nh+N63jmKCQDDv3DmpTCmOisRjS4XDkKwIIIUSDmgUiEkYGXjTzWGTTE/w
hszmWo/K7Y0n37gteLF0pH10rr/cQrP4PgtQEPIpIdRooiL2tgAx2fGcUxyC4FsO
CHK/1gIKdu/cUaWOZj2cdde1khOHrkcOeM/mOwt+e5u6QgPmAm7q0TBxzfUbRxhE
oDWICSxlL6ZjFpzK9e+D7QwAP9991NNrumaOmmvB5Q3v0tnrR2NwwJSaveHIfagz
Ej+RVEUQWGUCbdqCnE8CbD/MCxL5sMS47tgbzd03A88DKH+y464eh+Jt1aaidNqq
k3rug7kmsvPMNe8lhUPjHm/e4gGgBfU8aRbnMeR6K+9w9mnFEzZi48AhXMFVMg3p
acaXYajk0Z3yJpJgpSYU9oC+1zlHsdrQyrBXIszbv285mcDpubBvoXwJ2NE7+WM8
qHjNlL1RH8ueNmkfUed1p2S2JGnjus4PzJB1c0VbC0Z/w5OcYYMsCfnXOr9PVig2
I099h9k04M/NlNg0CkhUF/hU40h0j1Rjrodq2pA4pjmDjrNSOuSJd04MzKJ0PlXi
lxXTLWPSPokCigQTAQgAfgWCZoX/LwWJC7oVTgULCQgHAgmQnHi3Ygwema01FAAA
AAAAHAAQc2FsdEBub3RhdGlvbnMub3BlbnBncGpzLm9yZ8lEWqzpgmaFZNuUMypY
pbYGFQoJCAsCBBYCAwECF4ACmwMCHgEWIQSuv3xIOMRNL9yZo/mceLdiDB6ZrQAA
Q5MP/jfANxfiNIGsMrIpR7ehxNPBUWckHtZewG4JhOxzzvgx0Z5xu5I/NoLKX5x4
tWkDZuEmDVnyFkKA6k5KcjoQOFhMLyc8bbAPs/YIb4D0aAvz1OY6+OChuxQkAu+z
D6o3RalSjbSwyYmPjaLZ+d2MoXASI+kmfQEynXO5zb3Hnst+f8GDLIatbdC5tKCv
3Lnb+KWfjVtRZRCpZDSEYq8l3D7pnADFsSI397A7A/lfmJXIx5sNVZkJnRKmt63y
bK7CCOyKdeTFPw+ZCaB3Zx6LRdrLOvgU0TYXiUqHcv89BGls0WjDOgqBl2Gh2pLd
uZPAQd2SY0Z7Q0WcvGIkrI9/6gBRtOutTLCz0VqaPbIk7QitPyveCtzw2skHKamQ
3OqnGd7Arl0yjwsJVVYXgno+XnZkT/Mwh94qLjKhDk3DEuVKMPWTCuILRvc2EGLG
ZCUa75tQkOY7Lxr5okDuHDejwex4frUdWTGywX49fTLn3s++zPCK5gUHwUjPGuk5
T7mVs88InYersl3XjD4TBXu1jeqdVUxurJfaTWfwMm8zj3aESOs9/iut7SdRmju2
1uH795gAdoKROLxQ+IVh+1+TkTKk5Ez3E7PqMKw3iO2t5UhcxFrzKWcWGIjiFczL
Tkl3sUuRQiK6mMrWfogbfSukNLtXssIQQgWV2lEyMbUZJhnniQKKBBMBCAB+BYJo
iEezBYkNvF3SBQsJCAcCCRCceLdiDB6ZrTUUAAAAAAAcABBzYWx0QG5vdGF0aW9u
cy5vcGVucGdwanMub3Jn++ZfC3WTY64YWQvlVxZieQYVCgkICwIEFgIDAQIXgAKb
AwIeARYhBK6/fEg4xE0v3Jmj+Zx4t2IMHpmtAAA7sg//XRe2AYG4WiYcdfhw+Ns4
vECyh4j7OwS3wncSWvLvndDj1gM1nBzn9auZZgSoTnl1P3FjZ9ZhOh2BHz6eUQZr
BmIG8Wp2JCLfVwiCeKFMgPj/yvWjdwwArsnDhlugb1ju+9twdLQIttgUx5+kukzr
LPIbuxlm6xcdnAS+zFk992K39f3QUkLsbpWuC5EgaN+09QpVOV3oXoniEuc+dcQa
4AC69/CEkYfzpBLipZZrlxAEDtQUzGBoMqQFWuzih7WvFrspiFnuWtff1+v/8+9F
0yNzgGDEyv9adL2h9ge21j/hFq8beL5zfiBclksRJEviIQCqjbSJuUk6XNjfpqcS
e8YYGV2IIL8cMweKVhN7Gpww4Zp10gS+axrY331bW6FQuH7lM2ndKiR7MhgZZndu
URW8h5SeK0wvvLPuaQE3NajjUGwnUXcOvJcii5qVcEqGNS9D/46QNlANt01T6m1n
wTH0YQQgVW6mddx3M1goQk13jSdgSHYoBPb+1wvIJHisV+p+xGohyuAg1HZWGJG9
lSfKJrLikeVgmwL9ghxJeP4UevMPrKdTV9JIASTi1z/hn5u6gYZVuTB7282rczeP
RwWZsC+RGJz+s2/k8rHkCv3gwtHlzzK4Vr6vtnCsc1EBb3eJG5KfPHTqZIoF/BLV
rIKLDUNMeqWrjENBlqboYOO5Ag0EanruAQEQAL/AcUTaAcBWXLBARuuwy0r3zR+5
lY3CaBHRAnZkdCY+5T/30twyS7i0yHUSkkaN0+NhXG1w5dGbDUox5jIDofNTnBDx
79N/FVF6rL3Q9VU3QGDKZGXsJNuxIpCuGEfUP0to4cqc1Z9q2Ca37gKabv0F7/y2
bhSZvERNRyy44bzBmJ8jc8ZfSCgxVBFA/UYbBsa4FfFoHd0SmNv8J01c6B85Us8R
F0PtfcMynkgN557EnrwCBzEPfUA2tJJkKuXtTGInUP1Q3VfKFQPlXbu4wENinBHw
KRNetdWjjtxCKKa+XKea8SlVuInO/UT/7aqzLhY73Zj+CqApTdXksIqi5cWFDDMH
1hEjEVLP9UVuvgLaxJxfXnnpL1WgUB5O0Z0dcL8r51JirBX5foUH18RQ4SvLVHXz
lv5qY2s7LMsp89UP6Rk6QYdqJZVpVd/qZ2rJWMx4h7mAZf7ixj8SY66Gwiu5AsD9
HkBvCCiil4YlIDDaoLaEwMqvaCZGCdy8xJaeLgTNqZfxHv+6n/2sAxzt7QRpstbr
muuT7VEWY2bAIk7mgDCQfBVf4mCLCtp9x+J1AfCHHhnKIsrqKBDZHvTD3ik26Ksn
nFpzhQRuExrVD0vBqwLUGMzWfKTWIDNFxI7XEco3HYpGKz6WKi9j9/rFznQjcdjm
rAB5uVeU9M40/RZ5ABEBAAGJAnIEGAEIAGYFgmp67gEFiQJRQwAJEJx4t2IMHpmt
NRQAAAAAABwAEHNhbHRAbm90YXRpb25zLm9wZW5wZ3Bqcy5vcmfE0/SeH/q9oZZP
VXqFBXQLApsMFiEErr98SDjETS/cmaP5nHi3Ygwema0AAJ9XD/4k+AgpWwrYbQv9
7gemnDYirxuNSfQhfRmcwxhNftGrv6uHIEm3y2w4UhXudnigJR0j2XkJC0rUBU+K
u0pAqPd3hrSxSs+U830ZrhhzIv27k2o8/ZKKrlBVZFORjrel+O32LBMhZHDra709
tJcE6dEd1NCVop9A9hKelV/FmpsFm8Z98BrxxmWB7UDf4QeZwX4Mt9VQGzZLtSOG
8HnGBth1zZPP6X19dOHFzTzNLhdUSLQqp4pmJnkHhmCHzhZeiFwfcSKVCXHgOtp5
Z9vwQEWjm6BGtHaiIyAiR3yrpC5Ffvr1yEedsooST4pZEmiAxLPXtn74O1u4BgYH
HfUS5QCLYTYRzr/W9qOvntcM7WFlmdgR2C2DiPo8Sf6jUD9UMFNhA/n0PsqDegQB
hOnljNLwHLSmngJ2IOg7x647Eks3v/lQVQO9jgCoq90ihw/KPC/a5vPRCra5ursM
+ukjhnsjNZ+4B93Vnc2UMIMHLEu/LAiEEGCef2u/k4vzbwixB9kPbo07pT74XBQk
3+2RSiAUYW2Wg1/YB9sKHhJ5GPp361SI/EkVtiyTBtlKerfiQOZ66YwTPOfaCPIT
27paTSlvjoYANkrEQBmp9lMkWF+4FfkGEpLb0vHLTPS6Q6U9A0NWgdjSfXiE9W6y
eii7sVRlBcPF1nfv4HbxmOE705/JpbkCDQRqeu4CARAA6a/zCNW+STlFPfoNu1tP
ykDoH6LAJoP8M4ZJNkA6Dz6dq/48m/YmBpgKT7ZQsxf8lq/3Y61zUChWjKvaS/wG
CMnefr5/y5OdA3ef+vVP5V6odhg+7XZWzZbZ/ImMUsirAymqCGifPQWE5wUKTnox
1Om0st3wq5zV/AbOzUHz3pll6ufJ+iNNvy0Vzuojwjk3x/P2fCqHSXHbMi+nhQ0G
aJs4cJLppn+rLDG2hIkxt+ZNNOrRoWuP3YhOGav4kXG/EjfG4nzpyMfYFT2xghJK
AeO67YfPC5VJjEnx+HJ2z6owpG44r2J3TZo0XEDlpmmx0iX9AW3ej4OjYfvCfJCi
utLSqfiLAKY91qevq8irkOAC0XWx3g2yaF1z7wmwI6UeoS2sXfaOIOBwThuTtcX2
j0Wys5MeP2NECro9tJgu1H9rvMYBVOBLSGB8U/uJmJ4mvbUsoYxd+wWUngN2BLNR
3GWLWS1PDkeAeb76m9SjZlcl41hZXljYFn9v5jAty9piLq5kIiKpZc08EVMy63Ct
nmf++Hd3T2LJXQpulV/P45xXCjSh/7gexslrmuP8ciM51dbSJzFMhIspqwM0/KN+
XUHWir8bhztRSNF6dICZq1PnNlW3eaqnKN56PPl+TC2OUcOSegCnBPfk4uw79LY6
wvhLMqaFnyY4yJN/DO40PVcAEQEAAYkE3gQYAQgC0gWCanruAgWJAlFDAAkQnHi3
Ygwema01FAAAAAAAHAAQc2FsdEBub3RhdGlvbnMub3BlbnBncGpzLm9yZwgGI+09
z1gvrQIj+n86j/4CmwLBqqAEGQEIAF0Fgmp67gIJEFTf/pv7JWLiNRQAAAAAABwA
EHNhbHRAbm90YXRpb25zLm9wZW5wZ3Bqcy5vcmemZvyCZPPisDgjeYO/Y6g6FiEE
Wa/MZiy3S97rCm8zVN/+m/slYuIAAJ9rD/wP4yO3HON6dTQB5UebNps+RIlxmLCf
OcEOBXkjXpvKUy+yuIvkn9V47FQZb3H/LKUSfPjpIba1rYmDNIXmKvM1+xMQ6VKB
xWnwO5AkxSTrXnvLfaZ3icgN3CkCz3m580G/9QtY5p9VZA6RztaqV/la0X0rN02N
X1pvg+4zv8SNHPTE96Nujp8IN6s6XVnqfgEG+DbBUn7wpaIPvWWwQi5tBGj0mtmk
GRHffK3jjGStMVwUitZ2OLwiS/O1zPLFtRlkwmC0zL0AQbWVfdnocjdFKuLAidAT
MTEw0MIvvAuGcwXqb6dQPQWae0NT2FOCxtESw28dHJKhsewJ1nIHbHhgqAGFrxCc
5wHnJhSlCNBz+gQYorBGOFM52BV008sOTzjeFCWxIF6+Miss1JtYXudocSgShbrZ
2VEW5i8Dl/IRcdkgbjMR8aiSDxj1KEDv1lW0jK0Dqb1APl2zKVTxPdgPetBJRsRl
VzEPp+ydTs7aO/n11lVC3rt1Q0+L46evMjCUd4i5zC6CA76Rvw16q8cCLxoKVyJj
eaap6Jf9kVUlskofv2/fAbb8vpDQbXXlEkQZeogPc6VkQ24cercVFwERwN9IgTmj
8ORdVULzSgkDjJy13/ScPfsVFiC0A4MulSDkNHIXMmZzL9eT4o78RH7y99zuLVEi
HU83m4BlCIbzcRYhBK6/fEg4xE0v3Jmj+Zx4t2IMHpmtAACCaBAAoEjfgAVbu4qx
ukSE3doNxFk/pmV8Rt9naWr54izeVq7lXjVA7tQIRULeRk3+IowasI6BL7DI0jrG
QkoGZ1EVFrDyA5drpdV/f8uY+j+b8L/BB/SMp4dyxcRYovQLm8QIlAywBNPWJlbV
K2suAEqqH9paLr1gnEN2O3n29Oo9HcTRWweQbly0llxRBEJV0899ac+X99WrdA4W
Hf+/ss9LBC8G0Z49gB70GTpb0kN4IOoDYg19N58bMsb9baWUvtoihitbHeI0uVbE
4ssT2KcKQg6pCgT2YoSslwjFSgdUD2p8M2lXsGEI1Drw94QN/CcCNx8hbnGZ+VLJ
9wJMdZU2OfUGS3J8IsVzUlpaCFKXy8RgjOZBQkmbWbf+RlzDDQRAeXPpUO2msPgv
b4wJrAHcJKbdo7y6N+bE2HTeJOunai9WnMwNGr0VozJVFGmPN557TrsEDGPBbPp9
/QRsRS5HjJUnMVhAegmK2kRnB7hsXvqBgDdHmXwXOBRJrp3VGvQ59CtiUWbgdk0f
JLdR36aczkPOzd3tZyMV7mw1TmiAhFgGFJS5Hy0EorVVVlhkOTmcQ75vGtFTgyM7
31GFK2izC4mX16lHB5+RhOmzPlKbAg+OHesiYTpX3WZnyNn830N0PTnIT8EaIdJ/
BJk0jHCnxygA+4LXkoqa/VkgZaYsaXE=
=5EIE
-----END PGP PUBLIC KEY BLOCK-----
```

| Field | Value |
| --- | --- |
| Key ID | `9C78B7620C1E99AD` |
| Key type | `RSA` |
| Key size | `4096 bits` |
| Fingerprint | `AEBF 7C48 38C4 4D2F DC99 A3F9 9C78 B762 0C1E 99AD` |
| User ID | `Stripe Import Key (PCI) <support-migrations@stripe.com>` |

After importing the key, you can encrypt your file by running:

```bash
gpg --encrypt --recipient 9C78B7620C1E99AD FILENAME
```

This outputs `FILENAME.gpg`, which you can upload to the dedicated SFTP server.

### File format requirements 

Use CSV format and preserve identifiers, including leading zeros. Spreadsheet applications can alter these values when they treat them as numbers. See our [complete file format guidelines](https://docs.stripe.com/get-started/data-migrations/payment-method-imports.md) for details.

Stripe can import your customers’ saved payment details and billing address information, including cards, ACH Direct Debit, Bacs Direct Debit, SEPA Direct Debit, and pre-authorized debits (PADs). See [payment method imports](https://docs.stripe.com/get-started/data-migrations/payment-method-imports.md) for the required fields and details for each payment method.

Stripe can’t import:

- **Card security codes (CVC)**: PCI DSS rules prohibit storing the security code after a transaction is authorized, and the CVC isn’t required to charge a saved card.
- **Data your previous processor never stored**: Stripe can only import the data that’s provided.
- **Subscriptions, invoices, and other billing data**: You can migrate subscriptions using the [Billing migration toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit.md) or [the API](https://docs.stripe.com/billing/subscriptions/import-subscriptions.md). For more information, contact [billing-migrations@stripe.com](mailto:billing-migrations@stripe.com).

## Import execution

After your previous processor uploads the data, Stripe reviews it, works with you to resolve any issues, and shares a validation summary for your approval.

During validation, you might need to confirm the last four digits of the payment method for two of your customer IDs. This verifies that the received data aligns with your expectations.

After your explicit approval, Stripe executes the import, creating `Customer` and payment method objects in your account. Imports typically complete within 10 business days of Stripe receiving correct data. Larger datasets can take longer.

When the import completes, Stripe returns a [mapping file](https://docs.stripe.com/get-started/data-migrations/pan-import.md#update-integration) (CSV or JSON) linking your previous processor’s IDs to your new Stripe IDs.

## Post import

### Update your integration 

Parse the mapping file that Stripe returns after the import and update your database accordingly. After you update your integration with this mapping file, you can begin charging all of your customers on Stripe.

```
{
  "1893": {
    "cards": {
      "2600": {
        "id": "card_2222222222",
        "fingerprint": "x9yW1WE4nLvl6zjg",
        "last4": "4242",
        "exp_month": 1,
        "exp_year": 2020,
        "brand": "Visa"
      },
      "3520": {
        "id": "card_3333333333",
        "fingerprint": "nZnMWbJBurX3VHIN",
        "last4": "0341",
        "exp_month": 6,
        "exp_year": 2021,
        "brand": "Mastercard"
      }
    },
    "id": "cus_abc123def456"
  }
}
```

The example JSON mapping above shows:

- Imported customer ID 1893 as a new Stripe `Customer` with ID `cus_abc123def456`.
- Imported customer card ID 2600 as a new Stripe `Card` with ID `card_2222222222`.
- Imported customer card ID 3520 as a new Stripe `Card` with ID `card_3333333333`.

Stripe can import card data as [PaymentMethods](https://docs.stripe.com/api/payment_methods/object.md) instead of `Card` objects if you specify it in your migration request. The following examples show the mapping files for different types of payment information imports.

#### Card as card_ CSV

```csv
old_customer_id,customer_id,old_card_id,card_id,card_fingerprint,card_last4,card_exp_month,card_exp_year,card_brand
old_cus_100,cus_abc123def456,old_src_100,card_2222222222,x9yW1WE4nLvl6zjg,4242,09,2024,Visa
```

#### Card as PaymentMethod (pm_) CSV

```
old_id,source_old_id,created_customer,source_new_id,card_fingerprint,card_last4,card_exp_month,card_exp_year,card_brand
old_cus_100,old_src_100,cus_abc123def456,pm_2222222222,x9yW1WE4nLvl6zjg,4242,09,2024,Visa
```

#### ACH as bank account (ba_) CSV

```
old_customer_id,customer_id,old_bank_account_id,bank_account_id,bank_account_fingerprint,bank_account_last4
old_cus_100,cus_abc123def456,old_src_100,ba_2222222222,x9yW1WE4nLvl6zjg,4242
```

#### ACH as PaymentMethod (pm_) CSV

```
old_customer_id,customer_id,old_bank_account_id,bank_account_id,bank_account_fingerprint,bank_account_last4
old_cus_100,cus_abc123def456,old_src_100,pm_2222222222,x9yW1WE4nLvl6zjg,4242
```

#### Bacs as PaymentMethod (pm_) CSV

```
old_id,source_old_id,created_customer,source_new_id,mandate_id
old_cus_100,old_src_100,cus_abc123def456,pm_2222222222,mandate_1MvojA2eZvKYlo2CvqTABjZs
```

#### SEPA as PaymentMethod (pm_) CSV

```
old_customer_id,customer_id,old_source_id,source_id,type,bank_code,branch_code,country,fingerprint,last4,mandate_reference,mandate_url,mandate_id
old_cus_100,cus_abc123def456,old_src_100,pm_2222222222,sepa_debit,1111,000,DE,x9yW1WE4nLvl6zjg,4242,ref_000,example.com,mandate_1MvojA2eZvKYlo2CvqTABjZs
```

### Maximize authorization rates 

Your Stripe account has its own merchant identifier (MID), which differs from your previous MID. Because issuers might not recognize the new MID when you begin charging customers, you might experience a temporary increase in declined payments, which can appear as `generic_decline`, `do_not_honor`, `transaction_not_allowed`, or `try_again_later`.

To reduce these declines, we recommend ramping up your volume rather than switching everything at once, and sending your highest-quality traffic first: one-time and customer-initiated payments before recurring ones, and domestic before international. Learn more about [maintaining payments performance when adopting Stripe](https://stripe.com/guides/maintaining-payments-performance-when-adopting-stripe#introduction).

For a detailed breakdown of decline codes, causes, and recommended actions, see [Optimizing authorization rates](https://stripe.com/guides/optimizing-authorization-rates).

### Migration timeline 

After Stripe receives all valid data, the standard processing time is 10 business days. Imports exceeding 1M records might take longer, and [Bacs migrations](https://docs.stripe.com/get-started/data-migrations/payment-method-imports.md?payment-methods=bacs) take 4–6 weeks. The primary variable is your previous processor’s export timeline, which can range from days to months. We recommend [requesting the data export](https://docs.stripe.com/get-started/data-migrations/pan-import.md#request-data-export) from your previous processor as early as possible.

### Problems obtaining processor data 

Check your terms and conditions with your previous processor, because they might be contractually obligated to release your data on request. If you’re having difficulty, you can add us to your communication thread with them and we’ll help facilitate the conversation.

### Data Transfer Agreement requests 

The Stripe PCI DSS compliance is sufficient for a secure data transfer, so a your previous processor doesn’t need you to sign a Data Transfer Agreement (DTA) to be compliant. If your processor insists that you sign one, we can review the agreement with our Legal team on a case-by-case basis, though this significantly lengthens the migration timeline.

### Data protection during transfer 

All data must be [encrypted using the Stripe PGP key](https://docs.stripe.com/get-started/data-migrations/pan-import.md#migration-pgp-key) before transfer and delivered using [SFTP](https://docs.stripe.com/get-started/data-migrations/pan-import.md#sftp-credentials). Your previous processor handles the encryption and upload. Stripe provides the PGP key and SFTP credentials to facilitate this.

### Download the Stripe PCI AOC and PGP key 

You can download Stripe’s PCI Attestation of Compliance (AOC) directly from your Dashboard at **Settings** > **Compliance and documents** > [Stripe documents](https://dashboard.stripe.com/settings/compliance/download/pci).

The Stripe PGP migration key is available in the [PGP migration key](https://docs.stripe.com/get-started/data-migrations/pan-import.md#migration-pgp-key) dropdown on this page.

### Will I be able to export my data from Stripe at a later date? 

You can export your data to any PCI-compliant processor. The receiving processor needs to provide a valid PCI AOC document and an RSA 4096 PGP key hosted on their company website. Stripe encrypts the data and delivers it using SFTP.

## See also

- [Payments optimizations](https://docs.stripe.com/payments/analytics/optimization.md)
- [Multiple accounts](https://docs.stripe.com/get-started/account/multiple-accounts.md)
- [Account checklist](https://docs.stripe.com/get-started/account/checklist.md)

