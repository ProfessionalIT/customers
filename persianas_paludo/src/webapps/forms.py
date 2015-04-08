#!/usr/bin/python
# -*- coding: utf-8 -*-
from web import form
import model

# Commons Validators Expressions
vemail = form.regexp("^([0-9a-zA-Z]+([_.-]?[0-9a-zA-Z]+)*@[0-9a-zA-Z]+[0-9,a-z,A-Z,.,-]*(.){1}[a-zA-Z]{2,4})+$", "Precisa ser um endereco de e-mail válido !.")
vdigito = form.regexp("\d+", "Precisa ser um digito")
vmoeda = form.regexp("^\d{1,5}(\.\d{1,2})?$", "Precisa ser um valor inteiro OU com duas casas decimais !")
vdata =  form.regexp("^(((0[1-9]|[12][0-9]|3[01])([/])(0[13578]|10|12)([/])(\d{4}))|(([0][1-9]|[12][0-9]|30)([/])(0[469]|11)([/])(\d{4}))|((0[1-9]|1[0-9]|2[0-8])([/])(02)([/])(\d{4}))|((29)(\.|-|\/)(02)([/])([02468][048]00))|((29)([/])(02)([/])([13579][26]00))|((29)([/])(02)([/])([0-9][0-9][0][48]))|((29)([/])(02)([/])([0-9][0-9][2468][048]))|((29)([/])(02)([/])([0-9][0-9][13579][26])))$", "Precisa ser uma data no formato dd/mm/yyyy !")
vdatafull =  form.regexp("^\d{4}-([\d]|0[0-9]|1[0,1,2])-([0-9]|[0,1,2][0-9]|3[0,1]) ([0-1][0-9]|[2][0-3])(:([0-5][0-9])){1,2}(:([0-5][0-9])){1,2}$", "Precisa ser uma data e hora no formato yyyy-mm-dd hh:mm:ss !")
vurl = form.regexp("^(http[s]?://|ftp://)?(www\.)?[a-zA-Z0-9-\.]+\.(com|org|net|mil|edu|ca|co.uk|com.au|gov|br)$", "Precisa ser um endereço Web Válido !.")
vtelefone = form.regexp("^\(?\d{2}\)?[\s-]?\d{4}-?\d{4}$", "Precisa ser um telefone no formato (99) 9999-9999")
vcep = form.regexp("^[0-9]{2}\.[0-9]{3}-[0-9]{3}$", "Precisa estar no formato 99.999-999 !")
vcnpj = form.regexp("\d{2,3}.\d{3}.\d{3}/\d{4}-\d{2}", "Precisa estar no formato 99.999.999/9999-99 !")

# App Forms
def getSearchForm(fields):
    _form = form.Form(
            form.Dropdown('campo', fields, description='Campo:', onblur='clean_search(this.value, valor);', onclick='clean_search(this.value, valor);' ),
            form.Dropdown('criterio', [('=', '='), ('!=', '!='), (' LIKE ', ' LIKE ')], description='Critério:'),
            form.Textbox('valor', size=20, description="Valor:"),
            form.Button('Pesquisa', html="Pesquisar", type="submit"),
            form.Dropdown('resultados', [('10', '10'), ('50', '50'), ('100', '100')], onchange='form.submit()',description='Qtde Registros:'),
    )
    return _form

def getUsuarioForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('login', vemail, size="60", maxlength="250", title="E-mail de Login do Usuario.", description='Login:'),
        form.Password('senha', form.notnull, size="60", maxlength="08", title="Senha com 08 digitos.", description='Senha (08 digitos):'),
        form.Dropdown('nivel_acesso', [('1', 'Administrador'), ('2', 'Operador'), ('3', 'Visitante')], title="Nivel de Acesso do Usuario", description='Nível de Acesso:')
    )
    return _form

def getPaginaForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome da Página.", description='Titulo:'),
        form.Textbox('slug', size="60", maxlength="250", title="URL da Página.", readonly="readonly", class_="readonly", description='URL da Página:'),
        form.Textbox('descricao_completa', form.notnull, size="60", maxlength="250", title="Descrição Completa da Página.", description='Descrição Completa:'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlength="250", title="Palavras Chaves da Página separadas por vírgula.", description='Palavras Chaves:'),
        form.Textarea('conteudo', form.notnull, cols="70", rows="25", title="Conteúdo da Página.", description='Conteúdo da Página:')
    )
    return _form

def getProdutoForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome do Produto.", description='Titulo:'),
        form.Textbox('slug', size="60", maxlength="250", title="URL da Página.", readonly="readonly", class_="readonly", description='URL do Produto:'),
        form.Textarea('caracteristicas', form.notnull, cols="70", rows="25", title="Caracteristicas do Produto.", description='Características:'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlength="250", title="Palavras Chaves do Produto separadas por vírgula.", description='Palavras Chaves:'),
        form.Textbox('url_galeria', form.notnull, size="60", maxlength="250", title="Nome da Galeria de fotos.", description='Nome da Galeria:')
    )
    return _form

def getPromocaoForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome da Promoção.", description='Titulo:'),
        form.Textbox('slug', size="60", maxlength="250", title="URL da Página.", readonly="readonly", class_="readonly", description='URL da Promoção:'),
        form.Textarea('conteudo', form.notnull, cols="70", rows="25", title="Conteúdo da Página.", description='Conteúdo da Página:'),
        form.Dropdown('ativo', [('S', 'Sim'), ('N', 'Nao')], title="Promoção Ativa ?", description='Ativo:')
    )
    return _form
