from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.responsables_economicos_view,name='responsables_economicos_view')
]