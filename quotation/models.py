from django.db import models

class Quotation(models.Model):
    customer = models.ForeignKey(organization.Organization)
    quote_line = models.ForeignKey(QuotationDetail)
    revision = models.CharField(max_length = 3, default = '')
    sold_by = models.ForeignKey(admin.User)
    private_notes = models.TextField(null= True, blank = True)
    notes = models.TextField(null=True, blank = True)
    status =  models.CharField(max_lenght = 10,default= 'open') #open closed_lost , closed_won
    po = models.IntegerField(null = True)
    
class QuotationDetail(models.Model):
    quotation = models.ForeignKey(Quotation)
    line = models.AutoField()
    part_number = models.ForeignKey(products.Product)
    quantity = models.IntegerField(default = 1)
    
    
    
