from ..base_orders_items_test import BaseOrdersItemsTest

class OrderItemModelViewSetPermissionPostTest(BaseOrdersItemsTest):
    def test_permission_create_order_item(self):
        response = self.post(self.data, is_authorizade=False)

        self.assertEqual(response.status_code, 403)