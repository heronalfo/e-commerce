'''
apps.py

This module is responsible for defining our directory as an app.

for more informations: https://docs.djangoproject.com/en/5.0/ref/applications/

Author:
    Generate by Django.
'''

from django.apps import AppConfig

class AccountsConfig(AppConfig):
    '''
    Launches a new application
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    def ready(self):
        '''
        Cadastro dos sinais para a criação de um endereço após a criação de um usuário.
        '''
        import accounts.signals
