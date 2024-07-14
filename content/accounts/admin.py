'''
admin.py

This module offers a panel for managing products

for more informations: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Author:
    PyPeu (heronalfo)
'''

from .models import Costumer
from django.contrib import admin

@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    ...
