# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^auth/', include('intelectual.accounts.urls')),
	url(r'^admin/', include('intelectual.admin.urls')),
)
