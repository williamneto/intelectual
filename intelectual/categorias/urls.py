# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url

from .views import AddCategoriaView

urlpatterns = patterns('',
	url(r'^add/', AddCategoriaView.as_view()),
)
