from django.urls import reverse
from rest_framework.test import APIClient
from products.tests.products.base_products_test import BaseProductsTest
from products.models import Product, Category
import pdb

class BaseReviewsTest(BaseProductsTest):
    def setUp(self):    
        super().setUp()
                
        self.api_url = reverse('products:reviews-list')
        self.product = self.create_product()
        
        self.data = {
           'product_id': self.product.id,
           'comment': 'Product arrived successfully, says it is what it is, perfect!',
           'rating': 5
        }
        
    def post(self, data=None, authenticate=True):
        if authenticate:
            return self.client.post(self.api_url, data, format='json')
        
        return self.unauthorized_client.post(self.api_url, data, format='json')
        
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
            
        return self.unauthorized_client.patch(api_url, data, format='json')

        