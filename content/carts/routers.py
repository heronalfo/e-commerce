'''
routers.py

This model is responsible for defining the URLS.

for more informations: https://www.django-rest-framework.org/api-guide/routers/

Routers:

    Carts:
        http://127.0.0.1:8000/carts/api/v1/
        http://127.0.0.1:8000/carts/api/v1/<pk:int>
        
    Carts Items:
        http://127.0.0.1:8000/carts/items/api/v1/
        http://127.0.0.1:8000/carts/items/api/v1/<pk:int>
        
Author:
    PyPeu (heronalfo)
'''

from django.urls import path
from rest_framework.routers import SimpleRouter
from .viewsets import (CartModelViewSet,  CartItemModelViewSet)

#pylint: disable=invalid-name
app_name = 'carts'

router = SimpleRouter()
router.register('api/v1', CartModelViewSet, basename='carts')
router.register('items/api/v1', CartItemModelViewSet, basename='items')

urlpatterns = [
] + router.urls