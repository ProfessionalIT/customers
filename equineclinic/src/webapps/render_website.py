# -*- coding: utf-8 -*-
from web import template
from configuration import WEBSITE_URL
from model import get_active_template, get_menu_itens, get_pagina, get_pagina_preview, get_banners_produtos, get_banners_internos, get_images_slideshow, get_publicacoes, get_publicacao

def get_layout_path():
    import os
    rootpath = os.path.abspath(os.path.dirname(__file__))
    active_template = get_active_template()
    site_layout_path = template.render(rootpath + '/templates/' + active_template.path, cache=False)
    return site_layout_path
    
def layout(active_menu, where_i_am, content):
    template_vars = {'context_path': WEBSITE_URL, 'menu_itens': get_menu_itens(), 'active_menu': active_menu, 'where_i_am': where_i_am,  'banners_produtos': get_banners_produtos(), 'banners_internos': get_banners_internos()}
    return get_layout_path().layout(template_vars, content)

def index():
    images = get_images_slideshow()
    return get_layout_path().index(images)

def noticias(pagination):
    noticias = get_publicacoes('Notícia')
    return get_layout_path().publicacoes('noticia', 'Notícias', pagination)

def noticia(slug_noticia):
    noticia = get_publicacao(slug_noticia)
    return get_layout_path().publicacao(noticia)

def eventos(pagination):
    eventos = get_publicacoes('Eventos')
    return get_layout_path().publicacoes('evento', 'Eventos', pagination)

def evento(slug_evento):
    evento = get_publicacao(slug_evento)
    return get_layout_path().publicacao(evento)

def artigos(pagination):
    artigos = get_publicacoes('Artigos')
    return get_layout_path().publicacoes('artigo', 'Artigos', pagination)

def artigo(slug_artigo):
    artigo = get_publicacao(slug_artigo)
    return get_layout_path().publicacao(artigo)

def pesquisas(pagination):
    pesquisas = get_publicacoes('Pesquisas')
    return get_layout_path().publicacoes('pesquisa', 'Pesquisas', pagination)

def pesquisa(slug_pesquisa):
    pesquisa = get_publicacao(slug_pesquisa)
    return get_layout_path().publicacao(pesquisa)

def pagina(pagina_name):
    conteudo = get_pagina(pagina_name)
    if conteudo is None:
        return get_layout_path().construcao()
    else:
        return get_layout_path().pagina(conteudo)

def preview(param, slug):
    if param == 'Pagina':
        conteudo = get_pagina_preview(slug)
        return get_layout_path().pagina(conteudo)
    else:
        return pagina('index')

def contato():
    return get_layout_path().contato()
