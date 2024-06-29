from ..base_categories_test import BaseCategoriesTest

class PermissionsCategoriesModelViewSetPostTest(BaseCategoriesTest):
    def test_permissions_create_user_not_seller(self):
        response = self.post(self.data, seller=False)
        self.assertEqual(response.status_code, 403)
        