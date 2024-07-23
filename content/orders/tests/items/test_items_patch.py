from .base_orders_items_test import BaseOrdersItemsTest

class OrderItemModelViewSetPatchTest(BaseOrdersItemsTest):
    def test_patch_order_item(self):
        self.data['quantity'] = 5
        response = self.patch(self.data)

        self.assertEqual(response.status_code, 200)
    
    def test_patch_if_not_negative_quantities_are_allowed(self):
        self.data['quantity'] = -7
        response = self.patch(self.data)

        self.assertEqual(response.status_code, 400)
    
    def test_patch_if_it_is_not_allowed_to_insert_nonexistent_products(self):
        self.data['product'] = 292919182829
        response = self.patch(self.data)

        self.assertEqual(response.status_code, 400)