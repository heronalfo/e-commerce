from ..base_categories_test import BaseCategoriesTest

class CategoriesModelViewSetGetPermissionTest(BaseCategoriesTest):
    def test_permissions_categories_get(self):
        response = self.get(is_authorizade=False)

        self.assertEqual(response.status_code, 200)