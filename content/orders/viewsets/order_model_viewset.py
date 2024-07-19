"""
order_model_viewset.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    OrderModelViewSet: This class is responsible for creating a new viewset

Author:
    Pypeu (heronalfo)
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from core.viewsets import BaseModelViewSet
from products.permissions import IsOwner
from ..serializers import OrderModelSerializer
from ..models import Order

class OrderModelViewSet(BaseModelViewSet):
    '''
    This class is responsible for operating CRUD functionalities
    '''
    queryset = Order.objects.all() #pylint: disable=no-member
    serializer_class = OrderModelSerializer
    http_method_names = ['get', 'post', 'delete', 'patch', 'head', 'options']

    def perform_create(self, serializer):
        """
        Saves the order instance after creation, associating it with the current customer. 
        """
        serializer.save(costumer=self.request.user)
        return super().perform_create(serializer)

    def get_permissions(self):
        """
        Sets permissions based on the requested action.
        """
        if self.action == 'create':
            return [IsAuthenticated(),]

        if self.action in ['list', 'destroy', 'partial_update']:
            return [IsAuthenticated(), IsOwner()]

        return super().get_permissions()

    def get_queryset(self):
        '''
        Overrides the function so that only the owner sees their own orders.
        '''
        queryset = super().get_queryset().filter(costumer=self.request.user)
        
        return queryset

    @swagger_auto_schema(
        operation_description='Create a new order. Only authenticated users can create orders.',
        responses={
            201: 'Order added to database successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can create new orders',
            403: 'Only authenticated users can create an order'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update an order. Only the owner can update orders.',
        responses={
            200: 'Order edited successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can edit orders',
            403: 'Only owners can edit an order',
            404: 'Order not found'
        }
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete an order. Only the owner can delete orders.',
        responses={
            204: 'Order successfully deleted',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can delete orders',
            403: 'Only owners can delete an order',
            404: 'Order not found'
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)
