'''
order_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    OrderModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from ..models import Order, OrderItem

#pylint: disable=line-too-long

class OrderModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and hygiene of Orders
    '''
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), many=False, write_only=True, required=False)
    item = serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all(), many=False, write_only=True, required=False)
    items_removed = serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all(), many=True, write_only=True, required=False)

    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = Order
        fields = [
            'id', 'customer', 'order', 'ordered_at',
            'complete', 'shipping_address', 'payment_method',
            'item', 'items_removed',
        ]
        read_only_fields = [
            'id', 'ordered_at', 'order', 'complete', 'payment_method', 
            'customer', 'shipping_address',
        ]

    def validate_item(self, item):
        '''
        Checks if the item exists in the database.
        '''
        if not OrderItem.objects.filter(id=item.id).exists():
            raise serializers.ValidationError(_('The product %(id)s does not exist in the database') % {'id': item.id})
        return item

    def validate_items_removed(self, items):
        '''
        Checks if the item exists in the database
        '''
        for item in items:
            if not OrderItem.objects.filter(id=item.id).exists():
                raise serializers.ValidationError(_('The product %(id)s does not exist in the database') % {'id': item.id})
        return items

    def create(self, validated_data):
        '''
        Overridden method for saving OrderItems Instances.
        '''
        
        #pylint: disable=unused-variable
        item = validated_data.pop('item', None)
        items_removed = validated_data.pop('items_removed', [])

        order = super().create(validated_data)

        return order

    def update(self, instance, validated_data):
        '''
        Overridden method for updating OrderItem instances.
        '''
        item = validated_data.pop('item', None)
        items_removed = validated_data.pop('items_removed', [])

        instance = super().update(instance, validated_data)

        if item:
            instance.products.add(item)

        if items_removed:
            for item in items_removed:
                instance.products.remove(item)

        return instance
