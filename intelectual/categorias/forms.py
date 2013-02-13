# -*- coding: utf-8 -*-
from mongotools.forms import *

from .models import Categoria

class AddCategoriaForm(MongoForm):
	class Meta:
		document = Categoria
		
