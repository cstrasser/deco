# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_number', models.CharField(max_length=50, verbose_name=b'partnumber')),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=50)),
                ('notes', models.TextField(null=True, blank=True)),
                ('cost_price', models.DecimalField(verbose_name=b'Unit Cost', max_digits=20, decimal_places=4)),
                ('sell_price', models.DecimalField(max_digits=20, decimal_places=4)),
                ('special_order', models.BooleanField(default=False)),
                ('tax1', models.BooleanField(default=False)),
                ('tax2', models.BooleanField(default=False)),
                ('tax3', models.BooleanField(default=False)),
                ('is_inventory', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'Active', max_length=15)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierCatalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_partno', models.CharField(max_length=100)),
                ('supplier_description', models.CharField(max_length=250)),
                ('cost_price', models.DecimalField(verbose_name=b'Unit Cost', max_digits=20, decimal_places=4)),
                ('notes', models.TextField(null=True, db_column=b'Notes', blank=True)),
                ('manufacturer', models.CharField(max_length=100)),
                ('manufacturer_modelno', models.CharField(max_length=50)),
                ('organiation', models.ForeignKey(to='main.Organization')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Uom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('abbreviation', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='suppliercatalog',
            name='uom',
            field=models.ForeignKey(to='products.Uom'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.ForeignKey(to='products.Status'),
        ),
        migrations.AddField(
            model_name='product',
            name='uom',
            field=models.ForeignKey(to='products.Uom'),
        ),
    ]
