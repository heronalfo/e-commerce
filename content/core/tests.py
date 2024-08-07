'''
tests.py

This module provides a base test class for Django applications,
offering utility methods for creating and cleaning up test data.

Classes:

    UniversalBaseTests: Universal base class for providing all types of HTTP methods for testing.

Author:
    PyPeu (heronalfo)
'''

from typing import Optional, Dict
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .creators import Creators

class UniversalBaseTests(TestCase, Creators):
    '''
    Base class for tests, providing methods for setting up,
    tearing down, and creating various test data.
    '''
    def setUp(self) -> None:
        '''
        Set up the test environment. Initialize variables and clients.
        '''
        self.unauthorized_client = APIClient()
        self.client: Optional[APIClient]
        self.data: Optional[Dict]
        self.payload: Optional[Dict]
        self.api_url: Optional[str]
        self.api_url_detail: Optional[str]

    def get(self, is_authorizade: bool = True):
        if is_authorizade:
            return self.client.get(self.api_url)

        return self.unauthorized_client.get(self.api_url)

    def post(self, data=None, is_authorizade: bool = True, format: str = 'json'):
        '''
        Helper method to perform a POST request.

        Args:
            data (dict): The data to post.
            is_authorizade (bool): Whether the request is authorized.
            format (str): The format of the request data.

        Returns:
            Response: The response from the POST request.
        '''
        if is_authorizade:     
            return self.client.post(self.api_url, data, format='json')
        
        return self.unauthorized_client.post(self.api_url, data, format=format)

    def patch(self, data=None, is_authorizade: bool = True, format: str = 'json'):
        '''
        Helper method to perform a PATCH request.

        Args:
            data (dict): The data to patch.
            is_authorizade (bool): Whether the request is authorized.
            format (str): The format of the request data.

        Returns:
            Response: The response from the PATCH request.
        '''
        response = self.post(self.payload)
        
        if is_authorizade:        
            return self.client.patch(self.api_url_detail, data, format='json')

        return self.unauthorized_client.patch(self.api_url_detail, data, format='json')