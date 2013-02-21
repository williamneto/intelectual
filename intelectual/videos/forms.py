# -*- coding: utf-8 -*-

from mongotools.forms import *

from .models import Video

from gdata.youtube.service import YouTubeService

class AddVideoForm(MongoForm):	
	class Meta:
		document = Video
		exclude = ("views", "titulo")
	
	def save(self, *args, **kwargs):
		obj = super(AddVideoForm, self).save(commit=False)
		
		if kwargs.get('commit',True):			
			yt_service = YouTubeService()
			entry = yt_service.GetYouTubeVideoEntry(video_id=obj.yt_id)
			
			obj.titulo = entry.media.title.text
			obj.descricao = entry.media.description.text			
			
			obj.save()
		
		return obj
