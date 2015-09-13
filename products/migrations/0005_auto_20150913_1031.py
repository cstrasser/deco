# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150913_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=10, choices=[(b'ACTIVE', b'Active'), (b'OBSOLETE', b'Obsolete'), (b'INACTIVE', b'Inactive')]),
        ),
    ]
