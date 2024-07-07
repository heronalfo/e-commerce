"""
viewsets.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    CostumerModelViewSet: This class is responsible for creating a new viewset.

Author:
    Pypeu (heronalfo)
"""

from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from drf_yasg.utils import swagger_auto_schema

from .serializers import CostumerSerializer
from .models import Costumer
from .permissions import IsOwnerOfUser

class CostumerModelViewSet(ModelViewSet):
    '''
    Viewset for creating, updating and editing the user to obtain their access token
    '''
    serializer_class = CostumerSerializer
    queryset = Costumer.objects.all()
    parser_classes = [JSONParser,  XMLParser]
    renderer_classes = [JSONRenderer, XMLRenderer]
    http_method_names = ['post', 'delete', 'patch', 'head', 'options']

    def get_object(self):
        '''
        Get the object (user) and apply the appropriate permissions        
        :returns: 

         User.objects whether the object was found
         404 Not found if the object was not found         
        '''
        obj = get_object_or_404(self.get_queryset(), id=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)

        return obj

    def get_permissions(self):
        '''
        Applies the appropriate permissions to objects, meaning that only 
        the account owner can edit or delete their account.
        '''
        if self.action in ['delete', 'patch']:
            return [IsOwnerOfUser()]

        return super().get_permissions()

    @swagger_auto_schema(
        operation_description='Create, authenticate and log in new users',
        responses={
            201: 'User created successfully',
            400: "There was a problem with the customer's request"
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Allows the user to delete their own account',
        responses={
            200: 'Account removed successfully',
            400: 'There was an error in the request',
            401: 'Only users can remove their own accounts',
            404: 'Account not found'
        }
    )
    def destroy(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Allows you to perform a partial update',
        responses={
            200: 'Your account has been updated successfully',
            400: 'There was an error in the request',
            401: 'Only users can update their own accounts',
            404: 'Account not found'
        }
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)
