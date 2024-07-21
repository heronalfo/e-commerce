'''
review_model_admin.py

This module offers a panel for managing reviews

for more informations: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

Author:
    PyPeu (heronalfo)
'''

from django.contrib import admin
from ..models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''
    Registers a new panel for manipulating this table.
    '''
    ...
