# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_location_is_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='main_phone',
        ),
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.CharField(max_length=20, null=True, db_column=b'MainPhone', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='orgid',
            field=models.ForeignKey(related_name='organization', db_column=b'OrgID', to='main.Organization'),
        ),
    ]
