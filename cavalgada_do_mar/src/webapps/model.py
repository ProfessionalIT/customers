# -*- coding: utf-8 -*-
import web
import os
from configuration import DBN, HOST, DB, USER, PWD, AUTO_MODERATE, CONTROL_CONCURRENT_ACCESS
from utils import slugify, versionate, replace_separator, moeda_brasileira
from datetime import datetime

db = web.database(dbn=DBN, host=HOST, db=DB, user=USER, pw=PWD)
rootpath = os.path.abspath(os.path.dirname(__file__))

def unsetDB():
    global db
    db.ctx.db.close()
    db = None

def setDB():
    global db
    db = web.database(dbn=DBN, host=HOST, db=DB, user=USER, pw=PWD)

class ExistValueException(Exception):
   def __init__(self, value):
       self.parameter = "Existe um registro no banco de dados com esse valor: %s " % value
   def __str__(self):
       return repr(self.parameter)

# App Models.
class Usuario(object):
    __table__ = 'usuario'
    def __init__(self, id=None, login=None, senha=None, nivel_acesso=None):
        self.id = id
        self.login = login 
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    @classmethod
    def get_class_name(self):
        return "Usuario"

    @classmethod
    def get_list_title(self):
        return "Listagem de Usuários"

    @classmethod
    def get_form_title(self):
        return "Usuário"

    @classmethod
    def get_default_field_order(self):
        return "login"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('login', 'Login')] 

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Login']
        fields = ['login']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): return getattr(self, field)

    def __str__(self):
        if self is not None:
            if self.login:
                return self.login

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'login', form.login)
                if (entity is not None):
                    raise ExistValueException(form.login)
                else:
                    insert_id = db.insert(self.__table__, login=form.login, senha=form.senha, nivel_acesso=int(form.nivel_acesso))
            except IndexError:
                insert_id = db.insert(self.__table__, login=form.login, senha=form.senha, nivel_acesso=int(form.nivel_acesso))
        else:
            db.update(self.__table__, where="id=$id", vars=locals(), login=form.login, senha=form.senha, nivel_acesso=int(form.nivel_acesso))

class Log(object):
    __table__ = 'log'
    def __init__(self, id=None, usuario=None, operacao=None, endereco_ip=None, log=None, data=None, menu=None):
        self.id = id
        self.usuario = usuario
        self.operacao = operacao
        self.endereco_ip = endereco_ip
        self.log = log
        self.data = data
        self.menu = menu

    @classmethod
    def get_class_name(self):
        return "Log"

    @classmethod
    def get_list_title(self):
        return "Listagem de Logs"

    @classmethod
    def get_form_title(self):
        return "LOG"

    @classmethod
    def get_default_field_order(self):
        return "data desc"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('usuario', 'Usuário'), ('operacao','Operação'), ('endereco_ip','Endereço IP'), ('log', 'Log')] 

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Usuario', 'Operação', 'Endereço IP', 'Log', 'Data', 'Menu']
        fields = ['usuario', 'operacao', 'endereco_ip', 'log', 'data', 'menu']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'usuario':
                id = getattr(self, field)
                usuario = entity_by_id(Usuario, id)
                if usuario:
                    return usuario.login
                else:
                    return None
            elif field == 'data':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def new_log(self, record):
        insert_id = db.insert('log', usuario=record['usuario'], operacao=record['operacao'], endereco_ip=record['endereco_ip'], log=record['log'], data=datetime.now(), menu=record['menu'])

class Pagina(object):
    __table__ = 'pagina'
    def __init__(self, id=None, titulo=None, slug=None, descricao_completa=None, palavras_chaves=None, data_criacao=None, ultima_alteracao=None, autor=None, conteudo=None, locked=None, status=None, moderate_id=None, permite_comentario=None, draft=None):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.descricao_completa = descricao_completa
        self.palavras_chaves = palavras_chaves
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.autor = autor
        self.conteudo = conteudo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.permite_comentario = permite_comentario
        self.draft = draft

    @classmethod
    def get_class_name(self):
        return "Pagina"

    @classmethod
    def get_list_title(self):
        return "Listagem de Páginas"

    @classmethod
    def get_form_title(self):
        return "Página"

    @classmethod
    def get_default_field_order(self):
        return "id"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('draft', 'Rascunho')] 

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Permite Comentários', 'Em Edição', 'Status', 'Moderação', 'Rascunho']
            fields = ['titulo', 'permite_comentario', 'locked', 'status', 'moderate_id', 'draft']
        else:
            colunms = ['Titulo', 'Permite Comentários', 'Rascunho']
            fields = ['titulo', 'permite_comentario', 'draft']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'permite_comentario':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'draft':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None                
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def publish(self, form):
        id = form.id
        db.update(self.__table__, where="id=$id", vars=locals(), draft='N')

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        from auth import get_logged_user
        usuario = get_logged_user()
        hoje = datetime.now()
        slug = slugify(form.titulo)
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'titulo', form.titulo)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, descricao_completa=form.descricao_completa, palavras_chaves=form.palavras_chaves, data_criacao=hoje, ultima_alteracao=hoje, autor=usuario.id, conteudo=form.conteudo, permite_comentario=form.permite_comentario, draft=form.draft)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu a Pagina ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, descricao_completa=form.descricao_completa, palavras_chaves=form.palavras_chaves, data_criacao=hoje, ultima_alteracao=hoje, autor=usuario.id, conteudo=form.conteudo, permite_comentario=form.permite_comentario, draft=form.draft)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu a Pagina ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, descricao_completa=form.descricao_completa, palavras_chaves=form.palavras_chaves, ultima_alteracao=hoje, autor=usuario.id, conteudo=form.conteudo, permite_comentario=form.permite_comentario, status='A', locked='N', draft=form.draft)
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, descricao_completa=form.descricao_completa, palavras_chaves=form.palavras_chaves, ultima_alteracao=hoje, autor=usuario.id, conteudo=form.conteudo, permite_comentario=form.permite_comentario, status='W', locked='N', draft=form.draft)
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou a Pagina ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

def get_pagina(endereco):
    try:
        record = db.query("select titulo, descricao_completa, palavras_chaves, conteudo from pagina where slug = '%(endereco)s' and draft = 'N'" % {'endereco': endereco})[0]
        return record
    except IndexError:
        return None

def get_pagina_preview(endereco):
    record = db.query("select titulo, descricao_completa, palavras_chaves, conteudo from pagina where slug = '%(endereco)s' and draft = 'S'" % {'endereco': endereco})[0]
    return record or None

class Menu(object):
    __table__ = 'menu'
    def __init__(self, id, ordem, titulo, descricao, slug, data_criacao, ultima_alteracao, autor, pagina, endereco, menu_pai, nivel, key_words, locked=None, status=None, moderate_id=None, draft=None):
        self.id = id
        self.ordem = ordem
        self.titulo = titulo
        self.descricao = descricao
        self.slug = slug
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.autor = autor
        self.pagina = pagina
        self.endereco = endereco
        self.menu_pai = menu_pai
        self.nivel = nivel
        self.key_words = key_words
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.draft = draft

    @classmethod
    def get_class_name(self):
        return "Menu"

    @classmethod
    def get_list_title(self):
        return "Listagem de Menus"

    @classmethod
    def get_form_title(self):
        return "Menu"

    @classmethod
    def get_default_field_order(self):
        return "ordem"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('ordem', 'Ordem'), ('nivel', 'Nível'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Ordem', 'Nivel', 'Titulo', 'Endereço']
        fields = ['ordem', 'nivel', 'titulo', 'endereco']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        hoje = datetime.now()
        from auth import get_logged_user
        usuario = get_logged_user()
        slug = slugify(form.titulo)
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'titulo', form.titulo)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        if form.menu_pai: 
                            insert_id = db.insert(self.__table__, ordem=int(form.ordem), titulo=form.titulo, descricao=form.descricao, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, autor=int(usuario.id), pagina=int(form.pagina) or None, endereco=form.endereco, menu_pai=int(form.menu_pai), nivel=int(form.nivel), key_words=form.key_words, draft=form.draft)
                        else:
                            insert_id = db.insert(self.__table__, ordem=int(form.ordem), titulo=form.titulo, descricao=form.descricao, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, autor=int(usuario.id), pagina=int(form.pagina) or None, endereco=form.endereco, menu_pai=None, nivel=int(form.nivel), key_words=form.key_words, draft=form.draft)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Menu ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    if form.menu_pai: 
                        insert_id = db.insert(self.__table__, ordem=int(form.ordem), titulo=form.titulo, descricao=form.descricao, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, autor=int(usuario.id), pagina=int(form.pagina) or None, endereco=form.endereco, menu_pai=int(form.menu_pai), nivel=int(form.nivel), key_words=form.key_words, draft=form.draft)
                    else:
                        insert_id = db.insert(self.__table__, ordem=int(form.ordem), titulo=form.titulo, descricao=form.descricao, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, autor=int(usuario.id), pagina=int(form.pagina) or None, endereco=form.endereco, menu_pai=None, nivel=int(form.nivel), key_words=form.key_words, draft=form.draft)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Menu ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), ordem=int(form.ordem), titulo=form.titulo, descricao=form.descricao, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, autor=usuario.id, pagina=int(form.pagina) or None, endereco=form.endereco, menu_pai=int(form.menu_pai) or None, nivel=int(form.nivel), key_words=form.key_words, status='A', locked='N', draft=form.draft)
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), ordem=int(form.ordem), titulo=form.titulo, descricao=form.descricao, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, autor=usuario.id, pagina=int(form.pagina) or None, endereco=form.endereco, menu_pai=int(form.menu_pai) or None, nivel=int(form.nivel), key_words=form.key_words, status='W', locked='N', draft=form.draft)
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou o Menu ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

class Aviso(object):
    __table__ = 'aviso'
    def __init__(self, id=None, titulo=None, slug=None, data_publicacao=None, data_expiracao=None, autor=None, texto=None, ativo=None, locked=None, status=None, moderate_id=None, draft=None):
        self.id = id
        self.titulo = titulo
        self.slug=slug
        self.data_publicacao=data_publicacao
        self.data_expiracao=data_expiracao
        self.autor=autor
        self.texto=texto
        self.ativo=ativo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.draft = draft

    @classmethod
    def get_class_name(self):
        return "Aviso"

    @classmethod
    def get_list_title(self):
        return "Listagem de Avisos"

    @classmethod
    def get_form_title(self):
        return "Aviso"

    @classmethod
    def get_default_field_order(self):
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('texto', 'Texto'), ('draft','Rascunho')] 

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Publicação', 'Expira em', 'Ativo', 'Em Edição', 'Status', 'Moderação', 'Rascunho']
            fields = ['titulo', 'data_publicacao', 'data_expiracao', 'ativo', 'locked', 'status', 'moderate_id', 'draft']
        else:
            colunms = ['Titulo', 'Publicação', 'Expira em', 'Ativo', 'Rascunho']
            fields = ['titulo', 'data_publicacao', 'data_expiracao', 'ativo', 'draft']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'data_publicacao':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'data_expiracao':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'ativo':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'draft':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None   
            elif field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        slug = slugify(form.titulo)
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'slug', form.slug)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), data_expiracao=datetime.strptime(form.data_expiracao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, texto=form.texto, ativo=form.ativo, draft=form.draft)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Aviso ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), data_expiracao=datetime.strptime(form.data_expiracao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, texto=form.texto, ativo=form.ativo, draft=form.draft)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Aviso ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), data_expiracao=datetime.strptime(form.data_expiracao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, texto=form.texto, ativo=form.ativo, status='A', locked='N', draft=form.draft)
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), data_expiracao=datetime.strptime(form.data_expiracao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, texto=form.texto, ativo=form.ativo, status='W', locked='N', draft=form.draft)
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou o Aviso ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

class Enquete(object):
    __table__ = 'enquete'
    def __init__(self, id=None, pergunta=None, slug=None, resposta_01=None, votos_resposta_01=None, resposta_02=None, votos_resposta_02=None, resposta_03=None, votos_resposta_03=None, ativo=None, locked=None, status=None, moderate_id=None, autor=None, draft=None):
        self.id = id
        self.pergunta = pergunta
        self.slug = slug
        self.resposta_01 = resposta_01
        self.votos_resposta_01 = votos_resposta_01
        self.resposta_02 = resposta_02
        self.votos_resposta_02 = votos_resposta_02
        self.resposta_03 = resposta_03
        self.votos_resposta_03 = votos_resposta_03
        self.ativo = ativo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.autor = autor
        self.draft = draft

    @classmethod
    def get_class_name(self):
        return "Enquete"

    @classmethod
    def get_list_title(self):
        return "Listagem de Enquetes"

    @classmethod
    def get_form_title(self):
        return "Enquete"

    @classmethod
    def get_default_field_order(self):
        return "pergunta"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('pergunta', 'Pergunta'), ('ativo', 'Ativo'), ('draft', 'Rascunho')] 

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Pergunta', 'Resposta 1', 'Votos', 'Resposta 2', 'Votos', 'Resposta 3', 'Votos', 'Ativo', 'Editando', 'Status', 'Moderação', 'Rascunho']
            fields = ['pergunta', 'resposta_01', 'votos_resposta_01', 'resposta_02', 'votos_resposta_02', 'resposta_03', 'votos_resposta_03', 'ativo', 'locked', 'status', 'moderate_id', 'draft']
        else:
            colunms = ['Pergunta', 'Resposta 1', 'Votos', 'Resposta 2', 'Votos', 'Resposta 3', 'Votos', 'Ativo', 'Rascunho']
            fields = ['pergunta', 'resposta_01', 'votos_resposta_01', 'resposta_02', 'votos_resposta_02', 'resposta_03', 'votos_resposta_03', 'ativo', 'draft']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'ativo':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            elif field == 'draft':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None   
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        slug = slugify(form.pergunta)
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'slug', slug)
                if (entity is not None):
                    raise ExistValueException(form.pergunta)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, pergunta=form.pergunta, slug=slug, resposta_01=form.resposta_01, votos_resposta_01=int(form.votos_resposta_01), resposta_02=form.resposta_02, votos_resposta_02=int(form.votos_resposta_02), resposta_03=form.resposta_03, votos_resposta_03=int(form.votos_resposta_03), ativo=form.ativo, autor=usuario.id, draft=form.draft)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu a Enquete ' + form.pergunta)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                            
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, pergunta=form.pergunta, slug=slug, resposta_01=form.resposta_01, votos_resposta_01=int(form.votos_resposta_01), resposta_02=form.resposta_02, votos_resposta_02=int(form.votos_resposta_02), resposta_03=form.resposta_03, votos_resposta_03=int(form.votos_resposta_03), ativo=form.ativo, autor=usuario.id, draft=form.draft)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu a Enquete ' + form.pergunta)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), pergunta=form.pergunta, slug=slug, resposta_01=form.resposta_01, votos_resposta_01=int(form.votos_resposta_01), resposta_02=form.resposta_02, votos_resposta_02=int(form.votos_resposta_02), resposta_03=form.resposta_03, votos_resposta_03=int(form.votos_resposta_03), ativo=form.ativo, status='A', locked='N', draft=form.draft)
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), pergunta=form.pergunta, slug=slug, resposta_01=form.resposta_01, votos_resposta_01=int(form.votos_resposta_01), resposta_02=form.resposta_02, votos_resposta_02=int(form.votos_resposta_02), resposta_03=form.resposta_03, votos_resposta_03=int(form.votos_resposta_03), ativo=form.ativo, status='W', locked='N', draft=form.draft)
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou a enquete ' + form.pergunta, moderador=None, data_hora_operacao=None, acao=None)

    @classmethod
    def update_enquete(self, slug, valor_resposta):
        #sql_update = 'update enquete set %(valor_reposta)' 
        pass

class TipoPublicacao(object):
    __table__ = 'tipo_publicacao'
    def __init__(self, id=None, titulo=None, locked=None, status=None, moderate_id=None, autor=None):
        self.id = id
        self.titulo = titulo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.autor = autor

    @classmethod
    def get_class_name(self):
        return "TipoPublicacao"

    @classmethod
    def get_list_title(self):
        return "Listagem de Tipos de Publicações"

    @classmethod
    def get_form_title(self):
        return "Tipo Publicação"

    @classmethod
    def get_default_field_order(self):
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Em Edição', 'Status', 'Moderação']
            fields = ['titulo', 'locked', 'status', 'moderate_id']
        else:
            colunms = ['Titulo']
            fields = ['titulo']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'titulo', form.titulo)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Tipo Publicacao ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Tipo Publicacao ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, status='A', locked='N')
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, status='W', locked='N')
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou o Tipo Publicacao ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

class Publicacao(object):
    __table__ = 'publicacao'
    def __init__(self, id=None, titulo=None, slug=None, data_hora=None, autor=None, data_publicacao=None, palavras_chaves=None, intro=None, completa=None, thumb_publicacao=None, slug_galeria=None, destaque=None, locked=None, status=None, moderate_id=None, permite_comentario=None, tipos=None, draft=None):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_hora = data_hora
        self.autor = autor
        self.data_publicacao = data_publicacao
        self.palavras_chaves = palavras_chaves
        self.intro = intro
        self.completa = completa
        self.thumb_publicacao = thumb_publicacao
        self.slug_galeria = slug_galeria
        self.destaque = destaque
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.permite_comentario = permite_comentario
        self.tipos = tipos
        self.draft = draft

    def get_tipos(self):
        data=db.select('publicacao_tipo_publicacao', None, '*', 'publicacao=%s' % str(self.id))
        tipos= [] 
        for row in data:
            tipos.append(str(row.tipo_publicacao))
        return tipos

    @classmethod
    def galeria(self):
        return db.select('galeria', None, '*', 'slug=%s' % str(self.slug_galeria))[0]
    
    @classmethod
    def fotos_picasa(self):
        pass

    @classmethod
    def fotos_facebook(self):
        pass

    @classmethod
    def fotos_servidor(self):
        galeria_folder = os.listdir(os.path.abspath(self.galeria().url_galeria))
        arquivos_folder = [f for f in os.listdir(rootpath + galeria_folder) if f.endswith('.jpg')]
        arquivos_folder.sort()
        return arquivos_folder

    @classmethod
    def get_class_name(self):
        return "Publicacao"

    @classmethod
    def get_list_title(self):
        return "Listagem de Publicações"

    @classmethod
    def get_form_title(self):
        return "Publicação"

    @classmethod
    def get_default_field_order(self):
        return "data_publicacao desc"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Tipos', 'Data/Hora', 'Permite Comentário', 'Destaque', 'Publicado', 'Editando', 'Status', 'Moderação', 'Rascunho']
            fields = ['titulo', 'tipos', 'data_hora', 'permite_comentario', 'destaque', 'data_publicacao', 'locked', 'status', 'moderate_id', 'draft']
        else:
            colunms = ['Titulo', 'Tipos', 'Data/Hora', 'Permite Comentário', 'Destaque', 'Publicado', 'Rascunho']
            fields = ['titulo', 'tipos', 'data_hora', 'permite_comentario', 'destaque', 'data_publicacao', 'draft']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'data_hora':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'data_publicacao':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'permite_comentario':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'destaque':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'draft':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None   
            elif field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            elif field == 'tipos':
                data = db.select('publicacao_tipo_publicacao', None, '*', 'publicacao=%s' % str(self.id))
                tipos = ""
                for row in data:
                    tipo = db.select('tipo_publicacao', None, '*', 'id=%s' % row.tipo_publicacao)[0]
                    tipos += tipo.titulo + "</br>"
                return tipos
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        slug = slugify(form.titulo)
        hoje = datetime.now()
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'slug', slug)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, data_hora=datetime.strptime(form.data_hora,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), palavras_chaves=form.palavras_chaves, intro=form.intro, completa=form.completa, thumb_publicacao=form.thumb_publicacao, slug_galeria=form.slug_galeria, destaque=form.destaque, draft=form.draft)
                        for tipo in form.tipos:
                            db.insert('publicacao_tipo_publicacao', publicacao=int(insert_id), tipo_publicacao=int(tipo))
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu a Publicacao ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, data_hora=datetime.strptime(form.data_hora,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), palavras_chaves=form.palavras_chaves, intro=form.intro, completa=form.completa, thumb_publicacao=form.thumb_publicacao, slug_galeria=form.slug_galeria, destaque=form.destaque, draft=form.draft)
                    for tipo in form.tipos:
                        db.insert('publicacao_tipo_publicacao', publicacao=int(insert_id), tipo_publicacao=int(tipo))
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu a Publicacao ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_hora=datetime.strptime(form.data_hora,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), palavras_chaves=form.palavras_chaves, intro=form.intro, completa=form.completa, thumb_publicacao=form.thumb_publicacao, slug_galeria=form.slug_galeria, destaque=form.destaque, status='A', locked='N', draft=form.draft)
                db.delete('publicacao_tipo_publicacao', where="publicacao=$id", vars=locals())
                for tipo in form.tipos:
                    db.insert('publicacao_tipo_publicacao', publicacao=int(id), tipo_publicacao=int(tipo))
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_hora=datetime.strptime(form.data_hora,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), palavras_chaves=form.palavras_chaves, intro=form.intro, completa=form.completa, thumb_publicacao=form.thumb_publicacao, slug_galeria=form.slug_galeria, destaque=form.destaque, status='W', locked='N', draft=form.draft)
                db.delete('publicacao_tipo_publicacao', where="publicacao=$id", vars=locals())
                for tipo in form.tipos:
                    db.insert('publicacao_tipo_publicacao', publicacao=int(id), tipo_publicacao=int(tipo))
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou a Publicacao ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

class Banner(object):
    __table__ = 'banner'
    def __init__(self, id=None, titulo=None, slug=None, autor=None, tipo=None, foto_banner=None, link_banner=None, exibir_pagina_inicial=None, ativo=None, count_clicks=None, custom_banner_code=None, locked=None, status=None, moderate_id=None, draft=None):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.autor = autor
        self.tipo = tipo
        self.foto_banner = foto_banner
        self.link_banner = link_banner
        self.exibir_pagina_inicial = exibir_pagina_inicial
        self.ativo = ativo
        self.count_clicks = count_clicks
        self.custom_banner_code = custom_banner_code
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.draft = draft

    @classmethod
    def get_class_name(self):
        return "Banner"

    @classmethod
    def get_list_title(self):
        return "Listagem de Banners"

    @classmethod
    def get_form_title(self):
        return "Banner"

    @classmethod
    def get_default_field_order(self):
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('draft', 'Rascunho')] 

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Tipo', 'Exibir Página Inicial', 'Ativo', 'QTDE Cliques', 'Editando', 'Status', 'Moderação', 'Rascunho']
            fields = ['titulo', 'tipo', 'exibir_pagina_inicial', 'ativo', 'count_clicks', 'locked', 'status', 'moderate_id', 'draft']
        else:
            colunms = ['Titulo', 'Tipo', 'Exibir Página Inicial', 'Ativo', 'QTDE Cliques', 'Rascunho']
            fields = ['titulo', 'tipo', 'exibir_pagina_inicial', 'ativo', 'count_clicks', 'draft']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'tipo':
                data = getattr(self, field)
                if data == 'S':
                    return 'SlideShow'
                elif data == 'P':
                    return 'Parceiro'
                else:
                    return 'Cliente'
            elif field == 'exibir_pagina_inicial':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'ativo':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'draft':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None   
            elif field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        slug = slugify(form.titulo)
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'slug', slug)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, autor=usuario.id, tipo=form.tipo, foto_banner=form.foto_banner, link_banner=form.link_banner, exibir_pagina_inicial=form.exibir_pagina_inicial, ativo=form.ativo, custom_banner_code=form.custom_banner_code, draft=form.draft)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Banner ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, autor=usuario.id, tipo=form.tipo, foto_banner=form.foto_banner, link_banner=form.link_banner, exibir_pagina_inicial=form.exibir_pagina_inicial, ativo=form.ativo, custom_banner_code=form.custom_banner_code, draft=form.draft)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Banner ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, autor=usuario.id, tipo=form.tipo, foto_banner=form.foto_banner, link_banner=form.link_banner, exibir_pagina_inicial=form.exibir_pagina_inicial, ativo=form.ativo, custom_banner_code=form.custom_banner_code, status='A', locked='N', draft=form.draft)
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, autor=usuario.id, tipo=form.tipo, foto_banner=form.foto_banner, link_banner=form.link_banner, exibir_pagina_inicial=form.exibir_pagina_inicial, ativo=form.ativo, custom_banner_code=form.custom_banner_code, status='W', locked='N', draft=form.draft)
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou o Banner ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

def get_images_slideshow():
    records = db.query("select titulo, foto_banner, link_banner from banner where ativo = 'S' AND tipo = 'S' AND exibir_pagina_inicial = 'S'")
    return records or None
    
class TipoDocumento(object):
    __table__ = 'tipo_documento'
    def __init__(self, id=None, titulo=None, locked=None, status=None, moderate_id=None, autor=None):
        self.id = id
        self.titulo = titulo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.autor = autor

    @classmethod
    def get_class_name(self):
        return "TipoDocumento"

    @classmethod
    def get_list_title(self):
        return "Listagem de Tipos de Documento"

    @classmethod
    def get_form_title(self):
        return "Tipo Documento"

    @classmethod
    def get_default_field_order(self):
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Em Edição', 'Status', 'Moderação']
            fields = ['titulo', 'locked', 'status', 'moderate_id']
        else:
            colunms = ['Titulo']
            fields = ['titulo']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'titulo', form.titulo)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, autor=usuario.id)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Tipo Documento ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, autor=usuario.id)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Tipo Documento ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, status='A', locked='N')
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, status='W', locked='N')
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou o Tipo Documento ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

class Documento(object):
    __table__ = 'documento'
    def __init__(self, id=None, titulo=None, slug=None, data_publicacao=None, autor=None, tipo=None, thumb_arquivo=None, link_arquivo=None, ativo=None, locked=None, status=None, moderate_id=None, draft=None):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_publicacao = data_publicacao
        self.autor = autor
        self.tipo = tipo
        self.thumb_arquivo = thumb_arquivo
        self.link_arquivo = link_arquivo
        self.ativo = ativo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.draft = draft

    @classmethod
    def get_class_name(self):
        return "Documento"

    @classmethod
    def get_list_title(self):
        return "Listagem de Documentos"

    @classmethod
    def get_form_title(self):
        return "Documento"

    @classmethod
    def get_default_field_order(self):
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Publicado', 'Tipo', 'Ativo', 'Editando', 'Status', 'Moderação', 'Rascunho']
            fields = ['titulo', 'data_publicacao', 'tipo', 'ativo', 'locked', 'status', 'moderate_id', 'draft']
        else:
            colunms = ['Titulo', 'Publicado', 'Tipo', 'Ativo', 'Rascunho']
            fields = ['titulo', 'data_publicacao', 'tipo', 'ativo', 'draft']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'tipo':
                data = getattr(self, field)
                return entity_by_id(TipoDocumento, data).titulo
            elif field == 'data_publicacao':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'ativo':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'draft':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        slug = slugify(form.titulo)
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'slug', slug)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, tipo=form.tipo, thumb_arquivo=form.thumb_arquivo, link_arquivo=form.link_arquivo, ativo=form.ativo, draft=form.draft)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o documento ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, tipo=form.tipo, thumb_arquivo=form.thumb_arquivo, link_arquivo=form.link_arquivo, ativo=form.ativo, draft=form.draft)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o documento ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, tipo=form.tipo, thumb_arquivo=form.thumb_arquivo, link_arquivo=form.link_arquivo, ativo=form.ativo, status='A', locked='N', draft=form.draft)
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, tipo=form.tipo, thumb_arquivo=form.thumb_arquivo, link_arquivo=form.link_arquivo, ativo=form.ativo, status='W', locked='N', draft=form.draft)
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou o documento ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

class Parametro(object):
    __table__ = 'parametro'
    def __init__(self, id=None, titulo=None, valor=None, locked=None, status=None, moderate_id=None, autor=None):
        self.id = id
        self.titulo = titulo
        self.valor = valor
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.autor = autor

    @classmethod
    def get_class_name(self):
        return "Parametro"

    @classmethod
    def get_list_title(self):
        return "Listagem de Parâmetros"

    @classmethod
    def get_form_title(self):
        return "Parâmetros"

    @classmethod
    def get_default_field_order(self):
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo')]

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Valor', 'Editando', 'Status', 'Moderação']
            fields = ['titulo', 'valor', 'locked', 'status', 'moderate_id']
        else:
            colunms = ['Titulo', 'Valor']
            fields = ['titulo', 'valor']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'titulo', form.titulo)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, valor=form.valor, autor=usuario.id)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o parametro ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, valor=form.valor, autor=usuario.id)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o parametro ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, valor=form.valor, status='A', locked='N')
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, valor=form.valor, status='W', locked='N')
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou a parametro ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

class Galeria(object):
    __table__ = 'galeria'
    def __init__(self, id=None, titulo=None, slug=None, data_criacao=None, autor=None, tipo=None, midia=None, url_galeria=None, locked=None, status=None, moderate_id=None, permite_comentario=None, draft=None):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_criacao = data_criacao
        self.autor = autor
        self.tipo = tipo
        self.midia = midia
        self.url_galeria = url_galeria
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.permite_comentario = permite_comentario
        self.draft = draft

    @classmethod
    def get_class_name(self):
        return "Galeria"

    @classmethod
    def get_list_title(self):
        return "Listagem de Galerias"

    @classmethod
    def get_form_title(self):
        return "Galeria"

    @classmethod
    def get_default_field_order(self):
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('draft', 'Rascunho')] 

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Tipo', 'Midia', 'Permite Comentário', 'Editando', 'Status', 'Moderação', 'Rascunho']
            fields = ['titulo', 'tipo', 'midia', 'permite_comentario', 'locked', 'status', 'moderate_id', 'draft']
        else:
            colunms = ['Titulo', 'Tipo', 'Midia', 'Permite Comentário', 'Rascunho']
            fields = ['titulo', 'tipo', 'midia', 'permite_comentario', 'draft']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'tipo':
                data = getattr(self, field)
                if data == 'P':
                    return 'Picasa'
                elif data == 'F':
                    return 'Facebook'
                elif data == 'Y':
                    return 'Youtube'
                else:
                    return 'Servidor/Hospedagem'
            if field == 'midia':
                data = getattr(self, field)
                if data == 'F':
                    return 'Foto'
                else:
                    return 'Video'
            elif field == 'data_criacao':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'draft':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None  
            elif field == 'permite_comentario':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        slug = slugify(form.titulo)
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'slug', slug)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, tipo=form.tipo, midia=form.midia, url_galeria=form.url_galeria, data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, draft=form.draft)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu a galeria ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, tipo=form.tipo, midia=form.midia, url_galeria=form.url_galeria, data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, draft=form.draft)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu a galeria ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, tipo=form.tipo, midia=form.midia, url_galeria=form.url_galeria, data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S'), status='A', locked='N', draft=form.draft)
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, tipo=form.tipo, midia=form.midia, url_galeria=form.url_galeria, data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S'), status='W', locked='N', draft=form.draft)
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou a galeria ' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

class Moderacao(object):
    __table__ = 'moderacao'
    def __init__(self, id=None, data_hora=None, autor=None, onde=None, operacao=None, moderador=None, data_hora_operacao=None, acao=None, detalhamento=None):
        self.id = id
        self.data_hora = data_hora
        self.autor = autor
        self.onde = onde
        self.operacao = operacao
        self.moderador = moderador
        self.data_hora_operacao = data_hora_operacao
        self.acao = acao
        self.detalhamento = detalhamento

    @classmethod
    def get_class_name(self):
        return "Moderacao"

    @classmethod
    def get_list_title(self):
        return "Listagem de Moderações"

    @classmethod
    def get_form_title(self):
        return "Moderação"

    @classmethod
    def get_default_field_order(self):
        return "data_hora_operacao DESC"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('texto', 'Texto')] 

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Inclusão', 'Autor', 'Onde', 'Operação', 'Detalhamento', 'Moderador', 'Data Ação', 'Ação']
        fields = ['data_hora', 'autor', 'onde', 'operacao', 'detalhamento', 'moderador', 'data_hora_operacao', 'acao']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'data_hora':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'data_hora_operacao':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'autor':
                data = getattr(self, field)
                return entity_by_id(Usuario, data).login
            elif field == 'moderador':
                data = getattr(self, field)
                if data:
                    return entity_by_id(Usuario, data).login
                else:
                    return None
            else:
                return getattr(self, field)

class Template(object):
    __table__ = 'template'
    def __init__(self, id=None, titulo=None, slug=None, data_publicacao=None, autor=None, path=None, ativo=None, locked=None, status=None, moderate_id=None, draft=None):
        self.id = id
        self.titulo = titulo
        self.slug=slug
        self.data_publicacao=data_publicacao
        self.autor=autor
        self.path=path
        self.ativo=ativo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id
        self.draft = draft

    @classmethod
    def get_class_name(self):
        return "Template"

    @classmethod
    def get_list_title(self):
        return "Listagem de Templates"

    @classmethod
    def get_form_title(self):
        return "Template"

    @classmethod
    def get_default_field_order(self):
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo'), ('draft','Rascunho')] 

    @classmethod
    def exposed_list_properties(self):
        if CONTROL_CONCURRENT_ACCESS:
            colunms = ['Titulo', 'Publicação', 'Ativo', 'Em Edição', 'Status', 'Moderação', 'Rascunho']
            fields = ['titulo', 'data_publicacao', 'ativo', 'locked', 'status', 'moderate_id', 'draft']
        else:
            colunms = ['Titulo', 'Publicação', 'Ativo', 'Rascunho']
            fields = ['titulo', 'data_publicacao', 'ativo', 'draft']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): 
            if field == 'data_publicacao':
                data = getattr(self, field)
                if data:
                    return data.strftime('%d/%m/%Y %H:%M:%S')
                else:
                    return None
            elif field == 'ativo':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='active_result'>Sim</span>"
                    else:
                        return "<span class='inactive_result'>Não</span>"
                else:
                    return None
            elif field == 'draft':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None   
            elif field == 'locked':
                data = getattr(self, field)
                if data:
                    if data == 'S':
                        return "<span class='locked_yes'>Sim</span>"
                    else:
                        return "<span class='locked_no'>Não</span>"
                else:
                    return None
            elif field == 'status':
                data = getattr(self, field)
                if data:
                    if data == 'W':
                        return "<span class='status_waiting'>Waiting</span>"
                    elif data == 'A':
                        return "<span class='status_approved'>Approved</span>"
                    elif data == 'R':
                        return "<span class='status_recused'>Recused</span>"
                else:
                    return None
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id=id != '' and id != 'NULL' and id != None and id != 'None'
        slug = slugify(form.titulo)
        from auth import get_logged_user
        usuario = get_logged_user()
        if not has_id:
            try:
                entity=exists_entity(self.__table__, 'slug', form.slug)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    t = db.transaction()
                    try:
                        insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, path=form.path, ativo=form.ativo, draft=form.draft)
                        if AUTO_MODERATE:
                            db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                        else:
                            db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                            moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Aviso ' + form.titulo)
                            db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                    except:
                        t.rollback()
                        raise
                    else:
                        t.commit()
            except IndexError:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__, titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, path=form.path, ativo=form.ativo, draft=form.draft)
                    if AUTO_MODERATE:
                        db.update(self.__table__, where="id=$insert_id", status='A', vars=locals())
                    else:
                        db.update(self.__table__, where="id=$insert_id", status='W', vars=locals())
                        moderate_id = db.insert('moderacao', data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), insert_id), operacao='Inserir', detalhamento='Inseriu o Aviso ' + form.titulo)
                        db.update(self.__table__, where="id=$insert_id", moderate_id='%s' % moderate_id, vars=locals())
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            if AUTO_MODERATE:
                db.update(self.__table__, where="id > 0", ativo='N')
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, path=form.path, ativo=form.ativo, status='A', locked='N', draft=form.draft)
            else:
                db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_publicacao=datetime.strptime(form.data_publicacao,'%Y-%m-%d %H:%M:%S'), autor=usuario.id, path=form.path, ativo=form.ativo, status='W', locked='N', draft=form.draft)
                db.update('moderacao', where="id=%s" % form.moderate_id, data_hora=datetime.now(), autor=usuario.id, onde=generate_url(self.get_class_name(), id), operacao='Editar', detalhamento='Alterou o Template' + form.titulo, moderador=None, data_hora_operacao=None, acao=None)

# Generic Functions
def get_publicacoes(tipo_publicacao):
    records = db.query("select n.titulo, n.slug, n.intro, n.data_hora, n.thumb_publicacao, (select login from usuario where id = n.autor) as autor from publicacao n inner join publicacao f ON f.id = n.id AND f.status = 'A' inner join publicacao_tipo_publicacao p ON p.publicacao = n.id AND p.tipo_publicacao = (select t.id from tipo_publicacao t where t.titulo like '%(tipo_publicacao)s') order by n.data_hora desc" % {'tipo_publicacao': tipo_publicacao})
    return records or None

def get_publicacoes_rss(tipo_publicacao):
    records = db.query("select n.titulo, n.slug, n.intro, n.data_hora, (select login from usuario where id = n.autor) as autor from publicacao n inner join publicacao f ON f.id = n.id AND f.status = 'A' AND f.data_hora>=cast(now() as date)-15 inner join publicacao_tipo_publicacao p ON p.publicacao = n.id AND p.tipo_publicacao = (select t.id from tipo_publicacao t where t.titulo like '%(tipo_publicacao)s') order by n.data_hora desc" % {'tipo_publicacao': tipo_publicacao})
    return records or None

def get_publicacao(endereco):
    try:
        record = db.query("select n.titulo, n.slug, n.completa, n.data_hora, n.thumb_publicacao,  (select u.login from usuario u where u.id = n.autor) as autor from publicacao n where n.slug = '%(endereco)s'" % {'endereco': endereco})[0]
        return record
    except IndexError:
        return None

def get_banners_produtos():
    records = db.query("select titulo, foto_banner, link_banner from banner where ativo = 'S' AND tipo = 'P'")
    return records or None

def get_banners_internos():
    records = db.query("select titulo, foto_banner, link_banner from banner where ativo = 'S' AND tipo = 'I'")
    return records or None

def get_active_admin_modules():
    records = db.query("select class_name, titulo from modulo where ativo = 'S' AND perfil_acesso like 'A%'")
    return records or None

def get_active_oper_modules():
    records = db.query("select class_name, titulo from modulo where ativo = 'S' AND perfil_acesso like 'AO%'")
    return records or None

def get_active_moderate_modules():
    records = db.query("select class_name, titulo from modulo where ativo = 'S' AND perfil_acesso like 'AM%'")
    return records or None

def get_active_template():
    record = db.query("select path from template where ativo = 'S'")[0]
    return record or None

def get_menu_itens():
    menus = select_approved(Menu)
    menu_sup = 0
    tem_submenu = False
    menu_html = ''
    for menu in menus:
        nivel = int(menu.nivel)
        if nivel == 1:
            if tem_submenu:
                menu_html = menu_html + "</ul>"
                menu_html = menu_html + "</li>"
                tem_submenu = False
            menu_sup = str(menu.id)
            menu_html = menu_html + "<li><a href='" + menu.endereco + "' title='" + menu.descricao + "' id='menu_" + menu.titulo.lower() + "'>" + menu.titulo + "</a>"
        elif nivel == 2:
            if menu.menu_pai is not None:
                if str(menu_sup) == str(menu.menu_pai.id):
                    if tem_submenu == False:
                        tem_submenu = True
                        menu_html = menu_html + '<ul>'                    
                    menu_html = menu_html + "<li><a href='" + menu.endereco + "' title='" + menu.descricao + "' id='menu_" + menu.titulo.lower() + "'>" + menu.titulo + "</a>"
    if tem_submenu:
        menu_html = menu_html + "</ul>"
    menu_html = menu_html + "</li>"
    #print ' ======== HTML MENU ========= ' + menu_html
    return menu_html    

def login(login, senha):
    ident = db.query("select * from usuario where login = '%(login)s' and senha = '%(senha)s'" % {'login': login, 'senha': senha})[0]
    logado = None
    if ident:
        logado = Usuario(id=ident['id'], login=ident['login'], senha=ident['senha'], nivel_acesso=ident['nivel_acesso'])
    return logado

def get_exposed_managed_tables(nivel_acesso):
    values = []
    if nivel_acesso == 1:
        from configuration import ACTIVE_MODULES_ADMIN
        for module in ACTIVE_MODULES_ADMIN:
            values.append({'model_table': module[0], 'icon_file': '/static/images/' + module[0] + '.png', 'class_name': module[1]})
    elif nivel_acesso == 2:
        from configuration import ACTIVE_MODULES_OPER
        for module in ACTIVE_MODULES_OPER:
            values.append({'model_table': module[0], 'icon_file': '/static/images/' + module[0] + '.png', 'class_name': module[1]})
    elif nivel_acesso == 3:
        from configuration import ACTIVE_MODULES_MODER
        for module in ACTIVE_MODULES_MODER:
            values.append({'model_table': module[0], 'icon_file': '/static/images/' + module[0] + '.png', 'class_name': module[1]})
    return values

def latest_records(entity, q=None, start=1, PAGESIZE=10, order=None):
    limit=int(PAGESIZE)
    has_query=q != '' and q != 'NULL' and q != None and q != 'None' and q != 'all'
    if has_query:
        data = db.select(entity.__table__, None, '*', q, order, None, limit, int(start), False)
    else:
        data = db.select(entity.__table__, None, '*', None, order, None, limit, int(start), False)
    items = [ entity(**row) for row in data ]
    return items

def latest_publicacao_records(entity, q=None, start=1, PAGESIZE=10, order=None):
    limit=int(PAGESIZE)
    has_query=q != '' and q != 'NULL' and q != None and q != 'None' and q != 'all'
    if has_query:
        data = db.select(entity, None, '*', q, order, None, limit, int(start), False)
        return data
    else:
        data = db.select(entity, None, '*', None, order, None, limit, int(start), False)
        return data

def count_records(entity):
    qtde = db.query("select count(id) as value from %s" % entity.__table__)[0]
    return int(qtde['value'])

def count_records_publicacao(entity):
    qtde = db.query("select count(titulo) as value from %s" % entity)[0]
    return int(qtde['value'])

def entity_by_id(entity, id):
    try:
        return db.select(entity.__table__, where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def object_by_id(entity, id):
    try:
        row=db.select(entity.__table__, where='id=$id', vars=locals())[0]
        return entity(**row)
    except IndexError:
        return None

def entity_by_slug(entity, slug):
    try:
        return db.select(entity.__table__, where='slug=$slug', vars=locals())[0]
    except IndexError:
        return None

def delete_entity(entity, id):
    _obj = entity_by_id(entity, id);
    if AUTO_MODERATE:
        if entity.__table__ == 'publicacao':
            db.delete('publicacao_tipo_publicacao', where="publicacao=$id", vars=locals())
            db.delete('publicacao', where="id=$id", vars=locals())
        else:
            db.delete(entity.__table__, where="id=$id", vars=locals())
    else:
        if _obj.status == 'R':
            t = db.transaction()
            try:
                if entity.__table__ == 'publicacao':
                    db.delete('publicacao_tipo_publicacao', where="publicacao=$id", vars=locals())
                    db.delete('publicacao', where="id=$id", vars=locals())
                    db.delete('moderacao', where="id=%s" % _obj.moderate_id, vars=locals())
                else:
                    db.delete(entity.__table__, where="id=$id", vars=locals())
                    db.delete('moderacao', where="id=%s" % _obj.moderate_id, vars=locals())
            except:
                t.rollback()
                raise
            else:
                t.commit()
        else:
            t = db.transaction()
            try:
                db.update(entity.__table__, where="id=$id", vars=locals(), locked='N')
                db.update('moderacao', where="id=%s" % _obj.moderate_id, data_hora=datetime.now(), autor=_obj.autor, onde=generate_url(entity.get_class_name(), _obj.id), operacao='Excluir', detalhamento='Exluiu ' + entity.get_class_name() + " com o valor: " + _obj.titulo, moderador=None, data_hora_operacao=None, acao=None)
            except:
                t.rollback()
                raise
            else:
                t.commit()

def update_entity_lock(entity, id, value):
    return db.update('%s' % entity.__table__, where="id=$id", locked= '%(value)s' % {'value': value}, vars=locals())

def generate_url(entity, id):
    caminho = str(web.ctx.home) + "/editar/" + entity + "/" + str(id) + '?op=moderate_on'
    str_cota = '"'
    return  "<a href='javascript: void(0)' onclick=" + str_cota + "popup('" + caminho + "')" + str_cota + ">" + entity + "</a>"

def exists_entity(entity, field, value):
    return db.select('%s' % entity, where="%(field)s='%(value)s'" % {'field': field, 'value': value}, vars=locals())[0] or None

def find_slug(Entity, slug):
    q = db.Query(Entity).filter('slug =', slug).get()
    return q is not None

def get_entity_index_list(entity, filtro, valor, order, limit):
    query = db.Query(entity)
    if filtro is not None:
        q = db.Query(entity).filter('%s = ' % filtro, valor)
        q.order(order)
        return q.fetch(limit)
    else:
        query = db.Query(entity)
        query.order(order)
        return query.fetch(limit)

def select(entity):
    data = db.select(entity.__table__)
    items = [ entity(**row) for row in data ]
    return items

def select_approved(entity):
    data = db.select(entity.__table__, where="status='A'")
    items = [ entity(**row) for row in data ]
    return items

def moderate(verb, record_id):
    from auth import get_logged_user
    usuario = get_logged_user()
    moderate_record = entity_by_id(Moderacao, record_id)
    record_value = moderate_record.onde.split('/')
    record_class = record_value[5]
    related_id = record_value[6][0:record_value[6].find('?')]
    class_obj = globals()[record_class]
    instance_obj = class_obj()
    if verb == 'approves':
        if instance_obj.__table__=='template':
            db.update(instance_obj.__table__, where="id > 0", ativo='N')
        db.update('%s' % instance_obj.__table__, where="id=$related_id", status= 'A', vars=locals())
        db.update('moderacao', where="id=$record_id", moderador=usuario.id, data_hora_operacao=datetime.now(), acao='A', vars=locals())
    else:
        db.update('%s' % instance_obj.__table__, where="id=$related_id", status= 'R', vars=locals())
        db.update('moderacao', where="id=$record_id", moderador=usuario.id, data_hora_operacao=datetime.now(), acao='R', vars=locals())
