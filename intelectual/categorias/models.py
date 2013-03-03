# -*- coding: utf-8 -*-
from django.db import models

import intelectual.videos.models

class Categoria(models.Model):
	nome = models.CharField(
		blank=False,
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
