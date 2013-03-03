# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import ListVideoView, AddVideoView, UpdateVideoView, DeleteVideoView

urlpatterns = patterns('',
	url(r'^$', login_required(ListVideoView.as_view())),
	url(r'^add/$', login_required(AddVideoView.as_view())),
	url(r'^(?P<pk>\d+)/$', login_required(UpdateVideoView.as_view())),
	url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteVideoView.as_view()))
)
