from django.views.generic import TemplateView ,ListView, UpdateView, DetailView, CreateView

from models import Product

class ProductList(ListView):
    queryset = Product.objects.all()
    template_name = 'products_list.html'
   
class ProductCreate(CreateView):
    model = Product
    template_name = 'productcreate_form.html'
    fields  = ('part_number','name' ,'description', 'details', 'notes','uom', 'cost_price','sell_price',
               'special_order', 'tax1','tax2','tax3','status','is_inventory')
    
    
class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"
    
class ProductUpdate(UpdateView):
    model = Product
    template_name = 'productcreate_form.html'
    fields  = ('part_number','name' ,'description', 'details', 'notes','uom', 'cost_price','sell_price',
               'special_order', 'tax1','tax2','tax3','status','is_inventory')

