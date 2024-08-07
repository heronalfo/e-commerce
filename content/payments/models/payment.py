'''
payment.py

This module is responsible for modeling and creating a Model Instance in the database,
through ORM Django.

for more informations: https://docs.djangoproject.com/en/5.0/topics/db/queries/

Classes:
    Shipping: This class is responsible for modeling a new Payment Instance in the database.
    
Author:
    PyPeu (heronalfo)
'''

from django.db import models
from core.models import Extension
from accounts.models import Costumer
from orders.models import Order

class Payment(Extension):
    '''
    This model is responsible for creating a new instance in the database, 
    storing data such as: customer, order, amount, payment_method.
    '''

    PAYMENT_CHOICE = [
        ('P', 'Pix'),
        ('T', 'Transferência bancária'),
        ('C', 'Cartão de crédito'),
    ]

    customer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='payment')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(choices=PAYMENT_CHOICE, max_length=32, blank=True)
    transaction_id = models.AutoField(primary_key=True)

    class Meta:
        '''
        Category instance metadata.
        '''

        verbose_name = 'payment'
        verbose_name_plural = 'payments'

    def __str__(self):
        """
        String representation of the Shipping instance.
        """

        return self.amount