# -*- coding: utf-8 -*-
from django.db import models

from intelectual.categorias.models import Categoria
from intelectual.youtubers.models import Youtuber

from gdata.youtube.service import YouTubeService

class Video(models.Model):
	yt_id = models.CharField(
		blank=False,
		max_length=30,
		verbose_name="ID do YouTube"
	)
	
	titulo = models.CharField(
		blank=False,
		max_length=300
	)
	
	categoria = models.ForeignKey(
		Categoria,
		blank=False
	)
	
	youtuber = models.ForeignKey(
		Youtuber,
		blank=False
	)
	
	@property
	def url(self):
		return "/video/" + self.yt_id
	
	@property
	def youtube_url(self):
		return "http://youtube.com/watch?v=" + self.yt_id
	
	@property
	def thumbnail_default(self):
		return "http://i1.ytimg.com/vi/"+self.yt_id+"/mqdefault.jpg"
	
	@property
	def thumbnail_full_size(self):
		return "http://i1.ytimg.com/vi/"+self.yt_id+"/0.jpg"
	
	@property
	def iframe_url(self):
		return "http://www.youtube.com/embed/" + self.yt_id
	
	def get_iframe(self):
		return "<iframe width=\"640\" height=\"375\" src=\"%s\" frameborder=\"0\" allowfullscreen></iframe>" % self.iframe_url
	
	def to_json(self):
		data = {
			'titulo': self.titulo,
			'url': self.youtube_url,
			'iframe': self.get_iframe(),
			'thumbnail': self.thumbnail_default,
			'youtube_url': self.youtube_url,
			'categoria': self.categoria.nome
		}
		
		if self.youtuber:
			data['youtuber'] = self.youtuber.to_json()
		
		return data


