'''
order_item.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    OrderItem: This class is responsible for modeling a new Product Instance in the database.

Author:
    PyPeu (heronalfo)
'''

from django.db import models

class OrderItem(models.Model):
    '''
    Product added to shopping cart, quantity and price 
    '''

    product = models.ForeignKey('products.product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    #pylint: disable=invalid-str-returned
    def __str__(self):
        '''
        Instance Formatting 
        '''

        return f"{self.product.name}"
