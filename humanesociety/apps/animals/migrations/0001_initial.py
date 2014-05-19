# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Species'
        db.create_table(u'animals_species', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'animals', ['Species'])

        # Adding model 'Breed'
        db.create_table(u'animals_breed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animals.Species'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'animals', ['Breed'])

        # Adding model 'AdoptionCandidate'
        db.create_table(u'animals_adoptioncandidate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('breed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animals.Breed'])),
            ('sex', self.gf('django.db.models.fields.IntegerField')()),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('neutered', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('has_shots', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('available_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('published', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('good_with_pets', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('good_with_kids', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'animals', ['AdoptionCandidate'])

    def backwards(self, orm):
        # Deleting model 'Species'
        db.delete_table(u'animals_species')

        # Deleting model 'Breed'
        db.delete_table(u'animals_breed')

        # Deleting model 'AdoptionCandidate'
        db.delete_table(u'animals_adoptioncandidate')


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
