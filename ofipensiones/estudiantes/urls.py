from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.estudiantes_view, name='estudiantes_view'),
    path('<int:id>/', views.estudiantes_view, name='estudiantes_view')
]

