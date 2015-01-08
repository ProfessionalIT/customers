#!/usr/bin/python
# -*- coding: utf-8 -*-
from web import template
#from model import get_pagina, get_imoveis_venda_destaque,
#get_imoveis_locacao_destaque, get_imoveis_lista,
#entity_by_slug, get_fotos_imovel, Imovel
import os
rootpath = os.path.abspath(os.path.dirname(__file__))

site_layout_path = template.render(rootpath + '/templates/site', cache=False)


def layout(active_menu, content):
    #render_vars = {'active_menu': active_menu}
    render_vars = {'active_menu': ''}
    return site_layout_path.layout(render_vars, content)


def index():
    #vendas_destaque=get_imoveis_venda_destaque()
    #locacoes_destaque=get_imoveis_locacao_destaque()
    #return site_layout_path.index(vendas_destaque=vendas_destaque,
    #locacoes_destaque=locacoes_destaque)
    return site_layout_path.index()


def fotos_diversas_junho_2014():
    return site_layout_path.fotos_diversas_junho_2014()


def festa_junina_2014():
    return site_layout_path.festa_junina_2014()


def fotos_diversas_maio_2014_2():
    return site_layout_path.fotos_diversas_maio_2014_2()


def aula_culinaria_maio_2014():
    return site_layout_path.aula_culinaria_maio_2014()


def empresa_filosofia():
    return site_layout_path.empresa_filosofia()


def empresa_historia():
    return site_layout_path.empresa_historia()


def nossa_equipe():
    return site_layout_path.nossa_equipe()


def nossas_instalacoes():
    return site_layout_path.nossas_instalacoes()


def nossos_horarios():
    return site_layout_path.nossos_horarios()


def depoimentos():
    return site_layout_path.depoimentos()


def matriculas():
    return site_layout_path.matriculas()


def material_escolar():
    return site_layout_path.material_escolar()


def convenios():
    return site_layout_path.convenios()


def cardapio():
    return site_layout_path.cardapio()


def nossas_refeicoes():
    return site_layout_path.nossas_refeicoes_2012()


def avisos_importantes():
    return site_layout_path.avisos_importantes()


def eventos():
    return site_layout_path.eventos()


def dicas():
    return site_layout_path.dicas()


def galerias_foto():
    return site_layout_path.galerias_foto()


def evento_17_jan_2012():
    return site_layout_path.evento_17_jan_2012()


def evento_13_fev_2012():
    return site_layout_path.evento_13_fev_2012()


def evento_pascoa_2012():
    return site_layout_path.evento_pascoa_2012()


def evento_tio_2012():
    return site_layout_path.evento_tio_2012()


def evento_dia_2012():
    return site_layout_path.evento_dia_2012()


def evento_maio_dia_2012():
    return site_layout_path.evento_maio_dia_2012()


def dia_das_maes_2014():
    return site_layout_path.dia_das_maes_2014()


def evento_dia_das_maes_2012():
    return site_layout_path.evento_dia_das_maes_2012()


def semana_farroupilha_2012():
    return site_layout_path.semana_farroupilha_2012()


def semana_farroupilha_2013():
    return site_layout_path.semana_farroupilha_2013()


def semana_crianca_2013():
    return site_layout_path.semana_crianca_2013()


def aniversario_luiz_henrique():
    return site_layout_path.aniversario_luiz_henrique()


def noite_pijama_2012():
    return site_layout_path.noite_pijama_2012()


def passeio_zoologico_2012():
    return site_layout_path.passeio_zoologico_2012()


def passeio_museu_2013():
    return site_layout_path.passeio_museu_2013()


def fotos_diversas_janeiro_2014():
    return site_layout_path.fotos_diversas_janeiro_2014()


def fotos_diversas_fevereiro_2014():
    return site_layout_path.fotos_diversas_fevereiro_2014()


def fotos_diversas_maio_2014():
    return site_layout_path.fotos_diversas_maio_2014()

def fotos_carnaval_2014():
    return site_layout_path.fotos_carnaval_2014()


def fotos_ballet_marco_2014():
    return site_layout_path.fotos_ballet_marco_2014()


def obras_2012_2013():
    return site_layout_path.obras_2012_2013()


def aniversario_13_anos():
    return site_layout_path.aniversario_13_anos()


def carnaval_2013():
    return site_layout_path.carnaval_2013()


def marco_2013():
    return site_layout_path.marco_2013()


def diversas_2013():
    return site_layout_path.diversas_2013()


def bambino_2013():
    return site_layout_path.bambino_2013()


def bambino_201302():
    return site_layout_path.bambino_201302()


def bambino_201303():
    return site_layout_path.bambino_201303()


def dia_das_maes_2013():
    return site_layout_path.dia_das_maes_2013()


def visita_patati_patata():
    return site_layout_path.visita_patati_patata()


def dia_dos_pais_2013_jardim_a():
    return site_layout_path.dia_dos_pais_2013_jardim_a()


def dia_dos_pais_2013_jardim_b():
    return site_layout_path.dia_dos_pais_2013_jardim_b()


def dia_dos_pais_2013_maternal_2():
    return site_layout_path.dia_dos_pais_2013_maternal_2()


def dia_dos_pais_2013_maternal_1():
    return site_layout_path.dia_dos_pais_2013_maternal_1()


def visitinha_gostosa_mamae():
    return site_layout_path.visitinha_gostosa_mamae()


def construindo_com_sucata():
    return site_layout_path.construindo_com_sucata()


def educacao_fisica_prof_nilton():
    return site_layout_path.educacao_fisica_prof_nilton()


def nosso_dia_a_dia():
    return site_layout_path.nosso_dia_a_dia()


def nossos_pequenos_bambinos():
    return site_layout_path.nossos_pequenos_bambinos()


def teatro_na_escola():
    return site_layout_path.teatro_na_escola()


def piquenique_gostoso():
    return site_layout_path.piquenique_gostoso()


def parabens_theo():
    return site_layout_path.parabens_theo()


def galerias_video():
    return site_layout_path.galerias_video()


def proposta_pedagogica():
    return site_layout_path.proposta_pedagogica()


def bercario():
    return site_layout_path.bercario()


def prematernal():
    return site_layout_path.prematernal()


def maternal1():
    return site_layout_path.maternal1()


def maternal2():
    return site_layout_path.maternal2()


def jardima():
    return site_layout_path.jardima()


def jardimb():
    return site_layout_path.jardimb()


def atividades_extras():
    return site_layout_path.atividades_extras()


def fale_conosco():
    return site_layout_path.fale_conosco()


def localizacao():
    return site_layout_path.localizacao()


def download_musicas():
    music_path = os.path.abspath(rootpath + '/static/musicas')
    albuns_folder = os.listdir(music_path)
    folders = []
    for folder in albuns_folder:
        arquivos_folder = [f for f in
            os.listdir(rootpath + '/static/musicas/' + folder)
            if f.endswith('.mp3')]
        arquivos_folder.sort()
        inner_folder = {'folder': folder, 'arquivos_folder': arquivos_folder}
        folders.append(inner_folder)
    return site_layout_path.download_musicas(folders)


def download_videos():
    return site_layout_path.download_videos()


def download_papeis():
    return site_layout_path.download_papeis()


def download_desenhos():
    return site_layout_path.download_desenhos()


def agradecimento():
    return site_layout_path.obrigado_contato()

