'''
coupon.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    Order: This class is responsible for modeling a new Coupon Instance in the database.
    
    Functions:
    
        Save:
            It prohibits the discount from being null and void if it is not of the free shipping type.
            If the coupon is not filled in, they will automatically generate one.

Author:
    PyPeu (heronalfo)
'''

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.db import models

from core.models import Extension
from accounts.models import Costumer

class Coupon(Extension):
    '''
    Registration of coupon available for coupon, discount, descriptipn and other details.
    '''
    TYPE_CHOICES = [
        ('FREE_SHIPING', 'Free shipping'),
        ('PERCENTAGEM', 'Percentagem'),
        ('FIXED_VALUE', 'Fixed Value'),
    ]

    code = models.CharField(
        max_length=22,
        unique=True,
        null=True,
        blank=True,
    )

    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=13, choices=TYPE_CHOICES)

    discount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(50),
        ]
    )
    
    quantity = models.PositiveIntegerField()
    used = models.ManyToManyField(Costumer, blank=True)
    expiration = models.DateTimeField()
    status = models.BooleanField(default=True)

    def __str__(self):
        '''
        String representation of the Order instance.
        '''
        return self.code

    def save(self, *args, **kwargs):
        '''
        Overrides the save method to validate data according to the database standard.
        '''
        if self.discount is None and self.type != 'FREE_SHIPING':
            raise ValidationError('The discount cannot be null if it is not just free shipping.')

        if not self.code:
            code = get_random_string(4)

            for _ in range(3):
                code += f'-{get_random_string(4)}' 

            self.code = code.upper()

        return super().save(*args, **kwargs)

    @property
    def is_valid(self):
        '''
        Returns whether the coupon is valid.
        '''
        return self.status and self.expiration > timezone.now()
