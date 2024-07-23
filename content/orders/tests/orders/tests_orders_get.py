from .base_orders_test import BaseOrdersTest

class OrderModelViewSetGetTest(BaseOrdersTest):    
    def test_get_order(self):

        response = self.get()
        self.assertEqual(response.status_code, 200)