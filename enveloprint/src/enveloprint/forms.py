#!/usr/bin/python
# -*- coding: utf-8 -*-
import gae_form as form
import model

# Commons Validators Expressions
vemail = form.regexp("^([0-9a-zA-Z]+([_.-]?[0-9a-zA-Z]+)*@[0-9a-zA-Z]+[0-9,a-z,A-Z,.,-]*(.){1}[a-zA-Z]{2,4})+$", "Precisa ser um endereco de e-mail válido !.")
vdigito = form.regexp("\d+", "Precisa ser um digito")
vmoeda = form.regexp("^\d{1,5}(\.\d{1,2})?$", "Precisa ser um valor inteiro OU com duas casas decimais !")
vdata =  form.regexp("^(((0[1-9]|[12][0-9]|3[01])([/])(0[13578]|10|12)([/])(\d{4}))|(([0][1-9]|[12][0-9]|30)([/])(0[469]|11)([/])(\d{4}))|((0[1-9]|1[0-9]|2[0-8])([/])(02)([/])(\d{4}))|((29)(\.|-|\/)(02)([/])([02468][048]00))|((29)([/])(02)([/])([13579][26]00))|((29)([/])(02)([/])([0-9][0-9][0][48]))|((29)([/])(02)([/])([0-9][0-9][2468][048]))|((29)([/])(02)([/])([0-9][0-9][13579][26])))$", "Precisa ser uma data no formato dd/mm/yyyy !")
vdatafull =  form.regexp("^\d{4}-([\d]|0[0-9]|1[0,1,2])-([0-9]|[0,1,2][0-9]|3[0,1]) ([0-1][0-9]|[2][0-3])(:([0-5][0-9])){1,2}(:([0-5][0-9])){1,2}$", "Precisa ser uma data e hora no formato yyyy-mm-dd hh:mm:ss !")
vurl = form.regexp("^(http[s]?://|ftp://)?(www\.)?[a-zA-Z0-9-\.]+\.(com|org|net|mil|edu|ca|co.uk|com.au|gov|br)$", "Precisa ser um endereço Web Válido !.")
vtelefone = form.regexp("^\(?\d{2}\)?[\s-]?\d{4}-?\d{4}$", "Precisa ser um telefone no formato (99) 9999-9999")
vcep = form.regexp("^[0-9]{2}\.[0-9]{3}-[0-9]{3}$", "Precisa estar no formato 99.999-999 !")
vcnpj = form.regexp("\d{2,3}.\d{3}.\d{3}/\d{4}-\d{2}", "Precisa estar no formato 99.999.999/9999-99 !")

# App Forms
def getSearchForm(fields):
    search_form = form.GAEForm(
            form.Dropdown('campo', fields, description='Campo:', onblur='clean_search(this.value, valor);', onclick='clean_search(this.value, valor);' ),
            form.Dropdown('criterio', [('=', '=')], description='Critério:'),
            form.Textbox('valor', size=20, description="Valor:"),
            form.Button('Pesquisa', html="Pesquisar", type="submit"),
            form.Dropdown('resultados', [('10', '10'), ('50', '50'), ('100', '100')], onchange='form.submit()',description='Qtde Registros:'),
    )
    return search_form

def getForm(param):
    if param == 'FotoSite':
        return getFotoSiteForm()
    elif param == 'Curiosidade':
        return getCuriosidadeForm()
    elif param == 'CategoriaProduto':
        return getCategoriaProdutoForm()
    elif param == 'Produto':
        return getProdutoForm()
    elif param == 'Pagina':
        return getPaginaForm()
    elif param == 'Menu':
        return getMenuForm()
    elif param == 'Contato':
        return getContatoForm()
    elif param == 'Pedido':
        return getPedidoForm()
    else:
        return None

def getFotoSiteForm():
    foto_site_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Dropdown('tipo', [('Slide-Show', 'Slide-Show'), ('Header', 'Header')], title="Tipo de Foto ?", description='Tipo de Foto:'),
        form.Textbox('nome', form.notnull, size="60", maxlenght="250", title="Nome.", description='Nome:'),
        form.Textbox('descricao', form.notnull, size="60", maxlenght="250", title="Detalhamento.", description='Texto da Foto:'),
        form.Dropdown('ativo', [('Sim', 'Sim'), ('Nao', 'Nao')], title="Foto Ativa ?", description='Foto Ativa ?:'),
        form.Textbox('imagem_url', form.notnull, size="60", maxlenght="250", title="URL Imagem.", description='Endereço Imagem (673px X 310px):'),
        form.Textbox('data_inclusao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de inclusão da foto.", readonly="readonly", description='Incluído em: (YYYY-MM-DD HH:MM:SS)')
    )
    return foto_site_form

def getCuriosidadeForm():
    curiosidade_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('nome', form.notnull, size="60", maxlenght="250", title="Nome da Curiosidade.", description='Nome:'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlenght="250", title="Palavras Chaves da Página separadas por vírgula.", description='Palavras Chaves:'),
        form.Textarea('detalhamento', form.notnull, cols="70", rows="25", title="Detalhamento da Curiosidade.", description='Detalhamento:')
    )
    return curiosidade_form

def getCategoriaProdutoForm():
    categoria_produto_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('nome', form.notnull, size="60", maxlenght="250", title="Nome da Categoria de Produto.", description='Nome:'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlenght="250", title="Palavras Chaves da Página separadas por vírgula.", description='Palavras Chaves:'),
        form.Textbox('icone', form.notnull, size="60", maxlenght="250", title="Ícone da Categoria de Produto.", description='Ícone (128px X 128px):')
    )
    return categoria_produto_form

def getProdutoForm():
    categoria_list = model.CategoriaProduto.all()
    categoria_options = [(str(row.key().id()), row.nome) for row in categoria_list]
    produto_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Dropdown('categoria', categoria_options, title="Categoria do Produto.", description='Categoria: '),
        form.Textbox('codigo', form.notnull, size="10", maxlenght="10", title="Código do Produto.", description='Código:'),
        form.Textbox('referencia', form.notnull, size="60", maxlenght="250", title="Referência do Produto.", description='Referência:'),
        form.Textbox('formato', form.notnull, size="60", maxlenght="250", title="Formato do Produto.", description='Formato:'),
        form.Textbox('gramatura', form.notnull, size="60", maxlenght="250", title="Gramatura do Produto.", description='Gramatura:'),
        form.Dropdown('tipo_embalagem', [('Caixa', 'Caixa'), ('Cento', 'Cento'), ('Pacote', 'Pacote'), ('KG/Peca', 'KG/Peca')], title="Tipo de Embalagem", description='Tipo de Embalagem:'),
        form.Textbox('unidade_embalagem', form.notnull, size="60", maxlenght="250", title="Unidades por Embalagem.", description='Unid. P/ Embalagem:'),
        form.Textbox('cor', form.notnull, size="15", maxlenght="15", class_="iColorPicker", title="Cor do Produto.", description='Cor:', value='#cccccc'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlenght="250", title="Palavras Chaves da Página separadas por vírgula.", description='Palavras Chaves:'),
        form.Dropdown('destaque', [('Sim', 'Sim'), ('Nao', 'Nao')], title="O Produto é Destaque/Lançamento ?", description='Destaque/Lançamento ?:'),
        form.Textbox('foto_produto_01', size="60", maxlenght="250", title="URL/Endereço da Foto 01 do Produto.", description='URL Foto 01 (673px X 310px):'),
        form.Textbox('foto_produto_02', size="60", maxlenght="250", title="URL/Endereço da Foto 02 do Produto.", description='URL Foto 02 (673px X 310px):'),
        form.Textbox('foto_produto_03', size="60", maxlenght="250", title="URL/Endereço da Foto 03 do Produto.", description='URL Foto 03 (673px X 310px):'),
        form.Textbox('foto_produto_04', size="60", maxlenght="250", title="URL/Endereço da Foto 04 do Produto.", description='URL Foto 04 (673px X 310px):'),
        form.Textbox('foto_produto_05', size="60", maxlenght="250", title="URL/Endereço da Foto 05 do Produto.", description='URL Foto 05 (673px X 310px):')
    )
    return produto_form

def getMenuForm():
    menu_list = model.Menu.all()
    menu_options = [(str(row.key().id()), row.nome) for row in menu_list]
    pagina_list = model.Pagina.all()
    pagina_options = [(str(row.key().id()), row.nome) for row in pagina_list]
    menu_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('ordem', vdigito, size="10", maxlenght="50", title="Ordem de Exibição do Menu na Página. Deve seguir a sequência para que o menu funcione.", description='Ordem de Exibição:'),
        form.Textbox('nome', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Página.", description='Titulo:'),
        form.Textbox('descricao', form.notnull, size="60", maxlenght="250", title="Descrição do Menu.", description='Descrição:'),
        form.Textbox('data_criacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de criação da Página.", readonly="readonly", description='Criado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('ultima_alteracao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de última atualização da Página.", readonly="readonly", description='Última Alteração em: (YYYY-MM-DD HH:MM:SS)'),
        form.Dropdown('pagina', pagina_options, title="Página que deve ser exibida ao clicar no menu.", description='Página: '),
        form.Textbox('endereco', form.notnull, size="60", maxlenght="250", title="Endereço do link.", description='Endereço do Link:'),
        form.Dropdown('menu_pai', menu_options, title="Menu Pai/Superior do Menu.", description='Menu Superior: '),
        form.Dropdown('nivel', [('0', '0'), ('1', '1'), ('2', '2')], title="Nível do Menu: 0 - MenuBar, 1-Menu Principal, 2-Menu Interno.", description='Nível: ')
    )
    return menu_form

def getPaginaForm():
    pagina_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('nome', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Página.", description='Titulo:'),
        form.Textbox('slug', size="60", maxlenght="250", title="URL da Página.", readonly="readonly", description='URL da Página'),
        form.Textbox('descricao_completa', form.notnull, size="60", maxlenght="250", title="Descrição Completa da Página.", description='Descrição Completa:'),
        form.Textbox('palavras_chaves', form.notnull, size="60", maxlenght="250", title="Palavras Chaves da Página separadas por vírgula.", description='Palavras Chaves:'),
        form.Textbox('data_criacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de criação da Página.", readonly="readonly", description='Criado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('ultima_alteracao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de última atualização da Página.", readonly="readonly", description='Última Alteração em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textarea('conteudo', form.notnull, cols="70", rows="25", title="Conteúdo da Página.", description='Conteúdo da Página:')
    )
    return pagina_form

def getMenuForm():
    menu_list = model.Menu.all()
    menu_options = [(str(row.key().id()), row.nome) for row in menu_list]
    pagina_list = model.Pagina.all()
    pagina_options = [(str(row.key().id()), row.nome) for row in pagina_list]
    menu_form = form.GAEForm(
        form.Hidden('key'),
        form.Hidden('operation'),
        form.Textbox('ordem', vdigito, size="10", maxlenght="50", title="Ordem de Exibição do Menu na Página. Deve seguir a sequência para que o menu funcione.", description='Ordem de Exibição:'),
        form.Textbox('nome', form.notnull, size="60", maxlenght="250", title="Titulo/Nome da Página.", description='Titulo:'),
        form.Textbox('descricao', form.notnull, size="60", maxlenght="250", title="Descrição do Menu.", description='Descrição:'),
        form.Textbox('data_criacao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de criação da Página.", readonly="readonly", description='Criado em: (YYYY-MM-DD HH:MM:SS)'),
        form.Textbox('ultima_alteracao', vdatafull, size="15", maxlenght="20", class_="datetime", title="Data e Hora de última atualização da Página.", readonly="readonly", description='Última Alteração em: (YYYY-MM-DD HH:MM:SS)'),
        form.Dropdown('pagina', pagina_options, title="Página que deve ser exibida ao clicar no menu.", description='Página: '),
        form.Textbox('endereco', form.notnull, size="60", maxlenght="250", title="Endereço do link.", description='Endereço do Link:'),
        form.Dropdown('menu_pai', menu_options, title="Menu Pai/Superior do Menu.", description='Menu Superior: '),
        form.Dropdown('nivel', [('0', '0'), ('1', '1'), ('2', '2')], title="Nível do Menu: 0 - MenuBar, 1-Menu Principal, 2-Menu Interno.", description='Nível: ')
    )
    return menu_form

def getContatoForm():
    contato_form = form.Form(
        form.Textbox('nome', form.notnull, size="60", maxlenght="250", title="Informe o seu nome.", description='Nome:'),
        form.Textbox('telefone', form.notnull, size="60", maxlenght="250", title="Informe o seu telefone.", description='Telefone:'),
        form.Textbox('email', vemail, size="60", maxlenght="250", title="Informe o seu E-mail.", description='E-mail:'),
        form.Textbox('assunto', form.notnull, size="60", maxlenght="250", title="Informe o Assunto.", description='Assunto:'),
        form.Textarea('mensagem_adicional', cols="51", rows="15", title="Inclua sua mensagem.", description='Mensagem:'),
        form.Button('Submit!', html="Enviar", type="submit")
    )
    return contato_form

def getPedidoForm():
    pedido_form = form.Form(
        form.Textbox('razao_social', form.notnull, size="60", maxlenght="250", title="Informe o nome da sua empresa.", description='Razão Social:'),
        form.Textbox('cnpj', form.notnull, size="60", maxlenght="250", onblur="validate_cnpj(this);", title="Informe o CNPJ da sua empresa.", description='C.N.P.J:'),
        form.Textbox('telefone', form.notnull, size="60", maxlenght="250", title="Informe o seu telefone.", description='Telefone:'),
        form.Textbox('email', vemail, size="60", maxlenght="250", title="Informe o seu E-mail.", description='E-mail:'),
        form.Textbox('cod_01', form.notnull, size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_01', form.notnull, size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_02', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_02', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_03', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_03', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_04', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_04', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_05', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_05', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_06', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_06', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_07', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_07', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_08', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_08', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_09', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_09', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_10', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_10', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_11', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_11', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_12', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_12', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_13', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_13', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_14', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_14', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_15', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_15', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_16', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_16', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_17', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_17', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_18', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_18', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_19', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_19', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_20', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_20', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textbox('cod_21', size="10", maxlenght="10", onblur="ajax_get_data(this);", onkeypress="return only_integer(this);", title="Informe o Código do Produto.", description='Código:'),
        form.Textbox('qtde_21', size="10", maxlenght="10", onkeypress="return only_float(this);", title="Informe a Quantidade do Produto.", description='Qtde:'),
        form.Textarea('obs', cols="51", rows="15", title="Inclua sua mensagem.", description='Observações:'),
        form.Button('Submit!', html="Enviar", type="submit")
    )
    return pedido_form
