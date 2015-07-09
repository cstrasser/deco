from django.db import models

class Organization(models.Model):  #customer or vendor person or company 
    organizationname = models.CharField(db_column='OrgName', max_length=75,blank=True, null=True)  
    prefix = models.CharField(db_column='Prefix', max_length=50,blank=True, null=True)  
    firstname = models.CharField(db_column='FirstName', max_length=50,blank=True, null=True)  
    lastname = models.CharField(db_column='LastName', max_length=50,blank=True, null=True)  
    suffix = models.CharField(db_column='Suffix', max_length=50,blank=True, null=True)   
    mainnotes = models.TextField(db_column='MainNotes', blank=True, null=True)
    privatenotes = models.TextField(db_column='PrivateNotes', blank=True, null=True)
    is_company = models.NullBooleanField(db_column='IsCompany', default =True)
    is_active = models.BooleanField(db_column='Active', default = True)  
    dateterminated = models.DateTimeField(db_column='DateTerminated', blank=True, null=True)  
    extra1 = models.TextField(db_column='Extra1', blank=True, null=True) 
    extra2 = models.TextField(db_column='Extra2', blank=True, null=True)  
    extra3 = models.TextField(db_column='Extra3', blank=True, null=True)                                                    
    extra4 = models.TextField(db_column='Extra4', blank=True, null=True)
    lastedit_timestamp = models.DateTimeField(db_column='LastEdited', auto_now=True)  
    last_edit_by = models.CharField(db_column='Editor', max_length=50) 
    created_timestamp = models.DateTimeField(db_column='CreatedTimestamp', auto_now_add=True)
    created_by = models.CharField(db_column='Createdby', max_length=50) #foreign key to user that created this field
    is_customer = models.BooleanField(db_column='IsCustomer', default = True)  
    is_vendor = models.BooleanField(db_column='IsVendor', default = False)  
    alrtmessage = models.CharField(db_column='AlertMessage',max_length=200,blank=True, null=True) #if not null this message will pop up when customer opened
    alrtpastduetriggered = models.NullBooleanField(db_column='AlertPastDueTriggered')  
    alrtpastduedays = models.IntegerField(db_column='AlertPastDueDays',null=True)  
    alrtcreditlimitenabled = models.NullBooleanField(db_column='AlertCreditLimitEnabled')  
    alrtcreditlimittriggered = models.NullBooleanField(db_column='AlertCreditLimitTriggered')  
    creditlimit = models.DecimalField(db_column='AlertCreditLimitAmount', max_digits=12, decimal_places=2,blank= True,null=True)  
    alrthaltjobcreation = models.NullBooleanField(db_column='AlertHaltJobCreation')  

    class Meta:
        
        db_table = 'tblOrganization'
        
    def __str__(self):
        if (self.organizationname):
         return '%s ' %(self.organizationname)
        else:
         return '%s %s' %(self.firstname, self.lastname)

class Location(models.Model): 
    orgid = models.ForeignKey(Organization, db_column='OrgID')  
    locationname = models.CharField(db_column='LocationName', max_length=75, null=True)
    phone = models.CharField(db_column='MainPhone',max_length=20, blank=True, null=True) 
    is_default = models.BooleanField(db_column='default', default = True)
    address1 = models.CharField(db_column='Address1', max_length=200, blank=True, null=True)  
    address2 = models.CharField(db_column='Address2', max_length=200, blank=True, null=True)  
    address3 = models.CharField(db_column='Address3', max_length=200, blank=True, null=True)  
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  
    stateorprovince = models.CharField(db_column='StateOrProvince', max_length=50, blank=True, null=True)  
    zippostal_code = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)
    primary = models.NullBooleanField(db_column='Primary')  
    default_invoice_address = models.NullBooleanField(db_column='InvoiceAddress')  
    notes = models.TextField(db_column='Notes', blank=True, null=True)  
    #taxcodeid1 = models.ForeignKey(Lkptaxcodes, db_column='TaxCodeID1')  
    #taxcodeid2 = models.ForeignKey(Lkptaxcodes, db_column='TaxCodeID2') 
    #taxcodeid3 = models.ForeignKey(Lkptaxcodes, db_column='TaxCodeID3')  
    privatenotes = models.TextField(db_column='PrivateNotes', blank=True, null=True)  
    latitude = models.CharField(db_column='Latitude', max_length=10, blank=True, null=True)  
    longitude = models.CharField(db_column='Longitude', max_length=50, blank=True, null=True)  
    lastedit_timestamp = models.DateTimeField(db_column='LastEdited', auto_now=True)  
    created_timestamp = models.DateTimeField(db_column='CreatedTimestamp', auto_now_add=True)  
    active = models.BooleanField(db_column='Active', default = True)
    
    class Meta:     
        db_table = 'tblLocation'  
    def __str__(self):
         return '%s ' %(self.locationname)   
        
class Contact(models.Model):   
    locationid = models.ForeignKey(Location, db_column='LocationID')  
    firstname = models.CharField(db_column='FirstName', max_length=50,blank=True, null=True)  
    lastname = models.CharField(db_column='LastName', max_length=50,blank=True, null=True) 
    is_primary = models.NullBooleanField(db_column='PrimaryContact')
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  
    displayorder = models.SmallIntegerField(db_column='DisplayOrder',blank=True, null=True)  
    phone_type1 = models.CharField(db_column='PhType1', max_length=50, blank=True, null=True)  
    phone1 = models.CharField(db_column='Phone1',max_length=15, blank=True, null=True) 
    phone_type2 = models.CharField(db_column='PhType2', max_length=50, blank=True, null=True)  
    phone2 = models.CharField(db_column='Phone2',max_length=15, blank=True, null=True)  
    phone_type3 = models.CharField(db_column='PhType3', max_length=50, blank=True, null=True)  
    phone3 = models.CharField(db_column='Phone3',max_length=15, blank=True, null=True)   
    lastedit_timestamp = models.DateTimeField(db_column='LastEdited', auto_now =True)  
    created_timestamp = models.DateTimeField(db_column='CreatedTimestamp', auto_now_add=True) 
    active = models.BooleanField(db_column='Active', default = True)  
    
    class Meta: 
        db_table = 'tblContact' 
    def __str__(self):
        #return '%s %s %s %s %s' %( self.locationid.orgid.organizationname, self.firstname, self.lastname, self.phone1,self.email)
        return '%s %s' %( self.firstname, self.lastname)
