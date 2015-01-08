# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Galeria.foi_importante'
        db.add_column(u'website_galeria', 'foi_importante',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Galeria.foi_importante'
        db.delete_column(u'website_galeria', 'foi_importante')


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
            'foi_importante': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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