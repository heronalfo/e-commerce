'''
order_model_admin.py

This module offers a panel for managing orders

for more informations: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Author:
    PyPeu (heronalfo)
'''

from ..models import Order
from django.contrib import admin

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''
    Registers a new panel for manipulating this table.
    '''
    ...
