import os
from sys import argv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd1.settings')


import django
django.setup()

from main.models import Contact, Location

def addcontact(contact):
   o = Location.objects.filter(locationid = contact[0])[0]
   print contact[0], o.locationid, o.city
   c = Contact.objects.get_or_create(
      locationid  = o,
      firstname = contact[1],
      lastname = contact[2],   
      phone1 = contact[3],
      email = contact[4]
      )[0]
   return c
    
    
    
def run():    
    with  open('contacts.txt') as f:
    #print text.read()
     for contact in f:
        contact = contact.split()
        addcontact(contact)
        #print 'locid %s  firstnm: %s LastNM: %s Phone %s Email %s' %(contact[0], contact[1], contact[2], contact[3] ,contact[4])
          
    
    

if __name__ == '__main__':
    print "Starting  script..."
    run()    
