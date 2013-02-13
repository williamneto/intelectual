# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from.views import HomeAdminView

urlpatterns = patterns('',
	url(r'^$',HomeAdminView.as_view()),
	url(r'^videos/', include("intelectual.videos.urls")),
	url(r'^categorias/', include("intelectual.categorias.urls")),
	url(r'^youtubers/', include("intelectual.youtubers.urls")),
)
