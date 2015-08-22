from django.contrib.syndication.views import Feed
from models import Publicacao


class UltimasPublicacoes(Feed):
    title = "Ultimas Publicacoes"
    link = "/"

    def items(self):
        return Publicacao.objects.filter(rascunho=False)

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.introducao


