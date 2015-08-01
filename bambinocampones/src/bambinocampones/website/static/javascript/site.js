if (!document.getElementsByClassName) {
    document.getElementsByClassName = function(cl) {
        var retnode = [];
        var myclass = new RegExp('\\b'+cl+'\\b');
        var elem = this.getElementsByTagName('*');
        for (var i = 0; i < elem.length; i++) {
            var classes = elem[i].className;
            if (myclass.test(classes)) retnode.push(elem[i]);
        }
        return retnode;
        };
}
function restore_default_menu_color(){
    var obj = document.getElementById('menu_list');
    var elements = obj.getElementsByTagName('a');
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.color = '#fff';
    }
}
function hide_sub_menus(){
    var objs = document.getElementsByClassName('sub_menu');
    for (var i = 0; i < objs.length; i++) {
        objs[i].style.display = 'none';
    }
}
function show_element(parent, element){
    var obj = document.getElementById(element);
    if (obj.style.display=='block') {
        restore_menu();
    } else {
        hide_sub_menus();
        restore_default_menu_color();
        parent.style.color='#eee';
        obj.style.display='block';
    }
    return false;
}
function restore_menu(){
    hide_sub_menus();
    restore_default_menu_color();    
}
