'''
address.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    
        for more informations: https://docs.djangoproject.com/en/5.0/topics/db/managers/
    
    Costumer: This class is responsible for modeling
    a new Address Instance in the database.

Author:
    PyPeu (heronalfo)
'''

from django.contrib.auth.models import AbstractUser
from django.db import models

class Address(models.Model):
    '''
    Registering addresses from a user, road, cep, number and more.
    '''
    class Meta:
        '''
        Address instance metadata.
        '''
        verbose_name = 'address'
        verbose_name_plural = 'adresses'

    costumer = models.OneToOneField('Costumer', on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=37, db_index=True, null=True)
    cep = models.CharField(max_length=8, null=True)
    number = models.IntegerField(null=True)
    complement = models.CharField(max_length=324, null=True)
    neighborhood = models.CharField(max_length=50, null=True)
    uf = models.CharField(max_length=2, null=True)
    city = models.CharField(max_length=35, null=True, db_index=True)

    def __str__(self):
        '''
        String representation of the Product instance.
        '''

        return f'{self.city} {self.neighborhood} {self.road} {self.number}'
