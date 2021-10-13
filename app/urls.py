from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('', views.home,name='home'),
    path('new/', views.createRecord,name='CreateRecord'),
    path('delete/<str:pk>/', views.DeleteRecord,name='DeleteRecord'),
    path('update/<str:pk>/', views.UpdateRecord,name='UpdateRecord'),
  
]
