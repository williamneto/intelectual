# -*- coding: utf-8 -*-
from mongotools.views import CreateView, ListView

from .models import Categoria
from .forms import AddCategoriaForm

class ListCategoriaView(ListView):
	document = Categoria
	template_name = "categoria/list.html"

class AddCategoriaView(CreateView):
	model = Categoria
	form_class = AddCategoriaForm
	template_name = "categoria/form.html"
	success_url = "/admin/categoria/add/"
