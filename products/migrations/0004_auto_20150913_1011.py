# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150913_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldby',
            name='status',
            field=models.ForeignKey(to='products.Status'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='suppliercatalog',
            name='status',
            field=models.ForeignKey(to='products.Status'),
        ),
    ]
