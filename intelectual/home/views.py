# -*- coding: utf-8 -*-

import random

from django.views.generic import TemplateView
from django.http import HttpResponse, Http404
from django.utils import simplejson

from intelectual.videos.models import Video
from intelectual.categorias.models import Categoria

from .constants import BOTOES_IMAGENS

class HomePageView(TemplateView):
	template_name = "home_page.html"
	get_services = ('get_initial_wall', 'query', )

	def _get_initial_wall(self):
		categorias = Categoria.objects.all()		
		videos_list = []
		for categoria in categorias:
			videos = Video.objects.filter(categoria=categoria)

			if len(videos) > 0:
			    video = random.sample(videos, 1)            
			videos_list.append(video.to_json())

		return HttpResponse(simplejson.dumps(videos_list), content_type="application/json") 
  
	def _query(self):
  		categoria = self.request.GET.get('categoria', None)
  		term = self.request.GET.get('term', None)
  		if categoria and not term:
  			"""
  			Retorna todos os videos de uma categoria
  			"""
  			categoria = Categoria.objects.get(pk=categoria)
  			videos = Video.objects.filter(categoria=categoria)
  			
  			videos_list = []
  			
  			for video in videos:
  				videos_list.append(video.to_json())
  			return HttpResponse(simplejson.dumps(videos_list), content_type="application/json")
        
	        if categoria and term:
	            """
	            Pesquisa por um videos em uma categoria
	            """
	            categoria = Categoria.objects.get(pk=categoria)
	            videos = Video.objects.filter(categoria=categoria)
	
	            videos = videos.filter(titulo__icontains=term)
	
	            videos_list = []
	            for video in videos:
	                videos_list.append(video.to_json())
	            return HttpResponse(simplejson.dumps(videos_list), content_type="application/json")
	
	        raise Http404

	def get(self, *args, **kwargs):
		cmd = self.request.GET.get('cmd')
		if cmd and cmd in self.get_services:
			return getattr(self, '_%s' % cmd)()

		return super(HomePageView, self).get(*args, **kwargs)
    
