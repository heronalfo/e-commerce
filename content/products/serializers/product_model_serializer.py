from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from ..models import Product, Category

class ProductModelSerializer(serializers.ModelSerializer):
    '''
    Serialization and validation of product data through the model
    
    :validates:
     Checks if the filled category exists in the database
    '''
    class Meta:
        model = Product
        fields = ['id', 'seller', 'name', 
        'category', 'description', 'price',         
        'brand', 'image', 'stock',
        'created_at']
        
        read_only_fields = ['id', 'seller', 'image', 
        'created_at', ]
    
    def validate_category(self, category):
        if not Category.objects.filter(id=category.id).exists():
            raise serializers.ValidationError(_('The entered category does not exist in the database'))
                
        return category
    
    def validate_price(self, price):
        if price < 0.1:
            raise serializers.ValidationError(_('The price must be greater than 0'))
            
        return price
        
    def validate_stock(self, stock):
        if stock < 0:
            raise serializers.ValidationError(_('It is not possible to register with a number less than 0'))
                 
        return stock