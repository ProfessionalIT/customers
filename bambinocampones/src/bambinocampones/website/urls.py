from django.conf.urls import patterns, url
from website import views
from website import feeds

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'rss/$', feeds.UltimasPublicacoes()),
    url(r'^index/$', views.index, name='index'),
    url(r'^empresa/(?P<slug>\S+)$', views.empresa, name='empresa'),
    url(r'^depoimentos/$', views.depoimentos, name='depoimentos'),
    url(r'^depoimento/$', views.depoimento, name='depoimento'),
    url(r'^agradece-depoimento/$',
        views.agradece_depoimento, name='agradece-depoimento'),
    url(r'^matriculas/$', views.matriculas, name='matriculas'),
    url(r'^uniforme/$', views.uniforme, name='uniforme'),
    url(r'^determinacoes/$', views.determinacoes, name='determinacoes'),
    url(r'^material-escolar/$', views.material_escolar,
        name='material_escolar'),
    url(r'^cardapio/$', views.cardapio, name='cardapio'),
    url(r'^avisos-importantes/$', views.avisos_importantes,
        name='avisos_importantes'),
    url(r'^eventos/$', views.eventos, name='eventos'),
    url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^dicas/$', views.dicas, name='dicas'),
    url(r'^dica/(?P<slug>\S+)$', views.publicacao, name='dica'),
    url(r'^materiais-apoio/$', views.materiais_apoio, name='materiais_apoio'),
    url(r'^material_apoio/(?P<slug>\S+)$', views.material_apoio,
        name='material_apoio'),
    url(r'^responsabilidade-social/$', views.responsabilidade_social,
        name='responsabilidade_social'),
    url(r'^publicacao/(?P<slug>\S+)$', views.publicacao, name='publicacao'),
    url(r'^noticia/(?P<slug>\S+)$', views.publicacao, name='noticia'),
    url(r'^evento/(?P<slug>\S+)$', views.publicacao, name='evento'),
    url(r'^aviso/(?P<slug>\S+)$', views.publicacao, name='aviso'),
    url(r'^galeria-fotos/$', views.galerias_foto, name='galerias_foto'),
    url(r'^foto/(?P<slug>\S+)$', views.foto, name='foto'),
    url(r'^galeria-videos/$', views.galerias_video, name='galerias_video'),
    url(r'^video/(?P<slug>\S+)$', views.video, name='video'),
    url(r'^servicos/(?P<slug>\S+)$', views.servicos, name='servicos'),
    url(r'^downloads/(?P<slug>\S+)$', views.downloads, name='downloads'),
    url(r'^contato/(?P<slug>\S+)$', views.contato, name='contato'),
)
