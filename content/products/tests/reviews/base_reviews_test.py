from django.urls import reverse
from rest_framework.test import APIClient
from accounts.tests.base_accounts_test import BaseAccountsTest
from products.models import Product, Category
import pdb

class BaseReviewsTest(BaseAccountsTest):
    def setUp(self):    
        super().setUp()
        self.client_not_authenticate = APIClient()
                
        self.category = Category.objects.create(name='SmartPhone', description='cell phone model')  
        self.api_url = reverse('products:reviews-list')
        self.product = Product.objects.create(
            seller=self.user,
            name='Galaxy A10S',
            description='SAMSUNG Galaxy A10S 32G 2RAM',
            category=self.category,
            price=899.99,
            brand='SAMSUNG',
            stock=9,          
        )
        
        self.data = {
           'product_id': self.product.id,
           'comment': 'Product arrived successfully, says it is what it is, perfect!',
           'rating': 5
        }
        
    def post(self, data=None, authenticate=True):
        if authenticate:
            return self.client.post(self.api_url, data, format='json')
        
        return self.client_not_authenticate.post(self.api_url, data, format='json')


        
    def patch(self, data=None, authenticate=True):
        payload = {      
           'product_id': self.product.id,
           'comment': 'Product arrived successfully, says it is what it is, perfect!',
           'rating': 5
        }
        
        create = self.post(payload)                      
        api_url = reverse('products:reviews-detail', kwargs={'pk': create.data['id']})       
        
        if authenticate:       
            return self.client.patch(api_url, data, format='json')
            
        return self.client_not_authenticate.patch(api_url, data, format='json')

        