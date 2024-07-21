'''
create_costumer.py

This module is responsible for creating a new command for adding a new costumer.
for more informations: https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/

Class:
    Command: BaseCommand instance for command identification by Django.

Author:
    Pypeu (heronalfo)
    
'''
from django.core.management.base import (BaseCommand, CommandError)
from accounts.models import Costumer

class Command(BaseCommand):
    '''
    This class is responsible for creating a new costumer.
    '''
    def handle(self, *args, **options):
        '''
        Command header and body, passing all parameters.
        '''
        try:
            self.stdout.write('As an administrator, you have the responsibility to use VALID DATA. \n')

            name = str(input('name: '))
            about = str(input('about: '))
            cpf = str(input('cpf: '))
            number = str(input('number: '))
            is_seller = str(input('Is seller [y/n]: ')).lower()

            costumer = Costumer.objects.create(
                name=name,
                about=about,
                cpf=cpf,
                number=number,
                is_seller=True if is_seller == 'y' else False
            )

            self.stdout.write(f'Costumer created successfully {costumer.uuid}')
              
        except Exception as e:
            raise CommandError(e)
