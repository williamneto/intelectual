# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^auth/', include('intelectual.accounts.urls')),
	url(r'^$', include('intelectual.home.urls'))
)
