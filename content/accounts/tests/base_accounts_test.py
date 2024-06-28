from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import Costumer

class BaseAccountsTest(TestCase):
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
        
    def post(self, data):   
        return self.client.post(self.api_url, data, format='json')
        
    def patch(self, data=None):
        payload = {      
          'username': 'client-test-edit',
          'password': 'AbC1234_',
        }
            
        create = self.post(payload)                       
        api_url = reverse('accounts:accounts-detail', kwargs={'pk': create.data['id']})       
                 
        return self.client.patch(api_url, data, format='json')