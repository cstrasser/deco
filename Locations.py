import os
from sys import argv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd1.settings')
#first_name,last_name,company_name,address,city,province,postal,phone1,phone2,email,web
import csv
import django
django.setup()

from main.models import Location, Organization,Contact

def popcontact(row):
   contact = []
   contact[1] =row[1] #firstname
   contact[2] = row[2] #lastname
   contact[3] = row[6]
   
   
   
   
   return contact
    
def run():
   contact=[]
   for row in csv.reader(open('ca-500.csv')):
      fields=['firstname','lastname','organizationname','address1',
              'city','stateorprovince','zippostal_code','phone','notes','email','extra1']
      #c= (zip(fields,row))
      #Location.objects.create(**c)
      contact = popcontact(row)
      print contact
      
#http://stackoverflow.com/questions/5503925/how-do-i-use-a-dictionary-to-update-fields-in-django-models
if __name__ == '__main__':
    print "Starting  script..."
    run()    


#with  open('ca-500.csv') as f:
   #print text.read()