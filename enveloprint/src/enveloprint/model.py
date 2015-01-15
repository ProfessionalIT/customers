 # -*- coding: utf-8 -*-
from google.appengine.api import users
from google.appengine.ext import db
import logging

from utils import slugify, versionate

from datetime import datetime

# Generic Functions
def get_exposed_managed_tables():
    values = []
    values.append({'model_table': 'FotoSite', 'icon_file': '/static/images/Foto.png', 'class_name': 'FOTOS'})
    values.append({'model_table': 'Curiosidade', 'icon_file': '/static/images/Aviso.png', 'class_name': 'CURIOSIDADES'})
    values.append({'model_table': 'CategoriaProduto', 'icon_file': '/static/images/Parametro.png', 'class_name': 'CATEGORIAS'})
    values.append({'model_table': 'Produto', 'icon_file': '/static/images/Revista.png', 'class_name': 'PRODUTOS'})
    values.append({'model_table': 'Menu', 'icon_file': '/static/images/Menu.png', 'class_name': 'MENUS'})
    values.append({'model_table': 'Pagina', 'icon_file': '/static/images/Pagina.png', 'class_name': 'PÁGINAS'})
    return values

def latest_records(entity, q=None, start=1, PAGESIZE=10, order=None):
    limit=int(PAGESIZE)
    has_query=q != '' and q != 'NULL' and q != None and q != 'None' and q != 'all'
    if has_query:
        if order is not None:
            sql="SELECT * FROM %(entity)s WHERE %(query)s ORDER BY %(order)s" % {'entity': str(entity.kind()), 'query': q, 'order': order}
        else:
            sql="SELECT * FROM %(entity)s WHERE %(query)s" % {'entity': str(entity.kind()), 'query': q}
        query=db.GqlQuery(sql)
        return query.fetch(limit, start)
    else:
        if order is not None:
            try:
                query = db.Query(entity)
                query.order(order)
                return query.fetch(limit,int(start))
            except:
                query = db.Query(entity)
                query.order(order)
                return query.fetch(limit)
        else:
            try:
                return db.Query(entity).fetch(limit,int(start))
            except:
                return db.Query(entity).fetch(limit)

def count_records(entity):
    return entity.all().count()

def entity_by_id(entity, id):
    return entity.get_by_id(int(id))

def delete_entity(entity, id):
    entity=entity_by_id(entity, id)
    db.delete(entity)

def exists_entity(entity, field, value):
    q=db.Query(entity).filter('%s =' % field, value).get()
    return q

def find_slug(Entity, slug):
    q = db.Query(Entity).filter('slug =', slug).get()
    return q is not None

def get_model_by_name(name):
    if name == 'FotoSite':
        return FotoSite
    elif name == 'Curiosidade':
        return Curiosidade
    elif name == 'CategoriaProduto':
        return CategoriaProduto
    elif name == 'Produto':
        return Produto
    elif name == 'Pagina':
        return Pagina
    elif name == 'Menu':
        return Menu
    else:
        return None

def save_entity(entity, form):
    if entity == 'FotoSite':
        save_foto_site(form)
    elif entity == 'Curiosidade':
        save_curiosidade(form)
    elif entity == 'CategoriaProduto':
        save_categoria_produto(form)
    elif entity == 'Produto':
        save_produto(form)
    elif entity == 'Pagina':
        save_pagina(form)
    elif entity == 'Menu':
        save_menu(form)
    else:
        pass

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

# App Models.
class FotoSite(db.Model):
    tipo = db.StringProperty(required=True) # slide-show ou cabecalho
    nome = db.StringProperty(required=True)
    descricao = db.TextProperty(required=True)
    ativo = db.StringProperty(required=True) # sim ou não
    imagem_url = db.StringProperty(required=True)
    data_inclusao = db.DateTimeProperty()

    @classmethod
    def get_class_name(cls):
        return "FotoSite"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Fotos"

    @classmethod
    def get_default_field_order(cls):
        return "-data_inclusao"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('nome', 'Nome'), ('ativo', 'Ativo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Nome', 'Ativo', 'Data Inclusão']
        fields = ['nome', 'ativo', 'data_inclusao']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            if field == 'data_inclusao':
                data_hora = getattr(cls, field)
                if data_hora:
                    return data_hora.strftime('%d/%m/%Y %H:%M')
                else:
                    return None
            else:
                return getattr(cls, field)

def save_foto_site(form):
    entity=exists_entity(FotoSite, 'nome', form.nome)
    if (entity is not None):
        entity.tipo=form.tipo
        entity.nome=form.nome
        entity.descricao=form.descricao
        entity.ativo=form.ativo
        entity.imagem_url=form.imagem_url
        entity.data_inclusao=datetime.strptime(form.data_inclusao,'%Y-%m-%d %H:%M:%S')
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.tipo=form.tipo
        entity.nome=form.nome
        entity.descricao=form.descricao
        entity.ativo=form.ativo
        entity.imagem_url=form.imagem_url
        entity.data_inclusao=datetime.strptime(form.data_inclusao,'%Y-%m-%d %H:%M:%S')
        db.put(entity)
    else:
        db.put(FotoSite(
            tipo=form.tipo,
            nome=form.nome,
            descricao=form.descricao,
            ativo=form.ativo,
            imagem_url=form.imagem_url,
            data_inclusao = datetime.strptime(form.data_inclusao,'%Y-%m-%d %H:%M:%S')))

def get_header_image():
    sql="SELECT * FROM FotoSite WHERE ativo ='Sim' AND tipo='Header'"
    query=db.GqlQuery(sql)
    return query.fetch(1)

def get_fotos_slide_show():
    sql="SELECT * FROM FotoSite WHERE ativo ='Sim' AND tipo='Slide-Show' order by data_inclusao"
    query=db.GqlQuery(sql)
    return query.fetch(7)

class Curiosidade(db.Model):
    nome = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    palavras_chaves = db.StringProperty(required=True)
    detalhamento = db.TextProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Curiosidade"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Curiosidades"

    @classmethod
    def get_default_field_order(cls):
        return "nome"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('nome', 'Nome')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Nome']
        fields = ['nome']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            return getattr(cls, field)

def save_curiosidade(form):
    entity=exists_entity(Curiosidade, 'nome', form.nome)
    slug = slugify(form.nome)
    if (entity is not None):
        entity.nome=form.nome
        entity.slug=slug
        entity.palavras_chaves=form.palavras_chaves
        entity.detalhamento=form.detalhamento
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.nome=form.nome
        entity.slug=slug
        entity.palavras_chaves=form.palavras_chaves
        entity.detalhamento=form.detalhamento
        db.put(entity)
    else:
        while find_slug(Curiosidade, slug):
            slug = versionate(slug)
        db.put(Curiosidade(
            nome=form.nome,
            slug=slug,
            palavras_chaves=form.palavras_chaves,
            detalhamento=form.detalhamento))

class CategoriaProduto(db.Model):
    nome = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    palavras_chaves = db.StringProperty(required=True)
    icone = db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "CategoriaProduto"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Categorias de Produto"

    @classmethod
    def get_default_field_order(cls):
        return "nome"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('nome', 'Nome')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Nome']
        fields = ['nome']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            return getattr(cls, field)

def save_categoria_produto(form):
    entity=exists_entity(CategoriaProduto, 'nome', form.nome)
    slug = slugify(form.nome)
    if (entity is not None):
        entity.nome=form.nome
        entity.slug=slug
        entity.palavras_chaves=form.palavras_chaves
        entity.icone=form.icone
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.nome=form.nome
        entity.slug=slug
        entity.palavras_chaves=form.palavras_chaves
        entity.icone=form.icone
        db.put(entity)
    else:
        while find_slug(CategoriaProduto, slug):
            slug = versionate(slug)
        db.put(CategoriaProduto(
            nome=form.nome,
            slug=slug,
            palavras_chaves=form.palavras_chaves,
            icone=form.icone))

class Produto(db.Model):
    categoria = db.ReferenceProperty(CategoriaProduto, required=True, collection_name='categoria_set')
    codigo = db.StringProperty(required=True)
    referencia = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    formato = db.StringProperty(required=True)
    gramatura = db.StringProperty(required=True)
    tipo_embalagem = db.StringProperty(required=True)
    unidade_embalagem = db.StringProperty(required=True)
    cor = db.StringProperty(required=True)
    palavras_chaves = db.StringProperty(required=True)
    destaque = db.StringProperty(required=True)
    foto_produto_01 = db.StringProperty(required=False)
    foto_produto_02 = db.StringProperty(required=False)
    foto_produto_03 = db.StringProperty(required=False)
    foto_produto_04 = db.StringProperty(required=False)
    foto_produto_05 = db.StringProperty(required=False)

    @classmethod
    def get_class_name(cls):
        return "Produto"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Produto"

    @classmethod
    def get_default_field_order(cls):
        return "codigo"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('codigo', 'Codigo'), ('referencia', 'Referência'), ('destaque', 'Destaque')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Código', 'Referência', 'Formato', 'Gramatura', 'Categoria', 'Destaque']
        fields = ['codigo', 'referencia', 'formato', 'gramatura', 'categoria', 'destaque']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): 
            if field == 'categoria':
                return cls.categoria.nome
            else:
                return getattr(cls, field)

def save_produto(form):
    entity=exists_entity(Produto, 'codigo', form.codigo)
    slug = slugify(form.codigo)
    categoria = None
    if form.categoria is not None:
        categoria = CategoriaProduto.get_by_id(int(form.categoria))
    if (entity is not None):
        entity.categoria=categoria
        entity.codigo=form.codigo
        entity.referencia=form.referencia
        entity.slug=slug
        entity.formato=form.formato
        entity.gramatura=form.gramatura
        entity.tipo_embalagem=form.tipo_embalagem
        entity.unidade_embalagem=form.unidade_embalagem
        entity.cor=form.cor
        entity.palavras_chaves=form.palavras_chaves
        entity.destaque=form.destaque
        entity.foto_produto_01=form.foto_produto_01
        entity.foto_produto_02=form.foto_produto_02
        entity.foto_produto_03=form.foto_produto_03
        entity.foto_produto_04=form.foto_produto_04
        entity.foto_produto_05=form.foto_produto_05
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.categoria=categoria
        entity.codigo=form.codigo
        entity.referencia=form.referencia
        entity.slug=slug
        entity.formato=form.formato
        entity.gramatura=form.gramatura
        entity.tipo_embalagem=form.tipo_embalagem
        entity.unidade_embalagem=form.unidade_embalagem
        entity.cor=form.cor
        entity.palavras_chaves=form.palavras_chaves
        entity.destaque=form.destaque
        entity.foto_produto_01=form.foto_produto_01
        entity.foto_produto_02=form.foto_produto_02
        entity.foto_produto_03=form.foto_produto_03
        entity.foto_produto_04=form.foto_produto_04
        entity.foto_produto_05=form.foto_produto_05
        db.put(entity)
    else:
        while find_slug(Produto, slug):
            slug = versionate(slug)
        db.put(Produto(
            categoria=categoria,
            codigo=form.codigo,
            referencia=form.referencia,
            slug=slug,
            formato=form.formato,
            gramatura=form.gramatura,
            tipo_embalagem=form.tipo_embalagem,
            unidade_embalagem=form.unidade_embalagem,
            cor=form.cor,
            palavras_chaves=form.palavras_chaves,
            destaque=form.destaque,
            foto_produto_01=form.foto_produto_01,
            foto_produto_02=form.foto_produto_02,
            foto_produto_03=form.foto_produto_03,
            foto_produto_04=form.foto_produto_04,
            foto_produto_05=form.foto_produto_05))

def get_produtos_by_categoria(entity):
    sql="SELECT * FROM Produto WHERE categoria=KEY('CategoriaProduto', %s)" % str(entity.key().id())
    query=db.GqlQuery(sql)
    return query.fetch(10000)

def get_produtos_destaque():
    sql="SELECT * FROM Produto WHERE destaque = 'Sim'"
    query=db.GqlQuery(sql)
    return query.fetch(10000)

class Pagina(db.Model):
    nome = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    descricao_completa = db.StringProperty(required=True)
    palavras_chaves = db.StringProperty(required=True)
    data_criacao = db.DateTimeProperty()
    ultima_alteracao = db.DateTimeProperty()
    usuario_alteracao = db.UserProperty()
    conteudo=db.TextProperty(required=False)
    
    @classmethod
    def get_class_name(cls):
        return "Pagina"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Páginas"

    @classmethod
    def get_default_field_order(cls):
        return "nome"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('nome', 'Titulo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Titulo']
        fields = ['nome']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): return getattr(cls, field) 

def save_pagina(form):
    entity=exists_entity(Pagina, 'nome', form.nome)
    slug = slugify(form.nome)
    if (entity is not None):
        entity.nome=form.nome
        entity.slug=slug
        entity.descricao_completa=form.descricao_completa
        entity.palavras_chaves=form.palavras_chaves
        entity.data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S')
        entity.ultima_alteracao=datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S')
        entity.usuario_alteracao=users.get_current_user()
        entity.conteudo=form.conteudo
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.nome=form.nome
        entity.slug=slug
        entity.descricao_completa=form.descricao_completa
        entity.palavras_chaves=form.palavras_chaves
        entity.data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S')
        entity.ultima_alteracao=datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S')
        entity.usuario_alteracao=users.get_current_user()
        entity.conteudo=form.conteudo
        db.put(entity)
    else:
        while find_slug(Pagina, slug):
            slug = versionate(slug)
        db.put(Pagina(
            nome=form.nome,
            slug=slug,
            descricao_completa=form.descricao_completa,
            palavras_chaves=form.palavras_chaves,
            data_criacao = datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S'),
            ultima_alteracao = datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S'),
            usuario_alteracao = users.get_current_user(),
            conteudo=form.conteudo))

class Menu(db.Model):
    ordem = db.IntegerProperty(required=True)
    nome = db.StringProperty(required=True)
    descricao = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    data_criacao = db.DateTimeProperty()
    ultima_alteracao = db.DateTimeProperty()
    usuario_alteracao = db.UserProperty()
    pagina=db.ReferenceProperty(Pagina, required=False, collection_name='pagina_set')
    endereco=db.StringProperty(required=False)
    menu_pai = db.SelfReferenceProperty(required=False)
    nivel =db.StringProperty(required=True)

    @classmethod
    def get_class_name(cls):
        return "Menu"

    @classmethod
    def get_list_title(cls):
        return "Listagem de Menus"

    @classmethod
    def get_default_field_order(cls):
        return "ordem"

    @classmethod
    def exposed_search_properties(cls):
        return [('all', 'Todos'), ('ordem', 'Ordem'), ('nivel', 'Nível'), ('nome', 'Titulo')] 

    @classmethod
    def exposed_list_properties(cls):
        colunms = ['Ordem', 'Nível', 'Titulo', 'Endereço']
        fields = ['ordem', 'nivel', 'nome', 'endereco']
        attributes = {'colunms': colunms, 'fields':fields}
        return attributes

    def get_field_value(cls, field):
        if hasattr(cls, field): return getattr(cls, field) 

def save_menu(form):
    entity=exists_entity(Menu, 'nome', form.nome)
    slug = slugify(form.nome)
    parent = None
    if form.menu_pai is not None:
        parent = Menu.get_by_id(int(form.menu_pai))
    pagina = None
    if form.pagina is not None:
        pagina = Pagina.get_by_id(int(form.pagina))

    if (entity is not None):
        entity.ordem=int(form.ordem)
        entity.nome=form.nome
        entity.descricao=form.descricao
        entity.slug=slug
        entity.data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S')
        entity.ultima_alteracao=datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S')
        entity.usuario_alteracao=users.get_current_user()
        entity.pagina=pagina
        entity.endereco=form.endereco        
        entity.menu_pai=parent
        entity.nivel=form.nivel
        db.put(entity)
    elif (str(form.key) != ''):
        entity=db.get(form.key)
        entity.ordem=int(form.ordem)
        entity.nome=form.nome
        entity.descricao=form.descricao
        entity.slug=slug
        entity.data_criacao=datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S')
        entity.ultima_alteracao=datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S')
        entity.usuario_alteracao=users.get_current_user()
        entity.pagina=pagina
        entity.endereco=form.endereco
        entity.menu_pai=parent
        entity.nivel=form.nivel
        db.put(entity)
    else:
        while find_slug(Menu, slug):
            slug = versionate(slug)
        db.put(Menu(
            ordem=int(form.ordem),
            nome=form.nome,
            descricao=form.descricao,
            slug=slug,
            data_criacao = datetime.strptime(form.data_criacao,'%Y-%m-%d %H:%M:%S'),
            ultima_alteracao = datetime.strptime(form.ultima_alteracao,'%Y-%m-%d %H:%M:%S'),
            usuario_alteracao = users.get_current_user(),
            pagina=pagina,
            endereco=form.endereco,
            menu_pai=parent,
            nivel=form.nivel))

def get_pagina(endereco):
    menu = db.Query(Menu).filter('endereco =', endereco).get()
    if menu != None:
        pagina = Pagina.get_by_id(int(menu.pagina.key().id()))
    else:
        slug = endereco.replace('/pagina/','')
        pagina = exists_entity(Pagina, 'slug', slug)
    return pagina or None

def get_avaliables_menus():
    sql="SELECT * FROM Menu WHERE ordem > 0 ORDER BY ordem, menu_pai, nivel"
    query=db.GqlQuery(sql)
    return query.fetch(10000)

def get_menu_itens():
    menus = get_avaliables_menus()
    menu_sup = 0
    tem_submenu = False
    menu_html = ''
    for menu in menus:
        nivel = int(menu.nivel)
        if nivel == 1:
            if tem_submenu:
                menu_html = menu_html + '</ul>'
                menu_html = menu_html + '</li>'
                tem_submenu = False
            menu_sup = str(menu.key().id())
            menu_html = menu_html + '<li class="first_level_menu"><a href="' + menu.endereco + '" class="menu" title="' + menu.descricao + '">' + menu.nome + '</a>'
        elif nivel == 2:
            if menu.menu_pai is not None:
                if str(menu_sup) == str(menu.menu_pai.key().id()):
                    if tem_submenu == False:
                        tem_submenu = True
                        menu_html = menu_html + '<ul>'
                        menu_html = menu_html + '<li><a href="' + menu.endereco + '" title="' + menu.descricao + '">' + menu.nome + '</a></li>'
                    else:
                        menu_html = menu_html + '<li><a href="' + menu.endereco + '" title="' + menu.descricao + '">' + menu.nome + '</a></li>'
    if tem_submenu:
        menu_html = menu_html + '</ul>'
    menu_html = menu_html + '</li>'
    #logging.debug(' ======== HTML MENU ========= ' + menu_html)
    return menu_html
