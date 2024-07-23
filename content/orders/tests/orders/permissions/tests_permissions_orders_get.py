from ..base_orders_test import BaseOrdersTest

class OrderModelViewSetPermissionGetTest(BaseOrdersTest):    
    def test_get_order(self):

        response = self.get(is_authorizade=False)
        self.assertEqual(response.status_code, 403)
