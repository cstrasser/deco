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
                ('contactid', models.AutoField(serialize=False, primary_key=True, db_column=b'ContactID')),
                ('firstname', models.CharField(max_length=50, null=True, db_column=b'FirstName', blank=True)),
                ('lastname', models.CharField(max_length=50, null=True, db_column=b'LastName', blank=True)),
                ('is_primary', models.BooleanField(db_column=b'PrimaryContact')),
                ('title', models.CharField(max_length=50, db_column=b'Title')),
                ('email', models.CharField(max_length=50, null=True, db_column=b'Email', blank=True)),
                ('displayorder', models.SmallIntegerField(db_column=b'DisplayOrder')),
                ('phone_type1', models.CharField(max_length=50, null=True, db_column=b'PhType1', blank=True)),
                ('phone1', models.TextField(null=True, db_column=b'Phone1', blank=True)),
                ('phone_type2', models.CharField(max_length=50, null=True, db_column=b'PhType2', blank=True)),
                ('phone2', models.TextField(null=True, db_column=b'Phone2', blank=True)),
                ('phone_type3', models.CharField(max_length=50, null=True, db_column=b'PhType3', blank=True)),
                ('phone3', models.TextField(null=True, db_column=b'Phone3', blank=True)),
                ('lastedit_timestamp', models.DateTimeField(auto_now=True, db_column=b'LastEdited')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, db_column=b'CreatedTimestamp')),
                ('active', models.BooleanField(db_column=b'Active')),
            ],
            options={
                'db_table': 'tblContact',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationid', models.AutoField(serialize=False, primary_key=True, db_column=b'LocationID')),
                ('locationname', models.CharField(max_length=75, null=True, db_column=b'LocationName')),
                ('address1', models.CharField(max_length=200, null=True, db_column=b'Address1', blank=True)),
                ('address2', models.CharField(max_length=200, null=True, db_column=b'Address2', blank=True)),
                ('address3', models.CharField(max_length=200, null=True, db_column=b'Address3', blank=True)),
                ('city', models.CharField(max_length=100, null=True, db_column=b'City', blank=True)),
                ('stateorprovince', models.CharField(max_length=50, null=True, db_column=b'StateOrProvince', blank=True)),
                ('zippostal_code', models.CharField(max_length=20, null=True, db_column=b'PostalCode', blank=True)),
                ('primary', models.BooleanField(db_column=b'Primary')),
                ('default_invoice_address', models.BooleanField(db_column=b'InvoiceAddress')),
                ('notes', models.TextField(null=True, db_column=b'Notes', blank=True)),
                ('privatenotes', models.TextField(null=True, db_column=b'PrivateNotes', blank=True)),
                ('latitude', models.CharField(max_length=10, db_column=b'Latitude')),
                ('longitude', models.CharField(max_length=50, db_column=b'Longitude')),
                ('lastedit_timestamp', models.DateTimeField(auto_now=True, db_column=b'LastEdited')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, db_column=b'CreatedTimestamp')),
                ('active', models.BooleanField(db_column=b'Active')),
            ],
            options={
                'db_table': 'tblLocation',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('orgid', models.AutoField(serialize=False, primary_key=True, db_column=b'OrgID')),
                ('is_company', models.BooleanField(default=True, db_column=b'IsCompany')),
                ('organizationname', models.CharField(max_length=75, null=True, db_column=b'OrgName', blank=True)),
                ('prefix', models.CharField(max_length=50, null=True, db_column=b'Prefix', blank=True)),
                ('firstname', models.CharField(max_length=50, null=True, db_column=b'FirstName', blank=True)),
                ('lastname', models.CharField(max_length=50, null=True, db_column=b'LastName', blank=True)),
                ('suffix', models.CharField(max_length=50, null=True, db_column=b'Suffix', blank=True)),
                ('mainnotes', models.TextField(null=True, db_column=b'MainNotes', blank=True)),
                ('privatenotes', models.TextField(null=True, db_column=b'PrivateNotes', blank=True)),
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
                ('is_customer', models.BooleanField(db_column=b'IsCustomer')),
                ('is_vendor', models.BooleanField(db_column=b'IsVendor')),
                ('alertmessage', models.CharField(max_length=200, null=True, db_column=b'AlertMessage', blank=True)),
                ('alertpastduetriggered', models.BooleanField(db_column=b'AlertPastDueTriggered')),
                ('alertpastduedays', models.IntegerField(db_column=b'AlertPastDueDays')),
                ('alertcreditlimitenabled', models.BooleanField(db_column=b'AlertCreditLimitEnabled')),
                ('alertcreditlimittriggered', models.BooleanField(db_column=b'AlertCreditLimitTriggered')),
                ('alertcreditlimitamount', models.DecimalField(decimal_places=2, max_digits=12, db_column=b'AlertCreditLimitAmount')),
                ('alerthaltjobcreation', models.BooleanField(db_column=b'AlertHaltJobCreation')),
            ],
            options={
                'db_table': 'tblOrganization',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='orgid',
            field=models.ForeignKey(to='main.Organization', db_column=b'OrgID'),
        ),
        migrations.AddField(
            model_name='contact',
            name='locationid',
            field=models.ForeignKey(to='main.Location', db_column=b'LocationID'),
        ),
    ]
