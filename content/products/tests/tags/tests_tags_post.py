from .base_tags_test import BaseTagsTest

class TagsModelViewSetTestPost(BaseTagsTest):
    def test_tag_create(self):
        response = self.post(self.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], self.data['name'])

    def test_tag_if_it_is_allowed_to_break_the_character_limit(self):
        self.data['name'] = self.data['name'] * 30
        response = self.post(self.data)

        self.assertEqual(response.status_code, 400)
    
    def test_if_it_is_allowed_2_tags_with_the_same_name(self):
        tag = self.create_tag(name='tag')
        self.data['name'] = 'tag'
        
        response = self.post(self.data)
        self.assertEqual(response.status_code, 400)