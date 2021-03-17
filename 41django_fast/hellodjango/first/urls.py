from django.contrib import admin
from django.urls import path, include
from first import views

urlpatterns = [
    path('', views.show_index, name='show_index'),
]
