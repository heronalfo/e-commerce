'''
order_item_model_admin.py

This module offers a panel for managing order items

for more informations: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Author:
    PyPeu (heronalfo)
'''

from ..models import OrderItem
from django.contrib import admin

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''
    Registers a new panel for manipulating this table.
    '''
    ...
