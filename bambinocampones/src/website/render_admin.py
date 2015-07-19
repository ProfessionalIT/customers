# -*- coding: utf-8 -*-
from web import template
from configuration import (WEBSITE_NAME,
                           ADMIN_VERSION,
                           STATIC_URL)
from auth import get_logged_user, get_logoff_url
from model import get_exposed_managed_tables

import os
rootpath = os.path.abspath(os.path.dirname(__file__))

admin_template_path = template.render(rootpath + '/templates/admin',
                                      cache=False)


def layout(content):
    usuario = get_logged_user()
    if usuario:
        render_vars = {'website_name': WEBSITE_NAME,
                       'static_url': STATIC_URL,
                       'version': ADMIN_VERSION,
                       'user': get_logged_user(),
                       'logoff_url': get_logoff_url(),
                       'exposed_managed_tables':
                              get_exposed_managed_tables(usuario.nivel_acesso)}
    else:
        render_vars = {'website_name': WEBSITE_NAME,
                       'static_url': STATIC_URL,
                       'version': ADMIN_VERSION,
                       'user': get_logged_user(),
                       'logoff_url': get_logoff_url(),
                       'exposed_managed_tables': []}
    return admin_template_path.admin(render_vars, content)


def index_admin():
    return admin_template_path.index_admin()


def form(request_vars):
    request_vars['method'] = 'post'
    request_vars['action'] = ''
    return admin_template_path.form(request_vars)


def form_update(request_vars):
    request_vars['method'] = 'post'
    request_vars['action'] = ''
    return admin_template_path.form_update(request_vars)


def listar(request_vars):
    filtro = ''
    if request_vars['pagination'].query is not None \
        and request_vars['pagination'].query != 'None' \
        and request_vars['pagination'].query != 'all' \
        and request_vars['pagination'].query != '':
        query = request_vars['pagination'].query
        if query == "status='A'":
            query = 'Approved'
        elif query == "status='W'":
            query = 'Waiting'
        elif query == "status='R'":
            query = 'Refused'
        elif query == "locked='S'":
            query = 'Em Edição'
        filtro = 'Filtrando por: %(query)s' % {'query': query}
    request_vars['filtro'] = filtro
    return admin_template_path.lista(request_vars)


def moderar(request_vars):
    if request_vars['pagination'].query is not None \
        and request_vars['pagination'].query != 'None' \
        and request_vars['pagination'].query != 'all' \
        and request_vars['pagination'].query != '':
        query = request_vars['pagination'].query
        if query == "acao='A'":
            query = 'Approved'
        elif query == "acao='R'":
            query = 'Refused'
        request_vars['filtro'] = 'Filtrando por: %(query)s' % {'query': query}
    return admin_template_path.modera(request_vars)


def login(**d):
    error = d.pop('error', '')
    return admin_template_path.login(error)


def show_template(param):
    return admin_template_path.show_template(param)
