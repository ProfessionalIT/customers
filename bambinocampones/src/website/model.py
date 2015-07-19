# -*- coding: utf-8 -*-
"""
"""
import web
from configuration import DBN, HOST, DB, USER, PWD
from utils import slugify
from datetime import datetime
from auth import get_logged_user


if DBN == 'sqlite':
    db = web.database(dbn=DBN, db=DB)
else:
    db = web.database(dbn=DBN, host=HOST, db=DB, user=USER, pw=PWD)


def unsetDB():
    """
    """
    global db
    db.ctx.db.close()
    db = None


def setDB():
    """
    """
    global db
    if DBN == 'sqlite':
        db = web.database(dbn=DBN, db=DB)
    else:
        db = web.database(dbn=DBN, host=HOST, db=DB, user=USER, pw=PWD)


def validate_id(id):
    """
    """
    has_id = id != '' and id != 'NULL' and id is not None and id is not 'None'
    return has_id


class AlreadyExistsValueException(Exception):
    """
    """
    def __init__(self, value):
        """
        """
        self.parameter = """Existe um registro no banco de dados com
                           esse valor: %s """ % value

    def __str__(self):
        """
        """
        return repr(self.parameter)


# App Models.
class Usuario(object):
    """
    """
    __table__ = 'usuario'

    def __init__(self, id=None, login=None, senha=None, nivel_acesso=None):
        """
        """
        self.id = id
        self.login = login
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    @classmethod
    def get_class_name(self):
        """
        """
        return "Usuario"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Usuários"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Usuário"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "login"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('login', 'Login')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Login']
        fields = ['login']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
        if hasattr(self, field):
            return getattr(self, field)

    def __str__(self):
        """
        """
        if self is not None:
            if self.login:
                return self.login

    @classmethod
    def save(self, form):
        """
        """
        if not validate_id(form.id):
            entity = exists_entity(self.__table__, 'login', form.login)
            if entity is not None:
                raise AlreadyExistsValueException(form.login)
            else:
                db.insert(self.__table__,
                          id=get_next_id_value('usuario'),
                          login=form.login,
                          senha=form.senha,
                          nivel_acesso=int(form.nivel_acesso))
        else:
            db.update(self.__table__,
                      where="id=%s" % form.id,
                      vars=locals(),
                      login=form.login,
                      senha=form.senha,
                      nivel_acesso=int(form.nivel_acesso))


class Log(object):
    """
    """
    __table__ = 'log'

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
        """
        """
        return "Log"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Logs"

    @classmethod
    def get_form_title(self):
        """
        """
        return "LOG"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "data desc"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('usuario', 'Usuário'),
                ('operacao', 'Operação'),
                ('endereco_ip', 'Endereço IP'),
                ('log', 'Log')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Usuario',
                   'Operação',
                   'Endereço IP',
                   'Log',
                   'Data',
                   'Menu']
        fields = ['usuario',
                  'operacao',
                  'endereco_ip',
                  'log',
                  'data',
                  'menu']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
        """
        """
        db.insert('log',
                  id=get_next_id_value('log'),
                  usuario=record['usuario'],
                  operacao=record['operacao'],
                  endereco_ip=record['endereco_ip'],
                  log=record['log'],
                  data=datetime.now(),
                  menu=record['menu'])


class Pagina(object):
    """
    """
    __table__ = 'pagina'

    def __init__(self,
                 id=None,
                 titulo=None,
                 slug=None,
                 descricao_completa=None,
                 palavras_chaves=None,
                 data_criacao=None,
                 ultima_alteracao=None,
                 autor=None,
                 conteudo=None,
                 permite_comentario=None,
                 draft=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.descricao_completa = descricao_completa
        self.palavras_chaves = palavras_chaves
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.autor = autor
        self.conteudo = conteudo
        self.permite_comentario = permite_comentario
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Pagina"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Páginas"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Página"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "id"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Permite Comentários',
                   'Rascunho']
        fields = ['titulo',
                  'permite_comentario',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
            else:
                return getattr(self, field)

    @classmethod
    def publish(self, form):
        """
        """
        db.update(self.__table__,
                  where="id=%s" % form.id,
                  vars=locals(),
                  draft='N')

    @classmethod
    def save(self, form):
        """
        """
        usuario = get_logged_user()
        hoje = datetime.now()
        slug = slugify(form.titulo)
        entity = None

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'titulo',
                                   form.titulo)

            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('pagina'),
                              titulo=form.titulo,
                              slug=slug,
                              descricao_completa=form.descricao_completa,
                              palavras_chaves=form.palavras_chaves,
                              data_criacao=hoje,
                              ultima_alteracao=hoje,
                              autor=usuario.id,
                              conteudo=form.conteudo,
                              permite_comentario=form.permite_comentario,
                              draft=form.draft)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          slug=slug,
                          descricao_completa=form.descricao_completa,
                          palavras_chaves=form.palavras_chaves,
                          ultima_alteracao=hoje,
                          autor=usuario.id,
                          conteudo=form.conteudo,
                          permite_comentario=form.permite_comentario,
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()


def get_pagina(endereco):
    """
    """
    try:
        record = db.query("""select titulo, descricao_completa,
                             palavras_chaves, conteudo from pagina where
                             slug = '%(endereco)s'
                             and draft = 'N'""" % {'endereco': endereco})[0]
        return record
    except IndexError:
        return None


def get_pagina_preview(endereco):
    """
    """
    record = db.query("""select titulo, descricao_completa,
                         palavras_chaves, conteudo from pagina where
                         slug = '%(endereco)s'
                         and draft = 'S'""" % {'endereco': endereco})[0]
    return record or None


class Menu(object):
    """
    """
    __table__ = 'menu'

    def __init__(self,
                 id,
                 ordem,
                 titulo,
                 descricao,
                 slug,
                 data_criacao,
                 ultima_alteracao,
                 autor,
                 pagina,
                 endereco,
                 menu_pai,
                 nivel,
                 key_words,
                 draft=None):
        """
        """
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
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Menu"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Menus"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Menu"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "ordem"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('ordem', 'Ordem'),
                ('nivel', 'Nível'),
                ('titulo', 'Titulo')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Ordem',
                   'Nivel',
                   'Titulo',
                   'Endereço']
        fields = ['ordem',
                  'nivel',
                  'titulo',
                  'endereco']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        hoje = datetime.now()
        usuario = get_logged_user()
        slug = slugify(form.titulo)

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                 'titulo',
                                 form.titulo)

            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('menu'),
                              ordem=int(form.ordem),
                              titulo=form.titulo,
                              descricao=form.descricao,
                              slug=slug,
                              data_criacao=hoje,
                              ultima_alteracao=hoje,
                              autor=int(usuario.id),
                              pagina=int(form.pagina) or None,
                              endereco=form.endereco,
                              menu_pai=int(form.menu_pai) or None,
                              nivel=int(form.nivel),
                              key_words=form.key_words,
                              draft=form.draft)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          ordem=int(form.ordem),
                          titulo=form.titulo,
                          descricao=form.descricao,
                          slug=slug,
                          data_criacao=hoje,
                          ultima_alteracao=hoje,
                          autor=usuario.id,
                          pagina=int(form.pagina) or None,
                          endereco=form.endereco,
                          menu_pai=int(form.menu_pai) or None,
                          nivel=int(form.nivel),
                          key_words=form.key_words,
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Aviso(object):
    """
    """
    __table__ = 'aviso'

    def __init__(self,
                 id=None,
                 titulo=None,
                 slug=None,
                 data_publicacao=None,
                 data_expiracao=None,
                 autor=None,
                 texto=None,
                 ativo=None,
                 draft=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_publicacao = data_publicacao
        self.data_expiracao = data_expiracao
        self.autor = autor
        self.texto = texto
        self.ativo = ativo
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Aviso"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Avisos"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Aviso"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('texto', 'Texto'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Publicação',
                   'Expira em',
                   'Ativo',
                   'Rascunho']
        fields = ['titulo',
                  'data_publicacao',
                  'data_expiracao',
                  'ativo',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        slug = slugify(form.titulo)
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'slug',
                                   form.slug)

            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('aviso'),
                              titulo=form.titulo,
                              slug=slug,
                              data_publicacao=
                  datetime.strptime(form.data_publicacao, '%Y-%m-%d %H:%M:%S'),
                              data_expiracao=
                   datetime.strptime(form.data_expiracao, '%Y-%m-%d %H:%M:%S'),
                              autor=usuario.id,
                              texto=form.texto,
                              ativo=form.ativo,
                              draft=form.draft)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          slug=slug,
                          data_publicacao=
                  datetime.strptime(form.data_publicacao, '%Y-%m-%d %H:%M:%S'),
                          data_expiracao=
                   datetime.strptime(form.data_expiracao, '%Y-%m-%d %H:%M:%S'),
                          autor=usuario.id,
                          texto=form.texto,
                          ativo=form.ativo,
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Enquete(object):
    """
    """
    __table__ = 'enquete'

    def __init__(self,
                 id=None,
                 pergunta=None,
                 slug=None,
                 resposta_01=None,
                 votos_resposta_01=None,
                 resposta_02=None,
                 votos_resposta_02=None,
                 resposta_03=None,
                 votos_resposta_03=None,
                 ativo=None,
                 autor=None,
                 draft=None):
        """
        """
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
        self.autor = autor
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Enquete"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Enquetes"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Enquete"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "pergunta"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('pergunta', 'Pergunta'),
                ('ativo', 'Ativo'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Pergunta',
                   'Resposta 1',
                   'Votos',
                   'Resposta 2',
                   'Votos',
                   'Resposta 3',
                   'Votos',
                   'Ativo',
                   'Rascunho']
        fields = ['pergunta',
                  'resposta_01',
                  'votos_resposta_01',
                  'resposta_02',
                  'votos_resposta_02',
                  'resposta_03',
                  'votos_resposta_03',
                  'ativo',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
        """
        """
        slug = slugify(form.pergunta)
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'slug',
                                   slug)

            if entity is not None:
                raise AlreadyExistsValueException(form.pergunta)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('enquete'),
                              pergunta=form.pergunta,
                              slug=slug,
                              resposta_01=form.resposta_01,
                              votos_resposta_01=int(form.votos_resposta_01),
                              resposta_02=form.resposta_02,
                              votos_resposta_02=int(form.votos_resposta_02),
                              resposta_03=form.resposta_03,
                              votos_resposta_03=int(form.votos_resposta_03),
                              ativo=form.ativo,
                              autor=usuario.id,
                              draft=form.draft)

                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          pergunta=form.pergunta,
                          slug=slug,
                          resposta_01=form.resposta_01,
                          votos_resposta_01=int(form.votos_resposta_01),
                          resposta_02=form.resposta_02,
                          votos_resposta_02=int(form.votos_resposta_02),
                          resposta_03=form.resposta_03,
                          votos_resposta_03=int(form.votos_resposta_03),
                          ativo=form.ativo,
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()

    @classmethod
    def update_enquete(self, slug, valor_resposta):
        """
        """
        #sql_update = 'update enquete set %(valor_reposta)'
        pass


class TipoPublicacao(object):
    """
    """
    __table__ = 'tipo_publicacao'

    def __init__(self,
                 id=None,
                 titulo=None,
                 autor=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.autor = autor

    @classmethod
    def get_class_name(self):
        """
        """
        return "TipoPublicacao"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Tipos de Publicações"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Tipo Publicação"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo']
        fields = ['titulo']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                 'titulo',
                                 form.titulo)

            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('tipo_publicacao'),
                              titulo=form.titulo)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Publicacao(object):
    """
    """
    __table__ = 'publicacao'

    def __init__(self,
                 id=None,
                 titulo=None,
                 slug=None,
                 data_hora=None,
                 autor=None,
                 data_publicacao=None,
                 palavras_chaves=None,
                 intro=None,
                 completa=None,
                 thumb_publicacao=None,
                 slug_galeria=None,
                 destaque=None,
                 permite_comentario=None,
                 tipos=None,
                 draft=None):
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
        self.permite_comentario = permite_comentario
        self.tipos = tipos
        self.draft = draft

    def get_tipos(self):
        """
        """
        data = db.select('publicacao_tipo_publicacao',
                         None,
                         '*',
                         'publicacao=%s' % str(self.id))
        tipos = []
        for row in data:
            tipos.append(str(row.tipo_publicacao))
        return tipos

    @classmethod
    def get_class_name(self):
        """
        """
        return "Publicacao"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Publicações"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Publicação"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Tipos',
                   'Data/Hora',
                   'Permite Comentário',
                   'Destaque',
                   'Publicado',
                   'Rascunho']
        fields = ['titulo',
                  'tipos',
                  'data_hora',
                  'permite_comentario',
                  'destaque',
                  'data_publicacao',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
        if hasattr(self, field):
            if field == 'data_hora':
                strpformat_in = '%Y-%m-%d %H:%M:%S'
                strpformat_out = '%d/%m/%Y %H:%M:%S'
                data = getattr(self, field)
                if data:
                    if type(data) is unicode:
                        from datetime import datetime
                        data_in = datetime.strptime(data, strpformat_in)
                        return data_in.strftime(strpformat_out)
                    return data.strftime(strpformat_out)
                else:
                    return None
            elif field == 'data_publicacao':
                strpformat_in = '%Y-%m-%d %H:%M:%S'
                strpformat_out = '%d/%m/%Y %H:%M:%S'
                data = getattr(self, field)
                if data:
                    if type(data) is unicode:
                        from datetime import datetime
                        data_in = datetime.strptime(data, strpformat_in)
                        return data_in.strftime(strpformat_out)
                    return data.strftime(strpformat_out)
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
            elif field == 'tipos':
                data = db.select('publicacao_tipo_publicacao',
                                 None,
                                 '*',
                                 'publicacao=%s' % str(self.id))
                tipos = ""
                for row in data:
                    tipo = db.select('tipo_publicacao',
                                     None,
                                     '*',
                                     'id=%s' % row.tipo_publicacao)[0]
                    tipos += tipo.titulo + "</br>"
                return tipos
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        slug = slugify(form.titulo)
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'slug',
                                   slug)
            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    insert_id = db.insert(self.__table__,
                              id=get_next_id_value('publicacao'),
                              titulo=form.titulo,
                              slug=slug,
                              data_hora=
                        datetime.strptime(form.data_hora, '%Y-%m-%d %H:%M:%S'),
                              autor=usuario.id,
                              data_publicacao=
                  datetime.strptime(form.data_publicacao, '%Y-%m-%d %H:%M:%S'),
                              palavras_chaves=form.palavras_chaves,
                              intro=form.intro,
                              completa=form.completa,
                              thumb_publicacao=form.thumb_publicacao,
                              slug_galeria=form.slug_galeria,
                              destaque=form.destaque,
                              draft=form.draft)
                    for tipo in form.tipos:
                        db.insert('publicacao_tipo_publicacao',
                                  publicacao=int(insert_id),
                                  tipo_publicacao=int(tipo))
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          slug=slug,
                          data_hora=
                        datetime.strptime(form.data_hora, '%Y-%m-%d %H:%M:%S'),
                          autor=usuario.id,
                          data_publicacao=
                  datetime.strptime(form.data_publicacao, '%Y-%m-%d %H:%M:%S'),
                          palavras_chaves=form.palavras_chaves,
                          intro=form.intro,
                          completa=form.completa,
                          thumb_publicacao=form.thumb_publicacao,
                          slug_galeria=form.slug_galeria,
                          destaque=form.destaque,
                          draft=form.draft)
                db.delete('publicacao_tipo_publicacao',
                          where="publicacao=%s" % form.id,
                          vars=locals())
                for tipo in form.tipos:
                    db.insert('publicacao_tipo_publicacao',
                              publicacao=int(form.id),
                              tipo_publicacao=int(tipo))
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Banner(object):
    """
    """
    __table__ = 'banner'

    def __init__(self,
                 id=None,
                 titulo=None,
                 slug=None,
                 autor=None,
                 tipo=None,
                 foto_banner=None,
                 link_banner=None,
                 exibir_pagina_inicial=None,
                 ativo=None,
                 count_clicks=None,
                 custom_banner_code=None,
                 draft=None):
        """
        """
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
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Banner"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Banners"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Banner"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Tipo',
                   'Exibir Página Inicial',
                   'Ativo',
                   'QTDE Cliques',
                   'Rascunho']
        fields = ['titulo',
                  'tipo',
                  'exibir_pagina_inicial',
                  'ativo',
                  'count_clicks',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
        if hasattr(self, field):
            if field == 'tipo':
                data = getattr(self, field)
                if data == 'T':
                    return 'Topo do site'
                elif data == 'L':
                    return 'Lateral do site'
                else:
                    return 'Interno do Site'
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
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        slug = slugify(form.titulo)
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'slug',
                                   slug)
            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('banner'),
                              titulo=form.titulo,
                              slug=slug,
                              autor=usuario.id,
                              tipo=form.tipo,
                              foto_banner=form.foto_banner,
                              link_banner=form.link_banner,
                              exibir_pagina_inicial=
                                            form.exibir_pagina_inicial,
                              ativo=form.ativo,
                              custom_banner_code=
                                                form.custom_banner_code,
                              draft=form.draft)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          slug=slug,
                          autor=usuario.id,
                          tipo=form.tipo,
                          foto_banner=form.foto_banner,
                          link_banner=form.link_banner,
                          exibir_pagina_inicia=form.exibir_pagina_inicial,
                          ativo=form.ativo,
                          custom_banner_code=form.custom_banner_code,
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class TipoDocumento(object):
    """
    """
    __table__ = 'tipo_documento'

    def __init__(self,
                 id=None,
                 titulo=None,
                 autor=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.autor = autor

    @classmethod
    def get_class_name(self):
        """
        """
        return "TipoDocumento"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Tipos de Documento"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Tipo Documento"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo']
        fields = ['titulo']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'titulo',
                                   form.titulo)
            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('tipo_documento'),
                              titulo=form.titulo,
                              autor=usuario.id)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Documento(object):
    """
    """
    __table__ = 'documento'

    def __init__(self,
                 id=None,
                 titulo=None,
                 slug=None,
                 data_publicacao=None,
                 autor=None,
                 tipo=None,
                 thumb_arquivo=None,
                 link_arquivo=None,
                 ativo=None,
                 draft=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_publicacao = data_publicacao
        self.autor = autor
        self.tipo = tipo
        self.thumb_arquivo = thumb_arquivo
        self.link_arquivo = link_arquivo
        self.ativo = ativo
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Documento"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Documentos"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Documento"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Publicado',
                   'Tipo',
                   'Ativo',
                   'Rascunho']
        fields = ['titulo',
                  'data_publicacao',
                  'tipo',
                  'ativo',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        slug = slugify(form.titulo)
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'slug',
                                   slug)

            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('documento'),
                              titulo=form.titulo,
                              slug=slug,
                              data_publicacao=
                  datetime.strptime(form.data_publicacao, '%Y-%m-%d %H:%M:%S'),
                              autor=usuario.id,
                              tipo=form.tipo,
                              thumb_arquivo=form.thumb_arquivo,
                              link_arquivo=form.link_arquivo,
                              ativo=form.ativo,
                              draft=form.draft)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          slug=slug,
                          data_publicacao=
                  datetime.strptime(form.data_publicacao, '%Y-%m-%d %H:%M:%S'),
                          autor=usuario.id,
                          tipo=form.tipo,
                          thumb_arquivo=form.thumb_arquivo,
                          link_arquivo=form.link_arquivo,
                          ativo=form.ativo,
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Parametro(object):
    """
    """
    __table__ = 'parametro'

    def __init__(self,
                 id=None,
                 titulo=None,
                 valor=None,
                 autor=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.valor = valor
        self.autor = autor

    @classmethod
    def get_class_name(self):
        """
        """
        return "Parametro"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Parâmetros"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Parâmetros"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Valor']
        fields = ['titulo',
                  'valor']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
        if hasattr(self, field):
            return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'titulo',
                                   form.titulo)
            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('parametro'),
                              titulo=form.titulo,
                              valor=form.valor,
                              autor=usuario.id)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          valor=form.valor)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Galeria(object):
    """
    """
    __table__ = 'galeria'

    def __init__(self,
                 id=None,
                 titulo=None,
                 slug=None,
                 data_criacao=None,
                 autor=None,
                 tipo=None,
                 midia=None,
                 url_galeria=None,
                 permite_comentario=None,
                 draft=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_criacao = data_criacao
        self.autor = autor
        self.tipo = tipo
        self.midia = midia
        self.url_galeria = url_galeria
        self.permite_comentario = permite_comentario
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Galeria"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Galerias"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Galeria"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Tipo',
                   'Midia',
                   'Permite Comentário',
                   'Rascunho']
        fields = ['titulo',
                  'tipo',
                  'midia',
                  'permite_comentario',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        """
        """
        slug = slugify(form.titulo)
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'slug',
                                   slug)
            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('galeria'),
                              titulo=form.titulo,
                              slug=slug,
                              tipo=form.tipo,
                              midia=form.midia,
                              url_galeria=form.url_galeria,
                              data_criacao=
                     datetime.strptime(form.data_criacao, '%Y-%m-%d %H:%M:%S'),
                              autor=usuario.id,
                              draft=form.draft)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          slug=slug,
                          tipo=form.tipo,
                          midia=form.midia,
                          url_galeria=form.url_galeria,
                          data_criacao=
                     datetime.strptime(form.data_criacao, '%Y-%m-%d %H:%M:%S'),
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Moderacao(object):
    """
    """
    __table__ = 'moderacao'

    def __init__(self,
                 id=None,
                 data_hora=None,
                 autor=None,
                 onde=None,
                 operacao=None,
                 moderador=None,
                 data_hora_operacao=None,
                 acao=None,
                 detalhamento=None):
        """
        """
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
        """
        """
        return "Moderacao"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Moderações"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Moderação"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "data_hora_operacao DESC"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('texto', 'Texto')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Inclusão',
                   'Autor',
                   'Onde',
                   'Operação',
                   'Detalhamento',
                   'Moderador',
                   'Data Ação',
                   'Ação']
        fields = ['data_hora',
                  'autor',
                  'onde',
                  'operacao',
                  'detalhamento',
                  'moderador',
                  'data_hora_operacao',
                  'acao']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
    """
    """
    __table__ = 'template'

    def __init__(self,
                 id=None,
                 titulo=None,
                 slug=None,
                 data_publicacao=None,
                 autor=None,
                 path=None,
                 ativo=None,
                 draft=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.data_publicacao = data_publicacao
        self.autor = autor
        self.path = path
        self.ativo = ativo
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Template"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Templates"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Template"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "titulo"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Publicação',
                   'Ativo',
                   'Rascunho']
        fields = ['titulo',
                  'data_publicacao',
                  'ativo',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
            else:
                return getattr(self, field)

    @classmethod
    def save(self, form):
        slug = slugify(form.titulo)
        usuario = get_logged_user()

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'slug',
                                   form.slug)
            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('template'),
                              titulo=form.titulo,
                              slug=slug,
                              data_publicacao=
                  datetime.strptime(form.data_publicacao, '%Y-%m-%d %H:%M:%S'),
                              autor=usuario.id,
                              path=form.path,
                              ativo=form.ativo,
                              draft=form.draft)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          slug=slug,
                          data_publicacao=
                  datetime.strptime(form.data_publicacao, '%Y-%m-%d %H:%M:%S'),
                          autor=usuario.id,
                          path=form.path,
                          ativo=form.ativo,
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class Produto(object):
    """
    """
    __table__ = 'produto'

    def __init__(self,
                 id=None,
                 titulo=None,
                 slug=None,
                 descricao_resumida=None,
                 descricao_completa=None,
                 palavras_chaves=None,
                 url_recurso=None,
                 destaque=None,
                 data_criacao=None,
                 ultima_alteracao=None,
                 autor=None,
                 permite_comentario=None,
                 draft=None):
        """
        """
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.descricao_resumida = descricao_resumida
        self.descricao_completa = descricao_completa
        self.palavras_chaves = palavras_chaves
        self.url_recurso = url_recurso
        self.destaque = destaque
        self.data_criacao = data_criacao
        self.ultima_alteracao = ultima_alteracao
        self.autor = autor
        self.permite_comentario = permite_comentario
        self.draft = draft

    @classmethod
    def get_class_name(self):
        """
        """
        return "Produto"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Produtos"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Produtos"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "id"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('titulo', 'Titulo'),
                ('draft', 'Rascunho')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Titulo',
                   'Permite Comentários',
                   'Rascunho']
        fields = ['titulo',
                  'permite_comentario',
                  'draft']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
            elif field == 'destaque':
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
            else:
                return getattr(self, field)

    @classmethod
    def publish(self, form):
        """
        """
        #@TODO teste
        id = form.id
        db.update(self.__table__,
                  where="id=$id",
                  vars=locals(),
                  draft='N')

    @classmethod
    def save(self, form):
        """
        """
        usuario = get_logged_user()
        hoje = datetime.now()
        slug = slugify(form.titulo)

        if not validate_id(form.id):
            entity = exists_entity(self.__table__,
                                   'titulo',
                                   form.titulo)
            if entity is not None:
                raise AlreadyExistsValueException(form.titulo)
            else:
                t = db.transaction()
                try:
                    db.insert(self.__table__,
                              id=get_next_id_value('produto'),
                              titulo=form.titulo,
                              slug=slug,
                              descricao_resumida=form.descricao_resumida,
                              descricao_completa=form.descricao_completa,
                              palavras_chaves=form.palavras_chaves,
                              url_recurso=form.url_recurso,
                              destaque=form.destaque,
                              data_criacao=hoje,
                              ultima_alteracao=hoje,
                              autor=usuario.id,
                              permite_comentario=form.permite_comentario,
                              draft=form.draft)
                except:
                    t.rollback()
                    raise
                else:
                    t.commit()
        else:
            t = db.transaction()
            try:
                db.update(self.__table__,
                          where="id=%s" % form.id,
                          vars=locals(),
                          titulo=form.titulo,
                          slug=slug,
                          descricao_resumida=form.descricao_resumida,
                          descricao_completa=form.descricao_completa,
                          palavras_chaves=form.palavras_chaves,
                          url_recurso=form.url_recurso,
                          destaque=form.destaque,
                          ultima_alteracao=hoje,
                          autor=usuario.id,
                          permite_comentario=form.permite_comentario,
                          draft=form.draft)
            except:
                t.rollback()
                raise
            else:
                t.commit()


class ProdutoRecurso(object):
    """
    """
    __table__ = 'produto_recurso'

    def __init__(self,
                 id=None,
                 produto=None,
                 tipo_recurso=None,
                 url_miniatura=None,
                 url_recurso=None,
                 descricao_resumida=None):
        """
        """
        self.id = id
        self.produto = produto
        self.tipo_recurso = tipo_recurso
        self.url_miniatura = url_miniatura
        self.url_recurso = url_recurso
        self.descricao_resumida = descricao_resumida

    @classmethod
    def get_class_name(self):
        """
        """
        return "ProdutoRecurso"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Produtos Recursos"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Recurso Produtos"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "id"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('id', 'Id')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['ID']
        fields = ['id']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
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
            elif field == 'destaque':
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
        """
        """
        id = form.id
        db.update(self.__table__,
                  where="id=$id",
                  vars=locals(),
                  draft='N')

    @classmethod
    def save(self, form):
        """
        """
        pass


# Generic Functions
def get_next_id_value(table_name):
    inserted_id = db.query('''select max(id) as total from %s''' % table_name)
    next_id = int(inserted_id[0].total) + 1
    return next_id


def get_noticias_destaques():
    """
    Retorna a lista de notícias em destaque.
    """
    records = db.query("""
        select p.* from publicacao p
        inner join publicacao_tipo_publicacao u on u.publicacao = p.id
        inner join tipo_publicacao t on t.id = u.tipo_publicacao
        and t.titulo = 'Notícia'
        where p.destaque = 'S' and p.draft = 'N'
        order by data_publicacao desc""")
    return records or None


def get_produtos_destaques():
    """
    """
    records = db.query("""select * from
                          produto where destaque = 'S' AND draft = 'N'
                          order by titulo""")
    return records or None


def get_produtos_portifolio():
    """
    """
    records = db.query("""select * from
                          produto where draft = 'N'
                          order by titulo""")
    return records or None


def get_banners_topo():
    """
    """
    records = db.query("""select titulo, foto_banner, link_banner,
                          custom_banner_code from banner
                          where ativo = 'S' AND tipo = 'T'""")
    return records or None


def get_banners_desc():
    """
    """
    foto_itens = get_banners_topo()
    fotos_desc = ''
    loop_count = 1
    for foto in foto_itens:
        fotos_desc += '{"id":"slide-img-%(item_count)s", \
                        "client":"%(item_name)s", \
                        "desc":"%(item_desc)s"},' \
                        % {'item_count': str(loop_count),
                           'item_name': foto.titulo,
                           'item_desc': foto.custom_banner_code}
        loop_count += 1
    fotos_desc = fotos_desc[:-1]
    return fotos_desc


def get_banners_lateral():
    """
    """
    records = db.query("""select titulo, foto_banner, link_banner from
                          banner where ativo = 'S' AND tipo = 'L'""")
    return records or None


def get_banners_internos():
    """
    """
    records = db.query("""select titulo, foto_banner, link_banner from
                          banner where ativo = 'S' AND tipo = 'I'""")
    return records or None


def get_active_admin_modules():
    """
    """
    records = db.query("""select class_name, titulo from modulo
                          where ativo = 'S' AND
                          perfil_acesso like 'A%'""")
    return records or None


def get_active_oper_modules():
    """
    """
    records = db.query("""select class_name, titulo from modulo
                          where ativo = 'S' AND
                          perfil_acesso like 'AO%'""")
    return records or None


def get_active_moderate_modules():
    """
    """
    records = db.query("""select class_name, titulo from modulo
                        where ativo = 'S' AND
                        perfil_acesso like 'AM%'""")
    return records or None


def get_active_template():
    """
    """
    record = db.query("""select path from template where
                         ativo = 'S'""")[0]
    return record or None


def get_menu_itens():
    """
    """
    menus = select_approved(Menu)
    menu_sup = 0
    tem_submenu = False
    menu_html = ''
    for menu in menus:
        nivel = int(menu.nivel)
        if nivel == 1:
            if tem_submenu:
                menu_html += "</ul>"
                menu_html += "</li>"
                tem_submenu = False
            menu_sup = str(menu.id)
            menu_html += "<li><a href='" + menu.endereco
            menu_html += "' title='" + menu.descricao
            menu_html += "' id='menu_" + menu.titulo.lower()
            menu_html += "'>" + menu.titulo + "</a>"
        elif nivel == 2:
            if menu.menu_pai is not None:
                if str(menu_sup) == str(menu.menu_pai.id):
                    if not tem_submenu:
                        tem_submenu = True
                        menu_html += '<ul>'
                    menu_html += "<li><a href='" + menu.endereco
                    menu_html += "' title='" + menu.descricao
                    menu_html += "' id='menu_" + menu.titulo.lower()
                    menu_html += "'>" + menu.titulo + "</a>"
    if tem_submenu:
        menu_html += "</ul>"
    menu_html += "</li>"
    #print ' ======== HTML MENU ========= ' + menu_html
    return menu_html


def login(login, senha):
    """
    """
    ident = db.query("""select * from usuario
                        where login = '%(login)s'
                        and senha = '%(senha)s'""" % {'login': login,
                                                      'senha': senha})[0]
    logado = None
    if ident:
        logado = Usuario(id=ident['id'],
                         login=ident['login'],
                         senha=ident['senha'],
                         nivel_acesso=ident['nivel_acesso'])
    return logado


def get_exposed_managed_tables(nivel_acesso):
    """
    """
    values = []
    if nivel_acesso == 1:
        from configuration import ACTIVE_MODULES_ADMIN
        for module in ACTIVE_MODULES_ADMIN:
            values.append({'model_table': module[0],
                           'icon_file': '/static/images/' + module[0] + '.png',
                           'class_name': module[1]})
    elif nivel_acesso == 2:
        from configuration import ACTIVE_MODULES_OPER
        for module in ACTIVE_MODULES_OPER:
            values.append({'model_table': module[0],
                           'icon_file': '/static/images/' + module[0] + '.png',
                           'class_name': module[1]})
    elif nivel_acesso == 3:
        from configuration import ACTIVE_MODULES_MODER
        for module in ACTIVE_MODULES_MODER:
            values.append({'model_table': module[0],
                           'icon_file': '/static/images/' + module[0] + '.png',
                           'class_name': module[1]})
    return values


def latest_records(entity, q=None, start=1, PAGESIZE=10, order=None):
    """
    """
    limit = int(PAGESIZE)
    has_query = q != '' and q != 'NULL' and \
                q is not None and q != 'None' and q != 'all'
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
    """
    """
    qtde = db.query("select count(id) as value from %s" % entity.__table__)[0]
    return int(qtde['value'])


def entity_by_id(entity, id):
    """
    """
    try:
        return db.select(entity.__table__,
                         where='id=$id',
                         vars=locals())[0]
    except IndexError:
        return None


def object_by_id(entity, id):
    """
    """
    try:
        row = db.select(entity.__table__,
                        where='id=$id',
                        vars=locals())[0]
        return entity(**row)
    except IndexError:
        return None


def entity_by_slug(entity, slug):
    """
    """
    try:
        return db.select(entity.__table__,
                         where='slug=$slug',
                         vars=locals())[0]
    except IndexError:
        return None


def delete_entity(entity, id):
    """
    """
    if entity.__table__ == 'publicacao':
        db.delete('publicacao_tipo_publicacao',
                  where="publicacao=$id",
                  vars=locals())
        db.delete('publicacao',
                  where="id=$id",
                  vars=locals())
    else:
        db.delete(entity.__table__,
                  where="id=$id",
                  vars=locals())


def update_entity_lock(entity, id, value):
    """
    """
    return db.update('%s' % entity.__table__,
                     where="id=$id",
                     locked='%(value)s' % {'value': value},
                     vars=locals())


def generate_url(entity, id):
    """
    """
    caminho = str(web.ctx.home)
    caminho += "/editar/" + entity + "/" + str(id) + '?op=moderate_on'
    str_cota = '"'
    generated_url = "<a href='javascript: void(0)' onclick="
    generated_url += str_cota
    generated_url += "popup('" + caminho + "')"
    generated_url += str_cota + ">" + entity + "</a>"

    return generated_url


def exists_entity(entity, field, value):
    """
    """
    obj = None
    try:
        obj = db.select('%s' % entity,
                        where="%(field)s='%(value)s'" % {'field': field,
                                                           'value': value},
                        vars=locals())[0] or None
    except IndexError:
        obj = None
    return obj


def find_slug(Entity, slug):
    """
    """
    q = db.Query(Entity).filter('slug =', slug).get()
    return q is not None


def get_entity_index_list(entity, filtro, valor, order, limit):
    """
    """
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
    """
    """
    data = db.select(entity.__table__)
    items = [entity(**row) for row in data]
    return items


def select_approved(entity):
    """
    """
    data = db.select(entity.__table__, where="draft='N'")
    items = [entity(**row) for row in data]
    return items
