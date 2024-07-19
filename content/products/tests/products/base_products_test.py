from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.tests.accounts.base_accounts_test import BaseAccountsTest
from accounts.models import Costumer
from products.models import Category, Product
import pdb

class BaseProductsTest(BaseAccountsTest):
    def create_category(
        self, 
        name: str = 'category',
        description: str = 'description'
    ):
    
        category = Category.objects.create(
            name=name,
            description=description,
        )
        
        return category
        
    def create_product(            
      
        self,
        seller: int = 1,
        name: str = 'Product Name',         
        description: str = 'Description', 
        category: int = 1, 
        price: float = 19.99, 
        brand: str = 'Brand', 
        stock: int = 99
    ):
    
        product = Product.objects.create(
            seller=self.user,
            name=name,
            description=description,        
            category=self.create_category(),
            price=price,
            brand=brand,
            stock=stock,
        )
        
        return product
    
    def setUp(self):    
        super().setUp()
        
        self.unauthorized_client = APIClient()                
        self.category = self.create_category()
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
        product = self.create_product()                      
        api_url = reverse('products:products-detail', kwargs={'pk': product.id})  
         
        if seller:                 
            return self.client.patch(api_url, data, format='json')
            
        else:
            return self.unauthorized_client.patch(api_url, data, format='json')
              
             