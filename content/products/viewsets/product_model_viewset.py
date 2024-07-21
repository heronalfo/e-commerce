"""
product_model_viewset.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    ProsuctModelViewSet: This class is responsible for creating a new viewset.

Author:
    Pypeu (heronalfo)
"""

from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema

from core.viewsets import BaseModelViewSet
from core.permissions import IsSeller

from ..serializers import ProductModelSerializer
from ..models import Product
from ..filters import ProductFilters

class ProductModelViewSet(BaseModelViewSet):
    '''
    Model ViewSet for creating, deleting, editing and listing products.
    '''
    serializer_class = ProductModelSerializer
    filterset_class = ProductFilters
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'delete', 'patch', 'head', 'options']

    def perform_create(self, serializer):
        '''
        Override the default Django function to assign the seller attribute to the product.
        '''
        serializer.save(seller=self.request.user)
        return super().perform_create(serializer)

    def get_permissions(self):
        '''
        Apply permissions to objects allowing only 
        the account owner to edit or delete their products.
        '''
        if self.action in ['create', 'delete', 'partial_update']:
            return [IsSeller(), ]

        return super().get_permissions()

    @swagger_auto_schema(
        operation_description='Create a new product. Only sellers can create products.',
        responses={
            201: 'Product added to database successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized, only sellers can create new products'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete a product. Only sellers can delete products.',
        responses={
            204: 'Product deleted successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized, only sellers can delete products',
            404: 'Product not found',
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update a product. Only sellers can edit products.',
        responses={
            200: 'Product edited in database successfully',
            400: 'There was an error in the request',
            401: 'Action not authorized, only sellers can edit products',
            404: 'Product not found',
        }
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)
