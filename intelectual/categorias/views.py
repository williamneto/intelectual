# -*- coding: utf-8 -*-
from mongotools.views import CreateView, ListView, UpdateView, DeleteView

from .models import Categoria
from .forms import AddCategoriaForm

class ListCategoriaView(ListView):
	document = Categoria
	template_name = "categoria/list.html"

class AddCategoriaView(CreateView):
	model = Categoria
	form_class = AddCategoriaForm
	template_name = "categoria/form.html"
	success_url = "/admin/categorias/add/"

class UpdateCategoriaView(UpdateView):
	document = Categoria
	form_class = AddCategoriaForm
	template_name = "categoria/form.html"
	success_url = "/admin/categorias/"

class DeleteCategoriaView(DeleteView):
	document = Categoria
	success_url = "/admin/categorias/"


