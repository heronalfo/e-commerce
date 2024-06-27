from .base_accounts_test import BaseAccountsTest
import pdb

class AccountsUserPostTest(BaseAccountsTest):
    def test_create_user(self):
        response = self.post(self.data)
        self.assertEqual(response.status_code, 201)
        
    def test_if_it_is_not_allowed_to_excexer_the_limite_de_characters_of_username(self):
        self.data['username'] = 'aaa'*30
        response = self.post(self.data)
        self.assertEqual(response.status_code, 400)
    
    def test_if_not_allowed_usernames_fora_do_standard_slug(self):
        self.data['username'] = 'a 8w91nq 01010qba ajq'
        response = self.post(self.data)
        self.assertEqual(response.status_code, 400)
                
    def test_if_users_with_same_name_are_not_permitted(self):
        self.data['username'] = 'client-test'
        response = self.post(self.data)
        self.assertEqual(response.status_code, 400)
                
    def test_create_data_with_missing_password(self):
        data = {'username': 'client-test-other'}        
        response = self.post(data)
        self.assertEqual(response.status_code, 400)
        
    def test_if_passwords_with_less_than_8_characters_are_not_allowed(self):
        self.data['password'] = 'aaa'
        response = self.post(self.data)
        self.assertEqual(response.status_code, 400)
        
    def test_if_not_is_allowed_cep_invalid(self):
        self.data['cep'] = '1 01 zjskakq e / Y -01'
        response = self.post(self.data)
        self.assertEqual(response.status_code, 400)
        
    def test_if_not_is_allowed_cpf_invalid(self):
        self.data['cpf'] = '123 / £ .456.78 k a 9-01'
        response = self.post(self.data)
        self.assertEqual(response.status_code, 400)
        
    def test_if_not_is_allowed_number_invalid(self):
        self.data['cpf'] = '+ 1929sjqb 1kmsna010e 1mn qj '
        response = self.post(self.data)
        self.assertEqual(response.status_code, 400)        