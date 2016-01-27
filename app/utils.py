from django.core.exceptions import ObjectDoesNotExist

def get_or_none(Model, **kwargs):
	try:
		return Model.objects.get(**kwargs)
	except ObjectDoesNotExist:
		return None