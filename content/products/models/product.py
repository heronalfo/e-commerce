from accounts.models import Costumer
from django.db import models
from .category import Category

class Product(models.Model):
    '''
    Registration of products available for sale, name, category, price, and... 
    '''
    seller = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='costumer')
    name = models.CharField(max_length=64, db_index=True)
    description = models.CharField(max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category')
    price = models.FloatField()
    brand = models.CharField(max_length=64, blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:    
        ordering = ['-created_at']
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.name