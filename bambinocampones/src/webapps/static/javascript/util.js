//Generates the captcha function   
function generateCode(){
    var a = Math.ceil(Math.random() * 9)+ '';
    var b = Math.ceil(Math.random() * 9)+ '';
    var c = Math.ceil(Math.random() * 9)+ '';
    var d = Math.ceil(Math.random() * 9)+ '';
    var e = Math.ceil(Math.random() * 9)+ '';
    var code = a + b + c + d + e;
    document.getElementById("txtCaptcha").value = code;
    document.getElementById("txtCaptchaDiv").innerHTML = code; 
}
// Validate the Entered input aganist the generated security code function   
function ValidCaptcha(){
	var str1 = removeSpaces(document.getElementById('txtCaptcha').value);
	var str2 = removeSpaces(document.getElementById('txtInput').value);
	if (str1 == str2){
		return true;	
	}else{
		return false;
	}
}

// Remove the spaces from the entered and generated code
function removeSpaces(string){
	return string.split(' ').join('');
}
	

function IsEmail(email){
    var exclude=/[^@\-\.\w]|^[_@\.\-]|[\._\-]{2}|[@\.]{2}|(@)[^@]*\1/;
    var check=/@[\w\-]+\./;
    var checkend=/\.[a-zA-Z]{2,3}$/;
    if(((email.search(exclude) != -1)||(email.search(check)) == -1)||(email.search(checkend) == -1)){return false;}
    else {return true;}
}
function valida_contato(){
    obj_nome = document.getElementById('nome');
    obj_mail = document.getElementById('email');
    obj_telefone = document.getElementById('telefone');
    obj_mensagem = document.getElementById('mensagem');
    obj_form = document.getElementById('contato_form');
    
    if (obj_nome.value=='') { alert("Para o envio do Contato, o nome precisa ser informado !"); return false; }
    if (obj_telefone.value=='') { alert("Para o envio do Contato, o telefone precisa ser informado !"); return false; }
    if (obj_mail.value=='') { alert("Para o envio do Contato, um e-mail válido precisa ser informado !");  return false; }
    if (! IsEmail(obj_mail.value)) { alert("Para o envio do Contato, um e-mail válido precisa ser informado !");  return false; }
    if (obj_mensagem.value=='') { alert("Para o envio do Contato, a mensagem precisa ser informada !"); return false; }
    obj_form.submit();
    return true;
}

