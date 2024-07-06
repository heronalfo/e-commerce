from .base_products_test import BaseProductsTest
import pdb

class ProductModelViewSePpatchTest(BaseProductsTest):
    def test_patch_product(self):
        self.data['name'] = 'SAMSUNG GALAXY A10S'
        response = self.patch(self.data)        
        self.assertEqual(response.status_code, 200)
                
    def test_patch_if_is_allowed_name_greater_than_64_characters(self):
        self.data['name'] = self.data['name'] * 30
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('64', response.data['name'][0])
        
    def test_patch_if_is_allowed_price_less_than_0(self):
        self.data['price'] = -1
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('0', response.data['price'][0])
        
    def test_patch_if_is_allowed_stock_less_than_0(self):
        self.data['stock'] = -1
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 400)
        # self.assertIn('0', response.data['stock'])