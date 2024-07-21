'''
order_item_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    OrderItemModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from products.models import Product
from ..models import OrderItem

class OrderItemModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and hygiene of Order items.
    '''

    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = OrderItem
        fields = '__all__'
        read_only_fields = ['id', 'uuid', 'created_at', 
        'updated_at', ]

    def validate_product(self, product):
        '''
        Checks if the product exists in the database
        '''

        if not Product.objects.all().filter(id=product.id).exists():
            raise serializers.ValidationError(_('The product does not exist in the database'))

        return product
