# -*- coding: utf-8 -*-

from mongotools.views import CreateView, ListView, UpdateView, DeleteView

from .models import Video
from .forms import AddVideoForm

class AddVideoView(CreateView):
	model = Video
	form_class = AddVideoForm
	template_name = "video/form.html"
	success_url = "/admin/videos/add/"

class UpdateVideoView(UpdateView):
	document = Video
	form_class = AddVideoForm
	template_name = "video/form.html"
	success_url = "/admin/videos/"

class ListVideoView(ListView):
	document = Video
	template_name = "video/list.html"

class DeleteVideoView(DeleteView):
	document = Video
	success_url = "/admin/videos/"
	
	
