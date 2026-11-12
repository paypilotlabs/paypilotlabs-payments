# PayPilotLabs Payments

Payment gateway connections that let PayPilotLabs products take money from customers online.

By [PayPilotLabs](https://paypilotlabs.com). Support and requests: https://paypilotlabs.com/roadmap/

## What it does

- Connects your site to these payment providers: Stripe, Razorpay, PayPal, Braintree, GoCardless, Paytm, M-Pesa and Paymob.
- Gives each provider a settings page where you enter your keys and turn it on.
- Shows a checkout page where the customer pays, then a success, failed or cancelled page.
- Receives the provider's reply and tells the product that asked for the payment whether it went through.
- Keeps a record of each request sent to a provider.
- Handles recurring payments and direct debit mandates for providers that support them (for example Razorpay subscriptions and GoCardless).
- Lets website forms take a payment.

## How it helps your business

- Customers can pay online with the provider they already trust.
- You can offer more than one provider, so a customer in one country is not stuck with a method they cannot use.
- Payments are matched back to the invoice or request that asked for them, so you do not have to check by hand.
- Your keys stay in one place instead of being copied into every product.
- Adding a new provider later does not change the products that use it.

## How it fits with other PayPilotLabs products

- It is a companion app, not a product you use on its own.
- It runs on paypilotlabs-framework, like every PayPilotLabs product.
- PayPilotLabs ERP uses it to collect payment for invoices and payment requests. M-Pesa also works with ERP.
- It does not depend on any other PayPilotLabs product.

## Run it

This app is installed next to a PayPilotLabs product by that product's `docker/build.sh`. See the product's README for the build and run steps.

For development, install it into a PayPilotLabs framework v16 site together with the product that uses it.

## Licence

MIT. See [license.txt](license.txt). Based on open-source work by others; see NOTICE.md for credits.
