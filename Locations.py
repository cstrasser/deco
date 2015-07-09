import os
from sys import argv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd1.settings')
#first_name,last_name,company_name,address,city,province,postal,phone1,phone2,email,web
import csv
import django
django.setup()

from main.models import Location, Organization,Contact
    
def run():
   for row in csv.reader(open('ca-500.csv')):
      fields=['first_name','last_name','company_name','address','city','province','postal','phone1','phone2','email','web']
      c= dict(zip(fields,row))
      print c
      

if __name__ == '__main__':
    print "Starting  script..."
    run()    


#with  open('ca-500.csv') as f:
   #print text.read()