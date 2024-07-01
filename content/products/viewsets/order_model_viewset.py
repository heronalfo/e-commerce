from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .product_model_viewset import ProductModelViewSet
from ..serializers import OrderModelSerializer
from ..permissions import IsOwner
from ..models import Order

class OrderModelViewSet(ProductModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    
    def perform_create(self, serializer):       
        order = serializer.save(customer=self.request.user)
    
    def perform_update(self, serializer):
        add_product = serializer.validated_data.pop('add_product', [])
        remove_products = serializer.validated_data.pop('remove_products', [])
        order = serializer.save()
         
        if add_product:
            order.products.add(*add_product)
                                
        if remove_products:
            order.products.remove(*remove_products) 
                   
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['list', 'destroy', 'update']:
            return [IsOwner()]
        return super().get_permissions()
     
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