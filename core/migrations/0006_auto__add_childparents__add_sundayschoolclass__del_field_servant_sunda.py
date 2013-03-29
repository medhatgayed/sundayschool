# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChildParents'
        db.create_table('core_childparents', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('father_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('father_mobile', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('father_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('mother_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('mother_mobile', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('mother_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('core', ['ChildParents'])

        # Adding model 'SundaySchoolClass'
        db.create_table('core_sundayschoolclass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('book', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('core', ['SundaySchoolClass'])

        # Deleting field 'Servant.sunday_school_class'
        db.delete_column('core_servant', 'sunday_school_class')

        # Deleting field 'Child.sunday_school_class'
        db.delete_column('core_child', 'sunday_school_class')

        # Adding field 'Child.child_parents'
        db.add_column('core_child', 'child_parents',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ChildParents'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ChildParents'
        db.delete_table('core_childparents')

        # Deleting model 'SundaySchoolClass'
        db.delete_table('core_sundayschoolclass')

        # Adding field 'Servant.sunday_school_class'
        db.add_column('core_servant', 'sunday_school_class',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Child.sunday_school_class'
        db.add_column('core_child', 'sunday_school_class',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Child.child_parents'
        db.delete_column('core_child', 'child_parents_id')


    models = {
        'core.child': {
            'Meta': {'object_name': 'Child'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'book': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'child_parents': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ChildParents']", 'null': 'True', 'blank': 'True'}),
            'curriculum_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.childparents': {
            'Meta': {'object_name': 'ChildParents'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'father_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'father_mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'mother_mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mother_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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
        },
        'core.sundayschoolclass': {
            'Meta': {'object_name': 'SundaySchoolClass'},
            'book': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['core']