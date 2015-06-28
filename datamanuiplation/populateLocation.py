import os
from sys import argv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd1.settings')


import django
django.setup()

from main.models import Location, Organization

def addloc(location):
   o = Organization.objects.filter(orgid = location[0])[0]
   print location[0], o.orgid
   c = Location.objects.get_or_create(
      orgid  = o,
      address1 = location[1],
      city = location[2],   
      zippostal_code = location[4],
      stateorprovince = location[3]
      )[0]
   return c
    
    
    
def run():    
    with  open('locations.txt') as f:
    #print text.read()
     for location in f:
        location = location.split(",")
        addloc(location)
        #print 'id %s  Address: %s City %s Prov %s PC %s' %(location[0], location[1], location[2], location[3] ,location[4])
          
    
    

if __name__ == '__main__':
    print "Starting  script..."
    run()    
