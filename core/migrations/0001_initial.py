# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField(null=True, blank=True)),
                ('school_year', models.IntegerField(null=True, blank=True)),
                ('sent_emails', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChildParents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=255, blank=True)),
                ('father_name', models.CharField(max_length=255, blank=True)),
                ('father_mobile', models.CharField(max_length=255, blank=True)),
                ('father_email', models.EmailField(max_length=75, blank=True)),
                ('mother_name', models.CharField(max_length=255, blank=True)),
                ('mother_mobile', models.CharField(max_length=255, blank=True)),
                ('mother_email', models.EmailField(max_length=75, blank=True)),
                ('address', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('uid', models.CharField(max_length=255)),
                ('dob', models.DateField(null=True, blank=True)),
                ('phone', models.CharField(max_length=255, blank=True)),
                ('mobile', models.CharField(max_length=255, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('address', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServantAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('attended_mass', models.BooleanField()),
                ('attended_meeting', models.BooleanField()),
                ('attended_sunday_school', models.BooleanField()),
                ('servant', models.ForeignKey(to='core.Servant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SundaySchoolClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('book', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='servant',
            name='sunday_school_class',
            field=models.ForeignKey(blank=True, to='core.SundaySchoolClass', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='child',
            name='child_parents',
            field=models.ForeignKey(blank=True, to='core.ChildParents', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='child',
            name='sunday_school_class',
            field=models.ForeignKey(blank=True, to='core.SundaySchoolClass', null=True),
            preserve_default=True,
        ),
    ]
