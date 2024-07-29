'''
cart_item_model_admin.py

This module offers a panel for managing cart items

for more informations: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Author:
    PyPeu (heronalfo)
'''

from django.contrib import admin
from ..models import CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    '''
    Registers a new panel for manipulating this table.
    '''
    ...
