'''
cart_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    CartModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from ..models import Cart

class CartModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and hygiene of Carts
    '''

    class Meta:
        '''
        Meta data manipulation for Carts.
        '''

        model = Cart
        fields = ['id', 'costumer', 'category', 
        'name', 'uuid', 'created_at', 'updated_at']
         
        read_only_fields = ['id', 'costumer', 'category',
         'uuid', 'created_at', 'updated_at', 'name']