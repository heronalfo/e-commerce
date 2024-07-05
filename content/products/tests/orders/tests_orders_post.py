from .base_orders_test import BaseOrdersTest
import pdb

class OrderModelViewSetPostTest(BaseOrdersTest):
    def test_create_order(self):
        response = self.post(self.data)
        self.assertEqual(response.status_code, 201)       