from accounts.models import Costumer
from django.db import models
from orders.models import Order

class Shipping(models.Model):
    '''
    Important information about product shipping and delivery 
    '''
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=202)
    tracking_number = models.CharField(max_length=102)
    shipping_method = models.CharField(max_length=102)
    
    class Meta:    
        verbose_name = 'shipping'
        verbose_name_plural = 'shippings'
    
    def __str__(self):
        return self.address