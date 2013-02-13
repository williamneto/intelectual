# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from .views import ListVideoView, AddVideoView

urlpatterns = patterns('',
	url(r'^$', ListVideoView.as_view()),
	url(r'^add/$', AddVideoView.as_view()),
)
