# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=50, null=True, db_column=b'FirstName', blank=True)),
                ('lastname', models.CharField(max_length=50, null=True, db_column=b'LastName', blank=True)),
                ('is_primary', models.NullBooleanField(db_column=b'PrimaryContact')),
                ('title', models.CharField(max_length=50, null=True, db_column=b'Title', blank=True)),
                ('email', models.CharField(max_length=50, null=True, db_column=b'Email', blank=True)),
                ('displayorder', models.SmallIntegerField(null=True, db_column=b'DisplayOrder', blank=True)),
                ('phone_type1', models.CharField(max_length=50, null=True, db_column=b'PhType1', blank=True)),
                ('phone1', models.CharField(max_length=15, null=True, db_column=b'Phone1', blank=True)),
                ('phone_type2', models.CharField(max_length=50, null=True, db_column=b'PhType2', blank=True)),
                ('phone2', models.CharField(max_length=15, null=True, db_column=b'Phone2', blank=True)),
                ('phone_type3', models.CharField(max_length=50, null=True, db_column=b'PhType3', blank=True)),
                ('phone3', models.CharField(max_length=15, null=True, db_column=b'Phone3', blank=True)),
                ('lastedit_timestamp', models.DateTimeField(auto_now=True, db_column=b'LastEdited')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, db_column=b'CreatedTimestamp')),
                ('active', models.BooleanField(default=True, db_column=b'Active')),
            ],
            options={
                'db_table': 'tblContact',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locationname', models.CharField(max_length=75, null=True, db_column=b'LocationName')),
                ('phone', models.CharField(max_length=20, null=True, db_column=b'MainPhone', blank=True)),
                ('is_default', models.BooleanField(default=True, db_column=b'default')),
                ('address1', models.CharField(max_length=200, null=True, db_column=b'Address1', blank=True)),
                ('address2', models.CharField(max_length=200, null=True, db_column=b'Address2', blank=True)),
                ('address3', models.CharField(max_length=200, null=True, db_column=b'Address3', blank=True)),
                ('city', models.CharField(max_length=100, null=True, db_column=b'City', blank=True)),
                ('stateorprovince', models.CharField(max_length=50, null=True, db_column=b'StateOrProvince', blank=True)),
                ('zippostal_code', models.CharField(max_length=20, null=True, db_column=b'PostalCode', blank=True)),
                ('primary', models.NullBooleanField(db_column=b'Primary')),
                ('default_invoice_address', models.NullBooleanField(db_column=b'InvoiceAddress')),
                ('notes', models.TextField(null=True, db_column=b'Notes', blank=True)),
                ('privatenotes', models.TextField(null=True, db_column=b'PrivateNotes', blank=True)),
                ('latitude', models.CharField(max_length=10, null=True, db_column=b'Latitude', blank=True)),
                ('longitude', models.CharField(max_length=50, null=True, db_column=b'Longitude', blank=True)),
                ('lastedit_timestamp', models.DateTimeField(auto_now=True, db_column=b'LastEdited')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, db_column=b'CreatedTimestamp')),
                ('active', models.BooleanField(default=True, db_column=b'Active')),
            ],
            options={
                'db_table': 'tblLocation',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organizationname', models.CharField(max_length=75, null=True, db_column=b'OrgName', blank=True)),
                ('prefix', models.CharField(max_length=50, null=True, db_column=b'Prefix', blank=True)),
                ('firstname', models.CharField(max_length=50, null=True, db_column=b'FirstName', blank=True)),
                ('lastname', models.CharField(max_length=50, null=True, db_column=b'LastName', blank=True)),
                ('suffix', models.CharField(max_length=50, null=True, db_column=b'Suffix', blank=True)),
                ('mainnotes', models.TextField(null=True, db_column=b'MainNotes', blank=True)),
                ('privatenotes', models.TextField(null=True, db_column=b'PrivateNotes', blank=True)),
                ('is_company', models.NullBooleanField(default=True, db_column=b'IsCompany')),
                ('is_active', models.BooleanField(default=True, db_column=b'Active')),
                ('dateterminated', models.DateTimeField(null=True, db_column=b'DateTerminated', blank=True)),
                ('extra1', models.TextField(null=True, db_column=b'Extra1', blank=True)),
                ('extra2', models.TextField(null=True, db_column=b'Extra2', blank=True)),
                ('extra3', models.TextField(null=True, db_column=b'Extra3', blank=True)),
                ('extra4', models.TextField(null=True, db_column=b'Extra4', blank=True)),
                ('lastedit_timestamp', models.DateTimeField(auto_now=True, db_column=b'LastEdited')),
                ('last_edit_by', models.CharField(max_length=50, db_column=b'Editor')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, db_column=b'CreatedTimestamp')),
                ('created_by', models.CharField(max_length=50, db_column=b'Createdby')),
                ('is_customer', models.BooleanField(default=True, db_column=b'IsCustomer')),
                ('is_vendor', models.BooleanField(default=False, db_column=b'IsVendor')),
                ('alrtmessage', models.CharField(max_length=200, null=True, db_column=b'AlertMessage', blank=True)),
                ('alrtpastduetriggered', models.NullBooleanField(db_column=b'AlertPastDueTriggered')),
                ('alrtpastduedays', models.IntegerField(null=True, db_column=b'AlertPastDueDays')),
                ('alrtcreditlimitenabled', models.NullBooleanField(db_column=b'AlertCreditLimitEnabled')),
                ('alrtcreditlimittriggered', models.NullBooleanField(db_column=b'AlertCreditLimitTriggered')),
                ('creditlimit', models.DecimalField(null=True, decimal_places=2, max_digits=12, db_column=b'AlertCreditLimitAmount', blank=True)),
                ('alrthaltjobcreation', models.NullBooleanField(db_column=b'AlertHaltJobCreation')),
            ],
            options={
                'db_table': 'tblOrganization',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='orgid',
            field=models.ForeignKey(to='main.Organization'),
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.ForeignKey(to='main.Location'),
        ),
    ]
