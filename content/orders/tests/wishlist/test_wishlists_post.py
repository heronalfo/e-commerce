from .base_wishlist_test import BaseWishlistTest

class WishlistViewSetPostTest(BaseWishlistTest):
    def test_create_wishlist(self):
        response = self.post(self.data)

        self.assertEqual(response.status_code, 201)
    
    def test_post_if_it_is_not_allowed_to_insert_nonexistent_products(self):
        self.data['product'] = 9291011329102
        response = self.post(self.data)

        self.assertEqual(response.status_code, 400)