# -*- coding: utf-8 -*-
import os
import web

import render_admin as render
import render_website as render_layout
import model
from model import ExistValueException
from configuration import WEBSITE_URL, CONTROL_CONCURRENT_ACCESS
import forms

from paginator import Paginator, PaginatorSearch
from auth import requires_admin, get_logged_user

urls = (
  '', 'Main',
  '/', 'Main',
  '/index', 'Index',
  '/login/$', 'Login',
  '/logout/$', 'Logout',
  '/set-unlocked/(.+)/(.+)', 'AjaxSetUnlocked',
  '/moderate/(.+)/(.+)', 'ModerateRecord',
  '/listar/(.*)', 'EntityList',
  '/inserir/(.*)/(.*)', 'EntityInsert',
  '/editar/(.*)/(.*)', 'EntityEdit',
  '/preview/(.*)/(.*)', 'EntityPreview',
  '/show-template/(.*)', 'ShowTemplate',
  '/excluir/(.*)/(.*)/(.*)', 'EntityDelete'
)

d = {}

class Main():
    @requires_admin
    def GET(self):
        raise web.seeother(WEBSITE_URL + '/admin' + '/index')

class AjaxSetUnlocked():
    @requires_admin
    def GET(self, param, record_id):
        model.update_entity_lock(getattr(model, param), record_id, 'N')
        return 'OK'

    @requires_admin
    def POST(self, param, record_id):
        model.update_entity_lock(getattr(model, param), record_id, 'N')
        return 'OK'

class ModerateRecord():
    @requires_admin
    def GET(self, verb, record_id):
        model.moderate(verb, record_id)
        raise web.seeother(WEBSITE_URL + '/admin' + '/listar/Moderacao')

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
                    if logado.nivel_acesso == 1:
                        web.ctx.session.isAdmin = 1
                    else:
                        web.ctx.session.isAdmin = logado.nivel_acesso
                    web.ctx.session.admin_user = logado.login
                    web.ctx.session.logged=logado
                    getattr(model, 'Log').new_log({'usuario': logado.id, 'operacao': 'LOGIN', 'log': 'O usuario realizou o LOGIN no Modulo Administrativo', 'endereco_ip': web.ctx.ip, 'menu': 'Home'})
                    raise web.seeother(WEBSITE_URL + '/admin')
            else:
               d['error'] = "Usuário ou Senha inválidos!"
        except:
            d['error'] = "Usuário ou Senha inválidos!"
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
        request_vars = {'form': form, 'pagination': pagination, 'display_message': display_message, 'access_control': CONTROL_CONCURRENT_ACCESS}
        if param == 'Moderacao':
            return render.layout(render.moderar(request_vars))
        else:
            return render.layout(render.listar(request_vars))

    @requires_admin
    def POST(self, param):
        entity = getattr(model, param)
        form = forms.getSearchForm(entity.exposed_search_properties())
        if not form.validates():
            raise web.seeother(WEBSITE_URL + '/admin' + '/listar/%s' % param)
        pagination = PaginatorSearch(web.input(), form, entity)
        display_message=''
        request_vars = {'form': form, 'pagination': pagination, 'display_message': display_message, 'access_control': CONTROL_CONCURRENT_ACCESS}
        if param == 'Moderacao':
            return render.layout(render.moderar(request_vars))
        else:
            return render.layout(render.listar(request_vars))

class EntityInsert():
    @requires_admin
    def GET(self, param, alternate_id=None):
        frm = getattr(forms, 'get%sForm' % param)()
        display_message=web.cookies().get('display_message')
        web.setcookie('display_message', '')
        request_vars = {'form': frm, 'img_url': '/static/images/%s.png' % param, 'titulo': 'Incluir %s' % getattr(model, param).get_form_title(), 'verbo': 'incluir', 'display_message': display_message, 'in_moderation_mode': 'no', 'action_url': '', 'access_control': CONTROL_CONCURRENT_ACCESS}
        return render.layout(render.form(request_vars))

    @requires_admin
    def POST(self, param, alternate_id=None):
        frm = getattr(forms, 'get%sForm' % param)()
        if frm.validates():
            try:
                getattr(model, param).save(frm.d)
            except ExistValueException, (instance):
                frm.note=str(instance.parameter)
                request_vars = {'form': frm, 'img_url' : '/static/images/%s.png' % param, 'titulo': 'Incluir %s' % param, 'verbo': 'incluir', 'display_message': '', 'in_moderation_mode': 'no', 'action_url': '', 'access_control': CONTROL_CONCURRENT_ACCESS}
                return render.form(request_vars)
            if param=='Usuario':
                display_message='Inseriu o registro %s com sucesso !' % frm.d.login
            elif param=='Enquete':
                display_message='Inseriu o registro %s com sucesso !' % frm.d.pergunta
            else:
                display_message='Inseriu o registro %s com sucesso !' % frm.d.titulo
            web.setcookie('display_message', display_message)
            if frm.d.operation == 'save':
                raise web.seeother(WEBSITE_URL + '/admin' + '/inserir/%s' % param)
            else:
                raise web.seeother(WEBSITE_URL + '/admin' + '/listar/%s' % param)
        else:
            request_vars = {'form': frm, 'img_url': '/static/images/%s.png' % param, 'titulo': 'Incluir %s' % getattr(model, param).get_form_title(), 'verbo': 'incluir', 'display_message': '', 'in_moderation_mode': 'no', 'action_url': '', 'access_control': CONTROL_CONCURRENT_ACCESS}
            return render.layout(render.form(request_vars))

class EntityEdit():
    @requires_admin
    def GET(self, param, record_id):
        display_message=web.cookies().get('display_message')
        web.setcookie('display_message', '')
        in_moderation_mode = 'no'
        if web.ctx.query == '?op=moderate_on':
            in_moderation_mode = 'yes'
        else:
            if param != 'Usuario':
                from auth import get_logged_user
                usuario = get_logged_user()
                record_user = model.entity_by_id(getattr(model, param), record_id)
                if usuario.id != record_user.autor:
                    if record_user.locked == 'S':
                        if str(usuario.nivel_acesso) != '1':
                            display_message='Este registro já está em edição por OUTRO usuário e seu nível de acesso não é de Administrador.'
                            web.setcookie('display_message', display_message)
                            raise web.seeother(WEBSITE_URL + '/admin' + '/listar/%s' % param)
                else:
                    if record_user.locked == 'S':
                        display_message='Este registro já está em edição pelo SEU usuário !, por favor entre em contato com o responsável pelo site.'
                        web.setcookie('display_message', display_message)
                        raise web.seeother(WEBSITE_URL + '/admin' + '/listar/%s' % param)
                if CONTROL_CONCURRENT_ACCESS:
                    model.update_entity_lock(getattr(model, param), record_id, 'S')
        entry = model.entity_by_id(getattr(model, param), record_id)
        if param == 'Publicacao':
            frm = forms.getPublicacaoForm(record_id)
        else:
            frm = getattr(forms, 'get%sForm' % param)()
        frm.fill(entry)
        action_url = '%(path)s/set-unlocked/%(entity)s/%(id)s' % {'path': str(web.ctx.home), 'entity': param, 'id': record_id}
        request_vars = {'form': frm, 'img_url': '/static/images/%s.png' % param, 'titulo': 'Alterar %s' % getattr(model, param).get_form_title(), 'verbo': 'editar', 'display_message': display_message, 'action_url': action_url, 'in_moderation_mode': in_moderation_mode, 'access_control': CONTROL_CONCURRENT_ACCESS}
        return render.layout(render.form(request_vars))

    @requires_admin
    def POST(self, param, record_id):
        frm = getattr(forms, 'get%sForm' % param)()
        if param == 'Publicacao':
            if not frm.validates(web.input(tipos=[])):
                request_vars = {'form': frm, 'img_url': '/static/images/%s.png' % param, 'titulo': 'Alterar %s' % getattr(model, param).get_form_title(), 'verbo': 'editar', 'display_message': '', 'action_url': '', 'in_moderation_mode': 'no', 'access_control': CONTROL_CONCURRENT_ACCESS}
                return render.layout(render.form(request_vars))
        else:
            if not frm.validates():
                request_vars = {'form': frm, 'img_url': '/static/images/%s.png' % param, 'titulo': 'Alterar %s' % getattr(model, param).get_form_title(), 'verbo': 'editar', 'display_message': '', 'action_url': '', 'in_moderation_mode': 'no', 'access_control': CONTROL_CONCURRENT_ACCESS}
                return render.layout(render.form(request_vars))
        
        #obj = getattr(model, param).__init__(
        
        if param=='Enquete':
            display_message='Alterou o registro %s com sucesso !' % frm.d.pergunta
        elif param=='Usuario':
            display_message='Alterou o registro %s com sucesso !' % frm.d.login
        else:
            display_message='Alterou o registro %s com sucesso !' % frm.d.titulo
        web.setcookie('display_message', display_message)
        if frm.d.operation == 'delete':
            raise web.seeother(WEBSITE_URL + '/admin' + '/excluir/%(entity)s/%(id)s/' % {'entity': param, 'id': record_id})
        elif frm.d.operation == 'save':
            getattr(model, param).save(frm.d)
            raise web.seeother(WEBSITE_URL + '/admin' + '/editar/%(entity)s/%(id)s' % {'entity': param, 'id': record_id})
        elif frm.d.operation == 'publish':
            getattr(model, param).publish(frm.d)
            raise web.seeother(WEBSITE_URL + '/admin' + '/editar/%(entity)s/%(id)s' % {'entity': param, 'id': record_id})
        else:
            getattr(model, param).save(frm.d)
            raise web.seeother(WEBSITE_URL + '/admin' + '/listar/%s' % param)

class EntityPreview():
    @requires_admin
    def GET(self, param, slug):
        return render_layout.layout('menu_home',render_layout.preview(param, slug))
        
class EntityDelete():
    @requires_admin
    def GET(self, param, record_id, alternate_id=None):
        model.delete_entity(getattr(model, param), record_id)
        display_message='Excluiu o registro com sucesso !'
        web.setcookie('display_message', display_message)
        raise web.seeother(WEBSITE_URL + '/admin' + '/listar/%s' % param)

class ShowTemplate():
    @requires_admin
    def GET(self, param):
        return render.show_template(param)

    @requires_admin
    def POST(self, param):
        return render.show_template(param)

app = web.application(urls, globals())

def main():
    pass
