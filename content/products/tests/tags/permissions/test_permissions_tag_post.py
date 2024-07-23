from ..base_tags_test import BaseTagsTest

class TagsModelViewSetTestPermissionPost(BaseTagsTest):
    def test_tag_create_permission(self):
        response = self.post(self.data, is_authorizade=False)

        self.assertEqual(response.status_code, 403)
