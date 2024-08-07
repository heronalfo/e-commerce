from .base_wishlist_test import BaseWishlistTest

class WishlistViewSetGetTest(BaseWishlistTest):
    def test_get_wishlist(self):
        response = self.get(self.data)

        self.assertEqual(response.status_code, 200)