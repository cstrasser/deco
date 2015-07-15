from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login
from main.models import Organization, Location,Contact



def home(request):
    
    #customer_list = Organization.objects.all().order_by('organizationname')[:100]
    location_list = Location.objects.filter(is_default = True).order_by('orgid').select_related()[:100]
        
    return render(request,'home.html',{'list':location_list})


def do_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'home.html')
            else:
                pass # Return a 'disabled account' error message
        else:
            pass#  Return an 'invalid login' error message. 
    else:
        return render(request, 'loginform.html')
    
    
    
    
    
