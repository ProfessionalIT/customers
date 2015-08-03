from django.conf.urls import patterns, url
from website import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^empresa/(?P<slug>\S+)$', views.empresa, name='empresa'),
    url(r'^empresa-historia/$', views.historia, name='historia'),
)
