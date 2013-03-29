# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Servant.year'
        db.delete_column('core_servant', 'year')

        # Deleting field 'Servant.book'
        db.delete_column('core_servant', 'book')

        # Deleting field 'Child.father_name'
        db.delete_column('core_child', 'father_name')

        # Deleting field 'Child.phone'
        db.delete_column('core_child', 'phone')

        # Deleting field 'Child.father_email'
        db.delete_column('core_child', 'father_email')

        # Deleting field 'Child.year'
        db.delete_column('core_child', 'year')

        # Deleting field 'Child.mother_mobile'
        db.delete_column('core_child', 'mother_mobile')

        # Deleting field 'Child.address'
        db.delete_column('core_child', 'address')

        # Deleting field 'Child.mother_email'
        db.delete_column('core_child', 'mother_email')

        # Deleting field 'Child.father_mobile'
        db.delete_column('core_child', 'father_mobile')

        # Deleting field 'Child.book'
        db.delete_column('core_child', 'book')

        # Deleting field 'Child.mother_name'
        db.delete_column('core_child', 'mother_name')


    def backwards(self, orm):
        # Adding field 'Servant.year'
        db.add_column('core_servant', 'year',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Servant.book'
        db.add_column('core_servant', 'book',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Child.father_name'
        db.add_column('core_child', 'father_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Child.phone'
        db.add_column('core_child', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Child.father_email'
        db.add_column('core_child', 'father_email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'Child.year'
        db.add_column('core_child', 'year',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Child.mother_mobile'
        db.add_column('core_child', 'mother_mobile',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Child.address'
        db.add_column('core_child', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Child.mother_email'
        db.add_column('core_child', 'mother_email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'Child.father_mobile'
        db.add_column('core_child', 'father_mobile',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Child.book'
        db.add_column('core_child', 'book',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Child.mother_name'
        db.add_column('core_child', 'mother_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    models = {
        'core.child': {
            'Meta': {'object_name': 'Child'},
            'child_parents': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ChildParents']", 'null': 'True', 'blank': 'True'}),
            'curriculum_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_school_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SundaySchoolClass']", 'null': 'True', 'blank': 'True'})
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
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sunday_school_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SundaySchoolClass']", 'null': 'True', 'blank': 'True'})
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