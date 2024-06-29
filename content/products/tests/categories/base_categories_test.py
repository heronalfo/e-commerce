from django.urls import reverse
from rest_framework.test import APIClient
from accounts.tests.base_accounts_test import BaseAccountsTest
from products.models import Costumer
import pdb

class BaseCategoriesTest(BaseAccountsTest):
    def setUp(self):
        super().setUp()
        
        self.client_not_seller = APIClient()
        self.user_not_seller = Costumer.objects.create_user(username='test-permissions', password='_ABC123456')
        
        self.data = {
            'name': 'Clothes',
            'description': 'Clothes of all types, linen, silk, underwear, etc.',
        }      
        self.api_url = reverse('products:categories-list')
        
    def post(self, data=None, seller=True):
        if seller:
            return self.client.post(self.api_url, data, format='json')
                    
        return self.client_not_seller.post(self.api_url, data, format='json')
        
    def patch(self, data=None, seller=True):
        payload = {
            'name': 'Shoes',
            'description': 'Footwear of all types, shoes, sneakers, etc.',
        }
                             
        create = self.post(payload)
        api_url = reverse('products:categories-detail', kwargs={'pk': create.data['id']}) 
        
        if seller:
            return self.client.patch(api_url, data, format='json')         
        
        return self.client_not_seller.patch(api_url, data, format='json')
           
        