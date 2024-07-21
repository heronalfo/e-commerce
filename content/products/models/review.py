'''
review.py

This module is responsible for creating a new instance in the Review model in the database
Through the django ORM.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    ReviewManeger: This class is responsible for rendering in a relational way, 
    avoiding multiple unnecessary queries.
    
    for more informations: https://docs.djangoproject.com/en/5.0/topics/db/managers/
    
    Review: This class is responsible for modeling an instance in the database.
    
Author:
    PyPeu (heronalfo)
'''

from django.db import models
from core.models import Extension
from accounts.models import Costumer
from .product import Product

class ReviewManager(models.Manager):
    '''
    This class is responsible for ensuring that there are no duplicate queries.
    '''

    def get_queryset(self):
        '''
        Override the default queryset to prefetch related fields.
        '''

        return super().get_queryset().prefetch_related('accounts.costumer')

    def with_related(self):
        '''
        Customized method to return the query with related fields.
        '''

        return self.get_queryset()

class Review(Extension):
    '''
    This model is responsible for creating a new instance in the database, 
    storing data such as: customer, rating, comment.
    '''

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=150, blank=True, db_index=True)

    class Meta:
        '''
        Review instance metadata.
        '''
        ordering = ['-created_at']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        """
        String representation of the Product instance.
        """

        return self.comment
