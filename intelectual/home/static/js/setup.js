function Setup(){
    initial_wall = {};
    categorias = [];
    
    wall_category_index = 0
    wall_video_index = 0;
    
    that = this;
    
    this.NextWallVideo = function(){
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
    
    this.PreviousWallVideo =$.PreviousWallVideo = function(){
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
    
    this.SetButtons = function(){
        $("#botoes_container").html(" ")
       	buttons_template = _.template($("#botoes_template").text());
        buttons = $(buttons_template(categorias));
        
        buttons.hide();
        buttons.appendTo($("#botoes_container"));
        buttons.fadeIn();
    };
    
    this.SetMainWall = function(index){
	    wall_category_index = index;
	    wall_video_index  = 0;
	    categoria_inicial = initial_wall[index][0];
	    videos = categoria_inicial.videos;
			
	    video_inicial = videos[0];
	    if(video_inicial != undefined){
	        video_iframe = $(video_inicial.iframe);
	
	        container = $("#video_inicial_container");
	        container.hide();
	        $("#video_inicial_container").html(video_iframe);
	        container.fadeIn();
	    }
    }
    
    $.getJSON(
        ".",
        {"cmd": "get_initial_wall"},
        function(data){
            initial_wall = data;
            
            for (i=0; i < initial_wall.length; i++){
                object = initial_wall[i][0];
                index = 0;
                if (object.videos.length != 0){
                    if (index==0){
                        index = 1;
                    }
                    categoria = {
                        'id': object.id,
                        'index': i,
                        'nome': object.nome,
                        'botao_imagem': object.botao_imagem
                    }
                    categorias.push(categoria)
                }
            }
            that.SetMainWall(index);
            that.SetButtons();
        });
}
