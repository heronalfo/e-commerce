from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
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
        'created_at', ]
        
        read_only_fields = ['id', 'seller', 'image', 
        'created_at', ]
    
    def validate(self, attrs):
        _validate = super().validate(attrs)
        
        category_id = attrs.get('category').id
        if not Category.objects.filter(id=category_id).exists():
            raise serializers.ValidationError({'message': 'The entered category does not exist in the database'})
                
        return _validate