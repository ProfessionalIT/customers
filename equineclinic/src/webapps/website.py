# -*- coding: utf-8 -*-
import web
from web.contrib import PyRSS2Gen
import render_website as render
import model
import forms

import logging
from paginator import Paginator, PaginatorSearch, PaginatorPublicacao
from datetime import datetime

from configuration import WEBSITE_URL
from utils import break_string

urls = (
  '', 'Index',
  '/', 'Index',
  '/index', 'Index',
  '/quem-somos', 'QuemSomos',
  '/veterinarios', 'Veterinarios',
  '/servicos', 'Servicos',
  '/servico/(.+)', 'Servico',
  '/noticias', 'Noticias',
  '/noticia/(.+)', 'Noticia',
  '/eventos', 'Eventos',
  '/evento/(.+)', 'Evento',
  '/artigos', 'Artigos',
  '/artigo/(.+)', 'Artigo',
  '/pesquisas', 'Pesquisas',
  '/pesquisa/(.+)', 'Pesquisa',
  '/clientes', 'Clientes',
  '/parceiros', 'Parceiros',
  '/contatos', 'Contato',
  '/agradece-contato', 'Agradecimento',
  '/rss', 'RSS'
)

class Index:
    def GET(self):
        return render.layout('menu_home', 'Página Inicial do Site', render.index())

class QuemSomos:
    def GET(self):
        return render.layout('menu_empresa', 'A Clínica', render.pagina('quem-somos'))

class Veterinarios:
    def GET(self):
        return render.layout('menu_veterinarios', 'Veterinários', render.pagina('veterinarios'))

class Servicos:
    def GET(self):
        return render.layout('menu_servico', 'Serviços', render.pagina('servicos'))

class Servico:
    def GET(self, slug_servico):
        return render.layout('menu_servico', 'Serviços', render.pagina(slug_servico))

class Noticias:
    def GET(self):
        pagination = PaginatorPublicacao(web.input(), 'noticias')
        return render.layout('menu_noticias', 'Notícias', render.noticias(pagination))

    def POST(self):
        pagination = PaginatorPublicacao(web.input(), 'noticias')
        return render.layout('menu_noticias', 'Notícias', render.noticias(pagination))

class Noticia:
    def GET(self, slug_noticia):
        return render.layout('menu_noticias', 'Notícias', render.noticia(slug_noticia))

class Eventos:
    def GET(self):
        pagination = PaginatorPublicacao(web.input(), 'eventos')
        return render.layout('menu_eventos', 'Eventos', render.eventos(pagination))

    def POST(self):
        pagination = PaginatorPublicacao(web.input(), 'eventos')
        return render.layout('menu_eventos', 'Eventos', render.eventos(pagination))

class Evento:
    def GET(self, slug_evento):
        return render.layout('menu_eventos', 'Eventos', render.evento(slug_evento))

class Artigos:
    def GET(self):
        pagination = PaginatorPublicacao(web.input(), 'artigos')
        return render.layout('menu_artigos', 'Artigos', render.artigos(pagination))

    def POST(self):
        pagination = PaginatorPublicacao(web.input(), 'artigos')
        return render.layout('menu_artigos', 'Artigos', render.artigos(pagination))

class Artigo:
    def GET(self, slug_artigo):
        return render.layout('menu_artigos', 'Artigos', render.artigo(slug_artigo))

class Pesquisas:
    def GET(self):
        pagination = PaginatorPublicacao(web.input(), 'pesquisas')
        return render.layout('menu_pesquisas', 'Pesquisas', render.pesquisas(pagination))

    def POST(self):
        pagination = PaginatorPublicacao(web.input(), 'pesquisas')
        return render.layout('menu_noticias', 'Pesquisas', render.pesquisas(pagination))

class Pesquisa:
    def GET(self, slug_pesquisa):
        return render.layout('menu_pesquisas', 'Pequisas', render.pesquisa(slug_pesquisa))

class Clientes:
    def GET(self):
        return render.layout('menu_clientes', 'Clientes', render.pagina('clientes'))

class Parceiros:
    def GET(self):
        return render.layout('menu_parceiros', 'Parceiros', render.pagina('parceiros'))

class Contato:
    def GET(self):
        return render.layout('menu_contato', 'Contatos', render.contato())

    def POST(self):
        try:
            i = web.input()
            assunto='Assunto: ' + break_string(i.assunto)
            nome='O visitante ' + break_string(i.nome)
            telefone=' com o telefone: ' + break_string(i.telefone)
            estado='  do estado: ' + break_string(i.estado)
            cidade='  da cidade: ' + break_string(i.cidade)
            bairro='  do bairro: ' + break_string(i.bairro)
            email=' com o E-mail: ' + break_string(i.email)
            mensagem='Deixou a seguinte mensagem: ' + '\n\t' + break_string(i.texto)
            mensagem_completa = nome + telefone + estado + cidade + bairro + email + mensagem
            to_email = 'henrique@equineclinic.com.br'
            web.sendmail(email, to_email, '%s' % assunto, '%s' % mensagem_completa)
            raise web.seeother('/agradece-contato')
        except Exception:
            raise

class Agradecimento:
    def GET(self):
        return render.layout('menu_contato', 'Contatos', render.pagina('agradece'))

class RSS:
    def GET(self):
        items=[]
        noticias = model.get_publicacoes_rss('Notícia')
        eventos = model.get_publicacoes_rss('Eventos')
        artigos = model.get_publicacoes_rss('Artigos')
        pesquisas = model.get_publicacoes_rss('Pesquisas')
        
        for entry in noticias:
            link= WEBSITE_URL + '/noticia/%s' % entry.slug
            items.append(PyRSS2Gen.RSSItem(title=entry.titulo,
                        link=link,
                        description=entry.intro,
                        author='Equine Clinic - Clínica de Hipiatria em Viamão - RS',
                        guid=PyRSS2Gen.Guid(link),
                        pubDate=entry.data_hora))

        for entry in eventos:
            link= WEBSITE_URL + '/evento/%s' % entry.slug
            items.append(PyRSS2Gen.RSSItem(title=entry.titulo,
                        link=link,
                        description=entry.intro,
                        author='Equine Clinic - Clínica de Hipiatria em Viamão - RS',
                        guid=PyRSS2Gen.Guid(link),
                        pubDate=entry.data_hora))

        for entry in artigos:
            link= WEBSITE_URL + '/artigo/%s' % entry.slug
            items.append(PyRSS2Gen.RSSItem(title=entry.titulo,
                        link=link,
                        description=entry.intro,
                        author='Equine Clinic - Clínica de Hipiatria em Viamão - RS',
                        guid=PyRSS2Gen.Guid(link),
                        pubDate=entry.data_hora))

        for entry in pesquisas:
            link= WEBSITE_URL + '/pesquisa/%s' % entry.slug
            items.append(PyRSS2Gen.RSSItem(title=entry.titulo,
                        link=link,
                        description=entry.intro,
                        author='Equine Clinic - Clínica de Hipiatria em Viamão - RS',
                        guid=PyRSS2Gen.Guid(link),
                        pubDate=entry.data_hora))

        titulo = 'RSS da Equine Clinic'
        descricao = 'Últimas publicações da Equine Clinic - Clínica de Hipiatria em Viamão - RS'
        rss=PyRSS2Gen.RSS2(title=titulo,
                        link= WEBSITE_URL + '/rss',
                        description=descricao,
                        lastBuildDate=datetime.now(),
                        items=items)

        web.header('Content-Type', 'application/rss+xml; charset=utf-8')
        return rss.to_xml()

app = web.application(urls, globals())

def main():
    pass
