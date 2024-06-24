'''
  Documentation Swagger, for the use and application of the API. Addition of licenses and usage rights, for more informations: https://drf-yasg.readthedocs.io/en/stable/readme.html
'''
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='E-commerce API V1',
        default_version = 'v1',
        description='Documentation and guidance for using our API',
        contact=openapi.Contact('j040p3dr0s1lv4s4nt0s@gmail.com'),
        license=openapi.License('Copyright (c) 2024 João Pedro Silva Santos (heronalfo)'),    
    ),
    
    public=True,
    permission_classes = (permissions.AllowAny,  ),

)