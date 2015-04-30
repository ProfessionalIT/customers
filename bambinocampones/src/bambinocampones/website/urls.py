from django.conf.urls import patterns, url
from website import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^empresa-filosofia/$', views.empresa, name='empresa'),
)
