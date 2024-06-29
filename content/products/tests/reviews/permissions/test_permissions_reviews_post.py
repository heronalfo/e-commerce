from ..base_reviews_test import BaseReviewsTest
import pdb

class ReviewModelViewSetPostTest(BaseReviewsTest):
    def test_if_it_is_allowed_users_not_authenticated_make_comments(self):
        response = self.post(self.data, authenticate=False)        
        self.assertEqual(response.status_code, 403)