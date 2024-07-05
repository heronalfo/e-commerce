from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .product_model_serializer import ProductModelSerializer
from ..models import Order, Product

class OrderModelSerializer(serializers.ModelSerializer):
    add_product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=False, write_only=True, required=False)
    remove_products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, write_only=True, required=False)
    products = ProductModelSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'products', 'ordered_at',
            'complete', 'shipping_address',
            'payment_method', 'add_product', 'remove_products',
        ]
        read_only_fields = [
            'id', 'products', 'ordered_at', 'complete', 
            'payment_method', 'customer',
            'add_product', 'remove_products',
        ]

    def validate_add_product(self, product):                    
        if not Product.objects.filter(id=product.id).exists():
            raise serializers.ValidationError(_('The product does not exist in the database'))
        return product

    def validate_remove_products(self, products):        
        for product in products:
            if not Product.objects.filter(id=product.id).exists():
                raise serializers.ValidationError(_('Product %(id)s does not exist in the database') % {'id': product.id})
        return products

    def create(self, validated_data):
        add_product = validated_data.pop('add_product', None)
        remove_products = validated_data.pop('remove_products', [])
        order = super().create(validated_data)
        
        if add_product:
            order.products.add(add_product)
            
        for product in remove_products:
            order.products.remove(product)
            
        return order

    def update(self, instance, validated_data):
        add_product = validated_data.pop('add_product', None)
        remove_products = validated_data.pop('remove_products', [])
        instance = super().update(instance, validated_data)
        
        if add_product:
            instance.products.add(add_product)
            
        for product in remove_products:
            instance.products.remove(product)
            
        return instance