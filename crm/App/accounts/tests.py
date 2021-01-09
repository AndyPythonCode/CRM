from django.test import TestCase
from .models import *
import datetime

print("")
#Inicio ------------------------------------------------------------------------------------
Orders = Order.objects.all()

for element in Orders:
    print(f"Customer: {element.customer.name} Productos: {element.product.name} Status: {element.status} Tag: {[i.name for i in element.product.tags.filter()]}")
#Fin ----------------------------------------------------------------------------------------
print("")