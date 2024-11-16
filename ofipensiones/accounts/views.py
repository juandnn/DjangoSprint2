from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    dicc = {'form':form}
    return render(request, 'register.html', dicc )

def login(request):
    dicc = {'welcome_text':'Holaaa!!! '}
    return render(request, 'login.html', dicc )