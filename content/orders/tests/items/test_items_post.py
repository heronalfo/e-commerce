from .base_orders_items_test import BaseOrdersItemsTest

class OrderItemModelViewSetPostTest(BaseOrdersItemsTest):
    def test_create_order_item(self):
        response = self.post(self.data)

        self.assertEqual(response.status_code, 201)
    
    def test_post_if_not_negative_quantities_are_allowed(self):
        self.data['quantity'] = -7
        response = self.post(self.data)

        self.assertEqual(response.status_code, 400)
    
    def test_post_if_it_is_not_allowed_to_insert_nonexistent_products(self):
        self.data['product'] = 9291011329102
        response = self.post(self.data)

        self.assertEqual(response.status_code, 400)