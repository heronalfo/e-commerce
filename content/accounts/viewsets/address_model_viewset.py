"""
viewsets.py

This module is responsible for creating a model viewset for adding, editing, deleting, and others.

for more informations: https://www.django-rest-framework.org/api-guide/viewsets/

Class:
    AddressModelViewSet: This class is responsible for creating a new viewset.

Author:
    Pypeu (heronalfo)
"""

from drf_yasg.utils import swagger_auto_schema

from core.viewsets import BaseModelViewSet
from products.permissions import IsOwner
from ..serializers import CostumerModelSerializer
from ..models import Costumer, Address

class AddressModelViewSet(BaseModelViewSet):
    '''
    Viewset for creating, updating and editing the user to obtain their access token
    '''
    serializer_class = CostumerModelSerializer
    queryset = Costumer.objects.all()
    http_method_names = ['patch', 'head', 'options']

    def get_permissions(self):
        '''
        Applies the appropriate permissions to objects, meaning that only
        the account owner can edit or delete their account.
        '''
        if self.action == 'patch':
            return [IsOwner(), ]

        return super().get_permissions()

    @swagger_auto_schema(
        operation_description='Allows you to perform a partial update',
        responses={
            200: 'Your address has been updated successfully',
            400: 'There was an error in the request',
            401: 'Only users can update their own addresses',
            403: 'You are not allowed to change this address',
            404: 'Address not found'
        }
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)
