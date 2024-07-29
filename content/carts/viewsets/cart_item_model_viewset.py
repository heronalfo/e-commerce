'''
cart_item_model_viewset.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    CartItemModelViewSet: This class is responsible for creating a new viewset

Author:
    Pypeu (heronalfo)
'''

from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from core.viewsets import BaseModelViewSet
from core.permissions import IsOwner, IsOwnerOfCart
from ..serializers import CartItemModelSerializer
from ..models import CartItem

class CartItemModelViewSet(BaseModelViewSet):
    '''
    This class is responsible for operating CRUD functionalities
    '''
    queryset = CartItem.objects.all()
    serializer_class = CartItemModelSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        """
        Sets permissions based on the requested action.
        """
        if self.action == 'create':
            return [IsAuthenticated(), ]

        if self.action in ['get', 'update', 'destroy']:
            return [IsOwnerOfCart(), ]

        return super().get_permissions()

    def get_queryset(self):
        '''
        Overrides the function so that only the owner sees their own carts.
        '''
        queryset = super().get_queryset().filter(costumer=self.request.user)

        return queryset

    @swagger_auto_schema(
        operation_description='Create a new cart item. Only authenticated users can create carts itens.',
        responses={
            201: 'Cart item added to database successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can create new carts itens',
            403: 'Only authenticated users can create an cart item'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete an cart item. Only the owner can delete carts itens.',
        responses={
            204: 'Cart item successfully deleted',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can delete carts itens',
            403: 'Only owners can delete an cart item',
            404: 'Cart item not found'
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)
