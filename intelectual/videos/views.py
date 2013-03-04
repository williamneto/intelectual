# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Video
from .forms import AddVideoForm

class AddVideoView(CreateView):
	model = Video
	form_class = AddVideoForm
	template_name = "video/form.html"
	success_url = "/admin/videos/add/"

class UpdateVideoView(UpdateView):
	model = Video
	form_class = AddVideoForm
	template_name = "video/form.html"
	success_url = "/admin/videos/"

class ListVideoView(ListView):
	model = Video
	template_name = "video/list.html"

class DeleteVideoView(DeleteView):
	model = Video
	success_url = "/admin/videos/"
	template_name = "video/confirm_delete.html"
	
	
