from django.shortcuts import render

from main.models import Organization, Location,Contact


def orgview(request,org_id):
    organization = Organization.objects.get(pk =org_id)
         
    return render(request,'orgform.html',{'orginfo':organization})
