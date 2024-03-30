from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def index(request):
    # Lógica de la vista aquí
    products = Product.objects.all() # Trae todos los projectos
    return render(request, 'index.html', 
    {'products': products})

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'message': 'El usuario ya existe'})
            except ValueError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'message': 'Porfavor ingrese datos validos'})

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'message': "Las contraseñas no coinciden"})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('index')
        
        
@login_required          
def signout(request):
    logout(request)
    return redirect('index')

@login_required
@login_required
def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {'product': product})

    