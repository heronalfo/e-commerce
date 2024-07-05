from ..base_orders_test import BaseOrdersTest
import pdb

class OrdersModelViewSetPatchTest(BaseOrdersTest):
    def test_if_it_is_allowed_users_non_authenticate(self):
        response = self.patch(self.data, authenticate=False)
        self.assertEqual(response.status_code, 403)
        