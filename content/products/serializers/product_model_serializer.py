'''
product_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    ProductModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from ..models import Product, Category, Tag

#pylint: disable=line-too-long

class ProductModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and validation of product data through the model.

    :validates:
     Checks if the filled category exists in the database.
    '''

    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False)
    tags_removed = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False)

    class Meta:
        '''
        Meta data manipulation for Category.
        '''

        model = Product
        fields = ['id', 'seller', 'name',
        'category', 'description', 'price',
        'brand', 'stock', 'tags',
        'tags_removed', 'uuid', 'created_at', 
        'updated_at', ]

        read_only_fields = ['id', 'seller', 'tags',
        'tags_removed', 'created_at', 'uuid',
        'created_at', 'updated_at', ]

    def validate_category(self, category):
        '''
        Checks if the category exists.
        '''

        if not Category.objects.filter(id=category.id).exists():
            raise serializers.ValidationError(_('The entered category does not exist in the database'))

        return category

    def validate_price(self, price):
        '''
        Validates if the price is less than 0.1.
        '''
        if price < 0.1:
            raise serializers.ValidationError(_('The price must be greater than 0'))

        return price

    def validate_tags(self, tags: list):
        '''
        Checks if the tag exists in the database and if the number of tags to be added is less than 15.
        '''
        if len(tags) > 15:
            raise serializers.ValidationError(_('Exceeded the limit of possible tags to be added'))

        for tag in tags:
            if not Tag.objects.all().filter(id=tag.id).exists():
                raise serializers.ValidationError(_('The tag does not exist in the database'))

        return tags

    def validate_tags_removed(self, tags_removed: list):
        '''
        Checks if the tag exists on the product so that it is removable.
        '''
        product = self.instance

        for tag in tags_removed:
            if tag not in product.tags.all():
                raise serializers.ValidationError(_('The tag does not exist in the database'))

        return tags_removed

    def create(self, validated_data):
        '''
        Overrides the function so that there are no problems creating products.
        '''

        tags_removed = validated_data.pop('tags_removed', None) #pylint: disable=unused-variable
        product = super().create(validated_data)

        if tags:= validated_data.pop('tags', None):
            product.tags.add(*tags)

        return product

    def update(self, instance, validated_data):
        '''
        Overrides the function to add or remove tags.
        '''
        product = super().update(instance, validated_data)

        if tags:= validated_data.pop('tags', None):
            product.tags.add(*tags)

        if tags_removed:= validated_data.pop('tags_removed', None):
            product.tags.remove(*tags_removed)

        return product
