from ..base_reviews_test import BaseReviewsTest
import pdb

class ReviewModelViewSetPatchTest(BaseReviewsTest):
    def test_if_it_is_allowed_users_not_authenticated_patch_comments(self):
        response = self.patch(self.data, authenticate=False)        
        self.assertEqual(response.status_code, 403)