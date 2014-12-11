function construction(){
    alert("Rotina em desenvolvimento !.");
    return false;
}
function clean_search(criteria_value, value_field) {
    if (criteria_value == "all") { value_field.value = "";}
}
function popup(url) {
    var width  = 1100;
    var height = 650;
    var left   = (screen.width  - width)/2;
    var top    = (screen.height - height)/2;
    var params = 'width='+width+', height='+height;
    params += ', top='+top+', left='+left;
    params += ', directories=0';
    params += ', location=0';
    params += ', menubar=0';
    params += ', resizable=0';
    params += ', status=0';
    params += ', toolbar=0';
    newwin = window.open(url,'windowname5', params);
    if (window.focus) { newwin.focus() }
    return false;
}
function detect_edit_mode(){
    var url = window.location;
    url = url.toString()
    if (url.indexOf('editar') != -1) {
        urlCont = url.split("/");
        ajax_url = "/admin/set-unlocked/" + urlCont[5] + "/" + urlCont[6].substring(0,urlCont[6].length-2);
        set_unlocked(ajax_url);
    }
}
function set_unlocked(action){
    ajax_url = action;
    ajax(ajax_url, callback_function());
}
function callback_function(status){  }

function preview(){
    var url = window.location;
    url = url.toString()
    urlCont = url.split("/");
    var str_path = '/admin/preview/' + urlCont[5] + '/' + document.getElementById('slug').value;
    window.open(str_path,'_blank')
    return false;
}
function setMode(mode){
    document.operation_form.operation.value=mode;
    if (mode == 'delete'){ if (confirm('Deseja Realmente excluir o registro ?')) { return true; } else { return false; } } else { return true; }
}
bajb_backdetect.OnBack = function() {
    detect_edit_mode();
}
function set_buttons(){
    var has_id = jQuery('#id').val();
    if(has_id == ''){
        jQuery("#salvar_button").attr('disabled', 'disabled');
        jQuery("#excluir_button").attr('disabled', 'disabled');
        jQuery("#publicar_button").attr('disabled', 'disabled');
        jQuery("#visualizar_button").attr('disabled', 'disabled');
    } else {
        jQuery("#salvar_button").attr('disabled', '');
        jQuery("#excluir_button").attr('disabled', '');
        jQuery("#publicar_button").attr('disabled', '');
        var field_draft = jQuery('#draft').val();
        if(field_draft == 'N'){
            jQuery("#visualizar_button").attr('disabled', 'disabled');
            jQuery("#publicar_button").attr('disabled', 'disabled');
        }else{
            jQuery("#visualizar_button").attr('disabled', '');
            jQuery("#publicar_button").attr('disabled', '');
        }
    }
}
function showTemplate(obj){
    if (confirm('Deseja visualizar o template ?')){
        urlImagem = "/admin/show-template/" + obj.value;
        window.open(urlImagem,'Foto_Ampliada','toolbar=no,location=no,status=no,menubar=no,scrollbars=no,resizable=no,width=400,height=400');
    }
}
