from django.urls import reverse
from core.tests import UniversalBaseTests

class BaseOrdersItemsTest(UniversalBaseTests):
    def setUp(self):
        super().setUp()
        self.client = self.create_client(is_seller=True)
        self.item = self.create_item()
        self.api_url = reverse('orders:items-list')
        self.api_url_detail = reverse('orders:items-detail', kwargs={'pk': self.item.id})

        self.data = {
            'order': self.create_order().id,
            'product': self.create_product().id,
            'quantity': 2,
        }
        self.payload = self.data.copy()
