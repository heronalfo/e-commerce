from drf_yasg.utils import swagger_auto_schema
from .product_model_viewset import ProductModelViewSet
from ..models import Category
from ..serializers import CategoryModelSerializer

class CategoryModelViewSet(ProductModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    
    def perform_create(self, serializer):
        serializer.save()
             
    @swagger_auto_schema(
        operation_description='Create a new category. Only costumers and sellers can create categories.',
        responses={
            201: 'Category added to database successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only costumer can create new categories'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete a category. Only sellers can delete category.',
        responses={
            204: 'Category deleted successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only costumer can delete categories',
            404: 'Category not found',
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update a category. Only coetumer can edit categories.',
        responses={
            200: 'Category edited in database successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only costumer can edit category',
            404: 'Category not found',
        }
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)