# -*- coding: utf-8 -*-

from mongotools.views import CreateView, ListView, UpdateView, DeleteView

from intelectual.youtubers.models import Youtuber

from .forms import AddYoutuberForm

class UpdateYoutuberView(UpdateView):
	document = Youtuber
	form_class = AddYoutuberForm
	success_url = "/admin/youtubers/"

class AddYoutuberView(CreateView):
	document = Youtuber
	form_class = AddYoutuberForm
	template_name = "youtuber/form.html"
	success_url = "/admin/youtubers/add/"

class ListYoutuberView(ListView):
	document = Youtuber
	template_name = "youtuber/list.html"
	
class DeleteYoutuberView(DeleteView):
	document = Youtuber
	success_url = "/admin/youtubers/"
