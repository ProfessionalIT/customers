# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descri\xe7\xe3o')),
                ('url_resource', models.CharField(max_length=200, null=True, verbose_name='Link/URL', blank=True)),
                ('upload_resource', models.FileField(upload_to='banners', null=True, verbose_name=b'Arquivo', blank=True)),
                ('action_resource', models.CharField(max_length=200, null=True, verbose_name='A\xe7\xe3o ao Clicar', blank=True)),
                ('ativo', models.BooleanField(default=False, verbose_name='Banner ativo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('tipo', models.CharField(default='E', max_length=1, verbose_name='Tipo', choices=[('E', 'Evento'), ('R', 'Recesso'), ('D', 'Festa'), ('F', 'Feriado'), ('P', 'Ponte')])),
                ('data_agendamento', models.DateTimeField(default=datetime.datetime(2015, 8, 1, 12, 22, 20, 432476), verbose_name='Data do Agendamento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(default='1', max_length=1, verbose_name='Tipo', choices=[('1', 'Ber\xe7\xe1rio 1'), ('2', 'Ber\xe7\xe1rio 2'), ('3', 'Crian\xe7as Maiores de 1 ano')])),
                ('mes', models.CharField(default=b'8', max_length=2, verbose_name='M\xeas', choices=[('01', 'Janeiro'), ('02', 'Fevereiro'), ('03', 'Mar\xe7o'), ('04', 'Abril'), ('05', 'Maio'), ('06', 'Junho'), ('07', 'Julho'), ('08', 'Agosto'), ('09', 'Setembro'), ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')])),
                ('ano', models.CharField(default=b'2015', max_length=4, verbose_name='Ano Letivo', choices=[('2013', '2013'), ('2014', '2014')])),
                ('cardapio_file', models.FileField(upload_to=b'cardapios', verbose_name=b'Card\xc3\xa1pio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConteudoDownload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o')),
                ('tipo', models.CharField(default='1', max_length=1, verbose_name='Tipo', choices=[('1', 'M\xfasica'), ('2', 'Pap\xe9l de Parede'), ('3', 'Desenho para Pintar'), ('4', 'Material de Apoio')])),
                ('miniatura', models.ImageField(upload_to='downloads', verbose_name='Miniatura')),
                ('conteudo_file', models.FileField(upload_to='downloads', verbose_name=b'Arquivo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Depoimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conteudo', models.TextField(verbose_name='Conte\xfado')),
                ('autor', models.CharField(max_length=200, verbose_name='Autor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('tipo', models.CharField(default='F', max_length=1, verbose_name='Tipo Galeria', choices=[('F', 'Foto'), ('V', 'V\xeddeo')])),
                ('descricao', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o')),
                ('mes', models.CharField(default=b'8', max_length=2, verbose_name='M\xeas', choices=[('01', 'Janeiro'), ('02', 'Fevereiro'), ('03', 'Mar\xe7o'), ('04', 'Abril'), ('05', 'Maio'), ('06', 'Junho'), ('07', 'Julho'), ('08', 'Agosto'), ('09', 'Setembro'), ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')])),
                ('ano', models.CharField(default=b'2015', max_length=4, verbose_name='Ano Letivo', choices=[('2013', '2013'), ('2014', '2014')])),
                ('destaque', models.BooleanField(default=False, verbose_name='Destaque')),
                ('permite_comentario', models.BooleanField(default=False, verbose_name='Permite Coment\xe1rio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GaleriaResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_resource', models.CharField(max_length=200, null=True, verbose_name='Link/URL', blank=True)),
                ('upload_resource', models.FileField(upload_to=b'galerias', null=True, verbose_name=b'Arquivo', blank=True)),
                ('action_resource', models.CharField(max_length=200, null=True, verbose_name='A\xe7\xe3o ao Clicar', blank=True)),
                ('galeria', models.ForeignKey(verbose_name='Galeria', to='website.Galeria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaterialEscolar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ano', models.CharField(default=b'2015', max_length=4, verbose_name='Ano Letivo', choices=[('2013', '2013'), ('2014', '2014')])),
                ('miniatura', models.ImageField(upload_to='material_escolar', verbose_name='Miniatura')),
                ('anexo_file', models.FileField(upload_to='material_escolar', verbose_name=b'Anexo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('endereco', models.CharField(max_length=200, verbose_name='endere\xe7o')),
                ('ordem', models.IntegerField(verbose_name='Ordem De Exibi\xe7\xe3o')),
                ('nivel', models.IntegerField(verbose_name='N\xedvel do Menu')),
                ('palavras_chaves', models.CharField(max_length=200, verbose_name='Palavras Chaves')),
                ('rascunho', models.BooleanField(default=True, verbose_name='Rascunho')),
                ('menu_pai', models.ForeignKey(related_name='Menu Pai', blank=True, to='website.Menu', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('conteudo', models.TextField(verbose_name='Conte\xfado')),
                ('palavras_chaves', models.CharField(max_length=200, verbose_name='Palavras Chaves')),
                ('permite_comentario', models.BooleanField(default=False, verbose_name='Permite Coment\xe1rio')),
                ('rascunho', models.BooleanField(default=True, verbose_name='Rascunho')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.CharField(max_length=200, verbose_name='Valor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('data_hora', models.DateTimeField(verbose_name='Data')),
                ('data_publicacao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Publica\xe7\xe3o')),
                ('palavras_chaves', models.CharField(max_length=200, verbose_name='Palavras Chaves')),
                ('tipos', models.CharField(default='1', max_length=1, verbose_name='Tipos', choices=[(b'A', b'Aviso'), (b'D', b'Dicas'), (b'N', b'Di\xc3\xa1rio Online')])),
                ('introducao', models.TextField(verbose_name='Introdu\xe7\xe3o')),
                ('completa', models.TextField(verbose_name='Conte\xfado')),
                ('miniatura_publicacao', models.ImageField(upload_to='publicacao', verbose_name='Miniatura')),
                ('destaque', models.BooleanField(default=False, verbose_name='Destaque')),
                ('permite_comentario', models.BooleanField(default=False, verbose_name='Permite Coment\xe1rio')),
                ('rascunho', models.BooleanField(default=True, verbose_name='Rascunho')),
                ('galeria', models.ForeignKey(verbose_name='Galeria', blank=True, to='website.Galeria', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recomendacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(default='1', max_length=1, verbose_name='Tipo', choices=[('1', 'Livro'), ('2', 'V\xeddeo'), ('3', 'M\xfasica'), ('4', 'Texto'), ('5', 'Link')])),
                ('descricao', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o')),
                ('acao_link', models.CharField(max_length=200, null=True, verbose_name='A\xe7\xe3o Link', blank=True)),
                ('miniatura', models.ImageField(upload_to='imagens', verbose_name='Miniatura')),
                ('destaque', models.BooleanField(default=False, verbose_name='Destaque')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('conteudo_programatico', models.TextField(verbose_name='Conte\xfado Program\xe1tico')),
                ('atividades_incluidas', models.TextField(verbose_name='Atividades Inclu\xeddas')),
                ('atividades_extras', models.TextField(verbose_name='Atividades Extras')),
                ('rotina_diaria', models.TextField(verbose_name='Rotina Di\xe1ria')),
                ('observacoes', models.TextField(verbose_name='Observa\xe7\xf5es')),
                ('professor', models.ForeignKey(verbose_name='Professor(a)', to='website.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='menu',
            name='pagina',
            field=models.ForeignKey(verbose_name='P\xe1gina', to='website.Pagina', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='materialescolar',
            name='servico',
            field=models.ForeignKey(verbose_name='Tipo', to='website.Servico'),
            preserve_default=True,
        ),
    ]
