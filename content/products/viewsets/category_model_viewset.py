"""
category_model_viewset.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    CategoryModelViewSet: This class is responsible for creating a new viewset.

Author:
    Pypeu (heronalfo)
"""

from drf_yasg.utils import swagger_auto_schema

from .product_model_viewset import ProductModelViewSet
from ..models import Category
from ..serializers import CategoryModelSerializer

class CategoryModelViewSet(ProductModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    queryset = Category.objects.all() #pylint: disable=no-member
    serializer_class = CategoryModelSerializer

    def perform_create(self, serializer):
        """
        Save the category instance after creation.
        """
        serializer.save()

    @swagger_auto_schema(
        operation_description=(
            'Create a new category. Only customers and sellers can create categories.'
        ),
        responses={
            201: 'Category added to database successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only customers can create new categories'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete a category. Only sellers can delete categories.',
        responses={
            204: 'Category deleted successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only customers can delete categories',
            404: 'Category not found',
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update a category. Only customers can edit categories.',
        responses={
            200: 'Category edited in database successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only customers can edit categories',
            404: 'Category not found',
        }
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)
        