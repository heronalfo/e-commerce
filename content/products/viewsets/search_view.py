"""
search_view.py

This module is responsible for creating functionality for searching for products.

Class:

    ListAPIView:

    Used for read-only endpoints to represent a collection of model instances.
    Provides a get method handler.
    Extends: GenericAPIView, ListModelMixin
    
    SearchView: This class is responsible for product search.

Author:
    Pypeu (heronalfo)
"""

from django.db.models import Q
from rest_framework.generics import ListAPIView
from ..serializers import ProductModelSerializer
from ..models import Product

class SearchView(ListAPIView):
    '''
    View to search for registered products.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def get_queryset(self, *args, **kwargs):
        '''
        Overrides the function to filter the query by product name and description.
        '''
        queryset = super().get_queryset(*args, **kwargs)
        query = self.request['query_params']

        if name:= query.get('name'):
            queryset = queryset.filter(
                Q(name__icontains=name),
                Q(description__icontains=name),

            )

        if category:= query.get('category'):
            queryset = queryset.filter(
                Q(category=category)

            )

        if min_price:= query.get('min_price'):
            queryset = queryset.filter(
                Q(price__gte=min_price)

            )

        return queryset
