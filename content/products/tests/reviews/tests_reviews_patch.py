from .base_reviews_test import BaseReviewsTest
import pdb

class ReviewModelViewSetPostPatch(BaseReviewsTest):
    def test_patch_comment(self):
        self.data['comment'] = 'Good quality product and low price.'
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 200)
        
    def test_post_if_it_is_allowed_to_insert_more_than_150_characters(self):
        self.data['comment'] = self.data['comment'] * 50
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 400)