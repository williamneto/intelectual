# -*- coding: utf-8 -*-

from mongotools.forms import *

from .models import Video

class AddVideoForm(MongoForm):	
	class Meta:
		document = Video
		exclude = ("views", )
