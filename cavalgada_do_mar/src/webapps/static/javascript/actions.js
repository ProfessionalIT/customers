//var app_root_path = "http://app.cavalgadadomar.art.br";
var app_root_path = "http://localhost:8080";
//special_links = ['/patrocinadores', '/depoimentos', '/noticias', 'boletins', '/noticia/', '/boletim/'];
special_links = ['/patrocinadores', '/depoimentos'];

jQuery(document).ready(function() {
    
    jQuery('#slide').cycle({ 
        fx:      'fade',
        timeout: 4000,
        random:  1 
    });

    jQuery("#loading").hide();

    //jQuery('.menu a').live('click', function(){

        //var href = jQuery(this).attr('href');

        //var data_type = '';
        //var full_url = '';
        
        //var is_external_url = href.indexOf('http://') >= 0;

        //if (special_links.indexOf(href) >= 0) {
            //data_type = 'json';
            //full_url = app_root_path + "/getJSON/" + href;
        //} else {
            //data_type = 'html';
            //if (is_external_url) {
                //full_url = href;
            //} else {
                //full_url = app_root_path + href;
            //}
        //}
        //data_type = 'json';
        //// Dummie Debug 1 :(
        //alert('href: ' + href + ' is_external_url: ' + is_external_url + ' data_type: ' + data_type + ' full_url: ' + full_url);
        //jQuery.ajax({
            //url : full_url,
            //type: 'GET',
            //dataType : data_type,
            //async: true,
            //beforeSend: function () {
                //jQuery("#loading").show();
            //},
            //success : function(data) {
                //if (data_type == 'html'){
                    //if (data) {
                        //// Dummie Debug 2 :(
                        //alert(data[0]);
                        //jQuery('#content').html(data);
                    //} else {
                        //jQuery('#content').html("<span id='error_message'>Erro ao obter os dados !.</span>");
                    //}
                //} else {
                    //if (data) {
                        //// Dummie Debug 2 :(
                        //alert(data[0]);
                        //jQuery('#content').html(data);
                    //} else {
                        //jQuery('#content').html("<span id='error_message'>Erro ao obter os dados !.</span>");
                    //}
                //}
                //jQuery("#loading").hide(); 
            //}
        //});
        //return false;
    //});
});

 
  
