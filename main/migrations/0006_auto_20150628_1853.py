# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150628_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='alertcreditlimitenabled',
            new_name='alrtcreditlimitenabled',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='alertcreditlimittriggered',
            new_name='alrtcreditlimittriggered',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='alerthaltjobcreation',
            new_name='alrthaltjobcreation',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='alertmessage',
            new_name='alrtmessage',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='alertpastduedays',
            new_name='alrtpastduedays',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='alertpastduetriggered',
            new_name='alrtpastduetriggered',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='alertcreditlimitamount',
            new_name='creditlimit',
        ),
        migrations.AddField(
            model_name='organization',
            name='main_phone',
            field=models.CharField(max_length=20, null=True, db_column=b'MainPhone', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone1',
            field=models.CharField(max_length=15, null=True, db_column=b'Phone1', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone2',
            field=models.CharField(max_length=15, null=True, db_column=b'Phone2', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone3',
            field=models.CharField(max_length=15, null=True, db_column=b'Phone3', blank=True),
        ),
    ]
