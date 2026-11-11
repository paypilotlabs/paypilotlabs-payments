# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe

from payments.utils import get_safe_redirect_to

no_cache = True


def get_context(context):
	doc = frappe.get_doc(frappe.local.form_dict.doctype, frappe.local.form_dict.docname)

	context.redirect_to = get_safe_redirect_to()
	context.payment_message = ""
	if hasattr(doc, "get_payment_success_message"):
		context.payment_message = doc.get_payment_success_message()
