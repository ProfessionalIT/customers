# -*- coding: utf-8 -*-
import web
from configuration import DBN, HOST, DB, USER, PWD
from utils import slugify, versionate, replace_separator, moeda_brasileira
from datetime import datetime

db = web.database(dbn=DBN, host=HOST, db=DB, user=USER, pw=PWD)

class ExistValueException(Exception):
   def __init__(self, value):
       self.parameter = "Existe um registro no banco de dados com esse valor: %s " % value
   def __str__(self):
       return repr(self.parameter)

# App Models.
class Usuario(object):
    __table__ = 'website_usuario'
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
                    db.insert(self.__table__, login=form.login, senha=form.senha, nivel_acesso=int(form.nivel_acesso))
            except IndexError:
                db.insert(self.__table__, login=form.login, senha=form.senha, nivel_acesso=int(form.nivel_acesso))
        else:
            db.update(self.__table__, where="id=$id", vars=locals(), login=form.login, senha=form.senha, nivel_acesso=int(form.nivel_acesso))

class Log(object):
    __table__ = 'website_log'
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
        db.insert('website_log', usuario=record['usuario'], operacao=record['operacao'], endereco_ip=record['endereco_ip'], log=record['log'], data=datetime.now(), menu=record['menu'])

class Pagina(object):
    __table__ = 'website_pagina'
    def __init__(self, id, titulo, slug, descricao_completa, palavras_chaves, data_criacao, ultima_alteracao, usuario_alteracao, conteudo, locked, status, moderate_id):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.descricao_completa = descricao_completa
        self.palavras_chaves = palavras_chaves
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.usuario_alteracao = usuario_alteracao
        self.conteudo = conteudo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id

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
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Titulo']
        fields = ['titulo']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): return getattr(self, field)

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
                    db.insert(self.__table__, titulo=form.titulo, slug=slug, descricao_completa=form.descricao_completa, palavras_chaves=form.palavras_chaves, data_criacao=hoje, ultima_alteracao=hoje, usuario_alteracao=usuario.id, conteudo=form.conteudo, locked='N', status='A', moderate_id=int('1'))
            except IndexError:
                db.insert(self.__table__, titulo=form.titulo, slug=slug, descricao_completa=form.descricao_completa, palavras_chaves=form.palavras_chaves, data_criacao=hoje, ultima_alteracao=hoje, usuario_alteracao=usuario.id, conteudo=form.conteudo, locked='N', status='A', moderate_id=int('1'))
        else:
            db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, descricao_completa=form.descricao_completa, palavras_chaves=form.palavras_chaves, ultima_alteracao=hoje, usuario_alteracao=usuario.id, conteudo=form.conteudo, locked='N', status='A', moderate_id=int('1'))

def get_pagina(endereco):
    record = db.query("select titulo, descricao_completa, palavras_chaves, conteudo from website_pagina where slug = '%(endereco)s'" % {'endereco': endereco})[0]
    return record or None

class Produto(object):
    __table__ = 'website_produto'
    def __init__(self, id, titulo, slug, data_criacao, ultima_alteracao, usuario_alteracao, caracteristicas, palavras_chaves, url_galeria, locked, status, moderate_id):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.usuario_alteracao = usuario_alteracao
        self.caracteristicas = caracteristicas
        self.palavras_chaves = palavras_chaves
        self.url_galeria = url_galeria
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id

    @classmethod
    def get_class_name(self):
        return "Produto"

    @classmethod
    def get_list_title(self):
        return "Listagem de Produtos"

    @classmethod
    def get_form_title(self):
        return "Produto"

    @classmethod
    def get_default_field_order(self):
        return "id"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Titulo']
        fields = ['titulo']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): return getattr(self, field)

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
                    db.insert(self.__table__, titulo=form.titulo, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, usuario_alteracao=usuario.id, caracteristicas=form.caracteristicas, palavras_chaves=form.palavras_chaves, url_galeria=form.url_galeria, locked='N', status='A', moderate_id=int('1'))
            except IndexError:
                db.insert(self.__table__, titulo=form.titulo, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, usuario_alteracao=usuario.id, caracteristicas=form.caracteristicas, palavras_chaves=form.palavras_chaves, url_galeria=form.url_galeria, locked='N', status='A', moderate_id=int('1'))
        else:
            db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, usuario_alteracao=usuario.id, caracteristicas=form.caracteristicas, palavras_chaves=form.palavras_chaves, url_galeria=form.url_galeria, locked='N', status='A', moderate_id=int('1'))

def all_produtos_rss():
    records = db.query("select titulo, slug, caracteristicas, data_criacao from website_produto")
    return records or None

def get_produto(slug_produto):
    record = db.query("select titulo, slug, caracteristicas, palavras_chaves, url_galeria from website_produto where slug = '%(endereco)s'" % {'endereco': slug_produto})[0]
    return record or None

class Promocao(object):
    __table__ = 'website_promocao'
    def __init__(self, id, titulo, slug, data_criacao, ultima_alteracao, usuario_alteracao, conteudo, ativo, locked, status, moderate_id):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.usuario_alteracao = usuario_alteracao
        self.conteudo = conteudo
        self.ativo = ativo
        self.locked = locked
        self.status = status
        self.moderate_id = moderate_id

    @classmethod
    def get_class_name(self):
        return "Promocao"

    @classmethod
    def get_list_title(self):
        return "Listagem de Promoções"

    @classmethod
    def get_form_title(self):
        return "Promoção"

    @classmethod
    def get_default_field_order(self):
        return "id"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('titulo', 'Titulo')] 

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Titulo', 'Ativo']
        fields = ['titulo', 'ativo']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field): return getattr(self, field)

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
                    db.insert(self.__table__, titulo=form.titulo, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, usuario_alteracao=usuario.id, conteudo=form.conteudo, ativo=form.ativo, locked='N', status='A', moderate_id=int('1'))
            except IndexError:
                db.insert(self.__table__, titulo=form.titulo, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, usuario_alteracao=usuario.id, conteudo=form.conteudo, ativo=form.ativo, locked='N', status='A', moderate_id=int('1'))
        else:
            db.update(self.__table__, where="id=$id", vars=locals(), titulo=form.titulo, slug=slug, data_criacao=hoje, ultima_alteracao=hoje, usuario_alteracao=usuario.id, conteudo=form.conteudo, ativo=form.ativo, locked='N', status='A', moderate_id=int('1'))

def get_promocoes():
    records = db.query("select conteudo from website_promocao where ativo= 'S'")
    return records or None

# Generic Functions
def login(login, senha):
    ident = None
    logado = None
    try:
        ident = db.query("select * from website_usuario where login = '%(login)s' and senha = '%(senha)s'" % {'login': login, 'senha': senha})[0]
    except:
        raise
    if ident:
        logado = Usuario(id=ident['id'], login=ident['login'], senha=ident['senha'], nivel_acesso=ident['nivel_acesso'])
    return logado

def get_exposed_managed_tables():
    values = []
    values.append({'model_table': 'Usuario', 'icon_file': '/static/images/Usuario.png', 'class_name': 'Usuários'})
    values.append({'model_table': 'Pagina', 'icon_file': '/static/images/Pagina.png', 'class_name': 'Páginas'})
    values.append({'model_table': 'Produto', 'icon_file': '/static/images/Produto.png', 'class_name': 'Produtos'})
    values.append({'model_table': 'Promocao', 'icon_file': '/static/images/Promocao.png', 'class_name': 'Promoção'})
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

def count_records(entity):
    qtde = db.query("select count(id) as value from %s" % entity.__table__)[0]
    return int(qtde['value'])

def entity_by_id(entity, id):
    try:
        return db.select(entity.__table__, where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def entity_by_slug(entity, slug):
    try:
        return db.select(entity.__table__, where='slug=$slug', vars=locals())[0]
    except IndexError:
        return None

def delete_entity(entity, id):
    db.delete(entity.__table__, where="id=$id", vars=locals())

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
