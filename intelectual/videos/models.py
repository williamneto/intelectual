# -*- coding: utf-8 -*-
from mongoengine import *

from intelectual.categorias.models import Categoria
from intelectual.youtubers.models import Youtuber

class Video(Document):
	yt_id = StringField(
		required=True,
		max_length=10,
		verbose_name="ID do YouTube"
	)
	
	titulo = StringField(
		required=True,
		max_length=50,
		verbose_name="Título"
	)
	
	categoria = ReferenceField(
		Categoria,
		dbref=True,
		required=True
	)
	
	youtuber = ReferenceField(
		Youtuber,
		dbref=True,
		required=False
	)
	
	views = IntField(
		required=True,
		default=0
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
		return "<iframe width=\"180\" height=\"160\" src=\"%s\" frameborder=\"0\" allowfullscreen></iframe>" % self.iframe_url


