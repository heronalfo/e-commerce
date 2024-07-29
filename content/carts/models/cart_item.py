'''
cart_item.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    CartItem: This class is responsible for creating items related to a cart.

Author:
    PyPeu (heronalfo)
'''
from django.db import models
from core.models import Extension

class CartItem(Extension):
    '''
    This class registers new items related to a cart, with the following data: product, quantity.
    '''
    class Meta:
        '''
        Cart Item instance metadata.
        '''
        verbose_name = 'cart_item'
        verbose_name_plural = 'cart_items'

    cart = models.OneToOneField('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('products.product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.product.name} by {self.product.price}'
