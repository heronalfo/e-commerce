from django.urls import path
from rest_framework.routers import SimpleRouter
from .viewsets import *

app_name = 'products'

router = SimpleRouter()
router.register('categories/api/v1', CategoryModelViewSet, basename='categories')
router.register('reviews/api/v1', ReviewModelViewSet, basename='reviews')
router.register('api/v1', ProductModelViewSet, basename='products')

urlpatterns = router.urls