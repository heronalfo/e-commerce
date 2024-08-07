'''
wishlist.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    Wishlist: This class is responsible for modeling a new Wishlist Instance in the database.

Author:
    PyPeu (heronalfo)
'''

from django.db import models
from core.models import Extension
from accounts.models import Costumer
from products.models import Product

class Wishlist(Extension):
    '''
    This class is responsible for adding products to the wishlist.
    '''
    class Meta:
        '''
        Wishlist instance metadata.
        '''
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'

    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist')

    def __str__(self):
        '''
        String representation of the Product instance.
        '''

        return self.product.name
