from django.urls import reverse
from core.tests import UniversalBaseTests

class BaseProductsTest(UniversalBaseTests):
    def setUp(self):
        super().setUp()
        self.client = self.create_client(is_seller=True)
        self.product = self.create_product()
        self.api_url = reverse('products:products-list')
        self.api_url_detail = reverse('products:products-detail', kwargs={'pk': self.product.id})
           
        self.data = {      
          'name': 'Galaxy A10S',
          'description': 'SAMSUNG Galaxy A10S 32G 2RAM',
          'category': self.product.category.id,
          'price': 899.99,
          'brand': 'SAMSUNG',
          'stock': 9,
        }
        
        self.payload = self.data.copy()
