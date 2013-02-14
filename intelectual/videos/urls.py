# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from .views import ListVideoView, AddVideoView, UpdateVideoView, DeleteVideoView

urlpatterns = patterns('',
	url(r'^$', ListVideoView.as_view()),
	url(r'^add/$', AddVideoView.as_view()),
	url(r'^(?P<pk>\w{24})/$', UpdateVideoView.as_view()),
	url(r'^delete/(?P<pk>\w{24})/$', DeleteVideoView.as_view())
)
