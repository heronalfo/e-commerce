from ..base_wishlist_test import BaseWishlistTest

class WishlistViewSetPermissionPostTest(BaseWishlistTest):
    def test_permission_create_wishlist(self):
        response = self.post(self.data, is_authorizade=False)

        self.assertEqual(response.status_code, 403)