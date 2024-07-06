from django.urls import reverse
from rest_framework.test import APIClient
from products.tests.products.base_products_test import BaseProductsTest
from products.models import Product, Category, OrderItem
import pdb

class BaseOrdersTest(BaseProductsTest):

    def create_item(self, product=None, quantity: int = 12):     
        item = OrderItem.objects.create(
            product=self.create_product(),
            quantity=quantity
        )
        
        return item
        
    def setUp(self):
        super().setUp()
        
        self.data = {}
        self.api_url = reverse('products:orders-list')
                
        self.item = self.create_item()
                                     
        self.products = [self.item, ] 
                     
    def post(self, data=None, authenticate=True):
        if authenticate:
            return self.client.post(self.api_url, self.data, format='json')
        
        return self.unauthorized_client.post(self.api_url, self.data, format='json')
    
    def patch(self, data=None, authenticate=True):
          
        self.response = self.post({})        
        api_url = reverse('products:orders-detail', kwargs={'pk': int(self.response.data['id'])})
                        
        if authenticate:
            return self.client.patch(api_url, self.data, format='json')
        
        return self.unauthorized_client.patch(api_url, self.data, format='json')
        