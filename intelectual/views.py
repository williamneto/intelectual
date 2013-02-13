# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from intelectual.videos.models import Video

from intelectual.categorias.models import Categoria

class HomePageView(TemplateView):
	
