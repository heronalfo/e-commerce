from ..base_products_test import BaseProductsTest
import pdb

class ProductModelViewSetPostTest(BaseProductsTest):
    def test_if_it_is_allowed_users_non_seller(self):
        response = self.client_not_seller.post(self.api_url, self.data, format='json')
        self.assertEqual(response.status_code, 403)
        self.assertIn('not have permission', response.data['detail'])
        