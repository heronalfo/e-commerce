'''
apps.py

This module is responsible for defining our directory as an app.

for more informations: https://docs.djangoproject.com/en/5.0/ref/applications/

Author:
    Generate by Django.
'''

from django.apps import AppConfig

#pylint: disable=too-many-ancestors
class OrdersConfig(AppConfig):
    '''
    Initialize the Order project.
    '''

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
