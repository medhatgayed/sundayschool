# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Servant'
        db.create_table('core_servant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('core', ['Servant'])

        # Adding model 'ServantYear'
        db.create_table('core_servantyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Servant'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('sunday_school_class', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('book', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['ServantYear'])

        # Adding model 'ServantAttendance'
        db.create_table('core_servantattendance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Servant'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('attended_mass', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('attended_meeting', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('attended_sunday_school', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['ServantAttendance'])

        # Adding model 'Child'
        db.create_table('core_child', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('father_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('father_mobile', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('father_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('mother_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('mother_mobile', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('mother_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('core', ['Child'])

        # Adding model 'ChildYear'
        db.create_table('core_childyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('child', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Child'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('sunday_school_class', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('book', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('school_year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['ChildYear'])


    def backwards(self, orm):
        # Deleting model 'Servant'
        db.delete_table('core_servant')

        # Deleting model 'ServantYear'
        db.delete_table('core_servantyear')

        # Deleting model 'ServantAttendance'
        db.delete_table('core_servantattendance')

        # Deleting model 'Child'
        db.delete_table('core_child')

        # Deleting model 'ChildYear'
        db.delete_table('core_childyear')


    models = {
        'core.child': {
            'Meta': {'object_name': 'Child'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'father_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'father_mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'mother_mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mother_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'core.childyear': {
            'Meta': {'object_name': 'ChildYear'},
            'book': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'child': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Child']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school_year': ('django.db.models.fields.IntegerField', [], {}),
            'sunday_school_class': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.servant': {
            'Meta': {'object_name': 'Servant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'core.servantattendance': {
            'Meta': {'object_name': 'ServantAttendance'},
            'attended_mass': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attended_meeting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attended_sunday_school': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Servant']"})
        },
        'core.servantyear': {
            'Meta': {'object_name': 'ServantYear'},
            'book': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Servant']"}),
            'sunday_school_class': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']