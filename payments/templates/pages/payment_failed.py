from payments.utils import get_safe_redirect_to

no_cache = True


def get_context(context):
	context.redirect_to = get_safe_redirect_to()
