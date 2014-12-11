# -*- coding: utf-8 -*-
from web import form
from configuration import CONTROL_CONCURRENT_ACCESS
import model

import os
rootpath = os.path.abspath(os.path.dirname(__file__))

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
        form.Dropdown('nivel_acesso', [('1', 'Administrador'), ('2', 'Operador'), ('3', 'Moderador')], title="Nivel de Acesso do Usuario", description='Nível de Acesso:')
    )
    return _form

def getPaginaForm():
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome da Página.", description='Titulo:'))
    form_fields.append(form.Textbox('slug', size="60", maxlength="250", title="URL da Página.", readonly="readonly", class_="readonly", description='URL da Página:'))
    form_fields.append(form.Textbox('descricao_completa', form.notnull, size="60", maxlength="250", title="Descrição Completa da Página.", description='Descrição Completa:'))
    form_fields.append(form.Textbox('palavras_chaves', form.notnull, size="60", maxlength="250", title="Palavras Chaves da Página separadas por vírgula.", description='Palavras Chaves:'))
    form_fields.append(form.Textarea('conteudo', form.notnull, cols="70", rows="25", title="Conteúdo da Página.", description='Conteúdo da Página:'))
    form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:'))
    form_fields.append(form.Dropdown('permite_comentario', [('S', 'Sim'), ('N', 'Não')], title="Permite Comentários na Página ?", description='Permite Comentário:'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="window.location='/admin/listar/Pagina'"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish'');"))
    return form.Form(*form_fields)

def getMenuForm():
    menu_list = model.select(getattr(model, 'Menu'))
    menu_options = [(str(row.id), row.titulo) for row in menu_list]
    pagina_list = model.select(getattr(model, 'Pagina'))
    pagina_options = [(str(row.id), row.titulo) for row in pagina_list]
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('ordem', vdigito, size="10", maxlenght="50", title="Ordem de Exibição do Menu na Página. Deve seguir a sequência para que o menu funcione.", description='Ordem de Exibição:'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Página.", description='Titulo:'))
    form_fields.append(form.Textbox('descricao', form.notnull, size="60", maxlenght="250", title="Descrição do Menu.", description='Descrição:'))
    form_fields.append(form.Textbox('key_words', form.notnull, size="60", maxlenght="250", title="Palavras Chave da Página.", description='Palavras Chave:'))
    form_fields.append(form.Dropdown('pagina', pagina_options, title="Página que deve ser exibida ao clicar no menu.", description='Página: '))
    form_fields.append(form.Textbox('endereco', form.notnull, size="60", maxlenght="250", title="Endereço do link.", description='Endereço do Link:'))
    form_fields.append(form.Dropdown('menu_pai', menu_options, title="Menu Pai/Superior do Menu.", description='Menu Superior: '))
    form_fields.append(form.Dropdown('nivel', [('0', '0'), ('1', '1'), ('2', '2')], title="Nível do Menu: 0 - MenuBar, 1-Menu Principal, 2-Menu Interno.", description='Nível: '))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:', disabled='disabled', value='N'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)

def getParametroForm():
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome do Parâmetro.", description='Titulo:'))
    form_fields.append(form.Textbox('valor', form.notnull, size="60", maxlength="250", title="Valor do Parâmetro.", description='Valor:'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)

def getAvisoForm():
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome do Aviso.", description='Titulo:'))
    form_fields.append(form.Textbox('slug', size="60", maxlength="250", title="URL do Aviso.", readonly="readonly", class_="readonly", description='URL do Aviso:'))
    form_fields.append(form.Textbox('data_publicacao', form.notnull, size="20", maxlength="20", class_="datetime", title="Data e Hora da Publicação do Aviso.", readonly="readonly", description='Data Publicação: '))
    form_fields.append(form.Textbox('data_expiracao', form.notnull, size="20", maxlength="20", class_="datetime", title="Data e Hora da Expiração do Aviso.", readonly="readonly", description='Data Expiração: '))
    form_fields.append(form.Textarea('texto', form.notnull, cols="70", rows="25", title="Conteúdo do Aviso.", description='Conteúdo do Aviso:'))
    form_fields.append(form.Dropdown('ativo', [('S', 'Sim'), ('N', 'Não')], title="Aviso Ativo ?", description='Ativo:'))
    form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:', disabled='disabled', value='N'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)

def getBannerForm():
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome do Banner.", description='Titulo:'))
    form_fields.append(form.Textbox('slug', size="60", maxlength="250", title="URL do Banner.", readonly="readonly", class_="readonly", description='URL do Banner:'))
    form_fields.append(form.Dropdown('tipo', [('S', 'SlideShow'), ('P', 'Parceiro'), ('C', 'Cliente')], title="Tipo do Banner", description='Tipo:'))
    form_fields.append(form.Textbox('foto_banner', form.notnull, size="60", maxlength="250", title="Foto do Banner.", description='URL Foto:'))
    form_fields.append(form.Textbox('link_banner', form.notnull, size="60", maxlength="250", title="Link do Banner.", description='Link ao Clicar:'))
    form_fields.append(form.Dropdown('exibir_pagina_inicial', [('S', 'Sim'), ('N', 'Não')], title="Exibir na Página Inicial ?", description='Exibir Página Inicial ?:'))
    form_fields.append(form.Dropdown('ativo', [('S', 'Sim'), ('N', 'Não')], title="Banner Ativo ?", description='Ativo:'))
    form_fields.append(form.Textbox('custom_banner_code', size="60", maxlength="250", title="Código HTML do Banner.", description='HTML do Banner:'))
    form_fields.append(form.Textbox('count_clicks', size="5", maxlength="1", title="Quantidade de Cliques.", readonly="readonly", class_="readonly", description='Qtde Cliques:'))
    form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:', disabled='disabled', value='N'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)

def getTipoDocumentoForm():
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome do Aviso.", description='Titulo:'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    return form.Form(*form_fields)

def getDocumentoForm():
    form_fields = []
    tipo_list = model.select_approved(getattr(model, 'TipoDocumento'))
    tipo_options = [(str(row.id), row.titulo.encode('utf8')) for row in tipo_list]
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome da Publicação.", description='Titulo:'))
    form_fields.append(form.Textbox('slug', size="60", maxlength="250", title="URL da Publicação.", readonly="readonly", class_="readonly", description='URL do Documento:'))
    form_fields.append(form.Textbox('data_publicacao', form.notnull, size="20", maxlength="20", class_="datetime", title="Data e Hora da Publicação.", readonly="readonly", description='Data Publicação: '))
    form_fields.append(form.Dropdown('tipo', tipo_options, title="Tipo de Publicação", description='Tipo:'))
    form_fields.append(form.CustomLink('ListarTipo', link='/admin/listar/TipoDocumento', html='Listar Tipos'))
    form_fields.append(form.Textbox('thumb_arquivo', form.notnull, size="60", maxlength="250", title="Thumb do Arquivo.", description='URL Thumb:'))
    form_fields.append(form.Textbox('link_arquivo', form.notnull, size="60", maxlength="250", title="Link do Arquivo.", description='Link ao Clicar:'))
    form_fields.append(form.Dropdown('ativo', [('S', 'Sim'), ('N', 'Não')], title="Banner Ativo ?", description='Ativo:'))
    form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:', disabled='disabled', value='N'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)

def getGaleriaForm():
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome da Galeria.", description='Titulo:'))
    form_fields.append(form.Textbox('slug', size="60", maxlength="250", title="URL da Galeria.", readonly="readonly", class_="readonly", description='URL da Galeria:'))
    form_fields.append(form.Textbox('data_criacao', form.notnull, size="20", maxlength="20", class_="datetime", title="Data e Hora da Criação.", readonly="readonly", description='Criação: '))
    form_fields.append(form.Dropdown('tipo', [('P', 'Picasa'), ('F', 'Facebook'), ('Y', 'youtube'), ('S', 'Servidor/Hospedagem')], title="Tipo de Galeria", description='Tipo:'))
    form_fields.append(form.Dropdown('midia', [('F', 'Foto'), ('V', 'Video')], title="Tipo de Mídia", description='Mídia:'))
    form_fields.append(form.Textbox('url_galeria', form.notnull, size="60", maxlength="250", title="URL da Galeria.", description='Endereço da Galeria:'))
    form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:', disabled='disabled', value='N'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)

def getTipoPublicacaoForm():
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome do Aviso.", description='Titulo:'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    return form.Form(*form_fields)

def getPublicacaoForm(record_id=None):
    galeria_list = model.select_approved(getattr(model, 'Galeria'))
    galeria_options = [("Sem Galeria", "Sem Galeria")]
    galeria_options += [(row.slug, row.titulo) for row in galeria_list]
    tipo_list = model.select_approved(getattr(model, 'TipoPublicacao'))
    tipo_options = [(str(row.id), row.titulo.encode('utf8')) for row in tipo_list]
    checked_tipos=[]
    if record_id:
        checked_tipos = str(model.object_by_id(model.Publicacao, record_id).get_tipos())
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome da Publicação.", description='Titulo:'))
    form_fields.append(form.Textbox('slug', size="60", maxlength="250", title="URL da Publicação.", readonly="readonly", class_="readonly", description='URL da Data Publicação:'))
    form_fields.append(form.Textbox('data_hora', form.notnull, size="20", maxlength="20", class_="datetime", title="Data e Hora da Publicação.", readonly="readonly", description='Data/Hora: '))
    form_fields.append(form.Textbox('data_publicacao', form.notnull, size="20", maxlength="20", class_="datetime", title="Data e Hora da Publicação.", readonly="readonly", description='Publicado: '))
    form_fields.append(form.Textbox('palavras_chaves', form.notnull, size="60", maxlength="250", title="Palavras Chaves.", description='Palavras Chaves:'))
    form_fields.append(form.MultiCheckbox('tipos', tipo_options, form.notnull, checked=checked_tipos, description='Tipo:', class_='multicheckbox'))
    form_fields.append(form.CustomLink('ListarTipo', link='/admin/listar/TipoPublicacao', html='Listar Tipos'))
    form_fields.append(form.Textarea('intro', form.notnull, cols="70", rows="25", title="Introdução do conteúdo da Publicação.", description='Introdução Conteúdo:'))
    form_fields.append(form.Textarea('completa', form.notnull, cols="70", rows="25", title="Conteúdo da Publicação.", description='Conteúdo Completo:'))
    form_fields.append(form.Textbox('thumb_publicacao', form.notnull, size="60", maxlength="250", title="Thumb da Publicação.", description='URL Thumb:'))
    form_fields.append(form.Dropdown('slug_galeria', galeria_options, title="Slug da Galeria.", description='Galeria: '))
    form_fields.append(form.Dropdown('destaque', [('S', 'Sim'), ('N', 'Não')], title="Publicação é Destaque ?", description='Destaque ?:'))
    form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)

def getEnqueteForm():
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('pergunta', form.notnull, size="60", maxlength="250", title="Pergunta da Enquete.", description='Pergunta:'))
    form_fields.append(form.Textbox('slug', size="60", maxlength="250", title="URL da Enquente.", readonly="readonly", class_="readonly", description='URL da Enquete:'))
    form_fields.append(form.Textbox('resposta_01', form.notnull, size="60", maxlength="250", title="Alternativa 01.", description='Alternativa 01:'))
    form_fields.append(form.Textbox('votos_resposta_01', size="60", maxlength="250", title="Quantidade 01.", readonly="readonly", class_="readonly", value='0', description='Qtde Votos 01:'))
    form_fields.append(form.Textbox('resposta_02', form.notnull, size="60", maxlength="250", title="Alternativa 02.", description='Alternativa 02:'))
    form_fields.append(form.Textbox('votos_resposta_02', size="60", maxlength="250", title="Quantidade 02.", readonly="readonly", class_="readonly", value='0', description='Qtde Votos 02:'))
    form_fields.append(form.Textbox('resposta_03', size="60", maxlength="250", title="Alternativa 03.", description='Alternativa 03:'))
    form_fields.append(form.Textbox('votos_resposta_03', size="60", maxlength="250", title="Quantidade 03.", readonly="readonly", class_="readonly", value='0', description='Qtde Votos 03:'))
    form_fields.append(form.Dropdown('ativo', [('S', 'Sim'), ('N', 'Não')], title="Aviso Ativo ?", description='Ativo:'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:', disabled='disabled', value='N'))
    form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)

def getTemplateForm():
    template_path = os.path.abspath(rootpath + '/templates')
    templates_folder = os.listdir(template_path)
    folders = []
    for folder in templates_folder:
        if not str(folder).startswith('.') and str(folder) != 'admin' and not str(folder).startswith('__'):
            folders.append(folder) 
    path_options = [(row, row) for row in folders]
    form_fields = []
    form_fields.append(form.Hidden('id'))
    form_fields.append(form.Hidden('operation'))
    form_fields.append(form.Textbox('titulo', form.notnull, size="60", maxlength="250", title="Titulo/Nome do Aviso.", description='Titulo:'))
    form_fields.append(form.Textbox('slug', size="60", maxlength="250", title="URL do Template.", readonly="readonly", class_="readonly", description='URL do Template:'))
    form_fields.append(form.Textbox('data_publicacao', form.notnull, size="20", maxlength="20", class_="datetime", title="Data e Hora da Publicação do Aviso.", readonly="readonly", description='Data Publicação: '))
    form_fields.append(form.Dropdown('path', path_options, title="Modelo Template/Layout.", description='Template: ', onchange='showTemplate(this);'))
    form_fields.append(form.Dropdown('ativo', [('S', 'Sim'), ('N', 'Não')], title="Aviso Ativo ?", description='Ativo:'))
    form_fields.append(form.Dropdown('draft', [('S', 'Sim'), ('N', 'Não')], title="Rascunho ?", description='Rascunho:', disabled='disabled', value='N'))
    if CONTROL_CONCURRENT_ACCESS:
        form_fields.append(form.Textbox('locked', size="5", maxlength="1", title="Registro em Edição.", readonly="readonly", class_="readonly", description='Editando:'))
        form_fields.append(form.Textbox('status', size="5", maxlength="1", title="Status.", readonly="readonly", class_="readonly", description='Status:'))
        form_fields.append(form.Textbox('moderate_id', size="10", maxlength="15", title="Moderação.", readonly="readonly", class_="readonly", description='Moderação:'))
    form_fields.append(form.Button('cancelar_button', html="Cancelar", type="button", onclick="javascript:history.back();"))
    form_fields.append(form.Button('salvar_button', html="Salvar", type="submit", onclick="return setMode('save');"))
    form_fields.append(form.Button('salvar_sair_button', html="Salvar e Sair", type="submit", onclick="return setMode('save_exit');"))
    form_fields.append(form.Button('excluir_button', html="Excluir", type="submit", onclick="return setMode('delete');"))
    form_fields.append(form.Button('visualizar_button', html="Visualizar", type="button", onclick="return preview();"))
    form_fields.append(form.Button('publicar_button', html="Publicar", type="submit", onclick="return setMode('publish');"))
    return form.Form(*form_fields)
