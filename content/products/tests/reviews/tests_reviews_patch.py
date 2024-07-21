from .base_reviews_test import BaseReviewsTest
import pdb

class ReviewModelViewSetPatch(BaseReviewsTest):
    def test_patch_comment(self):
        self.data['comment'] = 'Good quality product and low price.'
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 200)
        
    def test_patch_if_it_is_allowed_to_insert_more_than_150_characters(self):
        self.data['comment'] = self.data['comment'] * 50
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 400)
        
    def test_if_it_is_allowed_to_patch_comment_on_a_product_that_does_not_exist(self):
        self.data['product'] = 12018*24      
        response = self.patch(self.data)
                
        self.assertEqual(response.status_code, 400)
    
    def test_patch_if_it_is_allowed_to_patch_more_than_150_characters(self):
        self.data['comment'] = self.data['comment'] * 50
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 400)
        
    def test_if_it_is_patch_allowed_rating_com_more_than_5_points(self):
        self.data['rating'] = 6
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 400)
        
    def test_if_it_is_patch_allowed_rating_com_minus_than_5_points(self):
        self.data['rating'] = 0
        response = self.patch(self.data)
        
        self.assertEqual(response.status_code, 400)