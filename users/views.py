from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'tittle': 'Вход',
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'tittle': 'Регистрация',
    }
    return render(request, 'users/register.html', context)
