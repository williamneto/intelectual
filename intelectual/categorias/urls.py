# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url

from .views import AddCategoriaView, ListCategoriaView, UpdateCategoriaView, DeleteCategoriaView

urlpatterns = patterns('',
	url(r'^$', ListCategoriaView.as_view()),
	url(r'^add/', AddCategoriaView.as_view()),
	url(r'^(?P<pk>\w{24})/$', UpdateCategoriaView.as_view()),
	url(r'^delete/(?P<pk>\w{24})/$', DeleteCategoriaView.as_view()),
	
)
