# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url

from .views import ListYoutuberView, AddYoutuberView

urlpatterns = patterns('',
	url(r'^$', ListYoutuberView.as_view()),
	url(r'^add/', AddYoutuberView.as_view())
)
