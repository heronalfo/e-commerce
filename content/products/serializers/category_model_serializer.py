'''
category_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    CategoryModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''
from rest_framework import serializers
from ..models import Category

class CategoryModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and hygiene of Categories.
    '''

    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id',]
