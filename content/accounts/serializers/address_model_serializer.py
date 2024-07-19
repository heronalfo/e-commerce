'''
address_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    AddressModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''

import re
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Address

#pylint: disable=line-too-long
class AddressModelSerializer(serializers.ModelSerializer):
    '''
    Serializes and validates costumer information through the database.
    '''
    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = Address
        fields = ['id', 'costumer', 'road',
        'cep', 'number', 'complement', 
        'neighborhood', 'uf', 'city', ]

        read_only_fields = ['id', 'costumer']
        
    def validate_cep(self, cep):
        '''
        Checks if the zip code is in the Brazilian standard, otherwise it raises an exception.
        '''

        pattern = re.compile(r'^\d{5}-\d{3}$') #12345-678

        if not re.match(pattern, cep):
            raise serializers.ValidationError({'message': 'The CEP sent does not comply with Brazilian standards. Example: 12345-678'})

        return cep

    def validate_number(self, number):
        '''
        Checks if the number is in the Brazilian standard.   
        '''
        pattern = re.compile(r'^\+\d{2} \(\d{2}\) \d{4,5} \d{4}$') #+55 (11) 9 1234 5678

        if not re.match(pattern, number):
            raise serializers.ValidationError({'message': 'The NUMBER sent does not comply with Brazilian standards. Example: +55 (11) 9 1234 5678'})

        return number
