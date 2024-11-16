from django.contrib import admin
from django.urls import include, path
from accounts import views

urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('login/', views.loginPage, name= 'login'),
    path('logout/', views.logoutUser, name= 'logout'),
    
]