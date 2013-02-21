initial_wall = {};
categorias = [];

wall_category_index = 0;
wall_video_index = 0;

$.NextWallVideo = function(){
	categoria = initial_wall[wall_category_index][0];
	videos = categoria.videos;
	
	if(wall_video_index < videos.length-1 ){
		wall_video_index = wall_video_index + 1;
		video = videos[wall_video_index];
		
		video_iframe = $(video.iframe);
		container.hide();
		$("#video_inicial_container").html(video_iframe);
		container.fadeIn();
	}
};
$.PreviousWallVideo = function(){
	categoria = initial_wall[wall_category_index][0];
	videos = categoria.videos;
	
	if(wall_video_index > 0 ){
		wall_video_index = wall_video_index - 1;
		video = videos[wall_video_index];
		
		video_iframe = $(video.iframe);
		container.hide();
		$("#video_inicial_container").html(video_iframe);
		container.fadeIn();
	}	
}

$.SetCategoriaWall = function(index){
	wall_category_index = index;
	wall_video_index  = 0;
	categoria_inicial = initial_wall[index][0];
	videos = categoria_inicial.videos;
			
	video_inicial = videos[0];
	video_iframe = $(video_inicial.iframe);
	
	container = $("#video_inicial_container");
	container.hide();
	$("#video_inicial_container").html(video_iframe);
	container.fadeIn();
};

$.SetButtons = function(){
	buttons_template = _.template($("#botoes_template").text());
	buttons = $(buttons_template(categorias));
	
	buttons.hide();
	buttons.appendTo($("#botoes_containter"));
	buttons.fadeIn();
};

$.Setup = function(){	
	$.getJSON(
		".",
		{"cmd": "get_initial_wall"},
		function(data){
			initial_wall = data;			
			
			for(i=0; i < initial_wall.length; i++){
				object = initial_wall[i][0];
				
				if(object.videos.length != 0){
					categoria = {
						'id': object.id,
						'index': i,
						'nome': object.nome,
						'botao_imagem': object.botao_imagem
					}
					categorias.push(categoria);
				}
			}
			$.SetButtons();
			$.SetCategoriaWall(0);					
		}
	)	
}

$(document).ready(function(){
	$.Setup();
	
	$("#action_previous").click(function(){
		$.PreviousWallVideo();
	});
	
	$("#action_next").click(function(){
		$.NextWallVideo();
	});
});

$(document).delegate("img.botao_imagem", "click", function(){
	index = this.id;	
	$.SetCategoriaWall(parseInt(index));
});
