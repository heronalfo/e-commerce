'''
routers.py

This model is responsible for defining the URLS.

for more informations: https://www.django-rest-framework.org/api-guide/routers/

Routers:
    http://127.0.0.1:8000/products/api/v1/
    http://127.0.0.1:8000/products/api/v1/<pk:int>
    
    http://127.0.0.1:8000/products/reviews/api/v1/
    http://127.0.0.1:8000/products/reviews/api/v1/<pk:int>
    
    http://127.0.0.1:8000/products/categories/api/v1/
    http://127.0.0.1:8000/products/categories/api/v1/<pk:int>

Author:
    PyPeu (heronalfo)
'''

from rest_framework.routers import SimpleRouter
from .viewsets import (CategoryModelViewSet, ReviewModelViewSet, ProductModelViewSet)

#pylint: disable=invalid-name
app_name = 'products'

router = SimpleRouter()
router.register('categories/api/v1', CategoryModelViewSet, basename='categories')
router.register('reviews/api/v1', ReviewModelViewSet, basename='reviews')
router.register('api/v1', ProductModelViewSet, basename='products')

urlpatterns = router.urls
