from django.urls import reverse
from rest_framework.test import APIClient
from accounts.tests.base_accounts_test import BaseAccountsTest
from products.models import Product, Category

class BaseOrdersTest(BaseAccountsTest):
    def setUp(self):
        super().setUp()
        
        self.unauthorized_client = APIClient()
        self.data = {}
        self.api_url = reverse('products:orders-list')
        
        self.cell_phones = Category.objects.create(
            name='Cell phones',
            description='Brands of electronic devices such as cell phones'
        )
        
        samsung = Product.objects.create(
            seller=self.user,     
            name='Galaxy A10S',
            description='SAMSUNG Galaxy A10S 32G 2RAM',
            category=self.cell_phones,
            price=899.99,
            brand='SAMSUNG',
            stock=9,       
        )
        
        iphone = Product.objects.create(
            seller=self.user,     
            name='Iphone X',
            description='IphoneX 64GB 2RAM',
            category=self.cell_phones,
            price=1799.99,
            brand='APPLE',
            stock=5,        
        )
        
        self.products = [samsung, iphone] 
                     
    def post(self, data=None, authenticate=True):
        if authenticate:
            return self.client.post(self.api_url, self.data, format='json')
        
        return self.unauthorized_client.post(self.api_url, self.data, format='json')
    
    def patch(self, data=None, authenticate=True):
        payload = {}
        
        self.post(payload)
        if authenticate:
            return self.client.post(self.api_url, self.data, format='json')
        
        return self.unauthorized_client.post(self.api_url, self.data, format='json')
        