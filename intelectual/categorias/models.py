# -*- coding: utf-8 -*-
from mongoengine import *

class Categoria(Document):
	nome = StringField(
		required=True,
		max_length=50
	)
	
	descricao = StringField(
		required=True,
		max_length=300
	)
	
	@property
	def url(self):
		return "/categoria/" + self.nome
	
	def __unicode__(self):
		return self.nome
