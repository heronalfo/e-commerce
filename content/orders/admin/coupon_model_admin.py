'''
coupon_model_admin.py

This module offers a panel for managing cupons.

for more informations: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Author:
    PyPeu (heronalfo)
'''

from ..models import Coupon
from django.contrib import admin

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    '''
    Registers a new panel for manipulating this table.
    '''
    ...
