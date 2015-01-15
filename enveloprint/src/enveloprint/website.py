# -*- coding: utf-8 -*-
import web
from web.contrib import PyRSS2Gen
import render_website
import model
import forms

import logging

from paginator import Paginator, PaginatorSearch

from datetime import datetime
from utils import break_string
from google.appengine.api import mail

urls = (
  '', 'Index',
  '/', 'Index',
  '/index', 'Index',
  '/atendimento_online', 'Atendimento',
  '/orcamento', 'Orcamento',
  '/contato', 'Contato',
  '/pagina/(.+)', 'pagina',
  '/detalhar/(.+)/(.+)', 'detalhar',
  '/listar/(.+)', 'listar'
)

class Index:
    def GET(self):
        return render_website.layout(render_website.index())

class Atendimento:
    def GET(self):
        return render_website.layout(render_website.atendimento())

class Orcamento:
    def GET(self):
        frm = forms.getForm('Pedido')
        return render_website.layout(render_website.pedido(frm))

    def POST(self):
        frm = forms.getForm('Pedido')
        if frm.validates():
            try:
                assunto="Orcamento pelo Site da Enveloprint"
                razao_social='Razao Social: ' + break_string(frm.d.razao_social)
                cnpj='CNPJ: ' + break_string(frm.d.cnpj)
                telefone='Telefone: ' + break_string(frm.d.telefone)
                email='E-mail: ' + break_string(frm.d.email)
                produtos ='Produtos: ' + '\n\t'
                produtos += "Codigo: " + frm.d.cod_01 + " - Qtde: " + break_string(frm.d.qtde_01)
                produtos += "Codigo: " + frm.d.cod_02 + " - Qtde: " + break_string(frm.d.qtde_02)
                produtos += "Codigo: " + frm.d.cod_03 + " - Qtde: " + break_string(frm.d.qtde_03)
                produtos += "Codigo: " + frm.d.cod_04 + " - Qtde: " + break_string(frm.d.qtde_04)
                produtos += "Codigo: " + frm.d.cod_05 + " - Qtde: " + break_string(frm.d.qtde_05)
                produtos += "Codigo: " + frm.d.cod_06 + " - Qtde: " + break_string(frm.d.qtde_06)
                produtos += "Codigo: " + frm.d.cod_07 + " - Qtde: " + break_string(frm.d.qtde_07)
                produtos += "Codigo: " + frm.d.cod_08 + " - Qtde: " + break_string(frm.d.qtde_08)
                produtos += "Codigo: " + frm.d.cod_09 + " - Qtde: " + break_string(frm.d.qtde_09)
                produtos += "Codigo: " + frm.d.cod_10 + " - Qtde: " + break_string(frm.d.qtde_10)
                produtos += "Codigo: " + frm.d.cod_11 + " - Qtde: " + break_string(frm.d.qtde_11)
                produtos += "Codigo: " + frm.d.cod_12 + " - Qtde: " + break_string(frm.d.qtde_12)
                produtos += "Codigo: " + frm.d.cod_13 + " - Qtde: " + break_string(frm.d.qtde_13)
                produtos += "Codigo: " + frm.d.cod_14 + " - Qtde: " + break_string(frm.d.qtde_14)
                produtos += "Codigo: " + frm.d.cod_15 + " - Qtde: " + break_string(frm.d.qtde_15)
                produtos += "Codigo: " + frm.d.cod_16 + " - Qtde: " + break_string(frm.d.qtde_16)
                produtos += "Codigo: " + frm.d.cod_17 + " - Qtde: " + break_string(frm.d.qtde_17)
                produtos += "Codigo: " + frm.d.cod_18 + " - Qtde: " + break_string(frm.d.qtde_18)
                produtos += "Codigo: " + frm.d.cod_19 + " - Qtde: " + break_string(frm.d.qtde_19)
                produtos += "Codigo: " + frm.d.cod_20 + " - Qtde: " + break_string(frm.d.qtde_20)
                produtos += "Codigo: " + frm.d.cod_21 + " - Qtde: " + break_string(frm.d.qtde_21)
                mensagem='Obs: ' + '\n\t' + break_string(frm.d.obs)
                mensagem_completa = razao_social + cnpj + telefone + email + produtos + mensagem
                message = mail.EmailMessage()
                message.sender = 'enveloprintsite@gmail.com'
                message.to = 'comercial@enveloprint.com.br'
                message.subject = assunto
                message.body = mensagem_completa
                message.send()

                return render_website.layout(render_website.agradece_pedido())
            except Exception:
                raise
        else:
            return render_website.layout(render_website.pedido(frm))

class Contato:
    def GET(self):
        frm = forms.getForm('Contato')
        return render_website.layout(render_website.contato(frm))

    def POST(self):
        frm = forms.getForm('Contato')
        if frm.validates():
            try:
                assunto=break_string(frm.d.assunto)
                nome='O visitante ' + break_string(frm.d.nome)
                telefone=' com o telefone: ' + break_string(frm.d.telefone)
                email=' com o E-mail: ' + break_string(frm.d.email)
                mensagem='Ele te deixou a seguinte mensagem: ' + '\n\t' + break_string(frm.d.mensagem_adicional)
                mensagem_completa = nome + telefone + email + mensagem

                message = mail.EmailMessage()
                message.sender = 'enveloprintsite@gmail.com'
                message.to = 'comercial@enveloprint.com.br'
                message.subject = assunto
                message.body = mensagem_completa
                message.send()

                return render_website.layout(render_website.agradece_contato())
            except Exception:
                raise
        else:
            return render_website.layout(render_website.contato(frm))

class pagina:
    def GET(self, pagina_name):
        conteudo = model.get_pagina('/pagina/' + pagina_name)
        return render_website.layout(render_website.pagina(conteudo))

class listar():
    def GET(self, param):
        entity = model.get_model_by_name(param)
        pagination = Paginator(web.input(), entity)
        return render_website.layout(render_website.listar_entity(pagination))

    def POST(self, param):
        entity = model.get_model_by_name(param)
        pagination = Paginator(web.input(), entity)
        return render_website.layout(render_website.listar_entity(pagination))

class detalhar:
    def GET(self, classe, slug):
        entity = model.exists_entity(model.get_model_by_name(classe), 'slug', slug)
        return render_website.layout(render_website.detalhar(entity))

app = web.application(urls, globals())

def main():
    pass
