# -*- coding: utf-8 -*-

from mongotools.views import CreateView, ListView

from .models import Video
from .forms import AddVideoForm

class AddVideoView(CreateView):
	model = Video
	form_class = AddVideoForm
	template_name = "form.html"
	success_url = "/admin/add_video/"

class ListVideoView(ListView):
	document = Video
	template_name = "video/list.html"
