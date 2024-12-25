from django.contrib import admin
from django.urls import path,include
from basic_admin import views


app_name = 'basic_admin'

urlpatterns = [

    path('register',views.register,name = 'register')
]