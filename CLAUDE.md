# PayPilotLabs Payments

Payment gateway integrations (Stripe, Razorpay, PayPal, Braintree, GoCardless, Paytm, M-Pesa, Paymob) installed alongside PayPilotLabs ERP. Fork of frappe/payments version-16.

> Global rules (ponytail, ADHD output, /browse browsing, impeccable UI defaults,
> commit/PR timing) are inherited from ~/.claude/CLAUDE.md — not repeated here.
> This file holds only what is specific to THIS project.

## Stack & key dirs
- Frappe v16 app (Python 3.14), MariaDB via the host product; no frontend build
- `payments/payment_gateways/doctype/*` gateway settings, `payments/templates/pages/*` checkout pages → ARCHITECTURE.md

## Project rules
- Bench app name, Python package and pyproject name are all `payments`; ERP and the framework reference it. Do not rename without docs/REVIEW-2026-11-11.md option B.
- Keep Frappe copyright headers and license.txt; update NOTICE.md if it becomes untrue.
- No imports of other products: `python .github/scripts/check_independence.py`
- Compile check: `uv run --no-project --python 3.14 python -m compileall -q payments`
- Runtime testing happens through paypilotlabs-erp's `docker/build.sh` (this repo has no docker/).
- main is protected: branch, PR, never push to main.
