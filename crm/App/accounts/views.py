from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.admin import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#each model
from .models import Customer as cus
from .models import *
from .forms import OrderForm, MyUserCreationForm, CustomerSetting
from .filters import *
from .decorators import unathenticated_user, user_allow, only_admin

@unathenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('accounts:home')
        else:
            messages.info(request, "Username and Password doesn't match ")

    context = {}
    return render(request, 'accounts/login/login.html', context)

def Logout(request):
    logout(request)
    return redirect('accounts:login')

@login_required(login_url='accounts:login')
@user_allow(roles=('customer'))
def setting_user(request):
    customer = request.user.customer
    form = CustomerSetting(instance=customer)
    if request.method == "POST":
        form = CustomerSetting(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/setting.html',context)

@login_required(login_url='accounts:login')
@user_allow(roles=('customer'))
def userPage(request):
    orders = request.user.customer.order_set.all()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    total_order = orders.count()

    context = {'orders':orders, 'total_order':total_order, "delivered":delivered, 'pending':pending}
    return render(request, 'accounts/user.html', context)

@unathenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        form = MyUserCreationForm()
        if request.method == 'POST':
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, f'Account was created for {user.username}')
                return redirect('accounts:login')
        context = {'form':form}
        return render(request, 'accounts/login/register.html', context)   

@login_required(login_url='accounts:login')
@only_admin
def DashBoard(request):
    customers = cus.objects.all()
    orders = Order.objects.all()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    total_order = orders.count()

    context = {"customers":customers, 'orders':orders, 'total_order':total_order, "delivered":delivered, 'pending':pending}

    return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='accounts:login')
@only_admin
def Products(request):
    Products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':Products})

@login_required(login_url='accounts:login')
@only_admin
def Customer(request, pk):
    customer = cus.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    filters = OrderFilter(request.GET, queryset=orders)
    #Es donde vamos a filtar, estaran cada unos de los componentes en la tabla a filtar
    orders = filters.qs

    context = {'customers':customer, 'order':orders, 'total_orders':total_orders, 'filter':filters}
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='accounts:login')
@only_admin
def order_created(request, pk):
    OrderFormSet = inlineformset_factory(cus, Order, fields=('product','status'), extra=3)
    customer = cus.objects.get(id=pk)
    formSet = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formSet = OrderFormSet(request.POST, instance=customer)
        if formSet.is_valid():
            formSet.save()
            return redirect('accounts:home')     
    context = {'form':formSet}
    return render(request, 'accounts/forms/order_created.html', context)

@login_required(login_url='accounts:login')
@only_admin
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

@login_required(login_url='accounts:login')
@only_admin
def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    url_back = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        order.delete()
        return redirect('accounts:home')
    context = {'item':order, 'url_back':url_back}
    return render(request, 'accounts/forms/order_delete.html', context)