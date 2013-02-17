# -*- coding: utf-8 -*-
from mongoengine import *

import intelectual.videos.models

class Categoria(Document):
	nome = StringField(
		required=True,
		max_length=50
	)
	
	@property
	def url(self):
		return "/categoria/" + self.nome
	
	@property
	def num_videos(self):
		num_videos = intelectual.videos.models.Video.objects.all().filter(categoria=self).count()
		
		return num_videos
	
	def __unicode__(self):
		return self.nome
