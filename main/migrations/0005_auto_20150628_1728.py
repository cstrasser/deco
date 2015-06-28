# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150628_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='alertcreditlimitamount',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=12, db_column=b'AlertCreditLimitAmount', blank=True),
        ),
    ]
