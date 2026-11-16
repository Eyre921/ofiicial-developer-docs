---
title: "Add discounts, upsells, and optional items"
source: https://docs.stripe.com/payments/checkout/promotions.md
path: payments/checkout/promotions
---

# Add discounts, upsells, and optional items

Boost sales with discounts and offers.

[Add discounts](https://docs.stripe.com/payments/checkout/discounts.md): Reduce the amount charged to a customer by discounting their subtotal with coupons and promotion codes.

[Configure free trials](https://docs.stripe.com/payments/checkout/free-trials.md): Offer customer free trials on subscriptions.

[Configure subscription upsells](https://docs.stripe.com/payments/checkout/upsells.md): Enable customers to upgrade their subscription plan at checkout by using upsells.

[Add optional items](https://docs.stripe.com/payments/checkout/optional-items.md): Enable customers to purchase complementary products at checkout by using optional items.

[Let customers complete orders for free](https://docs.stripe.com/payments/checkout/no-cost-orders.md): Accept orders for no-cost line items, and apply 100% off discounts in payment mode.

## Run pricing experiments 

Test two prices for a product to see which one earns more revenue in Checkout. Pricing experiments are in [private preview](https://docs.stripe.com/release-phases.md).

### Join the pricing experiments waitlist

Enter your email to request early access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/checkout/promotions" \
  -d '{"email": "EMAIL", "preview": "pricing_experiments_preview"}'
```

