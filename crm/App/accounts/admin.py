from django.contrib import admin

# Register your models here.
from .models import *

#Nuevo Nombre
admin.site.site_header = '(CRM) Customer Relationship Management'

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Tag)