from django.urls import path
from . import views

urlpatterns = [
    path("", views.DashBoard, name='home'),
    path("products/", views.Products, name='product'),
    path("customer/", views.Customer, name='customer'),
]
