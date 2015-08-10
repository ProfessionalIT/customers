from django.conf.urls import patterns, url
from website import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^empresa/(?P<slug>\S+)$', views.empresa, name='empresa'),
    url(r'^depoimentos/$', views.depoimentos, name='depoimentos'),
    url(r'^matriculas/$', views.matriculas, name='matriculas'),
    url(r'^material-escolar/$', views.material_escolar,
        name='material_escolar'),
    url(r'^cardapio/$', views.cardapio, name='cardapio'),
    url(r'^avisos-importantes/$', views.avisos_importantes,
        name='avisos_importantes'),
    url(r'^eventos/$', views.eventos, name='eventos'),
    url(r'^dicas/$', views.dicas, name='dicas'),
    url(r'^galerias-foto/$', views.galerias_foto, name='galerias_foto'),
    url(r'^galerias-video/$', views.galerias_video, name='galerias_video'),
    url(r'^servicos/(?P<slug>\S+)$', views.servicos, name='servicos'),
    url(r'^downloads/(?P<slug>\S+)$', views.downloads, name='downloads'),
    url(r'^contato/(?P<slug>\S+)$', views.contato, name='contato'),
)
