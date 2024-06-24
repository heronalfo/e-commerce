from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

class AuthTokenTests(APITestCase):
    def setUp(self):    
        self.username = 'client-test'
        self.password = 'client-test-password'
        
        self.user = User.objects.create_user(username=self.username, password=self.password)        
        self.client = APIClient()     
        self.data = {
        
            'username': self.username,
            'password': self.password
            
        }

    def test_obtain_token(self):    
        url = reverse('accounts:token')                
        response = self.client.post(url, self.data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertIn('access', response.data)        
        self.assertIn('refresh', response.data)
        
    def test_refresh_token(self):        
        token_url = reverse('accounts:token')        
        response = self.client.post(token_url, self.data, format='json')        
        refresh_token = response.data['refresh']

        refresh_url = reverse('accounts:refresh')        
        data = {     
            'refresh': refresh_token            
        }
        
        response = self.client.post(refresh_url, data, format='json')        
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertIn('access', response.data)

    def test_verify_token(self):      
        token_url = reverse('accounts:token')                
        response = self.client.post(token_url, self.data, format='json')        
        access_token = response.data['access']
        verify_url = reverse('accounts:verify')
        
        data = {        
            'token': access_token
        }
        
        response = self.client.post(verify_url, data, format='json')
        
        self.assertEqual(response.
        status_code, status.HTTP_200_OK)
                             
    def test_obtain_token_with_invalid_credentials(self):    
        url = reverse('accounts:token')        
        data = {        
            'username': self.username,            
            'password': 'wrongpassword'
            
        }
        
        response = self.client.post(url, data, format='json')        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)       
        self.assertNotIn('access', response.data)        
        self.assertNotIn('refresh', response.data)