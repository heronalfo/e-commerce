from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .product_model_serializer import ProductModelSerializer
from ..models import Order, Product

class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'products', 'ordered_at',
            'complete', 'transaction_id', 'shipping_address',
            'payment_method', 
        ]
        
        read_only_fields = [
            'id', 'products', 'ordered_at', 'complete', 
            'transaction_id', 'payment_method', 'costumer',
        ]
        
    products = ProductModelSerializer(many=True, read_only=True)
    add_product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=False, write_only=True, required=False)
    remove_products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, write_only=True, required=False)

    def validate_add_product(self, product):                    
        if not Product.objects.filter(id=product.id).exists():
            raise serializers.ValidationError(_('The product does not exist in the database'))
            
        return product

    def validate_remove_products(self, products):        
        for product in products:
            if not Product.objects.filter(id=product.id).exists():
                raise serializers.ValidationError(_(f'Product %(id) does not exist in the database') % {'id': product.id})
                
        return products