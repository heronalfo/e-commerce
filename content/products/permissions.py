from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    '''
    Permission created to check if the user is a seller
    
    :permissions: 
     Checks if the class user is a seller
    '''
    def has_object_permission(self, request, view, obj):
        return request.user and request.is_authenticated and request.user.is_seller
        
    def has_permission(self, request, view):
        return request.user and request.is_authenticated and request.user.is_seller