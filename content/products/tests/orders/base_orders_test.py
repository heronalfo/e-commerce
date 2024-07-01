from django.urls import reverse
from rest_framework.test import APIClient
from accounts.tests.base_accounts_test import BaseAccountsTest
from products.models import Product

class BaseOrdersTest(BaseAccountsTest):
    def setUp(self):
        super().setUp()
        
        self.unauthorized_client = APIClient()
        self.data = {}
        self.api_url = reverse('products:orders-list')
                        
    def post(self, data=None, authenticate=True):
        if authenticate:
            return self.client.post(self.api_url, self.data, format='json')
        
        return self.unauthorized_client.post(self.api_url, self.data, format='json')
    
    def patch(self, data=None, authenticate=True):
        payload = {}
        
        if authenticate:
            return self.client.post(self.api_url, self.data, format='json')
        
        return self.unauthorized_client.post(self.api_url, self.data, format='json')
        