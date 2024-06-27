from django.urls import path
from rest_framework.routers import SimpleRouter
from .viewsets import *

app_name = 'products'

router = SimpleRouter()
router.register('api/v1', ProductModelViewSet, basename='products')

urlpatterns = router.urls