from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .forms import CreateUserForm



def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    dicc = {'form':form}
    return render(request, 'register.html', dicc )

def login(request):
    form = AuthenticationForm()
    dicc = {'form':form}
    return render(request, 'login.html', dicc )