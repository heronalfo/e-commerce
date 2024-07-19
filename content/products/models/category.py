'''
category.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    This class is responsible for rendering in a relational way, 
    avoiding multiple unnecessary queries.

Author:
    PyPeu (heronalfo)
'''

from django.db import models
from core.models import Extension

class Category(Extension):
    '''
    Registration of categories available for name, description, other details.
    '''

    name = models.CharField(max_length=32)
    description = models.CharField(max_length=124)

    class Meta:
        '''
        Category instance metadata.
        '''

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """
        String representation of the Category instance.
        """

        return self.name
