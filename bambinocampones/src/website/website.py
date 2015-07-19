# -*- coding: utf-8 -*-
import web
from web.contrib import PyRSS2Gen
import render_website as render
import model
from datetime import datetime

from utils import break_string
from forms import getContatoForm, getOrcamentoForm


urls = (
  '', 'Index',
  '/', 'Index',
  '/index', 'Index',
  '/get-content/(.*)', 'AjaxGetPageContent',
  '/empresa', 'Empresa',
  '/servicos', 'Servicos',
  '/fotolito', 'Fotolito',
  '/gravacao-de-chapa', 'GravacaoDeChapa',
  '/impressao-digital', 'ImpressaoDigital',
  '/impressao-offset', 'ImpressaoOffset',
  '/acabamento', 'Acabamento',
  '/portifolio', 'Portifolio',
  '/agenda', 'Agenda',
  '/blocos', 'Blocos',
  '/cadernos-executivos', 'CadernosExecutivos',
  '/caixas-de-anotacao', 'CaixasDeAnotacao',
  '/calendarios-de-mesa', 'CalendarioDeMesa',
  '/capa-de-cd', 'CapaDeCD',
  '/cartao-postal', 'CartaoPostal',
  '/cartela-para-expositor', 'CartelaParaExpositor',
  '/cartoes-de-visita', 'CartoesDeVisita',
  '/catalagos', 'Catalogos',
  '/convites', 'Convites',
  '/embalagens', 'Embalagens',
  '/encartes', 'Encartes',
  '/envelopes', 'Envelopes',
  '/etiquetas', 'Etiquetas',
  '/folders', 'Folders',
  '/folhas-timbradas', 'FolhasTimbradas',
  '/imas-de-geladeira', 'ImasDeGeladeira',
  '/livros', 'Livros',
  '/manuais', 'Manuais',
  '/notas-fiscais', 'NotasFiscais',
  '/panfletos', 'Panfletos',
  '/pastas', 'Pastas',
  '/receituarios', 'Receituarios',
  '/revistas', 'Revistas',
  '/risque-e-rabisque', 'RisqueRabisque',
  '/sacolas', 'Sacolas',
  '/folha-a4', 'FolhaA4',
  '/folha-a3', 'FolhaA3',
  '/material-de-escritorio', 'MaterialDeEscritorio',
  '/orcamento', 'Orcamento',
  '/localizacao', 'Localizacao',
  '/contato', 'Contato',
  '/agradece-contato', 'Agradecimento',
  '/agradece-orcamento', 'AgradecimentoOrcamento',
  '/inscrever', 'Inscrever',
  '/agradece-inscricao', 'AgradecimentoInscrever',
  '/rss', 'RSS'
)


class AjaxGetPageContent():
    def POST(self, param):
        return render.ajax_page_content(param)


class Index:
    def GET(self):
        return render.layout('menu_home', render.index())


class Empresa:
    def GET(self):
        return render.layout('menu_empresa', render.pagina('empresa'))


class Servicos:
    def GET(self):
        return render.layout('menu_servicos', render.pagina('servicos'))


class Fotolito:
    def GET(self):
        return render.layout('menu_servicos', render.pagina('fotolito'))


class GravacaoDeChapa:
    def GET(self):
        return render.layout('menu_servicos',
                             render.pagina('gravacao-de-chapa'))


class ImpressaoDigital:
    def GET(self):
        return render.layout('menu_servicos',
                             render.pagina('impressao-digital'))


class ImpressaoOffset:
    def GET(self):
        return render.layout('menu_servicos',
                             render.pagina('impressao-offset'))


class Acabamento:
    def GET(self):
        return render.layout('menu_servicos', render.pagina('acabamento'))


class Portifolio:
    def GET(self):
        return render.layout('menu_portifolio', render.portifolio())


class Agenda:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('agenda'))


class Blocos:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('blocos'))


class CadernosExecutivos:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('cadernos-executivos'))


class CaixasDeAnotacao:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('caixas-de-anotacao'))


class CalendarioDeMesa:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('calendario-de-mesa'))


class CapaDeCD:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('capa-de-cd'))


class CartaoPostal:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('cartao-postal'))


class CartelaParaExpositor:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('cartela-para-expositor'))


class CartoesDeVisita:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('cartoes-de-visita'))


class Catalogos:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('catalagos'))


class Convites:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('convites'))


class Embalagens:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('embalagens'))


class Encartes:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('encartes'))


class Envelopes:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('envelopes'))


class Etiquetas:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('etiquetas'))


class Folders:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('folders'))


class FolhasTimbradas:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('folhas-timbradas'))


class ImasDeGeladeira:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('imas-de-geladeira'))


class Livros:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('livros'))


class Manuais:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('manuais'))


class NotasFiscais:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('notas-fiscais'))


class Panfletos:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('panfletos'))


class Pastas:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('pastas'))


class Receituarios:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('receituarios'))


class Revistas:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('revistas'))


class RisqueRabisque:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('risque-e-rabisque'))


class Sacolas:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('sacolas'))


class FolhaA4:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('folha-a4'))


class FolhaA3:
    def GET(self):
        return render.layout('menu_portifolio', render.pagina('folha-a3'))


class MaterialDeEscritorio:
    def GET(self):
        return render.layout('menu_portifolio',
                             render.pagina('material-de-escritorio'))


class Orcamento:
    def GET(self):
        form = getOrcamentoForm()
        return render.layout('menu_orcamento', render.orcamento(form=form))

    def POST(self):
        import os
        rootpath = os.path.abspath(os.path.dirname(__file__))
        upload_path = os.path.abspath(rootpath + '/uploads/')
        try:
            form = getOrcamentoForm()
            if form.validates():
                mensagem = break_string('===== Dados Gerais =====')
                mensagem += 'Empresa/Nome: ' + \
                                  break_string(form['razao_social_nome'].value)
                mensagem += 'CNPJ/CPF: ' + break_string(form['cnpj_cpf'].value)
                mensagem += 'Fone: ' + break_string(form['telefone'].value)
                mensagem += 'E-mail: ' + \
                                     break_string(form['mail_orcamento'].value)
                mensagem += break_string('===== Dados Produto =====')
                mensagem += 'Produto: ' + break_string(form['produto'].value)
                mensagem += 'Outro Produto: ' + \
                                      break_string(form['outro_produto'].value)
                mensagem += 'Formato (em cm) Aberto: ' + \
                                     break_string(form['formato_aberto'].value)
                mensagem += 'Formato (em cm) Fechado: ' + \
                                    break_string(form['formato_fechado'].value)
                mensagem += 'Quantidade: ' + \
                                         break_string(form['quantidade'].value)
                mensagem += 'Tipo de Papel: ' + \
                                         break_string(form['tipo_papel'].value)
                mensagem += 'Cores: ' + break_string(form['cores'].value)
                mensagem += 'Gramatura: ' + \
                                          break_string(form['gramatura'].value)
                mensagem += \
                   break_string('===== Revista/Livros/Catalogos/Manuais =====')
                mensagem += break_string('===== Dados da Capa =====')
                mensagem += 'Capa: ' + break_string(form['capa'].value)
                mensagem += 'Formato Capa: ' + \
                                       break_string(form['formato_capa'].value)
                mensagem += 'Papel Capa: ' + \
                                         break_string(form['papel_capa'].value)
                mensagem += 'Gramatura Capa: ' + \
                                     break_string(form['gramatura_capa'].value)
                mensagem += 'Cores Capa: ' + \
                                         break_string(form['cores_capa'].value)
                mensagem += 'Orelha Capa: ' + \
                                        break_string(form['orelha_capa'].value)
                mensagem += break_string('===== Dados do Miolo =====')
                mensagem += 'Miolo: ' + break_string(form['miolo'].value)
                mensagem += 'Formato Miolo: ' + \
                                      break_string(form['formato_miolo'].value)
                mensagem += 'Papel Miolo: ' + \
                                        break_string(form['papel_miolo'].value)
                mensagem += 'Gramatura Miolo: ' + \
                                    break_string(form['gramatura_miolo'].value)
                mensagem += 'Cores Miolo:  ' + \
                                        break_string(form['cores_miolo'].value)
                mensagem += 'QTDE Paginas Miolo: ' + \
                            break_string(form['quantidade_pagina_miolo'].value)
                mensagem += break_string('===== Acabamento =====')
                mensagem += 'Plastificacao Fosca: ' + \
                     break_string(form['plastificacao_fosca_acabamento'].value)
                mensagem += 'Numeracao: ' + \
                               break_string(form['numeracao_acabamento'].value)
                mensagem += 'Plastificacao Brilho: ' + \
                    break_string(form['plastificacao_brilho_acabamento'].value)
                mensagem += 'Colagem de Capas: ' + \
                            break_string(form['colagem_capa_acabamento'].value)
                mensagem += 'Plastificacao Bopp Fosca: ' + \
                break_string(form['plastificacao_bopp_fosca_acabamento'].value)
                mensagem += 'Dobras: ' + \
                                  break_string(form['dobras_acabamento'].value)
                mensagem += 'Numero de Dobras: ' + \
                           break_string(form['numero_dobras_acabamento'].value)
                mensagem += 'Plastificacao Bopp Brilho: ' + \
               break_string(form['plastificacao_bopp_brilho_acabamento'].value)
                mensagem += 'Encadernacao: ' + \
                            break_string(form['encardenacao_acabamento'].value)
                mensagem += 'Verniz UV Localizado: ' + \
                    break_string(form['verniz_uv_localizado_acabamento'].value)
                mensagem += 'Wiro: ' + \
                                    break_string(form['wiro_acabamento'].value)
                mensagem += 'Verniz Total: ' + \
                            break_string(form['verniz_total_acabamento'].value)
                mensagem += 'Aspiral: ' + \
                                 break_string(form['aspiral_acabamento'].value)
                mensagem += 'Hot Melt: ' + \
                                break_string(form['hot_melt_acabamento'].value)
                mensagem += break_string('===== Arte e Prova Digital =====')
                mensagem += 'Sem Arte: ' + break_string(form['sem_arte'].value)
                mensagem += 'Com Arte: ' + break_string(form['com_arte'].value)
                mensagem += 'Tipo de Arte: ' + \
                                          break_string(form['tipo_arte'].value)
                mensagem += 'Com Prova Digital: ' + \
                                  break_string(form['com_prova_digital'].value)
                mensagem += 'Sem Prova Digital: ' + \
                                  break_string(form['sem_prova_digital'].value)
                mensagem += \
                        break_string('===== Prazos, Entrega e Pagamento =====')
                mensagem += 'Prazo de Entrega: ' + \
                                   break_string(form['prazo_de_entrega'].value)
                mensagem += 'Forma de Entrega: ' + \
                                   break_string(form['forma_de_entrega'].value)
                mensagem += \
                         break_string('===== Informacoes Complementares =====')
                mensagem += 'Informacoes Complementares: ' + \
                         break_string(form['informacoes_complementares'].value)

                to_email = 'jacque@fenixgrafica.com'
                inputed_data = web.input(arquivo_arte={})

                uploaded_file = inputed_data.arquivo_arte

                if uploaded_file:
                    orcamento_file = open(upload_path + "/" +
                                          uploaded_file.filename, "wb")
                    orcamento_file.write(uploaded_file.file.read())
                    orcamento_file.close()

                    orcamento_file = open(upload_path + "/" +
                                          uploaded_file.filename, "rb")

                    web.sendmail(form['mail_orcamento'].value,
                                 to_email,
                     'Solicitação de Orçamento pelo site www.fenixgrafica.com',
                                 mensagem,
                                 attachments=[orcamento_file])

                    orcamento_file.close()
                else:
                    web.sendmail(form['mail_orcamento'].value,
                                 to_email,
                     'Solicitação de Orçamento pelo site www.fenixgrafica.com',
                                 mensagem)

                raise web.seeother('/agradece-orcamento')
            else:
                return render.layout('menu_orcamento',
                                     render.orcamento(form=form))
        except Exception:
            raise


class AgradecimentoOrcamento:
    def GET(self):
        return render.layout('menu_orcamento',
                             render.pagina('agradece-orcamento'))


class Localizacao:
    def GET(self):
        return render.layout('menu_localizacao', render.localizacao())


class Contato:
    def GET(self):
        form = getContatoForm()
        return render.layout('menu_contato', render.contato(form=form))

    def POST(self):
        try:
            form = getContatoForm()
            if form.validates():
                assunto = 'Contato realizado pelo site www.fenixgrafica.com'
                nome = 'O visitante ' + break_string(form['nome'].value)
                telefone = ' com o telefone: ' + \
                             break_string(form['telefone'].value)
                email = ' com o E-mail: ' + break_string(form['email'].value)
                mensagem = 'Deixou a seguinte mensagem: ' + '\n\t' + \
                            break_string(form['mensagem'].value)
                mensagem_completa = nome + telefone + email + mensagem
                to_email = 'beto@fenixgrafica.com'
                web.sendmail(email,
                             to_email,
                             '%s' % assunto,
                             '%s' % mensagem_completa)
                raise web.seeother('/agradece-contato')
            else:
                return render.layout('menu_contato', render.contato(form=form))
        except Exception:
            raise


class Agradecimento:
    def GET(self):
        return render.layout('menu_contato', render.pagina('agradece'))


class Inscrever:
    def POST(self):
        try:
            i = web.input()
            assunto = '''Inscrição para receber novidades
                         realizada pelo site www.fenixgrafica.com'''
            email = 'O E-mail: ' + break_string(i.email)
            mensagem_completa = email + ' Cadastrou-se para receber novidades.'
            to_email = 'beto@fenixgrafica.com'
            web.sendmail(email,
                         to_email,
                         '%s' % assunto,
                         '%s' % mensagem_completa)
            raise web.seeother('/agradece-inscricao')
        except Exception:
            raise


class AgradecimentoInscrever:
    def GET(self):
        return render.layout('menu_contato',
                             render.pagina('agradece-inscricao'))


class RSS:
    def GET(self):
        items = []
        hoje = datetime.now()
        items.append(
            PyRSS2Gen.RSSItem(
                title='''Fênix Artes Gráficas - Convites, impressos e impressão 
                         digital em Canoas/RS.''',
                description='''Convites, impressos e impressão digital em 
                               Canoas/RS.''',
                author='Gráfica Fênix em Canoas-RS.',
                guid=PyRSS2Gen.Guid('http://www.fenixgrafica.com'),
                pubDate=hoje
            )
        )
        items.append(
            PyRSS2Gen.RSSItem(
                title='''Fênix Artes Gráficas - Convites, impressos e impressão 
                         digital em Canoas/RS - Empresa.''',
                description='''Conheça a nossa empresa.''',
                author='Gráfica Fênix em Canoas-RS.',
                guid=PyRSS2Gen.Guid('http://www.fenixgrafica.com/empresa'),
                pubDate=hoje
            )
        )
        items.append(
            PyRSS2Gen.RSSItem(
                title='''Fênix Artes Gráficas - Convites, impressos e impressão 
                         digital em Canoas/RS - Serviços.''',
                description='''Nossos Serviços: Fotolito, CTP, 
                               Impressão Digital.''',
                author='Gráfica Fênix em Canoas-RS.',
                guid=PyRSS2Gen.Guid('http://www.fenixgrafica.com/servicos'),
                pubDate=hoje
            )
        )
        items.append(
            PyRSS2Gen.RSSItem(
                title='''Fênix Artes Gráficas - Convites, impressos e impressão 
                         digital em Canoas/RS - Portifólio.''',
                description='''Convites, impressos digitais, convites, 
                               cartões de visita, agenda, livros, sacolas, 
                               revistas, folders, panfletos, embalagens, 
                               calendários de mesa, caderno executivo, 
                               risque e rabisque, matériais de escritório, 
                               folhas A4, folhas A3''',
                author='Gráfica Fênix em Canoas-RS.',
                guid=PyRSS2Gen.Guid('http://www.fenixgrafica.com/portifolio'),
                pubDate=hoje
            )
        )
        items.append(
            PyRSS2Gen.RSSItem(
                title='''Fênix Artes Gráficas - Convites, impressos e impressão 
                         digital em Canoas/RS - Orçamento.''',
                description='''Faça seu orçamento gratuíto conosco.''',
                author='Gráfica Fênix em Canoas-RS.',
                guid=PyRSS2Gen.Guid('http://www.fenixgrafica.com/portifolio'),
                pubDate=hoje
            )
        )
        items.append(
            PyRSS2Gen.RSSItem(
                title='''Fênix Artes Gráficas - Convites, impressos e impressão 
                         digital em Canoas/RS - Localização.''',
                description='''Nosso Endereço.''',
                author='Gráfica Fênix em Canoas-RS.',
                guid=PyRSS2Gen.Guid('http://www.fenixgrafica.com/localizacao'),
                pubDate=hoje
            )
        )
        items.append(
            PyRSS2Gen.RSSItem(
                title='''Fênix Artes Gráficas - Convites, impressos e impressão 
                         digital em Canoas/RS - Contato.''',
                description='''Entre em contato conosco.''',
                author='Gráfica Fênix em Canoas-RS.',
                guid=PyRSS2Gen.Guid('http://www.fenixgrafica.com/portifolio'),
                pubDate=hoje
            )
        )
        rss = PyRSS2Gen.RSS2(title='''RSS das notícias da Gráfica Fênix.''',
                           link='http://www.fenixgrafica.com/rss',
                           description='''Ultimas notícias da Gráfica Fênix.''',
                           lastBuildDate=hoje,
                           items=items)

        web.header('Content-Type', 'application/rss+xml; charset=utf-8')
        return rss.to_xml()

app = web.application(urls, globals())


def main():
    pass
