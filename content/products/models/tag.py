'''
tag.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    
    Tag: This class is responsible for modeling a new Tag Instance in the database.

Author:
    PyPeu (heronalfo)
'''

from django.db import models
from core.models import Extension

class Tag(Extension):
    '''
    This class is responsible for creating new tags to improve product searches.
    '''
    class Meta:
        '''
        Tag instance metadata.
        '''
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    name = models.CharField(max_length=21, unique=True, db_index=True)

    def __str__(self):
        """
        String representation of the Product instance.
        """
        return self.name
