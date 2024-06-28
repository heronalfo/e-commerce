from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .product_model_viewset import ProductModelViewSet
from ..models import Review
from ..serializers import ReviewModelSerializer
from ..permissions import IsOwner

class ReviewModelViewSet(ProductModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
        return super().perform_create(serializer)
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), ]
        
        if self.action in ['destroy', 'update']:
            return [IsOwner(), ]
        
        return super().get_permissions()
            
    @swagger_auto_schema(
        operation_description='Create a new review. Only costumers and sellers can create reviews.',
        responses={
            201: 'Review added to database successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only costumer can create new reviews'
        }
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Delete a review. Only sellers can delete review.',
        responses={
            204: 'Review deleted successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only costumer can delete reviews',
            404: 'Review not found',
        }
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)

    @swagger_auto_schema(
        operation_description='Update a Review. Only coetumer can edit reviews.',
        responses={
            200: 'Review edited in database successfully',
            400: 'There was an error in the request',
            403: 'Action not authorized, only costumer can edit review',
            404: 'Review not found',
        }
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)