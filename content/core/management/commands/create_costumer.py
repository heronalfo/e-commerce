from django.core.management.base import (BaseCommand, CommandError)
from accounts.models import Costumer

class Command(BaseCommand):
    def handle(self, *args, **options):
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