from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Customer


class CustomerSetting(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('user',)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldName in ['username','email','password1','password2']:
            self.fields[fieldName].help_text = None
            self.fields[fieldName].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
