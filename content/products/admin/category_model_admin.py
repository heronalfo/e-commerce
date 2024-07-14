'''
category_model_admin.py

This module offers a panel for managing categories

for more informations: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Author:
    PyPeu (heronalfo)
'''

from django.contrib import admin
from ..models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
