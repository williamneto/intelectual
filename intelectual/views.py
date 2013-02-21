# -*- coding: utf-8 -*-

import random

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils import simplejson

from intelectual.videos.models import Video
from intelectual.categorias.models import Categoria
from intelectual.common.constants import BOTOES_IMAGENS

class HomePageView(TemplateView):
	template_name = "home_page.html"
	get_services = ('get_initial_wall', )
	
	def _get_initial_wall(self):
		categorias = Categoria.objects.all()
		
		categorias_videos = []
		for categoria in categorias:
			videos = Video.objects.filter(categoria=categoria)
			
			if len(videos) > 4:
				videos = random.sample(videos, 4)
			
			videos_json = []
			for video in videos:
				video = video.to_json()
				videos_json.append(video)
			
			json = [{
			    'nome': categoria.nome,
			    'id': str(categoria.pk),
			    'videos': videos_json,
			    'botao_imagem': BOTOES_IMAGENS[categoria.nome]
			 }]
							
			categorias_videos.append(json)
		
		return HttpResponse(simplejson.dumps(categorias_videos), content_type="application/json")
		
	
	def get(self, *args, **kwargs):
		cmd = self.request.GET.get('cmd')
		if cmd and cmd in self.get_services:
			return getattr(self, '_%s' % cmd)()
		
		return super(HomePageView, self).get(*args, **kwargs)
			
		
