from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Costumer, Address

@receiver(post_save, sender=Costumer)
def create_user_address(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(costumer=instance)