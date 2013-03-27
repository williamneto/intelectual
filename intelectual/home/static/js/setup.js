function Setup(){
    _instance = this;
    
    WALL_LIST = [];
    WALL_INDEX = 0;
    
    this.setWallList = function(wallList){
        WALL_LIST = wallList;
    }    
    this.getWallList = function(){
        return WALL_LIST;
    }
    
    this.setWallIndex = function(i){
        WALL_INDEX = i;
    }
    this.getWallIndex = function(i){
        return WALL_INDEX;
    }
    
    this.show = function(){
        var wall = _instance.getWallList();
        var i = _instance.getWallIndex();        
        
        if (i <= wall.length){
            var video = wall[i];
            
            video_inicial_container = $("#video_inicial_container");
            video_iframe = $(video.iframe);
            video_inicial_container.html(video_iframe);
        }
    }
    this.next = function(){
        var i = _instance.getWallIndex() + 1;
        
        _instance.setWallIndex(i);      
        _instance.show();
    }
    this.prev = function(){
        var i = _instance.getWallIndex() - 1;
        
        _instance.setWallIndex(i);      
        _instance.show();
    }
}
