from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios_view, name='usuarios_view'),
    path('<str:username>/', views.usuarios_view, name='usuarios_view')
]
