from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	#url(r'^$', 'app.views.inicio'),
	url(r'^$', 'app.views.home', name = 'home'),
	url(r'^close-service/(?P<orden>\d+)/$', 'app.views.close_service', name = 'close_service'),
	url(r'^tramite-service/(?P<orden>\d+)/$', 'app.views.tramite_service', name = 'tramite_service'),
]