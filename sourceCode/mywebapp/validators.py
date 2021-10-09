from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_domainonly_email(value):
	if not "name@yourdomain.com" in value:
		raise ValidationError(_("Enter A Valid Email."))
	return value	