from django.urls import reverse
from core.tests import UniversalBaseTests

class BaseWishlistTest(UniversalBaseTests):
    def setUp(self):
        super().setUp()
        self.client = self.create_client(is_seller=True)
        self.wishlist = self.create_wishlist()
        self.product = self.create_product()
        self.api_url = reverse('orders:wishlists-list')
        self.api_url_detail = reverse('orders:wishlists-detail', kwargs={'pk': self.wishlist.id})

        self.data = {
            'costumer': self.costumer.id,
            'product': self.product.id
        }
        self.payload = self.data.copy()
