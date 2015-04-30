from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")


def empresa(request):
    return HttpResponse("Empresa e Filosofia")
