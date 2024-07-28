from django.shortcuts import render, HttpResponseRedirect
from products.models import Products, ProductCategory, Basket
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

def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user = request.user,product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product,quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


