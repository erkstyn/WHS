# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BoardMember.photo'
        db.alter_column(u'board_members_boardmember', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'BoardMember.photo'
        db.alter_column(u'board_members_boardmember', 'photo', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

    models = {
        u'board_members.boardmember': {
            'Meta': {'ordering': "['order']", 'object_name': 'BoardMember'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['board_members']