from django.db import models

class OrderItem(models.Model):
    '''
    Product added to shopping cart, quantity and price 
    '''    
    product = models.ForeignKey('products.product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
        
    def __str__(self):
        return f"{self.product.name}"