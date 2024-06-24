from rest_framework.permissions import BasePermission

class IsOwnerOfUser(BasePermission):
    ''' 
    Verification to see if the person making the request is the account owner 
    '''
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username