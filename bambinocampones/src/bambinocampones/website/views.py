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


def depoimentos(request):
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
    depoimentos = models.Depoimento.objects.all()

    return render(request, 'depoimentos.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos})


def matriculas(request):
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

    pagina = models.Pagina.objects.get(slug='matriculas')
    return render(request, 'pagina.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'pagina': pagina})


def material_escolar(request):
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

    pagina = models.Pagina.objects.get(slug='material-escolar')
    return render(request, 'pagina.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'pagina': pagina})


def cardapio(request):
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
    cardapios = models.Cardapio.objects.all()
    return render(request, 'cardapios.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'cardapios': cardapios})


def avisos_importantes(request):
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
    avisos = models.Publicacao.objects.filter(tipos=u'A',
                                              rascunho=False)

    return render(request, 'avisos_importantes.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'avisos': avisos,
                                          'titulo': 'Pagina Inicial'})


def eventos(request):
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
    eventos = models.Publicacao.objects.filter(tipos=u'E',
                                              rascunho=False)

    return render(request, 'eventos.html', {'banners': banners,
                                            'calendarios': calendarios,
                                            'dicas': dicas,
                                            'fotos': fotos,
                                            'videos': videos,
                                            'material_apoio': material_apoio,
                                            'depoimentos': depoimentos,
                                            'eventos': eventos,
                                            'titulo': 'Eventos na Bambino'})


def dicas(request):
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
    lista_dicas = models.Publicacao.objects.filter(tipos=u'D',
                                                   rascunho=False)

    return render(request, 'dicas.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'lista_dicas': lista_dicas,
                                          'titulo': 'Dicas educacionais'})


def galerias_foto(request):
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
    lista_fotos = models.Galeria.objects.filter(tipos=u'F',
                                                rascunho=False)

    return render(request, 'fotos.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'lista_fotos': lista_fotos,
                                          'titulo': 'Galeria de Fotos'})


def galerias_video(request):
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
    lista_videos = models.Galeria.objects.filter(tipos=u'V',
                                                 rascunho=False)

    return render(request, 'videos.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'lista_videos': lista_videos,
                                          'titulo': 'Galeria de Vídeos'})


def servicos(request, slug):
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


def downloads(request, slug):
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


def contato(request, slug):
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
