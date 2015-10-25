# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_project_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(to='home.ProjectLanguage'),
        ),
    ]
