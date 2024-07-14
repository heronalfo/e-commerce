'''
wishlist_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    WishlistModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from products.models import Product
from ..models import Wishlist

class WishlistModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and hygiene of Wishlist items.
    '''

    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = Wishlist
        fields = ['id', 'product', 'costumer',]
        read_only_fields = ['id', 'costumer',]

    def validate_product(self, product):
        '''
        Checks if the product exists in the database
        '''

        if not Product.objects.all().filter(id=product.id).exists():
            raise serializers.ValidationError(_('The product does not exist in the database'))

        return product
