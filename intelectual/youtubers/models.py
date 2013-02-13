# -*- coding: utf-8 -*-
from mongoengine import *

from intelectual.categorias.models import Categoria

class Youtuber(Document):
	yt_user = StringField(
		required=True,
		verbose_name="YouTube username",
		max_length=50
	)
	
	categoria = ReferenceField(
		Categoria,
		dbref=True
	)
	
	@property
	def chanel(self):
		return "http://youtube.com/user/" + self.yt_user
	
	def __unicode__(self):
		return self.yt_user
