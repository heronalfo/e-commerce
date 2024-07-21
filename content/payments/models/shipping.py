'''
shipping.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    Shipping: This class is responsible for modeling a new Shipping Instance in the database.
    
Author:
    PyPeu (heronalfo)
'''

from django.db import models
from core.models import Extension
from accounts.models import Costumer
from orders.models import Order

class Shipping(Extension):
    '''
    Registration of shipping available for sale, order, costumer, address, and other details.
    '''

    class Meta:
        '''
        Shipping instance metadata.
        '''

        verbose_name = 'shipping'
        verbose_name_plural = 'shippings'

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=202)
    sent_at = models.DateTimeField(auto_now_add=True)
    tracking_number = models.CharField(max_length=102)
    shipping_method = models.CharField(max_length=102)

    def __str__(self):
        """
        String representation of the Shipping instance.
        """

        return self.address
