#!/usr/bin/python
# -*- coding: utf-8 -*-
from web import template

from model import get_header_image, get_fotos_slide_show, get_entity_index_list, get_produtos_destaque, get_produtos_by_categoria

from datetime import datetime
import logging

site_layout_path = template.render('templates/site', cache=False)

def layout(content):
    background_header = get_header_image()[0]
    render_vars = {'background_header': background_header.imagem_url }
    return site_layout_path.base(render_vars, content)

def index():
    destaques=get_produtos_destaque()
    foto_itens=get_fotos_slide_show()
    fotos_desc = ''
    loop_count=1
    for foto in foto_itens:
        fotos_desc+='{"id":"slide-img-%(item_count)s","client":"%(item_name)s","desc":"%(item_desc)s"},' % {'item_count': str(loop_count), 'item_name': foto.nome, 'item_desc': foto.descricao}
        loop_count += 1
    fotos_desc = fotos_desc[:-1]
    return site_layout_path.index(foto_itens, fotos_desc, destaques)

def orcamento():
    pass

def atendimento():
    return site_layout_path.atendimento()

def contato(form, **kw):
    method = kw.pop('method', 'post')
    action = kw.pop('action', '')
    return site_layout_path.contato(action, method, form)

def agradece_contato():
    return site_layout_path.agradece_contato()

def pedido(form, **kw):
    method = kw.pop('method', 'post')
    action = kw.pop('action', '')
    return site_layout_path.pedido(action, method, form)

def agradece_pedido():
    return site_layout_path.agradece_pedido()

def pagina(conteudo):
    return site_layout_path.pagina(conteudo)

def listar_entity(pagination):
    if pagination.classe_name == 'Curiosidade':
        return site_layout_path.listar_curiosidades(pagination)
    elif pagination.classe_name == 'CategoriaProduto':
        return site_layout_path.listar_produtos(pagination)

def detalhar(entity):
    produtos = get_produtos_by_categoria(entity)
    return site_layout_path.detalhar(entity.nome, produtos)
