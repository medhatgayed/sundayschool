# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ChildYear'
        db.delete_table('core_childyear')

        # Deleting model 'ServantYear'
        db.delete_table('core_servantyear')


    def backwards(self, orm):
        # Adding model 'ChildYear'
        db.create_table('core_childyear', (
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('school_year', self.gf('django.db.models.fields.IntegerField')()),
            ('book', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('child', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Child'])),
            ('sunday_school_class', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['ChildYear'])

        # Adding model 'ServantYear'
        db.create_table('core_servantyear', (
            ('servant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Servant'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('sunday_school_class', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('book', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['ServantYear'])


    models = {
        'core.child': {
            'Meta': {'object_name': 'Child'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'book': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'father_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'father_mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'mother_mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mother_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'school_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_school_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.servant': {
            'Meta': {'object_name': 'Servant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'book': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sunday_school_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.servantattendance': {
            'Meta': {'object_name': 'ServantAttendance'},
            'attended_mass': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attended_meeting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attended_sunday_school': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Servant']"})
        }
    }

    complete_apps = ['core']