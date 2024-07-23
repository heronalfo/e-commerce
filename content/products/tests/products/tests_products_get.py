from .base_products_test import BaseProductsTest

class ProductModelViewSetGetTest(BaseProductsTest):
    def test_product_get(self):
        response = self.get(self.data)
        
        self.assertEqual(response.status_code, 200)