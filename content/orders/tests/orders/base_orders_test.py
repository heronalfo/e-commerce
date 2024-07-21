from django.urls import reverse
from core.tests import UniversalBaseTests

class BaseOrdersTest(UniversalBaseTests):
    def setUp(self):
        super().setUp()
        self.client = self.create_client(is_seller=True)
        self.item = self.create_item()
        self.order = self.create_order()
        self.api_url = reverse('orders:orders-list')
        self.api_url_detail = reverse('orders:orders-detail', kwargs={'pk': self.order.id})          
        self.data = {}
        self.payload = self.data.copy()
