'''
cart.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    Cart: This class is responsible for creating a Cart for grouping items.

Author:
    PyPeu (heronalfo)
'''

from django.db import models
from core.models import Extension

class Cart(Extension):
    '''
    Registration of carts with the following data: costumer, category, name.
    '''
    class Meta:
        '''
        Cart Instance Metadata.
        '''
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    costumer = models.ForeignKey('accounts.costumer', on_delete=models.CASCADE)
    category = models.ForeignKey('products.category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=52, null=True, blank=True, db_index=True)

    def __str__(self):
        '''
        String representation of the Product instance.
        '''

        return self.name
