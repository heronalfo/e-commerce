from ..base_orders_items_test import BaseOrdersItemsTest

class OrderItemModelViewSetPermissionPatchTest(BaseOrdersItemsTest):
    def test_permission_patch_order_item(self):
        self.data['quantity'] = 5
        response = self.patch(self.data, is_authorizade=False)

        self.assertEqual(response.status_code, 403)
