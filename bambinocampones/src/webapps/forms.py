#!/usr/bin/python
# -*- coding: utf-8 -*-
from web import form
import model

# Commons Validators Expressions
vemail = form.regexp("^([0-9a-zA-Z]+([_.-]?[0-9a-zA-Z]+)*" \
                     "@[0-9a-zA-Z]+[0-9,a-z,A-Z,.,-]*(.){1}[a-zA-Z]{2,4})+$",
                      "Precisa ser um endereco de e-mail válido !.")
vdigito = form.regexp("\d+", "Precisa ser um digito")
vmoeda = form.regexp("^\d{1,5}(\.\d{1,2})?$",
                  "Precisa ser um valor inteiro OU com duas casas decimais !")
"""
vdata =  form.regexp("^(((0[1-9]|[12][0-9]|3[01])([/])(0[13578]|10|12)([/])
(\d{4}))|(([0][1-9]|[12][0-9]|30)([/])(0[469]|11)([/])
(\d{4}))|((0[1-9]|1[0-9]|2[0-8])([/])(02)([/])(\d{4}))|
((29)(\.|-|\/)(02)([/])([02468][048]00))|((29)([/])(02)([/])
([13579][26]00))|((29)([/])(02)([/])([0-9][0-9][0][48]))|
((29)([/])(02)([/])([0-9][0-9][2468][048]))|((29)([/])(02)([/])([0-9][0-9]
[13579][26])))$","Precisa ser uma data no formato dd/mm/yyyy !")
vdatafull =  form.regexp("^\d{4}-([\d]|0[0-9]|1[0,1,2])-" \
                         "([0-9]|[0,1,2][0-9]|3[0,1]) ([0-1][0-9]|[2][0-3])"
                         "(:([0-5][0-9])){1,2}(:([0-5][0-9])){1,2}$",
                         "Precisa ser uma data e hora no formato yyyy-mm-dd
                         hh:mm:ss !")
"""
vurl = form.regexp("""^(http[s]?://|ftp://)?(www\.)?[a-zA-Z0-9-\.]+\.
                       (com|org|net|mil|edu|ca|co.uk|com.au|gov|br)$""",
                       "Precisa ser um endereço Web Válido !.")
vtelefone = form.regexp("^\(?\d{2}\)?[\s-]?\d{4}-?\d{4}$",
                        "Precisa ser um telefone no formato (99) 9999-9999")
vcep = form.regexp("^[0-9]{2}\.[0-9]{3}-[0-9]{3}$",
                   "Precisa estar no formato 99.999-999 !")
vcnpj = form.regexp("\d{2,3}.\d{3}.\d{3}/\d{4}-\d{2}",
                    "Precisa estar no formato 99.999.999/9999-99 !")

# App Forms


def getSearchForm(fields):
    _form = form.Form(
            form.Dropdown('campo',
                          fields,
                          description='Campo:',
                          onblur='clean_search(this.value, valor);',
                          onclick='clean_search(this.value, valor);'),
            form.Dropdown('criterio',
                          [('=', '='),
                           ('!=', '!='),
                           (' LIKE ', ' LIKE ')],
                          description='Critério:'),
            form.Textbox('valor',
                         size=20,
                         description="Valor:"),
            form.Button('Pesquisa',
                        html="Pesquisar",
                        type="submit"),
            form.Dropdown('resultados',
                          [('10', '10'),
                           ('50', '50'),
                           ('100', '100')],
                          onchange='form.submit()',
                          description='Qtde Registros:'),
    )
    return _form


def getUsuarioForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('login',
                     vemail,
                     size="60",
                     maxlenght="250",
                     title="E-mail de Login do Usuario.",
                     description='Login:'),
        form.Password('senha',
                      form.notnull,
                      size="60",
                      maxlenght="08",
                      title="Senha com 08 digitos.",
                      description='Senha:'),
        form.Dropdown('nivel_acesso',
                      [('1', 'Administrador'),
                       ('2', 'Operador'),
                       ('3', 'Visitante')],
                      title="Nivel de Acesso do Usuario",
                      description='Nível de Acesso:')
    )
    return _form


def getPaginaForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('titulo',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Titulo/Nome da Página.",
                     description='Titulo:'),
        form.Textbox('descricao_completa',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Descrição Completa da Página.",
                     description='Descrição Completa:'),
        form.Textbox('palavras_chaves',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Palavras Chaves da Página separadas por vírgula.",
                     description='Palavras Chaves:'),
        form.Textbox('slug',
                     size="60",
                     maxlenght="250",
                     title="URL da Página.",
                     readonly="readonly",
                     class_="readonly",
                     description='URL da Página'),
        form.Textarea('conteudo',
                      form.notnull,
                      cols="70",
                      rows="25",
                      title="Conteúdo da Página.",
                      description='Conteúdo da Página:')
    )
    return _form


def getMenuForm():
    menu_list = model.select(getattr(model, 'Menu'))
    menu_options = [(str(row.id), row.titulo) for row in menu_list]
    pagina_list = model.select(getattr(model, 'Pagina'))
    pagina_options = [(str(row.id), row.titulo) for row in pagina_list]
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('ordem',
                     vdigito,
                     size="10",
                     maxlenght="50",
                     title="""Ordem de Exibição do Menu na Página. Deve seguir
                              a sequência para que o menu funcione.""",
                    description='Ordem de Exibição:'),
        form.Textbox('titulo',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Titulo/Nome da Página.",
                     description='Titulo:'),
        form.Textbox('descricao',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Descrição do Menu.",
                     description='Descrição:'),
        form.Textbox('key_words',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Palavras Chave da Página.",
                     description='Palavras Chave:'),
        form.Dropdown('pagina',
                      pagina_options,
                      title="Página que deve ser exibida ao clicar no menu.",
                      description='Página: '),
        form.Textbox('endereco',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Endereço do link.",
                     description='Endereço do Link:'),
        form.Dropdown('menu_pai', menu_options,
                      title="Menu Pai/Superior do Menu.",
                      description='Menu Superior: '),
        form.Dropdown('nivel',
                      [('0', '0'),
                       ('1', '1'),
                       ('2', '2')],
                      title="""Nível do Menu: 0 - MenuBar,
                                              1-Menu Principal,
                                              2-Menu Interno.""",
                      description='Nível: ')
    )
    return _form


def getProprietarioForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('nome',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Nome.",
                     description='Nome:')
    )
    return _form


def getAgenciadorForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('nome',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Nome.",
                     description='Nome:')
    )
    return _form


def getCorretorForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('nome',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Nome.",
                     description='Nome:')
    )
    return _form


def getOrigemImovelForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('nome',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Nome.",
                     description='Nome:')
    )
    return _form


def getTipoImovelForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('nome',
                     form.notnull,
                     size="75",
                     maxlenght="250",
                     title="Nome do Tipo de Imovel.",
                     description='Nome:')
    )
    return _form


def getImovelForm():
    proprietario_list = model.select(getattr(model, 'Proprietario'))
    proprietario_options = [(str(row.id), row.nome) for row in \
                            proprietario_list]
    agenciador_list = model.select(getattr(model, 'Agenciador'))
    agenciador_options = [(str(row.id), row.nome) for row in agenciador_list]
    corretor_list = model.select(getattr(model, 'Corretor'))
    corretor_options = [(str(row.id), row.nome) for row in corretor_list]
    origem_imovel_list = model.select(getattr(model, 'OrigemImovel'))
    origem_imovel_options = [(str(row.id), row.nome) for row in \
                             origem_imovel_list]
    tipo_imovel_list = model.select(getattr(model, 'TipoImovel'))
    tipo_imovel_options = [(str(row.id), row.nome) for row in tipo_imovel_list]
    uf_options = [('AC', 'AC'),
                  ('AL', 'AL'),
                  ('AM', 'AM'),
                  ('AP', 'AP'),
                  ('BA', 'BA'),
                  ('CE', 'CE'),
                  ('DF', 'DF'),
                  ('ES', 'ES'),
                  ('GO', 'GO'),
                  ('MA', 'MA'),
                  ('MG', 'MG'),
                  ('MS', 'MS'),
                  ('MT', 'MT'),
                  ('PA', 'PA'),
                  ('PB', 'PB'),
                  ('PE', 'PE'),
                  ('PI', 'PI'),
                  ('PR', 'PR'),
                  ('RJ', 'RJ'),
                  ('RN', 'RN'),
                  ('RO', 'RO'),
                  ('RR', 'RR'),
                  ('RS', 'RS'),
                  ('SC', 'SC'),
                  ('SE', 'SE'),
                  ('SP', 'SP'),
                  ('TO', 'TO')]
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('data_inclusao',
                     size="15",
                     maxlenght="20",
                     class_="datetime",
                     title="Data e Hora da Inclusão do Imóvel.",
                     readonly="readonly",
                     description='Data e Hora: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('slug',
                     size="60",
                     maxlenght="250",
                     title="URL da Página.",
                     readonly="readonly",
                     class_="readonly",
                     description='URL do Imóvel'),
        form.Textbox('codigo',
                     form.notnull,
                     size="15",
                     maxlenght="10",
                     title="Código do Imóvel.",
                     description='Código:'),
        form.Dropdown('proprietario',
                      proprietario_options,
                      title="Proprietário do Imóvel.",
                      description='Proprietário: '),
        form.Dropdown('agenciador',
                      agenciador_options,
                      title="Agenciador do Imóvel.",
                      description='Agenciador: '),
        form.Dropdown('corretor',
                      corretor_options,
                      title="Corretor do Imóvel.",
                      description='Corretor: '),
        form.Dropdown('origem_imovel',
                      origem_imovel_options,
                      title="Origem do Imóvel.",
                      description='Origem: '),
        form.Dropdown('finalidade_venda',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Imóvel para Venda ?",
                      description='Venda:'),
        form.Dropdown('finalidade_locacao',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Imóvel para Locação ?",
                      description='Locação:'),
        form.Dropdown('utilidade_comercial',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tipo Comercial ?",
                      description='Comercial:'),
        form.Dropdown('utilidade_residencial',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tipo Residencial ?",
                      description='Residencial:'),
        form.Dropdown('destaque',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Destaque ?",
                      description='Destaque:'),
        form.Dropdown('disponivel',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Disponível ?",
                      description='Disponível:'),
        form.Dropdown('tipo_imovel',
                      tipo_imovel_options,
                      title="Tipo do Imóvel.",
                      description='Tipo: '),
        form.Textbox('quantidade_dormitorios',
                     form.notnull,
                     size="15",
                     maxlenght="10",
                     title="Quantidade de dormitórios.",
                     description='Nº Dormitórios:'),
        form.Textbox('dormitorio_detalhes',
                     size="75",
                     maxlenght="250",
                     title="""Detalhamento da quantidade de
                              dormitórios do Imóvel.""",
                    description='Detalhes Nº Dormitórios:'),
        form.Textbox('quantidade_banheiros',
                     form.notnull,
                     size="15",
                     maxlenght="10",
                     title="Quantidade de banheiros.",
                     description='Nº Banheiros:'),
        form.Textbox('banheiro_detalhes',
                     size="75",
                     maxlenght="250",
                     title="""Detalhamento da quantidade de
                              banheiros do Imóvel.""",
                     description='Detalhes Nº Banheiros:'),
        form.Textbox('quantidade_suites',
                     form.notnull,
                     size="15",
                     maxlenght="10",
                     title="Quantidade de Suítes.",
                     description='Nº Suítes:'),
        form.Textbox('suite_detalhes',
                     size="75",
                     maxlenght="250",
                     title="Detalhamento da quantidade de suítes do Imóvel.",
                     description='Detalhes Nº Suíte:'),
        form.Textbox('quantidade_garagens',
                     form.notnull,
                     size="15",
                     maxlenght="10",
                     title="Quantidade de Garagens.",
                     description='Nº Garagens:'),
        form.Textbox('garagem_detalhes',
                     size="75",
                     maxlenght="250",
                     title="Detalhamento da quantidade de garagens do Imóvel.",
                     description='Detalhes Nº Garagens:'),
        form.Dropdown('dependencia_empregada',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tem Dependência de Empregada ?",
                      description='Dependência de Empregada:'),
        form.Dropdown('patio',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tem pátio ?",
                      description='Pátio:'),
        form.Dropdown('churrasqueira',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tem churrasqueira ?",
                      description='Churrasqueria:'),
        form.Dropdown('sacada',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tem sacada ?",
                      description='Sacada:'),
        form.Textbox('area_privativa',
                     size="15",
                     maxlenght="20",
                     title="Área Privativa.",
                     description='Área Privativa:'),
        form.Textbox('area_privativa_detalhes',
                     size="75",
                     maxlenght="250",
                     title="Detalhamento da Área Privativa do Imóvel.",
                     description='Detalhes Área Privativa:'),
        form.Textbox('terreno_largura',
                     size="15",
                     maxlenght="20",
                     title="Terreno Largura.",
                     description='Terreno Largura:'),
        form.Textbox('terreno_comprimento',
                     size="15",
                     maxlenght="20",
                     title="Terreno Comprimento.",
                     description='Terreno Comprimento:'),
        form.Dropdown('murado',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tem Muro ?",
                      description='Murado:'),
        form.Textbox('murado_detalhes',
                     size="75",
                     maxlenght="250",
                     title="Detalhamento do Murado do Imóvel.",
                     description='Detalhes Murado:'),
        form.Textbox('piso',
                     size="75",
                     maxlenght="250",
                     title="Informações sobre o piso.",
                     description='Piso:'),
        form.Textbox('cobertura',
                     size="75",
                     maxlenght="250",
                     title="Informações sobre a cobertura.",
                     description='Cobertura:'),
        form.Textbox('cep',
                     form.notnull,
                     size="15",
                     maxlenght="10",
                     title="CEP do Imóvel.",
                     description='CEP:'),
        form.Textbox('endereco',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Endereço do Imóvel.",
                     description='Endereço:'),
        form.Textbox('numero',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Número no Endereço do Imóvel.",
                     description='Número:'),
        form.Textbox('complemento',
                     size="60",
                     maxlenght="250",
                     title="Complemente do Endereço do Imóvel.",
                     description='Complemento:'),
        form.Textbox('bairro',
                     form.notnull,
                     size="60",
                     maxlenght="150",
                     title="Bairro do Imóvel.",
                     description='Bairro:'),
        form.Textbox('cidade',
                     form.notnull,
                     size="60",
                     maxlenght="150",
                     title="Cidade do Imóvel.",
                     description='Cidade:',
                     value='Canoas'),
        form.Dropdown('uf',
                      uf_options,
                      title="UF do Imóvel.",
                      description='UF:',
                      value='RS'),
        form.Textbox('ponto_referencia',
                     size="75",
                     maxlenght="250",
                     title="Ponto de Referência do Imóvel.",
                     description='Ponto de Referência:'),
        form.Textbox('coordenadas_mapa',
                     size="75",
                     maxlenght="250",
                     title="Coordenadas no Mapa.",
                     description='Coordenadas Mapa:'),
        form.Textbox('valor_aluguel',
                     size="20",
                     maxlenght="15",
                     title="Valor do Aluguél.",
                     description='Valor Aluguél:'),
        form.Textbox('valor_venda',
                     size="20",
                     maxlenght="15",
                     title="Valor do Imóvel para Venda.",
                     description='Valor Venda:'),
        form.Dropdown('aceita_proposta',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="O Proprietário aceita proposta ?",
                      description='Aceita Proposta:'),
        form.Dropdown('condominio',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tem condomínio ?",
                      description='Condomínio:'),
        form.Textbox('valor_condominio',
                     size="20",
                     maxlenght="15",
                     title="Valor do Condomínio.",
                     description='Valor Condomínio:'),
        form.Textbox('valor_agua',
                     size="20",
                     maxlenght="15",
                     title="Valor da Agua.",
                     description='Valor Agua:'),
        form.Dropdown('iptu',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="Tem IPTU ?",
                      description='IPTU:'),
        form.Textbox('valor_iptu',
                     size="20",
                     maxlenght="15",
                     title="Valor do IPTU.",
                     description='Valor IPTU:',
                     value='0,00'),
        form.Textarea('observacoes',
                      cols="70",
                      rows="25",
                      title="Observações do Imóvel.",
                      description='Observações:')
    )
    return _form


def getImovelRecursoForm(record_id=None):
    imovel_list = model.select(getattr(model, 'Imovel'))
    imovel_options = [(str(row.id), row.codigo) for row in imovel_list]
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Hidden('imovel',
                    value=record_id),
        form.Dropdown('tipo_recurso',
                      [('Foto', 'Foto'),
                       ('Video', 'Video')],
                      title="Recurso",
                      description='Recurso:'),
        form.Dropdown('tipo',
                      [('interno', 'Interno'),
                       ('externo', 'Externo'),
                       ('destaque', 'Destaque')],
                      title="Tipo",
                      description='Tipo:'),
        form.Textbox('url_recurso',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="URL/Endereço do Recurso.",
                     description='Endereço do Recurso:'),
        form.Textbox('url_miniatura',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="URL/Endereço da Miniatura.",
                     description='Endereço da Miniatura:'),
        form.Textbox('descricao',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Descrição do Recurso",
                     description='Descrição:')
    )
    return _form


def getContatoForm():
    _form = form.Form(
        form.Textbox('nome',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Informe o seu nome.",
                     description='Nome:'),
        form.Textbox('telefone',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Informe o seu telefone.",
                     description='Telefone:'),
        form.Textbox('email',
                     vemail,
                     size="60",
                     maxlenght="250",
                     title="Informe o seu E-mail.",
                     description='E-mail:'),
        form.Textarea('mensagem_adicional',
                      cols="70",
                      rows="15",
                      title="Inclua sua mensagem.",
                      description='Mensagem:')
    )
    return _form


def getNecessidadeForm():
    _form = form.Form(
        form.Hidden('id'),
        form.Hidden('operation'),
        form.Textbox('nome',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Informe o seu nome.",
                     description='Nome:'),
        form.Textbox('email',
                     vemail,
                     size="60",
                     maxlenght="250",
                     title="Informe o seu E-mail.",
                     description='E-mail:'),
        form.Textbox('telefone',
                     form.notnull,
                     size="60",
                     maxlenght="250",
                     title="Informe o seu telefone.",
                     description='Telefone:'),
        form.Dropdown('atendido',
                      [('S', 'Sim'),
                       ('N', 'Nao')],
                      title="A necessidade foi atendida ?",
                      description='Atendido:'),
        form.Textarea('necessidade',
                      cols="70",
                      rows="15",
                      title="Inclua sua necessidade.",
                      description='Necessidade:')
    )
    return _form
