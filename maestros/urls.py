from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
	url(r'^mecanicos/$', listMecanicosView.as_view(), name = 'list_mecanicos'),
	url(r'^mecanicos/(?P<pk>\d+)/$', login_required(detailMecanicosView.as_view()), name = 'detail_mecanicos'),
	url(r'^mecanicos/nuevo$', createMecanicoView.as_view(), name = 'create_mecanicos'),
	url(r'^mecanicos/actualizar/(?P<pk>\d+)/$', updateMecanicoView.as_view(), name = 'update_mecanicos'),
]