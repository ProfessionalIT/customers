#!/usr/bin/python
# -*- coding: utf-8 -*-
from web import template
from configuration import WEBSITE_NAME, ADMIN_VERSION
from auth import get_logged_user, get_logoff_url
from model import get_exposed_managed_tables

import os
rootpath = os.path.abspath(os.path.dirname(__file__))

admin_template_path = template.render(rootpath + '/templates/admin',
                                      cache=False)


def layout(content):
    render_vars = {'website_name': WEBSITE_NAME,
                   'version': ADMIN_VERSION,
                   'user': get_logged_user(),
                   'logoff_url': get_logoff_url(),
                   'exposed_managed_tables': get_exposed_managed_tables()}
    return admin_template_path.admin(render_vars, content)


def index_admin():
    return admin_template_path.index_admin()


def form(form,
         img_url=None,
         titulo=None,
         verbo=None,
         display_message=None,
         **kw):
    method = kw.pop('method', 'post')
    action = kw.pop('action', '')
    return admin_template_path.form(titulo,
                                    img_url,
                                    action,
                                    method,
                                    form,
                                    verbo,
                                    display_message)


def form_update(form,
                img_url,
                imovel_id,
                recursos,
                titulo=None,
                verbo=None,
                display_message=None,
                **kw):
    method = kw.pop('method', 'post')
    action = kw.pop('action', '')
    return admin_template_path.form_update(titulo,
                                           img_url,
                                           action,
                                           method,
                                           form,
                                           imovel_id,
                                           recursos,
                                           verbo,
                                           display_message)


def listar(frm, pagination, display_message=None):
    filtro = ''
    if pagination.query is not None \
        and pagination.query != 'None' \
        and pagination.query != 'all' and pagination.query != '':
        filtro = 'Filtrando por: %(query)s' % {'query': pagination.query}
    return admin_template_path.lista(frm, filtro, pagination, display_message)


def login(**d):
    error = d.pop('error', '')
    return admin_template_path.login(error)
