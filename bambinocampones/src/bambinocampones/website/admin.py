from django.contrib import admin
from website.models import (Banner,
                            Calendario,
                            Cardapio,
                            Galeria,
                            GaleriaResource,
                            Publicacao,
                            Pagina,
                            Menu,
                            Depoimento,
                            Professor,
                            Servico,
                            MaterialEscolar,
                            ConteudoDownload,
                            Recomendacao)


class BannerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


class CalendarioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


class GaleriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


class PublicacaoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


class PaginaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


class ProfessorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


class ServicoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


class ConteudoDownloadAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


admin.site.register(Banner, BannerAdmin)
admin.site.register(Calendario, CalendarioAdmin)
admin.site.register(Cardapio)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(GaleriaResource)
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Depoimento)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(MaterialEscolar)
admin.site.register(ConteudoDownload, ConteudoDownloadAdmin)
admin.site.register(Recomendacao)
