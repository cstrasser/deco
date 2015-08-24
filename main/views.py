from django.shortcuts import render, render_to_response
from django import forms
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.models import Organization, Location,Contact



def home(request):
    
    #customer_list = Organization.objects.all().order_by('organizationname')[:100]
    location_list = Location.objects.filter(is_default = True).order_by('orgid').select_related()
    paginator = Paginator(location_list, 25)
    
    page = request.GET.get('page')
    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        locations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        locations = paginator.page(paginator.num_pages)

    return render_to_response('home.html', {"locations": locations})
    
    #return render(request,'home.html',{'list':location_list})


def do_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                print 'login user is active'
                return render(request,'home.html',{})
            else:
                
                pass # Return a 'disabled account' error message
        else:
           pass#  Return an 'invalid login' error message.
            
    else:
        return render(request, 'loginform.html')
    
    
    
    
    
