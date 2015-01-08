# -*- coding: utf-8 -*-
import web
from configuration import DBN, HOST, DB, USER, PWD
from utils import slugify
from datetime import datetime

db = web.database(dbn=DBN, host=HOST, db=DB, user=USER, pw=PWD)


class ExistValueException(Exception):

    def __init__(self, value):
        self.parameter = """Existe um registro no banco de dados
                           com esse valor: %s """ % value

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
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    def __str__(self):
        if self is not None:
            if self.login:
                return self.login

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        if not has_id:
            try:
                entity = exists_entity(self.__table__, 'login', form.login)
                if (entity is not None):
                    raise ExistValueException(form.login)
                else:
                    db.insert(self.__table__,
                              login=form.login,
                              senha=form.senha,
                              nivel_acesso=int(form.nivel_acesso))
            except IndexError:
                db.insert(self.__table__,
                          login=form.login,
                          senha=form.senha,
                          nivel_acesso=int(form.nivel_acesso))
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      login=form.login,
                      senha=form.senha,
                      nivel_acesso=int(form.nivel_acesso))


class Log(object):

    __table__ = 'website_log'

    def __init__(self,
                 id=None,
                 usuario=None,
                 operacao=None,
                 endereco_ip=None,
                 log=None,
                 data=None,
                 menu=None):
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
        return [('all', 'Todos'),
                ('usuario', 'Usuário'),
                ('operacao', 'Operação'),
                ('endereco_ip', 'Endereço IP'),
                ('log', 'Log')]

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Usuario', 'Operação', 'Endereço IP', 'Log', 'Data', 'Menu']
        fields = ['usuario', 'operacao', 'endereco_ip', 'log', 'data', 'menu']
        attributes = {'colunms': colunms, 'fields': fields}
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
            elif field == 'menu':
                id = getattr(self, field)
                menu = entity_by_id(Menu, id)
                if menu:
                    return menu.endereco
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
        db.insert('website_log',
                  usuario=record['usuario'],
                  operacao=record['operacao'],
                  endereco_ip=record['endereco_ip'],
                  log=record['log'],
                  data=datetime.now(),
                  menu=record['menu'])


class Pagina(object):
    """
    pass
    """

    __table__ = 'website_pagina'

    def __init__(self,
                 id,
                 titulo,
                 slug,
                 descricao_completa,
                 palavras_chaves,
                 data_criacao,
                 ultima_alteracao,
                 usuario_alteracao,
                 conteudo):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.descricao_completa = descricao_completa
        self.palavras_chaves = palavras_chaves
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.usuario_alteracao = usuario_alteracao
        self.conteudo = conteudo

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
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        from auth import get_logged_user
        usuario = get_logged_user()
        hoje = datetime.now()
        slug = slugify(form.titulo)
        if not has_id:
            try:
                entity = exists_entity(self.__table__, 'titulo', form.titulo)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    db.insert(self.__table__,
                              titulo=form.titulo,
                              slug=slug,
                              descricao_completa=form.descricao_completa,
                              palavras_chaves=form.palavras_chaves,
                              data_criacao=hoje,
                              ultima_alteracao=hoje,
                              usuario_alteracao=usuario.id,
                              conteudo=form.conteudo)
            except IndexError:
                db.insert(self.__table__,
                          titulo=form.titulo,
                          slug=slug,
                          descricao_completa=form.descricao_completa,
                          palavras_chaves=form.palavras_chaves,
                          data_criacao=hoje,
                          ultima_alteracao=hoje,
                          usuario_alteracao=usuario.id,
                          conteudo=form.conteudo)
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      titulo=form.titulo,
                      slug=slug,
                      descricao_completa=form.descricao_completa,
                      palavras_chaves=form.palavras_chaves,
                      ultima_alteracao=hoje,
                      usuario_alteracao=usuario.id,
                      conteudo=form.conteudo)


def get_pagina(endereco):
    record = db.query("""select titulo, descricao_completa, palavras_chaves,
                         conteudo from website_pagina where slug =
                         '%(endereco)s'""" % {'endereco': endereco})[0]
    return record or None


class Menu(object):

    __table__ = 'website_menu'

    def __init__(self,
                 id,
                 ordem,
                 titulo,
                 descricao,
                 slug,
                 data_criacao,
                 ultima_alteracao,
                 usuario_alteracao,
                 pagina,
                 endereco,
                 menu_pai,
                 nivel,
                 key_words):
        self.id = id
        self.ordem = ordem
        self.titulo = titulo
        self.descricao = descricao
        self.slug = slug
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.usuario_alteracao = usuario_alteracao
        self.pagina = pagina
        self.endereco = endereco
        self.menu_pai = menu_pai
        self.nivel = nivel
        self.key_words = key_words

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
        return [('all', 'Todos'),
                ('ordem', 'Ordem'),
                ('nivel', 'Nível'),
                ('titulo', 'Titulo')]

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Ordem', 'Nivel', 'Titulo', 'Endereço']
        fields = ['ordem', 'nivel', 'titulo', 'endereco']
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        hoje = datetime.now()
        from auth import get_logged_user
        usuario = get_logged_user()
        slug = slugify(form.titulo)
        if not has_id:
            try:
                entity = exists_entity(self.__table__, 'titulo', form.titulo)
                if (entity is not None):
                    raise ExistValueException(form.titulo)
                else:
                    db.insert(self.__table__,
                              ordem=int(form.ordem),
                              titulo=form.titulo,
                              descricao=form.descricao,
                              slug=slug,
                              data_criacao=hoje,
                              ultima_alteracao=hoje,
                              usuario_alteracao=int(usuario.id),
                              pagina=int(form.pagina) or None,
                              endereco=form.endereco,
                              menu_pai=int(form.menu_pai) or None,
                              nivel=int(form.nivel),
                              key_words=form.key_words)
            except IndexError:
                db.insert(self.__table__,
                          ordem=int(form.ordem),
                          titulo=form.titulo,
                          descricao=form.descricao,
                          slug=slug,
                          data_criacao=hoje,
                          ultima_alteracao=hoje,
                          usuario_alteracao=int(usuario.id),
                          pagina=int(form.pagina) or None,
                          endereco=form.endereco,
                          menu_pai=int(form.menu_pai) or None,
                          nivel=int(form.nivel),
                          key_words=form.key_words)
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      ordem=int(form.ordem),
                       titulo=form.titulo,
                       descricao=form.descricao,
                       slug=slug,
                       data_criacao=hoje,
                       ultima_alteracao=hoje,
                       usuario_alteracao=usuario.id,
                       pagina=int(form.pagina) or None,
                       endereco=form.endereco,
                       menu_pai=int(form.menu_pai) or None,
                       nivel=int(form.nivel),
                       key_words=form.key_words)


class Proprietario(object):

    __table__ = 'website_proprietario'

    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    @classmethod
    def get_class_name(self):
        return "Proprietario"

    @classmethod
    def get_list_title(self):
        return "Listagem de Proprietários"

    @classmethod
    def get_form_title(self):
        return "Proprietáro"

    @classmethod
    def get_default_field_order(self):
        return "nome"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('nome', 'Nome')]

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Nome']
        fields = ['nome']
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        if not has_id:
            try:
                entity = exists_entity(self.__table__, 'nome', form.nome)
                if (entity is not None):
                    raise ExistValueException(form.nome)
                else:
                    db.insert(self.__table__, nome=form.nome)
            except IndexError:
                db.insert(self.__table__, nome=form.nome)
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      nome=form.nome)


class Agenciador(object):

    __table__ = 'website_agenciador'

    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    @classmethod
    def get_class_name(self):
        return "Agenciador"

    @classmethod
    def get_list_title(self):
        return "Listagem de Agenciadores"

    @classmethod
    def get_form_title(self):
        return "Agênciador"

    @classmethod
    def get_default_field_order(self):
        return "nome"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('nome', 'Nome')]

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Nome']
        fields = ['nome']
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        if not has_id:
            try:
                entity = exists_entity(self.__table__, 'nome', form.nome)
                if (entity is not None):
                    raise ExistValueException(form.nome)
                else:
                    db.insert(self.__table__, nome=form.nome)
            except IndexError:
                db.insert(self.__table__, nome=form.nome)
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      nome=form.nome)


class Corretor(object):

    __table__ = 'website_corretor'

    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    @classmethod
    def get_class_name(self):
        return "Corretor"

    @classmethod
    def get_list_title(self):
        return "Listagem de Corretores"

    @classmethod
    def get_form_title(self):
        return "Corretor"

    @classmethod
    def get_default_field_order(self):
        return "nome"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('nome', 'Nome')]

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Nome']
        fields = ['nome']
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        if not has_id:
            try:
                entity = exists_entity(self.__table__, 'nome', form.nome)
                if (entity is not None):
                    raise ExistValueException(form.nome)
                else:
                    db.insert(self.__table__, nome=form.nome)
            except IndexError:
                db.insert(self.__table__, nome=form.nome)
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      nome=form.nome)


class OrigemImovel(object):

    __table__ = 'website_origem_imovel'

    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    @classmethod
    def get_class_name(self):
        return "OrigemImovel"

    @classmethod
    def get_list_title(self):
        return "Listagem de Origens de Imóvel"

    @classmethod
    def get_form_title(self):
        return "Origem Imóvel"

    @classmethod
    def get_default_field_order(self):
        return "nome"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('nome', 'Nome')]

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Nome']
        fields = ['nome']
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        if not has_id:
            try:
                entity = exists_entity(self.__table__, 'nome', form.nome)
                if (entity is not None):
                    raise ExistValueException(form.nome)
                else:
                    db.insert(self.__table__, nome=form.nome)
            except IndexError:
                db.insert(self.__table__, nome=form.nome)
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      nome=form.nome)


class TipoImovel(object):

    __table__ = 'website_tipo_imovel'

    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    @classmethod
    def get_class_name(self):
        return "TipoImovel"

    @classmethod
    def get_list_title(self):
        return "Listagem de Tipos de Imóvel"

    @classmethod
    def get_form_title(self):
        return "Tipo Imóvel"

    @classmethod
    def get_default_field_order(self):
        return "nome"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('nome', 'Nome')]

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Nome']
        fields = ['nome']
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        if not has_id:
            try:
                entity = exists_entity(self.__table__, 'nome', form.nome)
                if (entity is not None):
                    raise ExistValueException(form.nome)
                else:
                    db.insert(self.__table__, nome=form.nome)
            except IndexError:
                db.insert(self.__table__, nome=form.nome)
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      nome=form.nome)


def get_imoveis_venda_destaque():
    return db.select('qry_imovel_venda_destaque', vars=locals())


def get_imoveis_locacao_destaque():
    return db.select('qry_imovel_locacao_destaque', vars=locals())


def get_imoveis_lista(utilidade, finalidade, tipo, quantidade_dormitorios):
    if quantidade_dormitorios > 0:
        if utilidade == 'residencial':
            if finalidade == 'locacao':
                where_dict = {'utilidade_residencial': 'S',
                              'finalidade_locacao': 'S',
                              'tipo': tipo,
                              'quantidade_dormitorios': quantidade_dormitorios}
                return db.select('qry_imovel_listas',
                                 where=web.db.sqlwhere(where_dict),
                                 vars=locals())
            else:
                where_dict = {'utilidade_residencial': 'S',
                              'finalidade_venda': 'S',
                              'tipo': tipo,
                              'quantidade_dormitorios': quantidade_dormitorios}
                return db.select('qry_imovel_listas',
                                 where=web.db.sqlwhere(where_dict),
                                 vars=locals())
        else:
            if finalidade == 'locacao':
                where_dict = {'utilidade_comercial': 'S',
                              'finalidade_locacao': 'S',
                              'tipo': tipo,
                              'quantidade_dormitorios': quantidade_dormitorios}
                return db.select('qry_imovel_listas',
                                 where=web.db.sqlwhere(where_dict),
                                 vars=locals())
            else:
                where_dict = {'utilidade_comercial': 'S',
                              'finalidade_venda': 'S',
                              'tipo': tipo,
                              'quantidade_dormitorios': quantidade_dormitorios}
                return db.select('qry_imovel_listas',
                                 where=web.db.sqlwhere(where_dict),
                                 vars=locals())
    else:
        if utilidade == 'residencial':
            if finalidade == 'locacao':
                where_dict = {'utilidade_residencial': 'S',
                              'finalidade_locacao': 'S',
                              'tipo': tipo}
                return db.select('qry_imovel_listas',
                                 where=web.db.sqlwhere(where_dict),
                                 vars=locals())
            else:
                where_dict = {'utilidade_residencial': 'S',
                              'finalidade_venda': 'S',
                              'tipo': tipo}
                return db.select('qry_imovel_listas',
                                 where=web.db.sqlwhere(where_dict),
                                 vars=locals())
        else:
            if finalidade == 'locacao':
                where_dict = {'utilidade_comercial': 'S',
                              'finalidade_locacao': 'S',
                              'tipo': tipo}
                return db.select('qry_imovel_listas',
                                 where=web.db.sqlwhere(where_dict),
                                 vars=locals())
            else:
                where_dict = {'utilidade_comercial': 'S',
                              'finalidade_venda': 'S',
                              'tipo': tipo}
                return db.select('qry_imovel_listas',
                                 where=web.db.sqlwhere(where_dict),
                                 vars=locals())


class Necessidade(object):

    __table__ = 'website_necessidade'

    def __init__(self,
                 id=None,
                 nome=None,
                 email=None,
                 telefone=None,
                 data_inclusao=None,
                 atendido=None,
                 necessidade=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_inclusao = data_inclusao
        self.atendido = atendido
        self.necessidade = necessidade

    @classmethod
    def get_class_name(self):
        return "Necessidade"

    @classmethod
    def get_list_title(self):
        return "Listagem de Necessidades"

    @classmethod
    def get_form_title(self):
        return "Necessidade"

    @classmethod
    def get_default_field_order(self):
        return "data_inclusao"

    @classmethod
    def exposed_search_properties(self):
        return [('all', 'Todos'), ('nome', 'Nome')]

    @classmethod
    def exposed_list_properties(self):
        colunms = ['Nome',
                   'E-mail',
                   'Telefone',
                   'Data',
                   'Atendido',
                   'Necessidade']
        fields = ['nome',
                  'email',
                  'telefone',
                  'data_inclusao',
                  'atendido',
                  'necessidade']
        attributes = {'colunms': colunms, 'fields': fields}
        return attributes

    def get_field_value(self, field):
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        id = form.id
        has_id = id != '' and id != 'NULL' and id != None and id != 'None'
        if not has_id:
            db.insert(self.__table__,
                      nome=form.nome,
                      email=form.email,
                      telefone=form.telefone,
                      data_inclusao=datetime.now(),
                      atendido='N',
                      necessidade=form.necessidade)
        else:
            db.update(self.__table__,
                      where="id=$id",
                      vars=locals(),
                      nome=form.nome,
                      email=form.email,
                      telefone=form.telefone,
                      atendido=form.necessidade,
                      necessidade=form.necessidade)


# Generic Functions
def login(login, senha):
    ident = db.query("""select * from website_usuario where
                        login = '%(login)s' and senha = '%(senha)s'"""
                         % {'login': login, 'senha': senha})[0]
    logado = None
    if ident:
        logado = Usuario(id=ident['id'],
                         login=ident['login'],
                         senha=ident['senha'],
                         nivel_acesso=ident['nivel_acesso'])
    return logado


def get_exposed_managed_tables():
    values = []
    values.append({'model_table': 'Usuario',
                   'icon_file': '/static/images/Usuario.png',
                   'class_name': 'Usuários'})
    values.append({'model_table': 'Pagina',
                   'icon_file': '/static/images/Pagina.png',
                   'class_name': 'Páginas'})
    values.append({'model_table': 'Proprietario',
                   'icon_file': '/static/images/Proprietario.png',
                   'class_name': 'Proprietários'})
    values.append({'model_table': 'Agenciador',
                   'icon_file': '/static/images/Agenciador.png',
                   'class_name': 'Agênciadores'})
    values.append({'model_table': 'Corretor',
                   'icon_file': '/static/images/Corretor.png',
                   'class_name': 'Corretores'})
    values.append({'model_table': 'OrigemImovel',
                   'icon_file': '/static/images/OrigemImovel.png',
                   'class_name': 'Origens Imóveis'})
    values.append({'model_table': 'TipoImovel',
                   'icon_file': '/static/images/TipoImovel.png',
                   'class_name': 'Tipos Imóveis'})
    values.append({'model_table': 'Imovel',
                   'icon_file': '/static/images/Imovel.png',
                   'class_name': 'Imóveis'})
    values.append({'model_table': 'Necessidade',
                   'icon_file': '/static/images/Necessidade.png',
                   'class_name': 'Necessidades'})
    return values


def latest_records(entity, q=None, start=1, PAGESIZE=10, order=None):
    limit = int(PAGESIZE)
    has_query = q != '' and q != 'NULL' and q != None and \
                q != 'None' and q != 'all'
    if has_query:
        data = db.select(entity.__table__,
                         None,
                         '*',
                         q,
                         order,
                         None,
                         limit,
                         int(start),
                         False)
    else:
        data = db.select(entity.__table__,
                         None,
                         '*',
                         None,
                         order,
                         None,
                         limit,
                         int(start),
                         False)
    items = [entity(**row) for row in data]
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
        return db.select(entity.__table__,
                         where='slug=$slug',
                         vars=locals())[0]
    except IndexError:
        return None


def delete_entity(entity, id):
    db.delete(entity.__table__, where="id=$id", vars=locals())


def exists_entity(entity, field, value):
    return db.select('%s' % entity,
                     where="%(field)s='%(value)s'" % {'field': field,
                                                      'value': value},
                     vars=locals())[0] or None


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
    items = [entity(**row) for row in data]
    return items
