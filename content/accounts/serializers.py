from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.status import (HTTP_400_BAD_REQUEST)
from re import compile, match
from .models import Costumer

class CostumerSerializer(serializers.ModelSerializer):
    '''
    Proper cleaning of received data,
    checks the length, naming pattern,
    and whether there is 
    '''
    class Meta:
        model = Costumer
        fields = ['id', 'username', 'password']
        read_only_fields = ['id',] 
                       
    def validate_username(self, username):
        pattern = compile('^[a-z0-9]+(?:-[a-z0-9]+)*$')
        
        if len(username) > 32:
            raise serializers.ValidationError({'detail': 'The username must not be longer than 32 characters'})
                           
        if match(pattern, username) is None:
            raise serializers.ValidationError({'detail': 'The name for username is invalid, it should be like: "username-name"'})            
             
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'detail': f'This username "{username}" already exists'})
            
        return username
        
    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError({'detail': 'Password must contain at least 8 characters'})
            
        return password
    