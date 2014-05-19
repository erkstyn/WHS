# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Species.slug'
        db.add_column(u'animals_species', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='test', max_length=50),
                      keep_default=False)

        # Adding field 'Breed.slug'
        db.add_column(u'animals_breed', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='test', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Species.slug'
        db.delete_column(u'animals_species', 'slug')

        # Deleting field 'Breed.slug'
        db.delete_column(u'animals_breed', 'slug')


    models = {
        u'animals.adoptioncandidate': {
            'Meta': {'ordering': "['-published']", 'object_name': 'AdoptionCandidate'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'available_on': ('django.db.models.fields.DateTimeField', [], {}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'breed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animals.Breed']"}),
            'good_with_kids': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'good_with_pets': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_shots': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'neutered': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'animals.breed': {
            'Meta': {'ordering': "['-species__name', 'name']", 'object_name': 'Breed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animals.Species']"})
        },
        u'animals.species': {
            'Meta': {'object_name': 'Species'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['animals']