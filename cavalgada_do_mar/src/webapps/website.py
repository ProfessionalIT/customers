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
  '/historico', 'Historico',
  '/projetos-sociais', 'ProjetosSociais',
  '/percurso', 'Percurso',
  '/atividades', 'Atividades',
  '/comenda', 'Comenda',
  '/premiacoes', 'Premiacoes', 
  '/dicas', 'Dicas',
  '/albuns', 'Albuns',
  '/fotos', 'Fotos',
  '/videos', 'Videos',
  '/depoimentos', 'Depoimentos',
  '/patrocinadores', 'Patrocionadores',
  '/inscricao', 'Inscricao',
  '/noticias', 'Noticias',
  '/noticia/(.+)', 'Noticia',
  '/boletins', 'Boletins',
  '/boletim/(.+)', 'Boletim',
  '/fale-conosco', 'Contato',
  '/agradece-contato', 'Agradecimento',
  '/rss', 'RSS'
)

class Index:
    def GET(self):
        return render.layout('menu_home', 'Página Inicial do Site', render.index())

class QuemSomos:
    def GET(self):
        return render.layout('menu_quem_somos', 'Fundação Cavalgada do Mar', render.pagina('quem-somos'))

class Historico:
    def GET(self):
        return render.layout('menu_historico', 'Nosso Histórico', render.pagina('historico'))

class ProjetosSociais:
    def GET(self):
        return render.layout('menu_projetos_sociais', 'Nossos Projetos Sociais', render.pagina('projetos-sociais'))

class Percurso:
    def GET(self):
        return render.layout('menu_percurso', 'O Percurso da Cavalgada', render.pagina('percurso'))

class Atividades:
    def GET(self):
        return render.layout('menu_atividades', 'As Atividades', render.pagina('atividades'))

class Comenda:
    def GET(self):
        return render.layout('menu_comenda', 'A Comenda e os Comendadores', render.pagina('comenda'))

class Premiacoes:
    def GET(self):
        return render.layout('menu_premiacoes', 'As Premiações', render.pagina('premiacoes'))

class Dicas:
    def GET(self):
        return render.layout('menu_dicas', 'Dicas da Cavalgada do Mar', render.pagina('dicas'))

class Albuns:
    def GET(self):
        return render.layout('menu_albuns', 'Os Albúns', render.pagina('albuns'))

class Fotos:
    def GET(self):
        return render.layout('menu_albuns', 'As Fotos', render.pagina('fotos'))

class Videos:
    def GET(self):
        return render.layout('menu_albuns', 'Os Videos', render.pagina('videos'))

class Depoimentos:
    def GET(self):
        return render.layout('menu_depoimentos', 'Os Depoímentos', render.pagina('depoimentos'))

class Patrocionadores:
    def GET(self):
        return render.layout('menu_patrocinadores', 'Os Patrocinadores', render.pagina('patrocinadores'))

class Inscricao:
    def GET(self):
        return render.layout('menu_inscricao', 'Faça sua Inscrição', render.pagina('inscricao'))

class Noticias:
    def GET(self):
        pagination = PaginatorPublicacao(web.input(), 'noticias', order='data_hora desc')
        return render.layout('menu_noticias', 'Notícias', render.noticias(pagination))

    def POST(self):
        pagination = PaginatorPublicacao(web.input(), 'noticias', order='data_hora desc')
        return render.layout('menu_noticias', 'Notícias', render.noticias(pagination))

class Noticia:
    def GET(self, slug_noticia):
        return render.layout('menu_noticias', 'Notícias', render.noticia(slug_noticia))

class Boletins:
    def GET(self):
        pagination = PaginatorPublicacao(web.input(), 'boletins', order='data_hora desc')
        return render.layout('menu_home', 'Boletins', render.boletins(pagination))

    def POST(self):
        pagination = PaginatorPublicacao(web.input(), 'boletins', order='data_hora desc')
        return render.layout('menu_home', 'Boletins', render.boletins(pagination))

class Boletim:
    def GET(self, slug_boletim):
        return render.layout('menu_home', 'Boletins', render.boletim(slug_boletim))

class Contato:
    def GET(self):
        return render.layout('menu_fale_conosco', 'Contatos', render.contato())

    def POST(self):
        try:
            i = web.input()
            assunto='Assunto: ' + break_string(i.assunto)
            nome='O visitante ' + break_string(i.nome)
            telefone=' com o telefone: ' + break_string(i.telefone)
            email=' com o E-mail: ' + break_string(i.email)
            mensagem='Deixou a seguinte mensagem: ' + '\n\t' + break_string(i.texto)
            mensagem_completa = nome + telefone + email + mensagem
            to_email = 'henrique@equineclinic.com.br'
            web.sendmail(email, to_email, '%s' % assunto, '%s' % mensagem_completa)
            raise web.seeother('/agradece-contato')
        except Exception:
            raise

class Agradecimento:
    def GET(self):
        return render.layout('menu_fale_conosco', 'Contatos', render.pagina('agradece-contato'))

class RSS:
    def GET(self):
        items=[]
        noticias = model.get_publicacoes_rss('Notícia')
        boletins = model.get_publicacoes_rss('Boletim')
        
        if noticias:
            for entry in noticias:
                link= WEBSITE_URL + '/noticia/%s' % entry.slug
                items.append(PyRSS2Gen.RSSItem(title=entry.titulo,
                            link=link,
                            description=entry.intro,
                            author='Fundação Cultural Cavalgada do Mar em Viamão - RS',
                            guid=PyRSS2Gen.Guid(link),
                            pubDate=entry.data_hora))

        if boletins:
            for entry in boletins:
                link= WEBSITE_URL + '/boletim/%s' % entry.slug
                items.append(PyRSS2Gen.RSSItem(title=entry.titulo,
                            link=link,
                            description=entry.intro,
                            author='Fundação Cultural Cavalgada do Mar em Viamão - RS',
                            guid=PyRSS2Gen.Guid(link),
                            pubDate=entry.data_hora))
        
        titulo = 'RSS da Cavalgada do Mar'
        descricao = 'Últimas publicações da Fundação Cultural Cavalgada do Mar em Porto Alegre - RS.'
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
