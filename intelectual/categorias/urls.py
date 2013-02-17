# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from .views import AddCategoriaView, ListCategoriaView, UpdateCategoriaView, DeleteCategoriaView, CategoriaVideosView

urlpatterns = patterns('',
	url(r'^$', login_required(ListCategoriaView.as_view())),
	url(r'^add/', login_required(AddCategoriaView.as_view())),
	url(r'^(?P<pk>\w{24})/$', login_required(UpdateCategoriaView.as_view())),
	url(r'^delete/(?P<pk>\w{24})/$', login_required(DeleteCategoriaView.as_view())),
	url(r'^videos/(?P<pk>\w{24})/$', login_required(CategoriaVideosView.as_view()))
	
)
