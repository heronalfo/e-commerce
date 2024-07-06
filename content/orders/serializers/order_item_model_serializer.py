from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from products.models import Product
from ..models import OrderItem, Order

class OrderItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['id', ]
        
    def validate_product(self, product):
        if not Product.objects.all().filter(id=product.id).exists():
            raise serializers.ValidationError(_('The product does not exist in the database'))
        
        return product
    
    def validate_order(self, order):
        if not Order.objects.all().filter(id=order.id).exists():
            raise serializers.ValidationError(_('The order does not exist in the database'))
        
        return order
        