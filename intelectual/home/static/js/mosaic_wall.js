videos_elements = [];

$.SetMosaicWall = function(){
	$("#main_wall").fadeOut();
	$("#mosaic_wall").fadeOut();
	$("#mosaic_wall").html(" ");
	
	$.getJSON(
		".",
		{"cmd": "get_initial_wall"},
		function(data){
			for(i=0;  i< data.length; i++){
				object = data[i][0];
				
				if(object.videos.length != 0){
					videos = object.videos;
					for(c=0; c < videos.length; c++){
						video = videos[c];
						thumbnail = "<div class='mosaic_image_container'><img src='"+video.thumbnail+"' class='mosaic_image' title='"+video.titulo+"' width='250' height='141'><p>"+ video.titulo +"<br><span style='margin-bottom: 1px;'><a href='"+ video.youtuber.chanel +"'>"+ video.youtuber.yt_user +"</a> em "+ video.categoria +"</span></p></div>";
						thumbnail_element = $(thumbnail);
						
						videos_elements.push(thumbnail_element);
					}
				}
			}
			
			center = $("<center></center>");
			content = $("#mosaic_wall");
			center.appendTo(content);
			for(i=0; i < videos_elements.length; i++){
				videos_elements[i].appendTo(center);
			}			
		}
	)
	
	$("#mosaic_wall").fadeIn();	
}
