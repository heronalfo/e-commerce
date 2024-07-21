from ..base_products_test import BaseProductsTest

class ProductModelViewSetPostTestPermission(BaseProductsTest):
    def test_if_it_is_allowed_users_non_seller(self):
        response = self.post(self.data, is_authorizade=False)
        self.assertEqual(response.status_code, 403)
        self.assertIn('credentials were not provided', response.data['detail'])
