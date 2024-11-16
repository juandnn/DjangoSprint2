from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required()
def home_login(request):
    return render(request, 'login_home.html')