# -*- coding: utf-8 -*-
from django.db import models

class Youtuber(models.Model):
	yt_user = models.CharField(
		blank=False,
		verbose_name="YouTube username",
		max_length=50
	)
	
	@property
	def chanel(self):
		return "http://youtube.com/user/" + self.yt_user
	
	def __unicode__(self):
		return self.yt_user
	
	def to_json(self):
	    data = {
            'yt_user': self.yt_user,
            'chanel': self.chanel
        };return data
