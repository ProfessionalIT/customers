from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.views.generic import TemplateView

from . import models


class Home(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        return context


def index(request):
    banners = models.Banner.objects.filter(ativo=True)
    calendarios = serializers.serialize('json', models.Calendario.objects.all())
    dicas = models.Publicacao.objects.filter(tipos=u'D',
                                             rascunho=False,
                                             destaque=True).\
        order_by('-data_publicacao')[0:10]
    fotos = models.Galeria.objects.filter(tipo=u'F',
                                          destaque=True)[0].\
        galeriaresource_set.filter()[:1].get()
    videos = models.Galeria.objects.filter(tipo=u'V',
                                           destaque=True)[0].\
        galeriaresource_set.filter()[:1].get()
    material_apoio = models.Recomendacao.objects.filter(destaque=True)
    depoimentos = models.Depoimento.objects.all()[0:5]
    destaques = models.Publicacao.objects.filter(tipos=u'N',
                                                 rascunho=False,
                                                 destaque=True).\
        order_by('-data_publicacao')[0:10]

    return render(request, 'index.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'destaques': destaques,
                                          'titulo': 'Pagina Inicial'})


def empresa(request, slug):
    banners = models.Banner.objects.filter(ativo=True)
    calendarios = serializers.serialize('json', models.Calendario.objects.all())
    dicas = models.Publicacao.objects.filter(tipos=u'D',
                                             rascunho=False,
                                             destaque=True).\
        order_by('-data_publicacao')[0:10]
    fotos = models.Galeria.objects.filter(tipo=u'F',
                                          destaque=True)[0].\
        galeriaresource_set.filter()[:1].get()
    videos = models.Galeria.objects.filter(tipo=u'V',
                                           destaque=True)[0].\
        galeriaresource_set.filter()[:1].get()
    material_apoio = models.Recomendacao.objects.filter(destaque=True)
    depoimentos = models.Depoimento.objects.all()[0:5]

    pagina = models.Pagina.objects.get(slug=slug)
    
    return render(request, 'pagina.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'pagina': pagina})


def historia(request):
    return HttpResponse("Historia da Empresa")
