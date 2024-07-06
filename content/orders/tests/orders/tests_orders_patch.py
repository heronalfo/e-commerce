from .base_orders_test import BaseOrdersTest
import pdb

class OrderModelViewSetPatchTest(BaseOrdersTest):    
    def test_patch_order(self):
        self.data = {'item': self.item.id}
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 200)
                
    def test_remove_product_order(self):
        self.data = {'item': self.item.id}
        self.data = {'items_removed': [self.item.id,]}
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 200)
        