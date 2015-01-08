    # -*- coding: utf-8 -*-
import web
import render_website as render
from utils import break_string


urls = (
  '', 'Index',
  '/', 'Index',
  '/index', 'Index',
  '/empresa-filosofia', 'EmpresaFilosofia',
  '/empresa-historia', 'EmpresaHistoria',
  '/nossa-equipe', 'NossaEquipe',
  '/nossas-instalacoes', 'NossasInstalacoes',
  '/horarios-de-funcionamento', 'NossosHorarios',
  '/depoimentos', 'Depoimentos',
  '/matriculas', 'Matriculas',
  '/material-escolar', 'MaterialEscolar',
  '/convenios', 'Convenios',
  '/cardapio', 'Cardapio',
  '/nossas-refeicoes', 'NossasRefeicoes',
  '/avisos-importantes', 'AvisosImportantes',
  '/eventos', 'Eventos',
  '/dicas', 'Dicas',
  '/galerias-fotos', 'GaleriasFoto',
  '/evento_17_jan_2012', 'Evento17012012',
  '/evento_13_fev_2012', 'Evento13022012',
  '/evento_pascoa_mar_2012', 'EventoPascoa2012',
  '/evento_tio_rogerio_mar_2012', 'EventoTio2012',
  '/evento_dia-a_dia_mar_2012', 'EventoDia2012',
  '/evento_dia-a_dia_maio_2012', 'EventoMaioDia2012',
  '/evento_dia-das-maes_2012', 'EventoDiaDasMaes2012',
  '/dia-das-maes-2014', 'DiaDasMaes2014',
  '/semana-farroupilha-2012', 'SemanaFarroupilha2012',
  '/aniversario-luiz-henrique', 'AniversarioLuizHenrique',
  '/noite-pijama-2012', 'NoitePijama2012',
  '/passeio-zoologico-2012', 'PasseioZoologico2012',
  '/obras-2012-2013', 'Obras_2012_2013',
  '/aniversario-13-anos', 'Aniversario_13_Anos',
  '/carnaval-2013', 'Carnaval2013',
  '/marco-2013', 'Marco2013',
  '/diversas-2013', 'Diversas2013',
  '/bambino-2013', 'Bambino2013',
  '/bambino-2013-02', 'Bambino201302',
  '/bambino-2013-03', 'Bambino201303',
  '/dia-das-maes-2013', 'DiaDasMaes2013',
  '/visita-patati-patata', 'VisitaPatatiPatata',
  '/dia-dos-pais-2013-jardim-a', 'DiaDosPais2013JardimA',
  '/dia-dos-pais-2013-jardim-b', 'DiaDosPais2013JardimB',
  '/dia-dos-pais-2013-maternal-2', 'DiaDosPais2013Maternal2',
  '/dia-dos-pais-2013-maternal-1', 'DiaDosPais2013Maternal1',
  '/semana-farroupilha-2013', 'SemanaFarroupilha2013',
  '/semana-crianca-2013', 'SemanaCrianca2013',
  '/passeio-museu-2013', 'PasseioMuseu2013',
  '/fotos-diversas-janeiro-2014', 'FotosDiversasJaneiro2014',
  '/fotos-diversas-fevereiro-2014', 'FotosDiversasFevereiro2014',
  '/fotos-carnaval-2014', 'FotosCarnaval2014',
  '/fotos-ballet-marco-2014', 'FotosBalletMarco2014',
  '/fotos-diversas-maio-2014', 'FotosDiversasMaio2014',
  '/aula-culinaria-maio-2014', 'AulaCulinariaMaio2014',
  '/fotos-diversas-maio-2014-2', 'FotosDiversasMaio20142',
  '/festa-junina-2014', 'FestaJunina2014',
  '/fotos-diversas-junho-2014', 'FotosDiversasJunho2014',

  '/construindo-com-sucata', 'ConstruindoComSucata',
  '/educacao-fisica-prof-nilton', 'EducacaoFisicaProfNilton',
  '/nosso-dia-a-dia', 'NossoDiaADia',
  '/nossos-pequenos-bambinos', 'NossosPequenosBambinos',

  '/que-visitinha-gostosa-da-mamae', 'VisitinhaGostosaMamae',
  '/teatro-na-escola', 'TeatroNaEscola',
  '/piquenique-gostoso', 'PiqueniqueGostoso',
  '/parabens-theo', 'ParabensTheo',

  '/galerias-videos', 'GaleriasVideo',
  '/proposta-pedagogica', 'PropostaPedagogica',
  '/bercario', 'Bercario',
  '/pre-maternal', 'PreMaternal',
  '/maternal-1', 'Maternal1',
  '/maternal-2', 'Maternal2',
  '/jardim-a', 'JardimA',
  '/jardim-b', 'JardimB',
  '/atividades-extras', 'AtividadesExtras',
  '/fale-conosco', 'FaleConosco',
  '/localizacao', 'Localizacao',
  '/download-musicas', 'DownloadMusicas',
  '/download-videos', 'DownloadVideos',
  '/download-papeis-de-parede', 'DownloadPapeis',
  '/download-desenhos', 'DownloadDesenhos',
  '/empresa', 'Empresa',
  '/locacao', 'Locacao',
  '/detalhar-imovel-locacao/(.+)', 'DetalharImovelLocacao',
  '/vendas', 'Venda',
  '/detalhar-imovel-venda/(.+)', 'DetalharImovelVenda',
  '/servicos', 'Servico',
  '/assessoria-juridica', 'Assessoria',
  '/contato', 'Contato',
  '/agradecimento', 'Agradecimento',
  '/necessidade', 'Necessidade',
  '/rss', 'RSS'
)


class Index:
    def GET(self):
        return render.layout('menu_home', render.index())


# class Empresa:
#     def GET(self):
#         return render.layout('menu_empresa', render.pagina('empresa'))


class EmpresaFilosofia:
    def GET(self):
        return render.layout('menu_empresa', render.empresa_filosofia())


class EmpresaHistoria:
    def GET(self):
        return render.layout('menu_empresa', render.empresa_historia())


class NossaEquipe:
    def GET(self):
        return render.layout('menu_empresa', render.nossa_equipe())


class NossasInstalacoes:
    def GET(self):
        return render.layout('menu_empresa', render.nossas_instalacoes())


class NossosHorarios:
    def GET(self):
        return render.layout('menu_empresa', render.nossos_horarios())


class Depoimentos:
    def GET(self):
        return render.layout('menu_empresa', render.depoimentos())


class Matriculas:
    def GET(self):
        return render.layout('menu_secretaria', render.matriculas())


class MaterialEscolar:
    def GET(self):
        return render.layout('menu_secretaria', render.material_escolar())


class Convenios:
    def GET(self):
        return render.layout('menu_secretaria', render.convenios())


class Cardapio:
    def GET(self):
        return render.layout('menu_mural', render.cardapio())


class NossasRefeicoes:
    def GET(self):
        return render.layout('menu_mural', render.nossas_refeicoes())


class AvisosImportantes:
    def GET(self):
        return render.layout('menu_mural', render.avisos_importantes())


class Eventos:
    def GET(self):
        return render.layout('menu_mural', render.eventos())


class Dicas:
    def GET(self):
        return render.layout('menu_mural', render.dicas())


class GaleriasFoto:
    def GET(self):
        return render.layout('menu_galerias', render.galerias_foto())


class Evento17012012:
    def GET(self):
        return render.layout('menu_galerias', render.evento_17_jan_2012())


class Evento13022012:
    def GET(self):
        return render.layout('menu_galerias', render.evento_13_fev_2012())


class EventoPascoa2012:
    def GET(self):
        return render.layout('menu_galerias', render.evento_pascoa_2012())


class EventoTio2012:
    def GET(self):
        return render.layout('menu_galerias', render.evento_tio_2012())


class EventoDia2012:
    def GET(self):
        return render.layout('menu_galerias', render.evento_dia_2012())


class EventoMaioDia2012:
    def GET(self):
        return render.layout('menu_galerias', render.evento_maio_dia_2012())


class EventoDiaDasMaes2012:
    def GET(self):
        return render.layout('menu_galerias',
                              render.evento_dia_das_maes_2012())

class DiaDasMaes2014:
    def GET(self):
        return render.layout('menu_galerias',
                              render.dia_das_maes_2014())


class SemanaFarroupilha2012:
    def GET(self):
        return render.layout('menu_galerias', render.semana_farroupilha_2012())


class AniversarioLuizHenrique:
    def GET(self):
        return render.layout('menu_galerias',
                              render.aniversario_luiz_henrique())


class NoitePijama2012:
    def GET(self):
        return render.layout('menu_galerias',
                              render.noite_pijama_2012())


class PasseioZoologico2012:
    def GET(self):
        return render.layout('menu_galerias', render.passeio_zoologico_2012())


class Obras_2012_2013:
    def GET(self):
        return render.layout('menu_galerias', render.obras_2012_2013())


class Aniversario_13_Anos:
    def GET(self):
        return render.layout('menu_galerias', render.aniversario_13_anos())


class Carnaval2013:
    def GET(self):
        return render.layout('menu_galerias', render.carnaval_2013())


class Marco2013:
    def GET(self):
        return render.layout('menu_galerias', render.marco_2013())


class Diversas2013:
    def GET(self):
        return render.layout('menu_galerias', render.diversas_2013())


class Bambino2013:
    def GET(self):
        return render.layout('menu_galerias', render.bambino_2013())


class Bambino201302:
    def GET(self):
        return render.layout('menu_galerias', render.bambino_201302())


class Bambino201303:
    def GET(self):
        return render.layout('menu_galerias', render.bambino_201303())


class DiaDasMaes2013:
    def GET(self):
        return render.layout('menu_galerias', render.dia_das_maes_2013())


class VisitaPatatiPatata:
    def GET(self):
        return render.layout('menu_galerias', render.visita_patati_patata())


class DiaDosPais2013JardimA:
    def GET(self):
        return render.layout('menu_galerias',
                             render.dia_dos_pais_2013_jardim_a())


class DiaDosPais2013JardimB:
    def GET(self):
        return render.layout('menu_galerias',
                             render.dia_dos_pais_2013_jardim_b())


class DiaDosPais2013Maternal2:
    def GET(self):
        return render.layout('menu_galerias',
                             render.dia_dos_pais_2013_maternal_2())


class DiaDosPais2013Maternal1:
    def GET(self):
        return render.layout('menu_galerias',
                             render.dia_dos_pais_2013_maternal_1())


class SemanaFarroupilha2013:
    def GET(self):
        return render.layout('menu_galerias', render.semana_farroupilha_2013())


class SemanaCrianca2013:
    def GET(self):
        return render.layout('menu_galerias', render.semana_crianca_2013())


class PasseioMuseu2013:
    def GET(self):
        return render.layout('menu_galerias', render.passeio_museu_2013())


class FotosDiversasJaneiro2014:
    def GET(self):
        return render.layout('menu_galerias', render.fotos_diversas_janeiro_2014())


class FotosDiversasFevereiro2014:
    def GET(self):
        return render.layout('menu_galerias', render.fotos_diversas_fevereiro_2014())


class FotosDiversasMaio2014:
    def GET(self):
        return render.layout('menu_galerias', render.fotos_diversas_maio_2014())


class FotosDiversasMaio20142:
    def GET(self):
        return render.layout('menu_galerias', render.fotos_diversas_maio_2014_2())


class FotosDiversasJunho2014:
    def GET(self):
        return render.layout('menu_galerias', render.fotos_diversas_junho_2014())


class FestaJunina2014:
    def GET(self):
        return render.layout('menu_galerias', render.festa_junina_2014())


class AulaCulinariaMaio2014:
    def GET(self):
        return render.layout('menu_galerias', render.aula_culinaria_maio_2014())


class FotosCarnaval2014:
    def GET(self):
        return render.layout('menu_galerias', render.fotos_carnaval_2014())


class FotosBalletMarco2014:
    def GET(self):
        return render.layout('menu_galerias', render.fotos_ballet_marco_2014())


class VisitinhaGostosaMamae:
    def GET(self):
        return render.layout('menu_galerias', render.visitinha_gostosa_mamae())


class ConstruindoComSucata:
    def GET(self):
        return render.layout('menu_galerias', render.construindo_com_sucata())


class EducacaoFisicaProfNilton:
    def GET(self):
        return render.layout('menu_galerias',
               render.educacao_fisica_prof_nilton())


class NossoDiaADia:
    def GET(self):
        return render.layout('menu_galerias', render.nosso_dia_a_dia())


class NossosPequenosBambinos:
    def GET(self):
        return render.layout('menu_galerias',
                             render.nossos_pequenos_bambinos())


class TeatroNaEscola:
    def GET(self):
        return render.layout('menu_galerias', render.teatro_na_escola())


class PiqueniqueGostoso:
    def GET(self):
        return render.layout('menu_galerias', render.piquenique_gostoso())


class ParabensTheo:
    def GET(self):
        return render.layout('menu_galerias', render.parabens_theo())


class GaleriasVideo:
    def GET(self):
        return render.layout('menu_galerias', render.galerias_video())


class PropostaPedagogica:
    def GET(self):
        return render.layout('menu_servicos', render.proposta_pedagogica())


class Bercario:
    def GET(self):
        return render.layout('menu_servicos', render.bercario())


class PreMaternal:
    def GET(self):
        return render.layout('menu_servicos', render.prematernal())


class Maternal1:
    def GET(self):
        return render.layout('menu_servicos', render.maternal1())


class Maternal2:
    def GET(self):
        return render.layout('menu_servicos', render.maternal2())


class JardimA:
    def GET(self):
        return render.layout('menu_servicos', render.jardima())


class JardimB:
    def GET(self):
        return render.layout('menu_servicos', render.jardimb())


class AtividadesExtras:
    def GET(self):
        return render.layout('menu_servicos', render.atividades_extras())


class FaleConosco:
    def GET(self):
        return render.layout('menu_contato', render.fale_conosco())

    def POST(self):
      try:
        i = web.input()
        assunto='Contato realizado pelo site www.bambinocampos.com.br'
        nome='O visitante ' + break_string(i.nome)
        telefone=' com o telefone: ' + break_string(i.telefone)
        email=' com o E-mail: ' + break_string(i.email)
        mensagem='Deixou a seguinte mensagem: ' + '\n\t' + break_string(i.mensagem)
        mensagem_completa = nome + telefone + email + mensagem
        to_email = 'bambinocampones@bol.com.br'
        web.sendmail(email, to_email, '%s' % assunto, '%s' % mensagem_completa)
        raise web.seeother('/agradecimento')
      except Exception:
        raise


class Agradecimento:
    def GET(self):
        return render.layout('menu_contato', render.agradecimento())


class Localizacao:
    def GET(self):
        return render.layout('menu_contato', render.localizacao())


class DownloadMusicas:
    def GET(self):
        return render.layout('menu_download', render.download_musicas())


class DownloadVideos:
    def GET(self):
        return render.layout('menu_download', render.download_videos())


class DownloadPapeis:
    def GET(self):
        return render.layout('menu_download', render.download_papeis())


class DownloadDesenhos:
    def GET(self):
        return render.layout('menu_download', render.download_desenhos())


app = web.application(urls, globals())


def main():
    pass
