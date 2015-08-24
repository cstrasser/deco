from django.conf.urls import include, url
from organization import views

urlpatterns = [
    url(r'^(?P<org_id>\d+)/$', views.orgview, name='orgview'),
    
]


#(?P<org_id>d+)
#url(r'^articles/(?P<year>[0-9]{4})/$',