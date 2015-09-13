from django.db import models
from main.models import Organization

class Uom(models.Model): #unit of measure
     # example  treatment, session, part, item, celcius, pound, load etc..(this is the product type as well )
    name = models.CharField(max_length = 25)
    abbreviation = models.CharField(max_length = 6)
    description = models.CharField(max_length = 50, blank = True)
    
    def __str__(self):
         return '%s ' %(self.abbreviation)

class Status(models.Model):
    status = models.CharField(max_length = 10 )

    def __str__(self):
        return '%s' %(self.status)

class Product(models.Model):
    part_number = models.CharField('partnumber', max_length = 50, blank = False ,null= False, unique = True )
    name = models.CharField( max_length=50,blank=True)   
    description = models.CharField(max_length=50,blank=True, null=True)
    details = models.CharField(max_length=250,blank=True, null=True)
    notes = models.TextField(blank=True, null=True)  
    uom = models.ForeignKey(Uom,blank=True,null=True)  
    cost_price = models.DecimalField("Unit Cost",max_digits=12, decimal_places=4,blank = True)  
    sell_price = models.DecimalField(max_digits=12, decimal_places=4 ,blank = True)  
    special_order = models.BooleanField(default = False)
    tax1 = models.BooleanField(default = False)
    tax2 = models.BooleanField(default = False)   
    tax3 = models.BooleanField(default = False)
    status = models.ForeignKey(Status, default = 'Active')
    is_inventory = models.NullBooleanField(default = False )  

        
class SupplierCatalog(models.Model):
    organiation = models.ForeignKey(Organization)
    product = models.ForeignKey(Product)  
    supplier_partno = models.CharField(max_length=75)  
    supplier_description = models.CharField( max_length=250, blank =True)  
    cost_price = models.DecimalField('Unit Cost',max_digits=12, decimal_places=4)
    uom = models.ForeignKey(Uom)
    notes = models.TextField(db_column='Notes', blank=True, null=True)   
    manufacturer = models.CharField( max_length=100)  
    manufacturer_modelno = models.CharField(max_length=75)
    status = models.ForeignKey(Status)
    lead_time_days = models.IntegerField(blank = True ,null = True)
    
class SoldBy(models.Model):
    productid = models.ForeignKey(Product)
    supplierid = models.ForeignKey(Organization)
    status = models.ForeignKey(Status, default = 'Active')
    
    
    
