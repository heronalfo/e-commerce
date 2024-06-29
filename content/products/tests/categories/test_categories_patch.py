from .base_categories_test import BaseCategoriesTest
import pdb

class CategoriesModelViewSetPatchTest(BaseCategoriesTest):
    def test_categories_patch(self):
        self.data['name'] = 'Cars'
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertEqual(response.data['description'], self.data['description'])
           
    def test_if_it_is_allowed_to_patch_more_than_124_characters_in_name(self):
        self.data['name'] = self.data['name'] * 30
        response = self.patch(self.data)        
        self.assertEqual(response.status_code, 400)
        
    def test_if_it_is_allowed_to_patch_more_than_x_characters_in_description(self):
        self.data['name'] = self.data['name'] * 30
        response = self.patch(self.data)        
        self.assertEqual(response.status_code, 400)