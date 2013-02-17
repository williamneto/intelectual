# -*- coding: utf-8 -*-
from mongoengine import *

class Youtuber(Document):
	yt_user = StringField(
		required=True,
		verbose_name="YouTube username",
		max_length=50
	)
	
	@property
	def chanel(self):
		return "http://youtube.com/user/" + self.yt_user
	
	def __unicode__(self):
		return self.yt_user
