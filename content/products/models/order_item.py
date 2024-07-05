from django.db import models
from .product import Product

class OrderItem(models.Model):
    '''
    Product added to shopping cart, quantity and price 
    '''
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.quantity} x {self.product.name} @ {self.unit_price}"