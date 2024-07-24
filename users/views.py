from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm
# Create your views here.

def login(request):
    context = {
        'title': 'Вход',
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Регистрация',
    }
    return render(request, 'users/register.html', context)
