from django.shortcuts import render
from products.models import Products, ProductCategory
# Create your views here.

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, "products/index.html", context)

def products(request):
    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Products.objects.all(),
    }
    return render(request,"products/products.html", context)


