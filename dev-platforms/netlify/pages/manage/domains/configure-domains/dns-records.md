---
title: "Netlify DNS Records"
source: https://docs.netlify.com/manage/domains/configure-domains/dns-records.md
path: manage/domains/configure-domains/dns-records
---

---
title: "DNS records"
description: "Learn about DNS records, supported DNS record types, and adding DNS records on our platform."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

DNS records are rules that tell domain name servers how to handle traffic to your domains and subdomains. 

For domains managed by Netlify, we will automatically create "NETLIFY" records that point to our servers when you assign a domain or subdomain for your site. To learn more, visit our Forums for a verified support guide on [this type of DNS record](https://answers.netlify.com/t/support-guide-what-are-the-netlify-and-netlifyv6-type-dns-records-how-do-i-delete-these-records/17430).

You can also add your own DNS records to point to other services, such as an email provider. Visit our Forums for a verified Support Guide on [how to receive emails on your domain](https://answers.netlify.com/t/support-guide-how-can-i-receive-emails-on-my-domain/178).

## Supported record types

Netlify DNS supports the following types of records:

- **A**: Address record, which is used to map host names to their IPv4 address.
- **AAAA**: IPv6 Address record, which is used to map host names to their IPv6 address.
- **CAA**: Certificate Authority (CA) Authorization, which is used to specify which CAs are allowed to create certificates for a domain.
- **CNAME**: Canonical name record, which is used to specify alias names.
- **MX**: Mail exchange record, which is used in routing requests to mail servers.
- **NS**: Name server record, which delegates a DNS zone to an authoritative server.
- **SPF**: Sender Policy Framework record, a deprecated record type formerly used in e-mail validation systems (use a TXT record instead).
- **SRV**: Service locator record, which is used by some voice over IP, instant messaging protocols, and other applications.
- **TXT**: Text record, up to 255 characters. Can contain arbitrary text and can also be used to define machine-readable data, such as security or abuse prevention information.

## Add a new record

To add a new DNS record:

> **Snippet** component (self-closing)

2. Select 
### NavigationPath Component:

DNS
 from the left sidebar.
    ![DNS option highlighted from team dashboard](/images/dns-option-from-team-dashboard.png)
3. Select the domain (or DNS zone) you want to add a new DNS record for.
4. At the bottom of the **DNS records** section, select **Add new record**.
5. Choose the type of record to create from the menu and fill in the remaining options. The fields you need to fill out will depend on the type of record you select.
6. Select **Save** to create the record and make the changes live.

Remember, it may take up to a few hours for record changes to propagate.

Note that you can host records for other services, such as your mail provider or your backend API, with us as long as you host at least one website with us that uses the domain.

### Tip - Next step

If you're adding DNS records as part of the process of moving your DNS service to Netlify DNS, your next step is to [delegate your domain to Netlify](/manage/domains/get-started-with-domains).

## Edit a record

To make DNS changes, you need to first [add a new record](#add-a-new-record) with the new value and then [delete the old record](#delete-a-record). DNS allows multiple entries for the same name and type, so you can avoid downtime by making changes this way.

## Delete a record

To delete a DNS record:

> **Snippet** component (self-closing)

2. Select 
### NavigationPath Component:

DNS
 from the left sidebar.
    ![DNS option highlighted from team dashboard](/images/dns-option-from-team-dashboard.png)
3. Select the domain (or DNS zone) you want to delete a DNS record for.
4. In the **DNS records** section, find the record you want to delete.
5. Select the record to expand the details and then select the delete option.
6. Review the warning message and select **Delete** to confirm. 

Remember, it may take up to a few hours for record changes to propagate.

## API endpoints

You can use the [API](https://open-api.netlify.com/#operation/getDnsRecords) to get DNS records, create DNS records, and more.
