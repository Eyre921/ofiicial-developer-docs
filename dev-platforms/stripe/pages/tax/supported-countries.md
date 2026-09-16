---
title: "Countries supported by Stripe Tax"
source: https://docs.stripe.com/tax/supported-countries.md
path: tax/supported-countries
---

# Countries supported by Stripe Tax

Learn where you can use Stripe Tax.

Stripe can calculate tax on sales in the locations listed in the table below. Select a location to learn more about:

- When to register for tax collection on your sales
- How to register to collect tax and links to the relevant tax authority
- How Stripe calculates tax
- How to report and file your taxes

### Request to join the preview for manual tax rules.

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/tax/supported-countries" \
  -d '{"email": "EMAIL", "preview": "manual_tax_rules_waitlist_unsupported_jurisdiction_preview"}'
```

You can also learn about tax calculation and collection in each region:

- [Africa](https://docs.stripe.com/tax/supported-countries/africa.md)
- [Asia Pacific](https://docs.stripe.com/tax/supported-countries/asia-pacific.md)
- [Canada](https://docs.stripe.com/tax/supported-countries/canada.md)
- [European Union](https://docs.stripe.com/tax/supported-countries/european-union.md)
- [Europe (outside of EU)](https://docs.stripe.com/tax/supported-countries/europe.md)
- [Latin America and the Caribbean](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md)
- [United States](https://docs.stripe.com/tax/supported-countries/united-states.md)

## Supported countries

Stripe supports tax calculation on different types of goods and services, and different types of sales (depending on the location).

The table below lists each location’s support. Select the country name to learn more about collecting tax in that country.

> If you’re missing a country or tax type you want, you can email us at [stripe-tax-support@stripe.com](mailto:stripe-tax-support@stripe.com?subject=%5BNew%20Country%20Request%5D).

The table references the following terms:

- **All PTCs**: You can use any supported [product tax codes (PTCs)](https://docs.stripe.com/tax/tax-codes.md) in this location.
- **Digital products**: We only support [digital products](https://docs.stripe.com/tax/tax-codes.md?type=digital) (non-physical items or services that are delivered, given, or rendered electronically) in this location and don’t calculate tax for any product not using a digital product tax code.
- **Your business location**: ✓ Supported means your business can be based in this location and use Stripe Tax. ❌ Not supported means your business can’t be based here.
- **Your customer location**: ✓ Supported means Stripe Tax can calculate tax on sales to customers in this location.

| Country | Product type | Tax type | Your business location | Your customer location | Supported since |
| --- | --- | --- | --- | --- | --- |
| [AL](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=albania) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [AO](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=angola) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [AM](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=armenia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [AW](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=aruba) | Digital products | Sales tax | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [AU](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=australia) | All PTCs | GST | ✓ Supported | ✓ Supported | 10/2/2023 |
| [AT](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=austria) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [AZ](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=azerbaijan) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [BS](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=bahamas) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [BH](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=bahrain) | Digital products | VAT | ❌ Not supported | ✓ Supported | 4/25/2024 |
| [BD](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=bangladesh) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [BB](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=barbados) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [BY](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=belarus) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [BE](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=belgium) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [BJ](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=benin) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [BA](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=bosnia-and-herzegovina) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [BG](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=bulgaria) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [BF](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=burkina-faso) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [KH](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=cambodia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [CM](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=cameroon) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [CA](https://docs.stripe.com/tax/supported-countries/canada.md) | All PTCs | GST and provincial taxes | ✓ Supported | ✓ Supported | 10/2/2023 |
| [CV](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=cape-verde) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [CL](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=chile) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [CO](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=colombia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [CR](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=costa-rica) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [HR](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=croatia) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [CY](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=cyprus) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [CZ](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=czechia) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [CD](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=democratic-republic-congo) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [DK](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=denmark) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [EC](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=ecuador) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [EG](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=egypt) | Digital products | VAT | ❌ Not supported | ✓ Supported | 4/25/2024 |
| [EE](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=estonia) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [ET](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=ethiopia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [FI](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=finland) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [FR](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=france) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [GE](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=georgia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 4/25/2024 |
| [DE](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=germany) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [GR](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=greece) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [GN](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=guinea) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [HK](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=hong-kong) | All PTCs | No tax | ✓ Supported | ✓ Supported | 10/2/2023 |
| [HU](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=hungary) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [IS](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=iceland) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/2/2023 |
| [IN](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=india) | Digital products | IGST | ❌ Not supported | ✓ Supported | 4/14/2025 |
| [ID](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=indonesia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [IE](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=ireland) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [IT](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=italy) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [JP](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=japan) | All PTCs | JCT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [KZ](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=kazakhstan) | Digital products | VAT | ❌ Not supported | ✓ Supported | 4/25/2024 |
| [KE](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=kenya) | Digital products | VAT | ❌ Not supported | ✓ Supported | 4/25/2024 |
| [KG](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=kyrgyzstan) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [LA](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=laos) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [LV](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=latvia) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [LI](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=switzerland-and-liechtenstein) | All PTCs | VAT | ✓ Supported | ✓ Supported | 1/1/2025 |
| [LT](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=lithuania) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [LU](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=luxembourg) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [MY](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=malaysia) | Digital products | Service tax | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [MT](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=malta) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [MR](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=mauritania) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [MX](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=mexico) | All PTCs | VAT | ✓ Supported | ✓ Supported | 9/2/2025 |
| [MD](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=moldova) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [ME](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=montenegro) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [MA](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=morocco) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [NP](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=nepal) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [NL](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=netherlands) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [NZ](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=new-zealand) | All PTCs | GST | ✓ Supported | ✓ Supported | 10/2/2023 |
| [NG](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=nigeria) | Digital products | VAT | ❌ Not supported | ✓ Supported | 4/25/2024 |
| [MK](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=north-macedonia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [NO](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=norway) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [OM](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=oman) | Digital products | VAT | ❌ Not supported | ✓ Supported | 4/25/2024 |
| [PE](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=peru) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [PH](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=philippines) | Digital products | VAT | ❌ Not supported | ✓ Supported | 5/2/2025 |
| [PL](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=poland) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [PT](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=portugal) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [PR](https://docs.stripe.com/tax/supported-countries/united-states/collect-tax.md?tax-jurisdiction-united-states=puerto-rico) | All PTCs | Sales tax | ✓ Supported | ✓ Supported | 10/17/2023 |
| [RO](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=romania) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [RU](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=russia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [SA](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=saudi-arabia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [SN](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=senegal) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [RS](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=serbia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [SG](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=singapore) | All PTCs | GST | ✓ Supported | ✓ Supported | 10/2/2023 |
| [SK](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=slovakia) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [SI](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=slovenia) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [ZA](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=south-africa) | All PTCs | VAT | ❌ Not supported | ✓ Supported | 10/2/2023 |
| [KR](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=south-korea) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [ES](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=spain) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [LK](https://docs.stripe.com/tax/supported-countries/asia-pacific/collect-tax.md?tax-jurisdiction-asia-pacific=sri-lanka) | Digital products | VAT | ❌ Not supported | ✓ Supported | 7/1/2026 |
| [SR](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=suriname) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [SE](https://docs.stripe.com/tax/supported-countries/european-union/collect-tax.md?tax-jurisdiction-european-union=sweden) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [CH](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=switzerland-and-liechtenstein) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [TW](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=taiwan) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/1/2025 |
| [TJ](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=tajikistan) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [TZ](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=tanzania) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [TH](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=thailand) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [TR](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=turkiye) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [UG](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=uganda) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [UA](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=ukraine) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/30/2024 |
| [AE](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=united-arab-emirates) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [GB](https://docs.stripe.com/tax/supported-countries/europe/collect-tax.md?tax-jurisdiction-europe=united-kingdom) | All PTCs | VAT | ✓ Supported | ✓ Supported | 10/2/2023 |
| [US](https://docs.stripe.com/tax/supported-countries/united-states.md) | All PTCs | Sales tax and some local taxes | ✓ Supported | ✓ Supported | 10/2/2023 |
| [UY](https://docs.stripe.com/tax/supported-countries/latin-america-and-caribbean.md?tax-jurisdiction-latin-america=uruguay) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [UZ](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=uzbekistan) | Digital products | VAT | ❌ Not supported | ✓ Supported | 10/7/2024 |
| [VN](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=vietnam) | Digital products | VAT | ❌ Not supported | ✓ Supported | 8/17/2023 |
| [ZM](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=zambia) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |
| [ZW](https://docs.stripe.com/tax/supported-countries/africa/collect-tax.md?tax-jurisdiction-africa=zimbabwe) | Digital products | VAT | ❌ Not supported | ✓ Supported | 12/18/2024 |

