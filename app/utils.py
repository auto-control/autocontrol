from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
"""
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
"""

def get_or_none(Model, **kwargs):
	try:
		return Model.objects.get(**kwargs)
	except ObjectDoesNotExist:
		return None
"""
def generar_pdf(html):
		result = StringIO.StringIO()
		pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
		if not pdf.err:
				return HttpResponse(result.getvalue(), content_type='application/pdf')
		return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))
"""