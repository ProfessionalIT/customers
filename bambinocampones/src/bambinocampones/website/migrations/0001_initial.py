# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calendario'
        db.create_table(u'website_calendario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default=u'E', max_length=1)),
            ('data_agendamento', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 12, 4, 0, 0))),
        ))
        db.send_create_signal(u'website', ['Calendario'])

        # Adding model 'Cardapio'
        db.create_table(u'website_cardapio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default=u'1', max_length=1)),
            ('mes', self.gf('django.db.models.fields.CharField')(default='12', max_length=2)),
            ('ano', self.gf('django.db.models.fields.CharField')(default='2013', max_length=4)),
            ('cardapio_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['Cardapio'])

        # Adding model 'Galeria'
        db.create_table(u'website_galeria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default=u'F', max_length=1)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mes', self.gf('django.db.models.fields.CharField')(default='12', max_length=2)),
            ('ano', self.gf('django.db.models.fields.CharField')(default='2013', max_length=4)),
            ('destaque', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('permite_comentario', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'website', ['Galeria'])

        # Adding model 'GaleriaResource'
        db.create_table(u'website_galeriaresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Galeria'])),
            ('url_resource', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('upload_resource', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('action_resource', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['GaleriaResource'])

        # Adding model 'Publicacao'
        db.create_table(u'website_publicacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('data_hora', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_publicacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('palavras_chaves', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipos', self.gf('django.db.models.fields.CharField')(default=u'1', max_length=1)),
            ('introducao', self.gf('django.db.models.fields.TextField')()),
            ('completa', self.gf('django.db.models.fields.TextField')()),
            ('miniatura_publicacao', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Galeria'], null=True, blank=True)),
            ('destaque', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('permite_comentario', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rascunho', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'website', ['Publicacao'])

        # Adding model 'Pagina'
        db.create_table(u'website_pagina', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('conteudo', self.gf('django.db.models.fields.TextField')()),
            ('palavras_chaves', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('permite_comentario', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rascunho', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'website', ['Pagina'])

        # Adding model 'Menu'
        db.create_table(u'website_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ordem', self.gf('django.db.models.fields.IntegerField')()),
            ('nivel', self.gf('django.db.models.fields.IntegerField')()),
            ('pagina', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Pagina'], null=True)),
            ('menu_pai', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'Menu Pai', null=True, to=orm['website.Menu'])),
            ('palavras_chaves', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rascunho', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'website', ['Menu'])

        # Adding model 'Depoimento'
        db.create_table(u'website_depoimento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conteudo', self.gf('django.db.models.fields.TextField')()),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'website', ['Depoimento'])

        # Adding model 'Professor'
        db.create_table(u'website_professor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'website', ['Professor'])

        # Adding model 'Servico'
        db.create_table(u'website_servico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('professor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Professor'])),
            ('conteudo_programatico', self.gf('django.db.models.fields.TextField')()),
            ('atividades_incluidas', self.gf('django.db.models.fields.TextField')()),
            ('atividades_extras', self.gf('django.db.models.fields.TextField')()),
            ('rotina_diaria', self.gf('django.db.models.fields.TextField')()),
            ('observacoes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'website', ['Servico'])

        # Adding model 'MaterialEscolar'
        db.create_table(u'website_materialescolar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ano', self.gf('django.db.models.fields.CharField')(default='2013', max_length=4)),
            ('servico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Servico'])),
            ('miniatura', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('anexo_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['MaterialEscolar'])

        # Adding model 'ConteudoDownload'
        db.create_table(u'website_conteudodownload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default=u'1', max_length=1)),
            ('miniatura', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('conteudo_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['ConteudoDownload'])

        # Adding model 'Recomendacao'
        db.create_table(u'website_recomendacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default=u'1', max_length=1)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('acao_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('miniatura', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('destaque', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'website', ['Recomendacao'])

        # Adding model 'Parametro'
        db.create_table(u'website_parametro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'website', ['Parametro'])


    def backwards(self, orm):
        # Deleting model 'Calendario'
        db.delete_table(u'website_calendario')

        # Deleting model 'Cardapio'
        db.delete_table(u'website_cardapio')

        # Deleting model 'Galeria'
        db.delete_table(u'website_galeria')

        # Deleting model 'GaleriaResource'
        db.delete_table(u'website_galeriaresource')

        # Deleting model 'Publicacao'
        db.delete_table(u'website_publicacao')

        # Deleting model 'Pagina'
        db.delete_table(u'website_pagina')

        # Deleting model 'Menu'
        db.delete_table(u'website_menu')

        # Deleting model 'Depoimento'
        db.delete_table(u'website_depoimento')

        # Deleting model 'Professor'
        db.delete_table(u'website_professor')

        # Deleting model 'Servico'
        db.delete_table(u'website_servico')

        # Deleting model 'MaterialEscolar'
        db.delete_table(u'website_materialescolar')

        # Deleting model 'ConteudoDownload'
        db.delete_table(u'website_conteudodownload')

        # Deleting model 'Recomendacao'
        db.delete_table(u'website_recomendacao')

        # Deleting model 'Parametro'
        db.delete_table(u'website_parametro')


    models = {
        u'website.calendario': {
            'Meta': {'object_name': 'Calendario'},
            'data_agendamento': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 12, 4, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'E'", 'max_length': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'website.cardapio': {
            'Meta': {'object_name': 'Cardapio'},
            'ano': ('django.db.models.fields.CharField', [], {'default': "'2013'", 'max_length': '4'}),
            'cardapio_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.CharField', [], {'default': "'12'", 'max_length': '2'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'1'", 'max_length': '1'})
        },
        u'website.conteudodownload': {
            'Meta': {'object_name': 'ConteudoDownload'},
            'conteudo_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miniatura': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'1'", 'max_length': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'website.depoimento': {
            'Meta': {'object_name': 'Depoimento'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'conteudo': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'website.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'ano': ('django.db.models.fields.CharField', [], {'default': "'2013'", 'max_length': '4'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.CharField', [], {'default': "'12'", 'max_length': '2'}),
            'permite_comentario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'F'", 'max_length': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'website.galeriaresource': {
            'Meta': {'object_name': 'GaleriaResource'},
            'action_resource': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Galeria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'upload_resource': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url_resource': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'website.materialescolar': {
            'Meta': {'object_name': 'MaterialEscolar'},
            'anexo_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'ano': ('django.db.models.fields.CharField', [], {'default': "'2013'", 'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miniatura': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'servico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Servico']"})
        },
        u'website.menu': {
            'Meta': {'object_name': 'Menu'},
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_pai': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'Menu Pai'", 'null': 'True', 'to': u"orm['website.Menu']"}),
            'nivel': ('django.db.models.fields.IntegerField', [], {}),
            'ordem': ('django.db.models.fields.IntegerField', [], {}),
            'pagina': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Pagina']", 'null': 'True'}),
            'palavras_chaves': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rascunho': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'website.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'conteudo': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palavras_chaves': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'permite_comentario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rascunho': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'website.parametro': {
            'Meta': {'object_name': 'Parametro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'website.professor': {
            'Meta': {'object_name': 'Professor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'website.publicacao': {
            'Meta': {'object_name': 'Publicacao'},
            'completa': ('django.db.models.fields.TextField', [], {}),
            'data_hora': ('django.db.models.fields.DateTimeField', [], {}),
            'data_publicacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Galeria']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introducao': ('django.db.models.fields.TextField', [], {}),
            'miniatura_publicacao': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'palavras_chaves': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'permite_comentario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rascunho': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'tipos': ('django.db.models.fields.CharField', [], {'default': "u'1'", 'max_length': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'website.recomendacao': {
            'Meta': {'object_name': 'Recomendacao'},
            'acao_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miniatura': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'1'", 'max_length': '1'})
        },
        u'website.servico': {
            'Meta': {'object_name': 'Servico'},
            'atividades_extras': ('django.db.models.fields.TextField', [], {}),
            'atividades_incluidas': ('django.db.models.fields.TextField', [], {}),
            'conteudo_programatico': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacoes': ('django.db.models.fields.TextField', [], {}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Professor']"}),
            'rotina_diaria': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['website']