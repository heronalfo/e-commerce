from django.urls import reverse
from accounts.tests.base_accounts_test import BaseAccountsTest
from ..models import Category
import pdb

class BaseProductsTest(BaseAccountsTest):
    def setUp(self):    
        super().setUp()
        
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
        
    def patch(self, data=None):
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
                 
        return self.client.patch(api_url, data, format='json')
              
             