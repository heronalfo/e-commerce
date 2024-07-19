'''
costumer_model_admin.py

This module offers a panel for managing products

for more informations: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Author:
    PyPeu (heronalfo)
'''

from django.contrib import admin
from ..models import Costumer

@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    ...
