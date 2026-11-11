# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe

from payments.utils import get_safe_redirect_to

no_cache = True


def get_context(context):
	context.redirect_to = get_safe_redirect_to()
	token = frappe.local.form_dict.token

	if token:
		frappe.db.set_value("Integration Request", token, "status", "Cancelled")
		# A page render is a GET, which Frappe does not commit.
		frappe.db.commit()  # nosemgrep
