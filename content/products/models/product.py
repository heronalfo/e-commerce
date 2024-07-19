'''
product.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    ProductManager: This class is responsible for rendering in a relational way, 
    avoiding multiple unnecessary queries. 
       
        for more informations: https://docs.djangoproject.com/en/5.0/topics/db/managers/
    
    Product: This class is responsible for modeling a new Product Instance in the database.

Author:
    PyPeu (heronalfo)
'''

from django.db import models
from core.models import Extension
from accounts.models import Costumer

class ProductManager(models.Manager):
    '''
    This class is responsible for ensuring that there are no duplicate queries.
    '''

    def get_queryset(self):
        '''
        Override the default queryset to prefetch related fields.
        '''
        return super().get_queryset().prefetch_related('category', 'tag')

    def with_related(self):
        '''
        Customized method to return the query with related fields.
        '''

        return self.get_queryset()

class Product(Extension):
    '''
    Registration of products available for sale, name, category, price, and other details.
    '''

    class Meta:
        '''
        Product instance metadata.
        '''
        ordering = ['-created_at']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    seller = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=64, db_index=True)
    description = models.TextField(max_length=5000)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name='products')
    tags = models.ManyToManyField('Tag', related_name='tags')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    brand = models.CharField(max_length=64, blank=True, null=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        '''
        String representation of the Product instance.
        '''
        return self.name

    def is_in_stock(self):
        '''
        Check if the product is in stock.
        '''
        return self.stock > 0

    def apply_discount(self, discount_percentage):
        '''
        Apply a discount to the product price.
        '''
        self.price = self.price * (1 - discount_percentage / 100)
        self.save()
