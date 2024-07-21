from django.urls import reverse
from core.tests import UniversalBaseTests

class BaseCategoriesTest(UniversalBaseTests):
    def setUp(self):
        super().setUp()
        self.client = self.create_client(is_seller=True)
        self.category = self.create_category()
        self.api_url = reverse('products:categories-list')
        self.api_url_detail = reverse('products:categories-detail', kwargs={'pk': self.category.id})
           
        self.data = {      
          'name': 'Cell phones',
          'description': 'Cell phones of all types'
        }

        self.payload = self.data.copy()
