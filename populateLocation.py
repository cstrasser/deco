import os
from sys import argv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd1.settings')


import django
django.setup()

from main.models import Location, Organization

def addloc(dataline):
   o =Organization.objects.get_or_create(organizationname =dataline[0])
   
   l = Location.objects.get_or_create( 
      address1 = dataline[1],
      city = dataline[2],
      stateorprovince = dataline[3],
      zippostal_code = dataline[4],
      orgid = o
      )
   c= Contact.objects.get_or_create(
         firstname = dataline[5],
         lastname = dataline[6],
         phone = dataline[7],
         email = dataline[8],
         location =  l)
   
   return c
    
    
def run():    
    with  open('data.txt') as f:
     #print f.read()
     for location in f:
        location = location.split(",")
        addloc(dataline)
        # #print 'orgname %s Address: %s City %s Prov %s PC %s firstname %s, Lastname %s ph %s eml %s' %(
        #                                            location[0], location[1],
        #                                            location[2], location[3],location[4],
        #                                            location[5], location[6],location[7],location[8] )
          
     
    

if __name__ == '__main__':
    print "Starting  script..."
    run()    
