function IsEmail(email){
    var exclude=/[^@\-\.\w]|^[_@\.\-]|[\._\-]{2}|[@\.]{2}|(@)[^@]*\1/;
    var check=/@[\w\-]+\./;
    var checkend=/\.[a-zA-Z]{2,3}$/;
    if(((email.search(exclude) != -1)||(email.search(check)) == -1)||(email.search(checkend) == -1)){return false;}
    else {return true;}
}

function valida_contato(){
    obj_nome = document.getElementById('nome_contato');
    obj_mail = document.getElementById('email_contato');
    obj_telefone = document.getElementById('telefone_contato');
    obj_mensagem = document.getElementById('mensagem_contato');
    obj_form = document.getElementById('contato_form');
    if (obj_nome.value=='') { alert("Para o envio do Contato, o nome precisa ser informado !"); return false; }
    if (obj_mail.value=='') { alert("Para o envio do Contato, um e-mail válido precisa ser informado !");  return false; }
    if (! IsEmail(obj_mail.value)) { alert("Para o envio do Contato, um e-mail válido precisa ser informado !");  return false; }
    if (obj_telefone.value=='') { alert("Para o envio do Contato, o telefone precisa ser informado !"); return false; }
    if (obj_mensagem.value=='') { alert("Para o envio do Contato, a mensagem precisa ser informada !"); return false; }
    obj_form.submit();
    return true;
}
