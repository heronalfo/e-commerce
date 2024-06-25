from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class Costumer(AbstractUser):
    name = models.CharField(max_length=32, null=True)
    about = models.CharField(max_length=324, null=True)
    cpf = models.CharField(max_length=15, null=True)
    cep = models.CharField(max_length=24, null=True)
    number = models.CharField(max_length=24, null=True)
    address = models.CharField(max_length=292, null=True)
    cnpj = models.CharField(max_length=34, null=True)    
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