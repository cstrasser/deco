# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150628_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='displayorder',
            field=models.SmallIntegerField(null=True, db_column=b'DisplayOrder', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_primary',
            field=models.NullBooleanField(db_column=b'PrimaryContact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=50, null=True, db_column=b'Title', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='default_invoice_address',
            field=models.NullBooleanField(db_column=b'InvoiceAddress'),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.CharField(max_length=10, null=True, db_column=b'Latitude', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.CharField(max_length=50, null=True, db_column=b'Longitude', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='primary',
            field=models.NullBooleanField(db_column=b'Primary'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='alertpastduedays',
            field=models.IntegerField(null=True, db_column=b'AlertPastDueDays'),
        ),
    ]
