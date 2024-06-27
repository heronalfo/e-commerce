from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from .viewsets import UserModelViewSet

app_name = 'accounts'

router = SimpleRouter()
router.register('api/v1', UserModelViewSet, basename=app_name)

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken

urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token'), 
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='refresh'),    
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='verify'),
      
] + router.urls