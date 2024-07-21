from ..base_orders_test import BaseOrdersTest
import pdb

class OrdersModelViewSetPostTest(BaseOrdersTest):
    def test_if_it_is_allowed_users_non_seller(self):
        response = self.post(self.data, is_authorizade=False)
        self.assertEqual(response.status_code, 403)