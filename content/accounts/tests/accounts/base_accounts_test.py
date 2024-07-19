from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.utils.translation import activate
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import Costumer, Address

class BaseAccountsTest(TestCase):
    def create_address(
        self,
        street: str = 'Aristides Fransico dos Santos',
        cep: str = '0000-000',
        number: int = 27,
        city: str = 'Euclides da Cunha',
        uf: str = 'BA',
        neighborhood: str = 'Dengo',
        complement: str = 'Vizinho da rita do bolo e o omarinho do carro pipa'
    ):

        address = Address.objects.create(
            street=street,
            cep=cep,
            number=number,
            city=city,
            uf=uf,
            neighborhood=neighborhood,
            complement=complement,
            costumer=self.user
        )

        return address

    def setUp(self):    
        self.client = APIClient()
        
        self.user = Costumer.objects.create_user(username='client-test', password='Abc123_', is_seller=True)
        self.client.force_authenticate(self.user)
        
        self.refresh = RefreshToken.for_user(user=self.user)
        self.token = str(self.refresh.access_token)
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {self.token}')
                
        self.api_url = reverse('accounts:accounts-list')
        
        self.data = {      
          'username': 'client-test-other',
          'password': 'AbC1234_',          
        }
        
    @override_settings(LANGUAGE_CODE='pt')
    def _post(self, data=None):
        activate('pt')
        
        return self.client.post(self.api_url, data, format='json')
                                                                                
    def post(self, data=None):                           
        return self.client.post(self.api_url, data, format='json')
                
    def patch(self, data=None):
        payload = {      
          'username': 'client-test-edit',
          'password': 'AbC1234_',
        }
            
        create = self.post(payload)                       
        api_url = reverse('accounts:accounts-detail', kwargs={'pk': create.data['id']})       
                 
        return self.client.patch(api_url, data, format='json')