from ..base_products_test import BaseProductsTest

class ProductModelViewSetPermissionGetTest(BaseProductsTest):
    def test_product_get(self):
        response = self.get(is_authorizade=False)

        self.assertEqual(response.status_code, 200)