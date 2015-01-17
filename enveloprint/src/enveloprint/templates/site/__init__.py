from web.template import CompiledTemplate, ForLoop, TemplateResult

_dummy = CompiledTemplate(lambda: None, 'dummy')
join_ = _dummy._join
escape_ = _dummy._escape

def agradece_pedido():
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes - Agredecimento do Pedido.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'or\xe7amento, pedido, formul\xe1rio de pedido, pedido enviado com sucesso')
    extend_([u'\n'])
    extend_([u'<span class="agradecimento_panel">Obrigado pelo seu pedido, entraremos em contato para a realizar a confirma\xe7\xe3o do mesmo !.</span>\n'])

    return self

agradece_pedido = CompiledTemplate(agradece_pedido, 'templates/site/agradece_pedido.html')

def contato (action, method, form):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes - Contato.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'contato, telefones, localiza\xe7\xe3o, pontos de refer\xeancia')
    extend_([u'\n'])
    extend_([u'<h3>Dados de Contato</h3>\n'])
    extend_([u'\n'])
    extend_([u'<div id="localization_panel">\n'])
    extend_([u'    <iframe width="640" height="480" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com.br/maps?f=q&amp;source=s_q&amp;hl=pt-BR&amp;geocode=&amp;q=Rua+Bernardino+Silveira+Amorim,+n%C2%BA.+961%2F971,+Bairro+Sarandi,+Porto+Alegre,+RS,+Brasil&amp;aq=&amp;sll=-14.239424,-53.186502&amp;sspn=41.378709,79.013672&amp;ie=UTF8&amp;hq=&amp;hnear=Av.+Bernardino+Silveira+Amorim,+961+-+Sarandi,+Porto+Alegre+-+Rio+Grande+do+Sul,+91140-410&amp;ll=-29.988616,-51.109943&amp;spn=0.035683,0.054932&amp;z=14&amp;iwloc=A&amp;output=embed"></iframe><br /><small><a href="http://maps.google.com.br/maps?f=q&amp;source=embed&amp;hl=pt-BR&amp;geocode=&amp;q=Rua+Bernardino+Silveira+Amorim,+n%C2%BA.+961%2F971,+Bairro+Sarandi,+Porto+Alegre,+RS,+Brasil&amp;aq=&amp;sll=-14.239424,-53.186502&amp;sspn=41.378709,79.013672&amp;ie=UTF8&amp;hq=&amp;hnear=Av.+Bernardino+Silveira+Amorim,+961+-+Sarandi,+Porto+Alegre+-+Rio+Grande+do+Sul,+91140-410&amp;ll=-29.988616,-51.109943&amp;spn=0.035683,0.054932&amp;z=14&amp;iwloc=A" style="color:#0000FF;text-align:left">Exibir mapa ampliado</a></small>\n'])
    extend_([u'    <h4>Endere\xe7o:</h4>\n'])
    extend_([u'    <span>Av. Bernardino Silveira Amorim, 961/971 - Sarandi - Porto Alegre - RS - Brasil, CEP: 91140-410</span>\n'])
    extend_([u'    <h4>Pontos de Refer\xeancia:</h4>\n'])
    extend_([u'    <span>Pr\xf3xima a FIERGS e o Porto Seco.</span>\n'])
    extend_([u'    <h4>Telefones:</h4>\n'])
    extend_([u'    <span>Comercial: (51) 3364-1537 e (51) 3364-1538 - Administrativo: (51) 3365-1166 - (51) 3365-3843</span>\n'])
    extend_([u'    <h4>E-mails:</h4>\n'])
    extend_([u'    <ul>\n'])
    extend_([u'        <li><span class="bold_style">Comercial: </span><span>comercial@enveloprint.com.br</span></li>\n'])
    extend_([u'        <li><span class="bold_style">Vendas: </span><span>vendas@enveloprint.com.br</span></li>\n'])
    extend_([u'        <li><span class="bold_style">Fin\xe2nceiro: </span><span>financeiro@enveloprint.com.br</span></li>\n'])
    extend_([u'        <li><span class="bold_style">RH: </span><span>rh@enveloprint.com.br</span></li>\n'])
    extend_([u'        <li><span class="bold_style">Administrativo: </span><span>administrativo@enveloprint.com.br</span></li>\n'])
    extend_([u'    </ul>\n'])
    extend_([u'    <h4>Deixe o seu recardo:</h4>\n'])
    extend_([u'    <form action="', escape_(action, True), u'" method="', escape_(method, True), u'">\n'])
    extend_([u'        ', escape_(form.render(), False), u'\n'])
    extend_([u'    </form>\n'])
    extend_([u'</div>\n'])

    return self

contato = CompiledTemplate(contato, 'templates/site/contato.html')

def listar_produtos (pagination):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'produtos, portif\xf3lio, cat\xe1logo')
    extend_([u'\n'])
    extend_([u'<h3>Categorias de Produto</h3>\n'])
    extend_([u'<ul id="lista_produtos">\n'])
    for record in loop.setup(pagination.records):
        extend_([u'<li>\n'])
        extend_([u'    <a href="/detalhar/CategoriaProduto/', escape_(record.slug, False), u'" class="titulo_noticia" title="Link para a not\xedcia ', escape_(record.nome, False), u' completa."><img src=" ', escape_(record.icone, False), u'" alt="Imagem da Categoria de Produto ', escape_(record.nome, False), u'." title="', escape_(record.nome, False), u'." class="thumb_noticia" /></a>\n'])
        extend_([u'    <a href="/detalhar/CategoriaProduto/', escape_(record.slug, False), u'" class="titulo_noticia" title="Link para a not\xedcia ', escape_(record.nome, False), u' completa.">', escape_(record.nome, False), u'</a>\n'])
        extend_([u'</li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'<div id="panel_records">\n'])
    if pagination.prev_page:
        extend_([u'<a href="/listar/', escape_(pagination.classe_name, True), u'?page=', escape_(pagination.prev_page, True), u'&size=', escape_(pagination.pagesize, True), u'&q=', escape_(pagination.query, True), u'" title="P\xe1gina Anterior."><img src="/static/images/back.png" alt="P\xe1gina Anterior." title="P\xe1gina Anterior." class="noborder" /></a>\n'])
        extend_([u'\n'])
    if not pagination.prev_page and not pagination.next_page and pagination.total_records > 0:
        extend_([u'<span>Mostrando de 1 \xe0 ', escape_(pagination.record_counts, True), u' registros.</span>\n'])
    elif pagination.total_records == 0:
        extend_([u'<span>Sem Registros.</span>\n'])
    else:
        if (int(pagination.pagesize) + int(pagination.start)) > int(pagination.total_records):
            extend_([u'<span>Mostrando registros de ', escape_((int(pagination.start) + 1), True), u' \xe0 ', escape_((int(pagination.total_records)), True), u'.</span>\n'])
        else:
            extend_([u'<span>Mostrando registros de ', escape_((int(pagination.start) + 1), True), u' \xe0 ', escape_((int(pagination.pagesize) + int(pagination.start)), True), u' no total de ', escape_(pagination.total_records, True), u' registros.</span>\n'])
            extend_([u'\n'])
    if pagination.next_page:
        extend_([u'<a href="/listar/', escape_(pagination.classe_name, True), u'?page=', escape_(pagination.next_page, True), u'&size=', escape_(pagination.pagesize, True), u'&q=', escape_(pagination.query, True), u'" title="Pr\xf3xima P\xe1gina."><img src="/static/images/forward.png" alt="Pr\xf3xima P\xe1gina." title="Pr\xf3xima P\xe1gina." class="noborder" /></a>\n'])
    extend_([u'</div>\n'])

    return self

listar_produtos = CompiledTemplate(listar_produtos, 'templates/site/listar_produtos.html')

def detalhar (nome, produtos):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes - Produtos da Categoria: ', escape_(nome, False), u'.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'produtos, listagem, ', escape_(nome, False))
    extend_([u'\n'])
    extend_([u'<style type="text/css">\n'])
    extend_([u'    #painel_visualizacao { margin: 0px auto;margin-top: 20px;height:310px;width:673px;background-color:#eee;border:01px solid #ccc; }\n'])
    extend_([u'    #painel_visualizacao_container { margin: 0px auto; width:673px;text-align:right;margin-top: 05px; }\n'])
    extend_([u'    #painel_visualizacao_buttons_panel { margin:0px auto;width:673px;float:left;margin-bottom:10px; }\n'])
    extend_([u'    .buttons_numbers { text-align:center; font-size: 14px; font-weight: bold;background-color: #ccc;height: 18px;width:20px;border:01px solid #000;float:left;margin-right:03px;padding:02px 02px 0px; }\n'])
    extend_([u'    #table_produtos { margin:0px auto;margin-top:20px;width:70%;border-style:thin; }\n'])
    extend_([u'</style>\n'])
    extend_([u'\n'])
    extend_([u'<h3>', escape_(nome, False), u'</h3>\n'])
    extend_([u'<div id="painel_visualizacao"><img src="" alt="" title="" id="img_obj" /></div>\n'])
    extend_([u'<div id="painel_visualizacao_container">\n'])
    extend_([u'    <div id="painel_visualizacao_buttons_panel">\n'])
    extend_([u'        <div id="icon_01" class="buttons_numbers" rel="" onclick="show_picture_from_icon(this);">1</div>\n'])
    extend_([u'        <div id="icon_02" class="buttons_numbers" rel="" onclick="show_picture_from_icon(this);">2</div>\n'])
    extend_([u'        <div id="icon_03" class="buttons_numbers" rel="" onclick="show_picture_from_icon(this);">3</div>\n'])
    extend_([u'        <div id="icon_04" class="buttons_numbers" rel="" onclick="show_picture_from_icon(this);">4</div>\n'])
    extend_([u'        <div id="icon_05" class="buttons_numbers" rel="" onclick="show_picture_from_icon(this);">5</div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<table id="table_produtos" border="1">\n'])
    extend_([u'    <tr><th></th><th>COD.</th><th>REFER\xcaNCIA</th><th>FORMATO</th><th>GRAMATURA</th><th>COR</th><th>UNDIDADES P/ EMBALAGEM</th></tr>\n'])
    for produto in loop.setup(produtos):
        extend_(['    ', u'<tr><td><input type="radio" name="produto_radio" id="', escape_(produto.codigo, False), u'" value="', escape_(produto.foto_produto_01, False), u'|', escape_(produto.foto_produto_02, False), u'|', escape_(produto.foto_produto_03, False), u'|', escape_(produto.foto_produto_04, False), u'|', escape_(produto.foto_produto_05, False), u'" onclick="set_picture_panel(this);"/></td><td>', escape_(produto.codigo, False), u'</td><td>', escape_(produto.referencia, False), u'</td><td>', escape_(produto.formato, False), u'</td><td>', escape_(produto.gramatura, False), u'</td><td style="background-color:', escape_(produto.cor, False), u';border:01px solid #000;"></td><td>', escape_(produto.unidade_embalagem, False), u' unidades por ', escape_(produto.tipo_embalagem, False), u'</td></tr>\n'])
    extend_([u'</table>\n'])
    extend_([u'\n'])
    extend_([u'<script type="text/javascript">\n'])
    extend_([u'    function set_picture_panel(obj){\n'])
    extend_([u'        str_pictures = obj.value;\n'])
    extend_([u'        pictures = str_pictures.split("|");\n'])
    extend_([u'        div_picture_01 = document.getElementById("icon_01");\n'])
    extend_([u'        div_picture_01.rel = pictures[0];\n'])
    extend_([u'        div_picture_02 = document.getElementById("icon_02");\n'])
    extend_([u'        div_picture_02.rel = pictures[1];\n'])
    extend_([u'        div_picture_03 = document.getElementById("icon_03");\n'])
    extend_([u'        div_picture_03.rel = pictures[2];\n'])
    extend_([u'        div_picture_04 = document.getElementById("icon_04");\n'])
    extend_([u'        div_picture_04.rel = pictures[3];\n'])
    extend_([u'        div_picture_05 = document.getElementById("icon_05");\n'])
    extend_([u'        div_picture_05.rel = pictures[4];\n'])
    extend_([u'        document.getElementById("img_obj").src = pictures[0];\n'])
    extend_([u'    }\n'])
    extend_([u'    function show_picture_from_icon(icon){ document.getElementById("img_obj").src = icon.rel; }\n'])
    extend_([u"    jQuery(document).ready(function(){ jQuery('#", escape_(produtos[0].codigo, False), u"').click(); })\n"])
    extend_([u'</script>\n'])

    return self

detalhar = CompiledTemplate(detalhar, 'templates/site/detalhar.html')

def listar_curiosidades (pagination):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes - Curiosidades.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'curiosidades, dicas, envelopes, dicas sobre envelopes')
    extend_([u'\n'])
    extend_([u'<h3>Curiosidades</h3>\n'])
    extend_([u'<div id="panel_curiosidades">\n'])
    for record in loop.setup(pagination.records):
        extend_([u'<h4 class="margintop10px">', escape_(record.nome, False), u'</h4>\n'])
        extend_([u'<p>', escape_(record.detalhamento, False), u'</p>\n'])
        extend_([u'<br class="clearboth" />\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="panel_records">\n'])
    if pagination.prev_page:
        extend_([u'<a href="/listar/', escape_(pagination.classe_name, True), u'?page=', escape_(pagination.prev_page, True), u'&size=', escape_(pagination.pagesize, True), u'&q=', escape_(pagination.query, True), u'" title="P\xe1gina Anterior."><img src="/static/images/back.png" alt="P\xe1gina Anterior." title="P\xe1gina Anterior." class="noborder" /></a>\n'])
        extend_([u'\n'])
    if not pagination.prev_page and not pagination.next_page and pagination.total_records > 0:
        extend_([u'<span>Mostrando de 1 \xe0 ', escape_(pagination.record_counts, True), u' registros.</span>\n'])
    elif pagination.total_records == 0:
        extend_([u'<span>Sem Registros.</span>\n'])
    else:
        if (int(pagination.pagesize) + int(pagination.start)) > int(pagination.total_records):
            extend_([u'<span>Mostrando registros de ', escape_((int(pagination.start) + 1), True), u' \xe0 ', escape_((int(pagination.total_records)), True), u'.</span>\n'])
        else:
            extend_([u'<span>Mostrando registros de ', escape_((int(pagination.start) + 1), True), u' \xe0 ', escape_((int(pagination.pagesize) + int(pagination.start)), True), u' no total de ', escape_(pagination.total_records, True), u' registros.</span>\n'])
            extend_([u'\n'])
    if pagination.next_page:
        extend_([u'<a href="/listar/', escape_(pagination.classe_name, True), u'?page=', escape_(pagination.next_page, True), u'&size=', escape_(pagination.pagesize, True), u'&q=', escape_(pagination.query, True), u'" title="Pr\xf3xima P\xe1gina."><img src="/static/images/forward.png" alt="Pr\xf3xima P\xe1gina." title="Pr\xf3xima P\xe1gina." class="noborder" /></a>\n'])
    extend_([u'</div>\n'])

    return self

listar_curiosidades = CompiledTemplate(listar_curiosidades, 'templates/site/listar_curiosidades.html')

def agradece_contato():
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes - Agredecimento do Contato.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'envio de e-mail, contato enviado com sucesso')
    extend_([u'\n'])
    extend_([u'<span class="agradecimento_panel">Obrigado pelo seu contato !.</span>\n'])

    return self

agradece_contato = CompiledTemplate(agradece_contato, 'templates/site/agradece_contato.html')

def atendimento ():
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes - Atendimento Online.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'atendimento, contato, MSN, messenger')
    extend_([u'\n'])
    extend_([u'<h3>Atendimento Online</h3>\n'])
    extend_([u'<div id="pagina">\n'])
    extend_([u'<p>Tire sua d\xfavida ou fa\xe7a seu coment\xe1rio no nosso atendimento online. Atrav\xe9s deste recurso temos um canal \xe1gil com voc\xea nosso cliente.</p>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="atendimento_panel" style="text-align:center;">\n'])
    extend_([u'    <iframe src="http://settings.messenger.live.com/Conversation/IMMe.aspx?invitee=191f6dfdf0da3caa@apps.messenger.live.com&mkt=pt-BR" width="300" height="300" style="border: solid 1px black; width: 300px; height: 300px;" frameborder="0" scrolling="no"></iframe>\n'])
    extend_([u'</div>\n'])

    return self

atendimento = CompiledTemplate(atendimento, 'templates/site/atendimento.html')

def base (render_vars, content):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n'])
    extend_([u'    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n'])
    extend_([u'<head>\n'])
    extend_([u'    <title>', escape_(content.title, True), u'</title>\n'])
    extend_([u'    <meta name="google-site-verification" content="nlaJXUykNvR8hx-48J4M7l2ZAnVmIjKtFw0sp1kfYME" />\n'])
    extend_([u'    <meta http-equiv="content-type" content="text/html;charset=utf-8" />\n'])
    extend_([u'    <meta name="generator" content="Geany 0.19.1" />\n'])
    extend_([u'    <meta name="language" content="pt-br"/>\n'])
    extend_([u'    <meta name="copyright" content="Copyright (c) 2011 Enveloprint. This site\'s design and html code is licensed under the terms of the GPLv3 or (at your option) any later version."/>\n'])
    extend_([u'    <meta name="organization name" content="Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes." />\n'])
    extend_([u'    <meta name="author" content="professionalit.com.br - Sistemas, Sites, Aplica\xe7\xf5es Web e Mobile."/>\n'])
    extend_([u'    <meta name="Description" content="', escape_(content.full_description, True), u'" lang="pt-BR"/>\n'])
    extend_([u'    <meta name="Keywords" content="', escape_(content.keywords_tags, True), u'" lang="pt-BR"/>\n'])
    extend_([u'    <meta name="rating" content="', escape_(content.keywords_tags, True), u'"/>\n'])
    extend_([u'    <meta name="DC.title" content="enveloprint.com.br"/>\n'])
    extend_([u'    <meta name="robots" content="ALL"/>\n'])
    extend_([u'    <meta name="googlebot" content="all" />\n'])
    extend_([u'    <meta name="classification" content="Internet" />\n'])
    extend_([u'    <meta name="distribution" content="Global" />\n'])
    extend_([u'    <meta name="revisit-after" content="2 days" />\n'])
    extend_([u"    <link rel='index' title='Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes.' href='http://www.enveloprint.com.br'></link>\n"])
    extend_([u'    <link rel="canonical" href="http://www.enveloprint.com.br"></link>\n'])
    extend_([u'    <link rel="author" title="Author information" href="/pagina/autor">\n'])
    extend_([u'    <link rel="copyright" title="Script license and terms of use" href="/pagina/termo">\n'])
    extend_([u'    <link rel="home" title="How To Create home" href="/">\n'])
    extend_([u'    <link rel="search" title="Search this site" href="/">\n'])
    extend_([u'    <link rel="bookmark" href="/" title="Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes">\n'])
    extend_([u'    <link rel="bookmark" href="/produtos" title="Nosso cat\xe1logo de produtos.">\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" media="screen" href="/static/css/style.css" />\n'])
    extend_([u'    <script type="text/javascript">var _siteRoot=\'base.html\',_root=\'base.html\';</script>\n'])
    extend_([u'    <script type="text/javascript" src="/static/javascript/jquery.js"></script>\n'])
    extend_([u'    <script type="text/javascript" src="/static/javascript/scripts.js"></script>\n'])
    extend_([u'    <script type="text/javascript" src="/static/javascript/ajax.js"></script>\n'])
    extend_([u'    <!-- Analitycs CODE -->\n'])
    extend_([u'    <script type="text/javascript">\n'])
    extend_([u'      var _gaq = _gaq || [];\n'])
    extend_([u"      _gaq.push(['_setAccount', 'UA-26023956-1']);\n"])
    extend_([u"      _gaq.push(['_trackPageview']);\n"])
    extend_([u'\n'])
    extend_([u'      (function() {\n'])
    extend_([u"        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;\n"])
    extend_([u"        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';\n"])
    extend_([u"        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);\n"])
    extend_([u'      })();\n'])
    extend_([u'    </script>\n'])
    extend_([u' </head>\n'])
    extend_([u'<body>\n'])
    extend_([u'    <div id="header" style="background: url(\'', escape_(render_vars['background_header'], True), u'\') no-repeat left top;">\n'])
    extend_([u'        <img src="/static/images/logotipo.png" alt="Logotipo da Enveloprint." title="Enveloprint-Solu\xe7\xf5es personalizadas em Envelopes." />\n'])
    extend_([u'        <div id="barra_lateral"></div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="content">\n'])
    extend_([u'        <div id="sidebar">\n'])
    extend_([u'            <ul id="menu">\n'])
    extend_([u'                <li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="P\xe1gina Inicial." /><a href="/" title="P\xe1gina Inicial." class="selected">Home</a></li>\n'])
    extend_([u'                <li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="Conhe\xe7a a Enveloprint." /><a href="/pagina/empresa" title="Conhe\xe7a a Enveloprint.">Empresa</a></li>\n'])
    extend_([u'                <!--li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="Conhe\xe7a o nosso processo de produ\xe7\xe3o." /><a href="/pagina/fabricacao" title="Conhe\xe7a o nosso processo de produ\xe7\xe3o.">Veja Fabrica\xe7\xe3o</a></li-->\n'])
    extend_([u'                <li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="Curiosidades sobre os Envelopes." /><a href="/listar/Curiosidade" title="Curiosidades sobre os Envelopes.">Curiosidades</a></li>\n'])
    extend_([u'                <li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="Conhe\xe7a nossa linha de produtos." /><a href="/listar/CategoriaProduto" title="Conhe\xe7a nossa linha de produtos.">Produtos</a></li>\n'])
    extend_([u'                <li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="Nossos representantes." /><a href="/pagina/representantes" title="Nossos representantes.">Representantes</a></li>\n'])
    extend_([u'                <li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="Entre em contato conosco." /><a href="/contato" title="Entre em contato conosco.">Contato</a></li>\n'])
    extend_([u'                <li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="Vagas e oportunidades de trabalho." /><a href="/pagina/trabalhe-conosco" title="Vagas e oportunidades de trabalho.">Trabalhe Conosco</a></li>\n'])
    extend_([u'                <li><img src="/static/images/email_16.png" alt="Icone do E-mail." title="Or\xe7amento Online." /><a href="/orcamento" title="Or\xe7amento Online.">Or\xe7amento</a></li>\n'])
    extend_([u'            </ul>\n'])
    extend_([u'            <div id="telefone_panel" class="call_panels">\n'])
    extend_([u'                <img src="/static/images/icone-telefone.png" alt="" title="" class="imgs_phone" />\n'])
    extend_([u'                <span class="span_details_phone">Comercial</span>\n'])
    extend_([u'                <span class="span_details_phone">(51) 3364-1537</span>\n'])
    extend_([u'                <span class="span_details_phone">(51) 3364-1538</span>\n'])
    extend_([u'                <br/>\n'])
    extend_([u'                <span class="span_details_phone">Administrativo</span>\n'])
    extend_([u'                <span class="span_details_phone">(51) 3365-1166</span>\n'])
    extend_([u'                <span class="span_details_phone">(51) 3365-3843</span>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div id="messenger_panel" class="call_panels">\n'])
    extend_([u'                <a href="/atendimento_online" title="Tire suas d\xfavidas online."><img src="/static/images/msn.png" alt="Icone do MSN" title="Tire suas d\xfavidas online." class="imgs_phone" /></a>\n'])
    extend_([u'                <span id="explain_msn">Atendimento Online</span>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div id="channel_panel" class="call_panels">\n'])
    extend_([u'                <a href="#" title="Twitter da Enveloprint."><img src="/static/images/twitter.png" alt="Icone do Twitter." title="Visite o nosso Twitter." /></a>\n'])
    extend_([u'                <span id="explain_msn">Nosso Twitter</span>\n'])
    extend_([u'                <a href="#" title="Nossa P\xe1gina no Facebook."><img src="/static/images/facebook.png" alt="Icone do Facebook." title="Visite a nossa p\xe1gina no Facebook." /></a>\n'])
    extend_([u'                <span id="explain_msn">Nosso Facebook</span>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div id="page">\n'])
    extend_([u'             ', escape_(content, False), u'\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="footer"><p>Enveloprint 2015 - Fones Comercial: (51) 3364-1537 - (51) 3364-1538 - Fones Administrativo: (51) 3365-1166 - (51) 3365-3843 | CNPJ: 001.887.292/0001-99</p></div>\n'])
    extend_([u'    <script type="text/javascript">\n'])
    extend_([u'        window.onload=auto_height();\n'])
    extend_([u'    </script>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/site/base.html')

def provisorio():
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'])
    extend_([u'<html xmlns="http://www.w3.org/1999/xhtml">\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n'])
    extend_([u'    <title>::: Enveloprint :::</title>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body style="font-family: arial;text-align:center;">\n'])
    extend_([u'    <div style="width:100%;height:100%;text-align:center;">\n'])
    extend_([u'        <img src="/static/images/logotipo.gif" alt="logotipo da Enveloprint." border="0"/>\n'])
    extend_([u'        <br/>\n'])
    extend_([u'        <br/>\n'])
    extend_([u'        <p>\n'])
    extend_([u'            Estamos <strong>desenvolvendo o nosso site</strong>, ent\xe3o em breve ele estar\xe1 no ar com muito conte\xfado e informa\xe7\xe3o. \n'])
    extend_([u'        </p>\n'])
    extend_([u'        <br/>\n'])
    extend_([u'        <p>Desenvolvido por: <a href="http://www.professionalit.com.br" target="_blank" style="text-decoration:none;" title="ProfessionalIt - Os Profissionais da Tecnologia da Informa\xe7\xe3o."><img src="/static/images/professionalit_badge.png" alt="logotipo da professionalIt" border="0"/></a></p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

provisorio = CompiledTemplate(provisorio, 'templates/site/provisorio.html')

def pagina (conteudo):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes - ', escape_(conteudo.nome, False))
    self['full_description'] = join_(escape_(conteudo.descricao_completa, False), u'.')
    self['keywords_tags'] = join_(escape_(conteudo.palavras_chaves, False))
    extend_([u'\n'])
    extend_([u'<div id="pagina">\n'])
    extend_([escape_(conteudo.conteudo, False), u'\n'])
    extend_([u'</div>\n'])

    return self

pagina = CompiledTemplate(pagina, 'templates/site/pagina.html')

def pedido (action, method, form):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes - Or\xe7amento.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'or\xe7amento, pedido, formul\xe1rio de pedido')
    extend_([u'\n'])
    extend_([u'<h3>Dados do Or\xe7amento</h3>\n'])
    extend_([u'\n'])
    extend_([u'<div id="localization_panel">\n'])
    extend_([u'    <form action="', escape_(action, True), u'" method="', escape_(method, True), u'" onsubmit="validate_fields();">\n'])
    extend_([u'        <table cellspacing="0" border="1" style="width:70%;">\n'])
    extend_([u'            <tr><td class="label_name"><span class="label_required">*</span>', escape_(form.razao_social.description, False), u'</td><td>', escape_(form.razao_social.render(), False), u'</td></tr>\n'])
    extend_([u'            <tr><td class="label_name"><span class="label_required">*</span>', escape_(form.cnpj.description, False), u'</td><td>', escape_(form.cnpj.render(), False), u'</td></tr>\n'])
    extend_([u'            <tr><td class="label_name"><span class="label_required">*</span>', escape_(form.telefone.description, False), u'</td><td>', escape_(form.telefone.render(), False), u'</td></tr>\n'])
    extend_([u'            <tr><td class="label_name"><span class="label_required">*</span>', escape_(form.email.description, False), u'</td><td>', escape_(form.email.render(), False), u'</td></tr>\n'])
    extend_([u'            <tr><td colspan="2" class="bold_style" style="background-color: #eee;margin-top:10px;height:30px;">Produtos</td></tr>\n'])
    extend_([u'            <tr align="center">\n'])
    extend_([u'                <td align="center" colspan="2">\n'])
    extend_([u'                    <table>\n'])
    extend_([u'                        <tr><td align="center" class="bold_style">C\xf3digo</td><td align="center" class="bold_style">Nome</td><td align="center" class="bold_style">Embalagem</td><td align="center" class="bold_style">Quantidade</td></tr>\n'])
    extend_([u'                        <tr><td>01 - ', escape_(form.cod_01.render(), False), u'</td><td><span id="nome_produto_01" class="txt_response_large"></span></td><td><span id="embalagem_produto_01" class="txt_response"></span></td><td>', escape_(form.qtde_01.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>02 - ', escape_(form.cod_02.render(), False), u'</td><td><span id="nome_produto_02" class="txt_response_large"></span></td><td><span id="embalagem_produto_02" class="txt_response"></span></td><td>', escape_(form.qtde_02.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>03 - ', escape_(form.cod_03.render(), False), u'</td><td><span id="nome_produto_03" class="txt_response_large"></span></td><td><span id="embalagem_produto_03" class="txt_response"></span></td><td>', escape_(form.qtde_03.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>04 - ', escape_(form.cod_04.render(), False), u'</td><td><span id="nome_produto_04" class="txt_response_large"></span></td><td><span id="embalagem_produto_04" class="txt_response"></span></td><td>', escape_(form.qtde_04.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>05 - ', escape_(form.cod_05.render(), False), u'</td><td><span id="nome_produto_05" class="txt_response_large"></span></td><td><span id="embalagem_produto_05" class="txt_response"></span></td><td>', escape_(form.qtde_05.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>06 - ', escape_(form.cod_06.render(), False), u'</td><td><span id="nome_produto_06" class="txt_response_large"></span></td><td><span id="embalagem_produto_06" class="txt_response"></span></td><td>', escape_(form.qtde_06.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>07 - ', escape_(form.cod_07.render(), False), u'</td><td><span id="nome_produto_07" class="txt_response_large"></span></td><td><span id="embalagem_produto_07" class="txt_response"></span></td><td>', escape_(form.qtde_07.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>08 - ', escape_(form.cod_08.render(), False), u'</td><td><span id="nome_produto_08" class="txt_response_large"></span></td><td><span id="embalagem_produto_08" class="txt_response"></span></td><td>', escape_(form.qtde_08.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>09 - ', escape_(form.cod_09.render(), False), u'</td><td><span id="nome_produto_09" class="txt_response_large"></span></td><td><span id="embalagem_produto_09" class="txt_response"></span></td><td>', escape_(form.qtde_09.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>10 - ', escape_(form.cod_10.render(), False), u'</td><td><span id="nome_produto_10" class="txt_response_large"></span></td><td><span id="embalagem_produto_10" class="txt_response"></span></td><td>', escape_(form.qtde_10.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>11 - ', escape_(form.cod_11.render(), False), u'</td><td><span id="nome_produto_11" class="txt_response_large"></span></td><td><span id="embalagem_produto_11" class="txt_response"></span></td><td>', escape_(form.qtde_11.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>12 - ', escape_(form.cod_12.render(), False), u'</td><td><span id="nome_produto_12" class="txt_response_large"></span></td><td><span id="embalagem_produto_12" class="txt_response"></span></td><td>', escape_(form.qtde_12.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>13 - ', escape_(form.cod_13.render(), False), u'</td><td><span id="nome_produto_13" class="txt_response_large"></span></td><td><span id="embalagem_produto_13" class="txt_response"></span></td><td>', escape_(form.qtde_13.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>14 - ', escape_(form.cod_14.render(), False), u'</td><td><span id="nome_produto_14" class="txt_response_large"></span></td><td><span id="embalagem_produto_14" class="txt_response"></span></td><td>', escape_(form.qtde_14.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>15 - ', escape_(form.cod_15.render(), False), u'</td><td><span id="nome_produto_15" class="txt_response_large"></span></td><td><span id="embalagem_produto_15" class="txt_response"></span></td><td>', escape_(form.qtde_15.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>16 - ', escape_(form.cod_16.render(), False), u'</td><td><span id="nome_produto_16" class="txt_response_large"></span></td><td><span id="embalagem_produto_16" class="txt_response"></span></td><td>', escape_(form.qtde_16.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>17 - ', escape_(form.cod_17.render(), False), u'</td><td><span id="nome_produto_17" class="txt_response_large"></span></td><td><span id="embalagem_produto_17" class="txt_response"></span></td><td>', escape_(form.qtde_17.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>18 - ', escape_(form.cod_18.render(), False), u'</td><td><span id="nome_produto_18" class="txt_response_large"></span></td><td><span id="embalagem_produto_18" class="txt_response"></span></td><td>', escape_(form.qtde_18.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>19 - ', escape_(form.cod_19.render(), False), u'</td><td><span id="nome_produto_19" class="txt_response_large"></span></td><td><span id="embalagem_produto_19" class="txt_response"></span></td><td>', escape_(form.qtde_19.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>20 - ', escape_(form.cod_20.render(), False), u'</td><td><span id="nome_produto_20" class="txt_response_large"></span></td><td><span id="embalagem_produto_20" class="txt_response"></span></td><td>', escape_(form.qtde_20.render(), False), u'</td></tr>\n'])
    extend_([u'                        <tr><td>21 - ', escape_(form.cod_21.render(), False), u'</td><td><span id="nome_produto_21" class="txt_response_large"></span></td><td><span id="embalagem_produto_21" class="txt_response"></span></td><td>', escape_(form.qtde_21.render(), False), u'</td></tr>\n'])
    extend_([u'                    </table>\n'])
    extend_([u'                </td>\n'])
    extend_([u'            </tr>\n'])
    extend_([u'        </table>\n'])
    extend_([u'        <button type="submit" id="salvar_button" name="salvar_button">Enviar</button>\n'])
    extend_([u'    </form>\n'])
    extend_([u'</div>\n'])
    extend_([u'<script type="text/javascript">\n'])
    extend_([u'    function validate_cnpj(obj) {\n'])
    extend_([u'        alert("CNPJ inv\xe1lido !");\n'])
    extend_([u'    }\n'])
    extend_([u'    function ajax_get_data(obj) {\n'])
    extend_([u'        alert("Buscando o c\xf3digo : " + obj.value);\n'])
    extend_([u'    }\n'])
    extend_([u'    function validate_fields(){\n'])
    extend_([u'        return false;\n'])
    extend_([u'    }\n'])
    extend_([u'    function only_integer(obj) {\n'])
    extend_([u'        if (isNumeric(obj.value)) {\n'])
    extend_([u'            return true;\n'])
    extend_([u'        } else {\n'])
    extend_([u'            return false;\n'])
    extend_([u'        }\n'])
    extend_([u'    } \n'])
    extend_([u'    function only_float(obj) {\n'])
    extend_([u'        return true;\n'])
    extend_([u'    }\n'])
    extend_([u'</script>\n'])

    return self

pedido = CompiledTemplate(pedido, 'templates/site/pedido.html')

def index (foto_itens, fotos_desc, destaques):
    __lineoffset__ = -3
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    self['title'] = join_(u'Enveloprint - Solu\xe7\xf5es Personalizadas em Envelopes.')
    self['full_description'] = join_(u'Ind\xfastria de fabrica\xe7\xe3o de envelopes.')
    self['keywords_tags'] = join_(u'envelopes, personalizados, fabrica\xe7\xe3o de envelopes')
    extend_([u'\n'])
    extend_([u'<link rel="stylesheet" type="text/css" media="screen" href="/static/css/galeria.css" />\n'])
    extend_([u'<script type="text/javascript" src="/static/javascript/jquery-1.3.2.min.js"></script>\n'])
    extend_([u'<script type="text/javascript" src="/static/javascript/jquery.easing.1.3.js"></script>\n'])
    extend_([u'<script type="text/javascript" src="/static/javascript/jquery.galleryview-1.1.js"></script>\n'])
    extend_([u'<script type="text/javascript" src="/static/javascript/jquery.timers-1.1.2.js"></script>\n'])
    extend_([u'<script type="text/javascript">\n'])
    extend_([u'    jQuery(document).ready(function(){\n'])
    extend_([u"        jQuery('#photos').galleryView({\n"])
    extend_([u'            panel_width: 576,\n'])
    extend_([u'            panel_height: 300,\n'])
    extend_([u'            transition_speed: 1500,\n'])
    extend_([u'            transition_interval: 5000,\n'])
    extend_([u"            nav_theme: 'dark',\n"])
    extend_([u"            border: '10px solid #eee',\n"])
    extend_([u'            pause_on_hover: true\n'])
    extend_([u'        });\n'])
    extend_([u'    });\n'])
    extend_([u'</script>\n'])
    extend_([u'\n'])
    extend_([u'<h3>Principais Produtos</h3>\n'])
    extend_([u'<div id="slide_content" style="">\n'])
    extend_([u'    <div class="wrap">\n'])
    extend_([u'        <div id="slide-holder">\n'])
    extend_([u'            <div id="slide-runner">\n'])
    for foto in loop.setup(foto_itens):
        extend_(['                ', u'<a href=""><img id="slide-img-', escape_(loop.index, True), u'" src="', escape_(foto.imagem_url, False), u'" class="slide" alt="" /></a>\n'])
    extend_([u'                <div id="slide-controls">\n'])
    extend_([u'                    <p id="slide-client" class="text"><strong class="no_background">Produto: </strong><span class="no_background"></span></p>\n'])
    extend_([u'                    <p id="slide-desc" class="text"></p>\n'])
    extend_([u'                    <p id="slide-nav"></p>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <script type="text/javascript">\n'])
    extend_([u'            if(!window.slider) var slider={};slider.data=[', escape_(fotos_desc, False), u'];\n'])
    extend_([u'        </script>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'\n'])
    if len(destaques)>0:
        extend_([u'<h3>Destaques / Lan\xe7amentos</h3>\n'])
        extend_([u'<div id="destaq_container">\n'])
        extend_([u'    <div id="photos" class="galleryview">\n'])
        for destaque in loop.setup(destaques):
            extend_(['        ', u'<div class="panel">\n'])
            extend_(['        ', u'    <img src="', escape_(destaque.foto_produto_01, False), u'" alt="Produto: ', escape_(destaque.codigo, False), u' | ', escape_(destaque.referencia, False), u'" title="Produto: ', escape_(destaque.codigo, False), u' | ', escape_(destaque.referencia, False), u'" />\n'])
            extend_(['        ', u'    <div class="panel-overlay">\n'])
            extend_(['        ', u'        <h2>Produto: ', escape_(destaque.codigo, False), u' - Refer\xeancia: ', escape_(destaque.referencia, False), u'</h2>\n'])
            extend_(['        ', u'        <!--p>', escape_(destaque.referencia[0:170], False), u'... <a href="/detalhar/locacao/', escape_(destaque.codigo, False), u'" class="photo_destaq">[Ver mais]</a></p-->\n'])
            extend_(['        ', u'    </div>\n'])
            extend_(['        ', u'    <div class="overlay"></div>\n'])
            extend_(['        ', u'</div>\n'])
        extend_([u'        <img class="nav-next" src="/static/images/next.png"><img class="nav-prev" src="/static/images/prev.png"><img class="nav-overlay" src="/static/images/panel-nav-next.png"><img class="nav-overlay_r" src="/static/images/panel-nav-prev.png">\n'])
        extend_([u'    </div>\n'])
        extend_([u'</div>\n'])

    return self

index = CompiledTemplate(index, 'templates/site/index.html')

