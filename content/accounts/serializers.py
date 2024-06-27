from django.contrib.auth.models import User
from rest_framework import serializers
import re
from .models import Costumer

class CostumerSerializer(serializers.ModelSerializer):
    '''
    Serializes and validates costumer information through the database
    
    :validates: 
     If the username is longer than 32 characters
     Checks if the username is in the slug pattern
     
     Check if the password contains less than 8 characters, if it is a weak password
     
     Chefk if the CPF according to Brazilian standard,otherwise it raises an exception
     
     Checks if the zip code is in the Brazilian standard, otherwise it raises an exception
     
     Checks if the number is in the Brazilian standard     
       
    '''
    class Meta:
        model = Costumer
        fields = ['id', 'username', 'password', 
        'name', 'about', 'cpf', 'cep', 
        'number', 'address', 'cnpj',
        'name', 'about', 'number',
        'address',]
        
        read_only_fields = ['id', ]
                                        
    def validate_username(self, username):
        pattern = re.compile('^[a-z0-9]+(?:-[a-z0-9]+)*$')
        
        if len(username) > 32:
            raise serializers.ValidationError({'message': 'The username must not be longer than 32 characters'})
                           
        if re.match(pattern, username) is None:
            raise serializers.ValidationError({'message': 'The name for username is invalid, it should be like: "username-name"'})            
             
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'message': f'This username "{username}" already exists'})
            
        return username
                
    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError({'message': 'Password must contain at least 8 characters'})
            
        return password
        
    def validate_cpf(self, cpf):
        pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$') #123.456.789.01
        
        if not re.match(pattern, cpf):
            raise serializers.ValidationError({'message': 'The CPF sent does not comply with Brazilian standards. Example: 123.456.789.01'})
            
        return cpf
        
    def validate_cep(self, cep):
        pattern = re.compile(r'^\d{5}-\d{3}$') #12345-678
        
        if not re.match(pattern, cep):
            raise serializers.ValidationError({'message': 'The CEP sent does not comply with Brazilian standards. Example: 12345-678'})
            
        return cep
             
    def validate_number(self, number):
        pattern = re.compile(r'^\+\d{2} \(\d{2}\) \d{4,5} \d{4}$') #+55 (11) 9 1234 5678
        
        if not re.match(pattern, number):
            raise serializers.ValidationError({'message': 'The NUMBER sent does not comply with Brazilian standards. Example: +55 (11) 9 1234 5678'})
            
        return number