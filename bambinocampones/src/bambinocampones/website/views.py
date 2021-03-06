from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from . import models
from .forms import DepoimentoForm


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
        order_by('-data_hora')[0:10]

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


def responsabilidade_social(request):
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

    pagina = models.Pagina.objects.get(slug='responsabilidade-social')
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

    return render(request, 'depoimentos.html',
                  {'banners': banners,
                   'calendarios': calendarios,
                   'dicas': dicas,
                   'fotos': fotos,
                   'videos': videos,
                   'material_apoio': material_apoio,
                   'depoimentos': depoimentos})


def depoimento(request):
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
    if request.method == 'POST':
        form = DepoimentoForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/agradece-depoimento')
    else:
        depoimento_form = DepoimentoForm()

    return render(request, 'depoimento.html',
                  {'banners': banners,
                   'calendarios': calendarios,
                   'dicas': dicas,
                   'fotos': fotos,
                   'videos': videos,
                   'material_apoio': material_apoio,
                   'depoimento_form': depoimento_form})



def agradece_depoimento(request):
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

    pagina = models.Pagina.objects.get(slug='agradece-depoimento')
    return render(request, 'pagina.html', {'banners': banners,
                                           'calendarios': calendarios,
                                           'dicas': dicas,
                                           'fotos': fotos,
                                           'videos': videos,
                                           'material_apoio': material_apoio,
                                           'depoimentos': depoimentos,
                                           'pagina': pagina})

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


def uniforme(request):
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

    pagina = models.Pagina.objects.get(slug='uniforme')
    return render(request, 'pagina.html', {'banners': banners,
                                           'calendarios': calendarios,
                                           'dicas': dicas,
                                           'fotos': fotos,
                                           'videos': videos,
                                           'material_apoio': material_apoio,
                                           'depoimentos': depoimentos,
                                           'pagina': pagina})


def determinacoes(request):
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

    pagina = models.Pagina.objects.get(slug='determinacoes')
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
    return render(request, 'cardapios.html',
                  {'banners': banners,
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

    return render(request, 'avisos_importantes.html',
                  {'banners': banners,
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


def noticias(request):
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
    noticias = models.Publicacao.objects.filter(tipos=u'N',
                                                rascunho=False)

    return render(request, 'noticias.html', {'banners': banners,
                                             'calendarios': calendarios,
                                             'dicas': dicas,
                                             'fotos': fotos,
                                             'videos': videos,
                                             'material_apoio': material_apoio,
                                             'depoimentos': depoimentos,
                                             'noticias': noticias,
                                             'titulo': 'Noticias da Bambino'})


def dicas(request):
    banners = models.Banner.objects.filter(ativo=True)
    calendarios = serializers.serialize('json', models.Calendario.objects.all())
    dicas = models.Publicacao.objects.filter(tipos=u'D',
                                             rascunho=False,
                                             destaque=True).\
        order_by('data_publicacao')[0:10]
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


def publicacao(request, slug):
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

    publicacao = models.Publicacao.objects.get(slug=slug, rascunho=False)
    return render(request, 'publicacao.html', {'banners': banners,
                                               'calendarios': calendarios,
                                               'dicas': dicas,
                                               'fotos': fotos,
                                               'videos': videos,
                                               'material_apoio': material_apoio,
                                               'depoimentos': depoimentos,
                                               'publicacao': publicacao})


def materiais_apoio(request):
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
    lista_material_apoio = models.Recomendacao.objects.all().order_by('tipo')

    return render(request, 'materiais_apoio.html',
                  {'banners': banners,
                   'calendarios': calendarios,
                   'dicas': dicas,
                   'fotos': fotos,
                   'videos': videos,
                   'material_apoio': material_apoio,
                   'depoimentos': depoimentos,
                   'lista_material_apoio': lista_material_apoio,
                   'titulo': 'Materias de Apoio'})


def material_apoio(request, slug):
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

    publicacao = models.Publicacao.objects.get(slug=slug, rascunho=False)
    return render(request, 'publicacao.html', {'banners': banners,
                                               'calendarios': calendarios,
                                               'dicas': dicas,
                                               'fotos': fotos,
                                               'videos': videos,
                                               'material_apoio': material_apoio,
                                               'depoimentos': depoimentos,
                                               'publicacao': publicacao})


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
    lista_fotos = models.Galeria.objects.filter(tipo=u'F').order_by('-ano',
                                                                    '-mes')

    return render(request, 'fotos.html', {'banners': banners,
                                          'calendarios': calendarios,
                                          'dicas': dicas,
                                          'fotos': fotos,
                                          'videos': videos,
                                          'material_apoio': material_apoio,
                                          'depoimentos': depoimentos,
                                          'lista_fotos': lista_fotos,
                                          'titulo': 'Galeria de Fotos'})


def foto(request, slug):
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

    galeria = models.Galeria.objects.get(slug=slug)
    fotos = galeria.galeriaresource_set.all()
    return render(request, 'recursos.html', {'banners': banners,
                                             'calendarios': calendarios,
                                             'dicas': dicas,
                                             'fotos': fotos,
                                             'videos': videos,
                                             'material_apoio': material_apoio,
                                             'depoimentos': depoimentos,
                                             'titulo': galeria.titulo,
                                             'recursos': fotos})


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
    lista_videos = models.Galeria.objects.filter(tipo=u'V')

    return render(request, 'videos.html', {'banners': banners,
                                           'calendarios': calendarios,
                                           'dicas': dicas,
                                           'fotos': fotos,
                                           'videos': videos,
                                           'material_apoio': material_apoio,
                                           'depoimentos': depoimentos,
                                           'lista_videos': lista_videos,
                                           'titulo': u'Galeria de Videos'})


def video(request, slug):
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

    galeria = models.Galeria.objects.get(slug=slug)
    videos = galeria.galeriaresource_set.all()
    return render(request, 'recursos.html', {'banners': banners,
                                             'calendarios': calendarios,
                                             'dicas': dicas,
                                             'fotos': fotos,
                                             'videos': videos,
                                             'material_apoio': material_apoio,
                                             'depoimentos': depoimentos,
                                             'titulo': galeria.titulo,
                                             'recursos': videos})


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
    agradecimento = None
    if request.POST:
        from_address = 'bambino@bambinocampones.com.br'
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        assunto = request.POST['assunto']
        messagem = request.POST['mensagem_adicional']
        
        complete_message = '''
            A pessoa %(nome)s com o telefone %(telefone)s e o e-mail
            %(email)s deixou o seguinte recado: %(messagem)s .
        ''' % {'nome': nome,
               'telefone': telefone,
               'email': email,
               'messagem': messagem}
                
        send_mail(assunto,
                  complete_message,
                  from_address,
                  ['bambino@bambinocampones.com.br'],
                  fail_silently=False)
        agradecimento = 'Sua mensagem foi enviada com SUCESSO !'

    return render(request,
                  'contato.html',
                  {'banners': banners,
                   'calendarios': calendarios,
                   'dicas': dicas,
                   'fotos': fotos,
                   'videos': videos,
                   'material_apoio': material_apoio,
                   'depoimentos': depoimentos,
                   'titulo': 'Deixe seu recado',
                   'agradecimento': agradecimento})
