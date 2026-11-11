# Architecture — PayPilotLabs Payments

## Overview
A Frappe app that adds payment gateway settings doctypes, guest checkout pages and provider callbacks. Host apps (PayPilotLabs ERP) create a Payment Request, get a checkout URL from here, and receive `on_payment_authorized` back.

## Stack
- Backend: Frappe v16, Python 3.14
- Frontend: Jinja web pages + plain JS in `templates/includes/`, `public/js/razorpay.js`
- Data: doctype JSON under `payments/**/doctype/`
- Hosting: installed into the ERP Docker image (`paypilotlabs-erp/docker/apps.json`)

## Directory map
```
payments/payments/            — Payment Gateway doctype (module "Payments")
payments/payment_gateways/    — one Settings doctype per provider (module "Payment Gateways"), paymob/ client, stripe_integration.py
payments/templates/pages/     — guest pages: *_checkout, payment-success/failed/cancel
payments/utils/               — checkout URL lookup, Web Form custom fields install/uninstall
payments/overrides/           — Web Form controller + accept() override for paid web forms
payments/brand.py             — PayPilotLabs title, logo and email used by hooks.py
```

## Key flows / entry points
- Checkout: `utils.get_checkout_url` → `/<gateway>_checkout` page → `make_payment` (guest) → Settings controller → Integration Request → host doc `on_payment_authorized`
- Callbacks: guest `/api/method/payments.payment_gateways.doctype.<gw>_settings.<gw>_settings.*` (M-Pesa, PayPal, Paytm, Razorpay, GoCardless, Paymob)

## Data model & external services
- Doctypes: Payment Gateway, <Provider> Settings, GoCardless Mandate; uses framework Integration Request
- External APIs: Stripe, Razorpay, PayPal, Braintree, GoCardless, Paytm, Safaricom M-Pesa, Paymob

## Run / test / deploy
- Compile: `uv run --no-project --python 3.14 python -m compileall -q payments`
- Independence: `python .github/scripts/check_independence.py`
- Run / deploy: via paypilotlabs-erp `GITHUB_TOKEN=… ./docker/build.sh`

## Gotchas
- Jinja autoescape is off in Frappe: escape query-string values yourself in templates.
- Provider webhooks are typed into provider dashboards with `/api/method/payments.…` paths; renaming the package breaks them.
