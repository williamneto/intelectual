# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url

from .views import ListYoutuberView, AddYoutuberView, UpdateYoutuberView, DeleteYoutuberView

urlpatterns = patterns('',
	url(r'^$', ListYoutuberView.as_view()),
	url(r'^(?P<pk>\w{24})/', UpdateYoutuberView.as_view()),
	url(r'^add/', AddYoutuberView.as_view()),
	url(r'^delete/(?P<pk>\w{24})/$', DeleteYoutuberView.as_view())
)
