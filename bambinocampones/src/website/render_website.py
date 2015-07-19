# -*- coding: utf-8 -*-
from web import template
from configuration import (WEBSITE_URL,
                           STATIC_URL)
from model import (get_active_template,
                   get_menu_itens,
                   get_pagina,
                   get_pagina_preview,
                   get_banners_topo,
                   get_banners_desc,
                   get_banners_lateral,
                   get_produtos_portifolio,
                   get_noticias_destaques)


def get_layout_path():
    """
    """
    import os
    rootpath = os.path.abspath(os.path.dirname(__file__))
    active_template = get_active_template()
    site_layout_path = template.render(rootpath +
                                       '/templates/' + active_template.path,
                                       cache=False)
    return site_layout_path


def layout(active_menu, content):
    """
    """
    template_vars = {'context_path': WEBSITE_URL,
                     'static_url': STATIC_URL,
                     'menu_itens': get_menu_itens(),
                     'active_menu': active_menu,
                     'banners_topo': get_banners_topo(),
                     'fotos_desc': get_banners_desc(),
                     'banners_lateral': get_banners_lateral()}
    return get_layout_path().layout(template_vars, content)


def index():
    """
    """
    destaques = get_noticias_destaques()
    return get_layout_path().index(destaques=destaques)


def pagina(pagina_name):
    """
    """
    conteudo = get_pagina(pagina_name)
    if conteudo is None:
        return get_layout_path().construcao()
    else:
        return get_layout_path().pagina(conteudo)


def ajax_page_content(pagina_name):
    """
    """
    conteudo = get_pagina(pagina_name)
    import json
    return json.dumps(conteudo)


def preview(param, slug):
    """
    """
    if param == 'Pagina':
        conteudo = get_pagina_preview(slug)
        return get_layout_path().pagina(conteudo)
    else:
        return pagina('index')


def portifolio():
    """
    """
    produtos = get_produtos_portifolio()
    return get_layout_path().portifolio(produtos=produtos)


def orcamento(form):
    """
    """
    return get_layout_path().orcamento(form)


def contato(form):
    """
    """
    return get_layout_path().contato(form)


def localizacao():
    """
    """
    return get_layout_path().localizacao()
