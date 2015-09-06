from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
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


class GaleriaResourceInline(admin.StackedInline):
    model = GaleriaResource


class GaleriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    inlines = [GaleriaResourceInline, ]


class PublicacaoAdminForm(forms.ModelForm):
    introducao = forms.CharField(widget=CKEditorWidget())
    completa = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Publicacao


class PublicacaoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    form = PublicacaoAdminForm


class PaginaAdminForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Pagina


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'palavras_chaves',)
    prepopulated_fields = {"slug": ("titulo",)}
    form = PaginaAdminForm


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
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Depoimento)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(MaterialEscolar)
admin.site.register(ConteudoDownload, ConteudoDownloadAdmin)
admin.site.register(Recomendacao)
