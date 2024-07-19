'''
filters.py

This module is responsible for creating filters for searching for products.
for more informations: https://django-filter.readthedocs.io/en/stable/

Class: 
    ProductFilters: This class creates an extension for viewsets

Author:
    PyPeu (heronalfo)
'''

from django_filters import rest_framework as filters
from .models import Product, Review

class ProductFilters(filters.FilterSet):
    '''
    Creates an extension so that it can be used in viewsets.
    '''
    class Meta:
        '''
        Overriding metadata to add filters.
        '''
        model = Product
        fields = {
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'category': ['exact'],
            'price': ['gte', 'lte'],
            'created_at': ['gte', 'lte'],
            'stock': ['gte', 'lte'],
        }

class ReviewFilters(filters.FilterSet):
    '''
    Creates an extension so that it can be used in viewsets.
    '''
    class Meta:
        '''
        Overriding metadata to add filters.
        '''
        model = Review
        fields = {
            'comment': ['exact', 'icontains'],
            'created_at': ['gte', 'lte'],
        }
