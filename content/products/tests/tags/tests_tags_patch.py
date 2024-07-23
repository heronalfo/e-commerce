from .base_tags_test import BaseTagsTest

class TagsModelViewSetTestPatch(BaseTagsTest):
    def test_tag_patch(self):
        self.data['name'] = 'Test Edit'
        response = self.patch(self.data)

        self.assertEqual(response.status_code, 200)

    def test_patch_tag_if_it_is_allowed_to_break_the_character_limit(self):
        self.data['name'] = self.data['name'] * 30
        response = self.patch(self.data)

        self.assertEqual(response.status_code, 400)
    
    def test_patch_if_it_is_allowed_2_tags_with_the_same_name(self):
        tag = self.create_tag(name='tag')
        self.data['name'] = 'tag'
        
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 400)