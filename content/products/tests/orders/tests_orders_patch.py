from .base_orders_test import BaseOrdersTest
import pdb

class OrderModelViewSetPatchTest(BaseOrdersTest):    
    def test_patch_order(self):
        self.data = {'add_product': self.products[0].id}
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 201)
                
    def test_remove_product_order(self):
        self.data = {'add_product': self.products[0].id}
        self.data = {'remove_products': [self.products[0].id,]}
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 201)
        
    def test_if_it_is_allowed_to_add_a_nonexistent_product(self):
        self.data = {'add_product': 999}
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 400)