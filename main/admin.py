from django.contrib import admin
from main.models import Organization,Location,Contact
#from main.forms import AuthenticationForm

admin.site.site_header = 'Decorator Administration'
#admin.autodiscover()
#admin.site.login_form = AuthenticationForm


#admin.site.register(Organization)
#admin.site.register(Location)
#admin.site.register(Contact)

@admin.register(Organization,Location,Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('organizationname', 'firstname', 'city','zippostal_code')
    pass

# Register your models here.

# Admin user: admin
#Admin Pass: Aema...
#adminsite.login_form
#AdminSite.each_context(request) ... returns a dict of variables  site header,site title,site url
#for above see adminSite methods