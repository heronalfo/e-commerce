from django.urls import reverse
from core.tests import UniversalBaseTests

class BaseAccountsTest(UniversalBaseTests):    
    def setUp(self):
        self.client = self.create_client()
        self.user = self.costumer
        self.api_url = reverse('accounts:accounts-list')

        self.api_url_detail = reverse('accounts:accounts-detail',
        kwargs={'pk': self.costumer.id})

        self.data = {
            'username': 'createuser', 
            'password': '12345678'
        }

        self.payload = self.data['username'] = 'otheruser'