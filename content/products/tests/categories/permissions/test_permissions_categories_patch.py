from ..base_categories_test import BaseCategoriesTest

class PermissionsCategoriesModelViewSetPatchTest(BaseCategoriesTest):
    def test_permissions_patch_category_user_not_seller(self):
        response = self.patch(self.data, seller=False)
        self.assertEqual(response.status_code, 403)
        