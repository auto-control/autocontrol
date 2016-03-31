from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'app.views.inicio'),
	url(r'^home$', 'app.views.home'),
]