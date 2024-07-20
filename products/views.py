from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, "products/index.html", context)

def products(request):
    context = {
        'title': 'Каталог',
    }
    return render(request,"products/products.html", context)

def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Welcome',
        'username':'Ivan',
        'products': [
            { "name": 'Худи', 'price':6000.00 },
            { "name": 'Футболка', 'price':6000.00 },
            { "name": 'Кросы', 'price':6500.00 }
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Кеды','price':1000.00}
        ]
    }
    return render(request, 'products/test_context.html',context)