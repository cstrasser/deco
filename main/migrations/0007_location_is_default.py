# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150628_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='is_default',
            field=models.BooleanField(default=True, db_column=b'default'),
        ),
    ]
