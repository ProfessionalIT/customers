# -*- coding: utf-8 -*-
import os
import web

import render_admin as render
import model
from model import ExistValueException
from configuration import WEBSITE_URL
import forms

from paginator import Paginator, PaginatorSearch
from auth import requires_admin, get_logged_user

urls = (
  '', 'Main',
  '/', 'Main',
  '/index', 'Index',
  '/login/$', 'Login',
  '/logout/$', 'Logout',
  '/listar/(.*)', 'EntityList',
  '/inserir/(.*)/(.*)', 'EntityInsert',
  '/editar/(.*)/(.*)', 'EntityEdit',
  '/excluir/(.*)/(.*)/(.*)', 'EntityDelete'
)

d = {}

class Main():
    @requires_admin
    def GET(self):
        raise web.seeother("/index")

class Index:
    @requires_admin
    def GET(self):
        return render.layout(render.index_admin())

class Login(object):
    def GET(self):
        return render.layout(render.login(**d))

    def POST(self):
        i = web.input()
        try:
            if i.username and i.password:
                logado = model.login(i.username, i.password)
                if logado.login:
                    web.ctx.session.isAdmin = 1
                    web.ctx.session.admin_user = logado.login
                    web.ctx.session.logged=logado
                    getattr(model, 'Log').new_log({'usuario': logado.id, 'operacao': 'LOGIN', 'log': 'O usuario realizou o LOGIN no Modulo Administrativo', 'endereco_ip': web.ctx.ip, 'menu': 'Home'})
                    raise web.seeother('/')
            else:
               d['error'] = "Usuário ou Senha inválidos!"
        except Exception as e:
            if str(e)=='0':
                d['error'] = "Usuário ou Senha inválidos!"
            else:
                d['error'] = str(e)
        return render.layout(render.login(**d))

class Logout(object):
    def GET(self):
        getattr(model, 'Log').new_log({'usuario': get_logged_user().id, 'operacao': 'LOGOFF', 'log': 'O usuario saiu do Modulo Administrativo', 'endereco_ip': web.ctx.ip, 'menu': 'Home'})
        web.ctx.session.kill()
        raise web.seeother(WEBSITE_URL)

class EntityList():
    @requires_admin
    def GET(self, param):
        entity = getattr(model, param)
        form = forms.getSearchForm(entity.exposed_search_properties())
        pagination = Paginator(web.input(), entity)
        display_message=web.cookies().get('display_message')
        web.setcookie('display_message', '')
        return render.layout(render.listar(form, pagination, display_message=display_message))

    @requires_admin
    def POST(self, param):
        entity = getattr(model, param)
        form = forms.getSearchForm(entity.exposed_search_properties())
        if not form.validates():
            raise web.seeother('/listar/%s' % param)
        pagination = PaginatorSearch(web.input(), form, entity)
        display_message=''
        return render.layout(render.listar(form, pagination, display_message=display_message))

class EntityInsert():
    @requires_admin
    def GET(self, param, alternate_id=None):
        if alternate_id:
            frm = forms.getImovelRecursoForm(alternate_id)
        else:
            frm = getattr(forms, 'get%sForm' % param)()
        
        display_message=web.cookies().get('display_message')
        web.setcookie('display_message', '')
        return render.layout(render.form(frm, '/static/images/%s.png' % param, titulo='Incluir %s' % getattr(model, param).get_form_title(), verbo='incluir', display_message=display_message))

    @requires_admin
    def POST(self, param, alternate_id=None):
        if alternate_id:
            frm = forms.getImovelRecursoForm(alternate_id)
        else:
            frm = getattr(forms, 'get%sForm' % param)()
        if frm.validates():
            try:
                getattr(model, param).save(frm.d)
            except ExistValueException, (instance):
                frm.note=str(instance.parameter)
                return render.form(frm, '/static/images/%s.png' % param, titulo='Incluir %s' % param, verbo='incluir', display_message='', estilo='table', )
            if param=='Usuario':
                display_message='Inseriu o registro %s com sucesso !' % frm.d.login
            elif param=='Enquete':
                display_message='Inseriu o registro %s com sucesso !' % frm.d.pergunta
            else:
                display_message='Inseriu o registro %s com sucesso !' % frm.d.titulo
            web.setcookie('display_message', display_message)
            if frm.d.operation == 'save':
                raise web.seeother('/inserir/%s' % param)
            else:
                if param=='ImovelRecurso':
                    raise web.seeother('/editar/Imovel/%s' % frm.d.imovel)
                else:
                    raise web.seeother('/listar/%s' % param)
        else:
            return render.layout(render.form(frm, '/static/images/%s.png' % param, titulo='Incluir %s' % getattr(model, param).get_form_title(), verbo='incluir', display_message='', estilo='table', ))

class EntityEdit():
    @requires_admin
    def GET(self, param, record_id):
        display_message=web.cookies().get('display_message')
        web.setcookie('display_message', '')
        if param=='Imovel':
            entry = model.entity_by_id(getattr(model, param), record_id)
            from utils import moeda_brasileira
            entry.valor_aluguel=moeda_brasileira(entry.valor_aluguel, False)
            entry.valor_venda=moeda_brasileira(entry.valor_venda, False)
            entry.valor_condominio=moeda_brasileira(entry.valor_condominio, False)
            entry.valor_agua=moeda_brasileira(entry.valor_agua, False)
            entry.valor_iptu=moeda_brasileira(entry.valor_iptu, False)
            frm = getattr(forms, 'get%sForm' % param)()
            frm.fill(entry)
            recursos = getattr(model, 'ImovelRecurso').get_recursos_by_imovel(entry.id)
            getattr(model, 'Log').new_log({'usuario': get_logged_user().id, 'operacao': 'EDITAR', 'log': 'O usuario editou o registro %(registro)s na Pagina %(pagina)s do Modulo Administrativo' % {'registro': frm.d['id'], 'pagina': param}, 'endereco_ip': web.ctx.ip, 'menu': 'Admin'})
            return render.layout(render.form_update(frm, '/static/images/%s.png' % param, entry.id, recursos, titulo='Alteracao de %s' % getattr(model, param).get_form_title(), verbo='editar', display_message=display_message, estilo='table'))
        else:
            entry = model.entity_by_id(getattr(model, param), record_id)
            frm = getattr(forms, 'get%sForm' % param)()
            frm.fill(entry)
        return render.layout(render.form(frm, '/static/images/%s.png' % param, titulo='Alterar %s' % getattr(model, param).get_form_title(), verbo='editar', display_message=display_message, estilo='table'))

    @requires_admin
    def POST(self, param, record_id):
        frm = getattr(forms, 'get%sForm' % param)()
        if not frm.validates():
            return render.layout(render.form(frm, '/static/images/%s.png' % param, titulo='Alterar %s' % getattr(model, param).get_form_title(), verbo='editar', estilo='table'))
        if param=='Enquete':
            display_message='Alterou o registro %s com sucesso !' % frm.d.pergunta
        elif param=='Usuario':
            display_message='Alterou o registro %s com sucesso !' % frm.d.login
        else:
            display_message='Alterou o registro %s com sucesso !' % frm.d.titulo
        web.setcookie('display_message', display_message)
        if frm.d.operation == 'delete':
            raise web.seeother('/excluir/%(entity)s/%(id)s/' % {'entity': param, 'id': record_id})
        elif frm.d.operation == 'save':
            getattr(model, param).save(frm.d)
            raise web.seeother('/editar/%(entity)s/%(id)s' % {'entity': param, 'id': record_id})
        else:
            getattr(model, param).save(frm.d)
            if param=='ImovelRecurso':
                raise web.seeother('/editar/Imovel/%s' % frm.d.imovel)
            else:
                raise web.seeother('/listar/%s' % param)

class EntityDelete():
    @requires_admin
    def GET(self, param, record_id, alternate_id=None):
        model.delete_entity(getattr(model, param), record_id)
        display_message='Excluiu o registro com sucesso !'
        web.setcookie('display_message', display_message)
        if alternate_id:
            raise web.seeother('/editar/Imovel/%s' % alternate_id)
        else:
            raise web.seeother('/listar/%s' % param)

app = web.application(urls, globals())

def main():
    pass
