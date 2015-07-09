from django.conf.urls import include, url
from main import views


urlpatterns = [
    url(r'^', views.home, name='home'),
    url(r'^login', views.do_login, name='do_login'),
]