# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from intelectual.youtubers.models import Youtuber

from .forms import AddYoutuberForm

class UpdateYoutuberView(UpdateView):
	model = Youtuber
	form_class = AddYoutuberForm
	success_url = "/admin/youtubers/"

class AddYoutuberView(CreateView):
	model = Youtuber
	form_class = AddYoutuberForm
	template_name = "youtuber/form.html"
	success_url = "/admin/youtubers/add/"

class ListYoutuberView(ListView):
	model = Youtuber
	template_name = "youtuber/list.html"
	
class DeleteYoutuberView(DeleteView):
	model = Youtuber
	success_url = "/admin/youtubers/"
	template_name = "youtuber/confirm_delete.html"
