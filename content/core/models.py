'''
models.py

This module is responsible for creating inheritance abstract for the extension of all tables,
ensuring that there is no code repetition

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/models/

Class:
    Extension: Abstract class for including 3 new columns.
    
    Colums:
        created_at: Records the exact moment of the created object.
        
        updated_at: Records the exact moment when the object was edited.
        
        uuid: Primary Key is universally unique, as common django ids are predictable, 
         causing a security problem.

Author:
    Pypeu (heronalfo)
'''

import uuid 
from django.db import models

class Extension(models.Model):
    '''
    This class is responsible for creating inheritance and adding 3 columns to.
    classes which inherit from it. 
    '''
    class Meta:
        '''
        Override to define that the class is abstract and the order to be displayed by date.
        '''
        abstract = True
        ordering = ['-created_at']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
