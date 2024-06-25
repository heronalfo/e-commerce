from accounts.models import Costumer
from django.db import models
from .product import Product

class Review(models.Model):
    '''
    Buyer review of the product 
    '''
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=150, blank=True, db_index=True)
    commented_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:    
        ordering = ['-commented_at']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
          
    def __str__(self):
        return self.comment
