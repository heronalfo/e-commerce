'''
routers.py

This model is responsible for defining the URLS.

for more informations: https://www.django-rest-framework.org/api-guide/routers/

Routers:

    Products:
        http://127.0.0.1:8000/products/api/v1/
        http://127.0.0.1:8000/products/api/v1/<pk:int>
        http://127.0.0.1:8000/products/api/v1/search/

    Reviews:
        http://127.0.0.1:8000/products/reviews/api/v1/
        http://127.0.0.1:8000/products/reviews/api/v1/<pk:int>
    
    Category:
        http://127.0.0.1:8000/products/categories/api/v1/
        http://127.0.0.1:8000/products/categories/api/v1/<pk:int>

Author:
    PyPeu (heronalfo)
'''

from django.urls import path
from rest_framework.routers import SimpleRouter
from .viewsets import (CategoryModelViewSet, ReviewModelViewSet,
ProductModelViewSet, TagModelViewSet, SearchView)

#pylint: disable=invalid-name
app_name = 'products'

router = SimpleRouter()
router.register('categories/api/v1', CategoryModelViewSet, basename='categories')
router.register('reviews/api/v1', ReviewModelViewSet, basename='reviews')
router.register('api/v1', ProductModelViewSet, basename='products')
router.register('tags/api/v1', TagModelViewSet, basename='tags')

urlpatterns = [
    path('api/v1/search/', SearchView.as_view(), name='search'),

] + router.urls
