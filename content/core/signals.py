'''
signals.py

This module defines signals for the accounts app to automatically create
related models when certain events occur.

Functions:

    create_user_address: Signal handler to create an address for a new costumer.

Author:
    PyPeu (heronalfo)
'''

from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Costumer, Address

@receiver(post_save, sender=Costumer)
def create_user_address(sender, instance, created, **kwargs):
    '''
    Signal handler that creates an Address instance whenever a new Costumer instance is created.

    Args:
        sender (type): The model class that sent the signal.
        instance (Costumer): The instance of the model that was saved.
        created (bool): A boolean indicating whether a new record was created.
        **kwargs: Additional keyword arguments.
    '''
    if created:
        Address.objects.create(costumer=instance)