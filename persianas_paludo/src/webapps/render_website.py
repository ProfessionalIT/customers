#!/usr/bin/python
# -*- coding: utf-8 -*-
from web import template
from model import get_pagina, get_produto, get_promocoes
import os

rootpath = os.path.abspath(os.path.dirname(__file__))

site_layout_path = template.render(rootpath + '/templates/site', cache=False)

def layout(active_menu, content):
    return site_layout_path.layout(active_menu, content)

def index():
    promocoes = get_promocoes()
    return site_layout_path.index(promocoes)

def pagina(pagina_name):
    conteudo = get_pagina(pagina_name)
    return site_layout_path.pagina(conteudo)

def produtos():
    produtos = []
    return site_layout_path.produtos(produtos)

def produto(slug_produto):
    conteudo = get_produto(slug_produto)
    return site_layout_path.produto(conteudo)

def agradecimento():
    return site_layout_path.obrigado_contato()
    
def rss():
    return site_layout_path.rss()
