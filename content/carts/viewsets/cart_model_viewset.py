"""
cart_model_viewset.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    CartModelViewSet: This class is responsible for creating a new viewset

Author:
    Pypeu (heronalfo)
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from core.viewsets import BaseModelViewSet
from core.permissions import IsOwner
from ..serializers import CartModelSerializer
from ..models import Cart

class CartModelViewSet(BaseModelViewSet):
    '''
    This class is responsible for operating CRUD functionalities
    '''
    queryset = Cart.objects.all() #pylint: disable=no-member
    serializer_class = CartModelSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def perform_create(self, serializer):
        """
        Saves the cart instance after creation, associating it with the current customer. 
        """
        serializer.save(costumer=self.request.user)
        return super().perform_create(serializer)

    def get_permissions(self):
        """
        Sets permissions based on the requested action.
        """
        if self.action in ['list', 'create']:
            return [IsAuthenticated(),]

        if self.action in ['update', 'destroy']:
            return [IsOwner(),]

        return super().get_permissions()

    @swagger_auto_schema(
        operation_description='Create a new cart. Only authenticated users can create carts.',
        responses={
            201: 'Cart added to database successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can create new carts',
            403: 'Only authenticated users can create an cart'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update an cart. Only the owner can update carts.',
        responses={
            200: 'Cart edited successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can edit carts',
            403: 'Only owners can edit an cart',
            404: 'Cart not found'
        }
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete an cart. Only the owner can delete carts.',
        responses={
            204: 'Cart successfully deleted',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can delete carts',
            403: 'Only owners can delete an cart',
            404: 'Cart not found'
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)
