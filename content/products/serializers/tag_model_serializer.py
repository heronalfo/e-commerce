'''
tag_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    TagModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''
from rest_framework import serializers
from ..models import Tag

class TagModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and hygiene of Tag.
    '''

    class Meta:
        '''
        Meta data manipulation for Tag.
        '''

        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id',]
