'''
costumer_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    CostumerModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''

import re
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Costumer

#pylint: disable=line-too-long
class CostumerModelSerializer(serializers.ModelSerializer):
    '''
    Serializes and validates costumer information through the database.
    '''
    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = Costumer
        fields = ['id', 'username', 'password',
        'name', 'about', 'cpf', 
        'number', ]

        read_only_fields = ['id', 'address',]

    def validate_username(self, username):
        '''
        Checks if the username is in the slug pattern.
        '''
        pattern = re.compile('^[a-z0-9]+(?:-[a-z0-9]+)*$')

        if len(username) > 32:
            raise serializers.ValidationError({'message': 'The username must not be longer than 32 characters'})

        if re.match(pattern, username) is None:
            raise serializers.ValidationError({'message': 'The name for username is invalid, it should be like: "username-name"'})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'message': f'This username "{username}" already exists'})

        return username

    def validate_password(self, password):
        '''
        Check if the password contains less than 8 characters, if it is a weak password.
        '''
        if len(password) < 8:
            raise serializers.ValidationError({'message': 'Password must contain at least 8 characters'})

        return password

    def validate_cpf(self, cpf):
        '''
        Checks if the CPF according to Brazilian standard,otherwise it raises an exception.
        '''
        pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$') #123.456.789.01

        if not re.match(pattern, cpf):
            raise serializers.ValidationError({'message': 'The CPF sent does not comply with Brazilian standards. Example: 123.456.789.01'})

        return cpf
    
    def validate_number(self, number):
        '''
        Checks if the number is in the Brazilian standard.   
        '''
        pattern = re.compile(r'^\+\d{2} \(\d{2}\) \d{4,5} \d{4}$') #+55 (11) 9 1234 5678

        if not re.match(pattern, number):
            raise serializers.ValidationError({'message': 'The NUMBER sent does not comply with Brazilian standards. Example: +55 (11) 9 1234 5678'})

        return number
