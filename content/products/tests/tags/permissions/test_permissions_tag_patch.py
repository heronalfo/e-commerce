from ..base_tags_test import BaseTagsTest

class TagsModelViewSetTestPermissionPatch(BaseTagsTest):
    def test_tag_patch(self):
        self.data['name'] = 'Test Edit'
        response = self.patch(self.data, is_authorizade=False)

        self.assertEqual(response.status_code, 403)
