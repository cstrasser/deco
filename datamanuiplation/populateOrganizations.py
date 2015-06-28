import os
from sys import argv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd1.settings')


import django
django.setup()

from main.models import Organization

def addorg(name):
   c = Organization.objects.get_or_create(organizationname=name)[0]
   return c
    
    
    
def run():    
    with  open('organizations.txt') as f:
    #print text.read()
     for name in f:
        addorg(name)
        print '><><><><><'
        
          
    
    

if __name__ == '__main__':
    print "Starting  script..."
    run()    
