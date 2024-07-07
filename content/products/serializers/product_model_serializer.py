'''
product_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    ProductModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from ..models import Product, Category

#pylint: disable=line-too-long

class ProductModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and validation of product data through the model.
    
    :validates:
     Checks if the filled category exists in the database.
    '''

    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = Product
        fields = ['id', 'seller', 'name',
        'category', 'description', 'price',
        'brand', 'stock',
        'created_at']

        read_only_fields = ['id', 'seller',
        'created_at', ]

    def validate_category(self, category):
        '''
        Checks if the category exists.
        '''

        if not Category.objects.filter(id=category.id).exists():
            raise serializers.ValidationError(_('The entered category does not exist in the database'))

        return category

    def validate_price(self, price):
        '''
        Validates if the price is less than 0.1.
        '''
        if price < 0.1:
            raise serializers.ValidationError(_('The price must be greater than 0'))

        return price
