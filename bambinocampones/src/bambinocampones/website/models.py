# -*- coding: utf-8 -*-
"""
Models utilizadas na app website.
"""
from django.db import models
import datetime


class Calendario(models.Model):
    """
    Calendário de atividades: Evento, Recesso, Festa, Feriado e Ponte.
    """
    TIPO_CALENDARIO = (
                        (u'E', u'Evento'),
                        (u'R', u'Recesso'),
                        (u'D', u'Festa'),
                        (u'F', u'Feriado'),
                        (u'P', u'Ponte'),
    )

    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    tipo = models.CharField(u'Tipo',
                            max_length=1,
                            choices=TIPO_CALENDARIO,
                            default=u'E')
    data_agendamento = models.DateTimeField(u'Data do Agendamento',
                                           default=datetime.datetime.now())

    def __unicode__(self):
        return self.titulo

class Cardapio(models.Model):
    """
    Cardápio Mensal de refeições.
    """
    TIPO_CARDAPIO = (
            (u'1', u'Berçário 1'),
            (u'2', u'Berçário 2'),
            (u'3', u'Crianças Maiores de 1 ano'),
    )

    MES_CARDAPIO = (
            (u'01', u'Janeiro'),
            (u'02', u'Fevereiro'),
            (u'03', u'Março'),
            (u'04', u'Abril'),
            (u'05', u'Maio'),
            (u'06', u'Junho'),
            (u'07', u'Julho'),
            (u'08', u'Agosto'),
            (u'09', u'Setembro'),
            (u'10', u'Outubro'),
            (u'11', u'Novembro'),
            (u'12', u'Dezembro'),
    )

    MES_ATUAL = datetime.datetime.now().month

    ANO_CARDAPIO = (
            (u'2013', u'2013'),
            (u'2014', u'2014'),
    )

    ANO_ATUAL = datetime.datetime.now().year

    tipo = models.CharField(u'Tipo',
                            max_length=1,
                            choices=TIPO_CARDAPIO,
                            default=u'1')
    mes = models.CharField(u'Mês',
                           max_length=2,
                           choices=MES_CARDAPIO,
                           default=str(MES_ATUAL))
    ano = models.CharField(u'Ano Letivo',
                           max_length=4,
                           choices=ANO_CARDAPIO,
                           default=str(ANO_ATUAL))
    cardapio_file = models.FileField('Cardápio',
                               upload_to = 'cardapios',
                                     null=False,
                                     blank=False)


class Galeria(models.Model):
    """
    Galeria de Fotos e/ou Vídeos.
    tipo, titulo, slug, mes, ano, destaqe, descricao
    """
    MES_GALERIA = (
            (u'01', u'Janeiro'),
            (u'02', u'Fevereiro'),
            (u'03', u'Março'),
            (u'04', u'Abril'),
            (u'05', u'Maio'),
            (u'06', u'Junho'),
            (u'07', u'Julho'),
            (u'08', u'Agosto'),
            (u'09', u'Setembro'),
            (u'10', u'Outubro'),
            (u'11', u'Novembro'),
            (u'12', u'Dezembro'),
    )

    MES_ATUAL = datetime.datetime.now().month

    ANO_GALERIA = (
            (u'2013', u'2013'),
            (u'2014', u'2014'),
    )

    ANO_ATUAL = datetime.datetime.now().year

    TIPO_GALERIA = (
            (u'F', u'Foto'),
            (u'V', u'Vídeo'),
    )

    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    tipo = models.CharField(u'Tipo Galeria',
                           max_length=1,
                           choices=TIPO_GALERIA,
                           default=u'F')
    descricao = models.CharField(u'Descrição',
                              max_length=200,
                              null=False,
                              blank=False)
    mes = models.CharField(u'Mês',
                           max_length=2,
                           choices=MES_GALERIA,
                           default=str(MES_ATUAL))
    ano = models.CharField(u'Ano Letivo',
                           max_length=4,
                           choices=ANO_GALERIA,
                           default=str(ANO_ATUAL))
    destaque = models.BooleanField(u'Destaque',
                                   default=False)
    permite_comentario = models.BooleanField(u'Permite Comentário',
                                             default=False)

    def __unicode__(self):
        return self.titulo


class GaleriaResource(models.Model):
    """
    Resource (Foto ou Video)
    """
    galeria = models.ForeignKey(Galeria, verbose_name=u'Galeria')
    url_resource = models.CharField(u'Link/URL',
                                    max_length=200,
                                    null=True,
                                    blank=True)
    upload_resource = models.FileField('Arquivo',
                                       upload_to = u'galerias',
                                       null=True,
                                       blank=True)
    action_resource = models.CharField(u'Ação ao Clicar',
                                       max_length=200,
                                       null=True,
                                       blank=True)


class Publicacao(models.Model):
    """
    Publicação de conteúdo dinâmico:
    Dicas, Avisos, Diário Online
    """
    TIPO_PUBLICACAO = (
            ('A', 'Aviso'),
            ('D', 'Dicas'),
            ('N', 'Diário Online'),
    )

    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    data_hora = models.DateTimeField(u'Data',
                                     null=False,
                                     blank=False)
    data_publicacao = models.DateTimeField(u'Data da Publicação',
                                           auto_now_add=True)
    palavras_chaves = models.CharField(u'Palavras Chaves',
                                       max_length=200,
                                       null=False,
                                       blank=False)
    tipos = models.CharField(u'Tipos',
                            max_length=1,
                            choices=TIPO_PUBLICACAO,
                            default=u'1')
    introducao = models.TextField(u'Introdução',
                                 blank=False,
                                 null=False)
    completa = models.TextField(u'Conteúdo',
                                blank=False,
                                null=False)
    miniatura_publicacao = models.ImageField(u'Miniatura',
                                             upload_to=u'publicacao')
    galeria = models.ForeignKey(Galeria,
                                verbose_name=u'Galeria',
                                null=True,
                                blank=True)
    destaque = models.BooleanField(u'Destaque',
                                   default=False)
    permite_comentario = models.BooleanField(u'Permite Comentário',
                                             default=False)
    rascunho = models.BooleanField(u'Rascunho', default=True)

    def __unicode__(self):
        return self.titulo


class Pagina(models.Model):
    """
    Página de conteúdo.
    """
    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    conteudo = models.TextField(u'Conteúdo',
                                blank=False,
                                null=False)
    palavras_chaves = models.CharField(u'Palavras Chaves',
                                       max_length=200,
                                       null=False,
                                       blank=False)
    permite_comentario = models.BooleanField(u'Permite Comentário',
                                             default=False)
    rascunho = models.BooleanField(u'Rascunho',
                                   default=True)

    def __unicode__(self):
        return self.titulo


class Menu(models.Model):
    """
    Menu montando dinâmicamente.
    """
    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    endereco = models.CharField(u'endereço',
                                max_length=200,
                                null=False,
                                blank=False)
    ordem = models.IntegerField(u'Ordem De Exibição',
                                null=False,
                                blank=False)
    nivel = models.IntegerField(u'Nível do Menu',
                                null=False,
                                blank=False)

    pagina = models.ForeignKey(Pagina,
                               verbose_name=u'Página',
                               null=True)
    menu_pai = models.ForeignKey('self',
                                 null=True,
                                 blank=True,
                                 related_name=u'Menu Pai')
    palavras_chaves = models.CharField(u'Palavras Chaves',
                                       max_length=200,
                                       null=False,
                                       blank=False)
    rascunho = models.BooleanField(u'Rascunho',
                                   default=True)

    def __unicode__(self):
        return self.titulo


class Depoimento(models.Model):
    """
    Depoimentos de pais, alunos e parceiros.
    depoimento, pessoa
    """
    conteudo = models.TextField(u'Conteúdo',
                                blank=False,
                                null=False)
    autor = models.CharField(u'Autor',
                              max_length=200,
                              null=False,
                              blank=False)


class Professor(models.Model):
    """
    Professores da Escola.
    """
    nome = models.CharField(u'Nome',
                             max_length=200,
                             null=False,
                             blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)

    def __unicode__(self):
        return self.nome

class Servico(models.Model):
    """
    Serviços prestados pela escola.
    """
    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    professor = models.ForeignKey(Professor,
                                  verbose_name=u'Professor(a)')
    conteudo_programatico = models.TextField(u'Conteúdo Programático',
                                             blank=False,
                                             null=False)
    atividades_incluidas = models.TextField(u'Atividades Incluídas',
                                            blank=False,
                                            null=False)
    atividades_extras = models.TextField(u'Atividades Extras',
                                         blank=False,
                                         null=False)
    rotina_diaria = models.TextField(u'Rotina Diária',
                                     blank=False,
                                     null=False)
    observacoes =models.TextField(u'Observações',
                                  blank=False,
                                  null=False)

    def __unicode__(self):
        return self.titulo


class MaterialEscolar(models.Model):
    """
    Material escolar utilizado no ano letivo.
    tipo, miniatura, anexo, ano_letivo
    """
    ANO_LETIVO = (
            (u'2013', u'2013'),
            (u'2014', u'2014'),
    )

    ANO_ATUAL = datetime.datetime.now().year

    ano = models.CharField(u'Ano Letivo',
                           max_length=4,
                           choices=ANO_LETIVO,
                           default=str(ANO_ATUAL))
    servico = models.ForeignKey(Servico,
                                verbose_name=u'Tipo')
    miniatura = models.ImageField(u'Miniatura',
                                  upload_to=u'material_escolar')
    anexo_file = models.FileField('Anexo',
                                  upload_to = u'material_escolar',
                                  null=False,
                                  blank=False)


class ConteudoDownload(models.Model):
    """
    Conteúdos para download:
    Músicas, Papéis de Parede, Desenhos para pintar, Material de Apoio.
    """
    TIPO_UPLOAD = (
            (u'1', u'Música'),
            (u'2', u'Papél de Parede'),
            (u'3', u'Desenho para Pintar'),
            (u'4', u'Material de Apoio'),)

    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    descricao = models.CharField(u'Descrição',
                              max_length=200,
                              null=False,
                              blank=False)
    tipo = models.CharField(u'Tipo',
                            max_length=1,
                            choices=TIPO_UPLOAD,
                            default=u'1')
    miniatura = models.ImageField(u'Miniatura',
                                  upload_to=u'downloads')
    conteudo_file = models.FileField('Arquivo',
                                  upload_to = u'downloads',
                                  null=False,
                                  blank=False)

    def __unicode__(self):
        return self.titulo


class Recomendacao(models.Model):
    """
    Recomendações de leitura, vídeo, música, texto, links e etc.
    """
    TIPO_RECOMENDACAO = (
            (u'1', u'Livro'),
            (u'2', u'Vídeo'),
            (u'3', u'Música'),
            (u'4', u'Texto'),
            (u'5', u'Link'),)

    tipo = models.CharField(u'Tipo',
                            max_length=1,
                            choices=TIPO_RECOMENDACAO,
                            default=u'1')
    descricao = models.CharField(u'Descrição',
                              max_length=200,
                              null=False,
                              blank=False)
    acao_link = models.CharField(u'Ação Link',
                              max_length=200,
                              null=True,
                              blank=True)
    miniatura = models.ImageField(u'Miniatura',
                                  upload_to=u'imagens')
    destaque = models.BooleanField(u'Destaque',
                                   default=False)

    def __unicode__(self):
        return self.descricao


class Parametro(models.Model):
    valor = models.CharField(u'Valor',
                              max_length=200,
                              null=False,
                              blank=False)


class Banner(models.Model):
    """
    Banners
    """
    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    descricao = models.CharField(u'Descrição',
                              max_length=200,
                              null=False,
                              blank=False)
    url_resource = models.CharField(u'Link/URL',
                                    max_length=200,
                                    null=True,
                                    blank=True)
    upload_resource = models.FileField('Arquivo',
                                       upload_to = u'banners',
                                       null=True,
                                       blank=True)
    action_resource = models.CharField(u'Ação ao Clicar',
                                       max_length=200,
                                       null=True,
                                       blank=True)

    def __unicode__(self):
        return self.titulo
