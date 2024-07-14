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

class Wishlist(models.Model):
    '''
    This class is responsible for adding products to the wishlist.
    '''
    class Meta:
        '''
        Wishlist instance metadata.
        '''
        ordering = ['-added_at']
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'

    costumer = models.ForeignKey('accounts.costumer', on_delete=models.CASCADE, related_name='costumer')
    product = models.ForeignKey('products.product', on_delete=models.CASCADE, related_name='product')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        String representation of the Product instance.
        '''

        return self.product.name
