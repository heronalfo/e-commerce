'''
wishlist_model_viewset.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    WishlistModelViewSet: This class is responsible for creating a new viewset

Author:
    Pypeu (heronalfo)
'''

from drf_yasg.utils import swagger_auto_schema
from .order_model_viewset import OrderModelViewSet
from ..serializers import WishlistModelSerializer
from ..models import Wishlist

class WishlistModelViewSet(OrderModelViewSet):
    '''
    This class is responsible for operating CRUD functionalities
    '''
    queryset = Wishlist.objects.all()
    serializer_class = WishlistModelSerializer
    http_method_names = ['post', 'delete', 'patch', 'head', 'options']
    
    def perform_update(self, serializer):
        serializer.save()

    @swagger_auto_schema(
        operation_description='Create a new Wishlist item. Only authenticated users can create wishlist itens.',
        responses={
            201: 'Wishlist item added to database successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can create new wishlists itens',
            403: 'Only authenticated users can create an wishlist item'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update an wishlist item. Only the owner can update wishlistss itens.',
        responses={
            200: 'Wishlist edited successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can edit wishlistss itens',
            403: 'Only owners can edit an wishlist item',
            404: 'Wishlist item not found'
        }
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete an wishlist item. Only the owner can delete wishlist itens.',
        responses={
            204: 'Wishlist item successfully deleted',
            400: 'There was an error in the request',
            401: 'Action not authorized. Only authenticated users can delete wishlist itens',
            403: 'Only owners can delete an wishlist item',
            404: 'wishlist item not found'
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)
