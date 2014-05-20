# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AdoptionCandidate.self_introduction'
        db.add_column(u'animals_adoptioncandidate', 'self_introduction',
                      self.gf('django.db.models.fields.TextField')(default=u'Laudantium nemo totam itaque sint consequatur maxime culpa molestiae, ab quia architecto exercitationem quisquam dignissimos, dolore praesentium consequatur quia rem dicta molestiae cupiditate quam beatae inventore, nobis debitis veniam placeat illo distinctio eligendi. Praesentium hic accusantium tempora quis laborum recusandae quaerat temporibus suscipit obcaecati, architecto quasi voluptate, maxime et provident a sit voluptatibus culpa, eveniet impedit quae aliquam expedita aut.\nVero ea quos laudantium, obcaecati praesentium quod molestiae qui. Error et nam, deserunt deleniti repellendus necessitatibus non doloribus et impedit quia ullam sint. Voluptas repellendus optio nobis perferendis, ducimus architecto repellendus vero reiciendis alias voluptatem consequatur molestias cupiditate deserunt repellat, inventore iusto laudantium ut est maiores cum saepe repudiandae dolorum quas, asperiores commodi cupiditate consectetur necessitatibus corporis natus deserunt nihil architecto, harum rerum commodi et beatae repellat possimus natus voluptate quaerat?'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AdoptionCandidate.self_introduction'
        db.delete_column(u'animals_adoptioncandidate', 'self_introduction')


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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'self_introduction': ('django.db.models.fields.TextField', [], {'default': "u'Ipsum mollitia sit iusto nostrum animi non quisquam beatae hic earum nam, adipisci deleniti architecto placeat blanditiis id, recusandae quae molestiae fuga reiciendis id dolore blanditiis rem libero quia quo? Voluptate vitae cupiditate facere voluptas rem dolorum dolorem iste dicta quae, eos assumenda quis corrupti exercitationem fugit, nemo debitis voluptatem quidem in molestias porro culpa expedita, similique nemo inventore accusamus temporibus. Doloremque aliquid dolores, sunt doloribus saepe nobis eveniet delectus fuga nulla, consequatur sapiente non sint doloremque obcaecati suscipit autem laudantium?\\nObcaecati ipsa quos, saepe totam vel cumque numquam pariatur deserunt optio libero explicabo? Perferendis saepe animi praesentium? Vitae dolore provident velit nam optio architecto rem quidem vero, dolores molestiae tempora, quod tempora quas sequi quaerat excepturi odit vitae quidem, quisquam doloremque eius ratione architecto perferendis maxime qui? Incidunt iste ea iure ducimus deserunt modi repudiandae aperiam, eveniet error quas aliquam, reiciendis quidem a excepturi, laboriosam quam sunt commodi unde perferendis officia maxime debitis beatae est, placeat ipsa voluptatem itaque quasi?'"}),
            'sex': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'animals.breed': {
            'Meta': {'ordering': "['-species__name', 'name']", 'object_name': 'Breed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animals.Species']"})
        },
        u'animals.species': {
            'Meta': {'object_name': 'Species'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['animals']