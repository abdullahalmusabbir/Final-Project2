from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<int:id>/', views.customer_detail, name='customer_detail'),
    path('customer/new/', views.customer_create, name='customer_create'),
    path('customer/<int:id>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:id>/delete/', views.customer_delete, name='customer_delete'),
]