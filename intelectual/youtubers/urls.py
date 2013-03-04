# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from .views import ListYoutuberView, AddYoutuberView, UpdateYoutuberView, DeleteYoutuberView

urlpatterns = patterns('',
	url(r'^$', login_required(ListYoutuberView.as_view())),
	url(r'^(?P<pk>\d+)/', login_required(UpdateYoutuberView.as_view())),
	url(r'^add/', login_required(AddYoutuberView.as_view())),
	url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteYoutuberView.as_view()))
)
