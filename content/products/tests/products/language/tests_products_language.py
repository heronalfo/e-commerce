from django.test import override_settings
from django.utils.translation import activate
from ..base_products_test import BaseProductsTest
import pdb

class MultiLanguageProductsTest(BaseProductsTest):

    @override_settings(LANGUAGE_CODE='pt')
    def test_language_when_creating_a_product_with_more_than_64_characters(self):
        activate('pt')
        
        self.data['name'] = self.data['name'] * 30
        response = self.post(self.data)
        
        self.assertIn('Certifique-se de que este campo não tenha mais de 64 caracteres.', response.data['name'])
        
    @override_settings(LANGUAGE_CODE='pt')
    def test_language_message_response_when_creating_a_product_with_price_0(self):
        activate('pt')
        
        self.data['price'] = -1
        response = self.post(self.data)
        
        self.assertIn('O preço deve ser maior que 0', response.data['price'])
    
    @override_settings(LANGUAGE_CODE='pt')   
    def test_language_if_is_allowed_stock_less_than_0(self):
        activate('pt')
        self.data['stock'] = -1
        response = self.post(self.data)
               
        self.assertIn('Certifque-se de que este valor seja maior ou igual a 0.', response.data['stock'])        