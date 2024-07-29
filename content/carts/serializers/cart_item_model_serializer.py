'''
cart_item_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    CartItemModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from products.models import Product
from ..models import Cart, CartItem

class CartItemModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and hygiene of Order items.
    '''
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), many=False, write_only=True, required=False)

    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = CartItem
        fields = ['id', 'product', 'quantity',
        'uuid', 'created_at', 'updated_at',
        'cart', ]

        read_only_fields = ['id', 'uuid', 'created_at', 
        'updated_at', 'cart', ]

    def validate_product(self, product):
        '''
        Checks if the product exists in the database
        '''

        if not Product.objects.all().filter(id=product.id).exists():
            raise serializers.ValidationError(_('The product does not exist in the database'))

        return product
    
    def validate_cart(self, cart):
        '''
        Checks if the cart exists in the database
        '''

        if not Cart.objects.all().filter(id=cart.id).exists():
            raise serializers.ValidationError(_('The cart does not exist in the database'))

        return cart