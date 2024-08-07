'''
routers.py

This model is responsible for defining the URLS.

for more informations: https://www.django-rest-framework.org/api-guide/routers/

Routers:
    Orders:
        http://127.0.0.1:8000/orders/api/v1/
        http://127.0.0.1:8000/orders/api/v1/<pk:int>
    
    Orders Items:
        http://127.0.0.1:8000/orders/items/api/v1/
        http://127.0.0.1:8000/orders/items/api/v1/<pk:int>
        
Author:
    PyPeu (heronalfo)
'''

from rest_framework.routers import SimpleRouter
from .viewsets import (OrderModelViewSet, OrderItemModelViewSet, )

#pylint: disable=invalid-name
app_name = 'orders'

router = SimpleRouter()
router.register('items/api/v1', OrderItemModelViewSet, basename='items')
router.register('api/v1', OrderModelViewSet, basename='orders')

urlpatterns = router.urls
