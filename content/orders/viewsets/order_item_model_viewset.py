'''
order_item_model_viewset.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    OrderItemModelViewSet: This class is responsible for creating a new viewset

Author:
    Pypeu (heronalfo)
'''

from drf_yasg.utils import swagger_auto_schema
from .order_model_viewset import OrderModelViewSet
from ..serializers import OrderItemModelSerializer
from ..models import OrderItem

class OrderItemModelViewSet(OrderModelViewSet):
    '''
    This class is responsible for operating CRUD functionalities
    '''
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemModelSerializer

    def perform_update(self, serializer):
        serializer.save()

    @swagger_auto_schema(
        operation_description='Create a new order item. Only authenticated users can create orders itens.',
        responses={
            201: 'Order item added to database successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can create new orders itens',
            403: 'Only authenticated users can create an order item'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update an order item. Only the owner can update orders itens.',
        responses={
            200: 'Order edited successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can edit orders itens',
            403: 'Only owners can edit an order item',
            404: 'order item not found'
        }
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete an order item. Only the owner can delete orders itens.',
        responses={
            204: 'Order item successfully deleted',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can delete orders itens',
            403: 'Only owners can delete an order item',
            404: 'Order item not found'
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)
