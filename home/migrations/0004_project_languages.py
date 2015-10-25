# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151006_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(to='home.ProjectLanguage'),
        ),
    ]
