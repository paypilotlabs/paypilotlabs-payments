try:
	from erpnext.tests.utils import ERPNextTestSuite as _BaseSuite
except ImportError:  # ERPNext not installed: fall back to the framework test case
	from frappe.tests.utils import FrappeTestCase as _BaseSuite


class PaymentsTestSuite(_BaseSuite):
	"""Class for creating Payments test records"""

	pass
