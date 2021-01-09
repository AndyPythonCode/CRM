from django.urls import path
from . import views

urlpatterns = [
    path("", views.DashBoard, name='home'),

    #Login
    path("login/", views.Login, name='login'),
    path("register/", views.register, name='register'),
    path("logout/", views.Logout, name='logout'),

    path("products/", views.Products, name='product'),
    path("user/", views.userPage, name= 'user-page'),
    path("settings/", views.setting_user, name= 'user-setting'),
    path("customer/<str:pk>/", views.Customer, name='customer'),
    path('order_created/<str:pk>/',views.order_created, name='order_created'),
    path('order_updated/<str:pk>/',views.order_updated, name='order_updated'),
    path('order_delete/<str:pk>/',views.order_delete, name='order_delete'),
]
