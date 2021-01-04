from django.shortcuts import render, redirect
#each model
from .models import Customer as cus
from .models import *
from .forms import OrderForm

def DashBoard(request):
    customers = cus.objects.all()
    orders = Order.objects.all()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    total_order = orders.count()

    context = {"customers":customers, 'orders':orders, 'total_order':total_order, "delivered":delivered, 'pending':pending}

    return render(request, 'accounts/dashboard.html',context)

def Products(request):
    Products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':Products})

def Customer(request, pk):
    customer = cus.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {'customers':customer, 'order':orders, 'total_orders':total_orders}
    return render(request, 'accounts/customer.html', context)

def order_created(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:home')     
    context = {'form':form}
    return render(request, 'accounts/forms/order_created.html', context)

def order_updated(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    url_back = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('accounts:home')

    context = {'form':form, 'url_back':url_back}
    return render(request, 'accounts/forms/order_created.html', context)

def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    url_back = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        order.delete()
        return redirect('accounts:home')
    context = {'item':order, 'url_back':url_back}
    return render(request, 'accounts/forms/order_delete.html', context)