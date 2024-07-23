from ..base_wishlist_test import BaseWishlistTest

class WishlistViewSetPermissionPatchTest(BaseWishlistTest):
    def test_permission_patch_wishlist(self):
        response = self.patch(self.data, is_authorizade=False)

        self.assertEqual(response.status_code, 403)