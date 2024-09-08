from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def frontpage (request) :
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products, 'request': request})

def login(request):
    if request.method == 'POST':
        print ('in if')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('frontpage')
    else:
        print ('in else')
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('frontpage')
