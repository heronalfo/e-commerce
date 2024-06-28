from django.urls import reverse
from accounts.tests.base_accounts_test import BaseAccountsTest
from products.models import Product, Category
import pdb

class BaseReviewsTest(BaseAccountsTest):
    def setUp(self):    
        super().setUp()
        
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
        
    def patch(self, data=None):
        payload = {      
           'product_id': self.product.id,
           'comment': 'Product arrived successfully, says it is what it is, perfect!',
           'rating': 5
        }
        
        create = self.post(payload)                      
        api_url = reverse('products:reviews-detail', kwargs={'pk': create.data['id']})       
                 
        return self.client.patch(api_url, data, format='json')