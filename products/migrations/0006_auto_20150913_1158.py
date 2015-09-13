# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150913_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost_price',
            field=models.DecimalField(verbose_name=b'Unit Cost', max_digits=12, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_inventory',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_number',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'partnumber'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_price',
            field=models.DecimalField(max_digits=12, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.ForeignKey(default=b'Active', to='products.Status'),
        ),
        migrations.AlterField(
            model_name='soldby',
            name='status',
            field=models.ForeignKey(default=b'Active', to='products.Status'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='suppliercatalog',
            name='supplier_description',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='uom',
            name='description',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
