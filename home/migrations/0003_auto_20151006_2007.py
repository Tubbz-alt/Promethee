# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151006_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectactivity',
            old_name='intensities',
            new_name='intensity',
        ),
    ]
