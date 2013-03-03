# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Categoria
from .forms import AddCategoriaForm

from intelectual.videos.models import Video

class ListCategoriaView(ListView):
    model = Categoria
    template_name = "categoria/list.html"

class AddCategoriaView(CreateView):
	model = Categoria
	form_class = AddCategoriaForm
	template_name = "categoria/form.html"
	success_url = "/admin/categorias/add/"

class UpdateCategoriaView(UpdateView):
	model = Categoria
	form_class = AddCategoriaForm
	template_name = "categoria/form.html"
	success_url = "/admin/categorias/"

class DeleteCategoriaView(DeleteView):
	model = Categoria
	success_url = "/admin/categorias/"

class CategoriaVideosView(ListView):
	template_name = "categoria/categoria_videos.html"
	
	def get_object(self, *args, **kwargs):
		object = Categoria.objects.get(pk=self.kwargs['pk'])
		return object
	
	def get_queryset(self, *args, **kwargs):
		categoria = self.get_object()
		
		queryset = Video.objects.all().filter(categoria=categoria)
		
		return queryset
	
	def get_context_data(self, *args, **kwargs):
		ctx = super(CategoriaVideosView, self).get_context_data(*args, **kwargs)
		
		ctx['categoria'] = self.get_object()
		
		return ctx
		


