from rest_framework.permissions import BasePermission
import pdb

class IsSeller(BasePermission):
    '''
    Permission created to check if the user is a seller
    
    :permissions: 
     Checks if the class user is a seller
    '''
    def has_object_permission(self, request, view, obj):
        return request.user.is_anonymous != True and request.user.is_seller == True
                
    def has_permission(self, request, view):
        return request.user.is_anonymous != True and request.user and request.user.is_seller == True

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user