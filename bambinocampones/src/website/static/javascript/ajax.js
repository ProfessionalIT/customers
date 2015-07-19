function ajax(url, callback_function) { 
    req = null; 
    // Procura por um objeto nativo (Mozilla/Safari) 
    if (window.XMLHttpRequest) { 
        req = new XMLHttpRequest(); 
        req.onreadystatechange = processReqChange(callback_function); 
        req.open("GET",url,false); 
        req.send(null); 
    // Procura por uma versão ActiveX (IE) 
    } else if (window.ActiveXObject) { 
        req = new ActiveXObject("Microsoft.XMLHTTP"); 
        if (req) { 
            req.onreadystatechange = processReqChange(callback_function); 
            req.open("GET",url,false); 
            req.send(); 
        } 
    } 
}
function processReqChange(callback_function){ 
    if (req.readyState == 4) { 
        if (req.status ==200) { 
            var ret = req.responseText;
            if (ret=="OK"){
                callback_function(ret);
            } else {
                //alert("Houve um problema ao obter os dados:n" + req.statusText); 
                //alert(req.statusText); 
            }
        } else {
            
        } 
    } 
}
