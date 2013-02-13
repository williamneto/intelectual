# -*- coding: utf-8 -*-
from mongotools.views import CreateView

from .models import Categoria
from .forms import AddCategoriaForm

class AddCategoriaView(CreateView):
	model = Categoria
	form_class = AddCategoriaForm
	template_name = "categoria/form.html"
	success_url = "/admin/add_categoria/"
