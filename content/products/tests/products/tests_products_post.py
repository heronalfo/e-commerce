from .base_products_test import BaseProductsTest
import pdb

class ProductModelViewSetPostTest(BaseProductsTest):
    def test_create_product(self):
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertEqual(response.data['description'], self.data['description'])
        self.assertEqual(response.data['category'], self.data['category'])
        
    def test_if_is_allowed_name_greater_than_64_characters(self):
        self.data['name'] = self.data['name'] * 30
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('64', response.data['name'][0])
        
    def test_if_is_allowed_price_less_than_0(self):
        self.data['price'] = -1
        response = self.post(self.data)   
        self.assertEqual(response.status_code, 400)
        self.assertIn('0', response.data['price'][0])
        
    def test_if_is_allowed_stock_less_than_0(self):
        self.data['stock'] = -1
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 400)
        # self.assertIn('0', response.data['stock']['message'])