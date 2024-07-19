'''
costumer.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    
        for more informations: https://docs.djangoproject.com/en/5.0/topics/db/managers/
    
    Costumer: This abstract class is responsible for modeling
    a new Costumer Instance in the database.

Author:
    PyPeu (heronalfo)
'''

from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import Extension

#pylint: disable=line-too-long
class Costumer(AbstractUser):
    '''
    Registration of Costumer available for sale, name, category, price, and other details.
    '''
    class Meta:
        '''
        Costumer instance metadata.
        '''
        verbose_name = 'costumer'
        verbose_name_plural = 'costumers'

    name = models.CharField(max_length=32, null=True)
    about = models.CharField(max_length=324, null=True)
    cpf = models.CharField(max_length=15, unique=True, db_index=True, null=True)
    number = models.CharField(max_length=24, db_index=True, unique=True, null=True)
    is_seller = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
