# -*- coding: utf-8 -*-

from mongotools.forms import MongoForm

from .models import Youtuber

class AddYoutuberForm(MongoForm):
	class Meta:
		document = Youtuber
