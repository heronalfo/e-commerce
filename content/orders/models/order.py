'''
order.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    Order: This class is responsible for modeling a new Order Instance in the database.

Author:
    PyPeu (heronalfo)
'''

from django.db import models
from accounts.models import Costumer

class Order(models.Model):
    '''
    Registration of orders available for order, name, category, price, and other details.
    '''

    class Meta:
        '''
        Order instance metadata.
        '''
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    products = models.ManyToManyField('OrderItem', related_name='orders')
    ordered_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, db_index=True)
    shipping_address = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        '''
        String representation of the Order instance.
        '''

        return f"Order {self.complete}"

    @property
    def is_complete(self):
        '''
        Returns whether the order is complete or not.
        '''

        return self.complete is True
