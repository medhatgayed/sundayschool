# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table('core_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('landline', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('emaiil', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('core', ['Contact'])

        # Adding model 'Servant'
        db.create_table('core_servant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Contact'])),
            ('sunday_school_class', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('book', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Servant'])

        # Adding model 'Child'
        db.create_table('core_child', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Contact'])),
            ('dob', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('school_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('sunday_school_class', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Child'])

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


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table('core_contact')

        # Deleting model 'Servant'
        db.delete_table('core_servant')

        # Deleting model 'Child'
        db.delete_table('core_child')

        # Deleting model 'ServantAttendance'
        db.delete_table('core_servantattendance')


    models = {
        'core.child': {
            'Meta': {'object_name': 'Child'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Contact']"}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sunday_school_class': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'emaiil': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'core.servant': {
            'Meta': {'object_name': 'Servant'},
            'book': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sunday_school_class': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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