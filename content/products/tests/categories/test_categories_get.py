from .base_categories_test import BaseCategoriesTest

class CategoriesModelViewSetGetTest(BaseCategoriesTest):
    def test_categories_get(self):
        response = self.get()

        self.assertEqual(response.status_code, 200)