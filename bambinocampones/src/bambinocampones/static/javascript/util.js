function setMessage(msg) {
    div_msg = document.getElementById('message_product');
    div_msg.innerHTML = "<span class='message_content'>" + msg + "</span>";
}


function unSetMessage() {
    div_msg = document.getElementById('message_product');
    div_msg.innerHTML = '';
}


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
    retorno = false;
    if(((email.search(exclude) != -1)||(email.search(check)) == -1)||(email.search(checkend) == -1)) {
        retorno = false;
    } else {
        retorno = true;
    }
    return retorno;
}


function valida_contato(){

    obj_nome = document.getElementById('nome');
    obj_mail = document.getElementById('mail_contato');
    obj_telefone = document.getElementById('telefone');
    obj_assunto = document.getElementById('assunto');
    obj_mensagem = document.getElementById('mensagem');
    obj_form = document.getElementById('contato');

    if (obj_nome.value == '') {
        alert("Para o envio do Contato, o nome precisa ser informado !");
        obj_nome.focus();
        return false;
    }

    if (obj_telefone.value == '') {
        alert("Para o envio do Contato, o telefone precisa ser informado !");
        obj_telefone.focus();
        return false;
    }

    if (obj_mail.value == '') {
        alert("Para o envio do Contato, um e-mail válido precisa ser informado.");
        obj_mail.focus();
        return false;
    }

    if (! IsEmail(obj_mail.value)) {
        alert("Para o envio do Contato, um e-mail válido precisa ser informado.");
        obj_mail.focus();
        return false;
    }

    if (obj_assunto.value == '') {
        alert("Para o envio do Contato, o assunto precisa ser informado !");
        obj_assunto.focus();
        return false;
    }

    if (obj_mensagem.value == '') {
        alert("Para o envio do Contato, a mensagem precisa ser informada !");
        obj_mensagem.focus();
        return false;
    }

    var why = "";

    if (obj_form.txtInput.value == "") {
        why += "- Código de Segurança não pode ser vázio !.\n";
    }

    if (obj_form.txtInput.value != "") {
        if (ValidCaptcha(obj_form.txtInput.value) == false) {
            why += "- Código de Segurança não confere !.\n";
        }
    }

    if (why != "") {
        alert(why);
        return false;
    }

    obj_form.submit();
    return true;
}

function valida_orcamento(){

    obj_razao_social_nome = document.getElementById('razao_social_nome');
    obj_cnpj_cpf = document.getElementById('cnpj_cpf');
    obj_telefone = document.getElementById('telefone');
    obj_mail_orcamento = document.getElementById('mail_orcamento');
    obj_produto = document.getElementById('produto');
    obj_outro_produto = document.getElementById('outro_produto');
    obj_formato_aberto = document.getElementById('formato_aberto');
    obj_formato_fechado = document.getElementById('formato_fechado');
    obj_quantidade = document.getElementById('quantidade');
    obj_tipo_papel = document.getElementById('tipo_papel');
    obj_cores = document.getElementById('cores');
    obj_gramatura = document.getElementById('gramatura');
    obj_capa = document.getElementById('capa');
    obj_formato_capa = document.getElementById('formato_capa');
    obj_papel_capa = document.getElementById('papel_capa');
    obj_gramatura_capa = document.getElementById('gramatura_capa');
    obj_cores_capa = document.getElementById('cores_capa');
    obj_orelha_capa = document.getElementById('orelha_capa');
    obj_miolo = document.getElementById('miolo');
    obj_formato_miolo = document.getElementById('formato_miolo');
    obj_papel_miolo = document.getElementById('papel_miolo');
    obj_gramatura_miolo = document.getElementById('gramatura_miolo');
    obj_cores_miolo = document.getElementById('cores_miolo');
    obj_quantidade_pagina_miolo = document.getElementById('quantidade_pagina_miolo');
    obj_platificacao_fosca_acabamento = document.getElementById('platificacao_fosca_acabamento');
    obj_numercacao_acabamento = document.getElementById('numercacao_acabamento');
    obj_plastificacao_brilho_acabamento = document.getElementById('plastificacao_brilho_acabamento');
    obj_colagem_capa_acabamento = document.getElementById('colagem_capa_acabamento');
    obj_plastificacao_bopp_fosca_acabamento = document.getElementById('plastificacao_bopp_fosca_acabamento');
    obj_dobras_acabamento = document.getElementById('dobras_acabamento');
    obj_numero_dobras_acabamento = document.getElementById('numero_dobras_acabamento');
    obj_plastificacao_bopp_brilho_acabamento = document.getElementById('plastificacao_bopp_brilho_acabamento');
    obj_encardenacao_acabamento = document.getElementById('encardenacao_acabamento');
    obj_verniz_uv_localizado_acabamento = document.getElementById('verniz_uv_localizado_acabamento');
    obj_wiro_acabamento = document.getElementById('wiro_acabamento');
    obj_verniz_total_acabamento = document.getElementById('verniz_total_acabamento');
    obj_aspiral_acabamento = document.getElementById('aspiral_acabamento');
    obj_hot_melt_acabamento = document.getElementById('hot_melt_acabamento');
    obj_sem_arte = document.getElementById('sem_arte');
    obj_com_arte = document.getElementById('com_arte');
    obj_tipo_arte = document.getElementById('tipo_arte');
    obj_arquivo_arte = document.getElementById('arquivo_arte');
    obj_com_prova_digital = document.getElementById('com_prova_digital');
    obj_sem_prova_digital = document.getElementById('sem_prova_digital');
    obj_prazo_de_entrega = document.getElementById('prazo_de_entrega');
    obj_forma_de_entrega = document.getElementById('forma_de_entrega');
    obj_forma_pagamento = document.getElementById('forma_pagamento');
    obj_informacoes_complementares = document.getElementById('informacoes_complementares');

    obj_form = document.getElementById('orcamento');

    if (obj_razao_social_nome.value == '') {
        alert("Para o envio do Orçamento, a empresa/nome precisa ser informado !");
        obj_razao_social_nome.focus();
        return false;
    }

    if (obj_cnpj_cpf.value == '') {
        alert("Para o envio do Orçamento, o CNPJ/CPF precisa ser informado !");
        obj_cnpj_cpf.focus();
        return false;
    }

    if (obj_telefone.value == '') {
        alert("Para o envio do Orçamento, o telefone precisa ser informado !");
        obj_telefone.focus();
        return false;
    }

    if (obj_mail_orcamento.value == '') {
        alert("Para o envio do Orçamento, um e-mail precisa ser informado !");
        obj_mail_orcamento.focus();
        return false;
    }

    if (! IsEmail(obj_mail_orcamento.value)) {
        alert("Para o envio do Orçamento, um e-mail válido precisa ser informado !");
        obj_mail_orcamento.focus();
        return false;
    }

    if (obj_produto.value == '') {
        alert("Para o envio do Orçamento, o produto precisa ser informado !");
        obj_produto.focus();
        return false;
    }

    if (obj_produto.value == 'outro' && obj_outro_produto.value == '') {
        alert("Para o envio do Orçamento, se for selecionado produto do tipo 'outro', o outro produto precisa ser informado !");
        obj_outro_produto.focus();
        return false;
    }

    if (obj_formato_aberto.value == '') {
        alert("Para o envio do Orçamento, o Formato Aberto (em CM) precisa ser informado !");
        obj_formato_aberto.focus();
        return false;
    }

    if (obj_formato_fechado.value == '') {
        alert("Para o envio do Orçamento, o Formato Fechado (em CM) precisa ser informado !");
        obj_formato_fechado.focus();
        return false;
    }

    if (obj_quantidade.value == '') {
        alert("Para o envio do Orçamento, a Quantidade precisa ser informada !");
        obj_quantidade.focus();
        return false;
    }

    if (obj_tipo_papel.value == '') {
        alert("Para o envio do Orçamento, o Tipo de Papel precisa ser informado !");
        obj_tipo_papel.focus();
        return false;
    }

    if (obj_cores.value == '') {
        alert("Para o envio do Orçamento, a Cores precisam ser informadas !");
        obj_cores.focus();
        return false;
    }

    if (obj_gramatura.value == '') {
        alert("Para o envio do Orçamento, a Gramatura do Papel precisa ser informada !");
        obj_gramatura.focus();
        return false;
    }

    if (obj_dobras_acabamento.checked) {
        if (obj_numero_dobras_acabamento.value == ''){
            alert("Para o envio do Orçamento, Se Dobras for selecionada, o Número de Dobras precisa ser informado !");
            obj_numero_dobras_acabamento.focus();
            return false;
        }
    }

    if (obj_com_arte.checked) {
        if (obj_tipo_arte.value == ''){
            alert("Para o envio do Orçamento, Se Com Arte for selecionada, o Tipo de Arte precisa ser informado !");
            obj_tipo_arte.focus();
            return false;
        }
        if (obj_arquivo_arte.value == ''){
            alert("Para o envio do Orçamento, Se Com Arte for selecionada, o Arquivo com a Arte precisa ser informado !");
            obj_tipo_arte.focus();
            return false;
        }
    }

    var why = "";

    if (obj_form.txtInput.value == "") {
        why += "- Código de Verificação não pode ser vázio !.\n";
    }

    if (obj_form.txtInput.value != "") {
        if (ValidCaptcha(obj_form.txtInput.value) == false) {
            why += "- Código de Verificação não confere !.\n";
        }
    }

    if (why != "") {
        alert(why);
        return false;
    }

    obj_form.submit();
    return true;
}


function validaMenuAcesso(){
    retorno = false;
    valor = 'bambino2015';
    var validation = prompt("Informe a senha de acesso:");
    if (validation != null) {
        if (validation == valor){
            retorno = true;
        } else {
            alert("Senha inválida !.");
        }
    } else {
        alert("Senha Não infomada !.");
    }
    return retorno;
}

