# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url

from .views import AddCategoriaView, ListCategoriaView

urlpatterns = patterns('',
	url(r'^$', ListCategoriaView.as_view()),
	url(r'^add/', AddCategoriaView.as_view()),
)
