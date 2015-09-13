from django.db import models

class PurchaseOrder(models.Model):
    po_number = modles.Autofield()
    organization = models.Foreignkey(Organization)
    shipto = models.ForeignKey(Location)
    soldby = models.Charfield(max_length = 25)
    lineitem = modles.Foreignkey(PoDetalis)
    expected_by = models.DateTimefield()
    
     
class PoDetails(modles.Model):
    linenumber = models.IntegerField(digits = 3)
    product = ForeignKey(Products.product)
    sellprice = number
    quantity = models.IntegerField()
    
    
    
    
    
    
    
