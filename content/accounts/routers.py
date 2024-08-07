'''
routers.py

This model is responsible for defining the URLS.

for more informations: https://www.django-rest-framework.org/api-guide/routers/

Routers:
    Accounts:
        http://127.0.0.1:8000/accounts/api/v1/
        http://127.0.0.1:8000/accounts/api/v1/<pk:int>
    
    Addresses:
        http://127.0.0.1:8000/accounts/addreases/api/v1/
        
    Tokens:
        http://127.0.0.1:8000/accounts/api/v1/token/
        http://127.0.0.1:8000/accounts/api/v1/refresh/
        http://127.0.0.1:8000/accounts/api/v1/verify/
    
Author:
    PyPeu (heronalfo)
'''

from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from .viewsets import (CostumerModelViewSet, AddressModelViewSet)

#pylint: disable=invalid-name
app_name = 'accounts'

router = SimpleRouter()
router.register('api/v1', CostumerModelViewSet, basename=app_name)
router.register('address/api/v1/', AddressModelViewSet, basename='addresses')

urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='verify'),

] + router.urls
