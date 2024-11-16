from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import path

from .forms import CreateUserForm



def register(request):
    if request.user.is_authenticated:
        return redirect('/home_login')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')

    dicc = {'form':form}
    return render(request, 'register.html', dicc )

def loginPage(request):
    form = AuthenticationForm()
    if request.user.is_authenticated:
        return redirect('/home_login')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home_login')

    dicc = {'form':form}
    return render(request, 'login.html', dicc )

def logoutUser(request):
    logout(request)
    return redirect('/')