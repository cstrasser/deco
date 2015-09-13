# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldBy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='status',
            name='description',
        ),
        migrations.AddField(
            model_name='suppliercatalog',
            name='lead_time_days',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suppliercatalog',
            name='status',
            field=models.ForeignKey(to='products.Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost_price',
            field=models.DecimalField(verbose_name=b'Unit Cost', max_digits=12, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_inventory',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_price',
            field=models.DecimalField(max_digits=12, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='uom',
            field=models.ForeignKey(blank=True, to='products.Uom', null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=10, choices=[(b'ACTIVE', b'Active'), (b'OBSOLETE', b'Obsolete'), (b'INACTIVE', b'Inactive')]),
        ),
        migrations.AlterField(
            model_name='suppliercatalog',
            name='cost_price',
            field=models.DecimalField(verbose_name=b'Unit Cost', max_digits=12, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='suppliercatalog',
            name='manufacturer_modelno',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='suppliercatalog',
            name='supplier_partno',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='uom',
            name='abbreviation',
            field=models.CharField(max_length=6),
        ),
        migrations.AddField(
            model_name='soldby',
            name='productid',
            field=models.ForeignKey(to='products.Product'),
        ),
        migrations.AddField(
            model_name='soldby',
            name='status',
            field=models.ForeignKey( to='products.Status'),
        ),
        migrations.AddField(
            model_name='soldby',
            name='supplierid',
            field=models.ForeignKey(to='main.Organization'),
        ),
    ]
