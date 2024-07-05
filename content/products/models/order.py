from django.db import models
from django.conf import settings
from accounts.models import Costumer

class Order(models.Model):
    customer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='orders')
    ordered_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    # = models.CharField(max_length=100, null=True, blank=True)
    shipping_address = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id}"