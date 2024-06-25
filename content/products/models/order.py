from django.db import models
from .product import Product
from accounts.models import Costumer
class Order(models.Model):
    '''
    Shopping cart, list of products purchased, total price and shipping status 
    '''
    PAYMENT_CHOICE = [
        ('P', 'Pix'),
        ('S', 'Stripe'),
    ]
    
    COMPLETE_CHOICE = [
        (0, 'Cancelled'),
        (1, 'Pending'),
        (2, 'Complete'),    
    ]
    
    customer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    ordered_at = models.DateTimeField(auto_now_add=True)
    complete = models.PositiveIntegerField(choices=COMPLETE_CHOICE, default=1)
    transaction_id = models.AutoField(primary_key=True)
    shipping_address = models.CharField(max_length=492, blank=True)
    payment_method = models.CharField(choices=PAYMENT_CHOICE, max_length=32, blank=True)