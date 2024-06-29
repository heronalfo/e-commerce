from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from ..models import Review, Product 

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'customer', 'commented_at']
        
    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(_('The rating cannot be less than 1 nor greater than 5'))
            
        return rating
        
    def validate_product_id(self, product_id):
        if not Product.objects.all().filter(id=product_id.id).exists():
            raise serializers.ValidationError(_('The entered product does not exist in the database'))
            
        return product_id