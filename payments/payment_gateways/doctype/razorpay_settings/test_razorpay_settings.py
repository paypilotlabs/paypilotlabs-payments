import hashlib
import hmac

import frappe

from payments.tests.utils import PaymentsTestSuite

SECRET = "test_secret"


def sign(body):
	return hmac.new(SECRET.encode(), body.encode(), hashlib.sha256).hexdigest()


class TestRazorpaySettings(PaymentsTestSuite):
	def setUp(self):
		self.settings = frappe.new_doc("Razorpay Settings")
		self.settings.get_settings = lambda data: frappe._dict(api_key="key", api_secret=SECRET)

	def test_order_signature(self):
		data = frappe._dict(order_id="order_1")
		self.assertTrue(self.settings.verify_payment_signature(data, "pay_1", sign("order_1|pay_1")))

	def test_subscription_signature(self):
		data = frappe._dict(order_id="order_1", subscription_id="sub_1")
		self.assertTrue(self.settings.verify_payment_signature(data, "pay_1", sign("pay_1|sub_1")))

	def test_payment_from_another_order_is_rejected(self):
		data = frappe._dict(order_id="order_1")
		with self.assertRaises(frappe.PermissionError):
			self.settings.verify_payment_signature(data, "pay_2", sign("order_2|pay_2"))

	def test_missing_signature_or_order_is_rejected(self):
		with self.assertRaises(frappe.PermissionError):
			self.settings.verify_payment_signature(frappe._dict(order_id="order_1"), "pay_1", None)
		with self.assertRaises(frappe.PermissionError):
			self.settings.verify_payment_signature(frappe._dict(), "pay_1", sign("|pay_1"))
