function Setup(){
    
    var params = {
        "cmd": "get_initial_wall"
    }
    $.getJSON(".", params, function(data){
        video_inicial_container = $("#video_inicial_container");
        video_iframe = $(data[0].iframe);
        video_inicial_container.html(video_iframe);        
    });
}
