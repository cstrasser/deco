# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150913_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliercatalog',
            name='lead_time_days',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
