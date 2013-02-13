# -*- coding: utf-8 -*-

from mongotools.views import CreateView, ListView

from intelectual.youtubers.models import Youtuber

from .forms import AddYoutuberForm

class AddYoutuberView(CreateView):
	document = Youtuber
	form_class = AddYoutuberForm
	template_name = "youtuber/form.html"
	success_url = "/admin/youtuber/add/"

class ListYoutuberView(ListView):
	document = Youtuber
	template_name = "youtuber/list.html"
