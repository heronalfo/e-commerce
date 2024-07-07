'''
review_model_serializer.py

This module is responsible for serializing and sanitizing the received data.
for more informations: https://www.django-rest-framework.org/api-guide/serializers/

Classes:
    ReviewModelSerializer: This class is responsible for serializing and 
    validating the received data.

Author:
    PyPeu (heronalfo)
'''
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from ..models import Review, Product

#pylint: disable=line-too-long

class ReviewModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and hygiene of Reviews
    
    Validates:
      Checks if the rating is between the range of 1 and 5
      
      Check if the product you are commenting on exists
    '''

    class Meta:
        '''
        Meta data manipulation for Reviews
        '''
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'customer', 'commented_at']

    def validate_rating(self, rating):
        '''
        Checks if the range is between 1 and 5
        '''

        if rating not in range(1, 6):
            raise serializers.ValidationError(_('The rating must be in the range between 1 and 5'))

        return rating

    def validate_product_id(self, product_id):
        '''
        Checks if the product exists in the database.
        '''

        if not Product.objects.all().filter(id=product_id.id).exists():
            raise serializers.ValidationError(_('The entered product does not exist in the database'))

        return product_id
