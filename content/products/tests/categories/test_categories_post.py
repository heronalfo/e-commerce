from .base_categories_test import BaseCategoriesTest

class CategoriesModelViewSetPostTest(BaseCategoriesTest):
    def test_categories_create(self):
        response = self.post(self.data)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertEqual(response.data['description'], self.data['description'])
           
    def test_if_it_is_allowed_to_insert_more_than_124_characters_in_name(self):
        self.data['name'] = self.data['name'] * 30
        response = self.post(self.data)        
        self.assertEqual(response.status_code, 400)
        
    def test_if_it_is_allowed_to_insert_more_than_x_characters_in_description(self):
        self.data['name'] = self.data['name'] * 30
        response = self.post(self.data)        
        self.assertEqual(response.status_code, 400)