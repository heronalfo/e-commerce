'''
permissions.py

This module is responsible for creating new specific permissions.

for more informations: https://www.django-rest-framework.org/api-guide/permissions/


Classes:
    IsSeller: Check if user is Owner of User.
    
Author:
    PyPeu (heronalfo)
'''

from rest_framework.permissions import BasePermission

class IsOwnerOfUser(BasePermission):
    ''' 
    Verification to see if the person making the request is the account owner.
    '''
    def has_object_permission(self, request, view, obj):
        '''
        Checks if the object's username is the client's username 
        '''
        return obj.username is request.user.username
