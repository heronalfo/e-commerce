from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.tests.base_accounts_test import BaseAccountsTest
from accounts.models import Costumer
from products.models import Category
import pdb

class BaseProductsTest(BaseAccountsTest):
    def setUp(self):    
        super().setUp()
        
        self.client_not_seller = APIClient()
        self.user_not_seller = Costumer.objects.create_user(username='test-permissions', password='_ABC123456')
        self.client_not_seller.force_authenticate(self.user_not_seller)
        
        self.refresh = RefreshToken.for_user(user=self.user_not_seller)
        self.token = str(self.refresh.access_token)
        self.client_not_seller.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')        
               
        self.category = Category.objects.create(name='SmartPhone', description='cell phone model')  
        self.api_url = reverse('products:products-list')
           
        self.data = {      
          'name': 'Galaxy A10S',
          'description': 'SAMSUNG Galaxy A10S 32G 2RAM',
          'category': self.category.id,
          'price': 899.99,
          'brand': 'SAMSUNG',
          'stock': 9,
        }
        
    def patch(self, data=None, seller=True):
        payload = {      
          'name': 'Galaxy A10S',
          'description': 'SAMSUNG Galaxy A10S 32G 2RAM',
          'category': self.category.id,
          'price': 899.99,
          'brand': 'SAMSUNG',
          'stock': 9,
        }
        create = self.post(payload)                      
        api_url = reverse('products:products-detail', kwargs={'pk': create.data['id']})       
         
        if seller:                 
            return self.client.patch(api_url, data, format='json')
            
        else:
            return self.client_not_seller.patch(api_url, data, format='json')
              
             