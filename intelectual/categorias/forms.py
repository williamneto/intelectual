# -*- coding: utf-8 -*-
from django.forms import ModelForm

from .models import Categoria

class AddCategoriaForm(ModelForm):
	class Meta:
		model = Categoria
		
