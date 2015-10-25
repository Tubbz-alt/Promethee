# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=10000)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('intensity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLanguage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='activity',
            field=models.ForeignKey(default=0, to='home.ProjectActivity'),
        ),
    ]
