'''
permissions.py

This module is responsible for creating new specific permissions.

for more informations: https://www.django-rest-framework.org/api-guide/permissions/


Classes:
    IsSeller: Check if user is Seller.
    
    IsOwner: Checks whether the user owns a given object.

Author:
    PyPeu (heronalfo)
'''

from rest_framework.permissions import BasePermission

#disable=too-many-ancestors

class IsSeller(BasePermission):
    '''
    Permission created to check if the user is a seller.
    '''

    def has_object_permission(self, request, view, obj):
        '''
        Checks if the class user is a seller
        '''

        return not request.user.is_anonymous and request.user.is_seller

    def has_permission(self, request, view):
        '''
        Checks if the class user is a seller
        '''

        return not request.user.is_anonymous and request.user.is_seller

class IsOwner(BasePermission):
    '''
    Permission created to check whether the user is the owner of an object
    '''

    def has_object_permission(self, request, view, obj):
        '''
        Checks if the user is the instance creator
        '''

        return obj.costumer == request.user
