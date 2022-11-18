var isActivate = false;

function menuClick(bool){
    var menu = document.getElementById('button-menu');
    if(isActivate == true){
        isActivate = false
        document.getElementById('menu-background').style.opacity = 0;
        document.getElementById('menu-background').style.zIndex = -2;
        if(bool == false){
            document.getElementById('menu-img').style.filter = 'invert(0%) sepia(0%) saturate(7%) hue-rotate(253deg) brightness(103%) contrast(100%)';
        } else {
            document.getElementById('menu-img').style.filter = 'invert(100%) sepia(62%) saturate(0%) hue-rotate(214deg) brightness(105%) contrast(108%)';
        } 
    } else {
        isActivate = true
        document.getElementById('menu-background').style.opacity = 1;
        document.getElementById('menu-background').style.zIndex = 10;
        if(bool == true){
            document.getElementById('menu-img').style.filter = 'invert(0%) sepia(0%) saturate(7%) hue-rotate(253deg) brightness(103%) contrast(100%)';
        } else {
            document.getElementById('menu-img').style.filter = 'invert(100%) sepia(62%) saturate(0%) hue-rotate(214deg) brightness(105%) contrast(108%)';
        }  
    }
    
}