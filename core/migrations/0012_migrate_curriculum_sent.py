# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        
        email_id = 'cur20130313'
        for child in orm['core.Child'].objects.filter(curriculum_sent=True):
            child.sent_emails += email_id + ','
            child.save()
        

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'core.child': {
            'Meta': {'object_name': 'Child'},
            'child_parents': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ChildParents']", 'null': 'True', 'blank': 'True'}),
            'curriculum_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sent_emails': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
    symmetrical = True
