from .base_accounts_test import BaseAccountsTest
import pdb

class AccountsUserPatchTest(BaseAccountsTest):

    def test_patch_user(self):
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 200)
        
    def test_patch_if_it_is_not_allowed_to_excexer_the_limite_de_characters_of_username(self):
        self.data['username'] = 'client-test-edit'*4
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 400)
    
    def test_patch_if_not_allowed_usernames_fora_do_standard_slug(self):
        self.data['username'] = 'a 8w91nq 01010qba ajq'
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 400)
                      
    def test_patch_if_passwords_with_less_than_8_characters_are_not_allowed(self):
        self.data['password'] = 'aaa'
        response = self.patch(self.data)
        self.assertEqual(response.status_code, 400)
