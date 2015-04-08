# -*- coding: utf-8 -*-
import web
from web.contrib import PyRSS2Gen
import render_website as render
from model import all_produtos_rss
import forms

import logging
from paginator import Paginator, PaginatorSearch
from datetime import datetime

from utils import break_string

urls = (
  '', 'Index',
  '/', 'Index',
  '/index', 'Index',
  '/empresa', 'Empresa',
  '/manutencao', 'Manutencao',
  '/produtos', 'Produtos',
  '/produto/(.+)', 'Produto',
  '/contato', 'Contato',
  '/agradece-contato', 'Agradecimento',
  '/rss', 'RSS'
)

class Index:
    def GET(self):
        return render.layout('menu_home',render.index())

class Empresa:
    def GET(self):
        return render.layout('menu_empresa',render.pagina('empresa'))

class Manutencao:
    def GET(self):
        return render.layout('menu_manutencao',render.pagina('manutencao'))

class Produtos:
    def GET(self):
        return render.layout('menu_produtos',render.produtos())

class Produto:
    def GET(self, slug_produto):
        print '#################### ' + slug_produto
        return render.layout(slug_produto, render.produto(slug_produto))

class Contato:
    def GET(self):
        return render.layout('menu_contato',render.pagina('contato'))

    def POST(self):
        try:
            i = web.input()
            assunto='Contato realizado pelo site www.persianaspaludo.com.br'
            nome='O visitante ' + break_string(i.nome_contato)
            telefone=' com o telefone: ' + break_string(i.telefone_contato)
            email=' com o E-mail: ' + break_string(i.email_contato)
            mensagem='Deixou a seguinte mensagem: ' + '\n\t' + break_string(i.mensagem_contato)
            mensagem_completa = nome + telefone + email + mensagem
            to_email = 'atendimento@persianaspaludo.com.br'
            web.sendmail(email, to_email, '%s' % assunto, '%s' % mensagem_completa)
            raise web.seeother('/agradece-contato')
        except Exception:
            raise

class Agradecimento:
    def GET(self):
        return render.layout('menu_contato',render.agradecimento())

class RSS:
    def GET(self):
        items=[]
        entries=all_produtos_rss()

        for entry in entries:
            link='http://www.persianaspaludo.com.br/produto/%s' % entry.slug
            items.append(PyRSS2Gen.RSSItem(title=entry.titulo,
                        link=link,
                        description=entry.caracteristicas,
                        author='Persianas Paludo.',
                        guid=PyRSS2Gen.Guid(link),
                        pubDate=entry.data_criacao))

        rss=PyRSS2Gen.RSS2(title='RSS dos Produtos da Persianas Paludo.',
                        link='http://www.persianaspaludo.com.br/rss',
                        description='Produtos da Persianas Paludo.',
                        lastBuildDate=datetime.now(),
                        items=items)

        web.header('Content-Type', 'application/rss+xml; charset=iso-8859-1')
        return rss.to_xml()

app = web.application(urls, globals())

def main():
    pass
