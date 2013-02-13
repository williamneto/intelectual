# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from .views import HomePageView

urlpatterns = patterns('',
	url(r'^$', HomePageView.as_view()),
	url(r'^auth/', include('intelectual.accounts.urls')),
	url(r'^admin/', include('intelectual.admin.urls')),
)
