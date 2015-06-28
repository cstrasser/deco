# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150628_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='active',
            field=models.BooleanField(default=True, db_column=b'Active'),
        ),
        migrations.AlterField(
            model_name='location',
            name='active',
            field=models.BooleanField(default=True, db_column=b'Active'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='alertcreditlimitenabled',
            field=models.NullBooleanField(db_column=b'AlertCreditLimitEnabled'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='alertcreditlimittriggered',
            field=models.NullBooleanField(db_column=b'AlertCreditLimitTriggered'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='alerthaltjobcreation',
            field=models.NullBooleanField(db_column=b'AlertHaltJobCreation'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='alertpastduetriggered',
            field=models.NullBooleanField(db_column=b'AlertPastDueTriggered'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='is_customer',
            field=models.BooleanField(default=True, db_column=b'IsCustomer'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='is_vendor',
            field=models.BooleanField(default=False, db_column=b'IsVendor'),
        ),
    ]
