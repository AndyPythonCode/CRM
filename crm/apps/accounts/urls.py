from django.urls import path
from . import views

urlpatterns = [
    path("", views.DashBoard, name='home'),
    path("products/", views.Products, name='product'),
    path("customer/<str:pk>/", views.Customer, name='customer'),
    path('order_created/',views.order_created, name='order_created'),
    path('order_updated/<str:pk>/',views.order_updated, name='order_updated'),
    path('order_delete/<str:pk>/',views.order_delete, name='order_delete'),
]
