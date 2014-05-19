# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

import json
import os

class Migration(DataMigration):

    def forwards(self, orm):
        path = os.path.dirname(__file__)
        path = os.path.join(path, '..', 'fixtures', 'breeds.json')
        path = os.path.realpath(path)

        with open(path, 'r') as json_input:
            all_info = json.loads(json_input.read())
            
            for info in all_info:
                model = orm[info['model']]
                
                if model is orm.Breed:
                    info['fields']['species'] = orm.Species.objects.get(pk=info['fields']['species'])                
                model(**info['fields']).save()
            
    def backwards(self, orm):
        pass

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
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animals.Species']"})
        },
        u'animals.species': {
            'Meta': {'object_name': 'Species'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['animals']
    symmetrical = True
