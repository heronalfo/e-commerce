from django.urls import reverse
from core.tests import UniversalBaseTests

class BaseTagsTest(UniversalBaseTests):
    def setUp(self):
        super().setUp()
        self.client = self.create_client(is_seller=True)
        self.tag = self.create_tag()
        self.api_url = reverse('products:tags-list')
        self.api_url_detail = reverse('products:tags-detail', kwargs={'pk': self.tag.id})

        self.data = {      
          'name': 'Cell phones',
        }

        self.payload = self.data['name'] = 'Phones cell'
